"""Memory-Aware RAG Agents.

from typing import Any
Memory-aware RAG with persistent context and iterative learning.
Uses structured output models for memory management.
"""

import logging
from datetime import datetime
from enum import Enum
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.models.llm.base import LLMConfig, OpenAILLMConfig
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.base.agent import Agent
from haive.agents.multi.base import SequentialAgent
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)


class MemoryType(str, Enum):
    """Types of memory in the system."""

    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    PROCEDURAL = "procedural"
    CONTEXTUAL = "contextual"
    FEEDBACK = "feedback"


class MemoryImportance(str, Enum):
    """Importance levels for memory items."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MemoryItem(BaseModel):
    """Individual memory item with metadata."""

    id: str = Field(description="Unique memory identifier")
    memory_type: MemoryType = Field(description="Type of memory")
    content: str = Field(description="Memory content")
    importance: MemoryImportance = Field(description="Importance level")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in this memory")
    created_at: datetime = Field(default_factory=datetime.now)
    keywords: list[str] = Field(
        default_factory=list, description="Key terms for retrieval"
    )


class MemoryRetrievalAgent(Agent):
    """Agent that retrieves relevant memories for context enhancement."""

    name: str = "Memory Retrieval"
    llm_config: LLMConfig | None = Field(default=None, description="LLM configuration")
    max_memories: int = Field(default=10, description="Maximum memories to retrieve")
    memory_store: dict = Field(default_factory=dict, description="Memory storage")

    def build_graph(self) -> BaseGraph:
        """Build memory retrieval graph."""
        graph = BaseGraph(name="MemoryRetrieval")

        def retrieve_memories(state: dict[str, Any]) -> dict[str, Any]:
            """Retrieve relevant memories for the current query."""
            query = getattr(state, "query", "")

            # Simple memory retrieval based on keyword matching
            relevant_memories = []
            query_words = set(query.lower().split())

            for memory in self.memory_store.values():
                keyword_overlap = len(
                    query_words.intersection({kw.lower() for kw in memory.keywords})
                )
                if keyword_overlap > 0:
                    score = keyword_overlap / len(query_words)
                    relevant_memories.append((memory, score))

            # Sort by relevance and take top memories
            relevant_memories.sort(key=lambda x: x[1], reverse=True)
            selected_memories = [
                mem for mem, _ in relevant_memories[: self.max_memories]
            ]

            # Format memory context
            memory_context = (
                "\n".join(
                    [
                        f"Memory ({mem.memory_type.value}): {mem.content}"
                        for mem in selected_memories
                    ]
                )
                if selected_memories
                else "No relevant memories found."
            )

            return {
                "retrieved_memories": selected_memories,
                "memory_context": memory_context,
                "memory_count": len(selected_memories),
            }

        graph.add_node("retrieve_memories", retrieve_memories)
        graph.add_edge(START, "retrieve_memories")
        graph.add_edge("retrieve_memories", END)

        return graph


class MemoryAwareRAGAgent(SequentialAgent):
    """Complete Memory-Aware RAG agent with persistent learning."""

    @classmethod
    def from_documents(
        cls,
        documents: list[Document],
        llm_config: LLMConfig | None = None,
        max_memories: int = 100,
        **kwargs,
    ):
        """Create Memory-Aware RAG agent from documents."""
        if not llm_config:
            llm_config = OpenAILLMConfig()

        # Step 1: Memory retrieval
        memory_retrieval = MemoryRetrievalAgent(
            llm_config=llm_config, max_memories=10, name="Memory Retrieval"
        )

        # Step 2: Document retrieval
        doc_retrieval = BaseRAGAgent.from_documents(
            documents=documents, name="Document Retrieval"
        )

        # Step 3: Memory integration and response
        memory_integration = SimpleAgent(
            engine=AugLLMConfig(
                **({"llm_config": llm_config} if llm_config else {}),
                prompt_template=ChatPromptTemplate.from_messages(
                    [
                        (
                            "system",
                            "You are an expert at integrating memory context with retrieved documents.",
                        ),
                        (
                            "human",
                            "Query: {query}\nMemory Context: {memory_context}\nDocuments: {retrieved_documents}\nProvide integrated response.",
                        ),
                    ]
                ),
            ),
            name="Memory Integration",
        )

        return cls(
            agents=[memory_retrieval, doc_retrieval, memory_integration],
            name=kwargs.pop("name", "Memory-Aware RAG Agent"),
            **kwargs,
        )


def create_memory_aware_rag_agent(
    documents: list[Document],
    llm_config: LLMConfig | None = None,
    memory_mode: str = "adaptive",
    **kwargs,
) -> MemoryAwareRAGAgent:
    """Create a Memory-Aware RAG agent."""
    if memory_mode == "basic":
        kwargs.setdefault("max_memories", 50)
    elif memory_mode == "comprehensive":
        kwargs.setdefault("max_memories", 200)
    else:  # adaptive
        kwargs.setdefault("max_memories", 100)

    return MemoryAwareRAGAgent.from_documents(
        documents=documents, llm_config=llm_config, **kwargs
    )


def get_memory_aware_rag_io_schema() -> dict[str, list[str]]:
    """Get I/O schema for Memory-Aware RAG agents."""
    return {
        "inputs": ["query", "conversation_history", "messages"],
        "outputs": [
            "retrieved_memories",
            "memory_context",
            "memory_count",
            "retrieved_documents",
            "response",
            "messages",
        ],
    }
