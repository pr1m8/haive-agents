"""Test SimpleRAG V3 with a real example."""

import asyncio

from langchain_core.documents import Document

from haive.agents.rag.simple.enhanced_v3.agent import SimpleRAGV3
from haive.core.engine.embedding.providers.HuggingFaceEmbeddingConfig import (
    HuggingFaceEmbeddingConfig,
)


async def test_real_rag_example():
    """Test SimpleRAG V3 with real documents and queries."""
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

    # 4. Test queries
    test_queries = [
        "What is deep learning and how does it relate to machine learning?",
        "Explain reinforcement learning",
        "How does computer vision work?",
        "What are the applications of NLP?",
    ]

    for _i, query in enumerate(test_queries, 1):
        try:
            # Execute the RAG pipeline
            result = await rag.arun(query)

            # Handle different result formats
            if isinstance(result, dict):
                if "sources" in result:
                    for _source in result["sources"]:
                        pass
                if "generation_time" in result:
                    pass
            else:
                pass

        except Exception:
            import traceback

            traceback.print_exc()

    # 5. Test the intermediate steps

    # Test retrieval directly
    retriever = rag.get_retriever_agent()
    retrieval_result = await retriever.arun({"query": "What is machine learning?", "k": 2})

    # Test answer generation with retrieved docs
    answer_agent = rag.get_answer_agent()
    await answer_agent.arun(
        {
            "query": "What is machine learning?",
            "documents": retrieval_result.get("documents", []),
        }
    )

    # 6. Check performance metrics
    if rag.performance_mode:
        perf_analysis = rag.analyze_agent_performance()
        if "agents" in perf_analysis:
            for _agent_name, _metrics in perf_analysis["agents"].items():
                pass


if __name__ == "__main__":
    asyncio.run(test_real_rag_example())
