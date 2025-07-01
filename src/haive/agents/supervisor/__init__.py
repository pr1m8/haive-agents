"""Haive Supervisor Agent Package

Provides sophisticated multi-agent orchestration using ReactAgent patterns
with dynamic routing and intelligent agent coordination.
"""

from .agent import SupervisorAgent, SupervisorState
from .registry import AgentRegistry

__all__ = [
    "SupervisorAgent",
    "SupervisorState",
    "AgentRegistry",
]
