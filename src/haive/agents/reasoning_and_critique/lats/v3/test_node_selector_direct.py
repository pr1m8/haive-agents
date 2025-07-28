"""Direct test of NodeSelector agent - avoids import issues."""

import asyncio
import sys
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

from haive.agents.reasoning_and_critique.lats.v3.agents.node_selector import (
    NodeSelector,
)
from haive.agents.reasoning_and_critique.lats.v3.models.evaluation_models import (
    UCBSelection,
)
from haive.agents.reasoning_and_critique.lats.v3.models.tree_models import LATSNode


async def test_node_selector():
    """Test the NodeSelector agent with real execution."""
    print("\n🧪 Testing NodeSelector Agent for LATS v3")
    print("=" * 60)

    # Create NodeSelector
    print("\n1. Creating NodeSelector...")
    selector = NodeSelector(name="lats_node_selector", exploration_weight=1.4)
    print(f"✅ Created NodeSelector: {selector.name}")
    print(f"   - Exploration weight: {selector.exploration_weight}")
    print(f"   - Agent type: {type(selector.agent).__name__}")

    # Test Case 1: Single node selection
    print("\n2. Testing single node selection...")
    root = LATSNode(
        action="Initial state",
        state_description="Starting the problem solving process",
        visits=5,
        reward_sum=3.5,
        reflection_score=0.7,
        reflection_reasoning="Good starting point",
    )

    nodes = {root.node_id: root}
    problem = "Find the best path through a maze"

    result = await selector.select_node(nodes, problem)
    print(f"✅ Selected node: {result.selected_node_id[:8]}...")
    print(f"   - UCB Score: {result.ucb_score}")
    print(f"   - Reasoning: {result.selection_reasoning[:100]}...")

    # Test Case 2: Multiple nodes with different UCB scores
    print("\n3. Testing multiple node selection...")

    node1 = LATSNode(
        action="Take the left path",
        state_description="Exploring the left branch of the maze",
        visits=10,
        reward_sum=7.0,  # Average: 0.7
        reflection_score=0.7,
        reflection_reasoning="Promising direction with moderate complexity",
    )

    node2 = LATSNode(
        action="Take the right path",
        state_description="Exploring the right branch of the maze",
        visits=5,
        reward_sum=4.0,  # Average: 0.8
        reflection_score=0.8,
        reflection_reasoning="Shorter path but with obstacles",
    )

    node3 = LATSNode(
        action="Go straight ahead",
        state_description="Following the main corridor",
        visits=0,  # Unvisited - should have infinite UCB
        reward_sum=0.0,
        reflection_score=0.0,
        reflection_reasoning="Not yet explored",
    )

    nodes = {node1.node_id: node1, node2.node_id: node2, node3.node_id: node3}

    problem = "Find the optimal path through a complex maze"

    result = await selector.select_node(nodes, problem)
    print(f"✅ Selected node: {result.selected_node_id[:8]}...")
    print(f"   - UCB Score: {result.ucb_score}")
    print(f"   - Exploitation: {result.exploitation_component}")
    print(f"   - Exploration: {result.exploration_component}")
    print(f"   - Reasoning: {result.selection_reasoning[:100]}...")

    # Verify unvisited node was selected
    if result.selected_node_id == node3.node_id:
        print("✅ Correctly selected unvisited node (infinite UCB)")
    else:
        print("⚠️  Did not select unvisited node as expected")

    # Test Case 3: All visited nodes
    print("\n4. Testing selection with all visited nodes...")

    # Make all nodes visited
    node3.visits = 3
    node3.reward_sum = 1.8  # Average: 0.6

    result = await selector.select_node(nodes, problem)
    print(f"✅ Selected node: {result.selected_node_id[:8]}...")
    print(f"   - UCB Score: {result.ucb_score}")

    # Show all UCB scores for comparison
    print("\n📊 UCB Score Comparison:")
    for node_id, node in nodes.items():
        ucb = node.ucb_score(exploration_weight=1.4, parent_visits=18)  # Total visits
        print(
            f"   - {node.action}: UCB={ucb:.3f} (avg_reward={node.average_reward():.2f})"
        )

    print("\n✅ All tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_node_selector())
