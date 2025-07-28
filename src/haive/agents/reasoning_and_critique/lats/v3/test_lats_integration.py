"""Integration test for all LATS v3 components."""

import asyncio
from typing import Dict, List

from agents.action_generator import ActionGenerator

# Direct imports to avoid parent module issues
from agents.node_selector import NodeSelector
from agents.reflection_evaluator import ReflectionEvaluator
from models.action_models import CandidateAction
from models.evaluation_models import ReflectionEvaluation, UCBSelection
from models.tree_models import LATSNode


async def test_full_lats_workflow():
    """Test complete LATS workflow with all components."""
    print("\n🧪 LATS v3 Full Integration Test")
    print("=" * 70)

    # Initialize all agents
    print("\n1️⃣ Initializing LATS Agents...")
    selector = NodeSelector(name="lats_selector", exploration_weight=1.4)
    generator = ActionGenerator(name="lats_generator", num_candidates=5)
    evaluator = ReflectionEvaluator(name="lats_evaluator", temperature=0.3)
    print("✅ All agents initialized")

    # Create test scenario - maze navigation
    print("\n2️⃣ Setting up test scenario...")
    problem = "Navigate through a complex maze to find the treasure at the center"
    goal = "Reach the treasure room at the center of the maze"

    # Create initial nodes representing different paths explored
    nodes = {
        "root": LATSNode(
            node_id="root",
            action="Start at maze entrance",
            state_description="Standing at the south entrance of the maze",
            depth=0,
            visits=10,
            reward_sum=5.0,
            reflection_score=0.5,
        ),
        "left_path": LATSNode(
            node_id="left_path",
            parent_id="root",
            action="Take the left corridor",
            state_description="In a dark corridor with ancient symbols on walls",
            depth=1,
            visits=5,
            reward_sum=3.0,
            reflection_score=0.6,
            reflection_reasoning="Shows promise but needs more exploration",
        ),
        "center_path": LATSNode(
            node_id="center_path",
            parent_id="root",
            action="Take the center path",
            state_description="In a well-lit hall with traps visible",
            depth=1,
            visits=3,
            reward_sum=2.1,
            reflection_score=0.7,
            reflection_reasoning="Direct route but dangerous",
        ),
        "right_unexplored": LATSNode(
            node_id="right_unexplored",
            parent_id="root",
            action="Take the right passage",
            state_description="Narrow passage leading into darkness",
            depth=1,
            visits=0,  # Unvisited - should have high UCB
            reward_sum=0.0,
            reflection_score=0.0,
        ),
    }

    print(f"✅ Created {len(nodes)} nodes in search tree")
    print("\n📊 Current Tree State:")
    for node_id, node in nodes.items():
        ucb = node.ucb_score(1.4, sum(n.visits for n in nodes.values()))
        print(
            f"  - {node_id}: visits={node.visits}, avg_reward={node.average_reward():.2f}, UCB={ucb:.2f}"
        )

    # Step 1: Node Selection
    print("\n3️⃣ Node Selection Phase...")
    print("🤖 Selecting best node for expansion using UCB...")

    try:
        selection_result = await selector.select_node(nodes, problem)
        print(f"\n✅ Selected Node: {selection_result.selected_node_id}")
        print(f"   UCB Score: {selection_result.ucb_score}")
        print(f"   Reasoning: {selection_result.selection_reasoning[:150]}...")

        selected_node = nodes[selection_result.selected_node_id]

    except Exception as e:
        print(f"❌ Node selection failed: {e}")
        return

    # Step 2: Action Generation
    print("\n4️⃣ Action Generation Phase...")
    print(
        f"🤖 Generating {generator.num_candidates} candidate actions for selected node..."
    )

    try:
        search_history = [
            "Started at south entrance",
            "Explored left corridor partially",
            "Checked center path but found traps",
        ]

        action_result = await generator.generate_actions(
            selected_node, problem, search_history
        )

        print(f"\n✅ Generated {len(action_result.candidate_actions)} actions:")
        for i, action in enumerate(action_result.candidate_actions, 1):
            print(f"\n   {i}. {action.action}")
            print(f"      Confidence: {action.confidence:.2f}")

    except Exception as e:
        print(f"❌ Action generation failed: {e}")
        return

    # Step 3: Reflection and Evaluation
    print("\n5️⃣ Reflection & Evaluation Phase...")
    print("🤖 Evaluating all candidate actions...")

    try:
        reflection_history = [
            "Left path shows ancient symbols that might be clues",
            "Center path is direct but has visible traps",
            "Right passage unexplored - high uncertainty",
        ]

        eval_result = await evaluator.evaluate_actions(
            selected_node,
            action_result.candidate_actions,
            problem,
            goal,
            reflection_history,
        )

        print(f"\n✅ Evaluation Complete:")
        print(f"   Overall Reflection: {eval_result.overall_reflection[:150]}...")

        if eval_result.scored_actions:
            print(f"\n📊 Action Scores:")
            for i, scored in enumerate(eval_result.scored_actions, 1):
                print(f"   {i}. {scored.action}")
                print(f"      Score: {scored.score:.2f}")
                print(f"      Reasoning: {scored.reasoning[:100]}...")

        best_action = evaluator.get_best_action(eval_result)
        if best_action:
            print(
                f"\n🏆 Best Action: {best_action.action} (score: {best_action.score:.2f})"
            )

        if evaluator.should_backtrack(eval_result):
            print("\n⚠️ Evaluator suggests backtracking - all actions scored poorly")

    except Exception as e:
        print(f"❌ Evaluation failed: {e}")
        import traceback

        traceback.print_exc()
        return

    # Summary
    print("\n6️⃣ Integration Test Summary")
    print("=" * 70)
    print("✅ Node Selection: Working")
    print("✅ Action Generation: Working")
    print("✅ Reflection & Evaluation: Working")
    print("\n🎯 LATS v3 components successfully integrated!")

    # Next steps that would happen in full LATS
    print("\n📝 Next Steps (TODO - TreeManager):")
    print("1. Execute best action to create new node")
    print("2. Simulate/expand from new node")
    print("3. Backpropagate rewards up the tree")
    print("4. Repeat MCTS iterations until solution found")


if __name__ == "__main__":
    asyncio.run(test_full_lats_workflow())
