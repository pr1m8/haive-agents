"""Test MultiAgent basic functionality with Self-Discover agents."""

import asyncio

from haive.agents.multi.clean import MultiAgent
from haive.agents.reasoning_and_critique.self_discover.adapter import AdapterAgent
from haive.agents.reasoning_and_critique.self_discover.executor import ExecutorAgent
from haive.agents.reasoning_and_critique.self_discover.selector import SelectorAgent
from haive.agents.reasoning_and_critique.self_discover.structurer import StructurerAgent


async def test_simple_sequential():
    """Test basic sequential execution with Self-Discover agents."""
    print("=== Test MultiAgent Sequential ===\n")

    # Create MultiAgent with list of agents (should work according to docs)
    multi_agent = MultiAgent(
        agents=[SelectorAgent(), AdapterAgent(), StructurerAgent(), ExecutorAgent()]
    )

    print(f"MultiAgent created: {multi_agent.name}")
    print(f"Number of agents: {len(multi_agent.agents)}")
    print(f"Agent names: {list(multi_agent.agents.keys())}")
    print(f"Execution mode: {multi_agent.execution_mode}")

    # Simple task
    task = "What is 2 + 2?"
    print(f"\nTask: {task}")

    # Test basic functionality
    try:
        result = await multi_agent.arun(task)
        print(f"\n✅ SUCCESS!")
        print(f"Result type: {type(result)}")
        print(f"Result: {result}")
        return True
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


async def test_multiagent_properties():
    """Test that MultiAgent properties work correctly."""
    print("\n=== Test MultiAgent Properties ===\n")

    # Create agents
    selector = SelectorAgent()
    adapter = AdapterAgent()

    # Create MultiAgent
    multi_agent = MultiAgent(agents=[selector, adapter])

    print(f"Agents dict: {multi_agent.agents}")
    print(f"Agent keys: {list(multi_agent.agents.keys())}")
    print(f"Agent types: {[type(a).__name__ for a in multi_agent.agents.values()]}")

    # Test that agents are accessible
    for name, agent in multi_agent.agents.items():
        print(f"Agent '{name}': {type(agent).__name__}")
        print(f"  - Name: {agent.name}")
        print(f"  - Has engine: {hasattr(agent, 'engine')}")

    return True


if __name__ == "__main__":

    async def main():
        test1 = await test_simple_sequential()
        test2 = await test_multiagent_properties()

        print(f"\n{'='*50}")
        print(f"Test Results:")
        print(f"  Sequential: {'✅ PASS' if test1 else '❌ FAIL'}")
        print(f"  Properties: {'✅ PASS' if test2 else '❌ FAIL'}")

        return test1 and test2

    success = asyncio.run(main())
    exit(0 if success else 1)
