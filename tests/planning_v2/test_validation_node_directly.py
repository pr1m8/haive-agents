#!/usr/bin/env python3
"""Test the validation node directly to understand the issue."""

import asyncio
from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.graph.node.validation_node_config_v2 import ValidationNodeConfigV2
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.utils.naming import sanitize_tool_name
from langchain_core.messages import AIMessage


def test_validation_node():
    """Test validation node setup and tool finding."""
    print("\n" + "="*80)
    print("🔍 TESTING VALIDATION NODE DIRECTLY")
    print("="*80)
    
    # Create model and show names
    model_class = Plan[Task]
    original_name = model_class.__name__
    sanitized_name = sanitize_tool_name(original_name)
    
    print(f"\n1. Model Names:")
    print(f"   Original: {original_name}")
    print(f"   Sanitized: {sanitized_name}")
    
    # Create config
    config = AugLLMConfig(
        structured_output_model=model_class,
        temperature=0.3
    )
    
    print(f"\n2. AugLLMConfig Tools:")
    print(f"   Tools: {config.tools}")
    print(f"   Tool type: {type(config.tools[0]) if config.tools else 'None'}")
    print(f"   Tool name: {config.tools[0].__name__ if config.tools else 'None'}")
    print(f"   Tool routes: {config.tool_routes}")
    
    # Create validation node
    validation_node = ValidationNodeConfigV2(
        name="validation",  # Add required name field
        engine_name=config.name,
        tool_node="tool_node",
        parser_node="parse_output"
    )
    
    # Create a mock state with the engine
    state = {
        "messages": [
            AIMessage(
                content="",
                tool_calls=[{
                    "id": "test_id",
                    "name": sanitized_name,  # LLM uses sanitized name
                    "args": {"objective": "Test objective", "steps": []}
                }]
            )
        ],
        "engines": {config.name: config},
        "tool_routes": config.tool_routes
    }
    
    print(f"\n3. Testing tool schema lookup...")
    
    # Call the internal method directly
    schema = validation_node._get_tool_args_schema(sanitized_name, state)
    
    print(f"\n4. Result:")
    print(f"   Found schema: {schema is not None}")
    print(f"   Schema type: {type(schema) if schema else 'None'}")
    print(f"   Is correct model: {schema == model_class if schema else False}")
    
    # Now test with original name too
    print(f"\n5. Testing with original name...")
    schema_orig = validation_node._get_tool_args_schema(original_name, state)
    print(f"   Found schema: {schema_orig is not None}")
    print(f"   Is correct model: {schema_orig == model_class if schema_orig else False}")


if __name__ == "__main__":
    test_validation_node()