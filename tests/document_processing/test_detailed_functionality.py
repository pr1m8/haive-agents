#!/usr/bin/env python3
"""Basic functionality test for DocumentProcessingAgent.

This test validates core functionality without external dependencies
like real LLM calls or external services.
"""

from pathlib import Path
import sys


# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_core.documents import Document

from haive.agents.document_processing import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
    DocumentProcessingResult,
)
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.query_state import (
    QueryComplexity,
    QueryIntent,
    QueryState,
    QueryType,
    RetrievalStrategy,
)


def test_basic_instantiation():
    """Test basic agent instantiation and configuration."""
    # Test with default config
    agent1 = DocumentProcessingAgent()
    assert agent1.name == "document_processor"
    assert agent1.config.rag_strategy == "adaptive"

    # Test with custom config
    custom_config = DocumentProcessingConfig(
        search_enabled=False, annotation_enabled=True, rag_strategy="basic"
    )

    engine_config = AugLLMConfig(temperature=0.1)
    agent2 = DocumentProcessingAgent(
        config=custom_config, engine=engine_config, name="custom_agent"
    )

    assert agent2.name == "custom_agent"
    assert agent2.config.rag_strategy == "basic"
    assert not agent2.config.search_enabled
    assert agent2.config.annotation_enabled


def test_query_state_functionality():
    """Test QueryState creation and methods."""
    # Basic query state
    query_state = QueryState(
        original_query="What is artificial intelligence?",
        query_type=QueryType.SIMPLE,
        retrieval_strategy=RetrievalStrategy.BASIC,
        query_complexity=QueryComplexity.LOW,
        query_intent=QueryIntent.INFORMATION_SEEKING,
    )

    assert query_state.original_query == "What is artificial intelligence?"
    assert query_state.query_type == QueryType.SIMPLE
    assert query_state.retrieval_strategy == RetrievalStrategy.BASIC

    # Test query management methods
    query_state.add_refined_query("AI definition and overview")
    query_state.add_expanded_query("Artificial intelligence concepts")
    query_state.add_query_variation("What does AI mean?")

    all_queries = query_state.get_all_queries()
    assert len(all_queries) == 4  # original + 3 added
    assert "AI definition and overview" in all_queries

    # Test document management
    doc1 = Document(
        page_content="AI is a branch of computer science", metadata={"source": "test"}
    )
    doc2 = Document(
        page_content="Machine learning is a subset of AI", metadata={"source": "test2"}
    )
    doc3 = Document(
        page_content="Deep learning is a subset of ML", metadata={"source": "test3"}
    )

    # Add documents to different collections
    query_state.add_context_document(doc1)
    query_state.add_retrieved_document(doc2)
    query_state.raw_documents.append(doc3)  # Add to raw_documents from DocumentState

    all_docs = query_state.get_all_documents()
    assert len(all_docs) == 3

    # Test processing summary
    summary = query_state.get_processing_summary()
    assert summary["original_query"] == "What is artificial intelligence?"
    assert summary["query_type"] == "simple"
    assert summary["total_queries"] == 4
    assert summary["total_documents"] == 3


def test_agent_capabilities():
    """Test agent capabilities reporting."""
    config = DocumentProcessingConfig(
        search_enabled=True,
        annotation_enabled=True,
        summarization_enabled=True,
        kg_extraction_enabled=True,
        rag_strategy="adaptive",
    )

    agent = DocumentProcessingAgent(config=config)
    capabilities = agent.get_capabilities()

    # Check capability structure
    assert "document_loading" in capabilities
    assert "search_capabilities" in capabilities
    assert "processing_pipeline" in capabilities
    assert "rag_capabilities" in capabilities
    assert "output_features" in capabilities

    # Check specific capabilities
    assert capabilities["document_loading"]["bulk_processing"]
    assert capabilities["search_capabilities"]["web_search"]
    assert capabilities["processing_pipeline"]["annotation"]
    assert capabilities["processing_pipeline"]["summarization"]
    assert capabilities["rag_capabilities"]["strategy"] == "adaptive"
    assert capabilities["output_features"]["structured_output"]


def test_state_management():
    """Test document processing state management."""
    from langchain_core.messages import HumanMessage

    from haive.agents.document_processing.agent import DocumentProcessingState

    # Create state
    state = DocumentProcessingState(
        messages=[HumanMessage(content="Test query")],
        original_query="Test query",
        processing_stage="initialized",
    )

    assert state.original_query == "Test query"
    assert state.processing_stage == "initialized"
    assert len(state.messages) == 1

    # Test document management
    doc = Document(page_content="Test content", metadata={"source": "test"})
    state.processed_documents.append(doc)

    assert len(state.processed_documents) == 1
    assert state.processed_documents[0].page_content == "Test content"

    # Test operation history
    state.operation_history.append(
        {"operation": "test_op", "timestamp": "2024-01-01", "result": "success"}
    )

    assert len(state.operation_history) == 1
    assert state.operation_history[0]["operation"] == "test_op"


def test_configuration_validation():
    """Test configuration validation and patterns."""
    # Test valid configurations
    valid_configs = [
        DocumentProcessingConfig(rag_strategy="basic"),
        DocumentProcessingConfig(rag_strategy="adaptive"),
        DocumentProcessingConfig(rag_strategy="self_rag"),
        DocumentProcessingConfig(search_depth="basic"),
        DocumentProcessingConfig(search_depth="advanced"),
        DocumentProcessingConfig(response_format="simple"),
        DocumentProcessingConfig(response_format="detailed"),
        DocumentProcessingConfig(response_format="comprehensive"),
    ]

    for config in valid_configs:
        agent = DocumentProcessingAgent(config=config)
        assert agent.config is not None

    # Test configuration field validation
    config = DocumentProcessingConfig(
        max_concurrent_loads=5,
        context_window_size=2000,
        chunk_size=500,
        chunk_overlap=50,
    )

    assert config.max_concurrent_loads == 5
    assert config.context_window_size == 2000
    assert config.chunk_size == 500
    assert config.chunk_overlap == 50


def test_source_processing_helpers():
    """Test source processing helper methods."""
    agent = DocumentProcessingAgent()

    # Test source extraction (basic functionality)
    from langchain_core.messages import HumanMessage

    from haive.agents.document_processing.agent import DocumentProcessingState

    state = DocumentProcessingState(
        messages=[HumanMessage(content="Test")],
        current_sources=["https://example.com", "/path/to/file.txt", "another_source"],
    )

    sources = agent._extract_sources(state)
    assert len(sources) == 3
    assert sources[0]["source"] == "https://example.com"
    assert sources[0]["type"] == "url"
    assert sources[1]["source"] == "/path/to/file.txt"
    assert sources[1]["type"] == "file"

    # Test metadata generation
    metadata = agent._generate_metadata(state)
    assert "config_used" in metadata
    assert "document_state" in metadata
    assert metadata["config_used"]["rag_strategy"] == "adaptive"
    assert metadata["config_used"]["search_enabled"]


def test_document_processing_result():
    """Test DocumentProcessingResult creation and validation."""
    # Create a sample result
    result = DocumentProcessingResult(
        response="Test response to the query",
        sources=[{"source": "test.pdf", "type": "file"}],
        metadata={"processing_time": 1.5, "model": "gpt-4"},
        documents=[Document(page_content="Test content", metadata={"source": "test"})],
        query_info={"original_query": "Test query", "refined_queries": []},
        timing={"total_time": 2.0, "processing_time": 1.5},
        statistics={"documents_processed": 1, "sources_used": 1},
    )

    assert result.response == "Test response to the query"
    assert len(result.sources) == 1
    assert result.sources[0]["source"] == "test.pdf"
    assert result.metadata["processing_time"] == 1.5
    assert len(result.documents) == 1
    assert result.documents[0].page_content == "Test content"
    assert result.query_info["original_query"] == "Test query"
    assert result.timing["total_time"] == 2.0
    assert result.statistics["documents_processed"] == 1


def test_comprehensive_workflow():
    """Test comprehensive workflow setup without external calls."""
    # Create comprehensive configuration
    config = DocumentProcessingConfig(
        search_enabled=True,
        annotation_enabled=True,
        summarization_enabled=True,
        kg_extraction_enabled=True,
        bulk_processing=True,
        rag_strategy="adaptive",
        query_refinement=True,
        multi_query_enabled=True,
        structured_output=True,
        max_concurrent_loads=10,
    )

    agent = DocumentProcessingAgent(config=config, name="comprehensive_agent")

    # Test all components are initialized
    assert agent.auto_loader is not None
    assert agent.search_agent is not None
    assert agent.rag_agent is not None
    assert agent.processing_agent is not None

    # Test configuration is applied
    assert agent.config.search_enabled
    assert agent.config.annotation_enabled
    assert agent.config.summarization_enabled
    assert agent.config.kg_extraction_enabled
    assert agent.config.rag_strategy == "adaptive"

    # Test query state integration
    query_state = QueryState(
        original_query="Comprehensive test query",
        query_type=QueryType.ANALYTICAL,
        retrieval_strategy=RetrievalStrategy.HYBRID,
        query_complexity=QueryComplexity.EXPERT,
        query_intent=QueryIntent.LEARNING,
        query_expansion_enabled=True,
        query_refinement_enabled=True,
        multi_query_enabled=True,
        structured_query_enabled=True,
    )

    assert query_state.is_multi_query_workflow()
    assert query_state.requires_structured_output()

    # Test cache key generation
    cache_key = query_state.create_cache_key()
    assert cache_key is not None
    assert len(cache_key) == 32  # MD5 hash length


def main():
    """Run all tests."""
    try:
        test_basic_instantiation()
        test_query_state_functionality()
        test_agent_capabilities()
        test_state_management()
        test_configuration_validation()
        test_source_processing_helpers()
        test_document_processing_result()
        test_comprehensive_workflow()

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
