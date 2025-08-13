"""Simple Multi-Agent implementation for basic multi-agent coordination.

This module provides a simplified multi-agent system that focuses on ease of use
and straightforward coordination patterns without complex orchestration.
"""

from __future__ import annotations

import logging
from typing import Any

from haive.core.engine.agent import Agent
from pydantic import Field

from haive.agents.multi.agent import MultiAgent

logger = logging.getLogger(__name__)


class SimpleMultiAgent(MultiAgent):
    """Simplified multi-agent system using MultiAgent.

    This class provides a simplified interface to MultiAgent with
    common defaults and simplified configuration. Perfect for simple workflows
    and quick prototyping using the enhanced base agent pattern.

    Examples:
        Basic sequential execution::

            from haive.agents.simple.agent import SimpleAgent
            from haive.agents.react.agent import ReactAgent

            agents = [
                ReactAgent(name="analyzer", tools=[...]),
                SimpleAgent(name="formatter")
            ]

            simple_multi = SimpleMultiAgent(
                name="simple_workflow",
                agents=agents,
                execution_mode="sequential"
            )

            result = await simple_multi.arun("Process this input")

        Parallel execution::

            simple_multi = SimpleMultiAgent(
                name="parallel_workflow",
                agents=agents,
                execution_mode="parallel"
            )
    """

    # Simplified defaults for common use cases
    execution_mode: str = Field(default="sequential", description="Execution mode")
    build_mode: str = Field(default="auto", description="Graph build mode")

    def model_post_init(self, __context: Any) -> None:
        """Initialize with simplified defaults."""
        super().model_post_init(__context)

        # Set up agent names if not already set
        if hasattr(self, "agents") and self.agents:
            for i, agent in enumerate(self.agents):
                if not hasattr(agent, "name") or not agent.name:
                    agent.name = f"simple_agent_{i}"

    def setup_simple_workflow(self) -> None:
        """Set up the simple multi-agent workflow with enhanced features."""
        logger.info(
            f"Setting up simple multi-agent with {len(self.agents) if hasattr(self, 'agents') else 0} agents"
        )
        logger.info(
            f"Using enhanced base agent pattern with execution mode: {self.execution_mode}"
        )

        # MultiAgent handles all the complex setup
        # We just add any simple-specific configuration here if needed


# Factory functions for common patterns


def create_simple_sequential(
    *agents: Agent, name: str = "simple_sequential"
) -> SimpleMultiAgent:
    """Create a simple sequential multi-agent using enhanced pattern."""
    return SimpleMultiAgent(name=name, agents=list(agents), execution_mode="sequential")


def create_simple_parallel(
    *agents: Agent, name: str = "simple_parallel"
) -> SimpleMultiAgent:
    """Create a simple parallel multi-agent using enhanced pattern."""
    return SimpleMultiAgent(name=name, agents=list(agents), execution_mode="parallel")


def create_simple_conditional(
    *agents: Agent, name: str = "simple_conditional"
) -> SimpleMultiAgent:
    """Create a simple conditional multi-agent using enhanced pattern."""
    return SimpleMultiAgent(
        name=name, agents=list(agents), execution_mode="conditional"
    )


# Export main classes and functions
__all__ = [
    "SimpleMultiAgent",
    "create_simple_conditional",
    "create_simple_parallel",
    "create_simple_sequential",
]
