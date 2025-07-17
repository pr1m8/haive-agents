"""Test sequential execution with composed multi-agent state."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


def test_sequential_execution():
    """Test ProperMultiAgent with sequential execution."""
    print("=== SEQUENTIAL EXECUTION TEST ===")

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
    print("\n1. Creating ProperMultiAgent:")
    multi = ProperMultiAgent(
        name="sequential_test", agents=[agent1, agent2], execution_mode="sequential"
    )
    print(f"   Multi.agents: {list(multi.agents.keys())}")
    print(f"   State schema: {multi.state_schema.__name__}")

    # Test state creation
    print("\n2. Testing state creation:")
    state = multi.state_schema(
        messages=[HumanMessage(content="What is the capital of France?")]
    )
    print(f"   ✅ State created successfully")
    print(f"   State.agents: {list(state.agents.keys())}")
    print(f"   State.messages: {len(state.messages)}")

    # Test agent node creation and execution
    print("\n3. Testing agent node creation:")
    try:
        # Create agent node for analyzer
        analyzer_node = create_agent_node_v3(
            agent_name="analyzer", agent=agent1, name="analyzer_node"
        )
        print(f"   ✅ Analyzer node created: {analyzer_node.name}")

        # Test node execution
        print("\n4. Testing node execution:")
        result = analyzer_node(state)
        print(f"   ✅ Node executed successfully")
        print(f"   Result type: {type(result)}")
        print(f"   Result has messages: {hasattr(result, 'messages')}")
        if hasattr(result, "messages"):
            print(f"   Result messages: {len(result.messages)}")

        # Show the agents are still in the result state
        if hasattr(result, "agents"):
            print(f"   Result.agents: {list(result.agents.keys())}")

    except Exception as e:
        print(f"   ❌ Node execution failed: {e}")
        import traceback

        traceback.print_exc()

    # Test multi-agent execution
    print("\n5. Testing multi-agent execution:")
    try:
        # Test with simple invoke
        input_data = {"messages": [HumanMessage(content="What is 2+2?")]}
        result = multi.invoke(input_data)
        print(f"   ✅ Multi-agent execution completed")
        print(f"   Result type: {type(result)}")
        if hasattr(result, "messages"):
            print(f"   Final messages: {len(result.messages)}")
            for i, msg in enumerate(result.messages):
                print(f"     Message {i}: {msg.content[:50]}...")

    except Exception as e:
        print(f"   ❌ Multi-agent execution failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Sequential execution test completed")


if __name__ == "__main__":
    test_sequential_execution()
