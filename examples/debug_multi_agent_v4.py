#!/usr/bin/env python3
"""Debug EnhancedMultiAgentV4 state handling with V3 agents."""

import asyncio
from typing import Any, Dict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


async def debug_multi_agent_state():
    """Debug the multi-agent state handling."""
    print("🔍 Debugging EnhancedMultiAgentV4 State Handling")
    print("=" * 60)

    # Create simple agents
    agent1 = SimpleAgentV3(
        name="agent1",
        engine=AugLLMConfig(temperature=0.1, system_message="You are agent 1."),
    )

    agent2 = SimpleAgentV3(
        name="agent2",
        engine=AugLLMConfig(temperature=0.1, system_message="You are agent 2."),
    )

    print(f"✅ Created agents: {agent1.name}, {agent2.name}")

    # Create multi-agent with explicit state
    try:
        multi_agent = EnhancedMultiAgentV4(
            name="debug_multi", agents=[agent1, agent2], execution_mode="sequential"
        )
        print(f"✅ Created EnhancedMultiAgentV4: {multi_agent.name}")
        print(f"   Agent names: {multi_agent.get_agent_names()}")

        # Check the state schema
        print(f"\n🔍 Multi-agent state schema: {multi_agent.state_schema}")

        # Try to create proper state
        test_state = {
            "messages": [HumanMessage(content="Hello world")],
            "agent_states": {},
            "execution_order": [],
            "current_agent": None,
        }

        print(f"\n🔍 Test state created: {list(test_state.keys())}")

        # Test execution with proper state format
        print("\n📋 Testing execution...")
        result = await multi_agent.arun(test_state)
        print(f"✅ Execution successful!")
        print(f"   Result type: {type(result)}")
        print(
            f"   Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
        )

    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"   Error type: {type(e).__name__}")

        # Try with string input instead
        print(f"\n🔄 Trying with string input...")
        try:
            result = await multi_agent.arun("Hello world")
            print(f"✅ String input worked!")
            print(f"   Result: {result}")
        except Exception as e2:
            print(f"❌ String input also failed: {e2}")
            import traceback

            traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(debug_multi_agent_state())
