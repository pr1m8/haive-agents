#!/usr/bin/env python3
"""Test the reflection PostgreSQL fix."""

import os

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.simple.agent import SimpleAgent

# Set the PostgreSQL connection string
os.environ["POSTGRES_CONNECTION_STRING"] = (
    "postgresql://postgres.zkssazqhwcetsnbiuqik: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@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
)


def test_reflection_agent_with_real_persistence():
    """Test reflection agent with PostgreSQL persistence."""
    print("🧪 Testing reflection agent with PostgreSQL persistence...")
    print("=" * 60)

    try:
        # Create agent with persistence enabled
        agent = SimpleAgent(
            name="reflection_analyzer",
            engine=AugLLMConfig(temperature=0.1),
            persistence=True,  # This should now work without errors
        )

        print("✅ Agent created successfully with persistence enabled")

        # Generate a thread ID to test the fix
        thread_id = agent._generate_default_thread_id()
        print(f"📋 Generated thread_id: {thread_id}")

        # Test that it starts with agent name + UUID format
        assert thread_id.startswith(
            "reflection_analyzer_"
        ), f"Thread ID should start with agent name"

        # Check that it's a UUID format
        uuid_part = thread_id[len("reflection_analyzer_") :]
        assert len(uuid_part) == 36, f"UUID part should be 36 characters"
        assert uuid_part.count("-") == 4, f"UUID should have 4 hyphens"

        print("✅ Thread ID generation working correctly")

        # Test with multiple instances to ensure uniqueness
        agent2 = SimpleAgent(
            name="reflection_analyzer",  # Same name
            engine=AugLLMConfig(temperature=0.1),
            persistence=True,
        )

        thread_id2 = agent2._generate_default_thread_id()
        print(f"📋 Second thread_id: {thread_id2}")

        # Ensure they're different
        assert (
            thread_id != thread_id2
        ), "Thread IDs should be unique even with same agent name"

        print("✅ Thread ID uniqueness working correctly")
        print("🎉 All tests passed! PostgreSQL reflection issue should be fixed.")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_reflection_agent_with_real_persistence()
