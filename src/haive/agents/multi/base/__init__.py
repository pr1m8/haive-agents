"""Base multi-agent module."""

from haive.agents.multi.base.agent import (
    MultiAgent,
    SequentialAgent,
)

# Aliases for legacy compatibility
ConditionalAgent = MultiAgent
ParallelAgent = MultiAgent

__all__ = [
    "ConditionalAgent",
    "MultiAgent",
    "ParallelAgent",
    "SequentialAgent",
]
