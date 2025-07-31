"""Tests for SimpleRAGAgentV4 - Dead simple RAG pattern."""

from langchain_core.documents import Document
import pytest

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.rag.answer_agent import AnswerAgent
from haive.agents.rag.simple_rag_agent_v4 import SimpleRAGAgentV4
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore.vectorstore import (
    VectorStoreConfig,
    VectorStoreProvider,
)
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig


class TestSimpleRAGAgentV4:
    """Test the simple RAG pattern."""

    @pytest.fixture
    def sample_documents(self):
        """Create sample documents."""
        return [
            Document(
                page_content="Python is a high-level programming language.",
                metadata={"source": "python_intro.pdf"},
            ),
            Document(
                page_content="Python was created by Guido van Rossum in 1991.",
                metadata={"source": "python_history.pdf"},
            ),
        ]

    @pytest.fixture
    def vector_store_config(self, sample_documents):
        """Create vector store config."""
        return VectorStoreConfig(
            name="test_store",
            documents=sample_documents,
            vector_store_provider=VectorStoreProvider.FAISS,
            embedding_model=HuggingFaceEmbeddingConfig(
                model="sentence-transformers/all-MiniLM-L6-v2"
            ),
        )

    def test_answer_agent_creation(self):
        """Test AnswerAgent is just a SimpleAgent with prompt template."""
        agent = AnswerAgent(name="test_answer")

        assert agent.name == "test_answer"
        assert "Retrieved Documents:" in agent.prompt_template
        assert "Question:" in agent.prompt_template
        assert agent.system_message is not None

    def test_simple_rag_creation(self, vector_store_config):
        """Test SimpleRAGAgentV4 creates a MultiAgent."""
        llm_config = AugLLMConfig(temperature=0.1)

        rag = SimpleRAGAgentV4(
            name="test_rag",
            vector_store_config=vector_store_config,
            llm_config=llm_config,
        )

        # Should be a MultiAgent
        assert isinstance(rag, EnhancedMultiAgentV4)
        assert len(rag.agents) == 2
        assert rag.execution_mode == "sequential"

        # First agent should be retriever
        assert "retriever" in rag.agents[0].name

        # Second agent should be answerer
        assert "answerer" in rag.agents[1].name

    def test_answer_agent_with_custom_prompt(self):
        """Test AnswerAgent with custom prompt template."""
        custom_prompt = """Context:
{documents}

Query: {query}

Please provide a detailed technical answer."""

        agent = AnswerAgent(
            name="custom_answer", prompt_template=custom_prompt, temperature=0.2
        )

        assert agent.prompt_template == custom_prompt
        assert agent.temperature == 0.2
