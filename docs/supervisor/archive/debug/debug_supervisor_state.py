"""Debug our actual SupervisorState."""

import contextlib

from agent_info import AgentInfo
from supervisor_state import SupervisorState


def test_supervisor_state():
    """Test the actual SupervisorState."""

    # Create dummy agent
    class DummyAgent:
        def __init__(self):
            self.name = "dummy"

    agent = DummyAgent()
    info = AgentInfo(agent=agent, name="test", description="Test")

    # Test 1: Empty state
    with contextlib.suppress(Exception):
        SupervisorState()

    # Test 2: With dict
    with contextlib.suppress(Exception):
        SupervisorState(agents={"test": {"agent": agent, "name": "test", "description": "Test"}})

    # Test 3: With AgentInfo
    try:
        SupervisorState(agents={"test": info})
    except Exception:
        import traceback

        traceback.print_exc()

        # Let's inspect the class more


if __name__ == "__main__":
    test_supervisor_state()
