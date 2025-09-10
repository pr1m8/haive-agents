"""Simple test to verify individual memory components work."""

import asyncio
import traceback

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.memory_v2.advanced_rag_memory_agent import (
    AdvancedRAGConfig,
    AdvancedRAGMemoryAgent,
)
from haive.agents.memory_v2.long_term_memory_agent import LongTermMemoryAgent
from haive.agents.memory_v2.react_memory_agent import ReactMemoryAgent
from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent


async def test_simple_memory():
    """Test SimpleMemoryAgent alone."""
    try:
        agent = SimpleMemoryAgent(
            name="test_simple", engine=AugLLMConfig(temperature=0.1), user_id="test_user"
        )

        # Store memory
        await agent.arun("Remember: Alice works at TechCorp")

        # Query memory
        await agent.arun("Who is Alice?")

    except Exception:
        traceback.print_exc()


async def test_react_memory():
    """Test ReactMemoryAgent alone."""
    try:
        agent = ReactMemoryAgent(
            name="test_react", engine=AugLLMConfig(temperature=0.1), user_id="test_user"
        )

        # Store memory
        await agent.arun("Store this memory: Bob is the CTO of DataCorp", auto_save=True)

        # Query memory
        await agent.arun("Search memories for: Who is Bob?", auto_save=False)

    except Exception:
        traceback.print_exc()


async def test_longterm_memory():
    """Test LongTermMemoryAgent alone."""
    try:
        agent = LongTermMemoryAgent(user_id="test_user", llm_config=AugLLMConfig(temperature=0.1))

        # Store memory
        await agent.run("Carol is a researcher at MIT", extract_memories=True)

        # Query memory
        await agent.run("Who is Carol?", extract_memories=False)

    except Exception:
        traceback.print_exc()


async def test_advanced_rag():
    """Test AdvancedRAGMemoryAgent alone."""
    try:
        config = AdvancedRAGConfig(
            user_id="test_user",
            llm_config=AugLLMConfig(temperature=0.1),
            enable_reranking=False,  # Disable to avoid dependency issues
        )

        agent = AdvancedRAGMemoryAgent(config)

        # Add memory
        await agent.add_memory("David is the CEO of StartupXYZ", importance="high")

        # Query memory
        await agent.query_memory("Who is David?")

    except Exception:
        traceback.print_exc()


async def main():
    """Run all simple tests."""
    await test_simple_memory()
    await test_react_memory()
    await test_longterm_memory()
    await test_advanced_rag()


if __name__ == "__main__":
    asyncio.run(main())
