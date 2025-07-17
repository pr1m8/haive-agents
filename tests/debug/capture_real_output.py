#!/usr/bin/env python3
"""Capture the real output from AgentNodeV3 by patching it."""

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
            print(f"\n🔍 CAPTURING: AgentNodeV3 call for '{self.agent_name}'")
            print(f"  Input state type: {type(state)}")
            print(
                f"  Input state keys: {list(state.keys()) if isinstance(state, dict) else 'Not dict'}"
            )

            # Call original method
            result = original_call(self, state, config)

            # Capture and show the result
            print("\n📋 CAPTURED OUTPUT:")
            print(f"  🔍 Type: {type(result)}")
            print(f"  🔍 Result: {result}")

            if hasattr(result, "update"):
                print(f"  🔍 Command.update: {result.update}")
                print(f"  🔍 Command.goto: {getattr(result, 'goto', 'No goto')}")

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
                print(f"  🔍 Dict keys: {list(result.keys())}")
                print(f"  🔍 Dict content: {result}")

                # Store the captured output
                captured_outputs.append(
                    {"agent_name": self.agent_name, "type": "dict", "content": result}
                )

            print(f"  ✅ Captured output for {self.agent_name}")
            return result

        # Apply the patch
        AgentNodeV3Config.__call__ = captured_call
        print("✅ Successfully patched AgentNodeV3")

    except Exception as e:
        print(f"❌ Failed to patch: {e}")
        import traceback

        traceback.print_exc()


def test_with_real_agent():
    """Test with the real self-discovery agent."""
    print("\n🚀 TESTING: Real Self-Discovery Agent")

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

        print(f"📝 Testing with: {list(test_input.keys())}")

        # This should trigger our patched AgentNodeV3 calls
        print("\n🔥 RUNNING AGENT (this will capture all node outputs)...")

        try:
            result = self_discovery.run(test_input)
            print("✅ Agent completed successfully")
        except Exception as e:
            print(f"❌ Agent failed (but we captured outputs): {e}")
            # Don't print full traceback, we just want the captured outputs

    except Exception as e:
        print(f"❌ Failed to load agent: {e}")


def show_captured_outputs():
    """Show all captured outputs."""
    print("\n🎯 CAPTURED OUTPUTS SUMMARY:")
    print(f"Total captures: {len(captured_outputs)}")

    for i, output in enumerate(captured_outputs):
        print(f"\n📋 Capture {i+1}:")
        print(f"  Agent: {output['agent_name']}")
        print(f"  Type: {output['type']}")

        if "update" in output:
            print(f"  Update: {output['update']}")
            print(f"  Goto: {output['goto']}")
        elif "content" in output:
            print(f"  Content: {output['content']}")


if __name__ == "__main__":
    print("🚀 Real AgentNodeV3 Output Capturer")
    print("=" * 50)

    # Step 1: Patch AgentNodeV3
    patch_agent_node_v3()

    # Step 2: Run real agent (this will trigger captures)
    test_with_real_agent()

    # Step 3: Show what we captured
    show_captured_outputs()
