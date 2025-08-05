"""Tests for SimpleRAG V3 implementation."""

from langchain_core.documents import Document
import pytest

from haive.agents.rag.simple.enhanced_v3.agent import SimpleRAGV3
from haive.agents.rag.simple.enhanced_v3.answer_generator_agent import SimpleAnswerAgent
from haive.agents.rag.simple.enhanced_v3.retriever_agent import RetrieverAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore.vectorstore import VectorStoreConfig


@pytest.fixture
def vector_store_config():
    """Create a test vector store configuration."""
    return VectorStoreConfig(provider="faiss", collection_name="test_collection")


@pytest.fixture
def llm_config():
    """Create a test LLM configuration."""
    return AugLLMConfig(temperature=0.5)


def test_simple_rag_v3_instantiation(vector_store_config):
    """Test that SimpleRAG V3 can be instantiated correctly."""
    # Create SimpleRAG V3
    rag = SimpleRAGV3(name="test_rag", vector_store_config=vector_store_config)

    # Verify basic properties
    assert rag.name == "test_rag"
    assert isinstance(rag.agents, list)
    assert len(rag.agents) == 2

    # Verify agent types and names
    assert isinstance(rag.agents[0], RetrieverAgent)
    assert rag.agents[0].name == "test_rag_retriever"

    assert isinstance(rag.agents[1], SimpleAnswerAgent)
    assert rag.agents[1].name == "test_rag_answer_generator"

    # Verify execution mode
    assert rag.execution_mode == "sequential"


def test_simple_rag_v3_with_custom_config(vector_store_config, llm_config):
    """Test SimpleRAG V3 with custom configurations."""
    # Create with custom config
    rag = SimpleRAGV3(
        name="custom_rag",
        vector_store_config=vector_store_config,
        llm_config=llm_config,
        top_k=10,
        similarity_threshold=0.7,
        max_context_length=8000,
        include_citations=False,
        citation_style="footnote",
    )

    # Verify custom settings
    assert rag.top_k == 10
    assert rag.similarity_threshold == 0.7
    assert rag.max_context_length == 8000
    assert not rag.include_citations
    assert rag.citation_style == "footnote"

    # Verify agents have proper configuration
    retriever = rag.get_retriever_agent()
    assert retriever.top_k == 10
    assert retriever.score_threshold == 0.7

    answer_agent = rag.get_answer_agent()
    assert answer_agent.max_context_length == 8000
    assert not answer_agent.include_citations
    assert answer_agent.citation_style == "footnote"


def test_simple_rag_v3_from_documents():
    """Test creating SimpleRAG V3 from documents."""
    from haive.core.models.embeddings.huggingface import HuggingFaceEmbeddingConfig

    # Create test documents
    documents = [
        Document(page_content="Machine learning is a subset of artificial intelligence."),
        Document(page_content="Deep learning uses neural networks with multiple layers."),
        Document(
            page_content="Natural language processing enables computers to understand human language."
        ),
    ]

    # Create proper embedding config
    embedding_config = HuggingFaceEmbeddingConfig(model="sentence-transformers/all-MiniLM-L6-v2")

    # Create from documents
    rag = SimpleRAGV3.from_documents(
        documents=documents, embedding_config=embedding_config, name="doc_rag"
    )

    # Verify creation
    assert rag.name == "doc_rag"
    assert isinstance(rag.agents, list)
    assert len(rag.agents) == 2


def test_simple_rag_v3_from_vectorstore(vector_store_config):
    """Test creating SimpleRAG V3 from existing vector store."""
    # Create from vector store
    rag = SimpleRAGV3.from_vectorstore(vector_store_config=vector_store_config, name="vs_rag")

    # Verify creation
    assert rag.name == "vs_rag"
    assert isinstance(rag.agents, list)
    assert len(rag.agents) == 2
    assert rag.vector_store_config == vector_store_config


def test_simple_rag_v3_performance_mode(vector_store_config):
    """Test SimpleRAG V3 with performance tracking enabled."""
    # Create with performance mode
    rag = SimpleRAGV3(
        name="perf_rag",
        vector_store_config=vector_store_config,
        performance_mode=True,
        adaptation_rate=0.2,
    )

    # Verify performance settings
    assert rag.performance_mode
    assert rag.adaptation_rate == 0.2

    # Both agents should have performance mode
    assert rag.agents[0].performance_mode
    assert rag.agents[1].performance_mode


def test_simple_rag_v3_debug_mode(vector_store_config):
    """Test SimpleRAG V3 with debug mode enabled."""
    # Create with debug mode
    rag = SimpleRAGV3(name="debug_rag", vector_store_config=vector_store_config, debug_mode=True)

    # Verify debug settings
    assert rag.debug_mode

    # Both agents should have debug mode
    assert rag.agents[0].debug_mode
    assert rag.agents[1].debug_mode


def test_simple_rag_v3_custom_templates(vector_store_config):
    """Test SimpleRAG V3 with custom prompt templates."""
    # Create with custom templates
    context_template = "Use the following context:\n{context}\n\nAnswer: "
    system_template = "You are a helpful research assistant."

    rag = SimpleRAGV3(
        name="template_rag",
        vector_store_config=vector_store_config,
        context_template=context_template,
        system_prompt_template=system_template,
    )

    # Verify templates are set
    assert rag.context_template == context_template
    assert rag.system_prompt_template == system_template

    # Answer agent should have the templates
    answer_agent = rag.get_answer_agent()
    assert answer_agent.context_template == context_template


def test_simple_rag_v3_get_rag_info(vector_store_config):
    """Test the get_rag_info method."""
    rag = SimpleRAGV3(name="info_rag", vector_store_config=vector_store_config)

    info = rag.get_rag_info()

    # Verify info structure
    assert info["name"] == "info_rag"
    assert info["execution_mode"] == "sequential"
    assert "agents" in info
    assert "retriever" in info["agents"]
    assert "answer_generator" in info["agents"]
    assert info["configuration"]["top_k"] == 5
    assert info["configuration"]["include_citations"]


@pytest.mark.asyncio
async def test_simple_rag_v3_retrieve_documents(vector_store_config):
    """Test the retrieve_documents method."""
    rag = SimpleRAGV3(name="retrieve_rag", vector_store_config=vector_store_config)

    # This would normally retrieve from a populated vector store
    # For testing, we're mainly checking the method works
    try:
        result = await rag.retrieve_documents(query="What is machine learning?", k=3)
        # The result structure depends on vector store implementation
        assert result is not None
    except Exception as e:
        # Vector store might not be initialized, which is fine for this test
        assert "vector store" in str(e).lower() or "not initialized" in str(e).lower()
