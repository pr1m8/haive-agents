"""Proper list multi-agent that uses MultiAgentState and AgentNodeV3.

from typing import Any
This implementation properly leverages the existing infrastructure:
- MultiAgentState for proper state management
- AgentNodeV3 for agent execution with state projection
- create_agent_node_v3 for creating agent nodes
- Proper engine syncing and recompilation tracking
"""

import logging
from collections.abc import Callable, Iterator, Sequence
from typing import Any, Union

from haive.core.common.mixins.recompile_mixin import RecompileMixin
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langgraph.graph import END, START
from pydantic import Field, PrivateAttr, create_model

from haive.agents.base.agent import Agent

logger = logging.getLogger(__name__)


class ProperListMultiAgent(Agent, RecompileMixin, Sequence[Agent]):
    """List-based multi-agent that properly uses MultiAgentState and AgentNodeV3.

    This implementation:
    - Uses MultiAgentState as the state schema
    - Uses AgentNodeV3 for proper agent execution
    - Handles state projection and hierarchical management
    - Supports recompilation tracking
    - Maintains the natural list interface

    Example:
        .. code-block:: python

            multi = ProperListMultiAgent("research_team")
            multi.append(PlannerAgent("planner"))
            multi.append(ResearchAgent("researcher"))
            multi.append(WriterAgent("writer"))

            # Agents are stored in MultiAgentState.agents
            # Each agent gets its own state in MultiAgentState.agent_states
            # Output tracked in MultiAgentState.agent_outputs

            result = multi.invoke({"messages": [HumanMessage("Research AI")]})

    """

    # Core agent list
    agents: list[Agent] = Field(default_factory=list)

    # Execution settings
    sequential: bool = Field(default=True, description="Execute agents sequentially")
    stop_on_error: bool = Field(
        default=False, description="Stop execution on agent error"
    )

    # Routing rules for conditional execution
    routing_rules: dict[str, dict[str, Any]] = Field(
        default_factory=dict, description="Conditional routing rules by agent name"
    )

    # State settings
    use_prebuilt_base: bool = Field(
        default=True, description="Use MultiAgentState as base"
    )

    # Private tracking
    _agent_index: dict[str, int] = PrivateAttr(default_factory=dict)

    def model_post_init(self, __context) -> None:
        """Initialize after model creation."""
        super().model_post_init(__context)
        self._update_agent_index()

    # ========== List Interface ==========

    def __getitem__(self, index: int | slice) -> Agent | list[Agent]:
        return self.agents[index]

    def __len__(self) -> int:
        return len(self.agents)

    def __iter__(self) -> Iterator[Agent]:
        return iter(self.agents)

    def append(self, agent: Agent) -> "ProperListMultiAgent":
        """Add agent to the list."""
        self.agents.append(agent)
        self._update_agent_index()
        self.mark_for_recompile(f"Added agent: {agent.name}")
        return self

    def insert(self, index: int, agent: Agent) -> "ProperListMultiAgent":
        """Insert agent at position."""
        self.agents.insert(index, agent)
        self._update_agent_index()
        self.mark_for_recompile(f"Inserted agent: {agent.name} at {index}")
        return self

    def remove(self, agent: Agent | str) -> "ProperListMultiAgent":
        """Remove agent."""
        if isinstance(agent, str):
            for i, a in enumerate(self.agents):
                if a.name == agent:
                    self.agents.pop(i)
                    break
        else:
            self.agents.remove(agent)

        self._update_agent_index()
        self.mark_for_recompile(
            f"Removed agent: {agent if isinstance(agent, str) else agent.name}"
        )
        return self

    def pop(self, index: int = -1) -> Agent:
        """Remove and return agent."""
        agent = self.agents.pop(index)
        self._update_agent_index()
        self.mark_for_recompile(f"Popped agent: {agent.name}")
        return agent

    # ========== Builder Interface ==========

    def then(self, agent: Agent) -> "ProperListMultiAgent":
        """Add next agent in sequence."""
        return self.append(agent)

    def when(
        self,
        condition: Callable[[Any], str | bool],
        routes: dict[str | bool, Union[str, Agent, "END"]]) -> "ProperListMultiAgent":
        """Add conditional routing for the last agent."""
        if not self.agents:
            raise ValueError("No agents to route from")

        last_agent = self.agents[-1]

        # Convert agent references to names
        route_map = {}
        for key, dest in routes.items():
            if isinstance(dest, Agent):
                if dest not in self.agents:
                    self.append(dest)
                route_map[key] = dest.name
            else:
                route_map[key] = dest

        self.routing_rules[last_agent.name] = {
            "condition": condition,
            "routes": route_map,
            "default": END,
        }

        self.sequential = False  # Switch to conditional mode
        self.mark_for_recompile(f"Added routing for {last_agent.name}")
        return self

    # ========== State Schema Setup ==========

    def _setup_schemas(self) -> None:
        """Setup using MultiAgentState as the base schema."""
        # Create MultiAgentState with our agents
        self.state_schema = MultiAgentState

        # Input schema - just messages by default

        self.input_schema = create_model(
            f"{self.name}Input",
            messages=(list[BaseMessage], Field(default_factory=list)))

        # Output schema - messages plus agent outputs
        self.output_schema = create_model(
            f"{self.name}Output",
            messages=(list[BaseMessage], Field(default_factory=list)),
            agent_outputs=(dict[str, Any], Field(default_factory=dict)))

    # ========== Agent Setup ==========

    def setup_agent(self) -> None:
        """Setup the multi-agent system."""
        self._update_agent_index()

        # Set schema to use MultiAgentState
        self.use_prebuilt_base = True
        self.state_schema = MultiAgentState

    def _update_agent_index(self) -> None:
        """Update agent name to index mapping."""
        self._agent_index = {agent.name: i for i, agent in enumerate(self.agents)}

    # ========== Graph Building ==========

    def build_graph(self) -> BaseGraph:
        """Build graph using AgentNodeV3 for proper state handling."""
        # Use MultiAgentState as schema
        graph = BaseGraph(state_schema=MultiAgentState)

        if not self.agents:
            # Empty graph just passes through
            graph.add_node("passthrough", self._passthrough_node)
            graph.add_edge(START, "passthrough")
            graph.add_edge("passthrough", END)
            return graph.compile()

        # Add initialization node to setup state
        graph.add_node("init_multi_agent", self._init_multi_agent_state)
        graph.add_edge(START, "init_multi_agent")

        # Build execution graph
        if self.sequential and not self.routing_rules:
            self._build_sequential_graph(graph)
        else:
            self._build_conditional_graph(graph)

        return graph.compile()

    def _build_sequential_graph(self, graph: BaseGraph) -> None:
        """Build sequential execution using AgentNodeV3."""
        prev_node = "init_multi_agent"

        for i, agent in enumerate(self.agents):
            # Use AgentNodeV3 for proper state projection
            node_config = create_agent_node_v3(
                agent_name=agent.name,
                agent=agent,
                name=f"agent_{agent.name}_{i}",
                extract_from_container=True,
                project_state=True,
                update_container_state=True,
                track_recompilation=True)

            node_name = f"agent_{agent.name}_{i}"
            graph.add_node(node_name, node_config)
            graph.add_edge(prev_node, node_name)
            prev_node = node_name

        graph.add_edge(prev_node, END)

    def _build_conditional_graph(self, graph: BaseGraph) -> None:
        """Build graph with conditional routing."""
        # Add all agent nodes using AgentNodeV3
        for i, agent in enumerate(self.agents):
            node_config = create_agent_node_v3(
                agent_name=agent.name,
                agent=agent,
                name=f"agent_{agent.name}_{i}",
                extract_from_container=True,
                project_state=True,
                update_container_state=True,
                track_recompilation=True)

            node_name = f"agent_{agent.name}_{i}"
            graph.add_node(node_name, node_config)

        # Add routing logic
        prev_node = "init_multi_agent"

        for i, agent in enumerate(self.agents):
            node_name = f"agent_{agent.name}_{i}"

            # Connect from previous if no explicit routing
            if prev_node and agent.name not in self.routing_rules:
                graph.add_edge(prev_node, node_name)

            # Add conditional routing if defined
            if agent.name in self.routing_rules:
                rule = self.routing_rules[agent.name]
                condition = rule["condition"]
                routes = rule["routes"]
                default = rule.get("default", END)

                # Map agent names to node names
                node_routes = {}
                for key, dest in routes.items():
                    if dest in self._agent_index:
                        dest_index = self._agent_index[dest]
                        node_routes[key] = f"agent_{dest}_{dest_index}"
                    else:
                        node_routes[key] = dest

                # Add conditional edges
                graph.add_conditional_edges(
                    source_node=node_name,
                    condition=condition,
                    destinations=node_routes,
                    default=default)

                prev_node = None  # No automatic progression
            else:
                prev_node = node_name

        # Connect last non-routing node to END
        if prev_node:
            graph.add_edge(prev_node, END)

        # Ensure first agent is connected
        if self.agents:
            first_node = f"agent_{self.agents[0].name}_0"
            graph.add_edge("init_multi_agent", first_node)

    # ========== Node Functions ==========

    def _passthrough_node(self, state: dict[str, Any]) -> dict[str, Any]:
        """Passthrough for empty multi-agent."""
        return state

    def _init_multi_agent_state(self, state: dict[str, Any]) -> dict[str, Any]:
        """Initialize MultiAgentState with our agents."""
        # Create agent dict from our list
        agents_dict = {agent.name: agent for agent in self.agents}

        # Create proper MultiAgentState
        multi_state = MultiAgentState(
            agents=agents_dict,
            messages=state.get("messages", []),
            agent_execution_order=[agent.name for agent in self.agents])

        # Return the state as dict for LangGraph
        return multi_state.model_dump()

    # ========== Utility Methods ==========

    def get_agent_by_name(self, name: str) -> Agent | None:
        """Get agent by name."""
        index = self._agent_index.get(name)
        return self.agents[index] if index is not None else None

    def get_agent_names(self) -> list[str]:
        """Get ordered list of agent names."""
        return [agent.name for agent in self.agents]

    def get_execution_summary(self) -> dict[str, Any]:
        """Get execution summary."""
        return {
            "name": self.name,
            "agent_count": len(self.agents),
            "agents": self.get_agent_names(),
            "sequential": self.sequential,
            "routing_rules": len(self.routing_rules),
            "recompile_count": self.recompile_count,
            "needs_recompile": self.needs_recompile,
        }

    # ========== String Representation ==========

    def __str__(self) -> str:
        agent_names = ", ".join(agent.name for agent in self.agents)
        return f"ProperListMultiAgent([{agent_names}])"

    def __repr__(self) -> str:
        return (
            f"ProperListMultiAgent(name='{self.name}', "
            f"agents={len(self.agents)}, "
            f"sequential={self.sequential}, "
            f"routing_rules={len(self.routing_rules)})"
        )


class MetaListMultiAgent(Agent, RecompileMixin, Sequence[Agent]):
    """List multi-agent that uses MetaStateSchema for single agent embedding.

    This is useful when you want to embed a sequence of agents as a single
    unit within another agent's state using the MetaStateSchema pattern.

    Example:
        .. code-block:: python

            # Create a meta multi-agent
            meta = MetaListMultiAgent("research_pipeline")
            meta.append(PlannerAgent())
            meta.append(ResearchAgent())
            meta.append(WriterAgent())

            # This can be embedded in another agent's state
            parent_state = MetaStateSchema(agent=meta)

    """

    # Core agent list
    agents: list[Agent] = Field(default_factory=list)

    # Current agent index for execution
    current_index: int = Field(default=0, description="Current agent being executed")

    # Results from each agent
    agent_results: list[dict[str, Any]] = Field(
        default_factory=list, description="Results from each agent execution"
    )

    # Private tracking
    _agent_index: dict[str, int] = PrivateAttr(default_factory=dict)

    # ========== List Interface ==========

    def __getitem__(self, index: int | slice) -> Agent | list[Agent]:
        return self.agents[index]

    def __len__(self) -> int:
        return len(self.agents)

    def __iter__(self) -> Iterator[Agent]:
        return iter(self.agents)

    def append(self, agent: Agent) -> "MetaListMultiAgent":
        """Add agent to the list."""
        self.agents.append(agent)
        self._update_agent_index()
        self.mark_for_recompile(f"Added agent: {agent.name}")
        return self

    # ========== State Schema Setup ==========

    def _setup_schemas(self) -> None:
        """Setup using MetaStateSchema as the base."""
        self.state_schema = MetaStateSchema

        # Input and output schemas

        self.input_schema = create_model(
            f"{self.name}Input",
            messages=(list[BaseMessage], Field(default_factory=list)))

        self.output_schema = create_model(
            f"{self.name}Output",
            messages=(list[BaseMessage], Field(default_factory=list)),
            agent_results=(list[dict[str, Any]], Field(default_factory=list)))

    def setup_agent(self) -> None:
        """Setup the meta multi-agent."""
        self._update_agent_index()
        self.state_schema = MetaStateSchema

    def _update_agent_index(self) -> None:
        """Update agent name to index mapping."""
        self._agent_index = {agent.name: i for i, agent in enumerate(self.agents)}

    # ========== Graph Building ==========

    def build_graph(self) -> BaseGraph:
        """Build graph that executes agents sequentially."""
        graph = BaseGraph(state_schema=MetaStateSchema)

        if not self.agents:
            graph.add_node("passthrough", lambda x: x)
            graph.add_edge(START, "passthrough")
            graph.add_edge("passthrough", END)
            return graph.compile()

        # Sequential execution through all agents
        prev_node = START

        for i, agent in enumerate(self.agents):
            node_name = f"meta_agent_{i}"

            # Create node that executes this specific agent
            def make_meta_agent_node(agent_instance: Any, agent_index: Any):
                def meta_node(state: dict[str, Any]) -> dict[str, Any]:
                    # Get messages from state
                    messages = state.get("messages", [])

                    # Execute this agent
                    result = agent_instance.invoke({"messages": messages})

                    # Update state
                    output = {
                        "messages": result.get("messages", messages),
                        "agent_results": [*state.get("agent_results", []), result],
                        "current_index": agent_index + 1,
                    }

                    return output

                return meta_node

            graph.add_node(node_name, make_meta_agent_node(agent, i))
            graph.add_edge(prev_node, node_name)
            prev_node = node_name

        graph.add_edge(prev_node, END)

        return graph.compile()


# ========== Convenience Functions ==========


def sequential_multi(
    *agents: Agent, name: str = "sequential_multi"
) -> ProperListMultiAgent:
    """Create a sequential multi-agent."""
    multi = ProperListMultiAgent(name=name)
    for agent in agents:
        multi.append(agent)
    return multi


def meta_multi(*agents: Agent, name: str = "meta_multi") -> MetaListMultiAgent:
    """Create a meta multi-agent."""
    multi = MetaListMultiAgent(name=name)
    for agent in agents:
        multi.append(agent)
    return multi
