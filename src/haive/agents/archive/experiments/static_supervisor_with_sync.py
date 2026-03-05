"""Static supervisor inheriting from ReactAgent with tool node modifications.

This supervisor uses ReactAgent's looping behavior but modifies the tool node
to execute agent handoffs stored in state.
"""

import logging
import pickle
from typing import Any

from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.tools import BaseTool, tool

# from langgraph_supervisor import create_forward_message_tool, create_handoff_tool  # Module doesn't exist
from pydantic import BaseModel, Field, model_validator

from haive.agents.base.agent import Agent
from haive.agents.react.agent import ReactAgent

logger = logging.getLogger(__name__)


class AgentEntry(BaseModel):
    """Represents a registered agent in the supervisor state."""

    name: str
    description: str
    agent_instance: bytes
    agent_class: str

    @classmethod
    def from_agent(cls, name: str, description: str, agent: Agent) -> "AgentEntry":
        """Create an AgentEntry from an agent instance."""
        return cls(
            name=name,
            description=description,
            agent_instance=pickle.dumps(agent),
            agent_class=agent.__class__.__name__,
        )

    def get_agent(self) -> Agent:
        """Deserialize and return the agent instance."""
        return pickle.loads(self.agent_instance)


class SupervisorReactState(StateSchema):
    """State schema for ReactAgent-based supervisor with agent registry."""

    messages: list[Any] = Field(default_factory=list)
    registered_agents: dict[str, AgentEntry] = Field(
        default_factory=dict,
        description="Registered agents stored as serialized entries",
    )
    handoff_tools: dict[str, BaseTool] = Field(
        default_factory=dict, description="Handoff tools mapped to agent names"
    )
    current_agent: str | None = Field(None, description="Currently active agent")
    last_handoff_result: Any | None = Field(
        None, description="Result from last handoff"
    )

    @model_validator(mode="after")
    def sync_tools_with_agents(self) -> "SupervisorReactState":
        """Ensure handoff tools are synchronized with registered agents.

        This validator runs after field assignment to ensure tools
        always match the registered agents.
        """
        for agent_name, agent_entry in self.registered_agents.items():
            if agent_name not in self.handoff_tools:
                tool = create_handoff_tool(
                    agent_name=agent_name, description=agent_entry.description
                )
                self.handoff_tools[agent_name] = tool
                logger.info(f"Created handoff tool for agent: {agent_name}")
        tools_to_remove = []
        for tool_name in self.handoff_tools:
            if tool_name not in self.registered_agents:
                tools_to_remove.append(tool_name)
        for tool_name in tools_to_remove:
            del self.handoff_tools[tool_name]
            logger.info(f"Removed handoff tool for unregistered agent: {tool_name}")
        return self


class StaticSupervisor(ReactAgent):
    """Supervisor that inherits ReactAgent behavior with modified tool node.

    This supervisor uses ReactAgent's looping behavior but overrides the tool
    node to execute agent handoffs from state instead of regular tools.
    """

    def __init__(self, **kwargs) -> None:
        """Initialize supervisor with custom state schema."""
        kwargs["state_schema"] = SupervisorReactState
        super().__init__(**kwargs)

    def setup_agent(self) -> None:
        """Setup the supervisor with dynamic tools."""
        super().setup_agent()
        self._update_engine_tools()

    def _update_engine_tools(self) -> None:
        """Update the engine's tools based on registered agents."""
        if not self.main_engine:
            return
        state = (
            self.get_state() if hasattr(self, "get_state") else SupervisorReactState()
        )
        tools = []
        tools.extend(state.handoff_tools.values())
        tools.append(create_forward_message_tool())
        tools.append(self._create_list_agents_tool())
        if hasattr(self.main_engine, "tools"):
            self.main_engine.tools = tools
        elif hasattr(self.main_engine, "config") and hasattr(
            self.main_engine.config, "tools"
        ):
            self.main_engine.config.tools = tools

    def _create_list_agents_tool(self) -> BaseTool:
        """Create tool for listing available agents."""

        @tool
        def list_agents() -> str:
            """List all available agents and their capabilities."""
            state = (
                self.get_state()
                if hasattr(self, "get_state")
                else SupervisorReactState()
            )
            agents = state.registered_agents
            if not agents:
                return "No agents registered."
            agent_list = []
            for name, entry in agents.items():
                agent_list.append(f"- {name}: {entry.description}")
            return "Available agents:\n" + "\n".join(agent_list)

        return list_agents

    def register_agent(self, name: str, description: str, agent: Agent) -> None:
        """Register an agent with the supervisor.

        This updates the state and triggers tool synchronization.
        """
        entry = AgentEntry.from_agent(name, description, agent)
        current_state = (
            self.get_state() if hasattr(self, "get_state") else SupervisorReactState()
        )
        current_state.registered_agents[name] = entry
        if hasattr(self, "update_state"):
            self.update_state(current_state)
        self._update_engine_tools()
        logger.info(f"Registered agent '{name}' with supervisor")

    def build_graph(self) -> BaseGraph:
        """Build graph using ReactAgent pattern with custom tool execution."""
        graph = super().build_graph()
        if "tool_node" in graph.nodes:
            graph.remove_node("tool_node")
            graph.add_node("tool_node", self._execute_tool_or_agent)
        return graph

    def _execute_tool_or_agent(self, state: SupervisorReactState) -> dict[str, Any]:
        """Execute tools or agent handoffs based on the tool call.

        This replaces the standard tool node behavior to handle agent handoffs
        from state instead of just executing tools.
        """
        messages = state.messages
        if not messages:
            return {"messages": []}
        last_message = messages[-1]
        if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
            return {"messages": []}
        tool_messages = []
        for tool_call in last_message.tool_calls:
            tool_name = tool_call.get("name", "")
            tool_id = tool_call.get("id", "")
            if tool_name in state.registered_agents:
                result = self._execute_agent_handoff(state, tool_name, tool_call)
                tool_messages.append(
                    ToolMessage(content=result, tool_call_id=tool_id, name=tool_name)
                )
            else:
                result = self._execute_regular_tool(state, tool_name, tool_call)
                tool_messages.append(
                    ToolMessage(content=result, tool_call_id=tool_id, name=tool_name)
                )
        return {"messages": tool_messages}

    def _execute_agent_handoff(
        self, state: SupervisorReactState, agent_name: str, tool_call: dict
    ) -> str:
        """Execute handoff to a specific agent from state."""
        try:
            agent_entry = state.registered_agents[agent_name]
            agent = agent_entry.get_agent()
            task = tool_call.get("args", {}).get("task", "")
            logger.info(f"Executing handoff to {agent_name} with task: {task}")
            result = agent.invoke({"messages": [HumanMessage(content=task)]})
            if isinstance(result, dict) and "messages" in result:
                response = result["messages"][-1].content
            else:
                response = str(result)
            state.current_agent = agent_name
            state.last_handoff_result = result
            return f"Result from {agent_name}: {response}"
        except Exception as e:
            error_msg = f"Error executing agent {agent_name}: {e!s}"
            logger.exception(error_msg)
            return error_msg

    def _execute_regular_tool(
        self, state: SupervisorReactState, tool_name: str, tool_call: dict
    ) -> str:
        """Execute regular supervisor tools."""
        try:
            {t.name: t for t in self._update_engine_tools() or []}
            if tool_name == "list_agents":
                tool = self._create_list_agents_tool()
                return tool.invoke({})
            if tool_name == "forward_message":
                message = tool_call.get("args", {}).get("message", "")
                return f"Message forwarded: {message}"
            return f"Unknown tool: {tool_name}"
        except Exception as e:
            return f"Error executing tool {tool_name}: {e!s}"


if __name__ == "__main__":
    pass
