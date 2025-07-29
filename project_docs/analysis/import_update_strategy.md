# Import Update Strategy - Memory Reorganization

**Date**: 2025-01-28  
**Purpose**: Fix all imports after memory module reorganization

## 🔍 Current Import Issues

### 1. **Source Files (memory_reorganized/)**

- Relative imports pointing to non-existent files
- Cross-references to old memory_v2 structure
- Missing dependencies after file moves

### 2. **Test Files (tests/memory_reorganized/)**

- All imports still pointing to `haive.agents.memory_v2.*`
- Need to update to new module structure
- Some imports reference files that were moved/renamed

## 📋 Import Update Plan

### Phase 1: Update Source File Imports

#### Files with Issues:

1. `agents/simple.py` - Relative imports to moved files
2. `agents/multi.py` - Cross-references to other agents
3. `base/token_state.py` - Relative imports
4. `agents/long_term_v2.py` - Old agent path references

#### Update Strategy:

```python
# OLD (broken)
from .memory_state_original import MemoryState
from .memory_tools import MemoryConfig

# NEW (fixed)
from haive.agents.memory_reorganized.base.state import MemoryState
from haive.agents.memory_reorganized.core.types import MemoryConfig
```

### Phase 2: Update Test File Imports

#### Pattern Updates:

```python
# OLD pattern in tests
from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent

# NEW pattern
from haive.agents.memory_reorganized.agents.simple import SimpleMemoryAgent
```

#### Files to Update:

- `agents/test_*.py` (8 files)
- `api/test_*.py` (2 files)
- `core/test_*.py` (3 files)
- `coordination/test_*.py` (1 file)
- `integrations/test_*.py` (3 files)
- `base/test_*.py` (1 file)

### Phase 3: Create Module **init**.py Files

#### Purpose:

- Expose public API from each submodule
- Allow clean imports like `from haive.agents.memory_reorganized import SimpleMemoryAgent`
- Hide internal implementation details

#### Structure:

```python
# memory_reorganized/__init__.py
from .agents.simple import SimpleMemoryAgent
from .agents.react import ReactMemoryAgent
from .api.unified import UnifiedMemoryAPI

# memory_reorganized/agents/__init__.py
from .simple import SimpleMemoryAgent
from .react import ReactMemoryAgent
from .multi import MultiMemoryAgent

# memory_reorganized/core/__init__.py
from .types import MemoryType, MemoryConfig
from .classifier import MemoryClassifier
```

## 🛠️ Implementation Commands

### Step 1: Fix Source File Imports

#### Fix agents/simple.py

```python
# Replace broken relative imports
from haive.agents.memory_reorganized.base.state import MemoryState
from haive.agents.memory_reorganized.base.token_state import MemoryStateWithTokens
from haive.agents.memory_reorganized.core.types import MemoryConfig
```

#### Fix agents/multi.py

```python
# Update cross-agent references
from haive.agents.memory_reorganized.agents.simple import SimpleMemoryAgent
from haive.agents.memory_reorganized.base.token_state import MemoryStateWithTokens
```

#### Fix agents/long_term_v2.py

```python
# Update old agent references
from haive.agents.react_agent2.agent import ReactAgentConfig  # If this exists
# Or find correct path for ReactAgentConfig
```

### Step 2: Batch Update Test Imports

#### Command to update all test files:

```bash
# Update memory_v2 references to memory_reorganized
find tests/memory_reorganized -name "*.py" -exec sed -i 's/haive\.agents\.memory_v2/haive.agents.memory_reorganized/g' {} \;

# Update specific component paths
find tests/memory_reorganized -name "*.py" -exec sed -i 's/\.simple_memory_agent/\.agents\.simple/g' {} \;
find tests/memory_reorganized -name "*.py" -exec sed -i 's/\.react_memory_agent/\.agents\.react/g' {} \;
find tests/memory_reorganized -name "*.py" -exec sed -i 's/\.multi_memory_agent/\.agents\.multi/g' {} \;
```

### Step 3: Create Public API **init**.py Files

#### Main module init:

```python
# memory_reorganized/__init__.py
"""Unified Memory Module for Haive Agents.

This module provides comprehensive memory functionality including:
- Simple and React memory agents
- Token-aware memory management
- Multi-agent coordination
- Search and retrieval capabilities
- Knowledge graph integration
"""

# Core agents
from .agents.simple import SimpleMemoryAgent
from .agents.react import ReactMemoryAgent
from .agents.multi import MultiMemoryAgent

# API
from .api.unified_memory_api import UnifiedMemoryAPI

# Base classes
from .base.state import MemoryState
from .core.types import MemoryType, MemoryConfig

__all__ = [
    "SimpleMemoryAgent",
    "ReactMemoryAgent",
    "MultiMemoryAgent",
    "UnifiedMemoryAPI",
    "MemoryState",
    "MemoryType",
    "MemoryConfig"
]
```

## 🎯 Success Criteria

### Import Resolution

- [ ] All source files import successfully
- [ ] No missing dependency errors
- [ ] Clean public API available

### Test Compatibility

- [ ] All test files import correctly
- [ ] Tests can find their target components
- [ ] No import path errors

### API Usability

- [ ] Simple imports work: `from haive.agents.memory_reorganized import SimpleMemoryAgent`
- [ ] Submodule imports work: `from haive.agents.memory_reorganized.search import SemanticSearchAgent`
- [ ] Backwards compatibility maintained where possible

## 🚨 Risk Mitigation

### Backup Strategy

- Keep original directories until imports are verified
- Test imports before committing changes
- Incremental updates with verification

### Testing Strategy

- Import test after each fix
- Run basic functionality tests
- Verify no circular dependencies

### Rollback Plan

- Document all changes made
- Keep import mapping for reverting
- Test restoration procedure

## 📊 Import Mapping Reference

### Component Mapping

| Old Import                           | New Import                              |
| ------------------------------------ | --------------------------------------- |
| `memory_v2.simple_memory_agent`      | `memory_reorganized.agents.simple`      |
| `memory_v2.react_memory_agent`       | `memory_reorganized.agents.react`       |
| `memory_v2.multi_memory_agent`       | `memory_reorganized.agents.multi`       |
| `memory_v2.memory_state`             | `memory_reorganized.base.state`         |
| `memory_v2.token_aware_memory_state` | `memory_reorganized.core.token_tracker` |

### Module Structure

| Component  | New Location                  |
| ---------- | ----------------------------- |
| Agents     | `memory_reorganized.agents.*` |
| States     | `memory_reorganized.base.*`   |
| Core Utils | `memory_reorganized.core.*`   |
| Search     | `memory_reorganized.search.*` |
| API        | `memory_reorganized.api.*`    |

Ready to execute import updates!
