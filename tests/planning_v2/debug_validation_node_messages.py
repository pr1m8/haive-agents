#!/usr/bin/env python3
"""Debug what happens in the validation node - why no ToolMessages?"""


from langchain_core.messages import AIMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)

def debug_validation_node():
    """Debug the validation node step by step."""
    print("🔍 DEBUG: VALIDATION NODE PROCESSING")
    print("=" * 80)

    agent = SimpleAgent(
        name="debug_validation",
        engine=AugLLMConfig(structured_output_model=Plan[Task]),
        debug=True
    )

    # Step 1: Create a mock AIMessage with tool calls (like agent_node would produce)
    mock_ai_message = AIMessage(
        content="I'll create a plan",
        tool_calls=[{
            "name": "plan_task_generic",
            "args": {"objective": "Test", "steps": [{"description": "Step 1"}]},
            "id": "test_call_1"
        }]
    )

    print("1. Mock AIMessage created:")
    print(f"   Tool calls: {len(mock_ai_message.tool_calls)}")
    print(f"   Tool name: {mock_ai_message.tool_calls[0]['name']}")

    # Step 2: Create mock state like agent_node would pass to validation
    mock_state = {
        "messages": [mock_ai_message],
        "tool_routes": agent.engine.tool_routes,
        "engines": {"main": agent.engine}
    }

    print("\n2. Mock state for validation:")
    print(f"   Messages: {len(mock_state['messages'])}")
    print(f"   Tool routes: {mock_state['tool_routes']}")

    # Step 3: Test ValidationNodeConfigV2 directly
    from haive.core.graph.node.validation_node_config_v2 import ValidationNodeConfigV2

    validation_node = ValidationNodeConfigV2(
        name="test_validation",
        engine_name="main",
        parser_node="parse_output"
    )

    print("\n3. Testing ValidationNodeConfigV2:")
    print(f"   Node: {validation_node}")

    try:
        # This should create ToolMessages
        result = validation_node(mock_state, {})
        print(f"   ✅ Validation result type: {type(result)}")

        if hasattr(result, "update"):
            updated_state = result.update
            print(f"   Updated state keys: {list(updated_state.keys())}")

            if "messages" in updated_state:
                messages = updated_state["messages"]
                print(f"   Updated messages count: {len(messages)}")

                tool_messages = [m for m in messages if hasattr(m, "name") and m.name]
                print(f"   ToolMessages created: {len(tool_messages)}")

                if tool_messages:
                    tm = tool_messages[0]
                    print(f"   ToolMessage name: {tm.name}")
                    print(f"   ToolMessage content: {str(tm.content)[:100]}...")

                    # Step 4: Now test validation_router_v2 with the ToolMessages
                    print("\n4. Testing validation_router_v2 with ToolMessages:")

                    router_state = {
                        "messages": messages,  # Include the ToolMessages
                        "tool_routes": mock_state["tool_routes"]
                    }

                    from haive.core.graph.node.validation_router_v2 import validation_router_v2
                    router_result = validation_router_v2(router_state)
                    print(f"   Router result: {router_result}")

                    if router_result == "parse_output":
                        print("   ✅ SUCCESS: Router correctly routes to parse_output!")
                    elif router_result == "__end__":
                        print("   ❌ PROBLEM: Router goes to END instead of parse_output")
                    else:
                        print(f"   ⚠️  UNEXPECTED: Router returns {router_result}")

        else:
            print("   ❌ No update field in result")

    except Exception as e:
        print(f"   ❌ Validation failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_validation_node()
