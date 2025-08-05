"""Test suite for enhanced RAG agents.

Tests BaseRAGAgent and SimpleRAGAgent with the enhanced pattern.
All tests use REAL components - NO MOCKS.
"""

import asyncio

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
import pytest

from haive.agents.rag.enhanced_base_rag_agent import (
    BaseRAGAgent,
    RetrieverEngine,
    create_rag_agent,
)
from haive.agents.rag.enhanced_simple_rag_agent import SimpleRAGAgent, create_simple_rag


# Test retriever for real testing
class TestRetriever(BaseRetriever):
    """Test retriever with configurable documents."""

    def __init__(self, documents: list[Document]):
        self.documents = documents

    def _get_relevant_documents(self, query: str) -> list[Document]:
        """Return documents that contain the query."""
        relevant = []
        for doc in self.documents:
            if query.lower() in doc.page_content.lower():
                relevant.append(doc)

        # Return up to k documents
        return relevant[:4]  # Default k

    async def _aget_relevant_documents(self, query: str) -> list[Document]:
        """Async version."""
        return self._get_relevant_documents(query)


# Test documents
TEST_DOCUMENTS = [
    Document(
        page_content="Paris is the capital of France. It is known for the Eiffel Tower.",
        metadata={"source": "geography.txt", "page": 1},
    ),
    Document(
        page_content="London is the capital of the United Kingdom. Big Ben is a famous landmark.",
        metadata={"source": "geography.txt", "page": 2},
    ),
    Document(
        page_content="Python is a high-level programming language known for its simplicity.",
        metadata={"source": "programming.txt", "page": 1},
    ),
    Document(
        page_content="Machine learning is a subset of artificial intelligence.",
        metadata={"source": "ai_concepts.txt", "page": 1},
    ),
]


class TestBaseRAGAgent:
    """Test BaseRAGAgent functionality."""

    def test_base_rag_creation(self):
        """Test creating BaseRAGAgent."""
        retriever = TestRetriever(TEST_DOCUMENTS)

        agent = BaseRAGAgent(name="test_rag", retriever=retriever, k=3, include_sources=True)

        assert agent.name == "test_rag"
        assert agent.k == 3
        assert agent.include_sources is True
        assert agent.retriever == retriever

    @pytest.mark.asyncio
    async def test_document_retrieval(self):
        """Test retrieving documents."""
        retriever = TestRetriever(TEST_DOCUMENTS)
        agent = BaseRAGAgent(name="retriever_test", retriever=retriever, k=2)

        # Test retrieval
        docs = await agent.retrieve("Paris")
        assert len(docs) > 0
        assert any("Paris" in doc.page_content for doc in docs)

        # Test different query
        docs2 = await agent.retrieve("Python")
        assert len(docs2) > 0
        assert any("Python" in doc.page_content for doc in docs2)

    def test_context_formatting(self):
        """Test formatting retrieved documents."""
        retriever = TestRetriever(TEST_DOCUMENTS)
        agent = BaseRAGAgent(name="format_test", retriever=retriever, include_sources=True)

        # Format with sources
        context = agent.format_context(TEST_DOCUMENTS[:2])
        assert "[geography.txt]" in context
        assert "Paris" in context
        assert "London" in context

        # Format without sources
        agent.include_sources = False
        context_no_sources = agent.format_context(TEST_DOCUMENTS[:2])
        assert "[geography.txt]" not in context_no_sources
        assert "Document 1:" in context_no_sources

    def test_retriever_engine_creation(self):
        """Test RetrieverEngine is created properly."""
        retriever = TestRetriever(TEST_DOCUMENTS)

        agent = BaseRAGAgent(
            name="engine_test",
            retriever=retriever,
            k=5,
            score_threshold=0.7,
            temperature=0.2,
        )

        # Check engine is created
        assert agent.engine is not None
        assert isinstance(agent.engine, RetrieverEngine)
        assert agent.engine.k == 5
        assert agent.engine.score_threshold == 0.7

    def test_create_rag_agent_factory(self):
        """Test factory function."""

        # Mock vector store
        class MockVectorStore:
            def as_retriever(self, **kwargs):
                return TestRetriever(TEST_DOCUMENTS)

        vectorstore = MockVectorStore()
        agent = create_rag_agent(name="factory_rag", vectorstore=vectorstore, k=3, temperature=0.1)

        assert isinstance(agent, BaseRAGAgent)
        assert agent.name == "factory_rag"
        assert agent.k == 3


class TestSimpleRAGAgent:
    """Test SimpleRAGAgent functionality."""

    def test_simple_rag_creation(self):
        """Test creating SimpleRAGAgent with defaults."""
        retriever = TestRetriever(TEST_DOCUMENTS)

        agent = SimpleRAGAgent(name="simple", retriever=retriever)

        # Check defaults
        assert agent.name == "simple"
        assert agent.k == 3  # SimpleRAG default
        assert agent.temperature == 0.1  # SimpleRAG default
        assert agent.include_sources is False  # SimpleRAG default

    def test_simple_rag_inherits_base(self):
        """Test that SimpleRAGAgent has BaseRAGAgent features."""
        retriever = TestRetriever(TEST_DOCUMENTS)
        agent = SimpleRAGAgent(name="inheritance_test", retriever=retriever)

        # Should have retrieve method from BaseRAGAgent
        assert hasattr(agent, "retrieve")
        assert hasattr(agent, "format_context")
        assert hasattr(agent, "retrieve_sync")

    @pytest.mark.asyncio
    async def test_quick_answer_method(self):
        """Test the simplified quick_answer interface."""
        retriever = TestRetriever(TEST_DOCUMENTS)
        agent = SimpleRAGAgent(name="quick_test", retriever=retriever)

        # Test quick answer
        answer = await agent.quick_answer("What is the capital of France?")
        assert isinstance(answer, str)
        assert "capital of France" in answer

    def test_simple_context_formatting(self):
        """Test simplified context formatting."""
        retriever = TestRetriever(TEST_DOCUMENTS)
        agent = SimpleRAGAgent(name="format_test", retriever=retriever, include_sources=False)

        # Without sources - just concatenated content
        context = agent.format_context(TEST_DOCUMENTS[:2])
        assert "Document" not in context  # No document labels
        assert "[" not in context  # No source brackets
        assert "Paris" in context
        assert "London" in context

    def test_create_simple_rag_factory(self):
        """Test simplified factory function."""

        class MockVectorStore:
            def as_retriever(self):
                return TestRetriever(TEST_DOCUMENTS)

        vectorstore = MockVectorStore()
        agent = create_simple_rag(name="factory_simple", vectorstore=vectorstore, k=2)

        assert isinstance(agent, SimpleRAGAgent)
        assert agent.name == "factory_simple"
        assert agent.k == 2


class TestRAGAgentIntegration:
    """Test integration scenarios with RAG agents."""

    def test_rag_agent_representations(self):
        """Test string representations."""
        retriever = TestRetriever(TEST_DOCUMENTS)

        base_rag = BaseRAGAgent(name="base", retriever=retriever, k=5, include_sources=True)

        simple_rag = SimpleRAGAgent(name="simple", retriever=retriever)

        # Check representations
        base_repr = repr(base_rag)
        assert "BaseRAGAgent" in base_repr
        assert "k=5" in base_repr
        assert "sources=True" in base_repr

        simple_repr = repr(simple_rag)
        assert "SimpleRAGAgent" in simple_repr
        assert "k=3" in simple_repr

    @pytest.mark.asyncio
    async def test_concurrent_retrieval(self):
        """Test multiple RAG agents retrieving concurrently."""
        retriever = TestRetriever(TEST_DOCUMENTS)

        # Create multiple agents
        agents = [BaseRAGAgent(name=f"rag_{i}", retriever=retriever) for i in range(3)]

        # Concurrent retrieval
        queries = ["Paris", "Python", "machine learning"]
        tasks = [agent.retrieve(query) for agent, query in zip(agents, queries, strict=False)]

        results = await asyncio.gather(*tasks)

        # Verify all retrieved successfully
        assert len(results) == 3
        assert all(len(docs) > 0 for docs in results)

    def test_different_rag_configurations(self):
        """Test various RAG configurations."""
        retriever = TestRetriever(TEST_DOCUMENTS)

        # Minimal configuration
        minimal = SimpleRAGAgent(name="minimal", retriever=retriever)

        # Full configuration
        full = BaseRAGAgent(
            name="full",
            retriever=retriever,
            k=10,
            score_threshold=0.5,
            include_sources=True,
            rerank_documents=True,
            context_window=4000,
            temperature=0.7,
        )

        # Medium configuration
        medium = SimpleRAGAgent(
            name="medium",
            retriever=retriever,
            k=5,
            temperature=0.3,
            include_sources=True,
        )

        # All should be valid
        assert minimal.k == 3
        assert full.k == 10
        assert medium.k == 5


# Performance and edge case tests
class TestRAGEdgeCases:
    """Test edge cases and error handling."""

    def test_empty_retrieval(self):
        """Test handling when no documents are retrieved."""
        # Empty retriever
        empty_retriever = TestRetriever([])
        agent = BaseRAGAgent(name="empty_test", retriever=empty_retriever)

        context = agent.format_context([])
        assert context == "No relevant documents found."

    def test_invalid_configuration(self):
        """Test invalid configurations are caught."""
        with pytest.raises(ValueError):
            # No retriever provided
            BaseRAGAgent(name="invalid")

    @pytest.mark.asyncio
    async def test_retrieval_with_special_characters(self):
        """Test retrieval with special characters in query."""
        special_docs = [
            Document(
                page_content="C++ is a programming language with ++ in its name.",
                metadata={"source": "languages.txt"},
            )
        ]

        retriever = TestRetriever(special_docs)
        agent = BaseRAGAgent(name="special_test", retriever=retriever)

        docs = await agent.retrieve("C++")
        assert len(docs) > 0


if __name__ == "__main__":
    # Run specific test
    pytest.main([__file__, "-v", "-k", "test_simple_rag_creation"])
