# Supervisor Archive

This directory contains archived supervisor implementations that are experimental, duplicates, or no longer actively maintained. These files are preserved for historical reference.

## Archived Files

### Alternative Implementations
- **agent_v2.py** - Alternative SupervisorAgent implementation (V2 attempt)
- **choice_model_supervisor.py** - Supervisor using choice models for agent selection
- **dynamic_supervisor.py** - Early dynamic supervisor implementation
- **dynamic_supervisor_fixed.py** - Fixed version of dynamic supervisor
- **proper_dynamic_supervisor.py** - Another dynamic supervisor attempt
- **rebuild_dynamic_supervisor.py** - Supervisor with rebuild capabilities
- **internal_dynamic_supervisor.py** - Internal dynamic supervisor variant

### Specialized Supervisors
- **dynamic_activation_supervisor.py** - Dynamic agent activation features
- **dynamic_agent_discovery_supervisor.py** - Automatic agent discovery
- **dynamic_tool_discovery_supervisor.py** - Automatic tool discovery
- **registry_supervisor.py** - Registry-based supervisor
- **integrated_supervisor.py** - Integrated supervisor approach

### Supporting Files
- **dynamic_executor_node.py** - Dynamic execution node implementation
- **multi_agent_dynamic_state.py** - Multi-agent dynamic state management

### Examples and Tests
- **example_delegation.py** - Delegation example
- **example_dynamic.py** - Dynamic supervisor example
- **example_dynamic_supervisor.py** - Another dynamic example
- **example_integrated.py** - Integrated supervisor example
- **simple_test.py** - Simple test implementation
- **simple_test_runner.py** - Test runner

## Migration Guide

If you're using any of these archived implementations:

### For Basic Supervision
Use `haive.agents.supervisor.SupervisorAgent` from agent.py

### For Dynamic Supervision
Use `haive.agents.supervisor.DynamicSupervisor` from clean_dynamic_supervisor.py

### For Simple Routing
Use `haive.agents.supervisor.SimpleSupervisor` from simple_supervisor.py

### For Custom Implementations
Extend one of the active base classes rather than using archived variants

## Active Implementations

The following remain active and supported:

- **agent.py** - SupervisorAgent (basic supervisor with routing)
- **clean_dynamic_supervisor.py** - DynamicSupervisor (dynamic agent management)
- **simple_supervisor.py** - SimpleSupervisor (simple routing supervisor)
- **dynamic_multi_agent.py** - DynamicMultiAgent (multi-agent coordination)
- **compatibility_bridge.py** - Compatibility with multi-agent patterns

### Supporting Active Files
- **registry.py** - Agent registry functionality
- **routing.py** - Routing strategies and engines
- **dynamic_agent_tools.py** - Tools for dynamic agent management
- **dynamic_state.py** - State management for dynamic supervisors

## Notes

- Some of these implementations may have unique features worth extracting
- Test files are preserved for reference but may not run without modification
- Examples show various usage patterns but may need updates for current APIs