# TODO - haive-agents

## 🚨 Critical Issues

### Multi-Agent Module Reorganization ✅ PARTIALLY COMPLETED

**Issue**: The multi-agent module has become messy with 30+ different implementations and broken supervisor imports.

**Progress (2025-01-29)**:

- ✅ Created `archive/` directory and moved experimental implementations
- ✅ Fixed supervisor imports with compatibility module
- ✅ Documented all active implementations (V4 as recommended, clean as default, V3 for generics)
- ✅ Created archive/README.md to explain archived files
- ⏳ Still need to complete full reorganization per Option 1

**Current State**:

- Multiple competing MultiAgent implementations (clean.py, multi_agent.py, enhanced_v3, enhanced_v4, generic, etc.)
- Supervisor agents have broken imports:
  - `compatibility_bridge.py` → imports from `multi.base` (exists but seems empty)
  - `internal_dynamic_supervisor.py` → imports from `multi.base_multi_agent` (doesn't exist!)
  - `simple_supervisor.py` → imports from `multi.multi_agent` (exists)
  - `dynamic_multi_agent.py` → imports from `multi.base_multi_agent` (doesn't exist!)
- No clear version hierarchy like React agents have

**Proposed Solution** (Option 1):

1. Make `enhanced_multi_agent_v4.py` the new default `MultiAgent`
   - Rename `EnhancedMultiAgentV4` → `MultiAgent`
   - Move to `multi/agent.py` (following React pattern)
2. Keep enhanced features as `MultiAgentV3`
   - Rename `enhanced_multi_agent_v3.py` → `agent_v3.py`
3. Make current `clean.py` the legacy version
   - Rename to `agent_legacy.py`
   - Add deprecation notice
4. Fix all supervisor imports to use new structure
5. Clean up duplicate/experimental implementations

**Benefits**:

- Clear version hierarchy (V4 default, V3 enhanced, legacy deprecated)
- Fixes broken supervisor imports
- Consistent with React agent pattern
- Reduces confusion from 30+ implementations

**Related Files**:

- `/packages/haive-agents/src/haive/agents/multi/` - needs reorganization
- `/packages/haive-agents/src/haive/agents/supervisor/` - needs import fixes
- `/packages/haive-agents/src/haive/agents/multi/experiments/` - needs cleanup

**Priority**: High - broken imports affect supervisor functionality

---

## 📝 Documentation Tasks

### React Agent Documentation

- ✅ Completed - Added comprehensive module docstrings for V4 (default), V3, and legacy
- ✅ Updated `__init__.py` to make ReactAgentV4 the default export

### Multi-Agent Documentation

- ✅ Partially completed - Documented V4 as recommended, clean as default, V3 for generics
- ✅ Created archive structure and moved 10+ experimental files
- ⏳ Full reorganization (Option 1) still pending

### Supervisor Documentation ✅ COMPLETED (2025-01-29)

- ✅ Created `archive/` directory and moved 17 experimental/duplicate files
- ✅ Cleaned up `__init__.py` with focused exports
- ✅ Added comprehensive module docs for SupervisorAgent, DynamicSupervisor, SimpleSupervisor
- ✅ Created archive/README.md explaining archived implementations
- ✅ Final structure: 10 active files (3 main implementations + 7 supporting modules)

### Modular Reorganization ✅ COMPLETED (2025-01-29)

- ✅ Reorganized both multi-agent and supervisor into modular structure
- ✅ Created subdirectories: core/, enhanced/, dynamic/, utils/, state/
- ✅ Maintained 100% backward compatibility with stub files
- ✅ Added STRUCTURE.md files documenting the new organization
- ✅ All imports work both ways (old flat style and new modular style)

### Planning Agent Documentation ✅ COMPLETED (2025-01-29)

- ✅ Updated `__init__.py` with comprehensive module documentation
- ✅ Added detailed documentation to main implementations:
  - clean_plan_execute.py - Marked as recommended for simple tasks
  - proper_plan_execute.py - Marked as advanced for complex tasks
  - rewoo_tree_agent_v3.py - Marked as recommended for research tasks
- ✅ Completely rewrote README.md with patterns, examples, and guidance
- ✅ PLANNING_AGENT_MEMORY_GUIDE.md already provides excellent pattern reference

## 🔧 Code Quality

### Planning Module Organization (Low Priority)

**Note**: The planning module is fairly well organized already but could benefit from:

- Consider archiving `rewoo_tree_agent.py` (V1 superseded by V2 and V3)
- Consider consolidating `p_and_e/` and `plan_and_execute/` directories
- Consider archiving `plan_execute_v3/` if experimental
- Consider consolidating `rewoo_v3/` with main `rewoo/` directory

**Current State**: Module is functional with clear main implementations documented

### Import Structure

- [ ] Ensure all agents use explicit `from haive.agents.X import Y` patterns
- [ ] Remove any relative imports that could cause issues

### Testing

- [ ] Add tests for multi-agent supervisor integration
- [ ] Verify all supervisor imports work after reorganization
