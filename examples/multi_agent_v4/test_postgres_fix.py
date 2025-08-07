#!/usr/bin/env python3
"""Test the postgres fix by running a simple agent with postgres enabled.

This will test if the ON CONFLICT fix resolves the duplicate key constraint error.

Date: August 7, 2025
"""

import asyncio
import os
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Simple model for testing
class SimpleResult(BaseModel):
    """Simple result output."""

    summary: str = Field(description="Brief summary")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")


async def test_postgres_persistence():
    """Test agent with postgres persistence enabled."""

    # Make sure postgres is enabled (remove disable flag if set)
    if "HAIVE_DISABLE_POSTGRES" in os.environ:
        del os.environ["HAIVE_DISABLE_POSTGRES"]

    print("🔍 TESTING POSTGRES PERSISTENCE FIX")
    print("=" * 60)

    # Create agent with v1 structured output (which works)
    agent = SimpleAgentV3(
        name="postgres_test_agent",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=150,
            system_message="You are a helpful assistant.",
            structured_output_model=SimpleResult,
            # Use v1 (parser-based) which works
            structured_output_version="v1",
        ),
    )

    print(f"Agent name: {agent.name}")
    print(f"Structured output: {agent.engine.structured_output_model}")
    print(f"Version: {agent.engine.structured_output_version}")

    try:
        print("\n🎯 RUNNING FIRST EXECUTION...")
        result1 = await agent.arun(
            {"messages": [HumanMessage(content="Analyze today's weather briefly")]}
        )
        print("✅ First execution completed successfully!")

        print("\n🎯 RUNNING SECOND EXECUTION (same agent)...")
        result2 = await agent.arun({"messages": [HumanMessage(content="What's 2+2?")]})
        print("✅ Second execution completed successfully!")

        print("\n🎯 CREATING NEW AGENT WITH SAME NAME...")
        agent2 = SimpleAgentV3(
            name="postgres_test_agent",  # Same name!
            engine=AugLLMConfig(
                temperature=0.3,
                structured_output_model=SimpleResult,
                structured_output_version="v1",
            ),
        )

        result3 = await agent2.arun(
            {"messages": [HumanMessage(content="Tell me about cats")]}
        )
        print("✅ Third execution (new agent, same name) completed!")

        print("\n" + "=" * 60)
        print(
            "🎉 SUCCESS: All postgres operations completed without duplicate key errors!"
        )
        print("✅ The ON CONFLICT fix appears to be working")

        return True

    except Exception as e:
        print(f"\n❌ ERROR: {type(e).__name__}: {e}")

        if "duplicate key value violates unique constraint" in str(e):
            print("\n🔍 POSTGRES DUPLICATE KEY ERROR DETECTED:")
            print("- This means the fix hasn't been applied yet")
            print("- Need to update postgres_saver_with_thread_creation.py")
            print("- Change 'ON CONFLICT (id, user_id)' to 'ON CONFLICT (id)'")

        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_postgres_persistence())

    if success:
        print("\n💡 POSTGRES PERSISTENCE IS WORKING!")
    else:
        print("\n🛠️  POSTGRES FIX STILL NEEDED")
        print("\nTo fix:")
        print(
            "1. Edit packages/haive-core/src/haive/core/persistence/postgres_saver_with_thread_creation.py"
        )
        print(
            "2. Change line 72 from 'ON CONFLICT (id, user_id)' to 'ON CONFLICT (id)'"
        )
        print("3. Do the same for lines 84, 209, and 222 (async versions)")
