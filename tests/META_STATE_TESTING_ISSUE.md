# MetaStateSchema Testing Issue - Context and Analysis

## Issue Summary

We're trying to test MetaStateSchema with real agent nodes to validate state hierarchy concepts (Phase 1, Task 1 of our action plan). The test is failing during agent creation due to unexpected persistence initialization.

## Core Problem

When creating a SimpleAgent for testing MetaStateSchema embedding, the agent automatically initializes PostgreSQL persistence, which causes the test to fail. This suggests there's mandatory persistence initialization happening in the agent lifecycle that we need to understand.

## Key Files and Context

### 1. **Test File Being Created**

- **Path**: `/packages/haive-agents/tests/test_meta_state_with_agents.py`
- **Purpose**: Test MetaStateSchema with real agents to validate:
  - Agents can be embedded in state
  - Embedded agents can be executed from within state
  - Recompilable mixin works with real graph changes
  - Dynamic tool routing works in practice

### 2. **MetaStateSchema Implementation**

- **Path**: `/packages/haive-core/src/haive/core/schema/prebuilt/meta_state.py`
- **Key Features**:

  ```python
  class MetaStateSchema(MessagesState):
      agent: Any | None = Field(default=None, description="Contained agent for meta execution")
      agent_state: dict[str, Any] = Field(default_factory=dict)
      meta_context: dict[str, Any] = Field(default_factory=dict)  # Note: NOT 'meta'

      def execute_agent(self, input_data, config, update_state=True):
          """Execute the contained agent with given input"""
  ```

### 3. **SimpleAgent Implementation**

- **Path**: `/packages/haive-agents/src/haive/agents/simple/agent.py`
- **Issue**: When instantiated, it automatically sets up PostgreSQL persistence
- **Error Output**:
  ```
  INFO     Set up PostgreSQL persistence for haive_test_agent_138746580973072
  INFO     Using PostgresSaverNoPreparedStatements to avoid prepared statement conflicts
  INFO     PostgreSQL connection pool opened successfully
  ```

### 4. **Agent Base Class**

- **Path**: `/packages/haive-agents/src/haive/agents/base/agent.py`
- **Key Lifecycle**:
  ```python
  class Agent(InvokableEngine, ExecutionMixin, StateMixin, PersistenceMixin, ...):
      # Lifecycle: normalize engines → setup_agent() → schema generation → persistence → graph building
  ```

## Secondary Issue Found and Fixed

### MessagesState Token Tracking Bug

- **Issue**: MessagesState had validators trying to access `token_usage` fields that don't exist
- **Location**: `/packages/haive-core/src/haive/core/schema/prebuilt/messages_state.py`
- **Fix Applied**: Removed token tracking validators from base MessagesState (they belong in MessagesStateWithTokenUsage)

## Current Test Failure

### Stack Trace Analysis

```
AssertionError during test_embed_agent_in_meta_state
- SimpleAgent creation triggers full persistence setup
- PostgreSQL connection attempted
- Test environment not configured for database access
```

## Questions Needing Answers

1. **Agent Initialization**: Can we create agents without persistence for testing? Or is persistence fundamental to the agent architecture?

2. **Testing Strategy**: Should we:
   - Mock the persistence layer for MetaStateSchema testing?
   - Set up test database configuration?
   - Create a "TestAgent" that doesn't require persistence?
   - Use a different approach entirely?

3. **MetaStateSchema Design**: Is the current design correct for embedding real agents? The `execute_agent()` method expects agents to have `run()`, `invoke()`, or be callable.

## Related Architecture Context

### From Our Investigation

- **Agent vs AgentLike**: We're designing a distinction where Agent requires AugLLMConfig but AgentLike doesn't
- **Recompilable Mixin**: Exists but not integrated (`/packages/haive-core/src/haive/core/common/mixins/recompile_mixin.py`)
- **Dynamic Tool Routing**: Exists but not widely used (`/packages/haive-core/src/haive/core/common/mixins/dynamic_tool_route_mixin.py`)
- **Multi-Agent State**: Needs shared vs private field mechanism (not yet implemented)

## Recommended Next Steps

1. **Understand Agent Lifecycle**: Review how persistence is initialized and if it can be optional
2. **Determine Testing Approach**: Decide if we need real agents or can use simplified versions
3. **Fix Test Implementation**: Based on decisions above
4. **Continue Phase 1**: Validate state hierarchy concepts with working tests

## Files to Review

1. `/packages/haive-agents/src/haive/agents/base/agent.py` - Agent initialization
2. `/packages/haive-agents/src/haive/agents/base/mixins/persistence_mixin.py` - How persistence works
3. `/packages/haive-agents/tests/test_simple.py` - How other agent tests handle this
4. `/packages/haive-core/src/haive/core/schema/prebuilt/meta_state.py` - Target of our test

## Current Todo Status

From our todo list, we're working on:

- **Test MetaStateSchema with real agent nodes** (HIGH PRIORITY) - BLOCKED by this issue
- Design shared vs private field mechanism (HIGH PRIORITY) - Not started
- Test recompilable mixin with actual graph changes (HIGH PRIORITY) - Not started

The resolution of this testing issue is critical to proceed with validating our architectural concepts.
