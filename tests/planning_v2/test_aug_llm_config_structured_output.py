#!/usr/bin/env python3
"""
Test AugLLMConfig with structured output model Plan[Task] and save the output for validation node debugging.
"""

import json
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


def test_aug_llm_config_structured_output():
    """Test AugLLMConfig with Plan[Task] structured output model."""
    print("🔧 TESTING AugLLMConfig WITH STRUCTURED OUTPUT")
    print("=" * 60)
    
    # Create AugLLMConfig with structured output
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )
    
    print(f"1. AugLLMConfig created:")
    print(f"   structured_output_model: {config.structured_output_model}")
    print(f"   structured_output_version: {config.structured_output_version}")
    print(f"   force_tool_use: {config.force_tool_use}")
    print(f"   tool_routes: {config.tool_routes}")
    
    # Check format instructions
    has_internal = hasattr(config, '_format_instructions_text') and config._format_instructions_text
    print(f"   _format_instructions_text: {'✅' if has_internal else '❌'}")
    if has_internal:
        print(f"   Instructions length: {len(config._format_instructions_text)} chars")
    
    # Get the runnable
    runnable = config.create_runnable()
    print(f"\n2. Runnable created:")
    print(f"   Type: {type(runnable)}")
    
    try:
        print(f"\n3. Testing direct execution...")
        
        # Simple input that should trigger Plan[Task] output
        input_data = {
            "messages": [
                {
                    "role": "user", 
                    "content": "Create a simple plan to organize a birthday party. Include exactly 2 tasks in your plan."
                }
            ]
        }
        
        print(f"   Input: {input_data['messages'][0]['content']}")
        
        # Execute the runnable
        result = runnable.invoke(input_data)
        
        print(f"\n4. EXECUTION RESULTS:")
        print(f"   ✅ Execution completed!")
        print(f"   Result type: {type(result)}")
        
        # Save raw result for debugging
        with open('/tmp/aug_llm_raw_result.json', 'w') as f:
            if hasattr(result, 'model_dump'):
                json.dump(result.model_dump(), f, indent=2)
            else:
                json.dump(str(result), f, indent=2)
        
        print(f"   Raw result saved to: /tmp/aug_llm_raw_result.json")
        
        # Print result details
        if hasattr(result, 'content'):
            print(f"   Content: {result.content}")
        if hasattr(result, 'tool_calls'):
            print(f"   Tool calls: {result.tool_calls}")
        if hasattr(result, 'additional_kwargs'):
            print(f"   Additional kwargs: {result.additional_kwargs}")
        
        # Try to check if it's our Plan[Task] model
        print(f"\n5. STRUCTURED OUTPUT ANALYSIS:")
        if isinstance(result, Plan):
            print(f"   ✅ Result is Plan[Task] instance!")
            print(f"   Objective: {result.objective}")
            print(f"   Steps: {[step.description for step in result.steps]}")
        else:
            print(f"   ⚠️  Result is not Plan[Task], investigating...")
            print(f"   Result attributes: {dir(result)}")
            
            # Check if content contains JSON
            if hasattr(result, 'content'):
                try:
                    content_json = json.loads(result.content)
                    print(f"   Content is JSON: {content_json}")
                    
                    # Try to parse as Plan[Task]
                    plan = Plan[Task](**content_json)
                    print(f"   ✅ Content can be parsed as Plan[Task]!")
                    print(f"   Parsed objective: {plan.objective}")
                    print(f"   Parsed steps: {[step.description for step in plan.steps]}")
                    
                except json.JSONDecodeError:
                    print(f"   Content is not valid JSON")
                except Exception as e:
                    print(f"   Cannot parse as Plan[Task]: {e}")
        
        # Save the result message for validation node debugging
        result_for_validation = {
            "message_type": type(result).__name__,
            "content": getattr(result, 'content', None),
            "tool_calls": getattr(result, 'tool_calls', None),
            "additional_kwargs": getattr(result, 'additional_kwargs', None),
            "raw_result": str(result)
        }
        
        with open('/tmp/validation_node_debug_message.json', 'w') as f:
            json.dump(result_for_validation, f, indent=2, default=str)
        
        print(f"   Message saved for validation debugging: /tmp/validation_node_debug_message.json")
        
        return True, result
        
    except Exception as e:
        print(f"\n❌ EXECUTION FAILED: {e}")
        import traceback
        traceback.print_exc()
        
        # Save error for debugging
        error_info = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "traceback": traceback.format_exc()
        }
        
        with open('/tmp/aug_llm_error.json', 'w') as f:
            json.dump(error_info, f, indent=2)
        
        print(f"   Error saved to: /tmp/aug_llm_error.json")
        return False, None


if __name__ == "__main__":
    success, result = test_aug_llm_config_structured_output()
    
    print(f"\n" + "=" * 60)
    print("🏁 SUMMARY")
    print("=" * 60)
    print(f"AugLLMConfig execution: {'✅' if success else '❌'}")
    
    if success:
        print(f"✅ SUCCESS: AugLLMConfig with Plan[Task] works!")
        print(f"📄 Files saved for validation node debugging:")
        print(f"   - /tmp/aug_llm_raw_result.json")
        print(f"   - /tmp/validation_node_debug_message.json")
    else:
        print(f"❌ FAILED: AugLLMConfig execution failed")
        print(f"📄 Error saved to: /tmp/aug_llm_error.json")