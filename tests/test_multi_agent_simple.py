"""Simple tests for ProperMultiAgent system."""

import sys

import pytest

# Add direct paths to avoid import issues
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


class TestProperMultiAgent:
    """Test suite for ProperMultiAgent functionality."""

    def test_agent_list_normalization(self):
        """Test that agents list gets normalized to dict."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        assert isinstance(multi.agents, dict)
        assert len(multi.agents) == 2
        assert "agent1" in multi.agents
        assert "agent2" in multi.agents
        assert multi.agents["agent1"] == agent1
        assert multi.agents["agent2"] == agent2

    def test_agent_dict_passthrough(self):
        """Test that agents dict is passed through correctly."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        multi = ProperMultiAgent(
            name="test_multi", agents={"first": agent1, "second": agent2}
        )

        assert isinstance(multi.agents, dict)
        assert len(multi.agents) == 2
        assert "first" in multi.agents
        assert "second" in multi.agents

    def test_single_agent_normalization(self):
        """Test that single agent gets normalized to dict."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())

        multi = ProperMultiAgent(name="test_multi", agent=agent1)

        assert isinstance(multi.agents, dict)
        assert len(multi.agents) == 1
        assert "agent1" in multi.agents
        assert multi.agents["agent1"] == agent1

    def test_engine_integration(self):
        """Test that agent engines are integrated properly."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Check that engines dict has agent engines
        assert isinstance(multi.engines, dict)

        # Should have namespaced engines
        agent1_engines = [k for k in multi.engines if k.startswith("agent1.")]
        agent2_engines = [k for k in multi.engines if k.startswith("agent2.")]

        assert len(agent1_engines) > 0
        assert len(agent2_engines) > 0

    def test_state_schema_setup(self):
        """Test that state schema is set up correctly."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Should use ProperMultiAgentState
        assert multi.state_schema.__name__ == "ProperMultiAgentState"
        assert multi.use_prebuilt_base is True

    def test_graph_building(self):
        """Test that graph builds without errors."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Should be able to build graph
        graph = multi.build_graph()
        assert graph is not None
        assert graph.name == "test_multi_graph"

    @pytest.mark.asyncio
    async def test_basic_execution(self):
        """Test basic execution without errors."""
        agent1 = SimpleAgent(
            name="agent1", engine=AugLLMConfig(system_message="You are agent 1.")
        )
        agent2 = SimpleAgent(
            name="agent2", engine=AugLLMConfig(system_message="You are agent 2.")
        )

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Test execution
        test_input = {"messages": [HumanMessage(content="Hello!")]}

        result = await multi.ainvoke(test_input)

        # Basic verification
        assert isinstance(result, dict)
        assert "messages" in result
        assert len(result["messages"]) > 0

    def test_empty_agents_handling(self):
        """Test handling of empty agents list."""
        multi = ProperMultiAgent(name="test_multi", agents=[])

        assert isinstance(multi.agents, dict)
        assert len(multi.agents) == 0

    def test_invalid_execution_mode(self):
        """Test error handling for invalid execution mode."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())

        multi = ProperMultiAgent(
            name="test_multi", agents=[agent1], execution_mode="invalid"
        )

        with pytest.raises(NotImplementedError):
            multi.build_graph()

    def test_sequential_execution_mode(self):
        """Test sequential execution mode setup."""
        agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
        agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

        multi = ProperMultiAgent(
            name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
        )

        assert multi.execution_mode == "sequential"

        # Should build graph without error
        graph = multi.build_graph()
        assert graph is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
