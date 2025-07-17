"""Debug test for self-discover agent state issues."""

import asyncio
import logging
import os
import sys

# Suppress all logging except errors
logging.getLogger().setLevel(logging.ERROR)

# Add direct paths to avoid import issues
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
    DEFAULT_REASONING_MODULES,
    self_discovery,
)


async def test_self_discover_debug():
    """Test self-discover agent with debug=True."""

    print("🧠 Testing Self-Discovery Agent with DEBUG=True...")

    # Simple test problem
    test_problem = "What is 2+2?"

    test_input = {
        "messages": [HumanMessage(content=test_problem)],
        "reasoning_modules": DEFAULT_REASONING_MODULES[:3],
        "task_description": test_problem,
    }

    print(f"Test input keys: {list(test_input.keys())}")

    try:
        print("🚀 Starting execution with debug=True...")
        result = await self_discovery.ainvoke(test_input, config={"debug": True})

        print("\n✅ Self-discovery completed!")
        print(f"Result type: {type(result)}")

        if isinstance(result, dict):
            print(f"Result keys: {list(result.keys())}")

        return result

    except Exception as e:
        print(f"❌ Self-discovery failed: {type(e).__name__}: {str(e)}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = asyncio.run(test_self_discover_debug())
