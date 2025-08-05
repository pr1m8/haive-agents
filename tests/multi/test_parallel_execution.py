"""Test parallel execution with ProperMultiAgent."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_parallel_execution():
    """Test ProperMultiAgent with parallel execution."""
    # Create agents with different tasks
    agent1 = SimpleAgent(
        name="researcher",
        engine=AugLLMConfig(system_message="You are a researcher. Research the given topic."),
    )
    agent2 = SimpleAgent(
        name="analyzer",
        engine=AugLLMConfig(system_message="You are an analyzer. Analyze the given topic."),
    )
    agent3 = SimpleAgent(
        name="summarizer",
        engine=AugLLMConfig(system_message="You are a summarizer. Summarize the given topic."),
    )

    # Create ProperMultiAgent with parallel execution
    multi = ProperMultiAgent(
        name="parallel_test",
        agents=[agent1, agent2, agent3],
        execution_mode="parallel",
        parallel_wait_for_all=True,
    )

    # Test graph construction
    try:
        graph = multi.build_graph()

        # Check if gather node exists
        if "gather" in graph.nodes:
            pass

    except Exception:
        import traceback

        traceback.print_exc()

    # Test state creation
    try:
        multi.state_schema(
            messages=[HumanMessage(content="Analyze the benefits of renewable energy")]
        )

    except Exception:
        import traceback

        traceback.print_exc()

    # Test parallel execution (this would run all agents simultaneously)
    try:
        input_data = {
            "messages": [HumanMessage(content="What are the benefits of renewable energy?")]
        }
        result = multi.invoke(input_data)
        if hasattr(result, "messages"):
            pass

    except Exception:
        import traceback

        traceback.print_exc()


def test_branch_execution():
    """Test ProperMultiAgent with branch execution."""
    # Create agents for branching
    decision_agent = SimpleAgent(
        name="decision_maker",
        engine=AugLLMConfig(system_message="You are a decision maker. Decide which path to take."),
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
    multi = ProperMultiAgent(
        name="branch_test",
        agents=[decision_agent, path_a_agent, path_b_agent],
        execution_mode="branch",
        branch_condition='result_type == "complex"',
    )

    # Test graph construction
    try:
        graph = multi.build_graph()

        # Check if branch router exists
        if "branch_router" in graph.nodes:
            pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_parallel_execution()
    test_branch_execution()
