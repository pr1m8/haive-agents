"""Integration tests for the complete Agentic RAG workflow."""

import pytest

from haive.agents.rag.agentic import (
    AgenticRAGAgent,
    DocumentGraderAgent,
    QueryRewriterAgent,
    ReactRAGAgent,
)
from haive.core.engine.vectorstore import VectorStoreConfig
from haive.core.models.embeddings import EmbeddingConfig


class TestAgenticRAGIntegration:
    """Integration tests for the complete Agentic RAG system."""

    @pytest.mark.asyncio
    async def test_document_grader_integration(self):
        """Test document grader with real LLM calls."""
        grader = DocumentGraderAgent.create_default(temperature=0.0)

        # Test grading multiple documents
        result = await grader.arun(
            {
                "query": "How does blockchain technology work?",
                "documents": [
                    {
                        "id": "doc1",
                        "content": "Blockchain is a distributed ledger technology that uses cryptographic hashing to create an immutable chain of blocks.",
                    },
                    {
                        "id": "doc2",
                        "content": "Pizza is a popular Italian dish with cheese and tomato sauce.",
                    },
                    {
                        "id": "doc3",
                        "content": "Each block in a blockchain contains transaction data and is linked to the previous block through cryptographic hashes.",
                    },
                ],
            }
        )

        # Verify grading
        assert len(result.document_decisions) == 3

        # Blockchain documents should pass, pizza should fail
        decisions_by_id = {d.document_id: d for d in result.document_decisions}
        assert decisions_by_id["doc1"].decision == "pass"
        assert decisions_by_id["doc2"].decision == "fail"
        assert decisions_by_id["doc3"].decision == "pass"

    @pytest.mark.asyncio
    async def test_query_rewriter_integration(self):
        """Test query rewriter with real LLM calls."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        # Test rewriting vague queries
        result = await rewriter.arun(
            {
                "query": "AI stuff",
                "context": "User is researching for a computer science course",
            }
        )

        # Verify improvements
        assert result.original_query == "AI stuff"
        assert len(result.best_refined_query) > len("AI stuff")
        assert len(result.refinement_suggestions) >= 2

        # Should incorporate context
        assert any(
            "computer science" in s.refined_query.lower()
            or "artificial intelligence" in s.refined_query.lower()
            for s in result.refinement_suggestions
        )

    @pytest.mark.asyncio
    async def test_react_rag_routing(self):
        """Test ReactRAG agent routing between tools and retrieval."""
        # Create mock vector store config
        embedding_config = EmbeddingConfig(
            provider="openai", model="text-embedding-3-small"
        )

        vector_store_config = VectorStoreConfig(
            provider="chroma",
            embedding=embedding_config,
            collection_name="test_routing",
        )

        # Create ReactRAG agent
        from langchain_core.tools import tool

        @tool
        def calculator(expression: str) -> str:
            """Calculate math expressions."""
            return str(eval(expression))

        agent = ReactRAGAgent.create_default(
            name="routing_test",
            retriever_config=vector_store_config,
            tools=[calculator],
            temperature=0.1,
        )

        # Verify graph structure
        graph = agent.build_graph()
        assert "retrieval_node" in graph.nodes
        assert "tool_node" in graph.nodes
        assert "agent_node" in graph.nodes

        # Test routing logic
        from langchain_core.messages import AIMessage

        class MockState:
            messages = []

        state = MockState()

        # Route to retrieval
        state.messages = [
            AIMessage(
                content="Searching knowledge base",
                tool_calls=[{"name": "retriever", "args": {}}],
            )
        ]
        route = agent._route_to_retrieval_or_tools(state)
        assert route == "retrieval"

        # Route to tools
        state.messages = [
            AIMessage(
                content="Calculating", tool_calls=[{"name": "calculator", "args": {}}]
            )
        ]
        route = agent._route_to_retrieval_or_tools(state)
        assert route == "tools"

    @pytest.mark.asyncio
    async def test_complete_workflow_components(self):
        """Test that all components work together."""
        # Create vector store config
        embedding_config = EmbeddingConfig(
            provider="openai", model="text-embedding-3-small"
        )

        vector_store_config = VectorStoreConfig(
            provider="chroma",
            embedding=embedding_config,
            collection_name="test_workflow",
        )

        # Create the complete agent
        agent = AgenticRAGAgent.create_default(
            name="workflow_test",
            retriever_config=vector_store_config,
            use_web_search=True,
            temperature=0.1,
        )

        # Verify all components exist
        assert agent.grader_agent is not None
        assert agent.rewriter_agent is not None
        assert agent.generator_agent is not None
        assert agent.web_search_agent is not None

        # Test component functionality
        # 1. Grader can grade
        grading_result = await agent.grader_agent.grade_documents(
            query="test query", documents=[{"id": "1", "content": "test content"}]
        )
        assert len(grading_result.document_decisions) == 1

        # 2. Rewriter can rewrite
        rewrite_result = await agent.rewriter_agent.rewrite_query("test")
        assert rewrite_result.best_refined_query != ""

        # 3. Graph is properly built
        graph = agent.build_graph()
        expected_nodes = [
            "retrieve",
            "grade_documents",
            "rewrite_query",
            "web_search",
            "generate_answer",
        ]
        for node in expected_nodes:
            assert node in graph.nodes

    @pytest.mark.asyncio
    async def test_state_flow(self):
        """Test the state flow through the system."""
        from haive.agents.rag.agentic import AgenticRAGState

        # Create state
        state = AgenticRAGState()

        # Simulate workflow progression
        # 1. Set original query
        state.original_query = "What is machine learning?"

        # 2. Add retrieved documents
        state.retrieved_documents = [
            {"content": "ML is AI that learns from data"},
            {"content": "Weather forecast for tomorrow"},
        ]

        # 3. Grade documents
        state.graded_documents = state.retrieved_documents
        state.relevant_documents = [state.retrieved_documents[0]]
        state.all_documents_relevant = False

        # 4. Rewrite query
        state.refined_query = "What is machine learning and how does it differ from traditional programming?"
        state.query_rewrite_count = 1

        # 5. Web search
        state.web_search_results = [
            {"content": "Recent ML developments in 2024", "source": "web"}
        ]

        # 6. Generate answer
        state.final_answer = "Machine learning is a type of AI that learns from data..."

        # Verify state progression
        assert state.original_query == "What is machine learning?"
        assert len(state.retrieved_documents) == 2
        assert len(state.relevant_documents) == 1
        assert state.query_rewrite_count == 1
        assert len(state.web_search_results) == 1
        assert state.final_answer != ""

    @pytest.mark.asyncio
    async def test_error_handling(self):
        """Test error handling in the system."""
        # Create agent without required config
        with pytest.raises(ValueError, match="retriever_config is required"):
            AgenticRAGAgent.create_default(name="no_retriever", retriever_config=None)
