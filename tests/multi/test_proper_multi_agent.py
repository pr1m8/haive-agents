"""Test ProperMultiAgent with basic MultiAgentState."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


def test_proper_multi_agent():
    """Test ProperMultiAgent with basic MultiAgentState."""
    print("=== PROPER MULTI-AGENT TEST ===")

    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create ProperMultiAgent
    print("\n1. Creating ProperMultiAgent:")
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )
    print(f"   Multi.agents: {list(multi.agents.keys())}")
    print(f"   State schema: {multi.state_schema.__name__}")

    # Test state creation
    print("\n2. Testing state creation:")
    try:
        state = multi.state_schema(messages=[HumanMessage(content="Hello")])
        print("   ✅ State created successfully")
        print(f"   State.agents: {list(state.agents.keys())}")
        print(f"   State.messages: {len(state.messages)}")

        # Test if it has MultiAgentState features
        if hasattr(state, "set_active_agent"):
            print("   ✅ Has set_active_agent method")
            try:
                state.set_active_agent("agent1")
                print(f"   ✅ set_active_agent works: {state.active_agent}")
            except Exception as e:
                print(f"   ❌ set_active_agent failed: {e}")

    except Exception as e:
        print(f"   ❌ State creation failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ ProperMultiAgent test completed")


if __name__ == "__main__":
    test_proper_multi_agent()
