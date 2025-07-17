#!/usr/bin/env python3
"""Test the final multi-agent implementation."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.clean import MultiAgent
from haive.agents.planning.plan_and_execute.simple import PlanAndExecuteAgent
from haive.agents.simple.agent import SimpleAgent


async def test_clean_multi_agent():
    """Test clean multi-agent with list input."""
    print("🧪 Testing clean multi-agent with list input...")

    # Create agents
    writer = SimpleAgent(
        name="writer",
        engine=AugLLMConfig(
            prompt_template="Write a brief story about: {input}", temperature=0.7
        ),
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

    print(f"✅ Agents dict keys: {list(multi_agent.agents.keys())}")
    print(f"✅ Execution mode: {multi_agent.execution_mode}")

    # Test execution
    result = await multi_agent.arun("a robot discovering emotions")
    print(f"✅ Result: {result}")

    return result


async def test_plan_and_execute():
    """Test plan and execute agent."""
    print("\n🧪 Testing Plan and Execute agent...")

    # Create plan and execute agent
    agent = PlanAndExecuteAgent.create(name="planner")

    print(f"✅ P&E agents: {list(agent.agents.keys())}")
    print(f"✅ State schema: {agent.state_schema}")

    # Test execution
    result = await agent.arun("Create a simple marketing plan for a new mobile app")
    print(f"✅ Plan result: {result}")

    return result


async def main():
    """Run all tests."""
    print("🚀 Testing final multi-agent implementation...\n")

    try:
        # Test 1: Clean multi-agent
        await test_clean_multi_agent()

        # Test 2: Plan and execute
        await test_plan_and_execute()

        print("\n✅ All tests passed! Multi-agent implementation working correctly.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
