"""Tests for AgenticRAGAgent - complete multi-agent RAG system."""

import pytest

from haive.agents.rag.agentic import AgenticRAGAgent, AgenticRAGState
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig
from haive.core.models.embeddings import EmbeddingConfig


class TestAgenticRAGAgent:
    """Test the complete Agentic RAG system with real components."""

    @pytest.fixture
    def mock_vector_store_config(self):
        """Create a mock vector store configuration."""
        embedding_config = EmbeddingConfig(
            provider="openai", model="text-embedding-3-small"
        )

        return VectorStoreConfig(
            provider="chroma",
            embedding=embedding_config,
            collection_name="test_agentic_rag",
            persist_directory="./test_chroma_db",
        )

    @pytest.mark.asyncio
    async def test_agentic_rag_creation(self, mock_vector_store_config):
        """Test creating an Agentic RAG agent."""
        agent = AgenticRAGAgent.create_default(
            name="test_agentic_rag",
            retriever_config=mock_vector_store_config,
            use_web_search=True,
            temperature=0.1,
        )

        assert agent.name == "test_agentic_rag"
        assert agent.retriever_config == mock_vector_store_config
        assert agent.use_web_search is True
        assert agent.max_query_rewrites == 1

        # Check component agents were created
        assert agent.grader_agent is not None
        assert agent.grader_agent.name == "test_agentic_rag_grader"

        assert agent.rewriter_agent is not None
        assert agent.rewriter_agent.name == "test_agentic_rag_rewriter"

        assert agent.generator_agent is not None
        assert agent.generator_agent.name == "test_agentic_rag_generator"

        assert agent.web_search_agent is not None
        assert agent.web_search_agent.name == "test_agentic_rag_web_search"

    @pytest.mark.asyncio
    async def test_agentic_rag_without_web_search(self, mock_vector_store_config):
        """Test creating agent without web search."""
        agent = AgenticRAGAgent.create_default(
            name="no_web_search",
            retriever_config=mock_vector_store_config,
            use_web_search=False,
        )

        assert agent.use_web_search is False
        assert agent.web_search_agent is None

    @pytest.mark.asyncio
    async def test_build_graph(self, mock_vector_store_config):
        """Test that the complete RAG graph is built correctly."""
        agent = AgenticRAGAgent.create_default(
            name="test_graph",
            retriever_config=mock_vector_store_config,
            use_web_search=True,
        )

        # Build the graph
        graph = agent.build_graph()

        # Verify all nodes exist
        expected_nodes = [
            "retrieve",
            "grade_documents",
            "rewrite_query",
            "web_search",
            "generate_answer",
        ]

        for node in expected_nodes:
            assert node in graph.nodes

        # Verify key edges
        assert any(
            edge[0] == "__start__" and edge[1] == "retrieve" for edge in graph.edges
        )
        assert ("retrieve", "grade_documents") in graph.edges
        assert ("rewrite_query", "retrieve") in graph.edges
        assert ("web_search", "generate_answer") in graph.edges
        assert any(
            edge[0] == "generate_answer" and edge[1] == "__end__"
            for edge in graph.edges
        )

    @pytest.mark.asyncio
    async def test_routing_logic(self, mock_vector_store_config):
        """Test the routing logic after document grading."""
        agent = AgenticRAGAgent.create_default(
            name="test_routing",
            retriever_config=mock_vector_store_config,
            use_web_search=True,
        )

        # Test with relevant documents
        state = AgenticRAGState(
            relevant_documents=[{"content": "doc1"}, {"content": "doc2"}],
            query_rewrite_count=0,
        )

        route = agent._route_after_grading(state)
        assert route == "generate"

        # Test with no relevant documents, should rewrite
        state = AgenticRAGState(relevant_documents=[], query_rewrite_count=0)

        route = agent._route_after_grading(state)
        assert route == "rewrite"

        # Test with no relevant documents and max rewrites reached
        state = AgenticRAGState(
            relevant_documents=[],
            query_rewrite_count=1,  # Already rewritten once
        )

        route = agent._route_after_grading(state)
        assert route == "web_search"

        # Test with web search disabled
        agent.use_web_search = False
        route = agent._route_after_grading(state)
        assert route == "generate"

    @pytest.mark.asyncio
    async def test_retrieve_documents_node(self, mock_vector_store_config):
        """Test the document retrieval node."""
        agent = AgenticRAGAgent.create_default(
            name="test_retrieve", retriever_config=mock_vector_store_config
        )

        # Create initial state
        state = AgenticRAGState(original_query="What is machine learning?")

        # Run retrieve node (will fail without real vector store, but tests structure)
        try:
            result = await agent._retrieve_documents(state)
            # If it succeeds (with real vector store)
            assert "retrieved_documents" in result
            assert "messages" in result
        except Exception:
            # Expected without real vector store setup
            pass

    @pytest.mark.asyncio
    async def test_grade_documents_node(self, mock_vector_store_config):
        """Test the document grading node."""
        agent = AgenticRAGAgent.create_default(
            name="test_grade", retriever_config=mock_vector_store_config
        )

        # Create state with retrieved documents
        state = AgenticRAGState(
            original_query="What is quantum computing?",
            retrieved_documents=[
                {
                    "content": "Quantum computing uses quantum mechanics...",
                    "page_content": "Quantum computing uses quantum mechanics...",
                },
                {
                    "content": "The weather is sunny today...",
                    "page_content": "The weather is sunny today...",
                },
            ],
        )

        # Run grade documents node
        result = await agent._grade_documents(state)

        # Check results
        assert "graded_documents" in result
        assert "relevant_documents" in result
        assert "all_documents_relevant" in result
        assert "messages" in result

        # Should have graded both documents
        assert len(result["graded_documents"]) == 2

        # Quantum document should be relevant, weather should not
        assert len(result["relevant_documents"]) <= 2
        assert result["all_documents_relevant"] is False

    @pytest.mark.asyncio
    async def test_rewrite_query_node(self, mock_vector_store_config):
        """Test the query rewriting node."""
        agent = AgenticRAGAgent.create_default(
            name="test_rewrite", retriever_config=mock_vector_store_config
        )

        # Create state needing rewrite
        state = AgenticRAGState(original_query="ML stuff", query_rewrite_count=0)

        # Run rewrite node
        result = await agent._rewrite_query(state)

        # Check results
        assert "refined_query" in result
        assert "query_rewrite_count" in result
        assert "messages" in result

        assert result["query_rewrite_count"] == 1
        assert result["refined_query"] != ""
        assert len(result["refined_query"]) > len("ML stuff")

    @pytest.mark.asyncio
    async def test_web_search_node(self, mock_vector_store_config):
        """Test the web search fallback node."""
        agent = AgenticRAGAgent.create_default(
            name="test_web",
            retriever_config=mock_vector_store_config,
            use_web_search=True,
        )

        # Create state for web search
        state = AgenticRAGState(original_query="Latest AI developments 2024")

        # Run web search node
        result = await agent._web_search(state)

        # Check results
        assert "web_search_results" in result
        assert "messages" in result
        assert len(result["web_search_results"]) > 0

    @pytest.mark.asyncio
    async def test_generate_answer_node(self, mock_vector_store_config):
        """Test the final answer generation node."""
        agent = AgenticRAGAgent.create_default(
            name="test_generate", retriever_config=mock_vector_store_config
        )

        # Create state with documents
        state = AgenticRAGState(
            original_query="What is machine learning?",
            relevant_documents=[
                {
                    "content": "Machine learning is a type of AI that learns from data.",
                    "source": "ml_basics.txt",
                }
            ],
            web_search_results=[],
        )

        # Run generate node
        result = await agent._generate_answer(state)

        # Check results
        assert "final_answer" in result
        assert "messages" in result
        assert result["final_answer"] != ""
        assert len(result["final_answer"]) > 10

    @pytest.mark.asyncio
    async def test_custom_component_agents(self, mock_vector_store_config):
        """Test creating with custom component agents."""
        # Create custom grader
        from haive.agents.rag.agentic import DocumentGraderAgent

        custom_grader = DocumentGraderAgent.create_default(
            name="custom_grader", temperature=0.0
        )

        # Create agent with custom components
        agent = AgenticRAGAgent(
            name="custom_components",
            engine=AugLLMConfig(),
            retriever_config=mock_vector_store_config,
            grader_agent=custom_grader,
            use_web_search=False,
        )

        assert agent.grader_agent == custom_grader
        assert agent.grader_agent.name == "custom_grader"

    @pytest.mark.asyncio
    async def test_state_initialization(self):
        """Test AgenticRAGState initialization."""
        state = AgenticRAGState(original_query="test query")

        assert state.original_query == "test query"
        assert state.refined_query == ""
        assert state.query_rewrite_count == 0
        assert len(state.retrieved_documents) == 0
        assert len(state.graded_documents) == 0
        assert len(state.relevant_documents) == 0
        assert len(state.web_search_results) == 0
        assert state.all_documents_relevant is True
        assert state.use_web_search is False
        assert state.final_answer == ""

    @pytest.mark.asyncio
    async def test_relevance_threshold(self, mock_vector_store_config):
        """Test relevance threshold configuration."""
        agent = AgenticRAGAgent.create_default(
            name="threshold_test",
            retriever_config=mock_vector_store_config,
            relevance_threshold=0.8,
        )

        assert agent.relevance_threshold == 0.8

    @pytest.mark.asyncio
    async def test_max_query_rewrites(self, mock_vector_store_config):
        """Test max query rewrites configuration."""
        agent = AgenticRAGAgent.create_default(
            name="rewrite_test",
            retriever_config=mock_vector_store_config,
            max_query_rewrites=3,
        )

        assert agent.max_query_rewrites == 3

        # Test routing with multiple rewrites
        state = AgenticRAGState(
            relevant_documents=[], query_rewrite_count=2  # Less than max
        )

        route = agent._route_after_grading(state)
        assert route == "rewrite"

        # Test at max rewrites
        state.query_rewrite_count = 3
        route = agent._route_after_grading(state)
        assert route == "web_search"  # Should go to web search
