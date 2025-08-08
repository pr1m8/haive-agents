# Multi-Agent Archive

This directory contains archived multi-agent implementations that are no longer actively maintained or recommended for use. These files are preserved for historical reference and to avoid breaking existing code that may depend on them.

## Archived Files

### Core Implementations

- **base.py** - Base classes and types (mostly empty, referenced by supervisors)
- **multi_agent.py** - Alternative MultiAgent implementation (used by simple_supervisor.py)
- **multi_agent_v4.py** - Early V4 attempt (superseded by enhanced_multi_agent_v4.py)

### Enhanced Variants

- **enhanced_clean_multi_agent.py** - Experimental clean multi-agent variant
- **enhanced_multi_agent_standalone.py** - Standalone enhanced implementation
- **enhanced_multi_agent_generic.py** - Generic typing experiments (moved from active)
- **enhanced_parallel_agent.py** - Specialized parallel execution agent
- **enhanced_sequential_agent.py** - Specialized sequential execution agent

### Supervisor Variants

- **enhanced_dynamic_supervisor.py** - Dynamic supervisor experiments
- **enhanced_supervisor_agent.py** - Supervisor agent experiments

### Experiments

- **experiments/** - Various experimental implementations and patterns
  - list_multi_agent.py
  - proper_list_multi_agent.py
  - routing_patterns.py
  - test_proper_usage.py

## Migration Guide

If you're using any of these archived implementations:

1. **base.py imports** → Use `haive.agents.multi.clean.MultiAgent` instead
2. **multi_agent.py** → Migrate to `haive.agents.multi.clean.MultiAgent`
3. **enhanced variants** → Use `haive.agents.multi.enhanced_multi_agent_v4.EnhancedMultiAgentV4`
4. **Generic typing needs** → Use `haive.agents.multi.enhanced_multi_agent_v3.EnhancedMultiAgent`

## Active Implementations

The following implementations remain active and supported:

- **clean.py** - Current default MultiAgent (production stable)
- **enhanced_multi_agent_v4.py** - Recommended for new projects
- **enhanced_multi_agent_v3.py** - Advanced features with generic typing

## Note on Supervisor Imports

Some supervisor implementations may still reference these archived files. These references will be updated in a future refactoring. For now, the files remain accessible to avoid breaking existing code.
