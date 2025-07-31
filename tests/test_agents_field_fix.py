"""Test the agents field fix."""

import asyncio
import sys


sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


async def test_fix():
    """Test that the agents field fix works."""
    # Create simple agents
    agent1 = SimpleAgent(name="test1", engine=AugLLMConfig(system_message="Agent 1"))
    agent2 = SimpleAgent(name="test2", engine=AugLLMConfig(system_message="Agent 2"))

    # Create multi-agent
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Test input WITHOUT agents field
    test_input = {"messages": [HumanMessage(content="Hello")]}

    # Try execution
    try:
        await multi.ainvoke(test_input)
        return True

    except Exception as e:
        if "not found in agents" in str(e):
            pass
        return False


if __name__ == "__main__":
    success = asyncio.run(test_fix())
    if success:
        pass
    else:
        pass
