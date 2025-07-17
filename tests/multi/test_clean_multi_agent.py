#!/usr/bin/env python3
"""Test the clean multi-agent pattern."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.clean import MultiAgent
from haive.agents.simple.agent import SimpleAgent


async def test_clean_multi_agent():
    """Test clean multi-agent sequential execution."""
    print("Testing clean multi-agent pattern...")

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

    print(f"✅ Multi-agent result: {result}")
    print(f"✅ Agents: {list(multi_agent.agents.keys())}")
    print(f"✅ Execution mode: {multi_agent.execution_mode}")

    return result


async def test_plan_and_execute():
    """Test simple plan and execute."""
    print("\nTesting simple plan and execute...")

    from haive.agents.planning.plan_and_execute.simple import PlanAndExecuteAgent

    # Create plan and execute agent
    agent = PlanAndExecuteAgent.create(
        tools=[], name="simple_planner"  # No tools for now
    )

    # Test execution
    result = await agent.arun("Write a haiku about programming")

    print(f"✅ Plan and execute result: {result}")
    print(f"✅ Plan: {result.plan}")
    print(f"✅ Final response: {result.final_response}")

    return result


async def main():
    """Run all tests."""
    print("🧪 Testing clean multi-agent patterns...\n")

    try:
        # Test 1: Basic multi-agent
        await test_clean_multi_agent()

        # Test 2: Plan and execute
        await test_plan_and_execute()

        print("\n✅ All tests passed! Clean multi-agent pattern working.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
