"""Test Self-Discover MultiAgent with sequential execution."""

import asyncio

import pytest

from haive.agents.multi.clean import MultiAgent
from haive.agents.reasoning_and_critique.self_discover.adapter import AdapterAgent
from haive.agents.reasoning_and_critique.self_discover.executor import ExecutorAgent
from haive.agents.reasoning_and_critique.self_discover.selector import SelectorAgent
from haive.agents.reasoning_and_critique.self_discover.structurer import StructurerAgent


@pytest.mark.asyncio
async def test_self_discover_multiagent():
    """Test Self-Discover MultiAgent with sequential execution."""
    # Create the four specialized agents
    agents = [SelectorAgent(), AdapterAgent(), StructurerAgent(), ExecutorAgent()]

    # Create MultiAgent
    multi_agent = MultiAgent(agents=agents)

    # Test input
    input_data = {
        "available_modules": """1. Critical Thinking: Question assumptions, identify biases, evaluate evidence
2. Systems Analysis: Break down complex systems, identify components and relationships
3. Root Cause Analysis: Identify underlying causes of problems or phenomena""",
        "task_description": "What is 2 + 2?",
    }

    # Execute the workflow
    result = await multi_agent.arun(input_data)

    # Verify we got some result
    assert result is not None
    assert isinstance(result, str | dict)

    return result


if __name__ == "__main__":
    result = asyncio.run(test_self_discover_multiagent())
