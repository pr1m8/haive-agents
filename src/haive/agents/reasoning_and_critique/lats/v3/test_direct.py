"""Direct test of LATS v3 components - minimal imports."""

import asyncio
import sys
from pathlib import Path

# Direct imports only
sys.path.insert(0, str(Path(__file__).parent))

print("Testing LATS v3 Components...")

# Test imports
try:
    from models.tree_models import LATSNode

    print("✅ Tree models imported")

    from models.action_models import ActionGeneration, CandidateAction

    print("✅ Action models imported")

    from models.evaluation_models import (
        ReflectionEvaluation,
        ScoredAction,
        UCBSelection,
    )

    print("✅ Evaluation models imported")

    # Now import agents - they depend on models
    from agents.node_selector import NodeSelector

    print("✅ NodeSelector imported")

    from agents.action_generator import ActionGenerator

    print("✅ ActionGenerator imported")

    from agents.reflection_evaluator import ReflectionEvaluator

    print("✅ ReflectionEvaluator imported")

except Exception as e:
    print(f"❌ Import failed: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)


async def quick_test():
    """Quick test of core functionality."""
    print("\n🧪 Running Quick Functionality Test...")

    # Create a test node
    node = LATSNode(
        node_id="test",
        action="Start",
        state_description="Initial state",
        visits=1,
        reward_sum=0.5,
    )
    print(f"✅ Created node: {node.node_id}")
    print(f"   UCB score: {node.ucb_score()}")

    # Test NodeSelector
    print("\n1️⃣ Testing NodeSelector...")
    selector = NodeSelector(name="test_selector")
    nodes = {node.node_id: node}

    # Create selection prompt (test without calling LLM)
    prompt = selector.create_selection_prompt(nodes, "Test problem")
    print(f"✅ Created selection prompt ({len(prompt)} chars)")

    # Test ActionGenerator
    print("\n2️⃣ Testing ActionGenerator...")
    generator = ActionGenerator(name="test_generator")

    # Create generation prompt
    prompt = generator.create_generation_prompt(node, "Test problem")
    print(f"✅ Created action prompt ({len(prompt)} chars)")

    # Test ReflectionEvaluator
    print("\n3️⃣ Testing ReflectionEvaluator...")
    evaluator = ReflectionEvaluator(name="test_evaluator")

    # Create test action
    action = CandidateAction(
        action="Test action",
        reasoning="Test reasoning",
        expected_outcome="Test outcome",
        confidence=0.7,
    )

    # Create evaluation prompt
    prompt = evaluator.create_evaluation_prompt(
        node, [action], "Test problem", "Test goal"
    )
    print(f"✅ Created evaluation prompt ({len(prompt)} chars)")

    print("\n✅ All components initialized and tested successfully!")
    print("\n📝 Component Summary:")
    print("- LATSNode with UCB scoring ✅")
    print("- NodeSelector with prompt generation ✅")
    print("- ActionGenerator with prompt generation ✅")
    print("- ReflectionEvaluator with prompt generation ✅")


if __name__ == "__main__":
    asyncio.run(quick_test())
