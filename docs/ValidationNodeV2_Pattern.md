# ValidationNodeV2 Pattern - Correct Implementation

**Version**: 1.0  
**Date**: 2025-07-29  
**Status**: Validated and Working

## Overview

The ValidationNodeV2 pattern was correctly implemented in the user's `.v2` branch and represents the proper way to handle conditional tool injection in Haive agents. This pattern solves the key problem of when to create ToolMessages vs when to let tool_node handle execution.

## Key Insight

**The ValidationNodeV2 acts as a conditional router that:**

- Creates ToolMessages for Pydantic models (for validation)
- Does NOT create ToolMessages for regular tools (lets tool_node execute them)

## Core Pattern

### 1. Dynamic Engine Extraction

```python
# Extract engine name from AIMessage attribution
engine_name_from_message = last_message.additional_kwargs.get("engine_name")
if engine_name_from_message:
    self.engine_name = engine_name_from_message
```

### 2. Tool Route Determination

```python
# Get tool routes from engine
tool_routes = engine.tool_routes  # e.g., {"TaskAnalysis": "pydantic_model", "calculator": "langchain_tool"}
route = tool_routes.get(tool_name, "unknown")
```

### 3. Conditional Tool Processing

```python
if route == "pydantic_model":
    # Create ToolMessage for Pydantic validation
    tool_msg = self._create_tool_message_for_pydantic(...)
    new_tool_messages.append(tool_msg)
elif route in ["langchain_tool", "function", "tool_node"]:
    # Let tool_node handle it - no ToolMessage here
    logger.debug(f"Regular tool {tool_name} will be handled by tool_node")
```

## Validation Results (Test Confirmed)

### ✅ Test Case 1: Pydantic Model (TaskAnalysis)

- **Input**: Tool call for "TaskAnalysis" with route "pydantic_model"
- **Result**: ✅ Creates ToolMessage with validation results
- **Content**: `{"success": true, "validated": true, "data": {...}}`

### ✅ Test Case 2: LangChain Tool (calculator)

- **Input**: Tool call for "calculator" with route "langchain_tool"
- **Result**: ✅ No ToolMessage created (correct behavior)
- **Flow**: Routes to tool_node for actual execution

### ✅ Test Case 3: Mixed Tool Calls

- **Input**: Both TaskAnalysis + calculator in same message
- **Result**: ✅ Only TaskAnalysis gets ToolMessage, calculator handled by tool_node

## Implementation Details

### Tool Routes Configuration

```python
engine.tool_routes = {
    "TaskAnalysis": "pydantic_model",      # → Create ToolMessage
    "calculator": "langchain_tool",        # → Let tool_node handle
    "search_tool": "langchain_tool",       # → Let tool_node handle
    "unknown_tool": "unknown"             # → Create error ToolMessage
}
```

### Engine Structure Requirements

```python
engine = AugLLMConfig(
    structured_output_model=TaskAnalysis,  # Pydantic model for validation
    tools=[calculator, search_tool],       # LangChain tools
    tool_routes={...}                      # Route mapping
)
engine.schemas = [TaskAnalysis]  # Additional schemas for validation
```

### State Structure

```python
state = {
    "messages": [...],
    "engines": {"engine_name": engine},
    "tool_routes": engine.tool_routes,
    "engine_name": "engine_name"
}
```

## Why This Pattern Works

1. **Type Safety**: Pydantic models get validated before downstream processing
2. **Performance**: Regular tools execute directly without validation overhead
3. **Flexibility**: Different engines can have different tool routing strategies
4. **Error Handling**: Validation errors create proper ToolMessages with error details
5. **Composability**: Works seamlessly with multi-agent workflows

## Integration with Agents

### SimpleAgentV3 Usage (Already Implemented)

```python
# Uses ValidationNodeConfigV2 (same pattern)
validation_config = ValidationNodeConfigV2(
    name="validation",
    engine_name=engine_name,
    tool_node="tool_node" if needs_tools else None,
    parser_node="parse_output" if needs_parsing else None,
)
```

### Tool Route Discovery

```python
# Routes are automatically configured by AugLLMConfig based on:
# - structured_output_model → "pydantic_model"
# - tools list → "langchain_tool"
# - Custom routes can be added manually
```

## Testing Pattern

```python
def test_validation_node_pattern():
    """Test the core ValidationNodeV2 pattern."""
    node = ValidationNodeV2(name="test", router_node="router")

    # Pydantic model should create ToolMessage
    result = node(state_with_pydantic_call)
    assert len(result.update["messages"]) > 0  # New ToolMessage created

    # LangChain tool should NOT create ToolMessage
    result = node(state_with_langchain_call)
    assert len(result.update["messages"]) == 0  # No new messages
```

## Files Implementing This Pattern

- **Core Implementation**: `packages/haive-core/src/haive/core/graph/node/validation_node_v2.py`
- **Config Version**: `packages/haive-core/src/haive/core/graph/node/validation_node_config_v2.py`
- **Agent Integration**: `packages/haive-agents/src/haive/agents/simple/agent_v3.py`
- **Test Suite**: `packages/haive-agents/tests/test_validation_node_v2_comprehensive.py`

## Summary

The ValidationNodeV2 pattern is the correct solution for conditional tool injection:

- **Pydantic models** get ToolMessages for validation
- **Regular tools** go directly to tool_node for execution
- **Dynamic engine attribution** supports multi-engine workflows
- **Error handling** creates appropriate error ToolMessages

This pattern enables proper structured output validation while maintaining efficient tool execution performance.
