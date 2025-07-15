"""Enhanced Memory Retriever Demo - Phase 2 Implementation.

This example demonstrates the Enhanced Self-Query Memory Retriever that builds on
the memory classification system to provide intelligent, context-aware retrieval.

Key Features Demonstrated:
- Memory type classification and targeting
- Query intent analysis and expansion
- Multi-factor scoring (similarity + importance + recency + type)
- Metadata filtering and self-query capabilities
- Performance monitoring and optimization

This represents Phase 2 of our incremental memory system implementation.
"""

import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def demo_enhanced_memory_retriever():
    """Demonstrate the enhanced memory retriever with real components."""

    try:
        # Import our memory system components
        from haive.core.tools.store_tools import StoreManager

        from haive.agents.memory import (
            MemoryClassifier,
            MemoryClassifierConfig,
            MemoryStoreConfig,
            MemoryStoreManager,
            MemoryType,
            create_enhanced_memory_retriever,
        )

        print("🧠 Enhanced Memory Retriever Demo - Phase 2")
        print("=" * 50)

        # Phase 1: Setup Memory Infrastructure
        print("\n📋 Phase 1: Setting up memory infrastructure...")

        # Create store manager (using memory for demo)
        store_manager = StoreManager(
            store_type="memory", collection_name="enhanced_memory_demo"
        )

        # Create enhanced memory retriever
        print("🔧 Creating enhanced memory retriever...")
        retriever = await create_enhanced_memory_retriever(
            store_manager=store_manager,
            namespace=("demo", "enhanced_retrieval"),
            similarity_threshold=0.6,
            enable_query_expansion=True,
            enable_temporal_scoring=True,
        )

        print("✅ Enhanced memory retriever created successfully!")

        # Phase 2: Store Sample Memories
        print("\n📝 Phase 2: Storing sample memories...")

        sample_memories = [
            # Semantic memories (facts)
            "Python is a high-level programming language known for its simplicity and readability.",
            "Machine learning is a subset of artificial intelligence that focuses on algorithms.",
            "The capital of France is Paris, located in the north-central part of the country.",
            # Episodic memories (events)
            "Yesterday I had a great conversation with Sarah about machine learning applications.",
            "Last week I attended a Python conference and learned about new frameworks.",
            "This morning I completed a challenging coding interview focused on algorithms.",
            # Procedural memories (how-to)
            "To create a virtual environment in Python, use: python -m venv myenv",
            "The process for training a machine learning model involves data prep, model selection, and evaluation.",
            "To debug Python code effectively, use print statements, logging, and debugger tools.",
            # Preference memories (likes/patterns)
            "I prefer using VS Code for Python development because of its excellent extensions.",
            "I find that working in the morning is most productive for complex coding tasks.",
            "I like to take breaks every hour when coding to maintain focus and prevent fatigue.",
            # Error memories (lessons learned)
            "I made an error yesterday by not handling the KeyError exception in my dictionary access.",
            "Common mistake: forgetting to activate virtual environment before installing packages.",
            "Bug fix: The issue was caused by incorrect indentation in the Python function.",
        ]

        # Store memories through the retriever's store manager
        memory_ids = []
        for i, memory_content in enumerate(sample_memories):
            memory_id = await retriever.memory_store.store_memory(
                content=memory_content,
                user_context={"demo_session": "enhanced_retriever", "memory_index": i},
                conversation_context={"session_id": "demo_2024", "context": "learning"},
            )
            memory_ids.append(memory_id)
            print(f"  📌 Stored memory {i+1}: {memory_content[:50]}...")

        print(f"✅ Stored {len(sample_memories)} memories successfully!")

        # Phase 3: Demonstrate Enhanced Retrieval
        print("\n🔍 Phase 3: Demonstrating enhanced retrieval...")

        # Test queries with different intents and memory types
        test_queries = [
            (
                "What did I learn about Python?",
                "Mixed query - should find procedural and episodic",
            ),
            (
                "How do I create a virtual environment?",
                "Procedural query - should find how-to knowledge",
            ),
            (
                "What conversations did I have recently?",
                "Episodic query - should find events",
            ),
            (
                "What are my coding preferences?",
                "Preference query - should find user patterns",
            ),
            (
                "What programming mistakes should I avoid?",
                "Error query - should find lessons learned",
            ),
            (
                "Facts about machine learning",
                "Semantic query - should find factual knowledge",
            ),
        ]

        for query, description in test_queries:
            print(f"\n🔍 Query: '{query}'")
            print(f"   Expected: {description}")

            # Perform enhanced retrieval
            result = await retriever.retrieve_memories(
                query=query, limit=3, include_metadata=True
            )

            print(f"   📊 Results: {len(result.memories)} memories found")
            print(
                f"   🧠 Memory types targeted: {[mt.value for mt in result.memory_types_targeted]}"
            )
            print(f"   🔄 Query expansion: '{result.expanded_query}'")
            print(f"   ⏱️  Retrieval time: {result.total_time_ms:.1f}ms")

            # Show top results
            for i, memory in enumerate(result.memories[:2]):
                content = (
                    memory.get("content", "")[:80] + "..."
                    if len(memory.get("content", "")) > 80
                    else memory.get("content", "")
                )
                final_score = (
                    result.final_scores[i] if i < len(result.final_scores) else 0.0
                )
                memory_types = memory.get("metadata", {}).get("memory_types", [])

                print(f"     #{i+1}: {content}")
                print(f"           Score: {final_score:.3f}, Types: {memory_types}")

        # Phase 4: Performance Analysis
        print("\n📈 Phase 4: Performance analysis...")

        # Get retrieval statistics
        stats = retriever.get_performance_stats()
        print(f"   📊 Total queries processed: {stats['total_queries']}")
        print(f"   ⚡ Average retrieval time: {stats['avg_retrieval_time']:.1f}ms")
        print(f"   📋 Average results returned: {stats['avg_results_returned']:.1f}")

        # Show memory type distribution
        print("   🧠 Memory type usage distribution:")
        for memory_type, count in stats["memory_type_distribution"].items():
            if count > 0:
                print(f"      {memory_type}: {count} queries")

        # Get optimization recommendations
        optimization_info = await retriever.optimize_for_usage_patterns()
        print("\n🔧 Optimization recommendations:")
        for recommendation in optimization_info["recommendations"]:
            print(f"   💡 {recommendation}")

        print("\n✅ Enhanced Memory Retriever Demo completed successfully!")
        print("\n🎯 Key Achievements:")
        print("   ✅ Phase 1: Memory Type Classification system working")
        print("   ✅ Phase 2: Enhanced Self-Query with Memory Context implemented")
        print("   📋 Ready for Phase 3: Graph RAG implementation")

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print(
            "💡 Make sure you're running from the correct environment with all dependencies"
        )

    except Exception as e:
        logger.error(f"Demo error: {e}")
        print(f"❌ Demo failed: {e}")


if __name__ == "__main__":
    asyncio.run(demo_enhanced_memory_retriever())
