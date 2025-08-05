#!/usr/bin/env python3
"""Comprehensive test suite for DocumentProcessingAgent.

This test demonstrates all features of the document processing system
including query state management, document processing workflows, and
advanced configurations.
"""

import logging
from pathlib import Path
import sys


# Suppress all logging output
logging.getLogger().setLevel(logging.CRITICAL)

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage

from haive.agents.document_processing import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
    DocumentProcessingResult,
    DocumentProcessingState,
)
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.query_state import (
    QueryComplexity,
    QueryIntent,
    QueryMetrics,
    QueryProcessingConfig,
    QueryResult,
    QueryState,
    QueryType,
    RetrievalStrategy,
)


class DocumentProcessingTestSuite:
    """Comprehensive test suite for DocumentProcessingAgent."""

    def __init__(self):
        self.test_results = []
        self.passed_tests = 0
        self.failed_tests = 0

    def log_test(self, test_name: str, passed: bool, details: str = ""):
        """Log test results."""
        if details:
            pass

        self.test_results.append({"test": test_name, "passed": passed, "details": details})

        if passed:
            self.passed_tests += 1
        else:
            self.failed_tests += 1

    def test_basic_agent_creation(self):
        """Test basic agent creation with different configurations."""
        try:
            # Test default configuration
            agent1 = DocumentProcessingAgent()
            assert agent1.name == "document_processor"
            assert agent1.config.rag_strategy == "adaptive"

            # Test custom configuration
            custom_config = DocumentProcessingConfig(
                search_enabled=True,
                annotation_enabled=True,
                summarization_enabled=True,
                kg_extraction_enabled=True,
                bulk_processing=True,
                rag_strategy="basic",
                query_refinement=True,
                multi_query_enabled=True,
                max_concurrent_loads=5,
            )

            engine_config = AugLLMConfig(temperature=0.1, max_tokens=1000)
            agent2 = DocumentProcessingAgent(
                config=custom_config, engine=engine_config, name="custom_agent"
            )

            assert agent2.name == "custom_agent"
            assert agent2.config.rag_strategy == "basic"
            assert agent2.config.search_enabled
            assert agent2.config.annotation_enabled
            assert agent2.config.max_concurrent_loads == 5

            self.log_test(
                "Basic Agent Creation",
                True,
                "Default and custom configurations working",
            )

        except Exception as e:
            self.log_test("Basic Agent Creation", False, f"Error: {e}")

    def test_query_state_advanced_features(self):
        """Test advanced QueryState features."""
        try:
            # Create comprehensive query state
            query_state = QueryState(
                original_query="Analyze the impact of machine learning on healthcare",
                query_type=QueryType.ANALYTICAL,
                retrieval_strategy=RetrievalStrategy.HYBRID,
                query_complexity=QueryComplexity.EXPERT,
                query_intent=QueryIntent.LEARNING,
                query_expansion_enabled=True,
                query_refinement_enabled=True,
                multi_query_enabled=True,
                structured_query_enabled=True,
                time_weighted_retrieval=True,
                source_filters=["medical_journals", "research_papers"],
                metadata_filters={"domain": "healthcare", "topic": "machine_learning"},
                similarity_threshold=0.85,
                max_results=20,
            )

            # Test query management
            query_state.add_refined_query("ML applications in medical diagnosis")
            query_state.add_refined_query("Healthcare automation using machine learning")
            query_state.add_expanded_query("Deep learning in medical imaging")
            query_state.add_expanded_query("AI-powered drug discovery")
            query_state.add_query_variation("How is AI transforming healthcare?")

            # Test document management
            docs = [
                Document(
                    page_content="Machine learning is revolutionizing medical diagnosis by enabling more accurate pattern recognition in medical images.",
                    metadata={
                        "source": "medical_journal_1",
                        "domain": "healthcare",
                        "topic": "diagnosis",
                    },
                ),
                Document(
                    page_content="AI-powered drug discovery is accelerating the identification of new therapeutic compounds.",
                    metadata={
                        "source": "research_paper_1",
                        "domain": "healthcare",
                        "topic": "drug_discovery",
                    },
                ),
                Document(
                    page_content="Healthcare automation through ML is improving patient care efficiency and reducing costs.",
                    metadata={
                        "source": "medical_journal_2",
                        "domain": "healthcare",
                        "topic": "automation",
                    },
                ),
            ]

            for doc in docs:
                query_state.add_context_document(doc)
                query_state.add_retrieved_document(doc)

            # Test advanced methods
            all_queries = query_state.get_all_queries()
            assert len(all_queries) == 6  # original + 5 added

            all_docs = query_state.get_all_documents()
            assert len(all_docs) == 6  # 3 docs × 2 collections

            # Test multi-query workflow detection
            assert query_state.is_multi_query_workflow()
            assert query_state.requires_structured_output()

            # Test filters
            active_filters = query_state.get_active_filters()
            assert "sources" in active_filters
            assert "metadata" in active_filters
            assert "similarity_threshold" in active_filters

            # Test cache key generation
            cache_key = query_state.create_cache_key()
            assert len(cache_key) == 32  # MD5 hash

            # Test processing summary
            summary = query_state.get_processing_summary()
            assert summary["query_type"] == "analytical"
            assert summary["total_queries"] == 6
            assert summary["total_documents"] == 6

            self.log_test(
                "Advanced QueryState Features",
                True,
                "Multi-query, filters, caching all working",
            )

        except Exception as e:
            self.log_test("Advanced QueryState Features", False, f"Error: {e}")

    def test_document_processing_state_management(self):
        """Test DocumentProcessingState management."""
        try:
            # Create processing state
            state = DocumentProcessingState(
                messages=[HumanMessage(content="Process these documents about AI")],
                original_query="Process these documents about AI",
                processing_stage="initialized",
            )

            # Test document management
            sample_docs = [
                Document(
                    page_content="Artificial intelligence is transforming industries worldwide.",
                    metadata={"source": "tech_report_1", "category": "overview"},
                ),
                Document(
                    page_content="Machine learning algorithms are becoming more sophisticated.",
                    metadata={"source": "research_paper_2", "category": "technical"},
                ),
                Document(
                    page_content="Deep learning networks require substantial computational resources.",
                    metadata={
                        "source": "technical_guide_3",
                        "category": "implementation",
                    },
                ),
            ]

            # Add documents to different collections
            state.processed_documents.extend(sample_docs)
            state.context_documents.extend(sample_docs[:2])
            state.retrieval_results.extend(sample_docs)

            # Test search results
            state.search_results.append(
                {
                    "query": "AI transformation",
                    "results": ["result1", "result2"],
                    "metadata": {"search_time": 0.5},
                }
            )

            # Test annotation results
            state.annotation_results = {
                "summary": "Documents cover AI overview, technical aspects, and implementation",
                "key_topics": ["AI", "machine learning", "deep learning"],
                "relevance_scores": [0.9, 0.8, 0.7],
            }

            # Test operation history
            state.operation_history.extend(
                [
                    {
                        "operation": "search",
                        "timestamp": "2024-01-01T10:00:00",
                        "status": "success",
                    },
                    {
                        "operation": "load_documents",
                        "timestamp": "2024-01-01T10:01:00",
                        "status": "success",
                    },
                    {
                        "operation": "annotate",
                        "timestamp": "2024-01-01T10:02:00",
                        "status": "success",
                    },
                ]
            )

            # Test state progression
            stages = [
                "initialized",
                "searching",
                "loading",
                "processing",
                "annotating",
                "complete",
            ]
            for stage in stages:
                state.processing_stage = stage
                state.last_operation = f"completed_{stage}"

            # Verify state
            assert len(state.processed_documents) == 3
            assert len(state.context_documents) == 2
            assert len(state.retrieval_results) == 3
            assert len(state.search_results) == 1
            assert len(state.operation_history) == 3
            assert state.processing_stage == "complete"
            assert state.annotation_results["summary"] is not None

            self.log_test(
                "DocumentProcessingState Management",
                True,
                "State tracking and management working",
            )

        except Exception as e:
            self.log_test("DocumentProcessingState Management", False, f"Error: {e}")

    def test_agent_capabilities_and_configuration(self):
        """Test agent capabilities reporting and configuration options."""
        try:
            # Test different RAG strategies
            strategies = ["basic", "adaptive", "self_rag", "hyde", "multi_strategy"]
            for strategy in strategies:
                config = DocumentProcessingConfig(rag_strategy=strategy)
                agent = DocumentProcessingAgent(config=config)
                assert agent.config.rag_strategy == strategy

            # Test comprehensive configuration
            comprehensive_config = DocumentProcessingConfig(
                # Core Processing
                enable_bulk_processing=True,
                max_concurrent_loads=10,
                # Search & Retrieval
                search_enabled=True,
                search_depth="advanced",
                retrieval_strategy="ensemble",
                # Query Processing
                query_refinement=True,
                multi_query_enabled=True,
                query_expansion=True,
                # Document Processing
                annotation_enabled=True,
                summarization_enabled=True,
                kg_extraction_enabled=True,
                # RAG Configuration
                rag_strategy="adaptive",
                context_window_size=4000,
                chunk_size=1000,
                chunk_overlap=200,
                # Output
                structured_output=True,
                response_format="comprehensive",
                include_sources=True,
                include_metadata=True,
            )

            agent = DocumentProcessingAgent(config=comprehensive_config)
            capabilities = agent.get_capabilities()

            # Test capability structure
            required_sections = [
                "document_loading",
                "search_capabilities",
                "processing_pipeline",
                "rag_capabilities",
                "output_features",
            ]

            for section in required_sections:
                assert section in capabilities

            # Test specific capabilities
            assert capabilities["document_loading"]["bulk_processing"]
            assert capabilities["search_capabilities"]["web_search"]
            assert capabilities["processing_pipeline"]["annotation"]
            assert capabilities["processing_pipeline"]["summarization"]
            assert capabilities["processing_pipeline"]["kg_extraction"]
            assert capabilities["rag_capabilities"]["strategy"] == "adaptive"
            assert capabilities["output_features"]["structured_output"]

            self.log_test(
                "Agent Capabilities & Configuration",
                True,
                "All configuration options working",
            )

        except Exception as e:
            self.log_test("Agent Capabilities & Configuration", False, f"Error: {e}")

    def test_document_processing_result_structure(self):
        """Test DocumentProcessingResult structure and validation."""
        try:
            # Create comprehensive result
            sample_docs = [
                Document(
                    page_content="Sample document content 1",
                    metadata={"source": "doc1.pdf", "processed": True},
                ),
                Document(
                    page_content="Sample document content 2",
                    metadata={"source": "doc2.pdf", "processed": True},
                ),
            ]

            result = DocumentProcessingResult(
                response="This is a comprehensive analysis of the provided documents covering AI and machine learning topics.",
                sources=[
                    {"source": "doc1.pdf", "type": "file", "relevance": 0.9},
                    {"source": "doc2.pdf", "type": "file", "relevance": 0.8},
                    {
                        "source": "https://ai-research.com/article",
                        "type": "url",
                        "relevance": 0.7,
                    },
                ],
                metadata={
                    "processing_strategy": "adaptive",
                    "annotation_enabled": True,
                    "summarization_enabled": True,
                    "total_processing_time": 2.5,
                    "model_used": "gpt-4",
                    "confidence_score": 0.85,
                },
                documents=sample_docs,
                query_info={
                    "original_query": "Analyze AI research trends",
                    "refined_queries": [
                        "Machine learning advancements",
                        "AI applications in industry",
                        "Deep learning research trends",
                    ],
                    "query_type": "analytical",
                    "search_results_count": 15,
                },
                timing={
                    "total_time": 5.2,
                    "document_loading_time": 1.8,
                    "processing_time": 2.5,
                    "annotation_time": 0.7,
                    "response_generation_time": 0.2,
                },
                statistics={
                    "documents_processed": 8,
                    "sources_used": 3,
                    "context_documents": 5,
                    "total_tokens": 1500,
                    "average_relevance": 0.8,
                },
            )

            # Test result structure
            assert isinstance(result.response, str)
            assert len(result.response) > 0
            assert len(result.sources) == 3
            assert result.sources[0]["source"] == "doc1.pdf"
            assert result.sources[0]["type"] == "file"
            assert result.sources[0]["relevance"] == 0.9

            assert "processing_strategy" in result.metadata
            assert result.metadata["confidence_score"] == 0.85

            assert len(result.documents) == 2
            assert result.documents[0].page_content == "Sample document content 1"

            assert result.query_info["original_query"] == "Analyze AI research trends"
            assert len(result.query_info["refined_queries"]) == 3

            assert result.timing["total_time"] == 5.2
            assert result.timing["document_loading_time"] == 1.8

            assert result.statistics["documents_processed"] == 8
            assert result.statistics["sources_used"] == 3

            self.log_test(
                "DocumentProcessingResult Structure",
                True,
                "Result structure comprehensive and validated",
            )

        except Exception as e:
            self.log_test("DocumentProcessingResult Structure", False, f"Error: {e}")

    def test_query_processing_configurations(self):
        """Test different query processing configurations."""
        try:
            # Test basic configuration
            basic_config = QueryProcessingConfig(
                max_query_variations=3,
                enable_query_expansion=True,
                enable_query_refinement=True,
                max_context_documents=5,
                similarity_threshold=0.7,
            )

            # Test advanced configuration
            advanced_config = QueryProcessingConfig(
                max_query_variations=10,
                enable_query_expansion=True,
                enable_query_refinement=True,
                enable_context_compression=True,
                enable_result_reranking=True,
                enable_citation_tracking=True,
                enable_confidence_scoring=True,
                max_context_documents=25,
                context_window_size=8000,
                similarity_threshold=0.85,
                time_weight_decay=0.1,
                enable_caching=True,
                cache_ttl=7200,
            )

            # Test query metrics
            metrics = QueryMetrics(
                processing_time=2.5,
                retrieval_time=1.2,
                generation_time=0.8,
                total_documents_searched=50,
                relevant_documents_found=15,
                confidence_score=0.87,
                retrieval_accuracy=0.92,
                query_complexity_score=0.75,
                context_utilization=0.68,
                cache_hit_rate=0.45,
            )

            # Test query result
            query_result = QueryResult(
                query_id="query_123456",
                response="Detailed analysis of the query results",
                confidence=0.87,
                source_documents=[
                    Document(page_content="Source content 1", metadata={"source": "doc1"}),
                    Document(page_content="Source content 2", metadata={"source": "doc2"}),
                ],
                citations=[
                    {"source": "doc1", "page": 1, "relevance": 0.9},
                    {"source": "doc2", "page": 3, "relevance": 0.8},
                ],
                metadata={"processing_method": "advanced", "model": "gpt-4"},
                processing_metrics=metrics,
            )

            # Validate configurations
            assert basic_config.max_query_variations == 3
            assert basic_config.similarity_threshold == 0.7

            assert advanced_config.max_query_variations == 10
            assert advanced_config.enable_result_reranking
            assert advanced_config.context_window_size == 8000
            assert advanced_config.cache_ttl == 7200

            # Validate metrics
            assert metrics.processing_time == 2.5
            assert metrics.confidence_score == 0.87
            assert metrics.cache_hit_rate == 0.45

            # Validate result
            assert query_result.query_id == "query_123456"
            assert query_result.confidence == 0.87
            assert len(query_result.source_documents) == 2
            assert len(query_result.citations) == 2
            assert query_result.processing_metrics.processing_time == 2.5

            self.log_test(
                "Query Processing Configurations",
                True,
                "All configurations and metrics working",
            )

        except Exception as e:
            self.log_test("Query Processing Configurations", False, f"Error: {e}")

    def test_integration_workflows(self):
        """Test integration between different components."""
        try:
            # Create integrated workflow
            config = DocumentProcessingConfig(
                search_enabled=True,
                annotation_enabled=True,
                summarization_enabled=True,
                bulk_processing=True,
                rag_strategy="adaptive",
                structured_output=True,
            )

            agent = DocumentProcessingAgent(config=config, name="integration_test")

            # Create query state for integration
            query_state = QueryState(
                original_query="Comprehensive analysis of AI research",
                query_type=QueryType.RESEARCH,
                retrieval_strategy=RetrievalStrategy.ENSEMBLE,
                query_complexity=QueryComplexity.HIGH,
                query_intent=QueryIntent.ANALYTICAL,
                multi_query_enabled=True,
                structured_query_enabled=True,
                processing_config=QueryProcessingConfig(
                    max_query_variations=5,
                    enable_query_expansion=True,
                    enable_result_reranking=True,
                    max_context_documents=15,
                ),
            )

            # Add comprehensive queries
            research_queries = [
                "Latest machine learning breakthroughs",
                "AI applications in healthcare",
                "Deep learning architectural innovations",
                "Natural language processing advances",
                "Computer vision research trends",
            ]

            for query in research_queries:
                query_state.add_refined_query(query)

            # Create sample documents
            research_docs = [
                Document(
                    page_content="Recent advances in transformer architectures have revolutionized NLP tasks.",
                    metadata={
                        "source": "nlp_research_2024",
                        "topic": "transformers",
                        "year": 2024,
                    },
                ),
                Document(
                    page_content="Computer vision models are achieving human-level performance in image recognition.",
                    metadata={
                        "source": "cv_advances_2024",
                        "topic": "computer_vision",
                        "year": 2024,
                    },
                ),
                Document(
                    page_content="Healthcare AI applications are improving diagnostic accuracy significantly.",
                    metadata={
                        "source": "healthcare_ai_2024",
                        "topic": "healthcare",
                        "year": 2024,
                    },
                ),
            ]

            for doc in research_docs:
                query_state.add_context_document(doc)
                query_state.add_retrieved_document(doc)

            # Test integration points
            assert len(query_state.get_all_queries()) == 6  # original + 5 added
            assert len(query_state.get_all_documents()) == 6  # 3 docs × 2 collections
            assert query_state.is_multi_query_workflow()
            assert query_state.requires_structured_output()

            # Test agent capabilities match query requirements
            capabilities = agent.get_capabilities()
            assert capabilities["processing_pipeline"]["annotation"] == config.annotation_enabled
            assert (
                capabilities["processing_pipeline"]["summarization"] == config.summarization_enabled
            )
            assert capabilities["rag_capabilities"]["strategy"] == config.rag_strategy
            assert capabilities["output_features"]["structured_output"] == config.structured_output

            # Test state management integration
            processing_state = DocumentProcessingState(
                messages=[HumanMessage(content=query_state.original_query)],
                original_query=query_state.original_query,
                refined_queries=query_state.refined_queries,
                processed_documents=research_docs,
                context_documents=research_docs,
                processing_stage="integration_test",
            )

            assert processing_state.original_query == query_state.original_query
            assert len(processing_state.refined_queries) == len(query_state.refined_queries)
            assert len(processing_state.processed_documents) == 3
            assert len(processing_state.context_documents) == 3

            self.log_test("Integration Workflows", True, "All components integrate seamlessly")

        except Exception as e:
            self.log_test("Integration Workflows", False, f"Error: {e}")

    def run_all_tests(self):
        """Run all tests in the comprehensive suite."""
        # Run all tests
        self.test_basic_agent_creation()
        self.test_query_state_advanced_features()
        self.test_document_processing_state_management()
        self.test_agent_capabilities_and_configuration()
        self.test_document_processing_result_structure()
        self.test_query_processing_configurations()
        self.test_integration_workflows()

        # Print summary

        if self.failed_tests == 0:
            pass
        else:
            pass

        return self.failed_tests == 0


def main():
    """Run the comprehensive test suite."""
    test_suite = DocumentProcessingTestSuite()
    success = test_suite.run_all_tests()
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
