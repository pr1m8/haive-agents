"""Dynamic Supervisor Agent - routes tasks to sub-agents via tool calls.

The supervisor extends ReactAgent. Each sub-agent becomes a handoff tool.
The LLM decides which agent to call by making tool calls. Adding or removing
agents triggers graph recompilation so the LLM always sees current tools.

Example::

    supervisor = DynamicSupervisor(name="boss", engine=AugLLMConfig())
    supervisor.add_agent(math_agent, "Solves math problems")
    supervisor.add_agent(writer_agent, "Writes creative content")
    result = supervisor.run("What is 42 * 17?")  # routes to math_agent
"""

import logging
from typing import Any

from langchain_core.messages import HumanMessage
from langchain_core.tools import StructuredTool
from pydantic import Field, PrivateAttr

from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

logger = logging.getLogger(__name__)

_DEFAULT_SUPERVISOR_PROMPT = """You are a supervisor that delegates tasks to specialized agents.

Available agents:
{agent_list}

For each user request:
1. Decide which agent is best suited for the task
2. Use the handoff_to_[agent_name] tool to delegate
3. Return the agent's response to the user

If no agent is suitable, answer directly with your own knowledge.
Always delegate when a specialized agent is available."""


class DynamicSupervisor(ReactAgent):
    """Supervisor that routes tasks to sub-agents via tool calls.

    Agents are added at runtime with add_agent(). Each becomes a
    handoff_to_{name} tool. The ReactAgent loop handles routing -
    the LLM makes tool calls to delegate work.
    """

    _agent_registry: dict[str, dict[str, Any]] = PrivateAttr(default_factory=dict)
    _base_system_message: str = PrivateAttr(default="")

    def model_post_init(self, __context: Any) -> None:
        """Store base system message before super init."""
        self._base_system_message = self.engine.system_message or ""
        super().model_post_init(__context)

    def compile(self, **kwargs) -> Any:
        """Compile using the LangGraph path (not SimpleAgent's create_runnable).

        SimpleAgent.compile() uses create_runnable() which doesn't rebuild
        properly after tool changes. We go through BaseGraph.to_langgraph()
        instead.
        """
        if not self._is_compiled or kwargs:
            if not hasattr(self, "graph") or self.graph is None:
                self._graph_built = False
                self._build_initial_graph()
            if not self.graph:
                raise RuntimeError("No graph to compile")
            if hasattr(self.graph, "to_langgraph"):
                lg_graph = self.graph.to_langgraph(state_schema=self.state_schema)
            else:
                lg_graph = self.graph
            self._app = lg_graph.compile(
                checkpointer=self.checkpointer, store=self.store, **kwargs
            )
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    def add_agent(
        self,
        agent: Any,
        description: str | None = None,
        name: str | None = None,
    ) -> None:
        """Add a sub-agent. Creates a handoff tool and recompiles the graph.

        Args:
            agent: The agent to add (must have .run() or .arun())
            description: What this agent does (shown to LLM)
            name: Override agent name (defaults to agent.name)
        """
        agent_name = name or getattr(agent, "name", f"agent_{len(self._agent_registry)}")
        desc = description or f"{agent_name} specialist"

        self._agent_registry[agent_name] = {
            "agent": agent,
            "description": desc,
        }

        # Create handoff tool
        handoff = self._make_handoff_tool(agent_name, agent, desc)

        # Add to tools
        if self.tools is None:
            self.tools = []
        self.tools.append(handoff)

        # Update system prompt with agent list
        self._update_prompt()

        # Recompile graph so the new tool is available
        self._is_compiled = False
        self._graph_built = False
        self.graph = None
        self.compile()

        logger.info(f"Added agent '{agent_name}': {desc}")

    def remove_agent(self, name: str) -> None:
        """Remove a sub-agent and its handoff tool."""
        if name not in self._agent_registry:
            return

        del self._agent_registry[name]
        tool_name = f"handoff_to_{name}"
        self.tools = [t for t in (self.tools or []) if getattr(t, "name", "") != tool_name]

        self._update_prompt()
        self._is_compiled = False
        self._graph_built = False
        self.graph = None
        self.compile()

        logger.info(f"Removed agent '{name}'")

    def create_agent(
        self,
        name: str,
        system_message: str,
        description: str,
        tools: list | None = None,
        temperature: float = 0.7,
    ) -> Any:
        """Create a new agent on the fly and add it to the supervisor.

        Args:
            name: Agent name
            system_message: System prompt for the new agent
            description: What this agent does
            tools: Optional tools for the new agent
            temperature: LLM temperature

        Returns:
            The created agent
        """
        from haive.agents.simple.agent import SimpleAgent

        engine = AugLLMConfig(temperature=temperature, system_message=system_message)

        if tools:
            from haive.agents.react.agent import ReactAgent as RA
            agent = RA(name=name, engine=engine, tools=tools)
        else:
            agent = SimpleAgent(name=name, engine=engine)

        self.add_agent(agent, description=description)
        return agent

    @property
    def agents(self) -> dict[str, Any]:
        """Get the current agent registry."""
        return {k: v["agent"] for k, v in self._agent_registry.items()}

    def _make_handoff_tool(self, agent_name: str, agent: Any, description: str) -> StructuredTool:
        """Create a handoff tool that executes the sub-agent."""

        def handoff(task: str) -> str:
            """Delegate task to the agent."""
            try:
                result = agent.run(task, debug=False)

                # Extract string response
                if hasattr(result, "messages") and result.messages:
                    return result.messages[-1].content
                if isinstance(result, dict) and "messages" in result:
                    msgs = result["messages"]
                    if msgs:
                        last = msgs[-1]
                        return last.content if hasattr(last, "content") else str(last)
                if isinstance(result, str):
                    return result
                return str(result)[:500]
            except Exception as e:
                return f"Error from {agent_name}: {e}"

        return StructuredTool.from_function(
            func=handoff,
            name=f"handoff_to_{agent_name}",
            description=f"Delegate task to {agent_name}: {description}",
        )

    def _update_prompt(self) -> None:
        """Update system prompt with current agent list."""
        if not self._agent_registry:
            agent_list = "(No agents registered yet - answer directly)"
        else:
            agent_list = "\n".join(
                f"- {name}: {info['description']}"
                for name, info in self._agent_registry.items()
            )

        base = self._base_system_message or ""
        full_prompt = _DEFAULT_SUPERVISOR_PROMPT.format(agent_list=agent_list)
        if base:
            full_prompt = f"{base}\n\n{full_prompt}"

        self.engine.system_message = full_prompt
