"""Final test of Self-Discover MultiAgent."""

import asyncio

from haive.agents.reasoning_and_critique.self_discover.agent import (
    create_self_discover_agent,
    get_default_modules,
)


async def test_self_discover():
    """Test Self-Discover with MultiAgent."""
    # Create agent
    agent = create_self_discover_agent()

    # Test task
    task = "What is 2 + 2?"
    input_data = {"available_modules": get_default_modules(), "task_description": task}

    try:
        await agent.arun(input_data)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    success = asyncio.run(test_self_discover())
