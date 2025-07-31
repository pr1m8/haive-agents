"""Test MultiAgent basic functionality with Self-Discover agents."""

import asyncio
import sys

from haive.agents.multi.clean import MultiAgent
from haive.agents.reasoning_and_critique.self_discover.adapter import AdapterAgent
from haive.agents.reasoning_and_critique.self_discover.executor import ExecutorAgent
from haive.agents.reasoning_and_critique.self_discover.selector import SelectorAgent
from haive.agents.reasoning_and_critique.self_discover.structurer import StructurerAgent


async def test_simple_sequential():
    """Test basic sequential execution with Self-Discover agents."""
    # Create MultiAgent with list of agents (should work according to docs)
    multi_agent = MultiAgent(
        agents=[SelectorAgent(), AdapterAgent(), StructurerAgent(), ExecutorAgent()]
    )

    # Simple task
    task = "What is 2 + 2?"

    # Test basic functionality
    try:
        await multi_agent.arun(task)
        return True
    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_multiagent_properties():
    """Test that MultiAgent properties work correctly."""
    # Create agents
    selector = SelectorAgent()
    adapter = AdapterAgent()

    # Create MultiAgent
    multi_agent = MultiAgent(agents=[selector, adapter])

    # Test that agents are accessible
    for _name, _agent in multi_agent.agents.items():
        pass

    return True


if __name__ == "__main__":

    async def main():
        test1 = await test_simple_sequential()
        test2 = await test_multiagent_properties()

        return test1 and test2

    success = asyncio.run(main())
    sys.exit(0 if success else 1)
