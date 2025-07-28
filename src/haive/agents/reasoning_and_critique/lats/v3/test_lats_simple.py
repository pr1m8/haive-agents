"""Simple test of LATS v3 components without import issues."""

import asyncio
import json

# Inline imports to avoid parent module issues
from agents.node_selector import NodeSelector
from models.tree_models import LATSNode


async def test_lats_node_selector():
    """Test NodeSelector with simple example."""
    print("\n🧪 Testing LATS v3 NodeSelector")
    print("=" * 60)

    # Create NodeSelector
    selector = NodeSelector(name="lats_selector")
    print(f"✅ Created NodeSelector: {selector.name}")

    # Create test nodes
    nodes = {
        "node_1": LATSNode(
            action="Take left path",
            state_description="Exploring left side of maze",
            visits=5,
            reward_sum=3.5,
            node_id="node_1",
        ),
        "node_2": LATSNode(
            action="Take right path",
            state_description="Exploring right side of maze",
            visits=0,  # Unvisited
            reward_sum=0.0,
            node_id="node_2",
        ),
        "node_3": LATSNode(
            action="Go straight",
            state_description="Following main corridor",
            visits=3,
            reward_sum=2.1,
            node_id="node_3",
        ),
    }

    # Calculate UCB scores
    print("\n📊 Node UCB Scores:")
    total_visits = sum(n.visits for n in nodes.values())
    for node_id, node in nodes.items():
        ucb = node.ucb_score(1.4, total_visits)
        print(f"  - {node_id}: {node.action} -> UCB = {ucb:.3f}")

    # Test selection
    problem = "Find the optimal path through a maze"
    print(f"\n🤖 Selecting best node for: '{problem}'")

    try:
        # Call the selector
        result = await selector.select_node(nodes, problem)

        # Handle both raw result and UCBSelection
        if hasattr(result, "selected_node_id"):
            print(f"\n✅ Selected: {result.selected_node_id}")
            print(f"   Reasoning: {result.selection_reasoning}")
            print(f"   UCB Score: {result.ucb_score}")
        else:
            # Raw result from agent
            print(f"\n📋 Raw result: {result}")

            # Try to extract structured data
            if isinstance(result, dict) and "ucb_selection" in result:
                selection_data = result["ucb_selection"]
                print(f"\n✅ Selection data found: {selection_data}")
            elif isinstance(result, str):
                # Parse JSON if string
                try:
                    parsed = json.loads(result)
                    print(f"\n✅ Parsed result: {parsed}")
                except:
                    print(f"\n📝 String result: {result}")

    except Exception as e:
        print(f"\n❌ Error during selection: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Test completed!")


if __name__ == "__main__":
    asyncio.run(test_lats_node_selector())
