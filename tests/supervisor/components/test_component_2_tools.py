"""Test Component 2: Tool generation from state.agents with choice model."""

import contextlib

from haive.agents.experiments.supervisor.component_2_tools import (
    SupervisorStateWithTools,
)
from haive.agents.experiments.supervisor.test_component_1_state import (
    create_real_agents,
)


def test_choice_model_integration():
    """Test choice model syncs with agents in state."""
    # Create state with choice model
    state = SupervisorStateWithTools()

    # Check initial choice model options

    # Create and add real agents
    agents = create_real_agents()

    # Add agents one by one and see choice model update
    state.add_agent(
        "search_agent",
        agents["search_agent"],
        "Web search and research specialist",
        active=True,
    )

    state.add_agent(
        "math_agent",
        agents["math_agent"],
        "Mathematical calculations specialist",
        active=True,
    )

    # Test choice model validation
    ChoiceModel = state.agent_choice_model.current_model

    # Test valid choices
    with contextlib.suppress(Exception):
        ChoiceModel(choice="search_agent")

    with contextlib.suppress(Exception):
        ChoiceModel(choice="END")

    # Test invalid choice
    with contextlib.suppress(Exception):
        ChoiceModel(choice="nonexistent_agent")


def test_tool_generation():
    """Test dynamic tool generation from agents."""
    # Create state and add agents
    state = SupervisorStateWithTools()
    agents = create_real_agents()

    # Add all agents
    state.add_agent("search_agent", agents["search_agent"], "Web search specialist", True)
    state.add_agent("math_agent", agents["math_agent"], "Math calculations specialist", True)
    state.add_agent("planning_agent", agents["planning_agent"], "Planning specialist", False)

    # Check generated tool names

    # Get actual tool objects
    tools = state.get_all_tools()

    for _tool in tools:
        pass

    # Test tool removal when agent removed
    state.remove_agent("planning_agent")


def test_handoff_tool_execution():
    """Test handoff tool execution."""
    # Create state with agents
    state = SupervisorStateWithTools()
    agents = create_real_agents()

    state.add_agent("search_agent", agents["search_agent"], "Web search specialist", True)
    state.add_agent("math_agent", agents["math_agent"], "Math specialist", True)

    # Get tools
    tools = state.get_all_tools()

    # Find handoff tool for search_agent
    search_handoff_tool = None
    for tool in tools:
        if tool.name == "handoff_to_search_agent":
            search_handoff_tool = tool
            break

    if search_handoff_tool:
        # Test tool execution
        search_handoff_tool.invoke({"task_description": "Search for Python tutorials"})

        # Check if state was updated
    else:
        pass


def test_choice_tool_execution():
    """Test choice tool execution."""
    # Create state with agents
    state = SupervisorStateWithTools()
    agents = create_real_agents()

    state.add_agent("search_agent", agents["search_agent"], "Web search specialist", True)
    state.add_agent("math_agent", agents["math_agent"], "Math specialist", True)

    # Get tools
    tools = state.get_all_tools()

    # Find choice tool
    choice_tool = None
    for tool in tools:
        if tool.name == "choose_agent":
            choice_tool = tool
            break

    if choice_tool:
        # Test different task types
        test_tasks = [
            "Search for information about Python",
            "Calculate 25 multiplied by 8",
            "Create a plan for learning AI",
            "Some random task",
        ]

        for task in test_tasks:
            choice_tool.invoke({"task_description": task, "reasoning": "Testing choice logic"})
    else:
        pass


def test_field_validation():
    """Test field validation with choice model."""
    # Create state with agents
    state = SupervisorStateWithTools()
    agents = create_real_agents()

    state.add_agent("search_agent", agents["search_agent"], "Web search specialist", True)

    # Test valid agent assignment
    with contextlib.suppress(Exception):
        state.next_agent = "search_agent"

    # Test END assignment
    with contextlib.suppress(Exception):
        state.next_agent = "END"

    # Test invalid agent assignment
    with contextlib.suppress(Exception):
        state.next_agent = "nonexistent_agent"


if __name__ == "__main__":
    try:
        test_choice_model_integration()
        test_tool_generation()
        test_handoff_tool_execution()
        test_choice_tool_execution()
        test_field_validation()

    except Exception:
        raise
