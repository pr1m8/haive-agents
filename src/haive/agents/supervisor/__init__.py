"""Haive Supervisor Agent Package.

Provides sophisticated multi-agent orchestration using ReactAgent patterns
with dynamic routing and intelligent agent coordination. Includes traditional
supervisor, enhanced dynamic supervisor, and integrated multi-agent supervisor
implementations with tool-based agent management.

New Dynamic Discovery Supervisors:
    - DynamicToolDiscoverySupervisor: Discovers and distributes tools to agents
    - DynamicAgentDiscoverySupervisor: Discovers and adds specialized agents

Example:
    Using dynamic agent discovery::

        from haive.agents.supervisor import (
            DynamicAgentDiscoverySupervisor,
            AgentDiscoveryMode
        )

        supervisor = DynamicAgentDiscoverySupervisor(
            name="team_builder",
            agents={"assistant": SimpleAgent(...)},
            engine=AugLLMConfig(),
            discovery_mode=AgentDiscoveryMode.HYBRID
        )

        result = await supervisor.arun("I need a data science expert")
"""

from haive.agents.supervisor.agent import SupervisorAgent, SupervisorState

# New dynamic discovery supervisors
# from haive.agents.supervisor.dynamic_tool_discovery_supervisor import (
#     DynamicToolDiscoverySupervisor,
#     ToolDiscoveryMode
# )
from haive.agents.supervisor.dynamic_agent_discovery_supervisor import (
    AgentCapability,
    AgentDiscoveryMode,
    DynamicAgentDiscoverySupervisor,
)

# from haive.agents.supervisor.dynamic_activation_supervisor import DynamicActivationSupervisor
# from haive.agents.supervisor.dynamic_agent_tools import (
#     AddAgentTool,
#     AgentDescriptor,
#     AgentRegistryManager,
#     ChangeAgentTool,
#     ListAgentsTool,
#     RemoveAgentTool,
#     create_agent_management_tools,
# )
from haive.agents.supervisor.dynamic_state import (
    AgentExecutionConfig,
    AgentExecutionResult,
    DynamicSupervisorState,
    SupervisorDecision,
)
from haive.agents.supervisor.dynamic_supervisor import DynamicSupervisorAgent

# from haive.agents.supervisor.integrated_supervisor import IntegratedDynamicSupervisor
from haive.agents.supervisor.multi_agent_dynamic_state import (
    AgentRegistryState,
    MultiAgentCoordinationState,
    MultiAgentDynamicSupervisorState,
)
from haive.agents.supervisor.registry import AgentRegistry

__all__ = [
    # "AddAgentTool",
    # Agent management tools
    # "AgentDescriptor",
    "AgentExecutionConfig",
    "AgentExecutionResult",
    "AgentRegistry",
    # "AgentRegistryManager",
    "AgentRegistryState",
    # "ChangeAgentTool",
    # Dynamic activation supervisor
    # "DynamicActivationSupervisor",
    # Dynamic supervisor
    "DynamicSupervisorAgent",
    "DynamicSupervisorState",
    # Integrated multi-agent supervisor
    # "IntegratedDynamicSupervisor",
    # "ListAgentsTool",
    "MultiAgentCoordinationState",
    "MultiAgentDynamicSupervisorState",
    # "RemoveAgentTool",
    # Traditional supervisor
    "SupervisorAgent",
    "SupervisorDecision",
    "SupervisorState",
    # "create_agent_management_tools",
    # New dynamic discovery supervisors
    # "DynamicToolDiscoverySupervisor",
    "DynamicAgentDiscoverySupervisor",
    # Discovery modes and types
    # "ToolDiscoveryMode",
    "AgentDiscoveryMode",
    "AgentCapability",
]
