"""Tests for CollectiveRAGAgentV4 - Multi-source RAG orchestration."""

from langchain_core.documents import Document
import pytest

from haive.agents.rag.collective_rag_agent_v4 import (
    CollectiveAnswer,
    CollectiveRAGAgentV4,
)
from haive.agents.rag.simple_rag_agent_v4 import SimpleRAGAgentV4
from haive.core.engine.aug_llm import AugLLMConfig


class MockVectorStoreConfig:
    """Mock vector store for testing."""
    def __init__(self, name: str, documents: list[Document]):
        self.name = name
        self.documents = documents

    def as_retriever(self, k=4):
        """Mock retriever that returns preset documents."""
        class MockRetriever:
            def __init__(self, docs):
                self.docs = docs

            def invoke(self, query, config=None):
                # Return documents as mock retrieval
                return {"documents": self.docs[:k]}

        return MockRetriever(self.documents)


class TestCollectiveRAGAgentV4:
    """Test CollectiveRAGAgentV4 basic functionality."""
    @pytest.fixture
    def tech_documents(self):
        """Technical domain documents."""
        return [
            Document(
                page_content="Machine learning uses neural networks for pattern recognition.",
                metadata={"source": "ml_basics.pdf", "domain": "tech"},
            ),
            Document(
                page_content="Deep learning is a subset of machine learning with multiple layers.",
                metadata={"source": "dl_intro.pdf", "domain": "tech"},
            ),
        ]

    @pytest.fixture
    def business_documents(self):
        """Business domain documents."""
        return [
            Document(
                page_content="AI adoption drives 30% efficiency gains in enterprise operations.",
                metadata={"source": "ai_business.pdf", "domain": "business"},
            ),
            Document(
                page_content="ROI on AI investments typically realized within 18-24 months.",
                metadata={"source": "ai_roi.pdf", "domain": "business"},
            ),
        ]

    @pytest.fixture
    def rag_agents(self, tech_documents, business_documents):
        """Create mock RAG agents for different domains."""
        tech_rag = SimpleRAGAgentV4(
            name="tech_rag",
            vector_store_config=MockVectorStoreConfig("tech", tech_documents),
            k=2,
        )

        business_rag = SimpleRAGAgentV4(
            name="business_rag",
            vector_store_config=MockVectorStoreConfig("business", business_documents),
            k=2,
        )

        return [tech_rag, business_rag]

    def test_basic_creation(self, rag_agents):
        """Test basic collective RAG creation."""
        collective = CollectiveRAGAgentV4(
            name="test_collective", rag_agents=rag_agents, aggregation_mode="synthesis"
        )

        assert collective.name == "test_collective"
        assert len(collective.rag_agents) == 2
        assert collective.aggregation_mode == "synthesis"
        assert collective.parallel_execution is True  # Default
        assert collective.structured_output_model == CollectiveAnswer

    def test_aggregation_modes(self, rag_agents):
        """Test different aggregation modes."""
        modes = ["synthesis", "best_match", "voting", "hierarchical"]

        for mode in modes:
            collective = CollectiveRAGAgentV4(
                name=f"collective_{mode}", rag_agents=rag_agents, aggregation_mode=mode
            )
            assert collective.aggregation_mode == mode

    def test_conflict_resolution_modes(self, rag_agents):
        """Test different conflict resolution strategies."""
        strategies = ["all", "consensus", "authoritative", "recent"]

        for strategy in strategies:
            collective = CollectiveRAGAgentV4(
                name=f"collective_{strategy}",
                rag_agents=rag_agents,
                conflict_resolution=strategy,
            )
            assert collective.conflict_resolution == strategy

    def test_source_weights_configuration(self, rag_agents):
        """Test hierarchical mode with source weights."""
        weights = {"tech_rag": 2.0, "business_rag": 1.5}

        collective = CollectiveRAGAgentV4(
            name="weighted_collective",
            rag_agents=rag_agents,
            aggregation_mode="hierarchical",
            source_weights=weights,
        )

        assert collective.source_weights == weights
        assert collective.aggregation_mode == "hierarchical"

    def test_parallel_vs_sequential(self, rag_agents):
        """Test parallel and sequential execution modes."""
        # Parallel execution
        parallel = CollectiveRAGAgentV4(
            name="parallel_collective", rag_agents=rag_agents, parallel_execution=True
        )
        assert parallel.parallel_execution is True

        # Sequential execution
        sequential = CollectiveRAGAgentV4(
            name="sequential_collective",
            rag_agents=rag_agents,
            parallel_execution=False,
        )
        assert sequential.parallel_execution is False

    def test_custom_synthesis_llm(self, rag_agents):
        """Test custom LLM configuration for synthesis."""
        custom_llm = AugLLMConfig(
            temperature=0.2,
            max_tokens=1000,
            system_message="You are an expert synthesizer.",
        )

        collective = CollectiveRAGAgentV4(
            name="custom_synthesis",
            rag_agents=rag_agents,
            synthesis_llm_config=custom_llm,
        )

        assert collective.synthesis_llm_config == custom_llm
        assert collective.synthesis_llm_config.temperature == 0.2

    def test_min_sources_validation(self, rag_agents):
        """Test minimum sources configuration."""
        collective = CollectiveRAGAgentV4(
            name="min_sources_test", rag_agents=rag_agents, min_sources=2
        )

        assert collective.min_sources == 2

        # Test with single agent should still work
        single_collective = CollectiveRAGAgentV4(
            name="single_source", rag_agents=[rag_agents[0]], min_sources=1
        )
        assert single_collective.min_sources == 1

    def test_deduplication_threshold(self, rag_agents):
        """Test document deduplication configuration."""
        collective = CollectiveRAGAgentV4(
            name="dedup_test", rag_agents=rag_agents, deduplication_threshold=0.9
        )

        assert collective.deduplication_threshold == 0.9

    def test_build_parallel_graph(self, rag_agents):
        """Test parallel graph building."""
        collective = CollectiveRAGAgentV4(
            name="parallel_graph_test", rag_agents=rag_agents, parallel_execution=True
        )

        # Build graph - this creates EnhancedMultiAgentV4 internally
        graph = collective.build_graph()

        assert graph is not None
        # The graph should contain all RAG agents plus aggregator
        # Exact structure depends on EnhancedMultiAgentV4 implementation

    def test_build_sequential_graph(self, rag_agents):
        """Test sequential graph building."""
        collective = CollectiveRAGAgentV4(
            name="sequential_graph_test",
            rag_agents=rag_agents,
            parallel_execution=False,
        )

        graph = collective.build_graph()
        assert graph is not None

    def test_document_deduplication(self, rag_agents):
        """Test document deduplication logic."""
        collective = CollectiveRAGAgentV4(name="dedup_logic_test", rag_agents=rag_agents)

        # Test deduplication with similar documents
        docs = [
            {"content": "This is a test document about AI."},
            {"content": "This is a test document about AI."},  # Duplicate
            {"content": "This is different content about ML."},
        ]

        unique_docs = collective.deduplicate_documents(docs)
        assert len(unique_docs) == 2  # Should remove duplicate

    def test_aggregator_prompt_generation(self, rag_agents):
        """Test aggregator prompt generation for different modes."""
        collective = CollectiveRAGAgentV4(
            name="prompt_test",
            rag_agents=rag_agents,
            aggregation_mode="synthesis",
            conflict_resolution="consensus",
        )

        prompt = collective._get_aggregator_prompt()

        assert "synthesizing information from multiple knowledge sources" in prompt
        assert "2 different RAG systems" in prompt  # Based on rag_agents length
        assert "consensus" in prompt.lower()

    def test_invalid_rag_agent_type(self):
        """Test validation of RAG agent types."""
        # Create a non-RAG agent
        class NotRAGAgent:
            def __init__(self):
                self.name = "not_rag"

        with pytest.raises(ValueError, match="must be SimpleRAGAgentV4"):
            CollectiveRAGAgentV4(name="invalid_test", rag_agents=[NotRAGAgent()])


class TestCollectiveRAGAgentV4Factory:
    """Test factory methods for creating collective RAG agents."""
    def test_from_vector_stores(self):
        """Test creation from vector store configurations."""
        configs = [
            {"name": "knowledge_base_1", "config": MockVectorStoreConfig("kb1", [])},
            {"name": "knowledge_base_2", "config": MockVectorStoreConfig("kb2", [])},
        ]

        collective = CollectiveRAGAgentV4.from_vector_stores(
            configs, name="multi_kb_rag", aggregation_mode="voting"
        )

        assert collective.name == "multi_kb_rag"
        assert len(collective.rag_agents) == 2
        assert collective.aggregation_mode == "voting"

    def test_from_domains(self):
        """Test creation with domain-specific configurations."""
        domains = {
            "technical": {
                "vector_store": MockVectorStoreConfig("tech", []),
                "system_message": "Focus on technical details",
                "weight": 2.0,
                "k": 5,
            },
            "business": {
                "vector_store": MockVectorStoreConfig("biz", []),
                "system_message": "Focus on business value",
                "weight": 1.5,
                "k": 3,
            },
        }

        collective = CollectiveRAGAgentV4.from_domains(
            domains, name="domain_collective", aggregation_mode="hierarchical"
        )

        assert collective.name == "domain_collective"
        assert len(collective.rag_agents) == 2
        assert collective.source_weights is not None
        assert collective.source_weights["technical_rag"] == 2.0
        assert collective.source_weights["business_rag"] == 1.5

        # Check individual RAG agent configurations
        tech_agent = next(a for a in collective.rag_agents if a.name == "technical_rag")
        assert tech_agent.k == 5
        assert tech_agent.system_message == "Focus on technical details"

        biz_agent = next(a for a in collective.rag_agents if a.name == "business_rag")
        assert biz_agent.k == 3
        assert biz_agent.system_message == "Focus on business value"


class TestCollectiveRAGAgentV4Integration:
    """Integration tests for multi-source RAG orchestration."""
    @pytest.fixture
    def multi_domain_setup(self):
        """Create multi-domain RAG setup."""
        # Tech domain
        tech_docs = [
            Document(
                page_content="Quantum computing uses qubits for parallel computation.",
                metadata={"source": "quantum.pdf", "year": 2024},
            ),
            Document(
                page_content="Quantum algorithms provide exponential speedup for certain problems.",
                metadata={"source": "algorithms.pdf", "year": 2023},
            ),
        ]

        # Science domain
        science_docs = [
            Document(
                page_content="Quantum mechanics describes behavior at atomic scales.",
                metadata={"source": "physics.pdf", "year": 2022},
            ),
            Document(
                page_content="Superposition allows quantum states to exist simultaneously.",
                metadata={"source": "quantum_physics.pdf", "year": 2024},
            ),
        ]

        # Business domain
        business_docs = [
            Document(
                page_content="Quantum computing market expected to reach $65B by 2030.",
                metadata={"source": "market_report.pdf", "year": 2024},
            ),
            Document(
                page_content="Early quantum adopters gain competitive advantage.",
                metadata={"source": "strategy.pdf", "year": 2023},
            ),
        ]

        return {
            "tech": MockVectorStoreConfig("tech", tech_docs),
            "science": MockVectorStoreConfig("science", science_docs),
            "business": MockVectorStoreConfig("business", business_docs),
        }

    def test_multi_domain_collective(self, multi_domain_setup):
        """Test collective RAG across multiple domains."""
        # Create RAG agents for each domain
        rag_agents = []
        for domain, config in multi_domain_setup.items():
            agent = SimpleRAGAgentV4(
                name=f"{domain}_expert",
                vector_store_config=config,
                k=2,
                system_message=f"You are a {domain} expert.",
            )
            rag_agents.append(agent)

        # Create collective with synthesis
        collective = CollectiveRAGAgentV4(
            name="quantum_collective",
            rag_agents=rag_agents,
            aggregation_mode="synthesis",
            conflict_resolution="all",
            min_sources=2,
        )

        assert len(collective.rag_agents) == 3
        assert collective.aggregation_mode == "synthesis"

        # Build workflow
        graph = collective.build_graph()
        assert graph is not None

    @pytest.mark.asyncio
    async def test_collective_workflow_structure(self, multi_domain_setup):
        """Test the complete collective workflow structure."""
        # Create domain collective
        collective = CollectiveRAGAgentV4.from_domains(
            {
                "technical": {
                    "vector_store": multi_domain_setup["tech"],
                    "weight": 2.0,
                },
                "scientific": {
                    "vector_store": multi_domain_setup["science"],
                    "weight": 1.5,
                },
                "business": {
                    "vector_store": multi_domain_setup["business"],
                    "weight": 1.0,
                },
            },
            aggregation_mode="hierarchical",
            parallel_execution=True,
        )

        # Build and verify workflow
        collective.build_graph()

        # The workflow should orchestrate all RAG agents
        assert len(collective.rag_agents) == 3
        assert collective.source_weights is not None
        assert collective.aggregation_mode == "hierarchical"
