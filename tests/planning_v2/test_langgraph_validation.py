#!/usr/bin/env python3
"""Test LangGraph ValidationNode directly to understand the issue."""

import asyncio
from haive.agents.planning_v2.base.models import Plan, Task
from langchain_core.messages import AIMessage
from langgraph.prebuilt import ValidationNode

def test_langgraph_validation():
    """Test LangGraph ValidationNode directly."""
    print("\n🔍 TESTING LANGGRAPH VALIDATION")
    print("="*60)
    
    # Create the model
    model = Plan[Task]
    print(f"Model: {model}")
    print(f"Model name: {model.__name__}")
    
    # Create ValidationNode with the model
    print("\nCreating ValidationNode...")
    try:
        validation_node = ValidationNode(schemas=[model])
        print("✅ ValidationNode created successfully")
    except Exception as e:
        print(f"❌ Failed to create ValidationNode: {e}")
        return
    
    # Create test state with tool call
    state = {
        "messages": [
            AIMessage(
                content="",
                tool_calls=[{
                    "id": "test_id",
                    "name": "plan_task_generic",  # Sanitized name
                    "args": {
                        "objective": "Build a simple REST API",
                        "steps": [
                            {"objective": "Set up project"},
                            {"objective": "Create endpoints"}
                        ]
                    }
                }]
            )
        ]
    }
    
    print("\nInvoking ValidationNode...")
    try:
        result = validation_node.invoke(state)
        print("✅ Validation succeeded!")
        print(f"Result type: {type(result)}")
        print(f"Result keys: {result.keys() if isinstance(result, dict) else 'Not a dict'}")
        
        if isinstance(result, dict) and 'messages' in result:
            print(f"\nAdded messages:")
            for msg in result['messages']:
                print(f"  - {type(msg).__name__}: {msg}")
                
    except Exception as e:
        print(f"❌ Validation failed: {type(e).__name__}")
        print(f"Error: {e}")
        
        # Try to understand what went wrong
        import traceback
        print("\nTraceback:")
        traceback.print_exc()


if __name__ == "__main__":
    test_langgraph_validation()