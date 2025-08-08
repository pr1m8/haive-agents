"""Configurable Multi-Agent Base for flexible agent orchestration.

This module provides a general multi-agent base where you can:
- Pass agents
- Define branches/routing between agents
- Override state schema
- Configure schema composition methods
"""

import logging
from collections.abc import Callable
from typing import Any

from haive.core.graph.node.agent_node import AgentNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.agent_schema_composer import AgentSchemaComposer, BuildMode
from haive.core.schema.state_schema import StateSchema
from langgraph.graph import END, START
from pydantic import Field, PrivateAttr, model_validator

from haive.agents.base.agent import Agent

logger = logging.getLogger(__name__)


class AgentBranch:
    """Represents a branch/routing between agents."""

    def __init__(
        self,
        from_agent: str | Agent,
        condition: Callable[[Any], str],
        destinations: dict[str, str | Agent],
        default: str | Agent | None = None,
    ):
        """Initialize agent branch.

        Args:
            from_agent: Source agent (name or Agent object)
            condition: Function that returns routing key based on state
            destinations: Mapping of condition results to target agents
            default: Default destination if condition doesn't match
        """
        self.from_agent = from_agent
        self.condition = condition
        self.destinations = destinations
        self.default = default


class WorkflowStep:
    """Represents a workflow step between agents."""

    def __init__(
        self,
        name: str,
        function: Callable,
        inputs: list[str | Agent] | None = None,
        outputs: list[str | Agent] | None = None,
    ):
        """Initialize workflow step.

        Args:
            name: Name of the workflow step
            function: Function to execute
            inputs: Agents/nodes that feed into this step
            outputs: Agents/nodes this step feeds into
        """
        self.name = name
        self.function = function
        self.inputs = inputs or []
        self.outputs = outputs or []


class ConfigurableMultiAgent(Agent):
    """Configurable multi-agent base that accepts agents and routing configuration.

    This base class allows you to:
    - Pass a list of agents
    - Define branches/routing between agents
    - Add workflow steps between agents
    - Override state schema or use composition
    - Configure schema composition methods
    """

    agents: list[Agent] = Field(description="List of agents to orchestrate")
    branches: list[AgentBranch] = Field(
        default_factory=list, description="Branches/routing between agents"
    )
    workflow_steps: list[WorkflowStep] = Field(
        default_factory=list, description="Workflow steps between agents"
    )
    state_schema_override: type[StateSchema] | None = Field(
        default=None, description="Optional state schema override"
    )
    schema_composition_method: str = Field(
        default="smart", description="Schema composition strategy"
    )
    include_meta: bool = Field(
        default=True, description="Include meta state for coordination"
    )
    start_agent: str | Agent | None = Field(
        default=None, description="Agent to start execution with"
    )
    end_condition: Callable[[Any], bool] | None = Field(
        default=None, description="Function to determine when to end"
    )
    _agent_node_mapping: dict[str, str] = PrivateAttr(default_factory=dict)
    _workflow_node_mapping: dict[str, str] = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def setup_configurable_multi_agent(self) -> "ConfigurableMultiAgent":
        """Set up the configurable multi-agent system."""
        if not self.agents:
            raise ValueError("ConfigurableMultiAgent requires at least one agent")
        if self.state_schema_override:
            self.state_schema = self.state_schema_override
            logger.info(f"Using provided state schema: {self.state_schema.__name__}")
        else:
            self.state_schema = AgentSchemaComposer.from_agents(
                agents=self.agents,
                name=f"{self.__class__.__name__}State",
                include_meta=self.include_meta,
                separation=self.schema_composition_method,
                build_mode=BuildMode.CUSTOM,
            )
            logger.info(f"Composed state schema: {self.state_schema.__name__}")
        if self.state_schema:
            self.input_schema = self.state_schema.derive_input_schema()
            self.output_schema = self.state_schema.derive_output_schema()
        return self

    def add_branch(
        self,
        from_agent: str | Agent,
        condition: Callable[[Any], str],
        destinations: dict[str, str | Agent],
        default: str | Agent | None = None,
    ) -> None:
        """Add a branch/routing between agents."""
        branch = AgentBranch(from_agent, condition, destinations, default)
        self.branches.append(branch)

    def add_workflow_step(
        self,
        name: str,
        function: Callable,
        inputs: list[str | Agent] | None = None,
        outputs: list[str | Agent] | None = None,
    ) -> None:
        """Add a workflow step between agents."""
        step = WorkflowStep(name, function, inputs, outputs)
        self.workflow_steps.append(step)

    def _get_agent_node_name(self, agent: str | Agent) -> str:
        """Get the node name for an agent."""
        if isinstance(agent, str):
            for a in self.agents:
                if getattr(a, "name", None) == agent:
                    return self._get_unique_node_name(agent)
            return agent
        if isinstance(agent, Agent):
            agent_name = getattr(agent, "name", agent.__class__.__name__)
            return self._get_unique_node_name(agent_name)
        return str(agent)

    def _get_unique_node_name(self, base_name: str) -> str:
        """Ensure unique node names."""
        if base_name not in self._agent_node_mapping:
            node_name = base_name
            counter = 1
            while node_name in self._agent_node_mapping.values():
                node_name = f"{base_name}_{counter}"
                counter += 1
            self._agent_node_mapping[base_name] = node_name
        return self._agent_node_mapping[base_name]

    def _normalize_destination(self, dest: str | Agent) -> str:
        """Normalize destination to node name."""
        if dest in (END, "END"):
            return END
        return self._get_agent_node_name(dest)

    def build_graph(self) -> BaseGraph:
        """Build the graph from agents, branches, and workflow steps."""
        graph = BaseGraph(name=self.name)
        for agent in self.agents:
            node_name = self._get_agent_node_name(agent)
            graph.add_node(node_name, AgentNodeConfig(name=node_name, agent=agent))
        for step in self.workflow_steps:
            graph.add_node(step.name, step.function)
            self._workflow_node_mapping[step.name] = step.name
        for step in self.workflow_steps:
            for input_agent in step.inputs:
                input_node = self._get_agent_node_name(input_agent)
                graph.add_edge(input_node, step.name)
            for output_agent in step.outputs:
                output_node = self._get_agent_node_name(output_agent)
                graph.add_edge(step.name, output_node)
        for branch in self.branches:
            source_node = self._get_agent_node_name(branch.from_agent)
            normalized_destinations = {}
            for key, dest in branch.destinations.items():
                normalized_destinations[key] = self._normalize_destination(dest)
            default_dest = None
            if branch.default:
                default_dest = self._normalize_destination(branch.default)
            graph.add_conditional_edges(
                source_node,
                branch.condition,
                normalized_destinations,
                default=default_dest,
            )
        if self.start_agent:
            start_node = self._get_agent_node_name(self.start_agent)
            graph.add_edge(START, start_node)
        elif self.agents:
            start_node = self._get_agent_node_name(self.agents[0])
            graph.add_edge(START, start_node)
        if not self.branches and (not self.workflow_steps):
            self._add_default_sequential_flow(graph)
        return graph

    def _add_default_sequential_flow(self, graph: BaseGraph) -> None:
        """Add default sequential flow if no branches/steps defined."""
        agent_nodes = [self._get_agent_node_name(agent) for agent in self.agents]
        for i in range(len(agent_nodes) - 1):
            graph.add_edge(agent_nodes[i], agent_nodes[i + 1])
        if agent_nodes:
            graph.add_edge(agent_nodes[-1], END)

    def setup_agent(self) -> None:
        """Set up the agent - called by parent Agent class."""


def create_sequential_multi_agent(
    agents: list[Agent],
    name: str = "SequentialMultiAgent",
    state_schema: type[StateSchema] | None = None,
    **kwargs,
) -> ConfigurableMultiAgent:
    """Create a sequential multi-agent system."""
    return ConfigurableMultiAgent(
        name=name, agents=agents, state_schema_override=state_schema, **kwargs
    )


def create_branching_multi_agent(
    agents: list[Agent],
    branches: list[AgentBranch],
    name: str = "BranchingMultiAgent",
    state_schema: type[StateSchema] | None = None,
    **kwargs,
) -> ConfigurableMultiAgent:
    """Create a multi-agent system with conditional branches."""
    return ConfigurableMultiAgent(
        name=name,
        agents=agents,
        branches=branches,
        state_schema_override=state_schema,
        **kwargs,
    )


def create_workflow_multi_agent(
    agents: list[Agent],
    workflow_steps: list[WorkflowStep],
    name: str = "WorkflowMultiAgent",
    state_schema: type[StateSchema] | None = None,
    **kwargs,
) -> ConfigurableMultiAgent:
    """Create a multi-agent system with workflow steps."""
    return ConfigurableMultiAgent(
        name=name,
        agents=agents,
        workflow_steps=workflow_steps,
        state_schema_override=state_schema,
        **kwargs,
    )
