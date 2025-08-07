#!/usr/bin/env python3
"""Test PostgreSQL connection with environment variables.

This script tests:
1. Loading .env file
2. PostgreSQL connection from environment
3. Store factory working correctly
4. Agent with PostgreSQL persistence
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
from haive.core.persistence.store.factory import create_store
from haive.core.persistence.store.types import StoreType

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Simple model
class TestModel(BaseModel):
    result: str = Field(description="Result")
    score: float = Field(ge=0.0, le=1.0)


async def test_postgres_connection():
    """Test PostgreSQL connection and store creation."""

    print("🔍 POSTGRESQL CONNECTION DEBUG")
    print("=" * 60)

    # Check environment variable
    conn_string = os.getenv("POSTGRES_CONNECTION_STRING")
    if conn_string:
        print(f"✅ POSTGRES_CONNECTION_STRING found: {conn_string[:50]}...")
    else:
        print("❌ POSTGRES_CONNECTION_STRING not found in environment")
        return False

    # Test store creation with PostgreSQL
    print("\n🔄 Testing PostgreSQL store creation...")
    try:
        # Create store with connection string
        postgres_store = create_store(
            store_type=StoreType.POSTGRES_SYNC, connection_string=conn_string
        )
        print(f"✅ PostgreSQL store created: {type(postgres_store).__name__}")

    except Exception as e:
        print(f"❌ PostgreSQL store creation failed: {e}")
        return False

    # Test agent with PostgreSQL persistence
    print("\n🤖 Testing agent with PostgreSQL persistence...")
    try:
        agent = SimpleAgentV3(
            name="postgres_test_agent",
            engine=AugLLMConfig(
                system_message="You are a test agent with PostgreSQL persistence.",
                structured_output_model=TestModel,
                temperature=0.1,
                max_tokens=50,
            ),
        )

        print(f"Agent created: {agent.name}")

        # Test execution
        result = await agent.arun(
            {"messages": [HumanMessage(content="Test PostgreSQL")]}
        )
        print(f"✅ Agent executed successfully")
        print(f"Result type: {type(result)}")

        return True

    except Exception as e:
        print(f"❌ Agent execution failed: {e}")
        import traceback

        traceback.print_exc()
        return False


async def test_without_disabling_postgres():
    """Test with PostgreSQL enabled."""

    # Make sure PostgreSQL is NOT disabled
    if "HAIVE_DISABLE_POSTGRES" in os.environ:
        del os.environ["HAIVE_DISABLE_POSTGRES"]

    return await test_postgres_connection()


if __name__ == "__main__":
    success = asyncio.run(test_without_disabling_postgres())

    if success:
        print("\n🎉 PostgreSQL connection test PASSED!")
    else:
        print("\n💥 PostgreSQL connection test FAILED!")
        print("\nPossible issues:")
        print("1. .env file not found or not loaded")
        print("2. POSTGRES_CONNECTION_STRING not set correctly")
        print("3. PostgreSQL server not accessible")
        print("4. Connection string format incorrect")
