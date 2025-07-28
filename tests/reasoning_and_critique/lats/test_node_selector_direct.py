"""Direct test for NodeSelector (bypassing import issues)."""

import asyncio
import sys

sys.path.append("/home/will/Projects/haive/backend/haive/packages/haive-agents/src")

# Import our NodeSelector directly (avoiding broken __init__.py)
import importlib.util

from haive.agents.reasoning_and_critique.lats.v3.models.evaluation_models import (
    UCBSelection,
)

# Import our models directly
from haive.agents.reasoning_and_critique.lats.v3.models.tree_models import LATSNode

# Direct imports to avoid the broken LATS __init__.py



spec = importlib.util.spec_from_file_location(
    "node_selector",
    "/home/will/Projects/haive/backend/haive/packages/haive-agents/src/haive/agents/reasoning_and_critique/lats/v3/agents/node_selector.py",
)
node_selector_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(node_selector_module)

NodeSelector = node_selector_module.NodeSelector


async def test_basic_creation():
    """Test basic NodeSelector creation."""
    print("🧪 Testing NodeSelector creation...")

    selector = NodeSelector()

    assert selector.name == "node_selector"
    assert selector.exploration_weight == 1.4
    assert selector.agent is not None

    print("✅ NodeSelector creation test passed!")


async def test_ucb_calculation():
    """Test UCB score calculation."""
    print("🧪 Testing UCB calculation...")

    selector = NodeSelector()

    # Create test nodes
    nodes = {
        "node1": LATSNode(
            action="action1", state_description="First state", visits=10, reward_sum=8.0
        ),
        "node2": LATSNode(
            action="action2", state_description="Second state", visits=5, reward_sum=4.5
        ),
        "node3": LATSNode(
            action="action3",
            state_description="Third state",
            visits=0,  # Unvisited node
            reward_sum=0.0,
        ),
    }

    ucb_scores = selector.calculate_ucb_scores(nodes)

    # Unvisited node should have highest score (infinite)
    assert ucb_scores["node3"] == float("inf")

    # Other nodes should have finite scores
    assert ucb_scores["node1"] > 0
    assert ucb_scores["node2"] > 0

    print(f"UCB scores: {ucb_scores}")
    print("✅ UCB calculation test passed!")


async def test_prompt_generation():
    """Test prompt creation."""
    print("🧪 Testing prompt generation...")

    selector = NodeSelector()

    # Create test nodes
    nodes = {
        "node1": LATSNode(
            action="Try approach A",
            state_description="Initial attempt with method A",
            visits=5,
            reward_sum=3.5,
            reflection_score=0.7,
        ),
        "node2": LATSNode(
            action="Try approach B",
            state_description="Alternative approach with method B",
            visits=3,
            reward_sum=2.8,
            reflection_score=0.85,
        ),
    }

    prompt = selector.create_selection_prompt(
        nodes=nodes,
        current_problem="Solve the equation x^2 + 5x + 6 = 0",
        search_context="Looking for mathematical solutions",
    )

    # Check that prompt contains key information
    assert "Solve the equation x^2 + 5x + 6 = 0" in prompt
    assert "Looking for mathematical solutions" in prompt
    assert "Try approach A" in prompt
    assert "Try approach B" in prompt
    assert "UCB score" in prompt

    print(f"✅ Prompt generation test passed! (Length: {len(prompt)} chars)")


async def test_real_selection():
    """Test actual node selection with real LLM."""
    print("🧪 Testing real node selection...")

    selector = NodeSelector.create(temperature=0.1)  # Low temp for consistency

    # Create test nodes representing different mathematical approaches
    nodes = {
        "factoring": LATSNode(
            action="Factor the quadratic equation",
            state_description="Attempting to find factors of x^2 + 5x + 6",
            visits=2,
            reward_sum=1.8,
            reflection_score=0.9,
            depth=1,
        ),
        "quadratic_formula": LATSNode(
            action="Use quadratic formula",
            state_description="Apply x = (-b ± √(b²-4ac)) / 2a",
            visits=1,
            reward_sum=0.7,
            reflection_score=0.6,
            depth=1,
        ),
        "completing_square": LATSNode(
            action="Complete the square",
            state_description="Rewrite in (x+h)² + k form",
            visits=0,  # Unvisited - should have high priority
            reward_sum=0.0,
            reflection_score=0.0,
            depth=1,
        ),
    }

    # Perform selection
    selection = await selector.select_node(
        nodes=nodes,
        current_problem="Solve x^2 + 5x + 6 = 0",
        search_context="Need to find the roots of this quadratic equation",
    )

    # Verify the result structure
    assert isinstance(selection, UCBSelection)
    assert selection.selected_node_id in nodes
    assert len(selection.selection_reasoning) > 0
    assert selection.ucb_score >= 0
    assert len(selection.strategy_notes) > 0

    print("✅ Real selection test passed!")
    print(f"Selected node: {selection.selected_node_id}")
    print(f"Selection reasoning: {selection.selection_reasoning[:100]}...")
    print(f"UCB score: {selection.ucb_score}")


async def main():
    """Run all tests."""
    print("🚀 Starting NodeSelector tests...\n")

    try:
        await test_basic_creation()
        print()

        await test_ucb_calculation()
        print()

        await test_prompt_generation()
        print()

        await test_real_selection()
        print()

        print("🎉 All NodeSelector tests passed! Ready for next component.")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
