"""Tests for ReactMemoryAgent with real components (no mocks).

These tests demonstrate the ReactAgent with memory tools pattern.
"""

import asyncio
import shutil
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.memory_v2.react_memory_agent import ReactMemoryAgent


class TestReactMemoryAgent:
    """Test ReactAgent with memory management tools."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for vector stores."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def memory_agent(self):
        """Create a ReactMemoryAgent for testing."""
        return ReactMemoryAgent(
            name="test_memory_agent",
            engine=AugLLMConfig(temperature=0.1),
            user_id="test_user",
            k=3,
            use_time_weighting=True,
        )

    @pytest.mark.asyncio
    async def test_memory_storage_and_retrieval(self, memory_agent):
        """Test storing and retrieving memories."""
        # Store a memory about user preferences
        response1 = await memory_agent.arun(
            "Please store a memory that I prefer Python over Java for data science work",
            auto_save=False,
        )
        assert "stored" in response1.lower()

        # Store another memory about work
        response2 = await memory_agent.arun(
            "Store a memory that I work at DataCorp as a senior analyst",
            auto_save=False,
        )
        assert "stored" in response2.lower()

        # Retrieve memories about work
        response3 = await memory_agent.arun(
            "What do you remember about my work?", auto_save=False
        )
        assert "datacorp" in response3.lower() or "analyst" in response3.lower()

        # Retrieve memories about preferences
        response4 = await memory_agent.arun(
            "Search my memories for programming language preferences", auto_save=False
        )
        assert "python" in response4.lower() or "java" in response4.lower()

    @pytest.mark.asyncio
    async def test_auto_save_conversations(self, memory_agent):
        """Test automatic conversation saving."""
        # Have a conversation with auto_save enabled
        await memory_agent.arun(
            "My favorite color is blue and I have two cats named Luna and Star",
            auto_save=True,
        )

        # Wait a moment for storage
        await asyncio.sleep(1)

        # Check if conversation was saved
        response2 = await memory_agent.arun("What are my cats' names?", auto_save=False)
        assert "luna" in response2.lower() or "star" in response2.lower()

    @pytest.mark.asyncio
    async def test_time_based_memory_search(self, memory_agent):
        """Test searching memories by time range."""
        # Store memories at different times
        await memory_agent.arun(
            "Store a memory that I started learning Spanish today", auto_save=False
        )

        # Get today's date
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # Search memories from today
        response2 = await memory_agent.arun(
            f"Search memories from {today}", auto_save=False
        )
        assert "spanish" in response2.lower() or "learning" in response2.lower()

        # Search memories from yesterday (should be empty or few)
        response3 = await memory_agent.arun(
            f"Search memories from {yesterday} to {yesterday}", auto_save=False
        )
        # Response should indicate no memories or very few
        assert "no memories" in response3.lower() or len(response3) < 100

    @pytest.mark.asyncio
    async def test_memory_importance_levels(self, memory_agent):
        """Test storing memories with different importance levels."""
        # Store critical memory
        response1 = await memory_agent.arun(
            'Store a critical importance memory: "Medical allergy to penicillin"',
            auto_save=False,
        )
        assert "critical" in response1.lower()

        # Store normal memory
        response2 = await memory_agent.arun(
            'Store a normal importance memory: "Likes coffee in the morning"',
            auto_save=False,
        )
        assert "normal" in response2.lower()

        # List recent memories to see importance levels
        response3 = await memory_agent.arun(
            "List my 5 most recent memories", auto_save=False
        )
        assert "importance" in response3.lower()

    @pytest.mark.asyncio
    async def test_memory_updates(self, memory_agent):
        """Test updating existing memories."""
        # Store initial memory
        await memory_agent.arun(
            "Store a memory that I live in New York City", auto_save=False
        )

        # Update the memory
        response2 = await memory_agent.arun(
            "Update the memory about where I live to say I moved to San Francisco",
            auto_save=False,
        )
        assert "updated" in response2.lower()

        # Verify update
        response3 = await memory_agent.arun("Where do I live?", auto_save=False)
        # Should mention San Francisco or the update
        assert "francisco" in response3.lower() or "updated" in response3.lower()

    @pytest.mark.asyncio
    async def test_memory_deletion(self, memory_agent):
        """Test marking memories as deleted."""
        # Store a memory
        await memory_agent.arun(
            "Store a memory that my phone number is 555-1234", auto_save=False
        )

        # Delete the memory
        response2 = await memory_agent.arun(
            "Delete the memory about my phone number", auto_save=False
        )
        assert "deleted" in response2.lower()

        # Verify deletion marker exists
        response3 = await memory_agent.arun(
            "Search for my phone number", auto_save=False
        )
        # Should show deleted marker or indicate deletion
        assert "deleted" in response3.lower() or "no" in response3.lower()

    @pytest.mark.asyncio
    async def test_custom_tools_integration(self):
        """Test ReactMemoryAgent with custom tools."""

        # Define custom tools
        @tool
        def word_counter(text: str) -> str:
            """Count words in text."""
            word_count = len(text.split())
            return f"The text contains {word_count} words"

        @tool
        def reverse_text(text: str) -> str:
            """Reverse the given text."""
            return text[::-1]

        # Create agent with custom tools
        agent = ReactMemoryAgent.create_with_custom_tools(
            name="enhanced_agent",
            engine=AugLLMConfig(temperature=0.1),
            custom_tools=[word_counter, reverse_text],
            user_id="enhanced_user",
        )

        # Test memory tools still work
        response1 = await agent.arun(
            "Store a memory that I like pizza", auto_save=False
        )
        assert "stored" in response1.lower()

        # Test custom tools work
        response2 = await agent.arun(
            "Count the words in 'The quick brown fox jumps'", auto_save=False
        )
        assert "5" in response2 or "five" in response2.lower()

        # Test combination
        response3 = await agent.arun(
            "Store a memory with the reversed version of 'hello world'", auto_save=False
        )
        assert "dlrow olleh" in response3 or "stored" in response3.lower()

    @pytest.mark.asyncio
    async def test_metadata_responses(self, memory_agent):
        """Test responses with metadata."""
        # Get response with metadata
        result = await memory_agent.arun(
            "Store a memory that I like hiking", auto_save=True, include_metadata=True
        )

        # Check metadata structure
        assert isinstance(result, dict)
        assert "response" in result
        assert "user_id" in result
        assert "timestamp" in result
        assert result["user_id"] == "test_user"

        # Verify response content
        assert "stored" in result["response"].lower()

    @pytest.mark.asyncio
    async def test_vector_store_persistence(self, memory_agent, temp_dir):
        """Test saving and loading vector store."""
        # Store some memories
        await memory_agent.arun(
            "Store a memory that my birthday is January 15th", auto_save=False
        )
        await memory_agent.arun(
            "Store a memory that I graduated from MIT", auto_save=False
        )

        # Save vector store
        save_path = Path(temp_dir) / "test_memories"
        memory_agent.save_vector_store(str(save_path))

        # Create new agent with loaded memories
        new_agent = ReactMemoryAgent(
            name="loaded_agent",
            engine=AugLLMConfig(temperature=0.1),
            user_id="test_user",
            memory_store_path=str(save_path),
        )

        # Verify memories were loaded
        response = await new_agent.arun("When is my birthday?", auto_save=False)
        assert "january" in response.lower() or "15" in response

        response2 = await new_agent.arun("Where did I graduate from?", auto_save=False)
        assert "mit" in response2.lower()

    @pytest.mark.asyncio
    async def test_complex_memory_queries(self, memory_agent):
        """Test complex multi-step memory operations."""
        # Store multiple related memories
        await memory_agent.arun(
            "Store these memories: I work as a software engineer, "
            "I specialize in machine learning, and I've been coding for 10 years",
            auto_save=False,
        )

        # Store project memories
        await memory_agent.arun(
            "Store a memory that I'm working on a recommendation system project using Python and TensorFlow",
            auto_save=False,
        )

        # Complex query combining search and reasoning
        response = await memory_agent.arun(
            "Based on my memories, what programming languages and tools am I experienced with? "
            "Also, how does my current project relate to my specialization?",
            auto_save=False,
        )

        # Should mention Python, TensorFlow, ML, and make connections
        assert any(
            term in response.lower()
            for term in ["python", "tensorflow", "machine learning", "ml"]
        )
        assert "recommendation" in response.lower() or "project" in response.lower()

    @pytest.mark.asyncio
    async def test_memory_tags_and_categories(self, memory_agent):
        """Test storing memories with tags."""
        # Store memories with tags
        response1 = await memory_agent.arun(
            'Store a memory with tags "health,exercise": I run 5 miles every morning',
            auto_save=False,
        )
        assert "stored" in response1.lower()

        response2 = await memory_agent.arun(
            'Store a memory with tags "work,skills": I am proficient in Docker and Kubernetes',
            auto_save=False,
        )
        assert "stored" in response2.lower()

        # Search for health-related memories
        response3 = await memory_agent.arun(
            "Search my memories for health and exercise information", auto_save=False
        )
        assert "run" in response3.lower() or "miles" in response3.lower()


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
