"""Simple test to show Self-Discover MultiAgent working."""

import asyncio

from haive.agents.reasoning_and_critique.self_discover.agent import SelfDiscoverAgent


async def test_simple_self_discover():
    """Test the Self-Discover MultiAgent with a simple task."""
    # Use the Self-Discover agent
    self_discover = SelfDiscoverAgent

    # Simple test
    task = "What is 2 + 2?"

    try:
        # Run the system
        await self_discover.arun(task)

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_simple_self_discover())
