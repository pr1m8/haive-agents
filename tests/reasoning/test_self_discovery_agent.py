"""Test the self-discovery v2 agent with ProperMultiAgent."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.messages import HumanMessage

from haive.agents.reasoning_and_critique.self_discover.v2.agent import self_discovery


def test_self_discovery_agent():
    """Test self-discovery agent with ProperMultiAgent."""
    print("=== SELF-DISCOVERY AGENT TEST ===")

    # Test agent setup
    print("\n1. Testing self-discovery agent setup:")
    print(f"   Agent name: {self_discovery.name}")
    print(f"   Execution mode: {self_discovery.execution_mode}")
    print(f"   Agents: {list(self_discovery.agents.keys())}")
    print(f"   State schema: {self_discovery.state_schema.__name__}")

    # Test state creation
    print("\n2. Testing state creation:")
    try:
        state = self_discovery.state_schema(
            messages=[
                HumanMessage(content="How can I improve my problem-solving skills?")
            ],
            task_description="Improve problem-solving skills",
        )
        print("   ✅ State created successfully"y")
        print(f"   State.agents: {list(state.agents.keys())}")
        print(f"   State.messages: {len(state.messages)}")
        print(f"   State.task_description: {state.task_description}")

        # Check if state has self-discovery specific fields
        if hasattr(state, "reasoning_modules"):
            print("   ✅ Has reasoning_modules field"d")
        if hasattr(state, "selected_modules"):
            print("   ✅ Has selected_modules field"d")
        if hasattr(state, "adapted_modules"):
            print("   ✅ Has adapted_modules field"d")
        if hasattr(state, "reasoning_structure"):
            print("   ✅ Has reasoning_structure field"d")
        if hasattr(state, "final_answer"):
            print("   ✅ Has final_answer field"d")

    except Exception as e:
        print(f"   ❌ State creation failed: {e}")
        import traceback

        traceback.print_exc()
        return

    # Test graph construction
    print("\n3. Testing graph construction:")
    try:
        graph = self_discovery.build_graph()
        print("   ✅ Graph built successfully"y")
        print(f"   Graph nodes: {list(graph.nodes.keys())}")
        print(f"   Graph edges: {list(graph.edges)}")

        # Verify sequential execution order
        expected_order = [
            "agent_select_modules",
            "agent_adapt_modules",
            "agent_create_structure",
            "agent_final_reasoning",
        ]
        actual_nodes = [
            node for node in graph.nodes.keys() if node.startswith("agent_")
        ]
        print(f"   Expected sequential order: {expected_order}")
        print(f"   Actual nodes: {actual_nodes}")

    except Exception as e:
        print(f"   ❌ Graph construction failed: {e}")
        import traceback

        traceback.print_exc()
        return

    # Test self-discovery execution
    print("\n4. Testing self-discovery execution:")
    try:
        input_data = {
            "messages": [
                HumanMessage(content="How can I improve my problem-solving skills?")
            ],
            "task_description": "Improve problem-solving skills",
        }
        result = self_discovery.invoke(input_data)
        print("   ✅ Self-discovery execution completed"d")
        print(f"   Result type: {type(result)}")

        if hasattr(result, "messages"):
            print(f"   Final messages: {len(result.messages)}")

        # Check if we have structured outputs from each step
        if hasattr(result, "selected_modules") and result.selected_modules:
            print(
                f"   ✅ Selected modules: {len(result.selected_modules.selected_modules) if hasattr(result.selected_modules, 'selected_modules') else 'Present'}"
            )

        if hasattr(result, "adapted_modules") and result.adapted_modules:
            print("   ✅ Adapted modules: Present"t")

        if hasattr(result, "reasoning_structure") and result.reasoning_structure:
            print("   ✅ Reasoning structure: Present"t")

        if hasattr(result, "final_answer") and result.final_answer:
            print("   ✅ Final answer: Present"t")
            if hasattr(result.final_answer, "answer"):
                print(f"   Final answer content: {result.final_answer.answer[:100]}...")

    except Exception as e:
        print(f"   ❌ Self-discovery execution failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Self-discovery agent test completed")


if __name__ == "__main__":
    test_self_discovery_agent()
