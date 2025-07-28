"""Test all LATS v3 components together."""

import asyncio

from haive.agents.reasoning_and_critique.lats.v3.agents.action_generator import (
    ActionGenerator,
)
from haive.agents.reasoning_and_critique.lats.v3.agents.node_selector import (
    NodeSelector,
)
from haive.agents.reasoning_and_critique.lats.v3.agents.reflection_evaluator import (
    ReflectionEvaluator,
)
from haive.agents.reasoning_and_critique.lats.v3.models.tree_models import LATSNode


async def test_lats_v3_pipeline():
    """Test complete LATS v3 pipeline."""
    print("\n🧪 LATS v3 Complete Pipeline Test")
    print("=" * 60)

    # Test scenario
    problem = "Navigate through a complex maze to find the treasure"
    goal = "Reach the treasure at the center of the maze"

    # Create test nodes
    nodes = {
        "left": LATSNode(
            node_id="left",
            action="Take left corridor",
            state_description="Dark corridor with symbols on walls",
            visits=5,
            reward_sum=3.5,
            depth=1,
        ),
        "center": LATSNode(
            node_id="center",
            action="Take center path",
            state_description="Well-lit hall with visible traps",
            visits=3,
            reward_sum=2.1,
            depth=1,
        ),
        "right": LATSNode(
            node_id="right",
            action="Take right passage",
            state_description="Narrow unexplored passage",
            visits=0,  # Unvisited
            reward_sum=0.0,
            depth=1,
        ),
    }

    # Step 1: Node Selection
    print("\n1️⃣ Node Selection (UCB)")
    selector = NodeSelector(exploration_weight=1.4)
    selection = await selector.select_node(nodes, problem)
    print(f"✅ Selected: {selection.selected_node_id}")
    print(f"   Reasoning: {selection.selection_reasoning[:100]}...")

    selected_node = nodes[selection.selected_node_id]

    # Step 2: Action Generation
    print("\n2️⃣ Action Generation")
    generator = ActionGenerator(num_candidates=3)
    actions = await generator.generate_actions(selected_node, problem)
    print(f"✅ Generated {len(actions.candidate_actions)} actions:")
    for i, action in enumerate(actions.candidate_actions, 1):
        print(f"   {i}. {action.action} (conf: {action.confidence:.1f})")

    # Step 3: Reflection & Evaluation
    print("\n3️⃣ Reflection & Evaluation")
    evaluator = ReflectionEvaluator()
    evaluation = await evaluator.evaluate_actions(
        selected_node, actions.candidate_actions, problem, goal
    )

    print("✅ Evaluated actions:")
    for i, scored in enumerate(evaluation.scored_actions[:3], 1):
        print(f"   {i}. {scored.action} - Score: {scored.score:.2f}")

    best = evaluator.get_best_action(evaluation)
    if best:
        print(f"\n🏆 Best Action: '{best.action}'")
        print(f"   Score: {best.score:.2f}")
        print(f"   Reasoning: {best.reasoning[:100]}...")

    print("\n✅ LATS v3 Pipeline Complete!")
    print("\nNext Steps (TODO):")
    print("- Execute best action")
    print("- Create new node in tree")
    print("- Backpropagate rewards")
    print("- Repeat MCTS iterations")


if __name__ == "__main__":
    asyncio.run(test_lats_v3_pipeline())
