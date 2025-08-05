"""List-based multi-agent implementation.

from typing import Any
A clean, simple multi-agent that acts like a Python list of agents.
Focus on composition and orchestration, not complex state management.
"""

import logging
from collections.abc import Iterator, Sequence
from typing import Any

from haive.core.common.mixins.recompile_mixin import RecompileMixin
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langchain_core.messages import BaseMessage
from langgraph.graph import END, START
from pydantic import Field, PrivateAttr

from haive.agents.base.agent import Agent

logger = logging.getLogger(__name__)


class ListMultiAgent(Agent, RecompileMixin, Sequence[Agent]):
    """Multi-agent system that works like a Python list.

    Simple, clean interface for composing agents:
    - Append, insert, remove agents like a list
    - Agents execute in sequence by default
    - Each agent manages its own tools/state
    - Message passing between agents

    Example:
        .. code-block:: python

            multi = ListMultiAgent("my_system")
            multi.append(PlannerAgent())
            multi.append(ResearchAgent())
            multi.append(WriterAgent())

            result = multi.invoke({"messages": [HumanMessage("Write about AI")]})

    """

    # The list of agents
    agents: list[Agent] = Field(default_factory=list)

    # Execution control
    stop_on_error: bool = Field(default=False)
    max_iterations: int = Field(default=1)

    # Private state
    _agent_index: dict[str, int] = PrivateAttr(default_factory=dict)

    # ========== List Interface ==========

    def __getitem__(self, index: int | slice) -> Agent | list[Agent]:
        return self.agents[index]

    def __len__(self) -> int:
        return len(self.agents)

    def __iter__(self) -> Iterator[Agent]:
        return iter(self.agents)

    def append(self, agent: Agent) -> "ListMultiAgent":
        """Add agent to end of list."""
        self.agents.append(agent)
        self._update_index()
        self.mark_for_recompile(f"Added agent: {agent.name}")
        return self

    def insert(self, index: int, agent: Agent) -> "ListMultiAgent":
        """Insert agent at specific position."""
        self.agents.insert(index, agent)
        self._update_index()
        self.mark_for_recompile(f"Inserted agent: {agent.name} at {index}")
        return self

    def remove(self, agent: Agent | str) -> "ListMultiAgent":
        """Remove agent by instance or name."""
        if isinstance(agent, str):
            # Remove by name
            for i, a in enumerate(self.agents):
                if a.name == agent:
                    self.agents.pop(i)
                    break
        else:
            # Remove by instance
            self.agents.remove(agent)

        self._update_index()
        self.mark_for_recompile(f"Removed agent: {agent if isinstance(agent, str) else agent.name}")
        return self

    def pop(self, index: int = -1) -> Agent:
        """Remove and return agent at index."""
        agent = self.agents.pop(index)
        self._update_index()
        self.mark_for_recompile(f"Popped agent: {agent.name}")
        return agent

    def clear(self) -> "ListMultiAgent":
        """Remove all agents."""
        self.agents.clear()
        self._update_index()
        self.mark_for_recompile("Cleared all agents")
        return self

    # ========== Builder Methods ==========

    def then(self, agent: Agent) -> "ListMultiAgent":
        """Add next agent in chain (alias for append)."""
        return self.append(agent)

    def __rshift__(self, agent: Agent) -> "ListMultiAgent":
        """Support >> operator for chaining."""
        return self.append(agent)

    # ========== Graph Building ==========

    def build_graph(self) -> BaseGraph:
        """Build simple sequential graph."""
        graph = BaseGraph(state_schema=self.state_schema)

        if not self.agents:
            # Empty multi-agent just passes through
            graph.add_node("passthrough", lambda x: x)
            graph.add_edge(START, "passthrough")
            graph.add_edge("passthrough", END)
            return graph.compile()

        # Build sequential chain
        prev_node = START

        for i, agent in enumerate(self.agents):
            node_name = f"{agent.name}_{i}"

            # Each agent processes the full state but we only pass messages
            # This keeps it simple - agents already have their tools in their
            # engine/state
            def make_agent_node(agent_instance: Any):
                def agent_node(state: dict[str, Any]) -> dict[str, Any]:
                    # Extract messages
                    messages = state.get("messages", [])

                    # Invoke agent with messages
                    agent_input = {"messages": messages}

                    # Add any other shared fields from state
                    for key in ["context", "metadata"]:
                        if key in state:
                            agent_input[key] = state[key]

                    # Run agent
                    result = agent_instance.invoke(agent_input)

                    # Update state with results
                    output = {}

                    # Always update messages
                    if "messages" in result:
                        output["messages"] = result["messages"]
                    elif isinstance(result, list) and all(
                        isinstance(m, BaseMessage) for m in result
                    ):
                        output["messages"] = result

                    # Pass through other fields
                    for key, value in result.items():
                        if key != "messages":
                            output[key] = value

                    return output

                return agent_node

            graph.add_node(node_name, make_agent_node(agent))
            graph.add_edge(prev_node, node_name)
            prev_node = node_name

        graph.add_edge(prev_node, END)

        return graph.compile()

    def setup_agent(self) -> None:
        """Setup the multi-agent system."""
        self._update_index()

    def _update_index(self) -> None:
        """Update agent name to index mapping."""
        self._agent_index = {agent.name: i for i, agent in enumerate(self.agents)}

    def get_agent_by_name(self, name: str) -> Agent | None:
        """Get agent by name."""
        index = self._agent_index.get(name)
        return self.agents[index] if index is not None else None

    def get_agent_names(self) -> list[str]:
        """Get list of agent names in order."""
        return [agent.name for agent in self.agents]

    # ========== String Representation ==========

    def __str__(self) -> str:
        """String representation."""
        agent_names = ", ".join(agent.name for agent in self.agents)
        return f"ListMultiAgent([{agent_names}])"

    def __repr__(self) -> str:
        """Detailed representation."""
        return f"ListMultiAgent(name='{self.name}', agents={len(self.agents)}, mode=sequential)"


# Convenience factory functions


def sequential(*agents: Agent, name: str = "sequential_multi") -> ListMultiAgent:
    """Create a sequential multi-agent from agents."""
    multi = ListMultiAgent(name=name)
    for agent in agents:
        multi.append(agent)
    return multi


def pipeline(*agents: Agent, name: str = "pipeline") -> ListMultiAgent:
    """Create a pipeline of agents (alias for sequential)."""
    return sequential(*agents, name=name)
