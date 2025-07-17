"""Check what MultiAgentState actually has vs what it should have."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


def check_multi_agent_state():
    """Check what MultiAgentState actually has."""

    print("🔍 Checking MultiAgentState...")
    print(f"MultiAgentState class: {MultiAgentState}")

    if hasattr(MultiAgentState, "model_fields"):
        fields = MultiAgentState.model_fields
        print(f"MultiAgentState fields ({len(fields)}):")
        for field_name, field_info in fields.items():
            print(f"  {field_name}: {field_info.annotation}")
    else:
        print("  No model_fields found")

    print("\n🎯 Problem: MultiAgentState only has generic fields!")
    print("  It doesn't have:")
    print("    - task_description")
    print("    - reasoning_modules")
    print("    - selected_modules")
    print("    - adapted_modules")
    print("    - reasoning_structure")
    print("    - final_answer")

    print("\n💡 Solution: AgentSchemaComposer should compose from agents dict")
    print("  It should create a custom state schema that includes:")
    print("    - Base MultiAgentState fields")
    print("    - All fields from individual agent state schemas")
    print("    - Proper field conflict resolution")


if __name__ == "__main__":
    check_multi_agent_state()
