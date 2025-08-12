#!/usr/bin/env python3
"""Test using a tool wrapper for LangGraph ValidationNode."""

from langchain_core.messages import AIMessage
from langchain_core.tools import BaseTool
from langgraph.prebuilt import ValidationNode
from pydantic import BaseModel

from haive.agents.planning_v2.base.models import Plan, Task
from haive.core.utils.naming import sanitize_tool_name


class ToolWrapper(BaseTool):
    """Wrapper to make a Pydantic model look like a tool with the right name."""
    name: str
    description: str = "Wrapper tool"
    args_schema: type[BaseModel]

    def _run(self, *args, **kwargs):
        """This shouldn't be called during validation."""
        raise NotImplementedError("This is just a wrapper for validation")

def test_tool_wrapper():
    """Test using a tool wrapper."""
    print("\n🔍 TESTING TOOL WRAPPER SOLUTION")
    print("="*60)

    # Create the model
    model = Plan[Task]
    original_name = model.__name__
    sanitized_name = sanitize_tool_name(original_name)

    print(f"Original model name: {original_name}")
    print(f"Sanitized name: {sanitized_name}")

    # Create a tool wrapper with the sanitized name
    print(f"\nCreating tool wrapper '{sanitized_name}'...")
    tool_wrapper = ToolWrapper(
        name=sanitized_name,
        description=f"Wrapper for {original_name}",
        args_schema=model
    )

    print(f"Tool name: {tool_wrapper.name}")
    print(f"Args schema: {tool_wrapper.args_schema}")

    # Create ValidationNode with the tool wrapper
    print("\nCreating ValidationNode with tool wrapper...")
    try:
        validation_node = ValidationNode(schemas=[tool_wrapper])
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
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_tool_wrapper()
