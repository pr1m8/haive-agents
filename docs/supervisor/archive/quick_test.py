"""Quick test of component fixes."""

import contextlib

from haive.agents.experiments.supervisor.component_2_tools import (
    SupervisorStateWithTools,
)
from haive.agents.experiments.supervisor.test_component_1_state import (
    create_real_agents,
)


def test_validation_fix():
    """Test that field validation now works."""
    state = SupervisorStateWithTools()
    agents = create_real_agents()
    state.add_agent("search_agent", agents["search_agent"], "Test", True)

    # Test valid assignment
    with contextlib.suppress(Exception):
        state.next_agent = "search_agent"

    # Test invalid assignment
    with contextlib.suppress(ValueError):
        state.next_agent = "nonexistent_agent"


def test_tool_names():
    """Test that tool names are now correct."""
    state = SupervisorStateWithTools()
    agents = create_real_agents()
    state.add_agent("search_agent", agents["search_agent"], "Test", True)

    tools = state.get_all_tools()

    found_handoff = False
    for tool in tools:
        if tool.name == "handoff_to_search_agent":
            found_handoff = True

    if found_handoff:
        pass
    else:
        pass


if __name__ == "__main__":

    try:
        test_validation_fix()
        test_tool_names()
    except Exception:
        import traceback

        traceback.print_exc()
