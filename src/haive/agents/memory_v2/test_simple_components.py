"""Simple test to verify individual memory components work."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig


async def test_simple_memory():
    """Test SimpleMemoryAgent alone."""
    print("\n=== Testing SimpleMemoryAgent ===")

    try:
        from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent

        agent = SimpleMemoryAgent(
            name="test_simple",
            engine=AugLLMConfig(temperature=0.1),
            user_id="test_user",
        )

        # Store memory
        result = await agent.arun("Remember: Alice works at TechCorp")
        print(f"Stored: {len(result) > 0}")

        # Query memory
        query_result = await agent.arun("Who is Alice?")
        print(f"Retrieved: {'alice' in query_result.lower()}")
        print("✅ SimpleMemoryAgent works!")

    except Exception as e:
        print(f"❌ SimpleMemoryAgent failed: {e}")
        import traceback

        traceback.print_exc()


async def test_react_memory():
    """Test ReactMemoryAgent alone."""
    print("\n=== Testing ReactMemoryAgent ===")

    try:
        from haive.agents.memory_v2.react_memory_agent import ReactMemoryAgent

        agent = ReactMemoryAgent(
            name="test_react", engine=AugLLMConfig(temperature=0.1), user_id="test_user"
        )

        # Store memory
        result = await agent.arun(
            "Store this memory: Bob is the CTO of DataCorp", auto_save=True
        )
        print(f"Stored: {'successfully' in str(result).lower()}")

        # Query memory
        query_result = await agent.arun(
            "Search memories for: Who is Bob?", auto_save=False
        )
        print(f"Retrieved: {'bob' in str(query_result).lower()}")
        print("✅ ReactMemoryAgent works!")

    except Exception as e:
        print(f"❌ ReactMemoryAgent failed: {e}")
        import traceback

        traceback.print_exc()


async def test_longterm_memory():
    """Test LongTermMemoryAgent alone."""
    print("\n=== Testing LongTermMemoryAgent ===")

    try:
        from haive.agents.memory_v2.long_term_memory_agent import LongTermMemoryAgent

        agent = LongTermMemoryAgent(
            user_id="test_user", llm_config=AugLLMConfig(temperature=0.1)
        )

        # Store memory
        result = await agent.run("Carol is a researcher at MIT", extract_memories=True)
        print(f"Stored: {result.get('status') == 'success'}")

        # Query memory
        query_result = await agent.run("Who is Carol?", extract_memories=False)
        print(f"Retrieved: {'carol' in str(query_result).lower()}")
        print("✅ LongTermMemoryAgent works!")

    except Exception as e:
        print(f"❌ LongTermMemoryAgent failed: {e}")
        import traceback

        traceback.print_exc()


async def test_advanced_rag():
    """Test AdvancedRAGMemoryAgent alone."""
    print("\n=== Testing AdvancedRAGMemoryAgent ===")

    try:
        from haive.agents.memory_v2.advanced_rag_memory_agent import (
            AdvancedRAGConfig,
            AdvancedRAGMemoryAgent,
        )

        config = AdvancedRAGConfig(
            user_id="test_user",
            llm_config=AugLLMConfig(temperature=0.1),
            enable_reranking=False,  # Disable to avoid dependency issues
        )

        agent = AdvancedRAGMemoryAgent(config)

        # Add memory
        result = await agent.add_memory(
            "David is the CEO of StartupXYZ", importance="high"
        )
        print(f"Stored: {result['stored']}")

        # Query memory
        query_result = await agent.query_memory("Who is David?")
        print(f"Retrieved: {'david' in query_result['answer'].lower()}")
        print("✅ AdvancedRAGMemoryAgent works!")

    except Exception as e:
        print(f"❌ AdvancedRAGMemoryAgent failed: {e}")
        import traceback

        traceback.print_exc()


async def main():
    """Run all simple tests."""
    print("\n🚀 Testing Individual Memory Components 🚀")
    print("=" * 50)

    await test_simple_memory()
    await test_react_memory()
    await test_longterm_memory()
    await test_advanced_rag()

    print("\n" + "=" * 50)
    print("✨ Simple component tests completed! ✨")


if __name__ == "__main__":
    asyncio.run(main())
