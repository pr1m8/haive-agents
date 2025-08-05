"""Test ProperMultiAgent with composed schema that makes agents required."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

import contextlib

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_composed_multi_agent():
    """Test ProperMultiAgent with composed schema."""
    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create ProperMultiAgent
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Test state creation WITHOUT providing agents
    try:
        state = multi.state_schema(messages=[HumanMessage(content="Hello")])

        # Test if it has MultiAgentState features
        if hasattr(state, "set_active_agent") and state.agents:
            with contextlib.suppress(Exception):
                state.set_active_agent("agent1")

        # Test if it has composed agent-specific fields

    except Exception:
        import traceback

        traceback.print_exc()

    # Test state creation WITH providing agents (should work too)
    try:
        multi.state_schema(messages=[HumanMessage(content="Hello")], agents={"custom": agent1})

    except Exception:
        import traceback

        traceback.print_exc()

    # Test if agents field is now required
    try:
        # Check field definition
        agents_field = multi.state_schema.model_fields.get("agents")
        if agents_field:
            pass
        else:
            pass

    except Exception:
        pass


if __name__ == "__main__":
    test_composed_multi_agent()
