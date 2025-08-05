"""Tests for ReactRAGAgent - real component testing with retriever node."""

from langchain_core.tools import tool
import pytest

from haive.agents.rag.agentic import ReactRAGAgent
from haive.core.engine.vectorstore import VectorStoreConfig
from haive.core.models.embeddings import EmbeddingConfig


class TestReactRAGAgent:
    """Test ReactRAGAgent with real components and retrieval node."""

    @pytest.fixture
    def mock_vector_store_config(self):
        """Create a mock vector store configuration."""
        # In real tests, this would be a proper vector store
        embedding_config = EmbeddingConfig(provider="openai", model="text-embedding-3-small")

        return VectorStoreConfig(
            provider="chroma",
            embedding=embedding_config,
            collection_name="test_collection",
            persist_directory="./test_chroma_db",
        )

    @pytest.fixture
    def calculator_tool(self):
        """Create a calculator tool for testing."""

        @tool
        def calculator(expression: str) -> str:
            """Calculate mathematical expressions.

            Args:
                expression: Math expression to evaluate

            Returns:
                Result of the calculation
            """
            try:
                result = eval(expression)
                return f"The result is: {result}"
            except Exception as e:
                return f"Error calculating: {e!s}"

        return calculator

    @pytest.mark.asyncio
    async def test_react_rag_agent_creation(self, mock_vector_store_config, calculator_tool):
        """Test creating a ReactRAG agent with retriever and tools."""
        agent = ReactRAGAgent.create_default(
            name="test_react_rag",
            retriever_config=mock_vector_store_config,
            tools=[calculator_tool],
            temperature=0.1,
        )

        assert agent.name == "test_react_rag"
        assert agent.retriever_config == mock_vector_store_config
        assert len(agent.tools) == 2  # calculator + retriever

        # Check that retriever tool was added
        tool_names = {t.name for t in agent.tools}
        assert "retriever" in tool_names
        assert "calculator" in tool_names

    @pytest.mark.asyncio
    async def test_build_graph_with_retrieval_node(self, mock_vector_store_config):
        """Test that the graph includes a retrieval node."""
        agent = ReactRAGAgent.create_default(
            name="test_graph",
            retriever_config=mock_vector_store_config,
            temperature=0.1,
        )

        # Build the graph
        graph = agent.build_graph()

        # Verify retrieval node exists
        assert "retrieval_node" in graph.nodes
        assert "agent_node" in graph.nodes

        # Verify routing exists
        # The agent_node should have conditional edges
        assert any(edge[0] == "agent_node" for edge in graph.edges)

        # Retrieval node should route back to agent_node (React loop)
        assert ("retrieval_node", "agent_node") in graph.edges

    @pytest.mark.asyncio
    async def test_routing_logic(self, mock_vector_store_config, calculator_tool):
        """Test the routing logic between retrieval and tools."""
        agent = ReactRAGAgent.create_default(
            name="test_routing",
            retriever_config=mock_vector_store_config,
            tools=[calculator_tool],
            temperature=0.1,
        )

        # Test routing with retriever tool call
        class MockState:
            messages = []

        state = MockState()

        # Test with no messages - should route to end
        result = agent._route_to_retrieval_or_tools(state)
        assert result == "end"

        # Test with AI message containing retriever tool call
        from langchain_core.messages import AIMessage

        ai_msg = AIMessage(
            content="I'll search for that information.",
            tool_calls=[{"name": "retriever", "args": {"query": "test"}}],
        )
        state.messages = [ai_msg]

        result = agent._route_to_retrieval_or_tools(state)
        assert result == "retrieval"

        # Test with calculator tool call
        ai_msg = AIMessage(
            content="Let me calculate that.",
            tool_calls=[{"name": "calculator", "args": {"expression": "2+2"}}],
        )
        state.messages = [ai_msg]

        result = agent._route_to_retrieval_or_tools(state)
        assert result == "tools"

    @pytest.mark.asyncio
    async def test_from_vectorstore_creation(self, mock_vector_store_config):
        """Test creating agent from vector store config."""
        agent = ReactRAGAgent.from_vectorstore(
            mock_vector_store_config, name="from_vs_agent", temperature=0.2
        )

        assert agent.name == "from_vs_agent"
        assert agent.retriever_config == mock_vector_store_config
        assert agent.engine.temperature == 0.2

    @pytest.mark.asyncio
    async def test_add_retriever_tool(self, calculator_tool):
        """Test adding retriever tool after creation."""
        # Create agent without retriever first
        agent = ReactRAGAgent.create_default(
            name="test_add_retriever", tools=[calculator_tool], temperature=0.1
        )

        # Initially should only have calculator
        assert len(agent.tools) == 1
        assert agent.tools[0].name == "calculator"

        # Add retriever
        embedding_config = EmbeddingConfig(provider="openai", model="text-embedding-3-small")

        vector_store_config = VectorStoreConfig(
            provider="chroma",
            embedding=embedding_config,
            collection_name="new_collection",
        )

        agent.add_retriever_tool(vector_store_config)

        # Should now have both tools
        assert len(agent.tools) == 2
        tool_names = {t.name for t in agent.tools}
        assert "retriever" in tool_names
        assert "calculator" in tool_names
        assert agent.retriever_config == vector_store_config

    @pytest.mark.asyncio
    async def test_retriever_tool_creation(self, mock_vector_store_config):
        """Test that retriever tool is properly created."""
        tool = ReactRAGAgent._create_retriever_tool(mock_vector_store_config)

        assert tool.name == "retriever"
        assert "knowledge base" in tool.description.lower()

        # Test the tool function
        result = tool.func("test query")
        assert "Searching knowledge base for: test query" in result

    @pytest.mark.asyncio
    async def test_multiple_tools_with_retriever(self, mock_vector_store_config):
        """Test agent with multiple tools plus retriever."""

        @tool
        def web_search(query: str) -> str:
            """Search the web for information."""
            return f"Web results for: {query}"

        @tool
        def weather(location: str) -> str:
            """Get weather for a location."""
            return f"Weather in {location}: Sunny, 72°F"

        agent = ReactRAGAgent.create_default(
            name="multi_tool_agent",
            retriever_config=mock_vector_store_config,
            tools=[self.calculator_tool(), web_search, weather],
            temperature=0.1,
        )

        # Should have all tools plus retriever
        assert len(agent.tools) == 4
        tool_names = {t.name for t in agent.tools}
        assert tool_names == {"calculator", "web_search", "weather", "retriever"}

    @pytest.mark.asyncio
    async def test_routing_strategies(self, mock_vector_store_config, calculator_tool):
        """Test different routing strategies."""
        # Test auto routing (default)
        agent_auto = ReactRAGAgent.create_default(
            name="auto_routing",
            retriever_config=mock_vector_store_config,
            tools=[calculator_tool],
            routing_strategy="auto",
        )
        assert agent_auto.routing_strategy == "auto"

        # Test retriever_first strategy
        agent_retriever_first = ReactRAGAgent.create_default(
            name="retriever_first",
            retriever_config=mock_vector_store_config,
            tools=[calculator_tool],
            routing_strategy="retriever_first",
        )
        assert agent_retriever_first.routing_strategy == "retriever_first"

    @pytest.mark.asyncio
    async def test_use_retriever_for_knowledge_flag(self, mock_vector_store_config):
        """Test the use_retriever_for_knowledge configuration."""
        agent = ReactRAGAgent.create_default(
            name="knowledge_flag_test",
            retriever_config=mock_vector_store_config,
            use_retriever_for_knowledge=False,
        )

        assert agent.use_retriever_for_knowledge is False
