#!/usr/bin/env python3
"""Test the clean multi-agent pattern - simple version."""

import asyncio

# Direct imports to avoid the broken agent module
from haive.agents.multi.clean import MultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


async def test_clean_multi_agent():
    """Test clean multi-agent sequential execution."""
    # Create simple agents
    agent1 = SimpleAgent(
        name="writer",
        engine=AugLLMConfig(
            prompt_template="Write a short story about: {input}", temperature=0.7
        ),
    )

    agent2 = SimpleAgent(
        name="editor",
        engine=AugLLMConfig(
            prompt_template="Edit and improve this story: {input}", temperature=0.3
        ),
    )

    # Create multi-agent
    multi_agent = MultiAgent.create(
        agents=[agent1, agent2], name="story_creator", execution_mode="sequential"
    )

    # Test execution
    result = await multi_agent.arun("a robot learning to love")

    return result


async def main():
    """Run all tests."""
    try:
        # Test 1: Basic multi-agent
        await test_clean_multi_agent()

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
