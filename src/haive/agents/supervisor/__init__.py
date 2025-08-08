"""Supervisor Module - Dynamic agent discovery and management.

This module provides the DynamicSupervisor (also exported as SupervisorAgent for compatibility),
which can discover, create, and manage agents at runtime based on task requirements.

Main Components:
    - SupervisorAgent/DynamicSupervisor: Main supervisor class
    - AgentSpec: Specifications for creating agents
    - AgentCapability: Agent capability metadata
    - SupervisorState: State management
    - Discovery tools and utilities
"""

# Main supervisor implementation
from haive.agents.supervisor.agent import DynamicSupervisor
from haive.agents.supervisor.agent import (
    DynamicSupervisor as SupervisorAgent,  # Compatibility alias
)
from haive.agents.supervisor.agent import create_dynamic_supervisor
from haive.agents.supervisor.agent import (
    create_dynamic_supervisor as create_supervisor,  # Compatibility alias
)

# Models and state
from haive.agents.supervisor.models import (
    AgentCapability,
    AgentDiscoveryMode,
    AgentSpec,
    DiscoveryConfig,
)
from haive.agents.supervisor.state import (
    ActiveAgent,
)
from haive.agents.supervisor.state import DynamicSupervisorState
from haive.agents.supervisor.state import (
    DynamicSupervisorState as SupervisorState,  # Compatibility alias
)
from haive.agents.supervisor.state import (
    SupervisorMetrics,
    create_initial_state,
)

# Tools and utilities
from haive.agents.supervisor.tools import (
    AgentManagementTools,
    create_agent_from_spec,
    create_handoff_tool,
    discover_agents,
    find_matching_agent_specs,
)

__all__ = [
    # Main classes (with compatibility names)
    "DynamicSupervisor",
    "SupervisorAgent",
    "create_dynamic_supervisor",
    "create_supervisor",
    # Models
    "AgentSpec",
    "AgentCapability",
    "AgentDiscoveryMode",
    "DiscoveryConfig",
    # State
    "DynamicSupervisorState",
    "SupervisorState",
    "ActiveAgent",
    "SupervisorMetrics",
    "create_initial_state",
    # Tools and utilities
    "create_agent_from_spec",
    "find_matching_agent_specs",
    "discover_agents",
    "create_handoff_tool",
    "AgentManagementTools",
]
