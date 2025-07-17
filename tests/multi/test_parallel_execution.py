"""Test parallel execution with ProperMultiAgent."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


def test_parallel_execution():
    """Test ProperMultiAgent with parallel execution."""
    print("=== PARALLEL EXECUTION TEST ===")

    # Create agents with different tasks
    agent1 = SimpleAgent(
        name="researcher",
        engine=AugLLMConfig(
            system_message="You are a researcher. Research the given topic."
        ),
    )
    agent2 = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="You are an analyzer. Analyze the given topic."
        ),
    )
    agent3 = SimpleAgent(
        name="summarizer",
        engine=AugLLMConfig(
            system_message="You are a summarizer. Summarize the given topic."
        ),
    )

    # Create ProperMultiAgent with parallel execution
    print("\n1. Creating ProperMultiAgent with parallel execution:")
    multi = ProperMultiAgent(
        name="parallel_test",
        agents=[agent1, agent2, agent3],
        execution_mode="parallel",
        parallel_wait_for_all=True,
    )
    print(f"   Multi.agents: {list(multi.agents.keys())}")
    print(f"   Execution mode: {multi.execution_mode}")
    print(f"   Wait for all: {multi.parallel_wait_for_all}")

    # Test graph construction
    print("\n2. Testing graph construction:")
    try:
        graph = multi.build_graph()
        print(f"   ✅ Graph built successfully")
        print(f"   Graph nodes: {list(graph.nodes.keys())}")
        print(f"   Graph edges: {list(graph.edges)}")

        # Check if gather node exists
        if "gather" in graph.nodes:
            print(f"   ✅ Gather node exists for parallel coordination")

    except Exception as e:
        print(f"   ❌ Graph construction failed: {e}")
        import traceback

        traceback.print_exc()

    # Test state creation
    print("\n3. Testing state creation:")
    try:
        state = multi.state_schema(
            messages=[HumanMessage(content="Analyze the benefits of renewable energy")]
        )
        print(f"   ✅ State created successfully")
        print(f"   State.agents: {list(state.agents.keys())}")
        print(f"   State.messages: {len(state.messages)}")

    except Exception as e:
        print(f"   ❌ State creation failed: {e}")
        import traceback

        traceback.print_exc()

    # Test parallel execution (this would run all agents simultaneously)
    print("\n4. Testing parallel execution:")
    try:
        input_data = {
            "messages": [
                HumanMessage(content="What are the benefits of renewable energy?")
            ]
        }
        result = multi.invoke(input_data)
        print(f"   ✅ Parallel execution completed")
        print(f"   Result type: {type(result)}")
        if hasattr(result, "messages"):
            print(f"   Final messages: {len(result.messages)}")
            print(f"   All agents contributed: {len(result.messages) > 1}")

    except Exception as e:
        print(f"   ❌ Parallel execution failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Parallel execution test completed")


def test_branch_execution():
    """Test ProperMultiAgent with branch execution."""
    print("\n=== BRANCH EXECUTION TEST ===")

    # Create agents for branching
    decision_agent = SimpleAgent(
        name="decision_maker",
        engine=AugLLMConfig(
            system_message="You are a decision maker. Decide which path to take."
        ),
    )
    path_a_agent = SimpleAgent(
        name="path_a",
        engine=AugLLMConfig(system_message="You handle path A scenarios."),
    )
    path_b_agent = SimpleAgent(
        name="path_b",
        engine=AugLLMConfig(system_message="You handle path B scenarios."),
    )

    # Create ProperMultiAgent with branch execution
    print("\n1. Creating ProperMultiAgent with branch execution:")
    multi = ProperMultiAgent(
        name="branch_test",
        agents=[decision_agent, path_a_agent, path_b_agent],
        execution_mode="branch",
        branch_condition='result_type == "complex"',
    )
    print(f"   Multi.agents: {list(multi.agents.keys())}")
    print(f"   Execution mode: {multi.execution_mode}")
    print(f"   Branch condition: {multi.branch_condition}")

    # Test graph construction
    print("\n2. Testing branch graph construction:")
    try:
        graph = multi.build_graph()
        print(f"   ✅ Branch graph built successfully")
        print(f"   Graph nodes: {list(graph.nodes.keys())}")
        print(f"   Graph edges: {list(graph.edges)}")

        # Check if branch router exists
        if "branch_router" in graph.nodes:
            print(f"   ✅ Branch router node exists")

    except Exception as e:
        print(f"   ❌ Branch graph construction failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Branch execution test completed")


if __name__ == "__main__":
    test_parallel_execution()
    test_branch_execution()
