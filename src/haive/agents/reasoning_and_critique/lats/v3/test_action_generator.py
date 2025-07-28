"""Test ActionGenerator agent directly."""

import asyncio

from agents.action_generator import ActionGenerator
from models.action_models import ActionGeneration, CandidateAction
from models.tree_models import LATSNode


async def test_action_generator():
    """Test the ActionGenerator agent."""
    print("\n🧪 Testing ActionGenerator for LATS v3")
    print("=" * 60)

    # Create ActionGenerator
    generator = ActionGenerator(
        name="lats_action_generator", num_candidates=5, temperature=0.7
    )
    print(f"✅ Created ActionGenerator: {generator.name}")
    print(f"   - Target candidates: {generator.num_candidates}")
    print(f"   - Temperature: {generator.temperature}")

    # Create a test node
    current_node = LATSNode(
        node_id="test_node",
        action="Enter the maze from the south entrance",
        state_description="Standing at the south entrance of a complex maze. Can see three paths ahead.",
        depth=1,
        visits=2,
        reward_sum=1.4,
        reflection_reasoning="Initial exploration shows promise, multiple paths available",
    )

    problem = "Navigate through a complex maze to find the treasure at the center"
    search_history = [
        "Started at south entrance",
        "Observed three paths: left (dark), center (lit), right (narrow)",
    ]

    print(f"\n📍 Current Node:")
    print(f"   - Action: {current_node.action}")
    print(f"   - State: {current_node.state_description}")
    print(f"   - Depth: {current_node.depth}")
    print(f"   - Average reward: {current_node.average_reward():.2f}")

    print(f"\n🎯 Problem: {problem}")

    # Generate actions
    print("\n🤖 Generating candidate actions...")
    try:
        result = await generator.generate_actions(
            current_node=current_node,
            problem_description=problem,
            search_history=search_history,
        )

        print(f"\n✅ Generated {len(result.candidate_actions)} actions:")
        print(f"\n📊 Situation Analysis:")
        print(f"   {result.situation_analysis}")

        print(f"\n🎬 Candidate Actions:")
        for i, action in enumerate(result.candidate_actions, 1):
            print(f"\n{i}. {action.action}")
            print(f"   Reasoning: {action.reasoning}")
            print(f"   Expected: {action.expected_outcome}")
            print(f"   Confidence: {action.confidence:.2f}")

        print(f"\n📋 Selection Criteria:")
        print(f"   {result.selection_criteria}")

        print(f"\n🌟 Diversity Check:")
        print(f"   {result.diversity_check}")

        # Test ranking
        ranked = generator.rank_actions(result.candidate_actions)
        print(f"\n🏆 Actions Ranked by Confidence:")
        for i, action in enumerate(ranked[:3], 1):
            print(f"   {i}. {action.action} (confidence: {action.confidence:.2f})")

        # Test diversity score
        diversity = generator.get_action_diversity_score(result.candidate_actions)
        print(f"\n📊 Action Diversity Score: {diversity:.2f}")

        # Test filtering
        filtered = generator.filter_actions(
            result.candidate_actions, min_confidence=0.5
        )
        print(f"\n🔍 High Confidence Actions (≥0.5): {len(filtered)}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Test completed!")


if __name__ == "__main__":
    asyncio.run(test_action_generator())
