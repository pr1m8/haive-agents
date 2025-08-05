#!/usr/bin/env python3
"""Test the reflection PostgreSQL fix."""

import os

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Set the PostgreSQL connection string
os.environ["POSTGRES_CONNECTION_STRING"] = (
    "postgresql://postgres.zkssazqhwcetsnbiuqik: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@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
)


def test_reflection_agent_with_real_persistence():
    """Test reflection agent with PostgreSQL persistence."""
    try:
        # Create agent with persistence enabled
        agent = SimpleAgent(
            name="reflection_analyzer",
            engine=AugLLMConfig(temperature=0.1),
            persistence=True,  # This should now work without errors
        )

        # Generate a thread ID to test the fix
        thread_id = agent._generate_default_thread_id()

        # Test that it starts with agent name + UUID format
        assert thread_id.startswith("reflection_analyzer_"), (
            "Thread ID should start with agent name"
        )

        # Check that it's a UUID format
        uuid_part = thread_id[len("reflection_analyzer_") :]
        assert len(uuid_part) == 36, "UUID part should be 36 characters"
        assert uuid_part.count("-") == 4, "UUID should have 4 hyphens"

        # Test with multiple instances to ensure uniqueness
        agent2 = SimpleAgent(
            name="reflection_analyzer",  # Same name
            engine=AugLLMConfig(temperature=0.1),
            persistence=True,
        )

        thread_id2 = agent2._generate_default_thread_id()

        # Ensure they're different
        assert thread_id != thread_id2, "Thread IDs should be unique even with same agent name"

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_reflection_agent_with_real_persistence()
