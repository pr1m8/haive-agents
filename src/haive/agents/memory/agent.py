"""Memory Agent - ReactAgent with long-term memory via vector store.

Extends ReactAgent with tools for saving/recalling memories across
conversations. Supports unstructured (vector) and structured (knowledge
triple) memory storage.
"""

import logging
from datetime import datetime
from typing import Any

from langchain_core.tools import StructuredTool
from langchain_core.vectorstores import VectorStore
from pydantic import Field

from haive.agents.memory.memory_utils import (
    create_memory_vectorstore,
    retrieve_memories,
    save_structured_memories,
    save_unstructured_memories,
)
from haive.agents.react.agent import ReactAgent

logger = logging.getLogger(__name__)


class MemoryAgent(ReactAgent):
    """ReactAgent with long-term memory via vector store + knowledge graph.

    Adds save_memory, recall_memories, and save_structured_memory tools
    to the standard ReactAgent tool set.
    """

    vector_store: Any = Field(default=None, description="Vector store for memory persistence")
    max_memories_per_retrieval: int = Field(default=10, description="Max memories to retrieve")
    memory_type: str = Field(default="both", description="Memory type: general, structured, both")
    current_user_id: str = Field(default="", description="Current user ID for memory scoping")

    def model_post_init(self, __context: Any) -> None:
        """Initialize vector store and memory tools after Pydantic init."""
        # Create vector store if not provided
        if self.vector_store is None:
            self.vector_store = create_memory_vectorstore()

        # Build memory tools
        self._add_memory_tools()

        super().model_post_init(__context)

    def _add_memory_tools(self) -> None:
        """Create and add memory tools to the agent's tool list."""
        vs = self.vector_store
        agent = self  # Capture for closures

        def save_memory(memory: str) -> str:
            """Save an important fact or detail about the user for future reference."""
            try:
                uid = agent._resolve_user_id()
                save_unstructured_memories([memory], vs, uid)
                return f"Memory saved: {memory}"
            except Exception as e:
                logger.exception(f"Error saving memory: {e}")
                return f"Error saving memory: {e}"

        def save_structured_memory(subject: str, predicate: str, object_: str) -> str:
            """Save a structured fact as a knowledge triple (subject, predicate, object)."""
            try:
                uid = agent._resolve_user_id()
                triple = {"subject": subject, "predicate": predicate, "object_": object_}
                save_structured_memories([triple], vs, uid)
                return f"Structured memory saved: {subject} {predicate} {object_}"
            except Exception as e:
                logger.exception(f"Error saving structured memory: {e}")
                return f"Error: {e}"

        def recall_memories(query: str) -> str:
            """Search for relevant memories about the current topic or user."""
            try:
                uid = agent._resolve_user_id()
                memories = retrieve_memories(query, vs, uid, limit=agent.max_memories_per_retrieval)
                if memories:
                    return "\n".join(f"- {m}" for m in memories)
                return "No relevant memories found."
            except Exception as e:
                logger.exception(f"Error recalling memories: {e}")
                return f"Error: {e}"

        tools = [
            StructuredTool.from_function(save_memory, name="save_memory", description=save_memory.__doc__),
            StructuredTool.from_function(recall_memories, name="recall_memories", description=recall_memories.__doc__),
        ]

        if self.memory_type in ("structured", "both"):
            tools.append(
                StructuredTool.from_function(
                    save_structured_memory,
                    name="save_structured_memory",
                    description=save_structured_memory.__doc__,
                )
            )

        # Extend existing tools
        if self.tools is None:
            self.tools = []
        self.tools.extend(tools)

    def _resolve_user_id(self) -> str:
        """Get or generate user ID for memory scoping."""
        if self.current_user_id:
            return self.current_user_id
        uid = f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.current_user_id = uid
        return uid

    class Config:
        arbitrary_types_allowed = True
