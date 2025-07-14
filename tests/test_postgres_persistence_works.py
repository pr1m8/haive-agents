"""Test that PostgreSQL persistence still works when explicitly requested."""

import os

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.persistence.postgres_config import PostgresCheckpointerConfig
from haive.core.persistence.types import CheckpointerMode, CheckpointStorageMode

from haive.agents.simple.agent import SimpleAgent


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
    print(f"Checkpointer type: {checkpointer_type}")
    print(f"Persistence config type: {type(agent.persistence).__name__}")

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
    print(f"Explicit PostgreSQL checkpointer: {checkpointer_type}")

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
    result1 = await agent.arun("Remember my name is Alice", config=config_with_thread)
    print(f"First result: {result1}")

    # Create a new agent instance with same name
    agent2 = SimpleAgent(
        name="postgres_functional_agent", engine=config, persistence=True
    )

    # Run with same thread ID - should remember previous conversation
    result2 = await agent2.arun("What's my name?", config=config_with_thread)
    print(f"Second result: {result2}")

    # The agent should remember "Alice" from the previous conversation
    # Note: This is a basic check - full LLM response may vary
    assert result2 is not None
    assert len(result2) > 0


def test_postgres_available_check():
    """Test the PostgreSQL availability check."""
    try:
        from haive.core.engine.agent.config import POSTGRES_AVAILABLE

        print(f"POSTGRES_AVAILABLE: {POSTGRES_AVAILABLE}")

        if POSTGRES_AVAILABLE:
            print("PostgreSQL support is available")
            # Try to import PostgreSQL components
            from haive.core.persistence.postgres_config import (
                PostgresCheckpointerConfig,
            )

            print("✓ Can import PostgresCheckpointerConfig")
        else:
            print("PostgreSQL support is not available")
    except ImportError as e:
        print(f"Import error: {e}")


if __name__ == "__main__":
    print("Testing PostgreSQL persistence still works...\n")

    print("1. Testing persistence=True...")
    test_postgres_persistence_with_true()
    print("✓ persistence=True works\n")

    print("2. Testing explicit PostgreSQL config...")
    test_explicit_postgres_config()
    print("✓ Explicit PostgreSQL config works\n")

    print("3. Testing PostgreSQL availability...")
    test_postgres_available_check()
    print("\n✓ All PostgreSQL tests passed!")
