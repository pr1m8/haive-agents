"""Simple test to verify PostgreSQL persistence is working."""

import os

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.simple.agent import SimpleAgent


def test_postgres_setup_works():
    """Test that PostgreSQL persistence sets up correctly."""
    # Create agent with persistence=True
    agent = SimpleAgent(name="postgres_test", engine=AugLLMConfig(), persistence=True)

    # Check persistence was set up
    print(f"\nPersistence type: {type(agent.persistence).__name__}")
    print(f"Checkpointer type: {type(agent.checkpointer).__name__}")

    # Should have PostgreSQL if POSTGRES_CONNECTION_STRING is set
    if os.getenv("POSTGRES_CONNECTION_STRING"):
        assert "Postgres" in type(agent.checkpointer).__name__
        print("✓ PostgreSQL persistence is set up correctly")
    else:
        assert (
            "Memory" in type(agent.checkpointer).__name__
            or "InMemory" in type(agent.checkpointer).__name__
        )
        print("✓ Memory persistence is set up (PostgreSQL not available)")


@pytest.mark.asyncio
async def test_basic_postgres_save_and_load():
    """Test basic save and load with PostgreSQL."""
    if not os.getenv("POSTGRES_CONNECTION_STRING"):
        pytest.skip("No PostgreSQL connection available")

    # Create agent
    agent = SimpleAgent(name="save_load_test", engine=AugLLMConfig(), persistence=True)

    # Get the checkpointer directly
    checkpointer = agent.checkpointer
    print(f"\nCheckpointer: {type(checkpointer).__name__}")

    # Create a simple checkpoint
    import uuid

    from langgraph.checkpoint import Checkpoint

    thread_id = str(uuid.uuid4())
    checkpoint = Checkpoint(
        id=str(uuid.uuid4()),
        ts=str(uuid.uuid4()),
        channel_values={"messages": []},
        channel_versions={},
        versions_seen={},
    )

    # Save checkpoint
    config = {"configurable": {"thread_id": thread_id}}
    checkpointer.put(config, checkpoint, {}, {})
    print("✓ Checkpoint saved successfully")

    # Load checkpoint
    loaded = checkpointer.get_tuple(config)
    assert loaded is not None
    assert loaded.checkpoint.id == checkpoint.id
    print("✓ Checkpoint loaded successfully")

    # Verify it's using PostgreSQL
    assert "Postgres" in type(checkpointer).__name__
    print("✓ Confirmed using PostgreSQL checkpointer")


if __name__ == "__main__":
    print("Testing PostgreSQL persistence...\n")

    test_postgres_setup_works()

    import asyncio

    asyncio.run(test_basic_postgres_save_and_load())
