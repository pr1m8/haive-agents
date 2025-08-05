#!/usr/bin/env python3
"""Capture the real output from AgentNodeV3 by patching it."""

import contextlib
import sys


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

# Monkey patch to capture output
original_call = None
captured_outputs = []


def patch_agent_node_v3():
    """Patch AgentNodeV3 to capture its output."""
    global original_call

    try:
        from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config

        # Store original __call__ method
        original_call = AgentNodeV3Config.__call__

        def captured_call(self, state, config=None):
            """Wrapped call that captures output."""
            # Call original method
            result = original_call(self, state, config)

            # Capture and show the result

            if hasattr(result, "update"):
                # Store the captured output
                captured_outputs.append(
                    {
                        "agent_name": self.agent_name,
                        "type": type(result).__name__,
                        "update": result.update,
                        "goto": getattr(result, "goto", None),
                    }
                )

            elif isinstance(result, dict):
                # Store the captured output
                captured_outputs.append(
                    {"agent_name": self.agent_name, "type": "dict", "content": result}
                )

            return result

        # Apply the patch
        AgentNodeV3Config.__call__ = captured_call

    except Exception:
        import traceback

        traceback.print_exc()


def test_with_real_agent():
    """Test with the real self-discovery agent."""
    try:
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        # Simple test input
        test_input = {
            "messages": [],
            "task_description": "What is 2 + 2?",
            "reasoning_modules": "Basic arithmetic",
            "selected_modules": None,
            "adapted_modules": None,
            "reasoning_structure": None,
            "answer": None,
            "error": None,
            "metadata": {},
        }

        # This should trigger our patched AgentNodeV3 calls

        with contextlib.suppress(Exception):
            self_discovery.run(test_input)
            # Don't print full traceback, we just want the captured outputs

    except Exception:
        pass


def show_captured_outputs():
    """Show all captured outputs."""
    for _i, output in enumerate(captured_outputs):
        if "update" in output or "content" in output:
            pass


if __name__ == "__main__":
    # Step 1: Patch AgentNodeV3
    patch_agent_node_v3()

    # Step 2: Run real agent (this will trigger captures)
    test_with_real_agent()

    # Step 3: Show what we captured
    show_captured_outputs()
