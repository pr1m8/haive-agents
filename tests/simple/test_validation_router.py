"""Test validation router directly to see what it returns"""

import logging
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from haive.core.graph.node.validation_router_v2 import validation_router_v2

# Set up logging to see validation router logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_validation_router_with_pydantic_model():
    """Test validation router with pydantic_model route"""
    
    # Create a mock state similar to what SimpleAgent would have
    state = {
        "messages": [
            HumanMessage(content="Say hello"),
            AIMessage(
                content="I'll help you with that.",
                tool_calls=[
                    {
                        "name": "SimpleResult",
                        "args": {"response": "Hello!", "confidence": 0.9},
                        "id": "call_123"
                    }
                ]
            ),
            # Simulate a successful ToolMessage from ValidationNodeV2
            ToolMessage(
                content='{"response": "Hello!", "confidence": 0.9}',
                tool_call_id="call_123",
                additional_kwargs={
                    "validation_passed": True,
                    "is_error": False
                }
            )
        ],
        "tool_routes": {
            "SimpleResult": "pydantic_model"
        }
    }
    
    print(f"🧪 Testing validation router with pydantic_model route")
    print(f"State messages: {len(state['messages'])}")
    print(f"Tool routes: {state['tool_routes']}")
    
    # Call the validation router
    result = validation_router_v2(state)
    
    print(f"📋 Router result: '{result}'")
    print(f"Expected: 'parse_output'")
    
    if result == "parse_output":
        print("✅ Router correctly routes to parse_output")
    else:
        print(f"❌ Router incorrectly routes to '{result}' instead of 'parse_output'")
    
    return result


def test_validation_router_with_error():
    """Test validation router with error case"""
    
    # Create a mock state with validation error
    state = {
        "messages": [
            HumanMessage(content="Say hello"),
            AIMessage(
                content="I'll help you with that.",
                tool_calls=[
                    {
                        "name": "SimpleResult", 
                        "args": {"response": "Hello!", "confidence": 0.9},
                        "id": "call_456"
                    }
                ]
            ),
            # Simulate a failed ToolMessage from ValidationNodeV2
            ToolMessage(
                content='{"error": "Validation failed", "success": false}',
                tool_call_id="call_456",
                additional_kwargs={
                    "validation_passed": False,
                    "is_error": True
                }
            )
        ],
        "tool_routes": {
            "SimpleResult": "pydantic_model"
        }
    }
    
    print(f"\n🧪 Testing validation router with error case")
    
    # Call the validation router
    result = validation_router_v2(state)
    
    print(f"📋 Router result: '{result}'")
    print(f"Expected: 'agent_node'")
    
    if result == "agent_node":
        print("✅ Router correctly routes to agent_node for errors")
    else:
        print(f"❌ Router incorrectly routes to '{result}' instead of 'agent_node'")
    
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING VALIDATION ROUTER DIRECTLY")
    print("=" * 60)
    
    # Test successful case
    result1 = test_validation_router_with_pydantic_model()
    
    # Test error case  
    result2 = test_validation_router_with_error()
    
    print(f"\n📊 Summary:")
    print(f"  Success case → '{result1}'")
    print(f"  Error case → '{result2}'")