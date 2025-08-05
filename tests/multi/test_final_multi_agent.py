#!/usr/bin/env python3
"""Test the final multi-agent implementation."""

import asyncio

from haive.agents.multi.clean import MultiAgent
from haive.agents.planning.plan_and_execute.simple import PlanAndExecuteAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


async def test_clean_multi_agent():
    """Test clean multi-agent with list input."""
    # Create agents
    writer = SimpleAgent(
        name="writer",
        engine=AugLLMConfig(prompt_template="Write a brief story about: {input}", temperature=0.7),
    )

    editor = SimpleAgent(
        name="editor",
        engine=AugLLMConfig(
            prompt_template="Edit and improve this story: {input}", temperature=0.3
        ),
    )

    # Create multi-agent with list (should convert to dict)
    multi_agent = MultiAgent.create(
        agents=[writer, editor], name="story_creator", execution_mode="sequential"
    )

    # Test execution
    result = await multi_agent.arun("a robot discovering emotions")

    return result


async def test_plan_and_execute():
    """Test plan and execute agent."""
    # Create plan and execute agent
    agent = PlanAndExecuteAgent.create(name="planner")

    # Test execution
    result = await agent.arun("Create a simple marketing plan for a new mobile app")

    return result


async def main():
    """Run all tests."""
    try:
        # Test 1: Clean multi-agent
        await test_clean_multi_agent()

        # Test 2: Plan and execute
        await test_plan_and_execute()

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
