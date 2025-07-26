"""Test SimpleRAG V3 with a real example."""

import asyncio

from haive.core.engine.embedding.providers.HuggingFaceEmbeddingConfig import (
    HuggingFaceEmbeddingConfig,
)
from langchain_core.documents import Document

from haive.agents.rag.simple.enhanced_v3.agent import SimpleRAGV3


async def test_real_rag_example():
    """Test SimpleRAG V3 with real documents and queries."""
    print("\n=== SimpleRAG V3 Real Example Test ===\n")

    # 1. Create sample documents about AI topics
    documents = [
        Document(
            page_content="Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. It focuses on developing computer programs that can access data and use it to learn for themselves.",
            metadata={"source": "AI Basics Guide", "topic": "machine learning"},
        ),
        Document(
            page_content="Deep learning is a specialized form of machine learning that uses neural networks with multiple layers (deep neural networks) to progressively extract higher-level features from raw input. It has achieved remarkable success in image recognition, natural language processing, and speech recognition.",
            metadata={"source": "Deep Learning Handbook", "topic": "deep learning"},
        ),
        Document(
            page_content="Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and manipulate human language. NLP draws from many disciplines, including computer science and computational linguistics, to fill the gap between human communication and computer understanding.",
            metadata={"source": "NLP Fundamentals", "topic": "NLP"},
        ),
        Document(
            page_content="Reinforcement learning is an area of machine learning where an agent learns to make decisions by taking actions in an environment to maximize some notion of cumulative reward. Unlike supervised learning, reinforcement learning doesn't require labeled input/output pairs.",
            metadata={"source": "RL Theory", "topic": "reinforcement learning"},
        ),
        Document(
            page_content="Computer vision is a field of AI that trains computers to interpret and understand the visual world. Using digital images from cameras and videos and deep learning models, machines can accurately identify and classify objects and react to what they see.",
            metadata={"source": "Computer Vision Guide", "topic": "computer vision"},
        ),
    ]

    # 2. Create embedding configuration
    embedding_config = HuggingFaceEmbeddingConfig(
        model="sentence-transformers/all-MiniLM-L6-v2",
        use_cache=True,  # Cache embeddings for faster testing
    )

    # 3. Create SimpleRAG V3 from documents
    print("Creating SimpleRAG V3 from documents...")
    rag = SimpleRAGV3.from_documents(
        documents=documents,
        embedding_config=embedding_config,
        name="ai_knowledge_rag",
        top_k=3,  # Retrieve top 3 documents
        similarity_threshold=0.0,  # No threshold for this test
        include_citations=True,
        citation_style="footnote",
        debug_mode=True,  # Enable debug for visibility
        performance_mode=True,  # Track performance
    )

    print(f"✅ Created: {rag}")
    print(f"   - Agents: {[agent.name for agent in rag.agents]}")
    print(f"   - Execution mode: {rag.execution_mode}")

    # 4. Test queries
    test_queries = [
        "What is deep learning and how does it relate to machine learning?",
        "Explain reinforcement learning",
        "How does computer vision work?",
        "What are the applications of NLP?",
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*60}")
        print(f"Query {i}: {query}")
        print(f"{'='*60}\n")

        try:
            # Execute the RAG pipeline
            result = await rag.arun(query)

            # Handle different result formats
            if isinstance(result, dict):
                print(
                    f"Answer: {result.get('answer', result.get('content', str(result)))}"
                )
                if "sources" in result:
                    print("\nSources:")
                    for source in result["sources"]:
                        print(f"  - {source}")
                if "generation_time" in result:
                    print(f"\nGeneration time: {result['generation_time']:.3f}s")
            else:
                print(f"Answer: {result}")

        except Exception as e:
            print(f"Error: {e}")
            import traceback

            traceback.print_exc()

    # 5. Test the intermediate steps
    print(f"\n{'='*60}")
    print("Testing intermediate steps")
    print(f"{'='*60}\n")

    # Test retrieval directly
    print("1. Testing RetrieverAgent directly:")
    retriever = rag.get_retriever_agent()
    retrieval_result = await retriever.arun(
        {"query": "What is machine learning?", "k": 2}
    )
    print(f"   Retrieved {len(retrieval_result.get('documents', []))} documents")

    # Test answer generation with retrieved docs
    print("\n2. Testing SimpleAnswerAgent with retrieved documents:")
    answer_agent = rag.get_answer_agent()
    answer_result = await answer_agent.arun(
        {
            "query": "What is machine learning?",
            "documents": retrieval_result.get("documents", []),
        }
    )
    print(
        f"   Generated answer: {answer_result[:200]}..."
        if isinstance(answer_result, str)
        else f"   Result type: {type(answer_result)}"
    )

    # 6. Check performance metrics
    if rag.performance_mode:
        print(f"\n{'='*60}")
        print("Performance Analysis")
        print(f"{'='*60}\n")

        perf_analysis = rag.analyze_agent_performance()
        print(f"Performance tracking enabled: {perf_analysis.get('performance_mode')}")
        if "agents" in perf_analysis:
            for agent_name, metrics in perf_analysis["agents"].items():
                print(f"\n{agent_name}:")
                print(f"  - Success rate: {metrics.get('success_rate', 0):.1%}")
                print(f"  - Avg duration: {metrics.get('avg_duration', 0):.3f}s")
                print(f"  - Task count: {metrics.get('task_count', 0)}")


if __name__ == "__main__":
    asyncio.run(test_real_rag_example())
