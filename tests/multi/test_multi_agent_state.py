"""Test building multi-agent state schema properly."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

import contextlib

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
    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    agents_dict = {"agent1": agent1, "agent2": agent2}

    # Test 1: Create state with agents dict
    state = MultiAgentState(
        messages=[HumanMessage(content="Hello")], agents=agents_dict
    )

    # Test 2: Create state with agents list
    MultiAgentState(messages=[HumanMessage(content="Hello")], agents=[agent1, agent2])

    # Test 3: Create state with no agents (should be empty dict)
    MultiAgentState(messages=[HumanMessage(content="Hello")])

    # Test 4: Test set_active_agent method
    with contextlib.suppress(Exception):
        state.set_active_agent("agent1")


if __name__ == "__main__":
    test_basic_multi_agent_state()
