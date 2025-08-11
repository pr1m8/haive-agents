#!/usr/bin/env python3
"""
Debug the actual tool schema that gets sent to the LLM in V2 mode.
"""

from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)


def debug_tool_schema_in_v2_mode():
    """Debug what tool schema is actually sent to the LLM in V2 mode."""
    print("🔧 DEBUGGING TOOL SCHEMA IN V2 MODE")
    print("=" * 60)
    
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )
    
    print(f"1. Configuration:")
    print(f"   structured_output_version: {config.structured_output_version}")
    print(f"   force_tool_use: {config.force_tool_use}")
    print(f"   tools: {config.tools}")
    
    # Get the runnable to see what gets bound to the LLM
    runnable = config.create_runnable()
    print(f"\n2. Runnable structure:")
    print(f"   Type: {type(runnable)}")
    
    # The runnable should be a sequence with bound tools
    if hasattr(runnable, 'steps'):
        for i, step in enumerate(runnable.steps):
            print(f"   Step {i}: {type(step)}")
            
            # Look for the LLM with bound tools
            if hasattr(step, 'bound'):
                bound_info = step.bound
                print(f"     Bound info: {bound_info}")
            
            if hasattr(step, 'kwargs'):
                kwargs = step.kwargs
                print(f"     Kwargs keys: {list(kwargs.keys())}")
                
                # Check for tools in kwargs
                if 'tools' in kwargs:
                    tools = kwargs['tools']
                    print(f"     Tools count: {len(tools)}")
                    
                    for j, tool in enumerate(tools):
                        print(f"     Tool {j}: {tool.name if hasattr(tool, 'name') else 'no name'}")
                        
                        # Get the tool schema
                        if hasattr(tool, 'get_input_schema'):
                            schema = tool.get_input_schema()
                            print(f"       Tool schema: {schema}")
                        elif hasattr(tool, 'args_schema'):
                            schema = tool.args_schema
                            print(f"       Args schema: {schema}")
                            
                            # If it's a Pydantic model, get the JSON schema
                            if hasattr(schema, 'model_json_schema'):
                                json_schema = schema.model_json_schema()
                                print(f"       JSON Schema:")
                                import json
                                print(json.dumps(json_schema, indent=2))


def test_direct_tool_creation():
    """Test creating the tool directly to see its schema."""
    print(f"\n" + "=" * 60)
    print("🛠️  TESTING DIRECT TOOL CREATION")
    print("=" * 60)
    
    from langchain_core.tools import StructuredTool
    
    try:
        # Try to create a tool with Plan[Task] as schema
        def dummy_function(**kwargs):
            return kwargs
        
        tool = StructuredTool.from_function(
            func=dummy_function,
            name="plan_task_generic",
            description="Create a plan with tasks",
            args_schema=Plan[Task]
        )
        
        print(f"1. Tool created successfully:")
        print(f"   Name: {tool.name}")
        print(f"   Description: {tool.description}")
        
        # Get the input schema
        schema = tool.get_input_schema()
        print(f"   Input schema type: {type(schema)}")
        
        if hasattr(schema, 'model_json_schema'):
            json_schema = schema.model_json_schema()
            print(f"\n2. Tool JSON Schema:")
            import json
            print(json.dumps(json_schema, indent=2))
            
            # Check if the Task reference is preserved
            if '$defs' in json_schema and 'Task' in json_schema['$defs']:
                task_schema = json_schema['$defs']['Task']
                print(f"\n3. ✅ Task schema preserved in tool:")
                print(json.dumps(task_schema, indent=2))
            else:
                print(f"\n3. ❌ Task schema missing from tool!")
        
        return True
        
    except Exception as e:
        print(f"1. ❌ Failed to create tool: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    debug_tool_schema_in_v2_mode()
    success = test_direct_tool_creation()
    
    print(f"\n" + "=" * 60)
    print("🏁 CONCLUSION")
    print("=" * 60)
    
    if success:
        print("✅ Tool creation works - schema should be preserved")
        print("🔍 Need to check why LLM ignores nested Task structure")
    else:
        print("❌ Tool creation fails - fundamental issue with Plan[Task]")