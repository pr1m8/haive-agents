"""Test MultiAgent list initialization patterns."""

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.multi import MultiAgent
from haive.agents.simple import SimpleAgent


def test_multi_agent_list_initialization():
    """Test that MultiAgent can be initialized with a list of agents."""
    # Create test agents
    agent1 = SimpleAgent(name="analyzer", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="formatter", engine=AugLLMConfig())
    agent3 = SimpleAgent(name="reviewer", engine=AugLLMConfig())

    # Test direct list initialization
    multi = MultiAgent(agents=[agent1, agent2, agent3])

    # Verify the agents are properly stored as a dict
    assert isinstance(multi.agents, dict)
    assert len(multi.agents) == 3
    assert "analyzer" in multi.agents
    assert "formatter" in multi.agents
    assert "reviewer" in multi.agents

    # Verify the agents are the same objects
    assert multi.agents["analyzer"] is agent1
    assert multi.agents["formatter"] is agent2
    assert multi.agents["reviewer"] is agent3


def test_multi_agent_factory_method():
    """Test the factory method for creating MultiAgent from list."""
    # Create test agents
    agent1 = SimpleAgent(name="analyzer", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="formatter", engine=AugLLMConfig())

    # Test factory method
    multi = MultiAgent.create(
        agents=[agent1, agent2], name="test_pipeline", execution_mode="sequential"
    )

    # Verify properties
    assert multi.name == "test_pipeline"
    assert multi.execution_mode == "sequential"
    assert len(multi.agents) == 2
    assert "analyzer" in multi.agents
    assert "formatter" in multi.agents


def test_multi_agent_agents_without_names():
    """Test MultiAgent with agents that don't have names."""
    # Create agents without explicit names
    agent1 = SimpleAgent(engine=AugLLMConfig())
    agent2 = SimpleAgent(engine=AugLLMConfig())

    multi = MultiAgent(agents=[agent1, agent2])

    # Should create default names
    assert len(multi.agents) == 2
    agent_names = list(multi.agents.keys())

    # Should have some form of default naming
    assert len(agent_names) == 2
    assert all(name for name in agent_names)  # Names should not be empty


def test_multi_agent_dict_initialization():
    """Test that dict initialization still works."""
    agent1 = SimpleAgent(name="analyzer", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="formatter", engine=AugLLMConfig())

    multi = MultiAgent(agents={"custom_analyzer": agent1, "custom_formatter": agent2})

    # Verify dict structure is preserved
    assert len(multi.agents) == 2
    assert "custom_analyzer" in multi.agents
    assert "custom_formatter" in multi.agents
    assert multi.agents["custom_analyzer"] is agent1
    assert multi.agents["custom_formatter"] is agent2


def test_multi_agent_single_agent():
    """Test initialization with a single agent."""
    agent = SimpleAgent(name="solo", engine=AugLLMConfig())

    multi = MultiAgent(agent=agent)

    # Should convert single agent to dict
    assert len(multi.agents) == 1
    assert "solo" in multi.agents
    assert multi.agents["solo"] is agent


def test_multi_agent_execution_modes():
    """Test that different execution modes are supported."""
    agent1 = SimpleAgent(name="first", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="second", engine=AugLLMConfig())

    # Test different execution modes
    sequential = MultiAgent(agents=[agent1, agent2], execution_mode="sequential")
    parallel = MultiAgent(agents=[agent1, agent2], execution_mode="parallel")
    conditional = MultiAgent(agents=[agent1, agent2], execution_mode="conditional")

    assert sequential.execution_mode == "sequential"
    assert parallel.execution_mode == "parallel"
    assert conditional.execution_mode == "conditional"


def test_multi_agent_default_execution_mode():
    """Test that default execution mode is 'infer'."""
    agent1 = SimpleAgent(name="first", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="second", engine=AugLLMConfig())

    multi = MultiAgent(agents=[agent1, agent2])

    # Default should be 'infer'
    assert multi.execution_mode == "infer"


def test_multi_agent_empty_agents_list():
    """Test handling of empty agents list."""
    with pytest.raises(Exception):  # Should raise some validation error
        MultiAgent(agents=[])


if __name__ == "__main__":
    # Run tests manually
    test_multi_agent_list_initialization()
    test_multi_agent_factory_method()
    test_multi_agent_agents_without_names()
    test_multi_agent_dict_initialization()
    test_multi_agent_single_agent()
    test_multi_agent_execution_modes()
    test_multi_agent_default_execution_mode()
