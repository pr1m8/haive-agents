"""Base MultiAgent implementation.

This module provides the base multi-agent class that other multi-agent
implementations can inherit from or use directly.
"""

from typing import Any

from haive.core.engine.agent import Agent, AgentConfig
from pydantic import Field

# Re-export the MultiAgent implementation as the base
from haive.agents.multi.agent import MultiAgent


class SequentialAgentConfig(AgentConfig):
    """Configuration for sequential multi-agent execution."""

    agents: list[Any] = Field(
        default_factory=list, description="List of agents to run sequentially"
    )
    pass_results: bool = Field(default=True, description="Pass results between agents")


class SequentialAgent(Agent):
    """Agent that executes multiple agents in sequence.

    This agent runs a list of agents one after another, optionally
    passing the output of one agent as input to the next.
    """

    def __init__(self, config: SequentialAgentConfig):
        self.agents = config.agents
        self.pass_results = config.pass_results
        super().__init__(config)

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


__all__ = ["MultiAgent", "SequentialAgent", "SequentialAgentConfig"]
