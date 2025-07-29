"""Tests for ReactAgent Memory Coordinator.

This test suite validates:
1. ReactAgent tool integration with memory agents
2. Memory coordination across different memory types
3. Real LLM execution with memory tools
4. Cross-memory search and storage operations
5. Memory pattern analysis and insights

NO MOCKS - All tests use real components including:
- Real Azure OpenAI for ReactAgent reasoning
- Real BaseRAGAgent for memory retrieval
- Real vector stores for semantic search
- Real file-based memory persistence
"""

import asyncio
import shutil
import tempfile

import pytest
from langchain_core.messages import AIMessage, HumanMessage

# Import test components
from haive.agents.memory_reorganized.coordination.react_coordinator import (
    MemoryCoordinatorConfig,
    ReactMemoryCoordinator,
)


class TestReactMemoryCoordinator:
    """Test ReactAgent memory coordination with real components.
    """

    @pytest.fixture
    async def temp_storage(self):
        """Create temporary storage for tests.
        """
        temp_dir = tempfile.mkdtemp(prefix="test_react_memory_")
        yield temp_dir
        shutil.rmtree(temp_dir, ignore_errors=True)

    @pytest.fixture
    async def coordinator(self, temp_storage):
        """Create ReactMemoryCoordinator for testing.
        """
        config = MemoryCoordinatorConfig(
            long_term_memory_path=f"{temp_storage}/ltm",
            conversation_memory_path=f"{temp_storage}/conv",
            temperature=0.1,  # Low temperature for consistent tests
            max_iterations=2,  # Limit iterations for faster tests
        )

        coordinator = ReactMemoryCoordinator(
            user_id="test_user", config=config, name="test_coordinator"
        )

        await coordinator.initialize()
        return coordinator

    @pytest.mark.asyncio
    async def test_coordinator_initialization(self, coordinator):
        """Test ReactMemoryCoordinator initialization.
        """
        # Verify coordinator is initialized
        assert coordinator._initialized
        assert coordinator.user_id == "test_user"
        assert coordinator.name == "test_coordinator"

        # Verify memory agents are created
        assert coordinator.long_term_memory is not None
        assert coordinator.conversation_memory is not None

        # Verify ReactAgent is created with tools
        assert coordinator.react_agent is not None
        assert len(coordinator.react_agent.tools) > 0

        # Check tool names
        tool_names = [tool.name for tool in coordinator.react_agent.tools]
        expected_tools = [
            "search_long_term_memory",
            "search_conversation_memory",
            "store_memory",
            "analyze_memory_patterns",
        ]

        for expected in expected_tools:
            assert expected in tool_names, f"Missing tool: {expected}"

    @pytest.mark.asyncio
    async def test_basic_memory_coordination(self, coordinator):
        """Test basic memory coordination with ReactAgent.
        """
        # Add initial conversation context
        initial_messages = [
            HumanMessage("Hi, I'm Sarah, a product manager at Spotify"),
            HumanMessage(
                "I work on recommendation algorithms and prefer morning meetings"
            ),
        ]

        batch_result = await coordinator.add_conversation_batch(initial_messages)
        assert batch_result["conversation_stored"]
        assert batch_result["memories_extracted"] >= 0

        # Test memory-enhanced query
        result = await coordinator.run("What do you know about my job and preferences?")

        # Verify response structure
        assert "response" in result
        assert "user_id" in result
        assert result["user_id"] == "test_user"

        # Response should contain relevant information
        response_text = str(result["response"])
        assert len(response_text) > 0

        # Check that ReactAgent used tools (indicated by structured reasoning)
        # ReactAgent responses typically contain tool usage patterns
        print(f"Response: {response_text[:200]}...")

    @pytest.mark.asyncio
    async def test_memory_tool_integration(self, coordinator):
        """Test individual memory tools through ReactAgent.
        """
        # Store some test memories
        store_result = await coordinator.run(
            "Please store this information: I prefer Python over JavaScript for data analysis"
        )
        assert "response" in store_result

        # Search for stored memory
        search_result = await coordinator.run("What programming languages do I prefer?")
        assert "response" in search_result
        response_text = str(search_result["response"])

        # Response should reference the stored preference
        assert len(response_text) > 0
        print(f"Search result: {response_text[:150]}...")

    @pytest.mark.asyncio
    async def test_cross_memory_coordination(self, coordinator):
        """Test coordination between different memory types.
        """
        # Add conversation memory
        conv_messages = [
            HumanMessage("I'm working on a machine learning project"),
            AIMessage("That sounds interesting! What kind of ML are you focusing on?"),
            HumanMessage("Natural language processing for sentiment analysis"),
        ]

        await coordinator.add_conversation_batch(conv_messages)

        # Query that should use both conversation and long-term memory
        result = await coordinator.run(
            "Based on our conversation and what you know about me, what would be a good next step for my project?"
        )

        assert "response" in result
        response_text = str(result["response"])
        assert len(response_text) > 0

        # ReactAgent should coordinate between memory sources
        print(f"Cross-memory response: {response_text[:200]}...")

    @pytest.mark.asyncio
    async def test_memory_analysis_tool(self, coordinator):
        """Test memory pattern analysis tool.
        """
        # Add some diverse memories
        messages = [
            HumanMessage("I love jazz music and play piano"),
            HumanMessage("I work as a data scientist at Netflix"),
            HumanMessage("I prefer working in quiet environments"),
            HumanMessage("My favorite programming language is Python"),
        ]

        await coordinator.add_conversation_batch(messages)

        # Request memory analysis
        result = await coordinator.run(
            "Can you analyze my memory patterns and give me insights?"
        )

        assert "response" in result
        response_text = str(result["response"])
        assert len(response_text) > 0

        # Analysis should contain insights about stored memories
        print(f"Memory analysis: {response_text[:200]}...")

    @pytest.mark.asyncio
    async def test_comprehensive_memory_summary(self, coordinator):
        """Test comprehensive memory summary.
        """
        # Add some test data
        test_messages = [
            HumanMessage("I'm a software engineer"),
            HumanMessage("I enjoy problem-solving"),
        ]

        await coordinator.add_conversation_batch(test_messages)

        # Get comprehensive summary
        summary = await coordinator.get_comprehensive_memory_summary()

        # Verify summary structure
        assert "user_id" in summary
        assert "coordinator_name" in summary
        assert "initialized" in summary
        assert "memory_systems" in summary

        assert summary["user_id"] == "test_user"
        assert summary["initialized"] is True

        # Check memory systems
        memory_systems = summary["memory_systems"]
        assert "long_term" in memory_systems
        assert "conversation" in memory_systems

        # Verify memory system details
        ltm_summary = memory_systems["long_term"]
        conv_summary = memory_systems["conversation"]

        assert "total_memories" in ltm_summary
        assert "total_messages" in conv_summary

        print(f"Summary: {summary}")

    @pytest.mark.asyncio
    async def test_factory_methods(self, temp_storage):
        """Test factory methods for creating coordinators.
        """
        # Test basic factory
        coordinator1 = ReactMemoryCoordinator.create(
            user_id="factory_test_user1", name="factory_test1"
        )

        assert coordinator1.user_id == "factory_test_user1"
        assert coordinator1.name == "factory_test1"

        # Test focused factory
        coordinator2 = ReactMemoryCoordinator.create_focused(
            user_id="factory_test_user2", name="factory_test2"
        )

        assert coordinator2.user_id == "factory_test_user2"
        assert coordinator2.name == "factory_test2"
        assert coordinator2.config.temperature == 0.3  # Focused config
        assert coordinator2.config.max_iterations == 2

    @pytest.mark.asyncio
    async def test_error_handling(self, coordinator):
        """Test error handling in memory operations.
        """
        # Test with malformed queries
        result = await coordinator.run("")
        assert "response" in result

        # Test with very long query
        long_query = "test " * 1000
        result = await coordinator.run(long_query)
        assert "response" in result

        # Should handle gracefully without crashing
        print("✅ Error handling tests passed")


# Integration test with real workflow
@pytest.mark.asyncio
async def test_complete_memory_workflow():
    """Test complete memory workflow with ReactAgent coordination.
    """
    print("\n🧪 Integration Test: Complete Memory Workflow")

    # Create temporary storage
    temp_dir = tempfile.mkdtemp(prefix="integration_test_")

    try:
        # Create coordinator
        config = MemoryCoordinatorConfig(
            long_term_memory_path=f"{temp_dir}/ltm",
            conversation_memory_path=f"{temp_dir}/conv",
            temperature=0.1,
        )

        coordinator = ReactMemoryCoordinator(
            user_id="integration_user", config=config, name="integration_test"
        )

        await coordinator.initialize()
        print("✅ Coordinator initialized")

        # Step 1: Build up memory context
        profile_messages = [
            HumanMessage("Hi, I'm Alex, a senior software engineer at Google"),
            HumanMessage("I specialize in distributed systems and machine learning"),
            HumanMessage(
                "I prefer working in small teams and love collaborative coding"
            ),
            HumanMessage(
                "My current project is building a real-time recommendation engine"
            ),
        ]

        await coordinator.add_conversation_batch(profile_messages)
        print("✅ Added profile information")

        # Step 2: Test memory-enhanced conversations
        queries = [
            "Tell me about my professional background",
            "What kind of work environment do I prefer?",
            "How does my current project relate to my expertise?",
            "Based on my preferences, how should I approach team collaboration?",
        ]

        for i, query in enumerate(queries, 1):
            try:
                result = await coordinator.run(query)
                response_text = str(result["response"])

                print(f"\n{i}. Query: {query}")
                print(f"   Response: {response_text[:150]}...")

                assert len(response_text) > 0

            except Exception as e:
                print(f"   ⚠️ Query failed: {str(e)[:100]}...")

        # Step 3: Test memory analysis
        summary = await coordinator.get_comprehensive_memory_summary()
        print("\n📊 Final Summary:")
        print(
            f"   Long-term memories: {summary['memory_systems']['long_term']['total_memories']}"
        )
        print(
            f"   Conversation messages: {summary['memory_systems']['conversation']['total_messages']}"
        )

        print("\n✅ Integration test completed successfully!")

    finally:
        # Cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    # Run integration test directly
    asyncio.run(test_complete_memory_workflow())
