"""Standalone test for LATS v3 components - avoids parent module imports."""

import asyncio
import sys
from pathlib import Path

# Add v3 directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.action_generator import ActionGenerator

# Import directly from local modules
from agents.node_selector import NodeSelector
from agents.reflection_evaluator import ReflectionEvaluator
from models.tree_models import LATSNode


async def test_lats_components():
    """Test all LATS v3 components work correctly."""
    print("\n🧪 LATS v3 Component Test")
    print("=" * 70)

    # Test data
    problem = "Navigate maze to find treasure"
    goal = "Reach the center of the maze"

    # Create test nodes
    nodes = {
        "node1": LATSNode(
            node_id="node1",
            action="Take left path",
            state_description="In dark corridor",
            visits=5,
            reward_sum=3.5,
        ),
        "node2": LATSNode(
            node_id="node2",
            action="Take right path",
            state_description="In narrow passage",
            visits=0,  # Unvisited
            reward_sum=0.0,
        ),
    }

    # Test 1: NodeSelector
    print("\n1️⃣ Testing NodeSelector...")
    selector = NodeSelector()
    selection = await selector.select_node(nodes, problem)
    print(f"✅ Selected: {selection.selected_node_id}")
    print(f"   UCB Score: {selection.ucb_score}")

    # Test 2: ActionGenerator
    print("\n2️⃣ Testing ActionGenerator...")
    generator = ActionGenerator(num_candidates=3)
    selected_node = nodes[selection.selected_node_id]
    actions = await generator.generate_actions(selected_node, problem)
    print(f"✅ Generated {len(actions.candidate_actions)} actions")
    for i, action in enumerate(actions.candidate_actions[:2], 1):
        print(f"   {i}. {action.action} (conf: {action.confidence:.1f})")

    # Test 3: ReflectionEvaluator
    print("\n3️⃣ Testing ReflectionEvaluator...")
    evaluator = ReflectionEvaluator()
    evaluation = await evaluator.evaluate_actions(
        selected_node, actions.candidate_actions, problem, goal
    )
    print("✅ Evaluated actions")
    best = evaluator.get_best_action(evaluation)
    if best:
        print(f"   Best: {best.action} (score: {best.score:.2f})")

    print("\n✅ All components working correctly!")


if __name__ == "__main__":
    asyncio.run(test_lats_components())
