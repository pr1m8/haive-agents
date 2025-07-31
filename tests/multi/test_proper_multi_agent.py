"""Test ProperMultiAgent with basic MultiAgentState."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

import contextlib

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_proper_multi_agent():
    """Test ProperMultiAgent with basic MultiAgentState."""
    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create ProperMultiAgent
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Test state creation
    try:
        state = multi.state_schema(messages=[HumanMessage(content="Hello")])

        # Test if it has MultiAgentState features
        if hasattr(state, "set_active_agent"):
            with contextlib.suppress(Exception):
                state.set_active_agent("agent1")

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_proper_multi_agent()
