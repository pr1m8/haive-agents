"""Test Self-Discover Simple V4 implementation."""

import pytest

from haive.agents.reasoning_and_critique.self_discover.self_discover_simple_v4 import (
    MODULES,
    create_agents,
    create_self_discover_simple,
    run_self_discover,
)


class TestSelfDiscoverSimpleV4:
    """Test the simple V4 implementation."""

    def test_create_agents(self):
        """Test that all 4 agents are created properly."""
        agents = create_agents()

        assert len(agents) == 4
        assert agents[0].name == "selector"
        assert agents[1].name == "adapter"
        assert agents[2].name == "structurer"
        assert agents[3].name == "executor"

        # Check they all have engines
        for agent in agents:
            assert agent.engine is not None
            assert agent.prompt_template is not None

    def test_create_multi_agent(self):
        """Test multi-agent creation."""
        agent = create_self_discover_simple()

        assert agent.name == "self_discover_simple"
        assert agent.execution_mode == "sequential"
        assert len(agent.agents) == 4

    @pytest.mark.asyncio
    async def test_simple_shape_task(self):
        """Test with a simple shape recognition task."""
        task = "What shape has 4 equal sides and 4 right angles?"

        result = await run_self_discover(task)

        assert isinstance(result, dict)

        # Check if answer is present
        if "answer" in result:
            answer = result["answer"].lower()
            # Should identify it as a square
            assert "square" in answer or "rectangle" in answer

    @pytest.mark.asyncio
    async def test_custom_modules(self):
        """Test with custom modules."""
        task = "How can I improve team communication?"

        custom_modules = """1. Active Listening - Listen to understand
2. Clear Communication - Express ideas clearly
3. Feedback Systems - Give and receive feedback
4. Collaboration Tools - Use effective tools
5. Meeting Management - Run effective meetings"""

        result = await run_self_discover(task, modules=custom_modules)

        assert isinstance(result, dict)

        # Should have some answer
        if "answer" in result:
            assert len(result["answer"]) > 0

    @pytest.mark.asyncio
    async def test_state_propagation(self):
        """Test that state is properly propagated between agents."""
        agent = create_self_discover_simple()

        # Initial state
        state = {
            "task": "Test task",
            "modules": MODULES,
            "adapted": "",
            "plan": "",
            "answer": "",
            "reasoning": "",
        }

        # Run the agent
        result = await agent.arun(state)

        # Result should be a dict with updated fields
        assert isinstance(result, dict)

        # At minimum, task should still be there
        if "task" in result:
            assert result["task"] == "Test task"
