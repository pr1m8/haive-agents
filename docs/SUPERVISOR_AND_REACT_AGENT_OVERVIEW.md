# Supervisor and React Agent Overview

## Current State Analysis

### React Agent

**Location**: `/packages/haive-agents/src/haive/agents/react/`

The React Agent is a clean, simple implementation that extends SimpleAgent with looping behavior:

```python
class ReactAgent(SimpleAgent):
    """ReAct agent with looping behavior."""

    def build_graph(self) -> BaseGraph:
        """Build ReAct graph with proper looping."""
        # Inherits from SimpleAgent but modifies graph to loop back
        # instead of ending after tool execution or parsing
```

**Key Features:**

- Extends SimpleAgent for base functionality
- Implements ReAct (Reasoning + Acting) pattern
- Tool execution loops back to agent_node for continued reasoning
- Clean, minimal implementation (~42 lines)

### Supervisor Implementations

We have THREE different supervisor locations:

#### 1. Dynamic Supervisor Package

**Location**: `/packages/haive-agents/src/haive/agents/dynamic_supervisor/`

This appears to be the main, production-ready implementation:

- `agent.py` - Main DynamicSupervisorAgent class
- `state.py` - SupervisorStateWithTools for dynamic agent management
- `tools.py` - Tool creation for handoff/routing
- `models.py` - AgentInfo and related models
- `prompts.py` - Supervisor-specific prompts

**Key Pattern**: Extends ReactAgent and uses tools that execute agents directly.

#### 2. Supervisor Package

**Location**: `/packages/haive-agents/src/haive/agents/supervisor/`

This contains multiple supervisor variants:

- `agent.py` - Basic SupervisorAgent
- `dynamic_supervisor.py` - Another DynamicSupervisorAgent variant
- `integrated_supervisor.py` - IntegratedDynamicSupervisor
- Multiple test and example files mixed in

**Issues**: Contains ~25+ files with tests, examples, and implementations mixed together.

#### 3. Experiments Folder

**Location**: `/packages/haive-agents/src/haive/agents/experiments/supervisor/`

Contains experimental implementations including:

- `three_agent_inactive_test.py` - The file you mentioned
- `clean_dynamic_supervisor.py` - A clean implementation using agent execution node pattern
- ~39 test/debug files
- Multiple experimental patterns

## Key Patterns Identified

### 1. Tool-Based Agent Execution

The main pattern uses tools that execute agents directly:

```python
@tool
def transfer_to_agent(task: str) -> str:
    """Transfer task to specific agent."""
    result = await agent.arun(task)
    return f"Agent response: {result}"
```

### 2. Agent Execution Node Pattern

An alternative pattern from experiments uses a dedicated node:

```python
# Supervisor decides routing
state.agent_route = "math_agent"

# Agent execution node runs the selected agent
async def _agent_execution_node(state):
    agent = registry.get_active_agent(state.agent_route)
    result = await agent.arun(state.current_task)
```

### 3. Dynamic Agent Management

All implementations support:

- Adding/removing agents at runtime
- Activating/deactivating agents
- Capability-based routing
- Agent registry management

## Recommendations

### 1. Use the Main Dynamic Supervisor

The implementation in `/packages/haive-agents/src/haive/agents/dynamic_supervisor/` appears to be the most complete and production-ready.

### 2. Clean Up Structure

The `/packages/haive-agents/src/haive/agents/supervisor/` folder needs organization:

- Move test files to proper test locations
- Move examples to an examples folder
- Keep only core implementation files

### 3. Archive Experiments

The experiments folder contains valuable patterns but should be:

- Documented for reference
- Key patterns extracted to main implementations
- Test files moved to proper test directories

### 4. Testing Organization

Current test locations:

- `/packages/haive-agents/tests/test_dynamic_supervisor/` - Proper location
- `/packages/haive-agents/tests/supervisor/` - Proper location
- Mixed in with source code - Need to be moved

## Next Steps

1. **Document the main dynamic supervisor** usage patterns
2. **Move test files** from source directories to test directories
3. **Extract useful patterns** from experiments
4. **Create clear examples** for common use cases
5. **Clean up the supervisor package** to remove duplication
