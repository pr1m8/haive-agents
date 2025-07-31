"""Simple test for multi-agent execution."""

import asyncio
import os
import sys

# Add paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig

# Direct imports to avoid broken __init__.py
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


async def test_execution():
    """Test multi-agent execution."""

    # Create agents
    agent1 = SimpleAgent(
        name="agent1",
        engine=AugLLMConfig(system_message="You are agent 1. Say hello from agent 1."),
    )

    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(
            system_message="You are agent 2. Respond to the previous message."
        ),
    )


    # Create multi-agent
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )


    try:

        # Test input
        test_input = {"messages": [HumanMessage(content="Hello!")]}

        # Execute
        result = await multi.ainvoke(test_input)


        # Check messages
        if isinstance(result, dict) and "messages" in result:
            if result["messages"]:
                last_message = result["messages"][-1]

        return True

    except Exception as e:
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_execution())
    if success:
        pass
    else:
        pass
