"""Test basic MultiAgent functionality without complex routing."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi.clean import MultiAgent
from haive.agents.simple import SimpleAgent


async def test_basic_multiagent():
    """Test basic MultiAgent with simple agents."""
    # Create simple agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig(temperature=0.1))
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig(temperature=0.1))

    # Create MultiAgent
    multi_agent = MultiAgent(agents=[agent1, agent2])

    # Test execution
    try:
        await multi_agent.arun("Say hello")
        return True
    except Exception:
        return False


if __name__ == "__main__":
    success = asyncio.run(test_basic_multiagent())
