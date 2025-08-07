# Structured Output Status Report

**Date**: August 7, 2025  
**Issue**: `structured_output_version="v2"` fails with "Unknown Pydantic model" error  
**Status**: 🔴 **BROKEN** - Bug identified in SimpleAgentV3

## 🔍 Root Cause Analysis

### The Problem

When `structured_output_version="v2"` is used in SimpleAgentV3:

1. Pydantic model is added as a tool with route `'pydantic_model'`
2. `force_tool_use=True` and `force_tool_choice='ModelName'` are set
3. Agent tries to call the model as if it were a tool
4. Validation node fails with "Unknown Pydantic model: ModelName"

### Why It Fails

The validation node (`ValidationNodeConfigV2`) looks for the model class in its `pydantic_models` dictionary, but SimpleAgentV3's `_add_validation_nodes()` method doesn't pass the models:

```python
# In SimpleAgentV3._add_validation_nodes()
validation_config = ValidationNodeConfigV2(**validation_kwargs)  # ❌ No pydantic_models!
```

Should be:

```python
validation_kwargs["pydantic_models"] = {
    model.__name__: model for model in self.engine.pydantic_tools
}
```

## 🧪 Testing Results

### ✅ What Works

- `structured_output_version="v1"` (parser-based) - **WORKS**
- No version specified (defaults to v1) - **WORKS**
- Manual extraction from tool calls in messages - **WORKS**

### ❌ What's Broken

- `structured_output_version="v2"` in SimpleAgentV3 - **FAILS**
- Both single agents and multi-agent workflows affected
- Error: "Unknown Pydantic model: ModelName"

## 🔧 Quick Fixes

### Option 1: Use v1 (Immediate)

```python
agent = SimpleAgentV3(
    name="analyzer",
    engine=AugLLMConfig(
        structured_output_model=MyModel
        # Don't specify structured_output_version - defaults to v1
    )
)
```

### Option 2: Extract from Messages

```python
# After running agent, extract from tool calls
def extract_from_tool_calls(messages, model_class):
    for msg in reversed(messages):
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for call in msg.tool_calls:
                if call.get("name") == model_class.__name__:
                    return model_class(**call.get("args", {}))
```

### Option 3: Fix ValidationNodeConfigV2 (Code Change Needed)

Modify SimpleAgentV3's `_add_validation_nodes()` to pass pydantic models.

## 🎯 Impact on Multi-Agent Workflows

- **Multi-agent workflows are NOT the problem**
- **SimpleAgentV3 v2 structured output is broken**
- **Single agents also fail with same error**
- **Use v1 for now, works perfectly in multi-agent**

## 📊 Postgres Error (Secondary Issue)

The test also had postgres unique constraint error:

```
psycopg.errors.UniqueViolation: duplicate key value violates unique constraint "threads_id_key"
```

This is a separate persistence issue, not related to structured output.

## 🚀 Next Steps

1. **Immediate**: Use v1 structured output for multi-agent workflows ✅
2. **Short-term**: Fix SimpleAgentV3 validation node to support v2
3. **Long-term**: Add tests to prevent regression

## 💡 Key Insight

**The "Unknown Pydantic model" error is a SimpleAgentV3 bug, not a multi-agent workflow limitation. Multi-agent workflows work fine with structured output when using v1 (parser-based) approach.**
