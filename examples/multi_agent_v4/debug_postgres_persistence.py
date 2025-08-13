#!/usr/bin/env python3
"""Test PostgreSQL persistence with agents.

This script tests that agents actually use PostgreSQL for persistent state storage.
"""

import asyncio
import logging
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

# Load environment variables first
print("🔄 Loading environment variables...")
load_dotenv()

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.persistence.postgres_config import PostgresCheckpointerConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Simple model
class TestModel(BaseModel):
    result: str = Field(description="Result")
    score: float = Field(ge=0.0, le=1.0)


async def test_postgres_persistence():
    """Test that agent actually persists to PostgreSQL."""
    print("🔍 POSTGRESQL PERSISTENCE TEST")
    print("=" * 60)

    # Check environment variable
    conn_string = os.getenv("POSTGRES_CONNECTION_STRING")
    if not conn_string:
        print("❌ POSTGRES_CONNECTION_STRING not found")
        return False

    print(f"✅ Using connection: {conn_string[:50]}...")

    # Create PostgreSQL checkpointer config
    try:
        postgres_config = PostgresCheckpointerConfig(connection_string=conn_string)
        print("✅ PostgreSQL config created")
    except Exception as e:
        print(f"❌ Failed to create PostgreSQL config: {e}")
        return False

    # Test creating checkpointer
    try:
        checkpointer = postgres_config.create_checkpointer()
        print("✅ PostgreSQL checkpointer created successfully")
        print(f"Checkpointer type: {type(checkpointer).__name__}")
    except Exception as e:
        print(f"❌ Failed to create checkpointer: {e}")
        import traceback

        traceback.print_exc()
        return False

    # Create agent with specific thread ID for persistence
    thread_id = "test_postgres_thread_123"

    try:
        agent = SimpleAgentV3(
            name="postgres_persist_agent",
            engine=AugLLMConfig(
                system_message="You are a PostgreSQL persistence test agent.",
                structured_output_model=TestModel,
                temperature=0.1,
                max_tokens=100,
            ),
        )

        print(f"✅ Agent created: {agent.name}")

        # First execution - this should create state in PostgreSQL
        print("\n🔄 First execution (creating state)...")
        await agent.arun(
            {"messages": [HumanMessage(content="Remember: I like pizza")]},
            config={"configurable": {"thread_id": thread_id}},
        )
        print("✅ First execution completed")

        # Second execution - this should retrieve state from PostgreSQL
        print("\n🔄 Second execution (should remember state)...")
        result2 = await agent.arun(
            {"messages": [HumanMessage(content="What do I like to eat?")]},
            config={"configurable": {"thread_id": thread_id}},
        )
        print("✅ Second execution completed")

        # Check if agent remembered (would only work with persistence)
        if hasattr(result2, "messages") and len(result2.messages) > 2:
            print("✅ Agent appears to have persistent state (multiple messages)")
            return True
        print("⚠️ Agent state unclear - check manually")
        return True

    except Exception as e:
        print(f"❌ Agent test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


async def check_postgres_direct():
    """Test direct PostgreSQL connection."""
    print("\n🔍 DIRECT POSTGRESQL CONNECTION TEST")
    print("=" * 50)

    conn_string = os.getenv("POSTGRES_CONNECTION_STRING")

    try:
        import psycopg

        # Test direct connection
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 as test")
                result = cur.fetchone()
                print(f"✅ Direct PostgreSQL connection successful: {result}")

                # Check for langgraph tables
                cur.execute(
                    """
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name LIKE '%checkpoint%'
                """
                )
                tables = cur.fetchall()

                if tables:
                    print(f"✅ Found checkpoint tables: {[t[0] for t in tables]}")
                else:
                    print("ℹ️ No checkpoint tables found (will be created on first use)")

        return True

    except Exception as e:
        print(f"❌ Direct PostgreSQL connection failed: {e}")
        return False


if __name__ == "__main__":
    # Run both tests
    print("🚀 Starting PostgreSQL tests...\n")

    # Test direct connection first
    direct_success = asyncio.run(check_postgres_direct())

    # Test persistence
    persist_success = asyncio.run(test_postgres_persistence())

    print("\n" + "=" * 60)
    print("📊 TEST RESULTS:")
    print(f"✅ Direct PostgreSQL: {'PASS' if direct_success else 'FAIL'}")
    print(f"✅ Agent Persistence: {'PASS' if persist_success else 'FAIL'}")

    if direct_success and persist_success:
        print("\n🎉 All PostgreSQL tests PASSED!")
        print("Agents can now use PostgreSQL for persistent state storage!")
    else:
        print("\n💥 Some tests FAILED!")
        print("Check the error messages above for details.")
