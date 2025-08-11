#!/usr/bin/env python3
"""Debug ValidationNodeConfigV2 behavior with Plan[Task]."""

import json
from typing import List
from pydantic import BaseModel, Field
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from haive.core.graph.node.validation_node_config_v2 import ValidationNodeConfigV2
from haive.core.engine.aug_llm import AugLLMConfig

print("\n" + "="*80)
print("DEBUGGING VALIDATION NODE WITH Plan[Task]")
print("="*80)

# Define models
class Task(BaseModel):
    description: str
    priority: int = 1

class Plan[T](BaseModel):
    objective: str
    steps: List[T]

def test_validation_node_directly():
    """Test ValidationNodeConfigV2 directly with Plan[Task]."""
    print("\n1️⃣ Direct ValidationNodeConfigV2 Test")
    print("-" * 40)
    
    # Create engine with Plan[Task]
    engine = AugLLMConfig(structured_output_model=Plan[Task])
    
    print(f"Engine tools: {[getattr(t, 'name', str(t)) for t in engine.tools]}")
    print(f"Tool routes: {engine.tool_routes}")
    print(f"Available tool names: {list(engine.tool_routes.keys())}")
    
    # Create validation node
    val_node = ValidationNodeConfigV2(
        name="test_validation",
        engine_name="test_engine"
    )
    
    # Create state with tool call using sanitized name
    messages = [
        HumanMessage(content="Create a plan"),
        AIMessage(
            content="",
            tool_calls=[{
                "id": "call_123",
                "name": "plan_task_generic",  # Sanitized name
                "args": {
                    "objective": "Test plan",
                    "steps": [
                        {"description": "Step 1", "priority": 1}
                    ]
                }
            }]
        )
    ]
    
    state = {
        "messages": messages,
        "engines": {"test_engine": engine},
        "engine_name": "test_engine"
    }
    
    print(f"\nTool call name: plan_task_generic")
    print(f"Available in routes: {'plan_task_generic' in engine.tool_routes}")
    
    # Try to get the schema
    try:
        # This is what happens inside ValidationNodeConfigV2
        tool_name = "plan_task_generic"
        route = engine.tool_routes.get(tool_name)
        print(f"\nRoute for {tool_name}: {route}")
        
        if route == "parse_output":
            # Try to find the schema
            print("\nLooking for schema...")
            
            # Check if it's the structured output model
            if hasattr(engine, 'structured_output_model'):
                model = engine.structured_output_model
                model_name = getattr(model, '__name__', 'Unknown')
                print(f"Structured output model name: {model_name}")
                
                # This is the problem - names don't match!
                if model_name == tool_name:
                    print("✅ Names match!")
                else:
                    print(f"❌ Name mismatch: {model_name} != {tool_name}")
                    
                    # Check if sanitized name matches
                    from haive.core.utils.naming import sanitize_tool_name
                    sanitized = sanitize_tool_name(model_name)
                    print(f"Sanitized model name: {sanitized}")
                    if sanitized == tool_name:
                        print("✅ Sanitized name matches tool call!")
        
        # Execute validation node
        print("\nExecuting validation node...")
        result = val_node(state)
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

def test_schema_lookup_issue():
    """Test the schema lookup issue in LangGraph's ValidationNode."""
    print("\n\n2️⃣ Schema Lookup Issue")
    print("-" * 40)
    
    # This simulates what happens in LangGraph's ValidationNode
    schemas_by_name = {}
    
    # When ValidationNode processes schemas
    model = Plan[Task]
    model_name = getattr(model, '__name__', 'Unknown')
    schemas_by_name[model_name] = model
    
    print(f"Schemas registered: {list(schemas_by_name.keys())}")
    
    # When LLM calls with sanitized name
    tool_call_name = "plan_task_generic"
    
    print(f"\nLooking up: {tool_call_name}")
    if tool_call_name in schemas_by_name:
        print("✅ Found directly")
    else:
        print("❌ Not found - this causes KeyError!")
        
        # Our fix would check sanitized names
        print("\nChecking with sanitization...")
        from haive.core.utils.naming import sanitize_tool_name
        
        for schema_name, schema in schemas_by_name.items():
            sanitized = sanitize_tool_name(schema_name)
            print(f"  {schema_name} -> {sanitized}")
            if sanitized == tool_call_name:
                print(f"  ✅ Match found via sanitization!")
                break

def test_fix_approaches():
    """Test different approaches to fix the issue."""
    print("\n\n3️⃣ Fix Approaches")
    print("-" * 40)
    
    print("Approach 1: Register both names in tool_routes")
    engine = AugLLMConfig(structured_output_model=Plan[Task])
    print(f"Current routes: {engine.tool_routes}")
    print("This already happens - both 'Plan[Task]' and 'plan_task_generic' are registered")
    
    print("\nApproach 2: Update schema lookup in ValidationNodeConfigV2")
    print("Check both original and sanitized names when looking up schemas")
    
    print("\nApproach 3: Use the sanitized name as the primary key")
    print("Register tools with sanitized names from the start")

if __name__ == "__main__":
    test_validation_node_directly()
    test_schema_lookup_issue()
    test_fix_approaches()