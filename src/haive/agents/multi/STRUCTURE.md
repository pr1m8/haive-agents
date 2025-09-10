# Multi-Agent Module Structure

## Modular Organization

```
multi/
├── __init__.py                      # Main module exports
├── core/                           # Core implementations
│   ├── __init__.py
│   └── clean_multi_agent.py        # Default MultiAgent
├── enhanced/                       # Enhanced versions
│   ├── __init__.py
│   ├── multi_agent_v4.py          # Recommended V4
│   └── multi_agent_v3.py          # V3 with generics
├── utils/                         # Utilities
│   ├── __init__.py
│   └── compatibility.py           # Backward compatibility
├── archive/                       # Archived implementations
│   ├── README.md
│   └── [10+ files]               # Old/experimental code
│
├── clean.py                      # ← Backward compat stub
├── enhanced_multi_agent_v4.py    # ← Backward compat stub
├── enhanced_multi_agent_v3.py    # ← Backward compat stub
└── compatibility.py              # ← Backward compat stub
```

## Import Examples

All these imports work:

```python
# New modular imports (preferred)
from haive.agents.multi.core import MultiAgent
from haive.agents.multi.enhanced import EnhancedMultiAgentV4
from haive.agents.multi.utils import ExecutionMode

# Old flat imports (still work)
from haive.agents.multi.clean import MultiAgent
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.multi.compatibility import ExecutionMode

# Main module import
from haive.agents.multi import MultiAgent  # Gets default
```

## Benefits

1. **Cleaner organization** - Related files grouped together
2. **Backward compatibility** - All old imports still work
3. **Easier navigation** - Clear where to find things
4. **Future-proof** - Easy to add new categories