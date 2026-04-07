"""Dynamic Supervisor - routes tasks to sub-agents via tool calls."""

from haive.agents.dynamic_supervisor.agent import DynamicSupervisor

# Backwards compatibility
DynamicSupervisorAgent = DynamicSupervisor

__all__ = ["DynamicSupervisor", "DynamicSupervisorAgent"]
