"""Test simple multi-agent implementation."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.messages import HumanMessage

# Fix forward reference issue
from haive.agents.base.agent import Agent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt import multi_agent_state
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


multi_agent_state.Agent = Agent
MultiAgentState.model_rebuild()

# Fix AgentNodeV3Config forward reference
from haive.core.graph.node import agent_node_v3
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config


agent_node_v3.Agent = Agent
AgentNodeV3Config.model_rebuild()


def test_simple_multi_agent():
    """Test simple multi-agent with AgentNodeV3."""
    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    agents_dict = {"agent1": agent1, "agent2": agent2}

    # Create initial state with agents
    state = MultiAgentState(
        messages=[HumanMessage(content="What is 2+2?")], agents=agents_dict
    )

    # Create agent node for agent1
    agent1_node = create_agent_node_v3(
        agent_name="agent1", agent=agent1, name="test_agent1_node"
    )

    # Test node execution
    try:
        result = agent1_node(state)
        if hasattr(result, "messages"):
            pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_simple_multi_agent()
