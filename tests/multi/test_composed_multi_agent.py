"""Test ProperMultiAgent with composed schema that makes agents required."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


def test_composed_multi_agent():
    """Test ProperMultiAgent with composed schema."""
    print("=== COMPOSED MULTI-AGENT TEST ===")

    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create ProperMultiAgent
    print("\n1. Creating ProperMultiAgent with composed schema:")
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )
    print(f"   Multi.agents: {list(multi.agents.keys())}")
    print(f"   State schema: {multi.state_schema.__name__}")
    print(
        f"   State schema bases: {[base.__name__ for base in multi.state_schema.__bases__]}"
    )

    # Test state creation WITHOUT providing agents
    print("\n2. Testing state creation without providing agents:")
    try:
        state = multi.state_schema(messages=[HumanMessage(content="Hello")])
        print("   ✅ State created successfullyy")
        print(f"   State.agents: {list(state.agents.keys())}")
        print(f"   State.messages: {len(state.messages)}")
        print(f"   State type: {type(state).__name__}")

        # Test if it has MultiAgentState features
        if hasattr(state, "set_active_agent"):
            print("   ✅ Has set_active_agent methodd")
            if state.agents:
                try:
                    state.set_active_agent("agent1")
                    print(f"   ✅ set_active_agent works: {state.active_agent}")
                except Exception as e:
                    print(f"   ❌ set_active_agent failed: {e}")

        # Test if it has composed agent-specific fields
        print(f"   State fields: {list(state.model_fields.keys())}")

    except Exception as e:
        print(f"   ❌ State creation failed: {e}")
        import traceback

        traceback.print_exc()

    # Test state creation WITH providing agents (should work too)
    print("\n3. Testing state creation WITH providing agents:")
    try:
        state2 = multi.state_schema(
            messages=[HumanMessage(content="Hello")], agents={"custom": agent1}
        )
        print("   ✅ State created successfullyy")
        print(f"   State.agents: {list(state2.agents.keys())}")

    except Exception as e:
        print(f"   ❌ State creation with agents failed: {e}")
        import traceback

        traceback.print_exc()

    # Test if agents field is now required
    print("\n4. Testing if agents field is required:")
    try:
        # Check field definition
        agents_field = multi.state_schema.model_fields.get("agents")
        if agents_field:
            print(f"   Agents field default: {agents_field.default}")
            print(f"   Agents field is required: {agents_field.is_required()}")
        else:
            print("   ❌ Agents field not found in schema")

    except Exception as e:
        print(f"   ❌ Field check failed: {e}")

    print("\n✅ Composed multi-agent test completed")


if __name__ == "__main__":
    test_composed_multi_agent()
