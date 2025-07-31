"""Debug test for self-discover agent state issues."""

import asyncio
import logging
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
    # Simple test problem
    test_problem = "What is 2+2?"

    test_input = {
        "messages": [HumanMessage(content=test_problem)],
        "reasoning_modules": DEFAULT_REASONING_MODULES[:3],
        "task_description": test_problem,
    }

    try:
        result = await self_discovery.ainvoke(test_input, config={"debug": True})

        if isinstance(result, dict):
            pass

        return result

    except Exception:
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = asyncio.run(test_self_discover_debug())
