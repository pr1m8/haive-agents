"""Haive Agents Memory System - Comprehensive long-term memory capabilities.

This module provides the complete memory system for building intelligent agents
with sophisticated memory management, classification, and retrieval capabilities.

Key Features:
    - 11 memory types (semantic, episodic, procedural, contextual, preference, etc.)
    - Automatic memory classification with LLM-based analysis
    - Enhanced self-query retriever with memory context
    - Memory lifecycle management and consolidation
    - Integration with existing store tools and RAG systems

Phase Implementation Status:
    ✅ Phase 1: Memory Type Classification System (COMPLETE)
    🔄 Phase 2: Enhanced Self-Query with Memory Context (CURRENT)
    📋 Phase 3: Graph RAG implementation (PLANNED)
    📋 Phase 4: Memory consolidation agent (PLANNED)

Usage:
    Basic memory classification:
        >>> from haive.agents.memory import MemoryClassifier, MemoryType
        >>> classifier = MemoryClassifier()
        >>> result = classifier.classify_memory("I learned Python yesterday")
        >>> print(result.memory_types)  # [MemoryType.EPISODIC, MemoryType.PROCEDURAL]

    Enhanced memory retrieval:
        >>> from haive.agents.memory import create_enhanced_memory_retriever
        >>> retriever = await create_enhanced_memory_retriever(store_manager)
        >>> results = await retriever.retrieve_memories("What did I learn about Python?")
        >>> print(f"Found {len(results.memories)} relevant memories")

    Memory-aware agents:
        >>> from haive.agents.memory import MemoryStoreManager
        >>> memory_manager = MemoryStoreManager(config)
        >>> memory_id = await memory_manager.store_memory("Important fact about AI")
        >>> memories = await memory_manager.retrieve_memories("AI facts")
"""

# Core memory system components
from haive.agents.memory.core import (  # Memory types and data structures; Memory classification system; Memory storage and management
    MemoryClassificationResult,
    MemoryClassifier,
    MemoryClassifierConfig,
    MemoryConsolidationResult,
    MemoryEntry,
    MemoryImportance,
    MemoryQueryIntent,
    MemoryStoreConfig,
    MemoryStoreManager,
    MemoryType,
)

# Enhanced retrieval system (Phase 2)
from haive.agents.memory.enhanced_retriever import (
    EnhancedMemoryRetriever,
    EnhancedQueryResult,
    EnhancedRetrieverConfig,
    create_enhanced_memory_retriever,
)

# Integration with existing memory agent framework
try:
    from haive.agents.memory.agent import MemoryAgent
    from haive.agents.memory.config import MemoryAgentConfig
    from haive.agents.memory.state import MemoryAgentState

    _EXISTING_MEMORY_AVAILABLE = True
except ImportError:
    _EXISTING_MEMORY_AVAILABLE = False

__all__ = [
    # Core Memory Types and Data Structures
    "MemoryType",  # 11 memory types (semantic, episodic, etc.)
    "MemoryEntry",  # Complete memory entry with metadata
    "MemoryImportance",  # Importance classification (critical, high, etc.)
    "MemoryClassificationResult",  # Result of memory classification
    "MemoryQueryIntent",  # Query intent analysis
    "MemoryConsolidationResult",  # Memory consolidation results
    # Memory Classification System (Phase 1 ✅)
    "MemoryClassifier",  # LLM-based memory classifier
    "MemoryClassifierConfig",  # Classifier configuration
    # Memory Storage and Management (Phase 1 ✅)
    "MemoryStoreManager",  # Enhanced memory storage manager
    "MemoryStoreConfig",  # Store manager configuration
    # Enhanced Retrieval System (Phase 2 🔄)
    "EnhancedMemoryRetriever",  # Memory-aware self-query retriever
    "EnhancedRetrieverConfig",  # Retriever configuration
    "EnhancedQueryResult",  # Detailed retrieval results
    "create_enhanced_memory_retriever",  # Factory function
]

# Add existing memory components if available
if _EXISTING_MEMORY_AVAILABLE:
    __all__.extend(
        [
            "MemoryAgent",  # Existing memory agent
            "MemoryAgentConfig",  # Existing agent configuration
            "MemoryAgentState",  # Existing agent state
        ]
    )

# Memory type constants for easy access
SEMANTIC = MemoryType.SEMANTIC
EPISODIC = MemoryType.EPISODIC
PROCEDURAL = MemoryType.PROCEDURAL
CONTEXTUAL = MemoryType.CONTEXTUAL
PREFERENCE = MemoryType.PREFERENCE
META = MemoryType.META
EMOTIONAL = MemoryType.EMOTIONAL
TEMPORAL = MemoryType.TEMPORAL
ERROR = MemoryType.ERROR
FEEDBACK = MemoryType.FEEDBACK
SYSTEM = MemoryType.SYSTEM

# Quick access to all memory types
ALL_MEMORY_TYPES = list(MemoryType)
