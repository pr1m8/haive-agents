"""Check what MultiAgentState actually has vs what it should have."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


def check_multi_agent_state():
    """Check what MultiAgentState actually has."""
    if hasattr(MultiAgentState, "model_fields"):
        fields = MultiAgentState.model_fields
        for _field_name, _field_info in fields.items():
            pass
    else:
        pass


if __name__ == "__main__":
    check_multi_agent_state()
