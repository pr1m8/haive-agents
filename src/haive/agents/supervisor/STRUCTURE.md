# Supervisor Module Structure

## Modular Organization

```
supervisor/
├── __init__.py                      # Main module exports
├── core/                           # Core implementations
│   ├── __init__.py
│   ├── supervisor_agent.py        # Basic SupervisorAgent
│   └── simple_supervisor.py       # Lightweight SimpleSupervisor
├── dynamic/                        # Dynamic features
│   ├── __init__.py
│   ├── dynamic_supervisor.py      # DynamicSupervisor (recommended)
│   ├── dynamic_multi_agent.py     # DynamicMultiAgent
│   └── dynamic_agent_tools.py     # Agent management tools
├── utils/                         # Utilities
│   ├── __init__.py
│   ├── registry.py               # Agent registry
│   ├── routing.py                # Routing strategies
│   └── compatibility_bridge.py   # Multi-agent compatibility
├── state/                         # State management
│   ├── __init__.py
│   └── dynamic_state.py          # State schemas
├── archive/                       # Archived implementations
│   ├── README.md
│   └── [17+ files]              # Old/experimental code
│
├── agent.py                      # ← Backward compat stub
├── clean_dynamic_supervisor.py   # ← Backward compat stub
├── simple_supervisor.py          # ← Backward compat stub
├── dynamic_multi_agent.py        # ← Backward compat stub
├── registry.py                   # ← Backward compat stub
├── routing.py                    # ← Backward compat stub
├── compatibility_bridge.py       # ← Backward compat stub
├── dynamic_agent_tools.py        # ← Backward compat stub
└── dynamic_state.py             # ← Backward compat stub
```

## Import Examples

All these imports work:

```python
# New modular imports (preferred)
from haive.agents.supervisor.core import SupervisorAgent
from haive.agents.supervisor.dynamic import DynamicSupervisor
from haive.agents.supervisor.utils import AgentRegistry

# Old flat imports (still work)
from haive.agents.supervisor.agent import SupervisorAgent
from haive.agents.supervisor.clean_dynamic_supervisor import DynamicSupervisor
from haive.agents.supervisor.registry import AgentRegistry

# Main module import
from haive.agents.supervisor import SupervisorAgent, DynamicSupervisor
```

## Module Categories

### Core (`core/`)

- Basic supervisor functionality
- Essential routing capabilities
- Lightweight implementations

### Dynamic (`dynamic/`)

- Runtime agent management
- Dynamic graph rebuilding
- Advanced coordination features

### Utils (`utils/`)

- Support utilities
- Integration helpers
- Common functionality

### State (`state/`)

- State schemas and models
- Shared state definitions

## Benefits

1. **Logical grouping** - Related functionality together
2. **Backward compatibility** - No breaking changes
3. **Clear hierarchy** - Easy to understand structure
4. **Scalable** - Easy to add new categories
