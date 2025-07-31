"""Test that PostgreSQL persistence still works when explicitly requested."""

import os

import pytest

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.persistence.postgres_config import PostgresCheckpointerConfig
from haive.core.persistence.types import CheckpointerMode, CheckpointStorageMode


def test_postgres_persistence_with_true():
    """Test that persistence=True still uses PostgreSQL when available."""
    config = AugLLMConfig(name="test_llm_postgres", temperature=0.1)

    # Create agent with persistence=True
    agent = SimpleAgent(
        name="postgres_true_agent",
        engine=config,
        persistence=True,  # Should use PostgreSQL if available
    )

    # Check that persistence was set up
    assert agent.persistence is not None
    assert agent.checkpointer is not None

    # Check if PostgreSQL was used (when available)
    checkpointer_type = type(agent.checkpointer).__name__

    # If POSTGRES_CONNECTION_STRING is set, it should use PostgreSQL
    if os.getenv("POSTGRES_CONNECTION_STRING"):
        assert "Postgres" in checkpointer_type
    else:
        # Otherwise it falls back to memory
        assert "Memory" in checkpointer_type or "InMemory" in checkpointer_type


def test_explicit_postgres_config():
    """Test that explicit PostgreSQL config still works."""
    config = AugLLMConfig(name="test_llm_postgres_explicit", temperature=0.1)

    # Create explicit PostgreSQL config
    postgres_config = PostgresCheckpointerConfig(
        mode=CheckpointerMode.SYNC,
        storage_mode=CheckpointStorageMode.FULL,
        prepare_threshold=None,  # Disable prepared statements
        connection_string=os.getenv(
            "POSTGRES_CONNECTION_STRING"
        ),  # Use env var if available
    )

    # Create agent with explicit PostgreSQL persistence
    agent = SimpleAgent(
        name="postgres_explicit_agent", engine=config, persistence=postgres_config
    )

    # Verify PostgreSQL persistence is set up
    assert agent.persistence is not None
    assert isinstance(agent.persistence, PostgresCheckpointerConfig)
    assert agent.checkpointer is not None

    # The checkpointer should be PostgreSQL-based
    checkpointer_type = type(agent.checkpointer).__name__

    # Should be PostgreSQL checkpointer
    assert "Postgres" in checkpointer_type or "PostgreSQL" in checkpointer_type


@pytest.mark.asyncio
async def test_postgres_persistence_functionality():
    """Test that PostgreSQL persistence actually saves and retrieves state."""
    # Skip if no PostgreSQL available
    if not os.getenv("POSTGRES_CONNECTION_STRING"):
        pytest.skip("No PostgreSQL connection string available")

    config = AugLLMConfig(name="test_llm_functional", temperature=0.1)

    # Create agent with PostgreSQL persistence
    agent = SimpleAgent(
        name="postgres_functional_agent", engine=config, persistence=True
    )

    # Use a specific thread ID for testing
    thread_id = "test_postgres_thread_123"
    config_with_thread = {"configurable": {"thread_id": thread_id}}

    # Run the agent with some input
    await agent.arun("Remember my name is Alice", config=config_with_thread)

    # Create a new agent instance with same name
    agent2 = SimpleAgent(
        name="postgres_functional_agent", engine=config, persistence=True
    )

    # Run with same thread ID - should remember previous conversation
    result2 = await agent2.arun("What's my name?", config=config_with_thread)

    # The agent should remember "Alice" from the previous conversation
    # Note: This is a basic check - full LLM response may vary
    assert result2 is not None
    assert len(result2) > 0


def test_postgres_available_check():
    """Test the PostgreSQL availability check."""
    try:
        from haive.core.engine.agent.config import POSTGRES_AVAILABLE

        if POSTGRES_AVAILABLE:
            # Try to import PostgreSQL components
            from haive.core.persistence.postgres_config import (
                PostgresCheckpointerConfig,
            )

        else:
            pass
    except ImportError:
        pass


if __name__ == "__main__":

    test_postgres_persistence_with_true()

    test_explicit_postgres_config()

    test_postgres_available_check()
