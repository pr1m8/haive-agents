"""Test simple multi-agent implementation."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt import multi_agent_state
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.messages import HumanMessage

# Fix forward reference issue
from haive.agents.base.agent import Agent
from haive.agents.simple.agent import SimpleAgent

multi_agent_state.Agent = Agent
MultiAgentState.model_rebuild()

# Fix AgentNodeV3Config forward reference
from haive.core.graph.node import agent_node_v3
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config

agent_node_v3.Agent = Agent
AgentNodeV3Config.model_rebuild()


def test_simple_multi_agent():
    """Test simple multi-agent with AgentNodeV3."""
    print("=== SIMPLE MULTI-AGENT TEST ===")

    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    agents_dict = {"agent1": agent1, "agent2": agent2}

    # Create initial state with agents
    print("\n1. Creating state with agents:")
    state = MultiAgentState(
        messages=[HumanMessage(content="What is 2+2?")], agents=agents_dict
    )
    print(f"   State.agents keys: {list(state.agents.keys())}")
    print(f"   State.messages: {len(state.messages)} messages")

    # Create agent node for agent1
    print("\n2. Creating agent node for agent1:")
    agent1_node = create_agent_node_v3(
        agent_name="agent1", agent=agent1, name="test_agent1_node"
    )
    print(f"   Node created: {agent1_node.name}")
    print(f"   Node agent_name: {agent1_node.agent_name}")

    # Test node execution
    print("\n3. Testing node execution:")
    try:
        result = agent1_node(state)
        print("   ✅ Node executed successfullyy")
        print(f"   Result type: {type(result)}")
        print(f"   Result has messages: {hasattr(result, 'messages')}")
        if hasattr(result, "messages"):
            print(f"   Result messages: {len(result.messages)}")

    except Exception as e:
        print(f"   ❌ Node execution failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Simple multi-agent test completed")


if __name__ == "__main__":
    test_simple_multi_agent()
