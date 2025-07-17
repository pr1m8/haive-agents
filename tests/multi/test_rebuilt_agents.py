#!/usr/bin/env python3
"""Test the rebuilt multi-agent patterns."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.clean import MultiAgent
from haive.agents.planning.plan_and_execute.simple import PlanAndExecuteAgent
from haive.agents.reflection.simple_agent import ReflectionAgent
from haive.agents.simple.agent import SimpleAgent


async def test_clean_multi_agent():
    """Test clean multi-agent sequential execution."""
    print("🧪 Testing clean multi-agent pattern...")

    # Create simple agents
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

    # Create multi-agent
    multi_agent = MultiAgent.create(
        agents=[writer, editor], name="story_creator", execution_mode="sequential"
    )

    # Test execution
    result = await multi_agent.arun("a robot discovering emotions")

    print(f"✅ Multi-agent result: {result}")
    print(f"✅ Agents: {list(multi_agent.agents.keys())}")
    print(f"✅ Execution mode: {multi_agent.execution_mode}")

    return result


async def test_plan_and_execute():
    """Test simple plan and execute."""
    print("\n🧪 Testing simple plan and execute...")

    # Create plan and execute agent
    agent = PlanAndExecuteAgent.create(name="simple_planner")

    # Test execution
    result = await agent.arun("Create a marketing plan for a new app")

    print(f"✅ Plan and execute result: {result}")
    print(f"✅ Plan: {result['plan']}")
    print(f"✅ Execution: {result['execution']}")
    print(f"✅ Final: {result['final_result']}")

    return result


async def test_reflection_agent():
    """Test simple reflection agent."""
    print("\n🧪 Testing simple reflection agent...")

    # Create reflection agent
    agent = ReflectionAgent.create(name="reflector")

    # Test execution
    result = await agent.arun("The quick brown fox jumps over the lazy dog.")

    print(f"✅ Reflection result: {result}")

    return result


async def test_enhanced_agent():
    """Test enhanced agent with reflection."""
    print("\n🧪 Testing enhanced agent with reflection...")

    # Create base agent
    base_agent = SimpleAgent(
        name="writer",
        engine=AugLLMConfig(
            prompt_template="Write a technical explanation of: {input}", temperature=0.7
        ),
    )

    # Enhance with reflection
    enhanced = ReflectionAgent.enhance_agent(
        base_agent=base_agent, name="enhanced_writer"
    )

    # Test execution
    result = await enhanced.arun("quantum computing")

    print(f"✅ Enhanced agent result: {result}")
    print(f"✅ Enhanced agents: {list(enhanced.agents.keys())}")

    return result


async def main():
    """Run all tests."""
    print("🚀 Testing rebuilt multi-agent patterns...\n")

    try:
        # Test 1: Basic multi-agent
        await test_clean_multi_agent()

        # Test 2: Plan and execute
        await test_plan_and_execute()

        # Test 3: Reflection agent
        await test_reflection_agent()

        # Test 4: Enhanced agent
        await test_enhanced_agent()

        print("\n✅ All tests passed! Rebuilt multi-agent patterns working perfectly.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
