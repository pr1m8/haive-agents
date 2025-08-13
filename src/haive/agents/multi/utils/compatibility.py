"""Compatibility module for legacy multi-agent imports.

This module provides backward compatibility for code that imports from:
- haive.agents.multi.base
- haive.agents.multi.multi_agent
- haive.agents.multi.base_multi_agent

New code should use:
- haive.agents.multi.clean.MultiAgent (current default)
- haive.agents.multi.enhanced_multi_agent_v4.MultiAgent (recommended)
"""

from enum import Enum

# Import the current MultiAgent implementation
from haive.agents.multi.agent import MultiAgent

# For imports that expect base_multi_agent.BaseMultiAgent
BaseMultiAgent = MultiAgent


class ExecutionMode(str, Enum):
    """Legacy ExecutionMode enum for backward compatibility.

    Modern implementations use string literals instead:
    - "sequential"
    - "parallel"
    - "conditional"
    - "branch"
    - "infer"
    """

    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    CONDITIONAL = "conditional"
    BRANCH = "branch"
    INFER = "infer"


# Aliases for backward compatibility
SequentialAgent = MultiAgent
ParallelAgent = MultiAgent
ConditionalAgent = MultiAgent
BranchAgent = MultiAgent


__all__ = [
    "BaseMultiAgent",
    "BranchAgent",
    "ConditionalAgent",
    "ExecutionMode",
    "MultiAgent",
    "ParallelAgent",
    "SequentialAgent",
]
