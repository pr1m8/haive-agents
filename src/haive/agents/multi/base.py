"""Compatibility module for legacy imports.

This module provides compatibility for legacy imports from haive.agents.multi.base.
New code should import from haive.agents.multi.clean instead.
"""

# Import ExecutionMode from the archived implementation for backward compatibility
from haive.agents.multi.archive.base import ExecutionMode

# Import everything from the current implementation
from haive.agents.multi.clean import MultiAgent

# Create aliases for backward compatibility
SequentialAgent = MultiAgent
ConditionalAgent = MultiAgent
ParallelAgent = MultiAgent
BranchAgent = MultiAgent

# Export the main classes
__all__ = [
    "MultiAgent",
    "SequentialAgent",
    "ConditionalAgent",
    "ParallelAgent",
    "BranchAgent",
    "ExecutionMode",
]
