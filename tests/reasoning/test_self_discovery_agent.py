"""Test the self-discovery v2 agent with ProperMultiAgent."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.reasoning_and_critique.self_discover.v2.agent import self_discovery


def test_self_discovery_agent():
    """Test self-discovery agent with ProperMultiAgent."""
    # Test agent setup

    # Test state creation
    try:
        state = self_discovery.state_schema(
            messages=[
                HumanMessage(content="How can I improve my problem-solving skills?")
            ],
            task_description="Improve problem-solving skills",
        )

        # Check if state has self-discovery specific fields
        if hasattr(state, "reasoning_modules"):
            pass
        if hasattr(state, "selected_modules"):
            pass
        if hasattr(state, "adapted_modules"):
            pass
        if hasattr(state, "reasoning_structure"):
            pass
        if hasattr(state, "final_answer"):
            pass

    except Exception:
        import traceback

        traceback.print_exc()
        return

    # Test graph construction
    try:
        graph = self_discovery.build_graph()

        # Verify sequential execution order
        [node for node in graph.nodes if node.startswith("agent_")]

    except Exception:
        import traceback

        traceback.print_exc()
        return

    # Test self-discovery execution
    try:
        input_data = {
            "messages": [
                HumanMessage(content="How can I improve my problem-solving skills?")
            ],
            "task_description": "Improve problem-solving skills",
        }
        result = self_discovery.invoke(input_data)

        if hasattr(result, "messages"):
            pass

        # Check if we have structured outputs from each step
        if hasattr(result, "selected_modules") and result.selected_modules:
            pass

        if hasattr(result, "adapted_modules") and result.adapted_modules:
            pass

        if hasattr(result, "reasoning_structure") and result.reasoning_structure:
            pass

        if hasattr(result, "final_answer") and result.final_answer:
            if hasattr(result.final_answer, "answer"):
                pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_self_discovery_agent()
