"""Clean MultiAgent base class - simple and proper."""

from typing import Any, Dict, List, Optional, Union

from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from pydantic import Field, computed_field, model_validator

from haive.agents.base.agent import Agent


class MultiAgent(Agent):
    """Simple multi-agent that coordinates other agents.

    Core concept: A MultiAgent IS an Agent that contains other agents.
    It uses BaseGraph to build the execution graph.
    """

    # Core agent management - follows same pattern as engines
    agents: Dict[str, Agent] = Field(
        default_factory=dict,
        description="Dictionary of agents this multi-agent coordinates",
    )

    agent: Agent | None = Field(
        default=None, description="Main/default agent for this multi-agent"
    )

    # Execution mode
    execution_mode: str = Field(
        default="infer",
        description="How to execute agents: infer, sequential, parallel, conditional, branch",
    )

    # Sequence inference configuration
    infer_sequence: bool = Field(
        default=True,
        description="Whether to automatically infer execution sequence from agent dependencies",
    )

    # Branch configuration
    branches: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="Branch configurations for conditional routing",
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_agents_and_name(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize agents dict and auto-generate name - follows engines pattern."""
        if not isinstance(values, dict):
            return values

        # Initialize agents dict if not present
        if "agents" not in values:
            values["agents"] = {}

        # Move single agent to agents dict
        if "agent" in values and values["agent"] is not None:
            agent = values["agent"]
            # Add to agents dict with appropriate key
            if hasattr(agent, "name") and agent.name:
                values["agents"][agent.name] = agent
            else:
                values["agents"]["main"] = agent

        # Normalize agents field to always be a dict
        if "agents" in values and values["agents"] is not None:
            agents = values["agents"]

            if isinstance(agents, list):
                # Convert list to dict using agent names
                agent_dict = {}
                for i, agent in enumerate(agents):
                    if hasattr(agent, "name") and agent.name:
                        # Handle duplicate names by adding index
                        base_name = agent.name
                        if base_name in agent_dict:
                            agent_dict[f"{base_name}_{i}"] = agent
                        else:
                            agent_dict[base_name] = agent
                    else:
                        agent_dict[f"agent_{i}"] = agent
                values["agents"] = agent_dict

            elif not isinstance(agents, dict):
                # Single agent not in dict form
                if hasattr(agents, "name") and agents.name:
                    values["agents"] = {agents.name: agents}
                else:
                    values["agents"] = {"main": agents}

        return values

    def setup_agent(self) -> None:
        """Setup multi-agent - use MultiAgentState by default."""
        super().setup_agent()

        # Set default state schema if none provided
        if self.state_schema is None:
            self.state_schema = MultiAgentState

    def build_graph(self) -> BaseGraph:
        """Build the BaseGraph for this multi-agent.

        Uses intelligent routing from BaseGraph for sequence inference and branching.
        """
        # Create BaseGraph with state schema
        graph = BaseGraph(name=f"{self.name}_graph", state_schema=self.state_schema)

        # Use BaseGraph's intelligent routing
        graph.add_intelligent_agent_routing(
            agents=self.agents,
            execution_mode=self.execution_mode,
            branches=self.branches,
            prefix="",  # No prefix for clean agent names
        )

        return graph

    @classmethod
    def create(
        cls,
        agents: List[Agent],
        name: str = "multi_agent",
        execution_mode: str = "infer",
        **kwargs,
    ) -> "MultiAgent":
        """Create a multi-agent from a list of agents."""
        return cls(name=name, agents=agents, execution_mode=execution_mode, **kwargs)

    def add_branch(self, source_agent: str, condition: str, target_agents: List[str]):
        """Add a branch condition for routing between agents.

        Args:
            source_agent: The agent to branch from
            condition: The condition logic (e.g., 'if error' or 'if success')
            target_agents: List of possible target agents
        """
        self.branches[source_agent] = {"condition": condition, "targets": target_agents}

    def set_sequence(self, sequence: List[str]):
        """Manually set the execution sequence of agents.

        Args:
            sequence: List of agent names in execution order
        """
        # Validate that all agents exist
        for agent_name in sequence:
            if agent_name not in self.agents:
                raise ValueError(f"Agent '{agent_name}' not found in agents dict")

        # Store the sequence and disable inference
        self.execution_mode = "sequential"
        self.infer_sequence = False

        # Reorder agents dict to match sequence
        ordered_agents = {name: self.agents[name] for name in sequence}
        # Add any remaining agents
        for name, agent in self.agents.items():
            if name not in ordered_agents:
                ordered_agents[name] = agent

        self.agents = ordered_agents
