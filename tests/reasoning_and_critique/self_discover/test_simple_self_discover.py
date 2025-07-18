"""Simple test to show Self-Discover MultiAgent working."""

import asyncio

from haive.agents.reasoning_and_critique.self_discover.agent import SelfDiscoverAgent


async def test_simple_self_discover():
    """Test the Self-Discover MultiAgent with a simple task."""
    print("=== Testing Self-Discover MultiAgent ===\n")

    # Use the Self-Discover agent
    self_discover = SelfDiscoverAgent

    # Simple test
    task = "What is 2 + 2?"

    print(f"Task: {task}")
    print(f"Agent type: {type(self_discover).__name__}")
    print(f"Number of agents: {len(self_discover.agents)}")
    print(f"Agent names: {[type(agent).__name__ for agent in self_discover.agents]}")
    print("\nExecuting...\n")

    try:
        # Run the system
        result = await self_discover.arun(task)

        print("=== SUCCESS ===")
        print(f"Result type: {type(result)}")
        print(f"Result: {result}")

        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_simple_self_discover())
    print(f"\nTest {'PASSED' if success else 'FAILED'}")
