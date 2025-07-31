#!/usr/bin/env python3
"""Debug EnhancedMultiAgentV4 state handling with V3 agents."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


async def debug_multi_agent_state():
    """Debug the multi-agent state handling."""
    # Create simple agents
    agent1 = SimpleAgentV3(
        name="agent1",
        engine=AugLLMConfig(temperature=0.1, system_message="You are agent 1."),
    )

    agent2 = SimpleAgentV3(
        name="agent2",
        engine=AugLLMConfig(temperature=0.1, system_message="You are agent 2."),
    )

    # Create multi-agent with explicit state
    try:
        multi_agent = EnhancedMultiAgentV4(
            name="debug_multi", agents=[agent1, agent2], execution_mode="sequential"
        )

        # Check the state schema

        # Try to create proper state
        test_state = {
            "messages": [HumanMessage(content="Hello world")],
            "agent_states": {},
            "execution_order": [],
            "current_agent": None,
        }

        # Test execution with proper state format
        await multi_agent.arun(test_state)

    except Exception:

        # Try with string input instead
        try:
            await multi_agent.arun("Hello world")
        except Exception:
            import traceback

            traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(debug_multi_agent_state())
