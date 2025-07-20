#!/usr/bin/env python3
"""Debug what the node is actually outputting - simplified version."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def debug_agent_node_v3_output():
    """Show exactly what AgentNodeV3 outputs."""
    try:
        from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config
        from langgraph.types import Command

        # Create a mock agent for testing
        class MockAgent:
            def __init__(self):
                self.name = "test_agent"

            def invoke(self, input_data, config=None):
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

        # Create AgentNodeV3Config
        node_config = AgentNodeV3Config(
            agent_name="test_agent",
            agent=MockAgent(),
            name="test_node",
        )

        # This is what should return Command or dict
        result = node_config(test_state)

        if hasattr(result, "update") and isinstance(result.update, dict):
            pass

        if hasattr(result, "goto"):
            pass

        # Test what LangGraph expects

        # LangGraph expects the node function to return something that can be processed
        # Let's see what happens if we extract the update
        if hasattr(result, "update"):
            update_part = result.update

            # This is what LangGraph actually wants
            if isinstance(update_part, dict):
                pass
            else:
                pass
        elif isinstance(result, dict):
            pass
        else:
            pass

        # Show what the Command object actually contains

        # Create a test Command to see its structure
        Command(update={"test": "value"})

    except Exception:
        import traceback

        traceback.print_exc()


def test_command_vs_dict():
    """Test the difference between Command and dict returns."""
    try:
        from langgraph.types import Command

        # Create both formats
        Command(update={"key": "value", "messages": []})

        # Test what LangGraph's _get_updates would do

        # For dict - LangGraph expects this

        # For Command - This is what causes the error

        # The issue is LangGraph tries to process the Command object itself
        # rather than extracting the .update field

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    debug_agent_node_v3_output()
    test_command_vs_dict()
