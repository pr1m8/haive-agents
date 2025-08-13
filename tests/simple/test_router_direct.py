#!/usr/bin/env python3
"""Test validation_router_v2 directly with simulated state."""

import sys
import os
import json

# Add the packages to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from pydantic import BaseModel, Field
from langchain_core.messages import AIMessage, ToolMessage


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def create_successful_state():
    """Create a state that should route to parse_output."""
    
    # AIMessage with tool call (what agent_node produces)
    ai_message = AIMessage(
        content="",
        tool_calls=[{
            "name": "SimpleResult",
            "args": {"answer": "4"},
            "id": "call_test123",
            "type": "tool_call"
        }]
    )
    
    # Successful ToolMessage (what ValidationNodeV2 should create)
    tool_message = ToolMessage(
        content='{"answer": "4"}',
        name="SimpleResult",
        tool_call_id="call_test123",
        additional_kwargs={
            "is_error": False,
            "validation_passed": True
        }
    )
    
    state = {
        "messages": [ai_message, tool_message],
        "tool_routes": {"SimpleResult": "parse_output"}
    }
    
    return state


def create_error_state():
    """Create a state that should route to agent_node."""
    
    # AIMessage with tool call
    ai_message = AIMessage(
        content="",
        tool_calls=[{
            "name": "SimpleResult", 
            "args": {"answer": "invalid"},
            "id": "call_test456",
            "type": "tool_call"
        }]
    )
    
    # Error ToolMessage
    tool_message = ToolMessage(
        content='{"error": "validation failed", "success": false}',
        name="SimpleResult",
        tool_call_id="call_test456",
        additional_kwargs={
            "is_error": True,
            "validation_passed": False
        }
    )
    
    state = {
        "messages": [ai_message, tool_message],
        "tool_routes": {"SimpleResult": "parse_output"}
    }
    
    return state


def test_validation_router_directly():
    """Test validation_router_v2 with different states."""
    
    print("🔍 TESTING VALIDATION_ROUTER_V2 DIRECTLY")
    print("=" * 60)
    
    try:
        from haive.core.graph.node.validation_router_v2 import validation_router_v2
        
        # Test 1: Successful state
        print("\n📋 TEST 1: Successful structured output")
        success_state = create_successful_state()
        
        print(f"   State summary:")
        print(f"   - Messages: {len(success_state['messages'])}")
        print(f"   - Tool routes: {success_state['tool_routes']}")
        print(f"   - ToolMessage is_error: {success_state['messages'][1].additional_kwargs.get('is_error')}")
        
        result1 = validation_router_v2(success_state)
        print(f"   🎯 Router result: '{result1}'")
        
        if result1 == "parse_output":
            print(f"   ✅ CORRECT: Routes to parse_output for successful validation")
        else:
            print(f"   ❌ WRONG: Should route to parse_output, not '{result1}'")
        
        # Test 2: Error state
        print("\n📋 TEST 2: Error structured output")
        error_state = create_error_state()
        
        print(f"   State summary:")
        print(f"   - Messages: {len(error_state['messages'])}")
        print(f"   - Tool routes: {error_state['tool_routes']}")
        print(f"   - ToolMessage is_error: {error_state['messages'][1].additional_kwargs.get('is_error')}")
        
        result2 = validation_router_v2(error_state)
        print(f"   🎯 Router result: '{result2}'")
        
        if result2 == "agent_node":
            print(f"   ✅ CORRECT: Routes to agent_node for error validation")
        else:
            print(f"   ❌ WRONG: Should route to agent_node, not '{result2}'")
        
        return result1, result2
        
    except Exception as e:
        print(f"❌ Error testing router: {e}")
        import traceback
        traceback.print_exc()
        return None, None


def test_toolmessage_creation():
    """Test how ValidationNodeV2 creates ToolMessages."""
    
    print("\n🔍 TESTING TOOLMESSAGE CREATION")
    print("=" * 60)
    
    try:
        from haive.core.graph.node.validation_node_v2 import ValidationNodeV2
        
        # Create a ValidationNodeV2 instance
        validation_node = ValidationNodeV2(
            name="test_validation",
            engine_name="test_engine"
        )
        
        # Test 1: Valid args
        print("\n📋 TEST 1: Valid args for SimpleResult")
        valid_args = {"answer": "4"}
        
        try:
            tool_msg = validation_node._create_tool_message_for_pydantic(
                "SimpleResult", "call_test123", valid_args, SimpleResult
            )
            
            print(f"   ✅ ToolMessage created:")
            print(f"      - content: {tool_msg.content}")
            print(f"      - additional_kwargs: {tool_msg.additional_kwargs}")
            
            is_error = tool_msg.additional_kwargs.get('is_error', False)
            print(f"      - is_error: {is_error}")
            
            if is_error:
                print(f"      ❌ MARKED AS ERROR - This would cause infinite loop!")
            else:
                print(f"      ✅ MARKED AS SUCCESS - This should work correctly")
            
        except Exception as e:
            print(f"   ❌ Error creating ToolMessage: {e}")
        
        # Test 2: Invalid args
        print("\n📋 TEST 2: Invalid args for SimpleResult")
        invalid_args = {"wrong_field": "value"}
        
        try:
            tool_msg = validation_node._create_tool_message_for_pydantic(
                "SimpleResult", "call_test456", invalid_args, SimpleResult
            )
            
            print(f"   ✅ Error ToolMessage created:")
            print(f"      - content: {tool_msg.content}")
            print(f"      - additional_kwargs: {tool_msg.additional_kwargs}")
            
        except Exception as e:
            print(f"   ❌ Exception during invalid args test: {e}")
        
    except Exception as e:
        print(f"❌ Error testing ToolMessage creation: {e}")
        import traceback
        traceback.print_exc()


def main():
    """Run direct router tests."""
    
    print("🔬 DIRECT VALIDATION ROUTER TESTING")
    print("=" * 80)
    
    # Test router directly
    success_result, error_result = test_validation_router_directly()
    
    # Test ToolMessage creation
    test_toolmessage_creation()
    
    print("\n" + "=" * 80)
    print("🎯 ANALYSIS:")
    print(f"   1. Successful state routes to: {success_result}")
    print(f"   2. Error state routes to: {error_result}")
    
    if success_result == "parse_output":
        print(f"\n✅ ROUTER IS WORKING CORRECTLY")
        print(f"   The issue must be that ValidationNodeV2 is creating ERROR ToolMessages")
        print(f"   when it should be creating SUCCESS ToolMessages")
    else:
        print(f"\n❌ ROUTER IS BROKEN")
        print(f"   The router itself has logic issues")
    
    print(f"\n📋 NEXT STEPS:")
    print(f"   1. Check why ValidationNodeV2 creates error ToolMessages")
    print(f"   2. Check if the args from agent_node are malformed")
    print(f"   3. Check if the model validation is failing")


if __name__ == "__main__":
    main()