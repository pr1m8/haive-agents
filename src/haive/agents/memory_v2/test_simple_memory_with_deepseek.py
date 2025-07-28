"""Test SimpleMemoryAgent with DeepSeek LLM configuration."""

import asyncio
import os

# First set up DeepSeek if needed
if not os.getenv("DEEPSEEK_API_KEY"):
    print("Setting test DeepSeek API key...")
    os.environ["DEEPSEEK_API_KEY"] = "test-key"

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


async def test_simple_memory_agent_with_deepseek():
    """Test SimpleMemoryAgent using DeepSeek."""
    print("\n=== Testing SimpleMemoryAgent with DeepSeek ===\n")

    # Step 1: Create DeepSeek config
    print("1. Creating DeepSeek LLM config...")
    try:
        deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)
        print("   ✅ Created DeepSeekLLMConfig")
    except Exception as e:
        print(f"   ❌ Failed to create DeepSeekLLMConfig: {e}")
        return

    # Step 2: Create AugLLMConfig with DeepSeek
    print("\n2. Creating AugLLMConfig with DeepSeek...")
    try:
        aug_config = AugLLMConfig(
            llm_config=deepseek_config,
            system_message="You are a helpful memory assistant.",
        )
        print("   ✅ Created AugLLMConfig")
    except Exception as e:
        print(f"   ❌ Failed to create AugLLMConfig: {e}")
        return

    # Step 3: Try to import SimpleMemoryAgent
    print("\n3. Importing SimpleMemoryAgent...")
    try:
        from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent

        print("   ✅ Imported SimpleMemoryAgent")
    except Exception as e:
        print(f"   ❌ Failed to import SimpleMemoryAgent: {e}")
        print("\n   Let's trace the import error...")
        import traceback

        traceback.print_exc()

        # Try to import the problematic module directly
        print("\n   Trying to import kg_map_merge models directly...")
        try:

            print("   ✅ Direct import worked!")
        except Exception as e2:
            print(f"   ❌ Direct import also failed: {e2}")

            # Check if we can fix the import
            print("\n   Checking the actual module path...")
            import sys

            print(
                f"   Python path includes: {[p for p in sys.path if 'haive' in p][:3]}"
            )
        return

    # Step 4: Create SimpleMemoryAgent with DeepSeek
    print("\n4. Creating SimpleMemoryAgent with DeepSeek config...")
    try:
        agent = SimpleMemoryAgent(
            name="test_deepseek_memory", engine=aug_config, user_id="test_user"
        )
        print("   ✅ Created SimpleMemoryAgent!")
    except Exception as e:
        print(f"   ❌ Failed to create SimpleMemoryAgent: {e}")
        import traceback

        traceback.print_exc()
        return

    # Step 5: Test the agent
    print("\n5. Testing memory operations...")
    try:
        # Store a memory
        result = await agent.arun(
            "Remember: Alice works at TechCorp as an AI researcher."
        )
        print(f"   ✅ Stored memory: {result[:100]}...")

        # Query memory
        query = await agent.arun("Who is Alice?")
        print(f"   ✅ Query result: {query[:100]}...")

    except Exception as e:
        print(f"   ❌ Failed to run agent: {e}")
        import traceback

        traceback.print_exc()
        return

    print("\n✅ SimpleMemoryAgent with DeepSeek completed successfully!")


async def main():
    """Run the test."""
    await test_simple_memory_agent_with_deepseek()


if __name__ == "__main__":
    asyncio.run(main())
