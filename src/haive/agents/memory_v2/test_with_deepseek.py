"""Test Memory V2 system with DeepSeek LLM to avoid OpenAI quota issues."""

import asyncio
import os
import traceback

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from langchain_community.embeddings import HuggingFaceEmbeddings

from haive.agents.memory_v2.memory_state_original import (
    EnhancedMemoryItem,
    ImportanceLevel,
    MemoryState,
    MemoryType,
)
from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent

# Set DeepSeek API key if available
if not os.getenv("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = "test-key-replace-with-real"


async def test_deepseek_config():
    """Test creating DeepSeek configuration."""
    try:
        # Create DeepSeek LLM config
        deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)

        # Create AugLLMConfig with DeepSeek
        aug_config = AugLLMConfig(
            llm_config=deepseek_config,
            system_message="You are a helpful memory assistant.",
        )

        return aug_config

    except Exception:
        traceback.print_exc()
        return None


async def test_simple_memory_with_deepseek():
    """Test SimpleMemoryAgent with DeepSeek."""
    aug_config = await test_deepseek_config()
    if not aug_config:
        return

    try:
        agent = SimpleMemoryAgent(
            name="test_deepseek", engine=aug_config, user_id="test_user"
        )

        # Test storing memory
        await agent.arun("Remember: Alice works at TechCorp as an AI researcher")

        # Test querying memory
        await agent.arun("Who is Alice and what does she do?")

    except Exception:
        traceback.print_exc()


async def test_react_memory_with_deepseek():
    """Test ReactMemoryAgent with DeepSeek."""
    aug_config = await test_deepseek_config()
    if not aug_config:
        return

    try:
        # First, let's try creating embeddings without OpenAI

        HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False},
        )

        # Now create ReactMemoryAgent with custom embeddings

        # We'll need to modify the agent to accept custom embeddings
        # For now, let's see if we can at least import it

    except Exception:
        traceback.print_exc()


async def test_models_only():
    """Test just the memory models without LLMs."""
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

    # Search memories
    results = state.search_memories("Bob")

    for _i, _result in enumerate(results):
        pass

    # Check stats


async def main():
    """Run all tests."""
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
        pass


if __name__ == "__main__":
    asyncio.run(main())
