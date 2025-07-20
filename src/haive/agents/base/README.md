# Base Agent Components

Core components and utilities for building agents in the Haive framework.

## Overview

This module provides the foundation for all agent implementations:

- **Agent**: Base class for all agents with engine-focused generics
- **Hooks**: Comprehensive lifecycle event system
- **Mixins**: Reusable functionality (persistence, execution, state management)
- **Types**: Core type definitions and protocols
- **Utilities**: Debug helpers and serialization support

## Key Components

### Classes

- **Agent**: Abstract base class with engine generics, state management, and graph building
- **HooksMixin**: Provides lifecycle event injection points
- **CompiledAgent**: Pre-compiled agent with optimized performance
- **EnhancedAgent**: Agent with additional features like token tracking
- **TypedAgent**: Strongly-typed agent with schema validation

### Hooks System

The hooks system allows injection of custom logic at various points in agent execution:

```python
from haive.agents.base.hooks import HookEvent, timing_hook, logging_hook
from haive.agents.simple import SimpleAgent

# Create agent and add hooks
agent = SimpleAgent(name="my_agent")
agent.add_hook(HookEvent.BEFORE_RUN, timing_hook)
agent.add_hook(HookEvent.AFTER_RUN, timing_hook)
agent.add_hook(HookEvent.ON_ERROR, logging_hook)

# Or use decorators
@agent.before_run
def my_custom_hook(context):
    print(f"Starting execution: {context.input_data}")
```

### Available Hook Events

- `BEFORE_SETUP` / `AFTER_SETUP` - Agent initialization
- `BEFORE_BUILD_GRAPH` / `AFTER_BUILD_GRAPH` - Graph construction
- `BEFORE_RUN` / `AFTER_RUN` - Execution lifecycle
- `ON_ERROR` - Error handling
- `ON_RETRY` - Retry attempts
- `BEFORE_STATE_UPDATE` / `AFTER_STATE_UPDATE` - State changes
- `BEFORE_TOOL_CALL` / `AFTER_TOOL_CALL` - Tool execution

### Common Hooks

- `logging_hook` - Log all events with structured data
- `timing_hook` - Track execution time between events
- `state_validation_hook` - Validate state updates
- `retry_limit_hook(max_retries)` - Limit retry attempts

### Mixins

- **ExecutionMixin**: Async/sync execution patterns
- **PersistenceMixin**: State saving and loading
- **StateMixin**: State management abstractions
- **HooksMixin**: Hook registration and execution

## Installation

This module is part of the `haive-agents` package. Install it using:

```bash
pip install haive-agents
```

## Usage Examples

### Basic Agent Creation

```python
from haive.agents.base import Agent
from haive.core.engine.aug_llm import AugLLMConfig

class MyAgent(Agent):
    """Custom agent implementation."""

    def build_graph(self) -> BaseGraph:
        """Build the agent's execution graph."""
        # Implementation here
        pass
```

### Using Hooks

```python
# Add lifecycle hooks
agent = SimpleAgent(name="monitored_agent")

# Track execution time
agent.add_hook(HookEvent.BEFORE_RUN, timing_hook)
agent.add_hook(HookEvent.AFTER_RUN, timing_hook)

# Custom validation
@agent.before_state_update
def validate_messages(context):
    if "messages" not in context.state:
        raise ValueError("State must contain messages")

# Execute with hooks
result = await agent.arun("Process this data")
```

### Using Mixins

```python
from haive.agents.base.mixins import PersistenceMixin, StateMixin

class PersistentAgent(Agent, PersistenceMixin, StateMixin):
    """Agent with automatic state persistence."""

    def after_run(self, result):
        # Automatically save state after each run
        self.save_state()
        return result
```

## Testing

```bash
# Run base module tests
poetry run pytest packages/haive-agents/tests/base/

# Run hook tests specifically
poetry run pytest packages/haive-agents/tests/base/test_hooks.py -v

# Run mixin tests
poetry run pytest packages/haive-agents/tests/base/test_mixins.py -v
```

## API Reference

For detailed API documentation, see the [API Reference](../../../docs/source/api/base/index.rst).

## See Also

- [`base.mixins`](./mixins/): Reusable agent functionality
- [SimpleAgent](../simple/README.md) - Basic agent implementation
- [ReactAgent](../react/README.md) - ReAct pattern agent
- [MultiAgent](../multi/README.md) - Multi-agent coordinator
