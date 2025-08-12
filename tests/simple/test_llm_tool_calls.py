"""Test what LLM generates for tool calls and test the full validation chain"""

from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_node_v2 import ValidationNodeV2
from haive.core.graph.node.validation_router_v2 import validation_router_v2


class SimpleResult(BaseModel):
    """Simple structured output."""
    response: str = Field(description="Response to the input")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in response")


def test_llm_tool_call_generation():
    """Test what the LLM generates for tool calls"""
    
    # Create engine with structured output
    engine = AugLLMConfig(
        structured_output_model=SimpleResult,
        temperature=0.1,
        max_tokens=100
    )
    
    print(f"🧪 Testing LLM tool call generation")
    print(f"Engine config:")
    print(f"  - force_tool_use: {engine.force_tool_use}")
    print(f"  - force_tool_choice: {engine.force_tool_choice}")
    print(f"  - tool_routes: {engine.tool_routes}")
    
    # Create a runnable and invoke it
    try:
        runnable = engine.create_runnable()
        
        # Invoke with a simple message
        from langchain_core.messages import HumanMessage
        messages = [HumanMessage(content="Say hello")]
        
        print(f"\n🚀 Invoking LLM...")
        
        result = runnable.invoke({"messages": messages})
        
        print(f"\n📋 LLM Result:")
        print(f"  - Type: {type(result)}")
        print(f"  - Content: '{result.content}'")
        
        if hasattr(result, 'tool_calls') and result.tool_calls:
            print(f"  - Tool calls: {len(result.tool_calls)}")
            for i, tool_call in enumerate(result.tool_calls):
                print(f"    [{i}] Name: {tool_call.get('name')}")
                print(f"    [{i}] Args: {tool_call.get('args')}")
                print(f"    [{i}] ID: {tool_call.get('id')}")
        else:
            print(f"  - Tool calls: None")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error invoking LLM: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_validation_chain():
    """Test the full validation chain with real LLM output"""
    
    print(f"\n{'='*60}")
    print("TESTING FULL VALIDATION CHAIN")
    print('='*60)
    
    # Generate real LLM response
    llm_result = test_llm_tool_call_generation()
    if not llm_result or not llm_result.tool_calls:
        print("❌ No tool calls to validate")
        return
    
    # Create state similar to SimpleAgent
    from langchain_core.messages import HumanMessage
    state = {
        "messages": [
            HumanMessage(content="Say hello"),
            llm_result  # Add the AI message with tool calls
        ],
        "tool_routes": {"SimpleResult": "pydantic_model"},
        "tool_metadata": {"SimpleResult": {"class_name": "SimpleResult", "tool_type": "pydantic_model"}},
        "engines": {"main": AugLLMConfig(structured_output_model=SimpleResult)}
    }
    
    print(f"\n🧪 Testing ValidationNodeV2...")
    
    try:
        # Create validation node directly
        validation_node = ValidationNodeV2(
            name="validation",
            engine_name="main",
            parser_node="parse_output"
        )
        
        # Run validation
        print("🚀 Running validation...")
        result = validation_node(state)
        
        # ValidationNodeV2 returns a Command, we need to get the updated state
        # For testing purposes, let's manually call the processing
        print(f"Validation node returned: {result}")
        
        # Let's manually process the validation to see what happens
        updated_state = state.copy()
        
        # Get the last AI message and process tool calls
        last_message = updated_state['messages'][-1]
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            print("Processing tool calls manually...")
            
            # Simulate what ValidationNodeV2 does
            for tool_call in last_message.tool_calls:
                tool_name = tool_call.get('name')
                tool_args = tool_call.get('args', {})
                tool_id = tool_call.get('id')
                
                print(f"  Processing tool call: {tool_name} with args {tool_args}")
                
                # Try to validate with SimpleResult
                try:
                    validated_result = SimpleResult(**tool_args)
                    print(f"  ✅ Validation passed: {validated_result}")
                    
                    # Create success ToolMessage
                    from langchain_core.messages import ToolMessage
                    import json
                    
                    success_content = {
                        "success": True,
                        "result": validated_result.model_dump()
                    }
                    
                    tool_message = ToolMessage(
                        content=json.dumps(success_content, indent=2),
                        tool_call_id=tool_id,
                        name=tool_name,
                        additional_kwargs={
                            "validation_passed": True,
                            "is_error": False
                        }
                    )
                    
                    updated_state['messages'].append(tool_message)
                    
                except Exception as e:
                    print(f"  ❌ Validation failed: {e}")
                    
                    # Create error ToolMessage
                    from langchain_core.messages import ToolMessage
                    import json
                    
                    error_content = {
                        "success": False,
                        "error": str(e)
                    }
                    
                    tool_message = ToolMessage(
                        content=json.dumps(error_content, indent=2),
                        tool_call_id=tool_id,
                        name=tool_name,
                        additional_kwargs={
                            "validation_passed": False,
                            "is_error": True
                        }
                    )
                    
                    updated_state['messages'].append(tool_message)
        
        print(f"\n📋 Validation Results:")
        print(f"  - Messages before: {len(state['messages'])}")
        print(f"  - Messages after: {len(updated_state['messages'])}")
        
        # Check if ToolMessages were added
        new_messages = updated_state['messages'][len(state['messages']):]
        if new_messages:
            print(f"  - New ToolMessages: {len(new_messages)}")
            for i, msg in enumerate(new_messages):
                print(f"    [{i}] Type: {type(msg).__name__}")
                if hasattr(msg, 'content'):
                    print(f"    [{i}] Content: {msg.content[:100]}...")
                if hasattr(msg, 'additional_kwargs'):
                    print(f"    [{i}] Additional kwargs: {msg.additional_kwargs}")
        else:
            print(f"  - New ToolMessages: 0")
        
        # Now test the router
        print(f"\n🧪 Testing validation router...")
        router_result = validation_router_v2(updated_state)
        print(f"📋 Router decision: '{router_result}'")
        
        if router_result == "parse_output":
            print("✅ Validation succeeded - should route to parse_output")
        elif router_result == "agent_node":
            print("❌ Validation failed - routing back to agent_node (this causes the loop!)")
        else:
            print(f"⚠️ Unexpected router result: {router_result}")
            
        return router_result
        
    except Exception as e:
        print(f"\n❌ Error in validation chain: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING LLM TOOL CALLS AND VALIDATION")
    print("=" * 60)
    
    # Test LLM generation
    llm_result = test_llm_tool_call_generation()
    
    # Test full validation chain
    validation_result = test_validation_chain()