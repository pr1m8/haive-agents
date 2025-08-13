#!/usr/bin/env python3
"""Check what the agent_node is actually outputting that causes validation errors."""

import sys
import os

# Add the packages to path  
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_engine_output_directly():
    """Test what AugLLMConfig with structured output actually produces."""
    
    print("🔍 TESTING ENGINE OUTPUT DIRECTLY")
    print("=" * 60)
    
    try:
        from haive.core.engine.aug_llm import AugLLMConfig
        
        # Create engine exactly like SimpleAgent does
        engine = AugLLMConfig(
            structured_output_model=SimpleResult,
            temperature=0.3,
        )
        
        print(f"📋 Engine configuration:")
        print(f"   - force_tool_use: {getattr(engine, 'force_tool_use', 'NOT_SET')}")
        print(f"   - tool_choice_mode: {getattr(engine, 'tool_choice_mode', 'NOT_SET')}")
        print(f"   - tools: {len(engine.tools)} tools")
        print(f"   - tool_routes: {engine.tool_routes}")
        print(f"   - structured_output_model: {engine.structured_output_model}")
        
        # Create input like agent_node would
        input_data = {
            "messages": [{"role": "user", "content": "What is 2+2?"}]
        }
        
        print(f"\n🎯 Calling engine directly...")
        print(f"   Input: {input_data}")
        
        # Call engine directly
        result = engine.invoke(input_data)
        
        print(f"\n✅ Engine result:")
        print(f"   - Type: {type(result)}")
        print(f"   - Content: {result.content}")
        print(f"   - Tool calls: {getattr(result, 'tool_calls', None)}")
        
        # Examine tool calls in detail
        if hasattr(result, 'tool_calls') and result.tool_calls:
            print(f"\n📋 TOOL CALL ANALYSIS:")
            for i, tool_call in enumerate(result.tool_calls):
                print(f"   [Tool Call {i}]:")
                print(f"      - name: {tool_call.get('name')}")
                print(f"      - id: {tool_call.get('id')}")
                print(f"      - args: {tool_call.get('args')}")
                print(f"      - type: {tool_call.get('type')}")
                
                # Check if args are valid for SimpleResult
                args = tool_call.get('args', {})
                print(f"\n   📋 Validating args against SimpleResult:")
                try:
                    validated = SimpleResult(**args)
                    print(f"      ✅ ARGS ARE VALID: {validated}")
                    print(f"      This should create a SUCCESS ToolMessage")
                except Exception as e:
                    print(f"      ❌ ARGS ARE INVALID: {e}")
                    print(f"      This would create an ERROR ToolMessage")
        
        return result
        
    except Exception as e:
        print(f"❌ Error testing engine: {e}")
        import traceback
        traceback.print_exc()
        return None


def test_validation_with_real_output():
    """Test ValidationNodeV2 with the actual engine output."""
    
    print(f"\n🔍 TESTING VALIDATION WITH REAL ENGINE OUTPUT")
    print("=" * 60)
    
    # Get real engine output
    engine_result = test_engine_output_directly()
    
    if not engine_result or not hasattr(engine_result, 'tool_calls'):
        print("❌ No tool calls to validate")
        return
    
    try:
        from haive.core.graph.node.validation_node_v2 import ValidationNodeV2
        
        # Create validation node
        validation_node = ValidationNodeV2(
            name="test_validation",
            engine_name="test_engine"
        )
        
        print(f"\n📋 Testing ValidationNodeV2 with real tool calls...")
        
        for i, tool_call in enumerate(engine_result.tool_calls):
            tool_name = tool_call.get('name')
            tool_id = tool_call.get('id', f'test_id_{i}')
            args = tool_call.get('args', {})
            
            print(f"\n   [Tool Call {i}] {tool_name}:")
            print(f"      - args: {args}")
            
            try:
                tool_msg = validation_node._create_tool_message_for_pydantic(
                    tool_name, tool_id, args, SimpleResult
                )
                
                print(f"      ✅ ToolMessage created:")
                print(f"         - content: {tool_msg.content[:200]}...")
                print(f"         - is_error: {tool_msg.additional_kwargs.get('is_error', False)}")
                
                if tool_msg.additional_kwargs.get('is_error', False):
                    print(f"         ❌ ERROR ToolMessage - This causes infinite loop!")
                    print(f"         📋 This is why validation_router_v2 routes back to agent_node")
                else:
                    print(f"         ✅ SUCCESS ToolMessage - This should work")
                    
            except Exception as e:
                print(f"      ❌ Error in validation: {e}")
        
    except Exception as e:
        print(f"❌ Error testing validation: {e}")


def main():
    """Run engine output analysis."""
    
    print("🔬 AGENT NODE OUTPUT ANALYSIS")
    print("=" * 80)
    
    # Test engine output
    engine_result = test_engine_output_directly()
    
    # Test validation with real output
    test_validation_with_real_output()
    
    print(f"\n" + "=" * 80)
    print("🎯 HYPOTHESIS:")
    print("If the engine produces tool calls with invalid args,")
    print("ValidationNodeV2 creates error ToolMessages,")
    print("validation_router_v2 routes back to agent_node,")
    print("causing the infinite loop we observed.")
    
    print(f"\n📋 KEY QUESTIONS:")
    print("1. Are the tool call args from the engine valid for SimpleResult?")
    print("2. If not, why is the engine producing invalid args?") 
    print("3. Is there a mismatch between tool schema and model schema?")


if __name__ == "__main__":
    main()