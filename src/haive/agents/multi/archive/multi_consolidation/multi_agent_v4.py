"""MultiAgent V4 - Clean implementation using enhanced base agent.

This implementation follows the V4 pattern with:
- Enhanced base agent integration
- MultiAgentState usage
- AgentNodeV3 execution
- Simple list initialization
- Incremental build-up approach

Start small, test incrementally, build up features.
"""

from __future__ import annotations

import logging
from typing import Any, Literal

from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph
from pydantic import Field, model_validator

from haive.agents.base.agent import Agent

logger = logging.getLogger(__name__)


class MultiAgentV4(Agent):
    """V4 Multi-agent coordinator using enhanced base agent.

    Simple, clean implementation that starts small and builds incrementally.
    Uses MultiAgentState and AgentNodeV3 for proper integration.

    Example:
        >>> from haive.agents.simple.agent import SimpleAgent
        >>> from haive.agents.react.agent import ReactAgent
        >>>
        >>> # Create agents
        >>> planner = ReactAgent(name="planner", engine=config, tools=[...])
        >>> writer = SimpleAgent(name="writer", engine=config)
        >>>
        >>> # Create multi-agent (simple list initialization)
        >>> workflow = MultiAgentV4(
        ...     name="content_workflow",
        ...     agents=[planner, writer],
        ...     execution_mode="sequential"
        ... )
        >>>
        >>> # Execute
        >>> result = await workflow.arun({"task": "Write an article"})
    """

    agents: list[Agent] = Field(
        default_factory=list,
        description="List of agents to coordinate (converted to dict internally)",
    )
    execution_mode: Literal["sequential", "parallel"] = Field(
        default="sequential", description="How to execute the agents"
    )
    build_mode: Literal["auto", "manual", "lazy"] = Field(
        default="auto", description="When to build the execution graph"
    )
    agent_dict: dict[str, Agent] = Field(
        default_factory=dict,
        description="Internal agent dictionary (converted from list)",
    )
    execution_graph: CompiledGraph | None = Field(
        default=None, description="Compiled LangGraph for execution"
    )
    state_schema: type[MultiAgentState] = Field(
        default=MultiAgentState, description="State schema to use"
    )

    @model_validator(mode="after")
    def setup_multi_agent(self):
        """Set up multi-agent system after initialization."""
        if self.agents:
            self.agent_dict = self._convert_agents_to_dict(self.agents)
            logger.info(
                f"Converted {len(self.agents)} agents to dict: {list(self.agent_dict.keys())}"
            )
        if self.build_mode == "auto":
            self._build_execution_graph()
        return self

    def _convert_agents_to_dict(self, agents: list[Agent]) -> dict[str, Agent]:
        """Convert agent list to dictionary keyed by name."""
        agent_dict = {}
        for i, agent in enumerate(agents):
            if not hasattr(agent, "name") or not agent.name:
                raise ValueError(f"Agent at index {i} must have a name: {agent}")
            if agent.name in agent_dict:
                raise ValueError(f"Duplicate agent name: {agent.name}")
            agent_dict[agent.name] = agent
        return agent_dict

    def _build_execution_graph(self) -> CompiledGraph:
        """Build LangGraph for agent execution."""
        if not self.agent_dict:
            raise ValueError("No agents to build graph with")
        logger.info(
            f"Building {self.execution_mode} execution graph for {len(self.agent_dict)} agents"
        )
        graph = StateGraph(self.state_schema)
        for agent_name, _agent in self.agent_dict.items():
            node_func = create_agent_node_v3(agent_name)
            graph.add_node(agent_name, node_func)
            logger.debug(f"Added node for agent: {agent_name}")
        if self.execution_mode == "sequential":
            self._add_sequential_edges(graph)
        elif self.execution_mode == "parallel":
            self._add_parallel_edges(graph)
        self.execution_graph = graph.compile()
        logger.info("Successfully compiled execution graph")
        return self.execution_graph

    def _add_sequential_edges(self, graph: StateGraph):
        """Add sequential edges: START -> agent1 -> agent2 -> ... -> END."""
        agent_names = list(self.agent_dict.keys())
        if not agent_names:
            return
        graph.add_edge(START, agent_names[0])
        for i in range(len(agent_names) - 1):
            current = agent_names[i]
            next_agent = agent_names[i + 1]
            graph.add_edge(current, next_agent)
            logger.debug(f"Added edge: {current} -> {next_agent}")
        graph.add_edge(agent_names[-1], END)
        logger.info(f"Added sequential edges for {len(agent_names)} agents")

    def _add_parallel_edges(self, graph: StateGraph):
        """Add parallel edges: START -> all agents -> END."""
        agent_names = list(self.agent_dict.keys())
        for agent_name in agent_names:
            graph.add_edge(START, agent_name)
            graph.add_edge(agent_name, END)
        logger.info(f"Added parallel edges for {len(agent_names)} agents")

    async def arun(self, input_data: Any, **kwargs) -> Any:
        """Execute the multi-agent workflow."""
        if not self.execution_graph:
            if self.build_mode == "manual":
                raise RuntimeError(
                    "Graph not built. Call build() first or use auto build mode."
                )
            self._build_execution_graph()
        initial_state = self._create_initial_state(input_data)
        logger.info(
            f"Executing {self.execution_mode} workflow with {len(self.agent_dict)} agents"
        )
        logger.debug(f"Initial state keys: {list(initial_state.__dict__.keys())}")
        try:
            final_state = await self.execution_graph.ainvoke(initial_state)
            logger.info("Workflow execution completed successfully")
            return self._extract_result(final_state)
        except Exception as e:
            logger.exception(f"Workflow execution failed: {e}")
            raise

    def _create_initial_state(self, input_data: Any) -> MultiAgentState:
        """Create initial MultiAgentState from input."""
        agents_for_state = self.agent_dict
        state_data = (
            input_data.copy() if isinstance(input_data, dict) else {"input": input_data}
        )
        state_data["agents"] = agents_for_state
        initial_state = self.state_schema(**state_data)
        logger.debug(f"Created initial state with {initial_state.agent_count} agents")
        return initial_state

    def _extract_result(self, final_state: MultiAgentState) -> Any:
        """Extract final result from state."""
        if (
            hasattr(final_state, "final_result")
            and final_state.final_result is not None
        ):
            return final_state.final_result
        if final_state.agent_outputs:
            return final_state.agent_outputs
        return final_state

    def build(self) -> CompiledGraph:
        """Manually build the execution graph."""
        return self._build_execution_graph()

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the workflow."""
        if not agent.name:
            raise ValueError("Agent must have a name")
        if agent.name in self.agent_dict:
            raise ValueError(f"Agent with name '{agent.name}' already exists")
        self.agent_dict[agent.name] = agent
        self.agents.append(agent)
        if self.build_mode == "auto" and self.execution_graph:
            self._build_execution_graph()
        logger.info(f"Added agent: {agent.name}")

    def get_agent_names(self) -> list[str]:
        """Get list of agent names."""
        return list(self.agent_dict.keys())

    def get_agent(self, name: str) -> Agent | None:
        """Get agent by name."""
        return self.agent_dict.get(name)

    def display_workflow_info(self) -> None:
        """Display workflow information."""
        for _i, (_name, agent) in enumerate(self.agent_dict.items(), 1):
            type(agent).__name__
