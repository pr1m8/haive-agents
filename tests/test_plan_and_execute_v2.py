"""Test Plan and Execute Agent v2 with real components."""

import pytest

from haive.agents.planning.plan_and_execute.v2.agent import PlanAndExecuteAgent
from haive.tools.math.calculator import Calculator


def test_plan_and_execute_agent_creation():
    """Test creating P&E agent with default configuration."""
    # Create agent with minimal tools
    agent = PlanAndExecuteAgent.create_default(tools=[Calculator()], name="test_pe_agent")

    # Verify agent structure
    assert agent.name == "test_pe_agent"
    assert agent.execution_mode == "sequential"
    assert len(agent.agents) == 3  # planner, executor, replanner

    # Verify agent names
    agent_names = [agent.name for agent in agent.agents]
    assert "planner" in agent_names
    assert "executor" in agent_names
    assert "replanner" in agent_names


def test_plan_and_execute_agent_state_schema():
    """Test P&E agent state schema composition."""
    agent = PlanAndExecuteAgent.create_default(tools=[Calculator()], name="test_pe_schema")

    # Test state schema
    assert agent.state_schema is not None

    # Create test state
    test_state = agent.state_schema(
        input="Calculate 15 * 23 and explain the result", agents=agent.agents
    )

    # Verify state fields
    assert test_state.input == "Calculate 15 * 23 and explain the result"
    assert test_state.plan is None
    assert test_state.past_steps == []
    assert test_state.response is None
    assert len(test_state.agents) == 3


@pytest.mark.asyncio
async def test_plan_and_execute_agent_real_execution():
    """Test P&E agent with real LLM execution."""
    # Create agent with calculator tool
    agent = PlanAndExecuteAgent.create_default(tools=[Calculator()], name="test_pe_execution")

    # Test simple calculation task
    result = await agent.arun("Calculate 15 * 23")

    # Verify result
    assert isinstance(result, str)
    assert len(result) > 0
    assert "345" in result or "15 * 23" in result

    # Check that agent executed through all phases
    # Note: This is a basic test - more detailed state inspection would require debug mode


def test_plan_and_execute_agent_methods():
    """Test P&E agent helper methods."""
    agent = PlanAndExecuteAgent.create_default(tools=[Calculator()], name="test_pe_methods")

    # Create test state
    from haive.agents.planning.plan_and_execute.v2.models import Plan, Step
    from haive.agents.planning.plan_and_execute.v2.state import PlanAndExecuteState

    test_state = PlanAndExecuteState(input="Test task", agents=agent.agents)

    # Test should_continue_execution with no plan
    assert not agent.should_continue_execution(test_state)

    # Test get_next_action with no plan
    assert agent.get_next_action(test_state) == "planner"

    # Add a plan with incomplete steps
    test_plan = Plan(
        description="Test plan",
        steps=[
            Step(id=1, description="Step 1", status="not_started"),
            Step(id=2, description="Step 2", status="not_started"),
        ],
    )
    test_state.plan = test_plan

    # Test with incomplete steps
    assert agent.should_continue_execution(test_state)
    assert agent.get_next_action(test_state) == "executor"

    # Mark steps as complete
    test_plan.steps[0].status = "complete"
    test_plan.steps[1].status = "complete"
    test_plan.update_status()

    # Test with complete plan
    assert not agent.should_continue_execution(test_state)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
