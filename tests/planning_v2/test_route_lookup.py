#!/usr/bin/env python3
"""Test route lookup in validation node."""


from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from pydantic import BaseModel

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_node_config_v2 import ValidationNodeConfigV2


print("\n" + "="*80)
print("TESTING ROUTE LOOKUP IN VALIDATION")
print("="*80)

class Task(BaseModel):
    description: str

class Plan[T](BaseModel):
    objective: str
    steps: list[T]

def test_route_lookup():
    """Test how routes are looked up in validation."""
    print("\n1️⃣ Setting up Engine and Validation Node")
    print("-" * 40)

    # Create engine
    engine = AugLLMConfig(structured_output_model=Plan[Task])
    print(f"Engine tool routes: {engine.tool_routes}")

    # Create validation node
    val_node = ValidationNodeConfigV2(
        name="test_validation",
        engine_name="test_engine"
    )

    # Create state
    messages = [
        HumanMessage(content="Test"),
        AIMessage(
            content="",
            tool_calls=[{
                "id": "call_123",
                "name": "plan_task_generic",
                "args": {"objective": "Test", "steps": []}
            }]
        )
    ]

    state = {
        "messages": messages,
        "engines": {"test_engine": engine},
        "engine_name": "test_engine"
    }

    print("\n2️⃣ Checking Route Retrieval")
    print("-" * 40)

    # What happens in _process_validation_results
    tool_calls = messages[-1].tool_calls

    # First, get tool routes from engine
    print("Getting tool routes from engine...")
    tool_routes = engine.tool_routes
    print(f"Tool routes from engine: {tool_routes}")

    # Then look up the specific tool
    tool_name = "plan_task_generic"
    route = tool_routes.get(tool_name, "unknown")
    print(f"\nRoute for '{tool_name}': {route}")

    # This should be 'parse_output' based on our earlier tests
    if route == "parse_output":
        print("✅ Route found correctly!")
    else:
        print("❌ Route not found - will default to 'unknown'")

    print("\n3️⃣ Testing Full Validation Flow")
    print("-" * 40)

    # Execute validation
    try:
        result = val_node(state)
        print(f"Result type: {type(result)}")
        print(f"Goto: {result.goto if hasattr(result, 'goto') else 'N/A'}")

        # Check the messages
        if hasattr(result, "update") and "messages" in result.update:
            new_messages = result.update["messages"]
            tool_messages = [m for m in new_messages if isinstance(m, ToolMessage)]
            print(f"Tool messages added: {len(tool_messages)}")
            if tool_messages:
                tm = tool_messages[0]
                print(f"Tool message error status: {tm.additional_kwargs.get('is_error', False)}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_route_lookup()
