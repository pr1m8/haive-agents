#!/usr/bin/env python3
"""Test ValidationNodeV2 with the exact AIMessage from AugLLMConfig to debug what goes wrong."""

import json

from langchain_core.messages import AIMessage
from pydantic import BaseModel, Field

from haive.core.graph.node.validation_node_v2 import ValidationNodeV2
from haive.core.schema.prebuilt.messages_state import MessagesState


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def create_test_state_with_saved_message():
    """Create test state with the exact AIMessage from AugLLMConfig execution."""
    # Recreate the exact AIMessage from our saved debug data
    tool_call = {
        "name": "plan_task_generic",
        "args": {
            "objective": "Organize a birthday party",
            "steps": [
                "Choose a theme for the party and decide on the decorations.",
                "Send out invitations to the guests."
            ]
        },
        "id": "call_ge4ZJG0M7t6cQ7AWXc12ZgBK",
        "type": "tool_call"
    }

    ai_message = AIMessage(
        content="",
        tool_calls=[tool_call],
        additional_kwargs={
            "tool_calls": [{
                "id": "call_ge4ZJG0M7t6cQ7AWXc12ZgBK",
                "function": {
                    "arguments": '{"objective":"Organize a birthday party","steps":["Choose a theme for the party and decide on the decorations.","Send out invitations to the guests."]}',
                    "name": "plan_task_generic"
                },
                "type": "function"
            }],
            "refusal": None
        },
        id="run--fc98e052-17e0-46b9-9964-d056c2b10538-0"
    )

    # Create state with this message
    state = MessagesState()
    state.messages = [ai_message]

    return state, ai_message


def test_validation_node_with_exact_message():
    """Test ValidationNodeV2 with the exact message from AugLLMConfig."""
    print("🔍 TESTING VALIDATION NODE WITH EXACT AIMESSAGE")
    print("=" * 60)

    # Create test state
    state, ai_message = create_test_state_with_saved_message()

    print("1. Test state created:")
    print(f"   Messages count: {len(state.messages)}")
    print(f"   Message type: {type(ai_message)}")
    print(f"   Tool calls count: {len(ai_message.tool_calls)}")
    print(f"   Tool call name: {ai_message.tool_calls[0]['name']}")
    print(f"   Tool call args: {ai_message.tool_calls[0]['args']}")

    # Create ValidationNodeV2 with correct configuration
    tool_routes = {"plan_task_generic": "parse_output"}
    tool_metadata = {
        "plan_task_generic": {
            "purpose": "structured_output",
            "version": "v2",
            "force_choice": True,
            "class_name": "Plan[Task]",
            "tool_type": "structured_output_model",
            "is_structured_output": True,
            "source": "aug_llm_config"
        }
    }

    validation_node = ValidationNodeV2(
        name="test_validation",
        tool_routes=tool_routes,
        tool_metadata=tool_metadata,
        pydantic_models={"plan_task_generic": Plan[Task]}  # Provide the model
    )

    print("\n2. ValidationNodeV2 created:")
    print(f"   Tool routes: {validation_node.tool_routes}")
    print(f"   Tool metadata keys: {list(validation_node.tool_metadata.keys())}")
    print(f"   Pydantic models: {getattr(validation_node, 'pydantic_models', 'Not found')}")

    try:
        print("\n3. Testing validation node execution...")

        # Call the validation node
        result_state = validation_node(state)

        print("   ✅ Validation node executed successfully!")
        print(f"   Result type: {type(result_state)}")
        print(f"   Result messages count: {len(result_state.messages) if hasattr(result_state, 'messages') else 'No messages'}")

        # Analyze the result
        if hasattr(result_state, "messages") and result_state.messages:
            last_message = result_state.messages[-1]
            print(f"   Last message type: {type(last_message)}")

            if hasattr(last_message, "content"):
                print(f"   Last message content: {last_message.content}")

            # Check if we got a ToolMessage with parsed content
            if hasattr(last_message, "tool_call_id"):
                print("   ✅ Got ToolMessage!")
                print(f"   Tool call ID: {last_message.tool_call_id}")

                # Try to parse the content
                if hasattr(last_message, "content"):
                    try:
                        if isinstance(last_message.content, str):
                            parsed_content = json.loads(last_message.content)
                        else:
                            parsed_content = last_message.content

                        # Try to create Plan[Task] from parsed content
                        plan = Plan[Task](**parsed_content)
                        print("   ✅ Content successfully parsed as Plan[Task]!")
                        print(f"   Objective: {plan.objective}")
                        print(f"   Steps: {[step.description for step in plan.steps]}")

                    except Exception as e:
                        print(f"   ❌ Failed to parse content as Plan[Task]: {e}")
                        print(f"   Raw content: {last_message.content}")

        # Save the result for further debugging
        result_data = {
            "success": True,
            "result_type": type(result_state).__name__,
            "messages_count": len(result_state.messages) if hasattr(result_state, "messages") else 0,
            "last_message_type": type(result_state.messages[-1]).__name__ if hasattr(result_state, "messages") and result_state.messages else None,
            "last_message_content": str(result_state.messages[-1].content) if hasattr(result_state, "messages") and result_state.messages else None
        }

        with open("/tmp/validation_node_test_result.json", "w") as f:
            json.dump(result_data, f, indent=2, default=str)

        print("   Result saved to: /tmp/validation_node_test_result.json")

        return True, result_state

    except Exception as e:
        print(f"\n❌ VALIDATION NODE FAILED: {e}")
        import traceback
        traceback.print_exc()

        # Save error info
        error_data = {
            "success": False,
            "error_type": type(e).__name__,
            "error_message": str(e),
            "traceback": traceback.format_exc()
        }

        with open("/tmp/validation_node_test_error.json", "w") as f:
            json.dump(error_data, f, indent=2)

        print("   Error saved to: /tmp/validation_node_test_error.json")
        return False, None


def test_manual_parse_output_route():
    """Test the parse_output route logic manually."""
    print("\n" + "=" * 60)
    print("🛠️  TESTING PARSE_OUTPUT ROUTE MANUALLY")
    print("=" * 60)

    state, ai_message = create_test_state_with_saved_message()

    # Extract tool call data
    tool_call = ai_message.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    print("1. Tool call data:")
    print(f"   Name: {tool_name}")
    print(f"   Args: {tool_args}")
    print(f"   Args type: {type(tool_args)}")

    # Try to manually create Plan[Task] from args
    try:
        print("\n2. Manual Plan[Task] creation:")

        # The args should be a dict that matches Plan[Task] fields
        plan = Plan[Task](**tool_args)
        print("   ✅ Successfully created Plan[Task]!")
        print(f"   Objective: {plan.objective}")
        print(f"   Steps count: {len(plan.steps)}")
        for i, step in enumerate(plan.steps):
            print(f"   Step {i+1}: {step.description}")

        # Convert back to dict for ToolMessage content
        plan_dict = plan.model_dump()
        plan_json = json.dumps(plan_dict, indent=2)

        print("\n3. Plan as JSON for ToolMessage:")
        print(f"   {plan_json}")

        return True, plan

    except Exception as e:
        print(f"\n❌ Manual parsing failed: {e}")
        import traceback
        traceback.print_exc()
        return False, None


if __name__ == "__main__":
    success1, result1 = test_validation_node_with_exact_message()
    success2, result2 = test_manual_parse_output_route()

    print("\n" + "=" * 60)
    print("🏁 DIAGNOSIS RESULTS")
    print("=" * 60)
    print(f"ValidationNode test: {'✅' if success1 else '❌'}")
    print(f"Manual parsing test: {'✅' if success2 else '❌'}")

    if success2 and not success1:
        print("\n🔍 CONCLUSION: Manual parsing works, ValidationNode has a bug!")
    elif success1 and success2:
        print("\n✅ CONCLUSION: Everything works - issue might be elsewhere!")
    elif not success2:
        print("\n❌ CONCLUSION: Fundamental parsing issue with Plan[Task] generic type!")
    else:
        print("\n❓ CONCLUSION: Need further investigation")

    print("\n📄 Debug files saved:")
    print("   - /tmp/validation_node_test_result.json (or _error.json)")
    print("   - /tmp/validation_node_debug_message.json (from previous test)")
    print("   - /tmp/aug_llm_raw_result.json (from previous test)")
