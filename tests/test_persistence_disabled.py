"""Test that persistence can be properly disabled with persistence=False."""

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def test_persistence_explicitly_disabled():
    """Test that persistence=False properly disables persistence."""
    config = AugLLMConfig(name="test_llm", temperature=0.1)

    # Create agent with persistence explicitly disabled
    agent = SimpleAgent(
        name="no_persistence_agent",
        engine=config,
        persistence=False,  # Explicitly disable persistence
    )

    # Verify persistence is disabled
    assert agent.persistence is False
    assert agent.checkpointer is None
    assert agent.store is None

    # But runnable config should still be set up for recursion limit
    assert agent.runnable_config is not None
    assert "configurable" in agent.runnable_config
    assert "recursion_limit" in agent.runnable_config["configurable"]
    assert agent.runnable_config["configurable"]["recursion_limit"] == 100


def test_persistence_default_is_memory():
    """Test that persistence=None (default) uses memory persistence."""
    config = AugLLMConfig(name="test_llm_2", temperature=0.1)

    # Create agent with default persistence (None)
    agent = SimpleAgent(
        name="default_persistence_agent",
        engine=config,
        # persistence defaults to None
    )

    # Verify memory persistence is set up
    assert agent.persistence is not None
    assert agent.checkpointer is not None
    assert (
        "Memory" in type(agent.checkpointer).__name__
        or "InMemory" in type(agent.checkpointer).__name__
    )

    # Store should also be set up
    assert agent.store is not None


def test_persistence_true_uses_defaults():
    """Test that persistence=True uses default persistence (PostgreSQL if available)."""
    config = AugLLMConfig(name="test_llm_3", temperature=0.1)

    # Create agent with persistence=True
    agent = SimpleAgent(
        name="postgres_persistence_agent",
        engine=config,
        persistence=True,  # Use default persistence
    )

    # Verify persistence is set up (could be PostgreSQL or memory depending on environment)
    assert agent.persistence is not None
    assert agent.checkpointer is not None

    # The type depends on whether PostgreSQL is available
    checkpointer_type = type(agent.checkpointer).__name__
    assert "Saver" in checkpointer_type or "Checkpointer" in checkpointer_type


if __name__ == "__main__":
    test_persistence_explicitly_disabled()

    test_persistence_default_is_memory()

    test_persistence_true_uses_defaults()
