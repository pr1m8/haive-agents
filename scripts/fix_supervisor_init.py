#!/usr/bin/env python3
"""Fix the broken supervisor __init__.py file."""

from pathlib import Path


def fix_supervisor_init():
    """Rewrite supervisor __init__.py with clean exports."""
    init_file = (
        Path(__file__).parent.parent
        / "src"
        / "haive"
        / "agents"
        / "supervisor"
        / "__init__.py"
    )

    # Write a clean version
    content = '''"""Supervisor module exports."""

from haive.agents.supervisor.agent import SupervisorAgent, SupervisorState
from haive.agents.supervisor.choice_model_supervisor import (
    AgentCreationTool,
    AgentSelectionTool,
    ChoiceModelSupervisor,
)
from haive.agents.supervisor.clean_dynamic_supervisor import (
    DynamicSupervisor,
    DynamicSupervisorState,
)
from haive.agents.supervisor.compatibility_bridge import (
    DynamicMultiAgentSupervisor,
    ReactMultiAgentSupervisor,
    create_compatible_supervisor,
    migrate_from_multi_agent,
)
from haive.agents.supervisor.dynamic_activation_supervisor import DynamicActivationSupervisor
from haive.agents.supervisor.dynamic_agent_discovery_supervisor import (
    AgentCapability,
    AgentDiscoveryMode,
    DynamicAgentDiscoverySupervisor,
)
from haive.agents.supervisor.dynamic_agent_tools import (
    AddAgentInput,
    AddAgentTool,
    AgentDescriptor,
    AgentRegistryManager,
    AgentSelectorTool,
    ChangeAgentInput,
    ChangeAgentTool,
    ListAgentsInput,
    ListAgentsTool,
    RemoveAgentInput,
    RemoveAgentTool,
    create_agent_management_tools,
    register_agent_constructor,
)
from haive.agents.supervisor.dynamic_executor_node import (
    DynamicExecutorNode,
    create_dynamic_executor_node,
)
from haive.agents.supervisor.dynamic_multi_agent import (
    DynamicMultiAgent,
    create_dynamic_multi_agent,
)
from haive.agents.supervisor.dynamic_state import (
    AgentExecutionConfig,
    AgentExecutionResult,
    DynamicSupervisorState,
    SupervisorDecision,
)
from haive.agents.supervisor.multi_agent_dynamic_state import (
    AgentRegistryState,
    MultiAgentCoordinationState,
    MultiAgentDynamicSupervisorState,
)
from haive.agents.supervisor.registry import AgentRegistry
from haive.agents.supervisor.registry_supervisor import (
    AgentRetrievalTool,
    RegistrySupervisor,
)
from haive.agents.supervisor.routing import (
    BaseRoutingStrategy,
    DynamicRoutingEngine,
    LLMRoutingStrategy,
    RoutingContext,
    RoutingDecision,
    RuleBasedRoutingStrategy,
    TaskClassifier,
)
from haive.agents.supervisor.simple_supervisor import SimpleSupervisor

# Note: dynamic_tool_discovery_supervisor has import issues, skipping for now

__all__ = [
    # Core supervisors
    "SupervisorAgent",
    "SupervisorState",
    "DynamicSupervisor",
    "DynamicSupervisorState",
    "SimpleSupervisor",
    
    # Specialized supervisors
    "ChoiceModelSupervisor",
    "DynamicActivationSupervisor",
    "DynamicAgentDiscoverySupervisor",
    "RegistrySupervisor",
    
    # Multi-agent support
    "DynamicMultiAgent",
    "DynamicMultiAgentSupervisor",
    "ReactMultiAgentSupervisor",
    
    # Tools and utilities
    "AgentRegistry",
    "AgentRegistryManager",
    "AddAgentTool",
    "RemoveAgentTool",
    "ListAgentsTool",
    "AgentSelectorTool",
    "ChangeAgentTool",
    "AgentCreationTool",
    "AgentSelectionTool",
    "AgentRetrievalTool",
    
    # State and configuration
    "DynamicSupervisorState",
    "AgentRegistryState",
    "MultiAgentCoordinationState",
    "MultiAgentDynamicSupervisorState",
    "AgentExecutionConfig",
    "AgentExecutionResult",
    "SupervisorDecision",
    
    # Routing
    "BaseRoutingStrategy",
    "DynamicRoutingEngine",
    "LLMRoutingStrategy",
    "RuleBasedRoutingStrategy",
    "RoutingContext",
    "RoutingDecision",
    "TaskClassifier",
    
    # Types
    "AgentCapability",
    "AgentDiscoveryMode",
    "AgentDescriptor",
    "AddAgentInput",
    "ChangeAgentInput",
    "ListAgentsInput",
    "RemoveAgentInput",
    
    # Functions
    "create_agent_management_tools",
    "create_compatible_supervisor",
    "create_dynamic_executor_node",
    "create_dynamic_multi_agent",
    "migrate_from_multi_agent",
    "register_agent_constructor",
    
    # Nodes
    "DynamicExecutorNode",
]
'''

    init_file.write_text(content)
    print("✅ Fixed supervisor __init__.py")


if __name__ == "__main__":
    fix_supervisor_init()
