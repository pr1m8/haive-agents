"""Clean test for self-discover agent to see actual results."""

import asyncio
import sys


# Add direct paths to avoid import issues
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

# Suppress debug logging
import logging


logging.getLogger().setLevel(logging.ERROR)

from langchain_core.messages import HumanMessage

from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
    DEFAULT_REASONING_MODULES,
    self_discovery,
)


async def test_self_discover_clean():
    """Test self-discover agent with clean output."""
    # Simple test problem
    test_problem = "How do I solve 25 * 36?"

    test_input = {
        "messages": [HumanMessage(content=test_problem)],
        "reasoning_modules": DEFAULT_REASONING_MODULES[:5],  # Use only first 5 modules
    }

    try:
        result = await self_discovery.ainvoke(test_input)

        if isinstance(result, dict):
            # Check messages
            if "messages" in result:
                for i, msg in enumerate(result["messages"]):
                    if hasattr(msg, "content"):
                        content = (
                            msg.content[:100] + "..." if len(msg.content) > 100 else msg.content
                        )

            # Check agent outputs
            if "agent_outputs" in result:
                # Show each agent's output
                for agent_name, output in result["agent_outputs"].items():
                    if isinstance(output, dict):
                        for key, value in output.items():
                            pass
                    else:
                        pass

        return result

    except Exception:
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    result = asyncio.run(test_self_discover_clean())

    if result:
        if isinstance(result, dict):
            pass
    else:
        pass
