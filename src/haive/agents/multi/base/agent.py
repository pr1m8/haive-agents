"""Base MultiAgent implementation.

This module provides the base multi-agent class that other multi-agent
implementations can inherit from or use directly.
"""

from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langgraph.graph import END, START
from pydantic import Field

from haive.agents.base.agent import Agent

# Re-export the MultiAgent implementation as the base
from haive.agents.multi.agent import MultiAgent


class SequentialAgent(Agent):
    """Agent that executes multiple agents in sequence.

    This agent runs a list of agents one after another, optionally
    passing the output of one agent as input to the next.
    """

    agents: list = Field(default_factory=list, description="Ordered list of agents")
    pass_results: bool = Field(
        default=True, description="Pass results between agents"
    )
    engine: AugLLMConfig | None = Field(
        default=None,
        description="Optional coordinator engine",
    )

    def build_graph(self) -> BaseGraph:
        """Build sequential execution graph."""
        graph = BaseGraph(name=self.name or "SequentialAgent")

        if not self.agents:
            # Empty agent list — create passthrough graph
            def passthrough(state: dict[str, Any]) -> dict[str, Any]:
                return state

            graph.add_node("passthrough", passthrough)
            graph.add_edge(START, "passthrough")
            graph.add_edge("passthrough", END)
            return graph

        # Build sequential chain: agent_0 → agent_1 → ... → agent_n
        prev_name = None
        for i, agent in enumerate(self.agents):
            node_name = f"agent_{i}"

            def make_node(a: Any) -> Any:
                def node_fn(state: dict[str, Any]) -> dict[str, Any]:
                    if hasattr(a, "run"):
                        result = a.run(state)
                        if isinstance(result, dict):
                            return result
                        return {"output": result}
                    return state

                return node_fn

            graph.add_node(node_name, make_node(agent))

            if prev_name is None:
                graph.add_edge(START, node_name)
            else:
                graph.add_edge(prev_name, node_name)

            prev_name = node_name

        if prev_name:
            graph.add_edge(prev_name, END)

        return graph

    def run(self, input_data: Any, **kwargs) -> Any:
        """Run all agents in sequence."""
        current_input = input_data
        results = []

        for agent in self.agents:
            if hasattr(agent, "run"):
                result = agent.run(current_input, **kwargs)
                results.append(result)

                if self.pass_results:
                    current_input = result
            else:
                results.append(f"Agent {agent} does not have run method")

        return results if len(results) > 1 else results[0] if results else None


__all__ = ["MultiAgent", "SequentialAgent"]
