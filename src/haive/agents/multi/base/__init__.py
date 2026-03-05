"""Base multi-agent module."""

from haive.agents.multi.base.agent import (
    MultiAgent,
    SequentialAgent,
    SequentialAgentConfig,
)

# Aliases for legacy compatibility
ConditionalAgent = MultiAgent
ParallelAgent = MultiAgent

__all__ = [
    "ConditionalAgent",
    "MultiAgent",
    "ParallelAgent",
    "SequentialAgent",
    "SequentialAgentConfig",
]
