#!/usr/bin/env python3
"""Test the self-discovery agent after fixing the __dict__ debug issue."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


def test_self_discovery_agent():
    """Test the self-discovery agent with proper input format."""
    print("🔍 TESTING: Self-Discovery Agent (Fixed)")

    try:
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        print(f"✅ Agent: {self_discovery.name}")
        print(f"✅ Type: {type(self_discovery)}")
        print(f"✅ Schema: {self_discovery.state_schema.__name__}")

        # Test with SelfDiscoveryState format
        problem = "Lisa has 10 apples. She gives 3 apples to her friend and then buys 5 more apples from the store. How many apples does Lisa have now?"

        # Use full SelfDiscoveryState format
        test_input = {
            "messages": [],
            "task_description": problem,
            "reasoning_modules": """1. How could I devise an experiment to help solve that problem?
2. Make a list of ideas for solving this problem, and apply them one by one to the problem to see if any progress can be made.
3. What are the key assumptions underlying this problem?""",
            "selected_modules": None,
            "adapted_modules": None,
            "reasoning_structure": None,
            "answer": None,
            "error": None,
            "metadata": {},
        }

        print(f"📝 Input keys: {list(test_input.keys())}")
        print(f"📝 Problem: {problem}")

        print("\n🚀 RUNNING AGENT...")
        result = self_discovery.run(test_input)

        print(f"✅ SUCCESS! Result type: {type(result)}")
        print(
            f"✅ Result keys: {list(result.keys()) if isinstance(result, dict) else 'N/A'}"
        )

        if isinstance(result, dict) and "answer" in result:
            print(f"✅ Final answer: {result['answer']}")

        return True

    except Exception as e:
        print(f"❌ FAILED: {e}")
        print(f"Error type: {type(e)}")

        # Check if it's the original LangGraph error
        if "Expected dict, got" in str(e):
            print(
                "🔴 CONFIRMED: This is the original 'Expected dict, got' LangGraph error"
            )
        else:
            print("🔵 DIFFERENT ERROR: Not the original LangGraph error")

        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("🚀 Testing Fixed Self-Discovery Agent")
    print("=" * 50)

    success = test_self_discovery_agent()

    if success:
        print("\n🎉 SUCCESS: Agent working properly!")
    else:
        print("\n💥 FAILED: Still has issues to resolve")
