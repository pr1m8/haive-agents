"""Memory-Aware RAG Module.

Memory-aware RAG with persistent context and iterative learning.
Uses structured output models for memory management.
"""

from haive.agents.rag.memory_aware.agent import (
    MemoryAwareRAGAgent,
    MemoryRetrievalAgent,
)

__all__ = ["MemoryAwareRAGAgent", "MemoryRetrievalAgent"]
