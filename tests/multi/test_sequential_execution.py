"""Test sequential execution with composed multi-agent state."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3


def test_sequential_execution():
    """Test ProperMultiAgent with sequential execution."""
    # Create agents with different system messages
    agent1 = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="You are an analyzer. Analyze the input and provide insights."
        ),
    )
    agent2 = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            system_message="You are a formatter. Format the analysis into a clear summary."
        ),
    )

    # Create ProperMultiAgent
    multi = ProperMultiAgent(
        name="sequential_test", agents=[agent1, agent2], execution_mode="sequential"
    )

    # Test state creation
    state = multi.state_schema(messages=[HumanMessage(content="What is the capital of France?")])

    # Test agent node creation and execution
    try:
        # Create agent node for analyzer
        analyzer_node = create_agent_node_v3(
            agent_name="analyzer", agent=agent1, name="analyzer_node"
        )

        # Test node execution
        result = analyzer_node(state)
        if hasattr(result, "messages"):
            pass

        # Show the agents are still in the result state
        if hasattr(result, "agents"):
            pass

    except Exception:
        import traceback

        traceback.print_exc()

    # Test multi-agent execution
    try:
        # Test with simple invoke
        input_data = {"messages": [HumanMessage(content="What is 2+2?")]}
        result = multi.invoke(input_data)
        if hasattr(result, "messages"):
            for _i, _msg in enumerate(result.messages):
                pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_sequential_execution()
