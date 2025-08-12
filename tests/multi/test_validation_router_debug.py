#!/usr/bin/env python3
"""Debug what the validation router is actually returning."""

import json
from pydantic import BaseModel, Field
from langchain_core.messages import AIMessage, ToolMessage

from haive.core.graph.node.validation_router_v2 import validation_router_v2


class SimpleResult(BaseModel):
    """Simple structured result."""
    answer: str = Field(description="The answer")


def test_validation_router_with_actual_state():
    """Test validation router with a state that mimics our execution."""
    
    print("🔍 Testing validation router with simulated state...")
    
    # Simulate the state after ValidationNodeV2 processes the tool call
    # This is what the state looks like when validation_router_v2 is called
    
    # Create an AIMessage with tool calls (like the agent produces)
    ai_message = AIMessage(
        content="",
        tool_calls=[{
            "name": "SimpleResult",
            "args": {"answer": "2 + 2 = 4"},
            "id": "call_test123",
            "type": "tool_call"
        }]
    )
    
    # Create a ToolMessage (like ValidationNodeV2 produces)
    tool_message = ToolMessage(
        content='{"answer": "2 + 2 = 4"}',
        name="SimpleResult",
        tool_call_id="call_test123"
    )
    
    # Create the state
    state = {
        "messages": [ai_message, tool_message],
        "tool_routes": {"SimpleResult": "parse_output"},
        # ... other state fields would be here
    }
    
    print(f"   📋 State summary:")
    print(f"     - Messages: {len(state['messages'])}")
    print(f"     - AI message tool calls: {len(ai_message.tool_calls)}")
    print(f"     - Tool routes: {state['tool_routes']}")
    print(f"     - Tool message content: {tool_message.content}")
    
    # Call the validation router
    print(f"\n   🎯 Calling validation_router_v2...")
    result = validation_router_v2(state)
    
    print(f"   ✅ Router returned: '{result}'")
    
    # Test what would happen with an error case
    print(f"\n   🔍 Testing error case...")
    error_tool_message = ToolMessage(
        content='{"error": "validation failed"}',
        name="SimpleResult", 
        tool_call_id="call_test123"
    )
    
    error_state = {
        "messages": [ai_message, error_tool_message],
        "tool_routes": {"SimpleResult": "parse_output"},
    }
    
    error_result = validation_router_v2(error_state)
    print(f"   ✅ Error case returned: '{error_result}'")
    
    return result


if __name__ == "__main__":
    result = test_validation_router_with_actual_state()
    print(f"\n🎯 Final result: '{result}'")
    
    if result == "parse_output":
        print("✅ Router correctly routes to parse_output")
    else:
        print("❌ Router does NOT route to parse_output - this explains the infinite loop")