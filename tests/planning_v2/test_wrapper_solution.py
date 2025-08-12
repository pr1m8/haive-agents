#!/usr/bin/env python3
"""Test the wrapper solution for LangGraph ValidationNode."""

from langchain_core.messages import AIMessage
from langgraph.prebuilt import ValidationNode

from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.utils.naming import sanitize_tool_name


def test_wrapper_solution():
    """Test creating a wrapper class with the sanitized name."""
    print("\n🔍 TESTING WRAPPER SOLUTION")
    print("="*60)

    # Create the model
    model = Plan[Task]
    original_name = model.__name__
    sanitized_name = sanitize_tool_name(original_name)

    print(f"Original model name: {original_name}")
    print(f"Sanitized name: {sanitized_name}")

    # Create a wrapper class with the sanitized name
    print(f"\nCreating wrapper class '{sanitized_name}'...")

    # For generic types, we need to handle them differently
    # Just create an alias instead of a subclass
    if hasattr(model, "__origin__"):  # It's a generic type like Plan[Task]
        # For generics, we can't subclass directly
        # Instead, create a simple wrapper that references the original
        wrapper_class = model
        # Monkey-patch the __name__ attribute
        wrapper_class.__name__ = sanitized_name
    else:
        # For non-generic types, create a proper subclass
        wrapper_class = type(
            sanitized_name,  # Use the sanitized name
            (model,),  # Inherit from original model
            {"__module__": model.__module__}
        )

    print(f"Wrapper class name: {wrapper_class.__name__}")
    print(f"Is subclass of original: {issubclass(wrapper_class, model)}")

    # Create ValidationNode with the wrapper
    print("\nCreating ValidationNode with wrapper...")
    try:
        validation_node = ValidationNode(schemas=[wrapper_class])
        print("✅ ValidationNode created successfully")
    except Exception as e:
        print(f"❌ Failed to create ValidationNode: {e}")
        return

    # Create test state with tool call using sanitized name
    state = {
        "messages": [
            AIMessage(
                content="",
                tool_calls=[{
                    "id": "test_id",
                    "name": sanitized_name,  # Use sanitized name
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

    print(f"\nInvoking ValidationNode with tool call name: {sanitized_name}")
    try:
        result = validation_node.invoke(state)
        print("✅ Validation succeeded!")
        print(f"Result type: {type(result)}")

        if isinstance(result, dict) and "messages" in result:
            print(f"\nValidation result messages: {len(result['messages'])}")
            for msg in result["messages"]:
                print(f"  - {type(msg).__name__}")
                if hasattr(msg, "content"):
                    print(f"    Content: {msg.content}")
                if hasattr(msg, "tool_call_id"):
                    print(f"    Tool call ID: {msg.tool_call_id}")

    except Exception as e:
        print(f"❌ Validation failed: {type(e).__name__}")
        print(f"Error: {e}")


if __name__ == "__main__":
    test_wrapper_solution()
