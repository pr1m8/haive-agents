"""Test Memory V2 system with DeepSeek LLM to avoid OpenAI quota issues."""

import asyncio
import os

# Set DeepSeek API key if available
if not os.getenv("DEEPSEEK_API_KEY"):
    print("⚠️  DEEPSEEK_API_KEY not set. Setting a test key...")
    os.environ["DEEPSEEK_API_KEY"] = "test-key-replace-with-real"

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


async def test_deepseek_config():
    """Test creating DeepSeek configuration."""
    print("\n=== Testing DeepSeek Configuration ===\n")

    try:
        # Create DeepSeek LLM config
        deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)
        print(f"✅ Created DeepSeekLLMConfig: {deepseek_config.model}")

        # Create AugLLMConfig with DeepSeek
        aug_config = AugLLMConfig(
            llm_config=deepseek_config,
            system_message="You are a helpful memory assistant.",
        )
        print("✅ Created AugLLMConfig with DeepSeek")

        return aug_config

    except Exception as e:
        print(f"❌ Failed to create DeepSeek config: {e}")
        import traceback

        traceback.print_exc()
        return None


async def test_simple_memory_with_deepseek():
    """Test SimpleMemoryAgent with DeepSeek."""
    print("\n=== Testing SimpleMemoryAgent with DeepSeek ===\n")

    aug_config = await test_deepseek_config()
    if not aug_config:
        return

    try:
        from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent

        agent = SimpleMemoryAgent(
            name="test_deepseek", engine=aug_config, user_id="test_user"
        )
        print("✅ Created SimpleMemoryAgent with DeepSeek")

        # Test storing memory
        result = await agent.arun(
            "Remember: Alice works at TechCorp as an AI researcher"
        )
        print(f"Stored memory: {len(str(result)) > 0}")

        # Test querying memory
        query_result = await agent.arun("Who is Alice and what does she do?")
        print(f"Query result preview: {str(query_result)[:200]}...")

    except Exception as e:
        print(f"❌ SimpleMemoryAgent test failed: {e}")
        import traceback

        traceback.print_exc()


async def test_react_memory_with_deepseek():
    """Test ReactMemoryAgent with DeepSeek."""
    print("\n=== Testing ReactMemoryAgent with DeepSeek ===\n")

    aug_config = await test_deepseek_config()
    if not aug_config:
        return

    try:
        # First, let's try creating embeddings without OpenAI
        from langchain_community.embeddings import HuggingFaceEmbeddings

        print("Creating HuggingFace embeddings (free, no API key needed)...")
        HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False},
        )
        print("✅ Created HuggingFace embeddings")

        # Now create ReactMemoryAgent with custom embeddings

        # We'll need to modify the agent to accept custom embeddings
        # For now, let's see if we can at least import it
        print("ReactMemoryAgent would need modification to accept custom embeddings")

    except Exception as e:
        print(f"❌ ReactMemoryAgent test failed: {e}")
        import traceback

        traceback.print_exc()


async def test_models_only():
    """Test just the memory models without LLMs."""
    print("\n=== Testing Memory Models (No LLM Required) ===\n")

    from haive.agents.memory_v2.memory_state_original import (
        EnhancedMemoryItem,
        ImportanceLevel,
        MemoryState,
        MemoryType,
    )

    # Create a memory state
    state = MemoryState(user_id="test_user")

    # Add some memories
    memories = [
        ("Bob is the CTO of DataCorp", MemoryType.FACTUAL, ImportanceLevel.HIGH),
        (
            "Meeting with Bob scheduled for Tuesday",
            MemoryType.CONVERSATIONAL,
            ImportanceLevel.MEDIUM,
        ),
        (
            "DataCorp specializes in cloud infrastructure",
            MemoryType.FACTUAL,
            ImportanceLevel.MEDIUM,
        ),
    ]

    for content, mem_type, importance in memories:
        memory = EnhancedMemoryItem(
            content=content,
            memory_type=mem_type,
            importance=importance,
            user_id="test_user",
        )
        state.add_memory_item(memory)

    print(f"✅ Added {len(memories)} memories to state")

    # Search memories
    results = state.search_memories("Bob")
    print(f"✅ Search 'Bob': Found {len(results)} results")

    for i, result in enumerate(results):
        print(f"   {i+1}. {result.content}")

    # Check stats
    print("\n📊 Memory Statistics:")
    print(f"   Total memories: {state.stats.total_memories}")
    print(f"   By type: {dict(state.stats.memories_by_type)}")
    print(f"   By importance: {dict(state.stats.memories_by_importance)}")


async def main():
    """Run all tests."""
    print("\n🚀 Testing Memory V2 with DeepSeek 🚀")
    print("=" * 60)

    # Test basic models first (no LLM needed)
    await test_models_only()

    # Test with DeepSeek if API key is available
    if (
        os.getenv("DEEPSEEK_API_KEY")
        and os.getenv("DEEPSEEK_API_KEY") != "test-key-replace-with-real"
    ):
        await test_simple_memory_with_deepseek()
        await test_react_memory_with_deepseek()
    else:
        print("\n⚠️  Skipping DeepSeek tests - no valid API key set")
        print("   Set DEEPSEEK_API_KEY environment variable to test with DeepSeek")

    print("\n" + "=" * 60)
    print("✨ Tests completed! ✨")


if __name__ == "__main__":
    asyncio.run(main())
