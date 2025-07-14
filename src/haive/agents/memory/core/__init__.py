"""Haive Agents Memory Core System - Comprehensive long-term memory for agents.

This module provides the core memory system components for building
intelligent agents with long-term memory capabilities.

Key Components:
    - Memory type classification and importance scoring (11 memory types)
    - Self-query retriever with memory context
    - Memory consolidation and lifecycle management
    - Integration with existing store tools

Phase Implementation:
    Phase 1 (✅ COMPLETE): Memory Type Classification
    Phase 2 (🔄 CURRENT): Enhanced Self-Query with Memory Context
    Phase 3 (📋 PLANNED): Graph RAG implementation
    Phase 4 (📋 PLANNED): Memory consolidation agent
"""

from haive.agents.memory.core.classifier import MemoryClassifier, MemoryClassifierConfig
from haive.agents.memory.core.stores import MemoryStoreConfig, MemoryStoreManager
from haive.agents.memory.core.types import (
    MemoryClassificationResult,
    MemoryConsolidationResult,
    MemoryEntry,
    MemoryImportance,
    MemoryQueryIntent,
    MemoryType,
)

__all__ = [
    # Core memory types and data structures
    "MemoryType",
    "MemoryEntry",
    "MemoryImportance",
    "MemoryClassificationResult",
    "MemoryQueryIntent",
    "MemoryConsolidationResult",
    # Memory classification system
    "MemoryClassifier",
    "MemoryClassifierConfig",
    # Memory storage and management
    "MemoryStoreManager",
    "MemoryStoreConfig",
]
