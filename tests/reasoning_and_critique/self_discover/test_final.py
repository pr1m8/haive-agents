"""Final test of Self-Discover MultiAgent."""

import asyncio

from haive.agents.reasoning_and_critique.self_discover.agent import (
    create_self_discover_agent,
    get_default_modules,
)


async def test_self_discover():
    """Test Self-Discover with MultiAgent."""
    print("=== Self-Discover MultiAgent Test ===")

    # Create agent
    agent = create_self_discover_agent()

    print(f"Agent: {agent.name}")
    print(f"Agents: {list(agent.agents.keys())}")
    print(f"Mode: {agent.execution_mode}")

    # Test task
    task = "What is 2 + 2?"
    input_data = {"available_modules": get_default_modules(), "task_description": task}

    print(f"\nTask: {task}")
    print("Executing sequential Self-Discover workflow...")

    try:
        result = await agent.arun(input_data)
        print("\n✅ SUCCESS!"!")
        print(f"Result: {result}")
        return True
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return False


if __name__ == "__main__":
    success = asyncio.run(test_self_discover())
    print(f"\nTest: {'PASSED' if success else 'FAILED'}")
