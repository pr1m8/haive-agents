"""Tests for DocumentGraderAgent - real component testing, no mocks."""

import pytest

from haive.agents.rag.agentic import DocumentGraderAgent
from haive.agents.rag.common.document_graders.models import DocumentBinaryResponse
from haive.core.engine.aug_llm import AugLLMConfig


class TestDocumentGraderAgent:
    """Test DocumentGraderAgent with real LLM calls."""

    @pytest.mark.asyncio
    async def test_document_grader_creation(self):
        """Test creating a document grader agent."""
        grader = DocumentGraderAgent.create_default(name="test_grader", temperature=0.0)

        assert grader.name == "test_grader"
        assert grader.structured_output_model == DocumentBinaryResponse
        assert isinstance(grader.engine, AugLLMConfig)
        assert grader.engine.temperature == 0.0

    @pytest.mark.asyncio
    async def test_grade_relevant_document(self):
        """Test grading a relevant document with real LLM."""
        grader = DocumentGraderAgent.create_default(temperature=0.0)

        # Create test input
        query = "What is machine learning?"
        documents = [
            {
                "id": "doc1",
                "content": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
            }
        ]

        # Grade documents
        result = await grader.grade_documents(query, documents)

        # Verify result structure
        assert isinstance(result, DocumentBinaryResponse)
        assert result.query == query
        assert len(result.document_decisions) == 1

        # Check the grading
        decision = result.document_decisions[0]
        assert decision.document_id == "doc1"
        assert decision.decision == "pass"  # Should be relevant
        assert decision.justification  # Should have reasoning
        assert 0.0 <= decision.confidence <= 1.0

    @pytest.mark.asyncio
    async def test_grade_irrelevant_document(self):
        """Test grading an irrelevant document with real LLM."""
        grader = DocumentGraderAgent.create_default(temperature=0.0)

        # Create test input with irrelevant document
        query = "What is quantum computing?"
        documents = [
            {
                "id": "doc2",
                "content": "The weather today is sunny with a chance of rain in the evening. Temperature will reach 75 degrees.",
            }
        ]

        # Grade documents
        result = await grader.grade_documents(query, documents)

        # Check the grading
        decision = result.document_decisions[0]
        assert decision.document_id == "doc2"
        assert decision.decision == "fail"  # Should be irrelevant
        assert decision.justification
        assert 0.0 <= decision.confidence <= 1.0

    @pytest.mark.asyncio
    async def test_grade_multiple_documents(self):
        """Test grading multiple documents with mixed relevance."""
        grader = DocumentGraderAgent.create_default(temperature=0.0)

        # Create test input with multiple documents
        query = "How does blockchain technology work?"
        documents = [
            {
                "id": "doc1",
                "content": "Blockchain is a distributed ledger technology that maintains a continuously growing list of records called blocks.",
            },
            {
                "id": "doc2",
                "content": "Pizza is a popular Italian dish consisting of a round, flat base of dough topped with cheese and tomatoes.",
            },
            {
                "id": "doc3",
                "content": "Each block in a blockchain contains a cryptographic hash of the previous block, creating an immutable chain.",
            },
        ]

        # Grade documents
        result = await grader.grade_documents(query, documents)

        # Verify we got results for all documents
        assert len(result.document_decisions) == 3

        # Check document IDs are preserved
        doc_ids = {d.document_id for d in result.document_decisions}
        assert doc_ids == {"doc1", "doc2", "doc3"}

        # Find decisions by ID
        decisions_by_id = {d.document_id: d for d in result.document_decisions}

        # Blockchain documents should be relevant
        assert decisions_by_id["doc1"].decision == "pass"
        assert decisions_by_id["doc3"].decision == "pass"

        # Pizza document should be irrelevant
        assert decisions_by_id["doc2"].decision == "fail"

    @pytest.mark.asyncio
    async def test_direct_agent_invocation(self):
        """Test invoking the agent directly with proper input format."""
        grader = DocumentGraderAgent.create_default(temperature=0.0)

        # Create input in the format the agent expects
        input_data = {
            "query": "What are the benefits of exercise?",
            "documents": [
                {
                    "id": "health1",
                    "content": "Regular exercise improves cardiovascular health, strengthens muscles, and boosts mental well-being.",
                },
                {
                    "id": "tech1",
                    "content": "Python is a high-level programming language known for its simplicity and readability.",
                },
            ],
        }

        # Run the agent
        result = await grader.arun(input_data)

        # Verify result
        assert isinstance(result, DocumentBinaryResponse)
        assert len(result.document_decisions) == 2

        # Exercise document should be relevant, Python should not
        decisions_by_id = {d.document_id: d for d in result.document_decisions}
        assert decisions_by_id["health1"].decision == "pass"
        assert decisions_by_id["tech1"].decision == "fail"

    @pytest.mark.asyncio
    async def test_custom_engine_configuration(self):
        """Test creating grader with custom engine configuration."""
        custom_engine = AugLLMConfig(
            temperature=0.5,
            max_tokens=500,
            system_message="You are a strict document relevance evaluator.",
        )

        grader = DocumentGraderAgent.create_default(name="custom_grader", engine=custom_engine)

        assert grader.engine == custom_engine
        assert grader.engine.temperature == 0.5
        assert grader.engine.max_tokens == 500

    @pytest.mark.asyncio
    async def test_empty_document_handling(self):
        """Test handling empty documents list."""
        grader = DocumentGraderAgent.create_default(temperature=0.0)

        # Test with empty documents
        result = await grader.grade_documents("test query", [])

        assert isinstance(result, DocumentBinaryResponse)
        assert len(result.document_decisions) == 0
        assert result.summary  # Should have some summary even with no docs
