"""Haive Agents Memory System - Comprehensive long-term memory capabilities.

This module provides the complete memory system for building intelligent agents
with sophisticated memory management, classification, and retrieval capabilities.

Key Features:
    - 11 memory types (semantic, episodic, procedural, contextual, preference, etc.)
    - Automatic memory classification with LLM-based analysis
    - Enhanced self-query retriever with memory context
    - Knowledge graph generation with entity/relationship extraction
    - Graph RAG retrieval with knowledge graph integration
    - Agentic RAG coordination with intelligent strategy selection
    - Multi-agent memory coordination using MetaStateSchema patterns
    - Unified API for easy integration and usage

Phase Implementation Status:
    ✅ Phase 1: Memory Type Classification System (COMPLETE)
    ✅ Phase 2: Enhanced Self-Query with Memory Context (COMPLETE)
    ✅ Phase 3: Graph RAG implementation (COMPLETE)
    ✅ Phase 4: Multi-agent coordination (COMPLETE)
    ✅ Phase 5: Unified API integration (COMPLETE)

Usage:
    Unified Memory System (Recommended):
        >>> from haive.agents.memory import UnifiedMemorySystem, MemorySystemConfig
        >>> config = MemorySystemConfig(store_type="memory", collection_name="my_memories")
        >>> memory_system = UnifiedMemorySystem(config)
        >>> await memory_system.store_memory("Alice works at TechCorp")
        >>> result = await memory_system.retrieve_memories("Who works at TechCorp?")
        >>> kg_result = await memory_system.generate_knowledge_graph()

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

from haive.agents.memory.agentic_rag_coordinator import (
    AgenticRAGCoordinator,
    AgenticRAGCoordinatorConfig,
    AgenticRAGResult,
)

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
from haive.agents.memory.graph_rag_retriever import (
    GraphRAGResult,
    GraphRAGRetriever,
    GraphRAGRetrieverConfig,
)

# Advanced memory components (Phase 3-5)
from haive.agents.memory.kg_generator_agent import (
    KGGeneratorAgent,
    KGGeneratorAgentConfig,
    KnowledgeGraphNode,
    KnowledgeGraphRelationship,
    MemoryKnowledgeGraph,
)
from haive.agents.memory.multi_agent_coordinator import (
    MemoryAgentCapabilities,
    MemoryTask,
    MultiAgentCoordinatorConfig,
    MultiAgentMemoryCoordinator,
)

# Unified API (Phase 5 - Recommended)
from haive.agents.memory.unified_memory_api import (
    MemorySystemConfig,
    MemorySystemResult,
    UnifiedMemorySystem,
    create_memory_system,
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
    # Enhanced Retrieval System (Phase 2 ✅)
    "EnhancedMemoryRetriever",  # Memory-aware self-query retriever
    "EnhancedRetrieverConfig",  # Retriever configuration
    "EnhancedQueryResult",  # Detailed retrieval results
    "create_enhanced_memory_retriever",  # Factory function
    # Knowledge Graph Generation (Phase 3 ✅)
    "KGGeneratorAgent",  # Knowledge graph generator agent
    "KGGeneratorAgentConfig",  # KG generator configuration
    "KnowledgeGraphNode",  # KG node representation
    "KnowledgeGraphRelationship",  # KG relationship representation
    "MemoryKnowledgeGraph",  # Complete knowledge graph
    # Graph RAG Retrieval (Phase 3 ✅)
    "GraphRAGRetriever",  # Graph RAG retriever
    "GraphRAGRetrieverConfig",  # Graph RAG configuration
    "GraphRAGResult",  # Graph RAG result
    # Agentic RAG Coordination (Phase 4 ✅)
    "AgenticRAGCoordinator",  # Agentic RAG coordinator
    "AgenticRAGCoordinatorConfig",  # Agentic RAG configuration
    "AgenticRAGResult",  # Agentic RAG result
    # Multi-Agent Coordination (Phase 4 ✅)
    "MultiAgentMemoryCoordinator",  # Multi-agent coordinator
    "MultiAgentCoordinatorConfig",  # Multi-agent configuration
    "MemoryTask",  # Memory task representation
    "MemoryAgentCapabilities",  # Agent capabilities
    # Unified API (Phase 5 ✅ - Recommended)
    "UnifiedMemorySystem",  # Unified memory system
    "MemorySystemConfig",  # System configuration
    "MemorySystemResult",  # System result
    "create_memory_system",  # Factory function
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
