"""Proper multi-agent base following exact engines dict pattern."""

from typing import Any

# Fix forward references EARLY before importing MultiAgentState
from haive.core.graph.node import agent_node_v3
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.prebuilt import multi_agent_state
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langgraph.graph import END, START
from pydantic import Field, model_validator

# Import Agent normally - circular import should be OK at runtime
from haive.agents.base.agent import Agent

# Add Agent to modules that need it for forward references
agent_node_v3.Agent = Agent
multi_agent_state.Agent = Agent

# Rebuild models that have forward references

# Now import MultiAgentState after fixing forward refs


AgentNodeV3Config.model_rebuild()
MultiAgentState.model_rebuild()


class ProperMultiAgent(Agent):
    """Multi-agent following exact engines dict pattern.

    Emulates the engines/engine pattern:
    - agents: Dict[str, Agent] = Field(default_factory=dict)
    - agent: Agent | None = Field(default=None)
    - Same normalization logic as engines
    """

    # Agent management - exact same pattern as engines
    agents: dict[str, Agent] = Field(
        default_factory=dict,
        description="Dictionary of agents this multi-agent coordinates",
    )

    agent: Agent | None = Field(
        default=None, description="Main/default agent for this multi-agent"
    )

    # Execution configuration
    execution_mode: str = Field(
        default="sequential",
        description="How to execute agents: sequential, parallel, conditional, branch",
    )

    # Branching configuration
    branch_condition: str | None = Field(
        default=None,
        description="Condition for branching execution (e.g., 'if result contains error')",
    )

    # Parallel execution settings
    parallel_wait_for_all: bool = Field(
        default=True, description="In parallel mode, wait for all agents to complete"
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_agents_and_engines(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Normalize agents dict exactly like engines normalization."""
        if not isinstance(values, dict):
            return values

        # First call parent normalization for engines
        values = super().normalize_engines_and_name(values)

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

            if isinstance(agents, list | tuple):
                # Convert list/tuple to dict
                agent_dict = {}
                for i, agent in enumerate(agents):
                    if hasattr(agent, "name") and agent.name:
                        agent_dict[agent.name] = agent
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
        """Setup hook - configure multi-agent state schema using composition."""
        if self.state_schema is None:
            # Create a simple schema that inherits from MultiAgentState
            # but requires agents to be provided
            from typing import Any

            from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
            from pydantic import model_validator

            # Store reference to the multi-agent instance for closure
            multi_agent_instance = self

            # Create a schema that inherits from MultiAgentState
            # but populates agents from the multi-agent instance
            class ComposedMultiAgentState(MultiAgentState):
                """MultiAgentState with agents populated from multi-agent instance."""

                @model_validator(mode="before")
                @classmethod
                def populate_agents_from_multi_agent(cls, data: dict[str, Any]):
                    """Populate agents if not provided."""
                    if isinstance(data, dict) and "agents" not in data:
                        # Get agents from the multi-agent instance
                        data["agents"] = multi_agent_instance.agents
                    return data

            self.state_schema = ComposedMultiAgentState
            self.use_prebuilt_base = True

    # NOTE: No need to override run/arun anymore - agents are now part of
    # state schema defaults

    def build_graph(self) -> BaseGraph:
        """Build graph using AgentNodeV3 properly."""
        # Create graph - let base agent handle state schema
        graph = BaseGraph(name=f"{self.name}_graph")

        if not isinstance(self.agents, dict):
            raise ValueError("Agents must be normalized to dict")

        # Use the create function - forward refs already fixed at import time
        from haive.core.graph.node.agent_node_v3 import create_agent_node_v3

        # Use create_agent_node_v3 factory function
        for agent_name, agent in self.agents.items():
            # Configure shared fields for structured output flow
            shared_fields = [
                "messages",
                "task_description",
                "reasoning_modules",
                # Add structured outputs from previous agents
                "selected_modules",
                "adapted_modules",
                "reasoning_structure",
                "final_answer",
            ]

            node_config = create_agent_node_v3(
                agent_name=agent_name,
                agent=agent,
                name=f"agent_{agent_name}",
                project_state=True,
                extract_from_container=True,
                update_container_state=True,
                shared_fields=shared_fields,
            )
            graph.add_node(f"agent_{agent_name}", node_config)

        # Build edges based on execution mode
        if self.execution_mode == "sequential":
            self._build_sequential_edges(graph)
        elif self.execution_mode == "parallel":
            self._build_parallel_edges(graph)
        elif self.execution_mode == "branch":
            self._build_branch_edges(graph)
        elif self.execution_mode == "conditional":
            self._build_conditional_edges(graph)
        else:
            raise NotImplementedError(f"Mode {self.execution_mode} not implemented")

        return graph

    def _build_sequential_edges(self, graph: BaseGraph):
        """Build sequential execution edges."""
        agent_names = list(self.agents.keys())

        # Connect START to first agent
        graph.add_edge(START, f"agent_{agent_names[0]}")

        # Connect agents in sequence
        for i in range(len(agent_names) - 1):
            graph.add_edge(f"agent_{agent_names[i]}", f"agent_{agent_names[i + 1]}")

        # Connect last agent to END
        graph.add_edge(f"agent_{agent_names[-1]}", END)

    def _build_parallel_edges(self, graph: BaseGraph):
        """Build parallel execution edges."""
        agent_names = list(self.agents.keys())

        # Connect START to all agents in parallel
        for agent_name in agent_names:
            graph.add_edge(START, f"agent_{agent_name}")

        if self.parallel_wait_for_all:
            # Add a gather node to wait for all agents
            def gather_results(state: dict[str, Any]):
                """Gather results from all parallel agents."""
                return state

            graph.add_node("gather", gather_results)

            # Connect all agents to gather node
            for agent_name in agent_names:
                graph.add_edge(f"agent_{agent_name}", "gather")

            # Connect gather to END
            graph.add_edge("gather", END)
        else:
            # Connect all agents directly to END
            for agent_name in agent_names:
                graph.add_edge(f"agent_{agent_name}", END)

    def _build_branch_edges(self, graph: BaseGraph):
        """Build branching execution edges."""
        agent_names = list(self.agents.keys())

        if len(agent_names) < 2:
            raise ValueError("Branch mode requires at least 2 agents")

        # First agent is the decision maker
        decision_agent = agent_names[0]
        branch_agents = agent_names[1:]

        # Connect START to decision agent
        graph.add_edge(START, f"agent_{decision_agent}")

        # Add branch router node
        def branch_router(state: dict[str, Any]):
            """Route to appropriate branch based on condition."""
            # Simple condition evaluation - can be enhanced
            if self.branch_condition:
                # Evaluate condition against state
                # For now, route to first branch agent
                return f"agent_{branch_agents[0]}"
            return f"agent_{branch_agents[0]}"

        graph.add_node("branch_router", branch_router)
        graph.add_edge(f"agent_{decision_agent}", "branch_router")

        # Connect router to branch agents
        for agent_name in branch_agents:
            graph.add_edge("branch_router", f"agent_{agent_name}")

        # Connect branch agents to END
        for agent_name in branch_agents:
            graph.add_edge(f"agent_{agent_name}", END)

    def _build_conditional_edges(self, graph: BaseGraph):
        """Build conditional execution edges."""
        agent_names = list(self.agents.keys())

        # Connect START to first agent
        graph.add_edge(START, f"agent_{agent_names[0]}")

        # Add conditional nodes between agents
        for i in range(len(agent_names) - 1):
            current_agent = agent_names[i]
            next_agent = agent_names[i + 1]

            # Add condition evaluator
            def condition_evaluator(
                state: dict[str, Any], current=current_agent, next=next_agent
            ):
                """Evaluate condition to determine next agent."""
                # Simple condition evaluation
                if self.branch_condition:
                    # For now, always proceed to next agent
                    return f"agent_{next}"
                return f"agent_{next}"

            condition_node = f"condition_{i}"
            graph.add_node(condition_node, condition_evaluator)
            graph.add_edge(f"agent_{current_agent}", condition_node)
            graph.add_edge(condition_node, f"agent_{next_agent}")

        # Connect last agent to END
        graph.add_edge(f"agent_{agent_names[-1]}", END)
