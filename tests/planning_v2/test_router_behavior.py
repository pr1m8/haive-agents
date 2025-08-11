#!/usr/bin/env python3
"""Test validation router behavior directly."""

from typing import List
from pydantic import BaseModel, Field
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from haive.core.graph.node.validation_router_v2 import validation_router_v2

class Task(BaseModel):
    description: str

class Plan[T](BaseModel):
    objective: str
    steps: List[T]

def test_router_directly():
    """Test the validation router directly."""
    print("\n=== TESTING VALIDATION ROUTER DIRECTLY ===\n")
    
    # Create a state that simulates after validation
    state = {
        "messages": [
            HumanMessage(content="Create a plan"),
            AIMessage(
                content="",
                tool_calls=[{
                    "id": "call_123",
                    "name": "plan_task_generic",
                    "args": {"objective": "Test", "steps": []}
                }]
            ),
            ToolMessage(
                content='{"objective":"Test","steps":[]}',
                name="plan_task_generic",
                tool_call_id="call_123",
                additional_kwargs={"is_error": False, "validation_passed": True}
            )
        ],
        "tool_routes": {
            "plan_task_generic": "parse_output"  # This is the route
        }
    }
    
    print("State setup:")
    print(f"- Tool name: plan_task_generic")
    print(f"- Tool route: parse_output")
    print(f"- ToolMessage added: Yes")
    print(f"- ToolMessage is_error: False")
    
    # Call the router
    print("\nCalling validation_router_v2...")
    result = validation_router_v2(state)
    
    print(f"\nRouter result: {result}")
    print("\nExpected: 'parse_output'")
    print(f"Actual: '{result}'")
    
    if result == "parse_output":
        print("\n✅ Router is working correctly!")
    else:
        print("\n❌ Router is NOT routing to parse_output")

if __name__ == "__main__":
    test_router_directly()