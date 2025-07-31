"""Comprehensive tests for ProperMultiAgent system."""

from langchain_core.messages import AIMessage, HumanMessage
import pytest

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class TestProperMultiAgent:
    """Test suite for ProperMultiAgent functionality."""

    @pytest.fixture
    def simple_agents(self):
        """Create simple agents for testing."""
        agent1 = SimpleAgent(
            name="agent1",
            engine=AugLLMConfig(
                system_message="You are agent 1. Say hello from agent 1."
            ),
        )

        agent2 = SimpleAgent(
            name="agent2",
            engine=AugLLMConfig(
                system_message="You are agent 2. Respond to the previous message."
            ),
        )

        return agent1, agent2

    def test_multi_agent_creation_with_list(self, simple_agents):
        """Test creating multi-agent with list of agents."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(
            name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
        )

        assert multi.name == "test_multi"
        assert isinstance(multi.agents, dict)
        assert "agent1" in multi.agents
        assert "agent2" in multi.agents
        assert multi.execution_mode == "sequential"

    def test_multi_agent_creation_with_dict(self, simple_agents):
        """Test creating multi-agent with dict of agents."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(
            name="test_multi",
            agents={"first": agent1, "second": agent2},
            execution_mode="sequential",
        )

        assert isinstance(multi.agents, dict)
        assert "first" in multi.agents
        assert "second" in multi.agents
        assert multi.agents["first"] == agent1
        assert multi.agents["second"] == agent2

    def test_multi_agent_creation_with_single_agent(self, simple_agents):
        """Test creating multi-agent with single agent."""
        agent1, _ = simple_agents

        multi = ProperMultiAgent(
            name="test_multi", agent=agent1, execution_mode="sequential"
        )

        assert isinstance(multi.agents, dict)
        assert "agent1" in multi.agents
        assert multi.agents["agent1"] == agent1

    def test_agent_normalization_list_to_dict(self, simple_agents):
        """Test that list of agents gets normalized to dict."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Should be converted to dict with agent names as keys
        assert isinstance(multi.agents, dict)
        assert len(multi.agents) == 2
        assert multi.agents["agent1"] == agent1
        assert multi.agents["agent2"] == agent2

    def test_engine_integration(self, simple_agents):
        """Test that agent engines are properly integrated."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Check that engines dict contains agent engines
        assert isinstance(multi.engines, dict)

        # Should have agent engines with proper namespacing
        agent1_engines = [k for k in multi.engines if k.startswith("agent1.")]
        agent2_engines = [k for k in multi.engines if k.startswith("agent2.")]

        assert len(agent1_engines) > 0
        assert len(agent2_engines) > 0

    def test_state_schema_composition(self, simple_agents):
        """Test that state schema is properly composed."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Should use MultiAgentState as base
        assert multi.state_schema.__name__ == "ProperMultiAgentState"
        assert multi.use_prebuilt_base is True

    def test_graph_building_without_errors(self, simple_agents):
        """Test that graph builds without errors."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Should be able to build graph
        graph = multi.build_graph()
        assert graph is not None
        assert graph.name == "test_multi_graph"

    @pytest.mark.asyncio
    async def test_sequential_execution(self, simple_agents):
        """Test sequential execution of agents."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(
            name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
        )

        # Test input
        test_input = {"messages": [HumanMessage(content="Hello multi-agent!")]}

        # Execute
        result = await multi.ainvoke(test_input)

        # Verify execution
        assert isinstance(result, dict)
        assert "messages" in result
        assert len(result["messages"]) > 1  # Should have more than input message

        # Check that we have messages from both agents
        messages = result["messages"]
        assert isinstance(messages[-1], AIMessage)  # Last should be AI response

    @pytest.mark.asyncio
    async def test_agent_state_management(self, simple_agents):
        """Test that agent states are properly managed."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        test_input = {"messages": [HumanMessage(content="Test state management")]}

        result = await multi.ainvoke(test_input)

        # Check for agent state fields
        assert isinstance(result, dict)

        # Should have agent_outputs tracking
        if "agent_outputs" in result:
            agent_outputs = result["agent_outputs"]
            assert isinstance(agent_outputs, dict)

    @pytest.mark.asyncio
    async def test_message_flow_between_agents(self, simple_agents):
        """Test that messages flow properly between agents."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        test_input = {
            "messages": [HumanMessage(content="Say hello and pass to next agent")]
        }

        result = await multi.ainvoke(test_input)

        # Should have accumulated messages from sequential execution
        assert "messages" in result
        messages = result["messages"]

        # Should have original message plus responses from agents
        assert len(messages) >= 2  # At least input + 1 response

        # First message should be the human input
        assert isinstance(messages[0], HumanMessage)
        assert messages[0].content == "Say hello and pass to next agent"

    def test_error_handling_with_invalid_execution_mode(self, simple_agents):
        """Test error handling with invalid execution mode."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(
            name="test_multi", agents=[agent1, agent2], execution_mode="invalid_mode"
        )

        # Should raise error when trying to build graph
        with pytest.raises(NotImplementedError):
            multi.build_graph()

    def test_empty_agents_handling(self):
        """Test handling of empty agents."""
        multi = ProperMultiAgent(
            name="test_multi", agents=[], execution_mode="sequential"
        )

        assert isinstance(multi.agents, dict)
        assert len(multi.agents) == 0

    def test_agents_field_type_validation(self, simple_agents):
        """Test that agents field accepts various types."""
        agent1, agent2 = simple_agents

        # Test with list
        multi1 = ProperMultiAgent(name="test1", agents=[agent1, agent2])
        assert isinstance(multi1.agents, dict)

        # Test with dict
        multi2 = ProperMultiAgent(name="test2", agents={"a": agent1, "b": agent2})
        assert isinstance(multi2.agents, dict)

        # Test with single agent
        multi3 = ProperMultiAgent(name="test3", agent=agent1)
        assert isinstance(multi3.agents, dict)
        assert len(multi3.agents) == 1

    @pytest.mark.asyncio
    async def test_real_llm_integration(self, simple_agents):
        """Test with real LLM calls (no mocks)."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="integration_test", agents=[agent1, agent2])

        # Real execution with actual LLM
        result = await multi.ainvoke(
            {"messages": [HumanMessage(content="Hello, please introduce yourselves")]}
        )

        # Verify real execution occurred
        assert isinstance(result, dict)
        assert "messages" in result
        assert len(result["messages"]) > 1

        # Check that actual content was generated
        last_message = result["messages"][-1]
        assert isinstance(last_message, AIMessage)
        assert len(last_message.content) > 0  # Should have real content

    def test_schema_composition_with_engines(self, simple_agents):
        """Test that schema composition includes engine fields."""
        agent1, agent2 = simple_agents

        multi = ProperMultiAgent(name="test_multi", agents=[agent1, agent2])

        # Should have engines from both agents
        assert isinstance(multi.engines, dict)
        assert len(multi.engines) > 0

        # Check that agent engines are namespaced properly
        engine_keys = list(multi.engines.keys())
        agent1_engines = [k for k in engine_keys if k.startswith("agent1.")]
        agent2_engines = [k for k in engine_keys if k.startswith("agent2.")]

        assert len(agent1_engines) > 0, f"No agent1 engines found in {engine_keys}"
        assert len(agent2_engines) > 0, f"No agent2 engines found in {engine_keys}"
