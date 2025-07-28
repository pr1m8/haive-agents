"""Test the NodeSelector agent for LATS algorithm."""

import pytest

from haive.agents.reasoning_and_critique.lats.v3.agents.node_selector import (
    NodeSelector,
    create_node_selector,
)
from haive.agents.reasoning_and_critique.lats.v3.models.evaluation_models import (
    UCBSelection,
)
from haive.agents.reasoning_and_critique.lats.v3.models.tree_models import LATSNode


@pytest.mark.asyncio
async def test_node_selector_creation():
    """Test that NodeSelector can be created with default settings."""
    selector = NodeSelector()

    assert selector.name == "node_selector"
    assert selector.exploration_weight == 1.4
    assert selector.agent is not None


@pytest.mark.asyncio
async def test_node_selector_create_factory():
    """Test the create factory method."""
    selector = NodeSelector.create(
        name="test_selector", exploration_weight=2.0, temperature=0.1
    )

    assert selector.name == "test_selector"
    assert selector.exploration_weight == 2.0


@pytest.mark.asyncio
async def test_node_selector_ucb_calculation():
    """Test UCB score calculation utility."""
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


@pytest.mark.asyncio
async def test_node_selector_prompt_creation():
    """Test prompt creation for node selection."""
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
    assert str(selector.exploration_weight) in prompt

    print(f"Generated prompt length: {len(prompt)}")
    print(f"Prompt preview: {prompt[:200]}...")


@pytest.mark.asyncio
async def test_node_selector_real_selection():
    """Test actual node selection with real LLM."""
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

    print(f"Selected node: {selection.selected_node_id}")
    print(f"Selection reasoning: {selection.selection_reasoning}")
    print(f"UCB score: {selection.ucb_score}")
    print(f"Strategy notes: {selection.strategy_notes}")

    # The unvisited node should likely be selected due to infinite UCB
    # But we don't enforce this since the LLM might have strategic reasons
    print(f"Alternatives considered: {len(selection.alternative_nodes)}")


@pytest.mark.asyncio
async def test_convenience_function():
    """Test the convenience creation function."""
    selector = create_node_selector(exploration_weight=1.8, temperature=0.2)

    assert selector.exploration_weight == 1.8
    assert selector.name == "node_selector"


if __name__ == "__main__":
    import asyncio

    async def run_tests():
        """Run tests individually for debugging."""
        print("Testing NodeSelector creation...")
        await test_node_selector_creation()
        print("✅ Creation test passed")

        print("\nTesting UCB calculation...")
        await test_node_selector_ucb_calculation()
        print("✅ UCB calculation test passed")

        print("\nTesting prompt creation...")
        await test_node_selector_prompt_creation()
        print("✅ Prompt creation test passed")

        print("\nTesting real node selection...")
        await test_node_selector_real_selection()
        print("✅ Real selection test passed")

        print("\n🎉 All NodeSelector tests passed!")

    asyncio.run(run_tests())
