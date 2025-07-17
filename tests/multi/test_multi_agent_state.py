"""Test building multi-agent state schema properly."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt import multi_agent_state
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.messages import HumanMessage

# Fix forward reference issue
from haive.agents.base.agent import Agent
from haive.agents.simple.agent import SimpleAgent

multi_agent_state.Agent = Agent
MultiAgentState.model_rebuild()


def test_basic_multi_agent_state():
    """Test basic multi-agent state creation."""
    print("=== BASIC MULTI-AGENT STATE TEST ===")

    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    agents_dict = {"agent1": agent1, "agent2": agent2}

    # Test 1: Create state with agents dict
    print("\n1. Creating state with agents dict:")
    state = MultiAgentState(
        messages=[HumanMessage(content="Hello")], agents=agents_dict
    )
    print(f"   State.agents keys: {list(state.agents.keys())}")
    print(f"   State.agents['agent1']: {state.agents['agent1'].name}")

    # Test 2: Create state with agents list
    print("\n2. Creating state with agents list:")
    state2 = MultiAgentState(
        messages=[HumanMessage(content="Hello")], agents=[agent1, agent2]
    )
    print(f"   State.agents keys: {list(state2.agents.keys())}")
    print(f"   State.agents['agent1']: {state2.agents['agent1'].name}")

    # Test 3: Create state with no agents (should be empty dict)
    print("\n3. Creating state with no agents:")
    state3 = MultiAgentState(messages=[HumanMessage(content="Hello")])
    print(f"   State.agents keys: {list(state3.agents.keys())}")
    print(f"   State.agents type: {type(state3.agents)}")

    # Test 4: Test set_active_agent method
    print("\n4. Testing set_active_agent:")
    try:
        state.set_active_agent("agent1")
        print(f"   Active agent: {state.active_agent}")
    except Exception as e:
        print(f"   Error: {e}")

    print("\n✅ Basic multi-agent state tests completed")


if __name__ == "__main__":
    test_basic_multi_agent_state()
