"""SimpleMemoryAgent that works with DeepSeek - avoiding broken imports.

This is a working version of SimpleMemoryAgent that:
1. Uses DeepSeek LLM configuration
2. Avoids the broken kg_map_merge imports
3. Implements core memory functionality
"""

import asyncio
import logging
import os
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent import SimpleAgent

# Import memory types and classes directly
from .memory_state_original import (
    EnhancedMemoryItem,
    ImportanceLevel,
    MemoryState,
    MemoryType,
    UnifiedMemoryEntry)
from .memory_state_with_tokens import MemoryStateWithTokens

logger = logging.getLogger(__name__)


class SimpleMemoryAgentDeepSeek(SimpleAgent):
    """Memory-enhanced SimpleAgent that works with DeepSeek.

    This agent provides:
    - Memory storage and retrieval
    - Token-aware memory management
    - Conversation context preservation
    - Works with DeepSeek LLM
    """

    def __init__(
        self,
        name: str = "memory_agent",
        engine: AugLLMConfig | None = None,
        user_id: str = "default_user",
        max_memories: int = 100,
        **kwargs):
        """Initialize the memory agent.

        Args:
            name: Agent name
            engine: AugLLMConfig (can use DeepSeek)
            user_id: User identifier for memories
            max_memories: Maximum memories to store
        """
        # Initialize parent SimpleAgent
        super().__init__(name=name, engine=engine, **kwargs)

        # Initialize memory state
        self.user_id = user_id
        self.memory_state = MemoryState(user_id=user_id, max_memories=max_memories)

        # Token-aware state
        self.token_state = MemoryStateWithTokens(
            messages=[], total_tokens=0, current_memories=[]
        )

        # Update system message to include memory awareness
        if self.engine and hasattr(self.engine, "system_message"):
            self.engine.system_message = (
                self.engine.system_message
                or ""
                + "\n\nYou have access to a memory system. You can store important information "
                "and retrieve it later. When asked about something, check if you have relevant "
                "memories stored."
            )

        logger.info(
            f"Initialized SimpleMemoryAgentDeepSeek: {name} for user: {user_id}"
        )

    def _classify_input(self, user_input: str) -> dict[str, Any]:
        """Classify user input to determine if it's a memory operation.

        Args:
            user_input: User's message

        Returns:
            Classification result
        """
        lower_input = user_input.lower()

        # Check if it's a memory storage request
        store_keywords = ["remember", "store", "save", "record", "note that"]
        is_store = any(keyword in lower_input for keyword in store_keywords)

        # Check if it's a memory query
        query_keywords = [
            "recall",
            "what do you remember",
            "tell me about",
            "who is",
            "what is",
        ]
        is_query = (
            any(keyword in lower_input for keyword in query_keywords)
            or "?" in user_input
        )

        # Determine memory type
        memory_type = MemoryType.CONVERSATIONAL
        if any(
            word in lower_input for word in ["fact", "is", "are", "works at", "located"]
        ):
            memory_type = MemoryType.FACTUAL

        # Determine importance
        importance = ImportanceLevel.MEDIUM
        if any(
            word in lower_input for word in ["important", "critical", "urgent", "must"]
        ):
            importance = ImportanceLevel.HIGH
        elif any(word in lower_input for word in ["minor", "trivial", "maybe"]):
            importance = ImportanceLevel.LOW

        return {
            "is_store": is_store,
            "is_query": is_query,
            "memory_type": memory_type,
            "importance": importance,
        }

    def _store_memory(
        self, content: str, memory_type: MemoryType, importance: ImportanceLevel
    ) -> str:
        """Store a memory.

        Args:
            content: Memory content
            memory_type: Type of memory
            importance: Importance level

        Returns:
            Confirmation message
        """
        memory = EnhancedMemoryItem(
            content=content,
            memory_type=memory_type,
            importance=importance,
            user_id=self.user_id)

        self.memory_state.add_memory_item(memory)

        # Also add to token state
        entry = UnifiedMemoryEntry.from_memory_item(memory)
        self.token_state.current_memories.append(entry)

        return f"I've stored that in my memory (ID: {memory.id}). Type: {memory_type.value}, Importance: {importance.value}"

    def _search_memories(self, query: str, k: int = 5) -> list[EnhancedMemoryItem]:
        """Search for relevant memories.

        Args:
            query: Search query
            k: Number of results

        Returns:
            List of relevant memories
        """
        # Simple text-based search for now
        results = self.memory_state.search_memories(query, limit=k)

        # Extract memory items
        memory_items = []
        for entry in results:
            if entry.entry_type == "memory_item" and entry.memory_item:
                memory_items.append(entry.memory_item)

        return memory_items

    def _format_memories_as_context(self, memories: list[EnhancedMemoryItem]) -> str:
        """Format memories as context for the LLM.

        Args:
            memories: List of memories

        Returns:
            Formatted context string
        """
        if not memories:
            return "No relevant memories found."

        context_parts = ["Relevant memories:"]
        for i, memory in enumerate(memories, 1):
            timestamp = (
                memory.created_at.strftime("%Y-%m-%d %H:%M")
                if memory.created_at
                else ""
            )
            context_parts.append(
                f"{i}. [{memory.memory_type.value}] {memory.content} "
                f"(importance: {memory.importance.value}, time: {timestamp})"
            )

        return "\n".join(context_parts)

    async def arun(self, user_input: str, **kwargs) -> str:
        """Process user input with memory awareness.

        Args:
            user_input: User's message
            **kwargs: Additional arguments

        Returns:
            Agent's response
        """
        # Classify the input
        classification = self._classify_input(user_input)

        # Handle memory storage
        if classification["is_store"]:
            # Extract the content to remember
            # Simple extraction - remove "remember" type keywords
            content = user_input
            for keyword in ["remember", "store", "save", "record", "note that"]:
                content = content.lower().replace(keyword, "").strip()
                content = content.replace(":", "").strip()

            # Store the memory
            result = self._store_memory(
                content, classification["memory_type"], classification["importance"]
            )

            # Also process with LLM for natural response
            response = await super().arun(user_input, **kwargs)
            return f"{result}\n\n{response}"

        # Handle memory queries
        if classification["is_query"]:
            # Search for relevant memories
            memories = self._search_memories(user_input)
            context = self._format_memories_as_context(memories)

            # Add context to the query
            enhanced_input = f"{context}\n\nUser question: {user_input}"

            # Process with LLM
            response = await super().arun(enhanced_input, **kwargs)
            return response

        # Normal processing
        # Check if we should add any context
        memories = self._search_memories(user_input, k=3)
        if memories:
            context = self._format_memories_as_context(memories)
            enhanced_input = f"Context from memory:\n{context}\n\nUser: {user_input}"
            return await super().arun(enhanced_input, **kwargs)
        return await super().arun(user_input, **kwargs)

    def get_memory_stats(self) -> dict[str, Any]:
        """Get memory statistics.

        Returns:
            Memory statistics
        """
        return {
            "total_memories": self.memory_state.stats.total_memories,
            "memories_by_type": dict(self.memory_state.stats.memories_by_type),
            "memories_by_importance": dict(
                self.memory_state.stats.memories_by_importance
            ),
            "user_id": self.user_id,
        }


async def test_with_deepseek():
    """Test the agent with DeepSeek configuration."""
    # Create DeepSeek configuration

    deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)

    aug_config = AugLLMConfig(
        llm_config=deepseek_config,
        system_message="You are a helpful assistant with memory capabilities.")

    # Create agent
    agent = SimpleMemoryAgentDeepSeek(
        name="deepseek_memory", engine=aug_config, user_id="test_user"
    )

    # Test interactions
    test_inputs = [
        "Remember: Alice Johnson is a senior AI researcher at TechCorp.",
        "Remember: Bob Smith is the CTO of DataCorp.",
        "Important: Meeting with Alice scheduled for Monday at 2 PM.",
        "Who is Alice?",
        "What do you know about Bob?",
        "When is my meeting?",
    ]

    for user_input in test_inputs:
        await agent.arun(user_input)

    # Show stats
    stats = agent.get_memory_stats()
    for _key, _value in stats.items():
        pass


if __name__ == "__main__":

    # Set DeepSeek API key if needed
    if not os.getenv("DEEPSEEK_API_KEY"):
        os.environ["DEEPSEEK_API_KEY"] = "test-key-replace-with-real"

    asyncio.run(test_with_deepseek())
