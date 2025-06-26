"""
Test cases for the MultiAgent implementation.

This module contains test cases for the improved MultiAgent implementation,
focusing on structured output models and proper tool routing.
"""

from typing import List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


# Test model for structured output
class Plan(BaseModel):
    """A planning model for structured output."""

    steps: List[str] = Field(description="List of steps")


# Example tool for testing
@pytest.fixture
def add_tool():
    def add(a: int, b: int) -> int:
        """Returns the sum of two numbers."""
        return a + b

    return add


def test_multi_agent_creation():
    """Test basic multi-agent creation."""
    multi_agent = MultiAgent(name="Test Multi-Agent")
    assert multi_agent.name == "Test Multi-Agent"
    assert multi_agent.coordination_strategy == "sequential"
    assert multi_agent.route_tools is True
    assert multi_agent.share_structured_outputs is True


def test_multi_agent_with_simple_react_agents(add_tool):
    """Test creating a multi-agent with SimpleAgent and ReactAgent."""
    # Create multi-agent
    multi_agent = MultiAgent(name="Test Multi-Agent")

    # Create a simple agent with Plan structured output
    plan_aug = AugLLMConfig(
        structured_output_model=Plan, structured_output_version="v2"
    )
    simple_agent = SimpleAgent(name="Planner", engine=plan_aug)

    # Create a react agent with tools
    add_aug = AugLLMConfig(tools=[add_tool])
    react_agent = ReactAgent(name="Calculator", engine=add_aug)

    # Add agents to multi-agent
    simple_id = multi_agent.add_agent(simple_agent)
    react_id = multi_agent.add_agent(react_agent)

    # Verify agents were added
    assert simple_id in multi_agent._state_instance.agents
    assert react_id in multi_agent._state_instance.agents

    # Verify tool routes were registered
    assert "Plan" in multi_agent._state_instance.tool_routes
    assert "add" in multi_agent._state_instance.tool_routes

    # Verify tool routes map to correct agents
    assert multi_agent._state_instance.tool_routes["Plan"] == simple_id
    assert multi_agent._state_instance.tool_routes["add"] == react_id


def test_multi_agent_structured_agent_factory():
    """Test creating a multi-agent using the structured agent factory method."""
    # Create agent configs
    agent_configs = [
        {
            "type": "simple",
            "name": "Planner",
            "structured_output_model": Plan,
            "structured_output_version": "v2",
        },
        {"type": "react", "name": "Executor", "tools": []},  # No tools for this test
    ]

    # Create multi-agent using factory method
    multi_agent = MultiAgent.with_structured_agents(
        agent_configs=agent_configs, name="Test Factory Multi-Agent"
    )

    # Verify agents were created
    assert len(multi_agent._state_instance.agents) == 2

    # Find the planner agent
    planner_id = None
    for agent_id, agent in multi_agent._state_instance.agents.items():
        if agent.name == "Planner":
            planner_id = agent_id
            break

    assert planner_id is not None

    # Verify structured output model was properly set up
    planner = multi_agent._state_instance.agents[planner_id]
    assert hasattr(planner, "structured_output_model")
    assert planner.structured_output_model == Plan
    assert hasattr(planner.engine, "structured_output_model")
    assert planner.engine.structured_output_model == Plan
    assert planner.engine.structured_output_version == "v2"


def test_multi_agent_invoke_sharing_structured_output(monkeypatch):
    """Test invoking a multi-agent with structured output sharing."""

    # Mock the invoke method for agents to avoid actual LLM calls
    def mock_invoke(self, input_data):
        if self.name == "Planner":
            # Return a plan from the planner
            plan_data = {"plan": {"steps": ["Step 1: Plan", "Step 2: Execute"]}}
            return plan_data
        elif self.name == "Executor":
            # Use the plan from the planner
            structured_outputs = input_data.get("structured_outputs", {})
            if structured_outputs:
                # Extract the planner's output and incorporate it
                planner_output = next(iter(structured_outputs.values()))
                steps = planner_output.get("steps", [])
                return {"output": f"Executing plan with {len(steps)} steps"}
            return {"output": "No plan available"}

    # Apply the mock
    monkeypatch.setattr(SimpleAgent, "invoke", mock_invoke)

    # Create multi-agent with two simple agents
    agent_configs = [
        {
            "type": "simple",
            "name": "Planner",
            "structured_output_model": Plan,
        },
        {
            "type": "simple",
            "name": "Executor",
        },
    ]

    multi_agent = MultiAgent.with_structured_agents(
        agent_configs=agent_configs, name="Test Sharing Multi-Agent"
    )

    # Invoke the multi-agent
    result = multi_agent.invoke(
        {"messages": [HumanMessage(content="Plan and execute")]}
    )

    # Verify the second agent received and used the structured output from the first
    outputs = result.get("outputs", {})
    assert len(outputs) == 2

    # Find the executor's output
    executor_output = None
    for agent_id, agent_output in outputs.items():
        if multi_agent._state_instance.agents[agent_id].name == "Executor":
            executor_output = agent_output
            break

    assert executor_output is not None
    assert executor_output.get("output") == "Executing plan with 2 steps"
