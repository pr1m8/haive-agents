"""Comprehensive test suite for DocumentProcessingAgent.

This test suite validates the complete document processing pipeline with real components.
NO MOCKS - all tests use real LLMs, real tools, and real components.

Test Categories:
1. Basic agent creation and configuration
2. Document loading and processing
3. Search and retrieval capabilities
4. RAG processing with different strategies
5. End-to-end workflows
6. Error handling and edge cases

Author: Claude (Haive AI Agent Framework)
Version: 1.0.0
"""

import asyncio

import pytest

from haive.agents.document_processing import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
    DocumentProcessingResult,
    DocumentProcessingState,
)
from haive.core.engine.aug_llm import AugLLMConfig


class TestDocumentProcessingAgent:
    """Test suite for DocumentProcessingAgent with real components."""

    @pytest.fixture
    def basic_config(self) -> DocumentProcessingConfig:
        """Create basic configuration for testing."""
        return DocumentProcessingConfig(
            search_enabled=True,
            enable_bulk_processing=True,
            annotation_enabled=True,
            rag_strategy="basic",
            max_concurrent_loads=3,
            enable_caching=False,  # Disable caching for consistent tests
        )

    @pytest.fixture
    def advanced_config(self) -> DocumentProcessingConfig:
        """Create advanced configuration for testing."""
        return DocumentProcessingConfig(
            search_enabled=True,
            search_depth="advanced",
            enable_bulk_processing=True,
            annotation_enabled=True,
            summarization_enabled=True,
            kg_extraction_enabled=True,
            rag_strategy="adaptive",
            query_refinement=True,
            multi_query_enabled=True,
            structured_output=True,
            max_concurrent_loads=5,
            enable_caching=False,
        )

    @pytest.fixture
    def llm_config(self) -> AugLLMConfig:
        """Create LLM configuration for testing."""
        return AugLLMConfig(
            temperature=0.1, max_tokens=2000  # Low temperature for consistent tests
        )

    def test_agent_creation_basic(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test basic agent creation with real components."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="test_agent"
        )

        assert agent.name == "test_agent"
        assert agent.config.rag_strategy == "basic"
        assert agent.config.search_enabled is True
        assert agent.auto_loader is not None
        assert agent.search_agent is not None
        assert agent.rag_agent is not None

    def test_agent_creation_advanced(
        self, advanced_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test advanced agent creation with all features enabled."""
        agent = DocumentProcessingAgent(
            config=advanced_config, engine=llm_config, name="advanced_test_agent"
        )

        assert agent.name == "advanced_test_agent"
        assert agent.config.rag_strategy == "adaptive"
        assert agent.config.annotation_enabled is True
        assert agent.config.summarization_enabled is True
        assert agent.config.kg_extraction_enabled is True

    def test_agent_capabilities(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test agent capabilities reporting."""
        agent = DocumentProcessingAgent(config=basic_config, engine=llm_config)

        capabilities = agent.get_capabilities()

        assert "document_loading" in capabilities
        assert "search_capabilities" in capabilities
        assert "processing_pipeline" in capabilities
        assert "rag_capabilities" in capabilities
        assert "output_features" in capabilities

        # Check specific capabilities
        assert capabilities["document_loading"]["auto_loader"] is True
        assert capabilities["search_capabilities"]["web_search"] is True
        assert capabilities["rag_capabilities"]["strategy"] == "basic"

    @pytest.mark.asyncio
    async def test_simple_query_processing(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test simple query processing with real LLM."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="simple_test"
        )

        # Simple query that should work without external documents
        query = "What is artificial intelligence?"

        result = await agent.process_query(query)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert len(result.response) > 0
        assert result.query_info["original_query"] == query
        assert "total_time" in result.timing

    @pytest.mark.asyncio
    async def test_document_loading_with_sources(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test document loading with specific sources."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="doc_loading_test"
        )

        # Test with a simple text "document" (simulating a file)
        test_sources = [
            "This is a test document about machine learning algorithms.",
            "Another document discussing neural networks and deep learning.",
        ]

        query = "What are the main topics in these documents?"

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert len(result.sources) == len(test_sources)
        assert result.statistics["sources_used"] == len(test_sources)

    @pytest.mark.asyncio
    async def test_search_enabled_processing(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test processing with search enabled."""
        basic_config.search_enabled = True

        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="search_test"
        )

        # Query that should trigger search
        query = "Find information about Python programming best practices"

        result = await agent.process_query(query)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        # Should have attempted search even if no sources found
        assert result.metadata["config_used"]["search_enabled"] is True

    @pytest.mark.asyncio
    async def test_annotation_enabled_processing(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test processing with annotation enabled."""
        basic_config.annotation_enabled = True

        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="annotation_test"
        )

        test_sources = [
            "Machine learning is a subset of artificial intelligence that focuses on algorithms.",
            "Deep learning uses neural networks with multiple layers to learn complex patterns.",
        ]

        query = "Analyze the relationship between machine learning and deep learning"

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert result.metadata["config_used"]["annotation_enabled"] is True

    @pytest.mark.asyncio
    async def test_different_rag_strategies(self, llm_config: AugLLMConfig):
        """Test different RAG strategies."""
        strategies = ["basic", "adaptive"]  # Start with available strategies

        for strategy in strategies:
            config = DocumentProcessingConfig(
                rag_strategy=strategy,
                search_enabled=False,  # Disable search for consistent testing
                enable_bulk_processing=True,
                annotation_enabled=True,
            )

            agent = DocumentProcessingAgent(
                config=config, engine=llm_config, name=f"rag_test_{strategy}"
            )

            test_sources = [
                "Quantum computing uses quantum mechanical phenomena to process information.",
                "Classical computers use bits that are either 0 or 1, while quantum computers use qubits.",
            ]

            query = "How does quantum computing differ from classical computing?"

            result = await agent.process_query(query, sources=test_sources)

            assert isinstance(result, DocumentProcessingResult)
            assert result.response is not None
            assert result.metadata["config_used"]["rag_strategy"] == strategy

    @pytest.mark.asyncio
    async def test_bulk_processing_enabled(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test bulk processing with multiple sources."""
        basic_config.enable_bulk_processing = True
        basic_config.max_concurrent_loads = 3

        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="bulk_test"
        )

        # Multiple test sources
        test_sources = [
            "Document 1: Introduction to machine learning and its applications.",
            "Document 2: Deep learning architectures and neural networks.",
            "Document 3: Natural language processing and transformer models.",
            "Document 4: Computer vision techniques and convolutional networks.",
        ]

        query = "Provide an overview of AI technologies mentioned in these documents"

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert result.statistics["sources_used"] == len(test_sources)
        assert result.metadata["config_used"]["bulk_processing"] is True

    @pytest.mark.asyncio
    async def test_query_refinement_enabled(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test query refinement functionality."""
        basic_config.query_refinement = True

        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="refinement_test"
        )

        test_sources = [
            "Financial report Q1 2024: Revenue increased by 15% year-over-year.",
            "Q2 2024 earnings: Profit margins improved due to cost reduction initiatives.",
            "Q3 2024 analysis: Market expansion led to 20% growth in user base.",
        ]

        query = (
            "financial performance"  # Vague query that should benefit from refinement
        )

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert len(result.query_info.get("refined_queries", [])) > 0

    @pytest.mark.asyncio
    async def test_process_sources_method(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test the process_sources method specifically."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="sources_test"
        )

        test_sources = [
            "Research paper on climate change impacts on agriculture.",
            "Study on renewable energy adoption in developing countries.",
            "Analysis of carbon footprint reduction strategies.",
        ]

        query = "What are the main environmental themes in these documents?"

        result = await agent.process_sources(test_sources, query)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert result.statistics["sources_used"] == len(test_sources)

    @pytest.mark.asyncio
    async def test_error_handling_invalid_sources(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test error handling with invalid sources."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="error_test"
        )

        # Mix of valid and invalid sources
        test_sources = [
            "Valid document content about technology trends.",
            None,  # Invalid source
            "",  # Empty source
            "Another valid document about innovation.",
        ]

        query = "Analyze the technology trends"

        # Should handle errors gracefully
        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        # Should still process valid sources

    @pytest.mark.asyncio
    async def test_timing_and_statistics(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test timing and statistics collection."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="timing_test"
        )

        test_sources = [
            "Document about software engineering best practices.",
            "Guide to agile development methodologies.",
            "Overview of DevOps tools and processes.",
        ]

        query = "What are the key software development practices?"

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert "total_time" in result.timing
        assert result.timing["total_time"] > 0
        assert "documents_processed" in result.statistics
        assert "sources_used" in result.statistics
        assert result.statistics["sources_used"] == len(test_sources)

    @pytest.mark.asyncio
    async def test_metadata_generation(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test metadata generation and tracking."""
        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="metadata_test"
        )

        test_sources = [
            "Technical documentation about API design patterns.",
            "Best practices for database optimization.",
        ]

        query = "Summarize the technical information"

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert "config_used" in result.metadata
        assert "processing_stages" in result.metadata
        assert "operation_history" in result.metadata
        assert len(result.metadata["operation_history"]) > 0

    @pytest.mark.asyncio
    async def test_comprehensive_workflow(
        self, advanced_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test comprehensive workflow with all features enabled."""
        agent = DocumentProcessingAgent(
            config=advanced_config, engine=llm_config, name="comprehensive_test"
        )

        test_sources = [
            "Comprehensive analysis of artificial intelligence trends in healthcare.",
            "Machine learning applications in medical diagnosis and treatment.",
            "Deep learning for drug discovery and pharmaceutical research.",
            "Natural language processing in electronic health records.",
            "Computer vision for medical imaging and radiology.",
        ]

        query = "Analyze the current state of AI in healthcare and identify key applications"

        result = await agent.process_query(query, sources=test_sources)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert len(result.response) > 100  # Should be comprehensive
        assert result.statistics["sources_used"] == len(test_sources)
        assert result.metadata["config_used"]["rag_strategy"] == "adaptive"
        assert result.metadata["config_used"]["annotation_enabled"] is True

    def test_state_initialization(self):
        """Test DocumentProcessingState initialization."""
        state = DocumentProcessingState()

        assert state.processing_stage == "initialized"
        assert state.original_query == ""
        assert len(state.current_sources) == 0
        assert len(state.processed_documents) == 0
        assert len(state.operation_history) == 0

    def test_config_validation(self):
        """Test configuration validation."""
        # Test valid configuration
        config = DocumentProcessingConfig(
            rag_strategy="adaptive",
            search_depth="advanced",
            max_concurrent_loads=5,
            chunk_size=1000,
            chunk_overlap=200,
        )

        assert config.rag_strategy == "adaptive"
        assert config.search_depth == "advanced"
        assert config.max_concurrent_loads == 5

        # Test invalid configuration (should raise validation error)
        with pytest.raises(ValueError):
            DocumentProcessingConfig(max_concurrent_loads=0)  # Invalid: must be >= 1

    @pytest.mark.asyncio
    async def test_real_world_scenario(
        self, basic_config: DocumentProcessingConfig, llm_config: AugLLMConfig
    ):
        """Test a real-world scenario with multiple document types."""
        basic_config.annotation_enabled = True
        basic_config.structured_output = True

        agent = DocumentProcessingAgent(
            config=basic_config, engine=llm_config, name="real_world_test"
        )

        # Simulate different document types
        test_sources = [
            {
                "content": "Executive Summary: Q4 2024 revenue reached $2.5M with 18% growth.",
                "type": "financial_report",
            },
            {
                "content": "Product roadmap includes AI features, mobile app updates, and cloud migration.",
                "type": "product_plan",
            },
            {
                "content": "Customer satisfaction survey shows 85% positive feedback on new features.",
                "type": "customer_feedback",
            },
        ]

        # Convert to strings for processing
        source_strings = [f"{src['type']}: {src['content']}" for src in test_sources]

        query = "Create a comprehensive business analysis based on these documents"

        result = await agent.process_query(query, sources=source_strings)

        assert isinstance(result, DocumentProcessingResult)
        assert result.response is not None
        assert (
            "financial" in result.response.lower()
            or "business" in result.response.lower()
        )
        assert result.statistics["sources_used"] == len(source_strings)


# Integration test that can be run independently
async def test_integration_run():
    """Standalone integration test that can be run directly."""
    # Create basic configuration
    config = DocumentProcessingConfig(
        search_enabled=True,
        enable_bulk_processing=True,
        annotation_enabled=True,
        rag_strategy="basic",
        max_concurrent_loads=3,
        enable_caching=False,
    )

    # Create LLM configuration
    llm_config = AugLLMConfig(temperature=0.1, max_tokens=2000)

    # Create agent
    agent = DocumentProcessingAgent(
        config=config, engine=llm_config, name="integration_test"
    )

    # Test capabilities
    agent.get_capabilities()

    # Test simple query
    result = await agent.process_query("What is machine learning?")

    # Test with sources
    test_sources = [
        "Machine learning is a method of data analysis that automates analytical model building.",
        "Deep learning is a subset of machine learning that uses neural networks with multiple layers.",
        "Natural language processing enables computers to understand and process human language.",
    ]

    result = await agent.process_sources(test_sources, "Compare these AI technologies")

    return result


if __name__ == "__main__":
    # Run the integration test directly
    result = asyncio.run(test_integration_run())
