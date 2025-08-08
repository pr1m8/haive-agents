"""Tests for Advanced RAG Memory Agent with real components.

Tests multi-stage retrieval, reranking, and advanced RAG capabilities.
"""

import asyncio
import shutil
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.memory_v2.advanced_rag_memory_agent import (
    AdvancedRAGConfig,
    AdvancedRAGMemoryAgent,
    QueryComplexity,
    RetrievalStrategy,
)


class TestAdvancedRAGMemoryAgent:
    """Test Advanced RAG Memory Agent functionality."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for memory stores."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def basic_config(self, temp_dir):
        """Create basic test configuration."""
        return AdvancedRAGConfig(
            user_id="test_user",
            memory_store_path=str(Path(temp_dir) / "memory_store"),
            llm_config=AugLLMConfig(temperature=0.1),
            strategy=RetrievalStrategy.ADAPTIVE,
            k_initial=10,
            k_final=3,
            enable_reranking=False,  # Disable for basic tests
            enable_bm25=True,
        )

    @pytest.fixture
    def advanced_config(self, temp_dir):
        """Create advanced test configuration."""
        return AdvancedRAGConfig(
            user_id="advanced_user",
            memory_store_path=str(Path(temp_dir) / "advanced_store"),
            llm_config=AugLLMConfig(temperature=0.1),
            strategy=RetrievalStrategy.RERANKED,
            k_initial=15,
            k_final=5,
            enable_reranking=True,
            enable_bm25=True,
            enable_query_expansion=True,
            include_citations=True,
            importance_boost=1.2,
        )

    @pytest.fixture
    async def basic_agent(self, basic_config):
        """Create basic Advanced RAG agent for testing."""
        agent = AdvancedRAGMemoryAgent(basic_config)
        return agent

    @pytest.fixture
    async def advanced_agent(self, advanced_config):
        """Create advanced RAG agent for testing."""
        agent = AdvancedRAGMemoryAgent(advanced_config)
        return agent

    @pytest.mark.asyncio
    async def test_agent_initialization(self, basic_agent):
        """Test proper agent initialization."""
        assert basic_agent.config.user_id == "test_user"
        assert basic_agent.vector_store is not None
        assert basic_agent.dense_retriever is not None
        assert len(basic_agent.documents) >= 1  # Initial document

    @pytest.mark.asyncio
    async def test_add_memory_basic(self, basic_agent):
        """Test adding memories to the system."""
        # Add a simple memory
        result = await basic_agent.add_memory(
            "Alice Johnson is a software engineer at TechCorp.", importance="normal"
        )

        assert result["stored"] is True
        assert "doc_id" in result
        assert result["total_documents"] >= 2  # Initial + new

        # Add an important memory
        result2 = await basic_agent.add_memory(
            "Critical: Alice has access to the production database passwords.",
            importance="critical",
        )

        assert result2["importance"] == "critical"
        assert result2["total_documents"] >= 3

    @pytest.mark.asyncio
    async def test_query_complexity_analysis(self, basic_agent):
        """Test query complexity analysis."""
        # Simple query
        simple_complexity = basic_agent.analyze_query_complexity("Who is Alice?")
        assert simple_complexity == QueryComplexity.SIMPLE

        # Medium complexity query
        medium_complexity = basic_agent.analyze_query_complexity(
            "What are Alice's roles and when did she join the company?"
        )
        assert medium_complexity in [QueryComplexity.MEDIUM, QueryComplexity.COMPLEX]

        # Complex query
        complex_complexity = basic_agent.analyze_query_complexity(
            "How does Alice's role relate to database security and what are the implications for our data governance policies?"
        )
        assert complex_complexity == QueryComplexity.COMPLEX

    @pytest.mark.asyncio
    async def test_retrieval_strategies(self, basic_agent):
        """Test different retrieval strategies."""
        # Add test memories
        memories = [
            "Bob Smith works as a data scientist at DataCorp.",
            "DataCorp specializes in machine learning solutions.",
            "Bob has 10 years of experience in Python and TensorFlow.",
            "He recently published a paper on neural networks.",
        ]

        for memory in memories:
            await basic_agent.add_memory(memory)

        # Test dense retrieval
        dense_docs = await basic_agent.retrieve_documents(
            "Who works at DataCorp?", strategy=RetrievalStrategy.DENSE_ONLY, k=3
        )
        assert len(dense_docs) <= 3
        assert any("DataCorp" in doc.page_content for doc in dense_docs)

        # Test hybrid retrieval (if BM25 available)
        if basic_agent.sparse_retriever:
            hybrid_docs = await basic_agent.retrieve_documents(
                "machine learning experience", strategy=RetrievalStrategy.HYBRID, k=3
            )
            assert len(hybrid_docs) <= 3

    @pytest.mark.asyncio
    async def test_memory_query_with_citations(self, basic_agent):
        """Test querying memory with citation generation."""
        # Add memories with metadata
        memories = [
            ("Sarah Lee is the CTO of InnovateTech.", {"source": "company_directory"}),
            (
                "InnovateTech develops AI-powered healthcare solutions.",
                {"source": "company_website"},
            ),
            (
                "Sarah has a PhD in Computer Science from MIT.",
                {"source": "linkedin_profile"},
            ),
        ]

        for content, metadata in memories:
            await basic_agent.add_memory(content, metadata=metadata, importance="high")

        # Query with citations
        result = await basic_agent.query_memory(
            "What do you know about Sarah Lee?", include_analysis=True
        )

        assert "answer" in result
        assert "analysis" in result
        assert result["analysis"]["complexity"] in ["simple", "medium"]
        assert result["retrieved_docs"] > 0

        # Check for relevant content
        answer_lower = result["answer"].lower()
        assert any(term in answer_lower for term in ["sarah", "cto", "innovatetech"])

    @pytest.mark.asyncio
    async def test_importance_boosting(self, basic_agent):
        """Test importance boosting in retrieval."""
        # Add memories with different importance levels
        await basic_agent.add_memory(
            "Low priority: Office coffee machine needs refilling.", importance="low"
        )

        await basic_agent.add_memory(
            "Critical security vulnerability found in authentication system.",
            importance="critical",
        )

        await basic_agent.add_memory(
            "Regular team meeting scheduled for next Tuesday.", importance="normal"
        )

        # Query should prioritize critical information
        result = await basic_agent.query_memory(
            "What important issues need attention?", include_analysis=True
        )

        assert (
            "critical" in result["answer"].lower()
            or "security" in result["answer"].lower()
        )

    @pytest.mark.asyncio
    async def test_time_weighted_retrieval(self, basic_agent):
        """Test time-weighted retrieval functionality."""
        # Add recent memory
        await basic_agent.add_memory(
            "Project Alpha launched successfully today.",
            metadata={"timestamp": datetime.now().isoformat()},
            importance="high",
        )

        # Add older memory
        old_time = datetime.now() - timedelta(days=30)
        await basic_agent.add_memory(
            "Project Beta was cancelled last month.",
            metadata={"timestamp": old_time.isoformat()},
            importance="normal",
        )

        # Enable time weighting and query
        basic_agent.config.enable_time_weighting = True
        basic_agent._init_retrievers()  # Reinitialize with time weighting

        result = await basic_agent.query_memory(
            "What are the latest project updates?",
            strategy=RetrievalStrategy.DENSE_ONLY,
        )

        # Recent project should be prioritized
        assert "alpha" in result["answer"].lower()

    @pytest.mark.asyncio
    async def test_advanced_features(self, advanced_agent):
        """Test advanced features like reranking and query expansion."""
        # Add technical memories
        technical_memories = [
            (
                "Graph Neural Networks use message passing for node representation learning.",
                "high",
            ),
            (
                "Attention mechanisms in transformers compute weighted averages of input sequences.",
                "high",
            ),
            ("BERT uses bidirectional attention for contextual embeddings.", "high"),
            (
                "GPT models employ causal attention masks for autoregressive generation.",
                "normal",
            ),
            (
                "Graph attention networks combine GNNs with attention mechanisms.",
                "critical",
            ),
        ]

        for content, importance in technical_memories:
            await advanced_agent.add_memory(content, importance=importance)

        # Complex technical query
        result = await advanced_agent.query_memory(
            "How do attention mechanisms work in graph neural networks and transformers?",
            include_analysis=True,
        )

        assert result["analysis"]["complexity"] == "complex"
        assert "attention" in result["answer"].lower()
        assert result["retrieved_docs"] > 0

        # Check citations if enabled
        if advanced_agent.config.include_citations and result["citations"]:
            assert len(result["citations"]) > 0

    @pytest.mark.asyncio
    async def test_memory_analytics(self, basic_agent):
        """Test memory analytics functionality."""
        # Add diverse memories
        memories = [
            ("Important client meeting tomorrow at 2 PM.", "high"),
            ("Coffee break discussion about new frameworks.", "low"),
            ("Critical bug in production needs immediate fix.", "critical"),
            ("Regular code review scheduled.", "normal"),
        ]

        for content, importance in memories:
            await basic_agent.add_memory(content, importance=importance)

        # Perform some queries
        await basic_agent.query_memory("What meetings are coming up?")
        await basic_agent.query_memory("Are there any critical issues?")

        # Get analytics
        analytics = await basic_agent.get_memory_analytics()

        assert "documents" in analytics
        assert "queries" in analytics
        assert analytics["documents"]["total_documents"] >= 4
        assert analytics["queries"]["total_queries"] >= 2
        assert "by_importance" in analytics["documents"]

        # Check importance distribution
        importance_dist = analytics["documents"]["by_importance"]
        assert "critical" in importance_dist
        assert "high" in importance_dist

    @pytest.mark.asyncio
    async def test_adaptive_strategy_selection(self, basic_agent):
        """Test adaptive strategy selection based on query type."""
        # Add test data
        await basic_agent.add_memory("John Doe is the CEO of Acme Corporation.")
        await basic_agent.add_memory("Acme Corporation was founded in 1995.")

        # Simple query should use simpler strategy
        simple_result = await basic_agent.query_memory(
            "Who is the CEO?", include_analysis=True
        )

        simple_strategy = simple_result["analysis"]["strategy_used"]
        assert simple_strategy in ["contextual", "hybrid", "dense_only"]

        # Complex query should use more advanced strategy
        complex_result = await basic_agent.query_memory(
            "What is the relationship between John Doe's role and the founding of Acme Corporation, and how might this impact the company's leadership structure?",
            include_analysis=True,
        )

        complex_strategy = complex_result["analysis"]["strategy_used"]
        # Complex queries should prefer more sophisticated strategies
        assert complex_strategy in ["reranked", "multi_query", "contextual"]

    @pytest.mark.asyncio
    async def test_memory_persistence(self, basic_agent, temp_dir):
        """Test memory store persistence."""
        # Add memories
        memories = [
            "Tesla Model 3 is an electric vehicle.",
            "Elon Musk is the CEO of Tesla.",
            "Tesla was founded in 2003.",
        ]

        for memory in memories:
            await basic_agent.add_memory(memory)

        # Save memory store
        save_path = str(Path(temp_dir) / "persistence_test")
        basic_agent.config.memory_store_path = save_path
        basic_agent.save_memory_store()

        # Create new agent with same config
        new_config = AdvancedRAGConfig(
            user_id="test_user",
            memory_store_path=save_path,
            llm_config=AugLLMConfig(temperature=0.1),
        )

        new_agent = AdvancedRAGMemoryAgent(new_config)

        # Query should find previous memories
        result = await new_agent.query_memory("Who is the CEO of Tesla?")
        assert "elon" in result["answer"].lower() or "musk" in result["answer"].lower()

    @pytest.mark.asyncio
    async def test_error_handling(self, basic_agent):
        """Test error handling in various scenarios."""
        # Test retrieval with invalid strategy
        docs = await basic_agent.retrieve_documents(
            "test query",
            strategy="invalid_strategy",  # Should fallback gracefully
        )
        assert len(docs) >= 0  # Should not crash

        # Test query with empty memory
        empty_agent = AdvancedRAGMemoryAgent(AdvancedRAGConfig())
        result = await empty_agent.query_memory("What do you know?")
        assert "answer" in result
        # Should handle gracefully even with minimal content


# Integration tests
@pytest.mark.asyncio
async def test_research_workflow():
    """Test complete research workflow with Advanced RAG."""
    config = AdvancedRAGConfig(
        user_id="researcher",
        strategy=RetrievalStrategy.ADAPTIVE,
        include_citations=True,
        enable_reranking=True,
    )

    agent = AdvancedRAGMemoryAgent(config)

    # Simulate research paper ingestion
    papers = [
        (
            "'Attention is All You Need' by Vaswani et al. introduced the Transformer architecture.",
            "critical",
        ),
        (
            "BERT uses bidirectional training to achieve state-of-the-art results on NLP tasks.",
            "high",
        ),
        (
            "GPT-3 demonstrates few-shot learning capabilities with 175 billion parameters.",
            "high",
        ),
        (
            "Vision Transformers apply transformer architecture to image classification.",
            "normal",
        ),
        (
            "The paper was published in NeurIPS 2017 and has over 50,000 citations.",
            "normal",
        ),
    ]

    for content, importance in papers:
        await agent.add_memory(content, importance=importance)

    # Research queries
    queries = [
        "What is the Transformer architecture?",
        "How does BERT differ from GPT models?",
        "What are the applications of transformers beyond NLP?",
    ]

    results = []
    for query in queries:
        result = await agent.query_memory(query, include_analysis=True)
        results.append(result)

        # Verify quality of responses
        assert len(result["answer"]) > 50  # Substantial answer
        assert result["retrieved_docs"] > 0
        assert "transformer" in result["answer"].lower()

    # Check analytics
    analytics = await agent.get_memory_analytics()
    assert analytics["documents"]["total_documents"] >= 5
    assert analytics["queries"]["total_queries"] >= 3


if __name__ == "__main__":
    # Run integration test
    asyncio.run(test_research_workflow())
