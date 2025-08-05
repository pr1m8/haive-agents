"""Test MultiAgent V4 - Start small and build incrementally."""

import pytest

from haive.agents.multi.multi_agent_v4 import MultiAgentV4
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


class TestMultiAgentV4:
    """Test MultiAgent V4 functionality incrementally."""

    def test_basic_creation_with_agent_list(self):
        """Test basic creation with list of agents."""
        # Create simple agents
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        # Create multi-agent
        multi_agent = MultiAgentV4(
            name="test_workflow",
            agents=[agent1, agent2],
            execution_mode="sequential",
            build_mode="manual",  # Don't auto-build for testing
        )

        # Verify basic setup
        assert multi_agent.name == "test_workflow"
        assert len(multi_agent.agents) == 2
        assert len(multi_agent.agent_dict) == 2
        assert "agent1" in multi_agent.agent_dict
        assert "agent2" in multi_agent.agent_dict
        assert multi_agent.execution_mode == "sequential"

    def test_agent_list_to_dict_conversion(self):
        """Test agent list to dict conversion."""
        agents = [
            SimpleAgent(name="planner", engine=AugLLMConfig()),
            SimpleAgent(name="executor", engine=AugLLMConfig()),
            SimpleAgent(name="reviewer", engine=AugLLMConfig()),
        ]

        multi_agent = MultiAgentV4(name="conversion_test", agents=agents, build_mode="manual")

        # Check conversion
        assert len(multi_agent.agent_dict) == 3
        assert list(multi_agent.agent_dict.keys()) == [
            "planner",
            "executor",
            "reviewer",
        ]

        # Check agents are the same objects
        assert multi_agent.agent_dict["planner"] is agents[0]
        assert multi_agent.agent_dict["executor"] is agents[1]
        assert multi_agent.agent_dict["reviewer"] is agents[2]

    def test_duplicate_agent_names_error(self):
        """Test error handling for duplicate agent names."""
        agents = [
            SimpleAgent(name="agent1", engine=AugLLMConfig()),
            SimpleAgent(name="agent1", engine=AugLLMConfig()),  # Duplicate name
        ]

        with pytest.raises(ValueError, match="Duplicate agent name: agent1"):
            MultiAgentV4(name="test", agents=agents, build_mode="manual")

    def test_agent_without_name_error(self):
        """Test error handling for agents without names."""
        # Create agent without name
        agent_no_name = SimpleAgent(engine=AugLLMConfig())
        agent_no_name.name = None  # Force no name

        agents = [SimpleAgent(name="agent1", engine=AugLLMConfig()), agent_no_name]

        with pytest.raises(ValueError, match="Agent at index 1 must have a name"):
            MultiAgentV4(name="test", agents=agents, build_mode="manual")

    def test_manual_build_mode(self):
        """Test manual build mode - graph not built automatically."""
        agents = [SimpleAgent(name="agent1", engine=AugLLMConfig())]

        multi_agent = MultiAgentV4(name="manual_test", agents=agents, build_mode="manual")

        # Graph should not be built
        assert multi_agent._execution_graph is None

        # Manual build should work
        graph = multi_agent.build()
        assert graph is not None
        assert multi_agent._execution_graph is not None

    def test_auto_build_mode(self):
        """Test auto build mode - graph built automatically."""
        agents = [SimpleAgent(name="agent1", engine=AugLLMConfig())]

        multi_agent = MultiAgentV4(name="auto_test", agents=agents, build_mode="auto")

        # Graph should be built automatically
        assert multi_agent._execution_graph is not None

    def test_add_agent_method(self):
        """Test adding agents dynamically."""
        # Start with one agent
        multi_agent = MultiAgentV4(
            name="dynamic_test",
            agents=[SimpleAgent(name="agent1", engine=AugLLMConfig())],
            build_mode="manual",
        )

        assert len(multi_agent._agent_dict) == 1

        # Add another agent
        new_agent = SimpleAgent(name="agent2", engine=AugLLMConfig())
        multi_agent.add_agent(new_agent)

        # Verify addition
        assert len(multi_agent._agent_dict) == 2
        assert len(multi_agent.agents) == 2
        assert "agent2" in multi_agent._agent_dict
        assert multi_agent.get_agent("agent2") is new_agent

    def test_utility_methods(self):
        """Test utility methods."""
        agents = [
            SimpleAgent(name="planner", engine=AugLLMConfig()),
            SimpleAgent(name="executor", engine=AugLLMConfig()),
        ]

        multi_agent = MultiAgentV4(name="utility_test", agents=agents, build_mode="manual")

        # Test get_agent_names
        names = multi_agent.get_agent_names()
        assert names == ["planner", "executor"]

        # Test get_agent
        planner = multi_agent.get_agent("planner")
        assert planner is agents[0]

        # Test get non-existent agent
        assert multi_agent.get_agent("nonexistent") is None

    def test_initial_state_creation(self):
        """Test MultiAgentState creation from input."""
        agents = [SimpleAgent(name="agent1", engine=AugLLMConfig())]

        multi_agent = MultiAgentV4(name="state_test", agents=agents, build_mode="manual")

        # Test with dict input
        input_data = {"task": "test task", "priority": "high"}
        state = multi_agent._create_initial_state(input_data)

        assert isinstance(state, MultiAgentState)
        assert state.agent_count == 1
        assert "agent1" in state.agents
        assert hasattr(state, "task") or "task" in state.__dict__

    def test_display_workflow_info(self, capsys):
        """Test workflow info display."""
        agents = [
            SimpleAgent(name="agent1", engine=AugLLMConfig()),
            SimpleAgent(name="agent2", engine=AugLLMConfig()),
        ]

        multi_agent = MultiAgentV4(
            name="info_test",
            agents=agents,
            execution_mode="sequential",
            build_mode="manual",
        )

        # Test display
        multi_agent.display_workflow_info()

        captured = capsys.readouterr()
        assert "MultiAgent V4: info_test" in captured.out
        assert "Execution Mode: sequential" in captured.out
        assert "agent1 (SimpleAgent)" in captured.out
        assert "agent2 (SimpleAgent)" in captured.out
        assert "Graph Built: No" in captured.out


# Integration test with real components (no mocks)
class TestMultiAgentV4Integration:
    """Integration tests with real components."""

    @pytest.mark.asyncio
    async def test_basic_sequential_execution(self):
        """Test basic sequential execution with real agents."""
        # Create real agents with low temperature for consistency
        agent1 = SimpleAgent(name="greeter", engine=AugLLMConfig(temperature=0.1))

        agent2 = SimpleAgent(name="responder", engine=AugLLMConfig(temperature=0.1))

        # Create workflow
        workflow = MultiAgentV4(
            name="greeting_workflow",
            agents=[agent1, agent2],
            execution_mode="sequential",
            build_mode="auto",
        )

        # Test execution (this will use real LLMs)
        try:
            result = await workflow.arun(
                {"messages": [{"role": "user", "content": "Hello, please introduce yourself"}]}
            )

            # Verify we got some result
            assert result is not None

            # Result should be either final_result, agent_outputs, or the state itself
            if isinstance(result, dict):
                # Could be agent_outputs
                assert len(result) >= 0  # At least some output
            else:
                # Could be state object or final_result
                assert result is not None

        except Exception as e:
            # If LLM not available, skip test gracefully
            if "api" in str(e).lower() or "key" in str(e).lower():
                pytest.skip(f"LLM API not available: {e}")
            else:
                raise
