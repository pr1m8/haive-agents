"""Clean test of ActionGenerator to see structured output."""

import asyncio

from agents.action_generator import ActionGenerator
from models.tree_models import LATSNode


async def test_action_generator_clean():
    """Test ActionGenerator with clean output."""
    print("\n🧪 LATS v3 ActionGenerator Test")
    print("=" * 60)

    # Create generator
    generator = ActionGenerator(name="action_gen", num_candidates=5)

    # Create test node
    node = LATSNode(
        node_id="test",
        action="Enter maze",
        state_description="At entrance, three paths visible",
        depth=1,
        visits=2,
        reward_sum=1.4,
    )

    problem = "Navigate maze to find treasure"

    # Generate actions
    result = await generator.generate_actions(node, problem)

    print(f"\n📊 Situation: {result.situation_analysis}")
    print(f"\n🎬 Generated {len(result.candidate_actions)} Actions:")

    for i, action in enumerate(result.candidate_actions, 1):
        print(f"\n{i}. {action.action} (confidence: {action.confidence:.1f})")
        print(f"   Why: {action.reasoning}")

    print(f"\n✅ Selection Criteria: {result.selection_criteria}")
    print(f"\n🌟 Diversity: {result.diversity_check}")


if __name__ == "__main__":
    asyncio.run(test_action_generator_clean())
