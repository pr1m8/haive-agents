#!/usr/bin/env python3
"""Debug what the node is actually outputting - simplified version."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def debug_agent_node_v3_output():
    """Show exactly what AgentNodeV3 outputs."""
    print("🔍 DEBUGGING: AgentNodeV3 Direct Output")

    try:
        from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config
        from langgraph.types import Command

        print("✅ Successfully imported AgentNodeV3Config and Command")

        # Create a mock agent for testing
        class MockAgent:
            def __init__(self):
                self.name = "test_agent"

            def invoke(self, input_data, config=None):
                print(f"    Mock agent invoked with: {list(input_data.keys())}")
                return {
                    "messages": [],
                    "result": "test output",
                    "task_description": input_data.get("task_description", ""),
                }

        # Create test state
        test_state = {
            "task_description": "Simple test task",
            "messages": [],
            "selected_modules": None,
        }

        print(f"📝 Input state: {test_state}")

        # Create AgentNodeV3Config
        node_config = AgentNodeV3Config(
            agent_name="test_agent",
            agent=MockAgent(),
            name="test_node",
        )

        print("\n🚀 CALLING AgentNodeV3 DIRECTLY...")

        # This is what should return Command or dict
        result = node_config(test_state)

        print("\n📋 EXACT OUTPUT:")
        print(f"  Result type: {type(result)}")
        print(f"  Result: {result}")

        if hasattr(result, "update"):
            print("\n🔍 Command.update attribute:")
            print(f"    Type: {type(result.update)}")
            print(f"    Is dict: {isinstance(result.update, dict)}")
            print(f"    Content: {result.update}")

            if isinstance(result.update, dict):
                print(f"    Keys: {list(result.update.keys())}")

        if hasattr(result, "goto"):
            print("\n🔍 Command.goto attribute:")
            print(f"    Value: {result.goto}")
            print(f"    Type: {type(result.goto)}")

        # Test what LangGraph expects
        print("\n🔍 LangGraph Compatibility Test:")

        # LangGraph expects the node function to return something that can be processed
        # Let's see what happens if we extract the update
        if hasattr(result, "update"):
            update_part = result.update
            print(f"  ✅ Extracted update: {update_part}")
            print(f"  ✅ Update is dict: {isinstance(update_part, dict)}")

            # This is what LangGraph actually wants
            if isinstance(update_part, dict):
                print("  ✅ LangGraph would accept this dict")
            else:
                print(f"  ❌ LangGraph expects dict, got {type(update_part)}")
        elif isinstance(result, dict):
            print("  ✅ Node returned plain dict - LangGraph compatible")
        else:
            print(f"  ❌ Node returned {type(result)} - not LangGraph compatible")

        # Show what the Command object actually contains
        print("\n🔍 Command Object Details:")
        print(f"  Command class: {Command}")
        print(
            f"  Command fields: {getattr(Command, '__annotations__', 'No annotations')}"
        )

        # Create a test Command to see its structure
        test_command = Command(update={"test": "value"})
        print(f"  Test Command: {test_command}")
        print(f"  Test Command type: {type(test_command)}")
        print(
            f"  Test Command dict: {test_command.__dict__ if hasattr(test_command, '__dict__') else 'No __dict__'}"
        )

    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback

        traceback.print_exc()


def test_command_vs_dict():
    """Test the difference between Command and dict returns."""
    print("\n🔍 TESTING: Command vs Dict")

    try:
        from langgraph.types import Command

        # Create both formats
        dict_return = {"key": "value", "messages": []}
        command_return = Command(update={"key": "value", "messages": []})

        print("📋 Dict return:")
        print(f"  Type: {type(dict_return)}")
        print(f"  Content: {dict_return}")

        print("📋 Command return:")
        print(f"  Type: {type(command_return)}")
        print(f"  Content: {command_return}")
        print(f"  Update: {command_return.update}")
        print(f"  Goto: {getattr(command_return, 'goto', 'Not set')}")

        # Test what LangGraph's _get_updates would do
        print("\n🔍 LangGraph Processing Simulation:")

        # For dict - LangGraph expects this
        print("  Dict processing: Direct use ✅")

        # For Command - This is what causes the error
        print(f"  Command processing: Extracts .update = {command_return.update}")

        # The issue is LangGraph tries to process the Command object itself
        # rather than extracting the .update field

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("🚀 Simple Node Output Debugger")
    print("=" * 50)
    debug_agent_node_v3_output()
    test_command_vs_dict()
