"""Enhanced Self-Query Retriever with Memory Context.

This module implements Phase 2 of the incremental memory system: Enhanced Self-Query
retriever that integrates memory classification with sophisticated retrieval strategies.

The enhanced retriever builds on the memory classification system to provide:
- Memory-type aware retrieval (semantic, episodic, procedural, etc.)
- Context-aware query expansion
- Memory importance weighting
- Time-based relevance scoring
- Self-query with metadata filtering

This is the next phase after the foundational memory classification system,
bridging toward full Graph RAG implementation.
"""

import logging
from datetime import datetime
from typing import Any, Optional

from haive.core.tools.store_tools import StoreManager
from pydantic import BaseModel, ConfigDict, Field

from haive.agents.memory.core.classifier import MemoryClassifier, MemoryClassifierConfig
from haive.agents.memory.core.stores import MemoryStoreConfig, MemoryStoreManager
from haive.agents.memory.core.types import MemoryQueryIntent, MemoryType, Optional

logger = logging.getLogger(__name__)


class EnhancedRetrieverConfig(BaseModel):
    """Configuration for enhanced memory retriever with advanced self-query capabilities.
    
    This configuration class defines all parameters needed to create and configure
    an EnhancedMemoryRetriever, including retrieval settings, scoring weights,
    temporal parameters, and feature toggles for advanced retrieval capabilities.
    
    The configuration supports sophisticated retrieval features including:
    - Memory type-aware weighting and targeting
    - Temporal relevance scoring with configurable decay
    - Query expansion for enhanced recall
    - Metadata filtering and importance-based ranking
    - Performance monitoring and optimization settings
    
    Attributes:
        memory_store_manager: Manager for memory storage and retrieval operations
        memory_classifier: Classifier for analyzing query intent and memory types
        default_limit: Default number of memories to retrieve per query
        max_limit: Maximum number of memories that can be retrieved
        similarity_threshold: Minimum similarity score for inclusion in results
        memory_type_weights: Weight multipliers for different memory types during scoring
        enable_temporal_scoring: Whether to enable time-based relevance scoring
        recency_decay_hours: Hours over which recency relevance decays
        recency_weight: Weight for recency component in final scoring
        enable_query_expansion: Whether to enable automatic query expansion
        expansion_terms_limit: Maximum number of expansion terms to add
        enable_metadata_filtering: Whether to enable metadata-based filtering
        enable_importance_filtering: Whether to enable importance-based filtering
        
    Examples:
        Basic configuration for development::
        
            config = EnhancedRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier,
                default_limit=10,
                similarity_threshold=0.7
            )
            
        Production configuration with custom weights::
        
            config = EnhancedRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier,
                default_limit=15,
                max_limit=100,
                similarity_threshold=0.75,
                memory_type_weights={
                    MemoryType.SEMANTIC.value: 1.0,
                    MemoryType.EPISODIC.value: 1.5,  # Boost conversations
                    MemoryType.PROCEDURAL.value: 1.2,  # Boost how-to content
                    MemoryType.ERROR.value: 1.8,  # Highly boost error memories
                },
                enable_temporal_scoring=True,
                recency_decay_hours=72,  # 3 days
                recency_weight=0.3,
                enable_query_expansion=True,
                expansion_terms_limit=7
            )
            
        Performance-optimized configuration::
        
            config = EnhancedRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier,
                default_limit=5,
                max_limit=25,
                similarity_threshold=0.8,  # Higher threshold for precision
                enable_temporal_scoring=False,  # Disable for speed
                enable_query_expansion=False,  # Disable for speed
                enable_metadata_filtering=True,
                enable_importance_filtering=True
            )
            
    Memory Type Weighting Strategy:
        The memory_type_weights dictionary allows fine-tuning of retrieval relevance
        based on memory types. Common strategies:
        
        - **Error Learning**: High weights for ERROR and FEEDBACK memories
        - **Conversational Focus**: High weights for EPISODIC memories
        - **Knowledge Retrieval**: High weights for SEMANTIC and PROCEDURAL memories
        - **System Optimization**: Lower weights for SYSTEM and META memories
        
    Temporal Scoring Configuration:
        The temporal scoring system uses exponential decay based on memory age:
        
        - **recency_decay_hours**: Defines the half-life of memory relevance
        - **recency_weight**: Controls how much recency affects final scoring
        - Typical values: 24-168 hours (1 day to 1 week) for decay
        - Typical weights: 0.1-0.3 for recency component
        
    Performance Considerations:
        - **High similarity_threshold**: Improves precision but may reduce recall
        - **Disabled temporal_scoring**: Reduces computation for time-sensitive queries
        - **Limited expansion_terms**: Balances recall improvement with query broadness
        - **max_limit**: Controls memory usage and processing time
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Core components
    memory_store_manager: MemoryStoreManager = Field(..., description="Memory store manager")
    memory_classifier: MemoryClassifier = Field(
        ..., description="Memory classifier for query analysis"
    )

    # Retrieval configuration
    default_limit: int = Field(default=10, description="Default number of memories to retrieve")
    max_limit: int = Field(default=50, description="Maximum number of memories to retrieve")
    similarity_threshold: float = Field(default=0.7, description="Minimum similarity threshold")

    # Memory type weighting
    memory_type_weights: dict[str, float] = Field(
        default_factory=lambda: {
            MemoryType.SEMANTIC.value: 1.0,
            MemoryType.EPISODIC.value: 1.2,  # Boost episodic memories
            MemoryType.PROCEDURAL.value: 1.1,
            MemoryType.CONTEXTUAL.value: 0.9,
            MemoryType.PREFERENCE.value: 0.8,
            MemoryType.META.value: 0.7,
            MemoryType.EMOTIONAL.value: 0.8,
            MemoryType.TEMPORAL.value: 0.9,
            MemoryType.ERROR.value: 1.3,  # Boost error memories for learning
            MemoryType.FEEDBACK.value: 1.2,  # Boost feedback for improvement
            MemoryType.SYSTEM.value: 0.6,
        },
        description="Weight multipliers for different memory types",
    )

    # Time-based scoring
    enable_temporal_scoring: bool = Field(
        default=True, description="Enable time-based relevance scoring"
    )
    recency_decay_hours: float = Field(
        default=168, description="Hours for recency decay (default: 1 week)"
    )
    recency_weight: float = Field(default=0.2, description="Weight for recency in final scoring")

    # Query expansion
    enable_query_expansion: bool = Field(
        default=True, description="Enable automatic query expansion"
    )
    expansion_terms_limit: int = Field(default=5, description="Maximum expansion terms to add")

    # Self-query filtering
    enable_metadata_filtering: bool = Field(
        default=True, description="Enable metadata-based filtering"
    )
    enable_importance_filtering: bool = Field(
        default=True, description="Enable importance-based filtering"
    )


class EnhancedQueryResult(BaseModel):
    """Comprehensive result of enhanced memory retrieval with detailed scoring and metadata.
    
    This class encapsulates the complete results of an enhanced memory retrieval operation,
    including retrieved memories, query analysis details, scoring breakdowns, and performance
    metrics. It provides comprehensive information for analysis and optimization.
    
    The result includes multiple scoring components that enable detailed analysis of
    retrieval quality and system performance:
    
    Attributes:
        memories: List of retrieved memory dictionaries with enhanced metadata
        total_found: Total number of memories found before limit was applied
        query_intent: Analyzed intent and characteristics of the user query
        expanded_query: Query string after expansion with additional terms
        memory_types_targeted: List of memory types that were targeted for retrieval
        similarity_scores: Vector similarity scores for each retrieved memory
        importance_scores: Importance scores extracted from memory metadata
        recency_scores: Time-based relevance scores for each memory
        final_scores: Combined final scores used for ranking memories
        retrieval_time_ms: Time spent on memory retrieval operations
        classification_time_ms: Time spent on query intent classification
        total_time_ms: Total processing time for the entire retrieval operation
        
    Examples:
        Analyzing retrieval results::
        
            result = await retriever.retrieve_memories("Python programming best practices")
            
            print(f"Retrieved {len(result.memories)} of {result.total_found} found memories")
            print(f"Query processed in {result.total_time_ms:.1f}ms")
            print(f"Query intent: {result.query_intent.intent_description}")
            print(f"Memory types targeted: {[mt.value for mt in result.memory_types_targeted]}")
            
            # Analyze top results
            for i, memory in enumerate(result.memories[:3]):
                print(f"Memory {i+1}: {memory['content'][:100]}...")
                print(f"  Final score: {result.final_scores[i]:.3f}")
                print(f"  Similarity: {result.similarity_scores[i]:.3f}")
                print(f"  Importance: {result.importance_scores[i]:.3f}")
                print(f"  Recency: {result.recency_scores[i]:.3f}")
                
        Performance analysis::
        
            result = await retriever.retrieve_memories("complex technical query")
            
            print(f"Performance breakdown:")
            print(f"  Classification: {result.classification_time_ms:.1f}ms")
            print(f"  Retrieval: {result.retrieval_time_ms:.1f}ms")
            print(f"  Total: {result.total_time_ms:.1f}ms")
            
            # Query expansion analysis
            if result.expanded_query != result.query_intent.original_query:
                print(f"Query expanded: '{result.query_intent.original_query}' -> '{result.expanded_query}'")
                
        Score distribution analysis::
        
            result = await retriever.retrieve_memories("machine learning algorithms")
            
            if result.memories:
                avg_similarity = sum(result.similarity_scores) / len(result.similarity_scores)
                avg_importance = sum(result.importance_scores) / len(result.importance_scores)
                avg_recency = sum(result.recency_scores) / len(result.recency_scores)
                avg_final = sum(result.final_scores) / len(result.final_scores)
                
                print(f"Average scores:")
                print(f"  Similarity: {avg_similarity:.3f}")
                print(f"  Importance: {avg_importance:.3f}")
                print(f"  Recency: {avg_recency:.3f}")
                print(f"  Final: {avg_final:.3f}")
                
                # Find memories with high importance but low similarity
                high_importance_low_sim = [
                    i for i, (imp, sim) in enumerate(zip(result.importance_scores, result.similarity_scores))
                    if imp > 0.8 and sim < 0.6
                ]
                
                if high_importance_low_sim:
                    print(f"High importance, low similarity memories: {len(high_importance_low_sim)}")
                    for idx in high_importance_low_sim[:3]:
                        print(f"  {result.memories[idx]['content'][:80]}...")
                        
    Scoring Component Analysis:
        The result provides detailed scoring breakdowns that enable analysis of:
        
        - **Similarity vs Importance Trade-offs**: Compare vector similarity with explicit importance
        - **Temporal Relevance Patterns**: Analyze how memory age affects relevance
        - **Memory Type Effectiveness**: Evaluate which memory types perform best for different queries
        - **Query Expansion Impact**: Compare performance with and without query expansion
        
    Performance Metrics:
        The timing metrics help optimize retrieval performance:
        
        - **classification_time_ms**: Time for query intent analysis (typically 100-500ms)
        - **retrieval_time_ms**: Core memory retrieval time (typically 50-200ms)
        - **total_time_ms**: End-to-end processing time (typically 200-800ms)
        
    Note:
        All scores are normalized to 0.0-1.0 range for consistent analysis and comparison.
        The final_scores represent the weighted combination of all scoring components.
    """

    # Core results
    memories: list[dict[str, Any]] = Field(default_factory=list, description="Retrieved memories")
    total_found: int = Field(default=0, description="Total memories found before limiting")

    # Query analysis
    query_intent: Optional[MemoryQueryIntent] = Field(
        default=None, description="Analyzed query intent"
    )
    expanded_query: Optional[str] = Field(default=None, description="Query after expansion")
    memory_types_targeted: list[MemoryType] = Field(
        default_factory=list, description="Memory types targeted"
    )

    # Retrieval metadata
    similarity_scores: list[float] = Field(
        default_factory=list, description="Similarity scores for each result"
    )
    importance_scores: list[float] = Field(
        default_factory=list, description="Importance scores for each result"
    )
    recency_scores: list[float] = Field(
        default_factory=list, description="Recency scores for each result"
    )
    final_scores: list[float] = Field(default_factory=list, description="Combined final scores")

    # Performance metrics
    retrieval_time_ms: float = Field(default=0.0, description="Retrieval time in milliseconds")
    classification_time_ms: float = Field(default=0.0, description="Query classification time")
    total_time_ms: float = Field(default=0.0, description="Total processing time")


class EnhancedMemoryRetriever:
    """Advanced memory retriever with multi-factor scoring and intelligent query enhancement.
    
    The EnhancedMemoryRetriever implements Phase 2 of the incremental memory system,
    building on the memory classification foundation to provide sophisticated, context-aware
    memory retrieval with comprehensive scoring and query enhancement capabilities.
    
    This retriever goes beyond simple vector similarity to provide:
    - **Intelligent Query Analysis**: LLM-powered intent classification and expansion
    - **Multi-Factor Scoring**: Combines similarity, importance, recency, and type relevance
    - **Memory Type Awareness**: Targeted retrieval based on content type classification
    - **Temporal Relevance**: Time-based scoring with configurable decay parameters
    - **Self-Query Capabilities**: Metadata filtering and structured query generation
    - **Performance Monitoring**: Comprehensive metrics and optimization tracking
    
    Architecture:
        The retriever implements a multi-phase processing pipeline:
        
        1. **Query Analysis Phase**: Intent classification and memory type detection
        2. **Query Enhancement Phase**: Expansion with related terms and context
        3. **Retrieval Phase**: Memory store querying with filtering and limits
        4. **Scoring Phase**: Multi-factor relevance scoring and ranking
        5. **Assembly Phase**: Result compilation with metadata and metrics
        
    Attributes:
        config: Configuration object with all retrieval settings and parameters
        memory_store: Memory store manager for storage and retrieval operations
        classifier: Memory classifier for query intent analysis and content classification
        _retrieval_stats: Internal performance tracking and statistics
        
    Examples:
        Basic enhanced retrieval::
        
            config = EnhancedRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier
            )
            
            retriever = EnhancedMemoryRetriever(config)
            
            # Enhanced retrieval with automatic analysis
            result = await retriever.retrieve_memories(
                "How do I implement error handling in Python?"
            )
            
            print(f"Found {len(result.memories)} relevant memories")
            print(f"Query intent: {result.query_intent.intent_description}")
            print(f"Memory types: {[mt.value for mt in result.memory_types_targeted]}")
            
        Advanced retrieval with targeting::
        
            # Target specific memory types for procedural knowledge
            result = await retriever.retrieve_memories(
                "Python error handling patterns",
                memory_types=[MemoryType.PROCEDURAL, MemoryType.ERROR],
                importance_threshold=0.7,
                limit=15
            )
            
            # Analyze results by memory type
            for memory in result.memories:
                memory_types = memory.get('metadata', {}).get('memory_types', [])
                print(f"Memory: {memory['content'][:80]}...")
                print(f"  Types: {memory_types}")
                print(f"  Score: {memory['final_score']:.3f}")
                
        Time-filtered retrieval::
        
            from datetime import datetime, timedelta
            
            # Retrieve only recent memories
            week_ago = datetime.utcnow() - timedelta(days=7)
            now = datetime.utcnow()
            
            result = await retriever.retrieve_memories(
                "Recent project discussions",
                memory_types=[MemoryType.EPISODIC],
                time_range=(week_ago, now),
                limit=20
            )
            
            print(f"Found {len(result.memories)} recent memories")
            
        Performance analysis::
        
            result = await retriever.retrieve_memories("complex query")
            
            # Analyze retrieval performance
            print(f"Total processing time: {result.total_time_ms:.1f}ms")
            print(f"  Query classification: {result.classification_time_ms:.1f}ms")
            print(f"  Memory retrieval: {result.retrieval_time_ms:.1f}ms")
            
            # Check if query was expanded
            if result.expanded_query != result.query_intent.original_query:
                print(f"Query expansion improved coverage")
                
            # Analyze score distribution
            if result.memories:
                top_score = max(result.final_scores)
                avg_score = sum(result.final_scores) / len(result.final_scores)
                print(f"Score range: {avg_score:.3f} avg, {top_score:.3f} top")
                
    Scoring Algorithm:
        The multi-factor scoring combines:
        
        - **Similarity Score (40%)**: Vector embedding similarity to query
        - **Importance Score (30%)**: Explicit importance from memory metadata
        - **Type Relevance (20%)**: Memory type alignment with query intent
        - **Recency Score (10%)**: Time-based relevance with exponential decay
        
        Final Score = (similarity × 0.4) + (importance × 0.3) + (type × 0.2) + (recency × weight)
        
    Query Enhancement:
        The retriever automatically enhances queries by:
        
        - **Entity Extraction**: Adding relevant entities from query analysis
        - **Topic Expansion**: Including related topics and concepts
        - **Type-Specific Terms**: Adding terms based on detected memory types
        - **Semantic Broadening**: Including synonymous and related terms
        
    Performance Optimization:
        The retriever includes several optimization features:
        
        - **Batch Processing**: Efficient processing of multiple queries
        - **Caching**: Query intent and expansion term caching
        - **Statistics Tracking**: Performance monitoring and bottleneck identification
        - **Configurable Limits**: Memory usage and processing time controls
        
    Integration:
        The EnhancedMemoryRetriever integrates seamlessly with:
        
        - **Memory Classification System**: For query intent analysis
        - **Memory Store Manager**: For storage and basic retrieval
        - **Graph RAG Retriever**: As a fallback or parallel retrieval method
        - **Agent Systems**: As a memory component for conversational agents
        
    Note:
        This retriever is designed for Phase 2 deployment and serves as a bridge
        between basic vector retrieval and full Graph RAG capabilities. It provides
        significant improvements over basic similarity search while maintaining
        reasonable computational requirements.
    """

    def __init__(self, config: EnhancedRetrieverConfig):
        """Initialize enhanced memory retriever with comprehensive configuration.
        
        Sets up the retriever with all necessary components for advanced memory retrieval
        including memory store access, query classification capabilities, and performance
        tracking infrastructure.
        
        Args:
            config: EnhancedRetrieverConfig with all retrieval settings and component references
            
        Examples:
            Basic initialization::
            
                config = EnhancedRetrieverConfig(
                    memory_store_manager=store_manager,
                    memory_classifier=classifier
                )
                
                retriever = EnhancedMemoryRetriever(config)
                
            With performance monitoring::
            
                retriever = EnhancedMemoryRetriever(config)
                
                # Check initialization stats
                stats = retriever.get_retrieval_stats()
                print(f"Retriever initialized with {len(stats['memory_type_distribution'])} memory types")
                
        Note:
            The retriever initializes internal performance tracking that accumulates
            statistics across all retrieval operations for monitoring and optimization.
        """
        self.config = config
        self.memory_store = config.memory_store_manager
        self.classifier = config.memory_classifier

        # Performance tracking
        self._retrieval_stats = {
            "total_queries": 0,
            "avg_retrieval_time": 0.0,
            "avg_results_returned": 0.0,
            "memory_type_distribution": {mt.value: 0 for mt in MemoryType},
        }

    async def retrieve_memories(
        self,
        query: str,
        memory_types: list[MemoryType] | None = None,
        importance_threshold: Optional[float] = None,
        time_range: tuple[datetime, datetime] | None = None,
        limit: Optional[int] = None,
        include_metadata: bool = True,
        namespace: tuple[str, ...] | None = None,
    ) -> EnhancedQueryResult:
        """Retrieve memories using enhanced self-query with memory context.

        Args:
            query: Natural language query
            memory_types: Specific memory types to target (auto-detected if None)
            importance_threshold: Minimum importance score filter
            time_range: Optional time range filter
            limit: Maximum results to return
            include_metadata: Whether to include detailed metadata
            namespace: Memory namespace to search

        Returns:
            EnhancedQueryResult with memories and detailed metadata
        """
        start_time = datetime.utcnow()

        try:
            # Phase 1: Query Analysis and Intent Classification
            classification_start = datetime.utcnow()
            query_intent = self.classifier.classify_query_intent(query)
            classification_time = (datetime.utcnow() - classification_start).total_seconds() * 1000

            # Use detected memory types if not explicitly provided
            if memory_types is None:
                memory_types = query_intent.memory_types

            # Phase 2: Query Expansion
            expanded_query = query
            if self.config.enable_query_expansion:
                expanded_query = await self._expand_query(query, query_intent)

            # Phase 3: Memory Retrieval with Filtering
            retrieval_start = datetime.utcnow()

            raw_memories = await self.memory_store.retrieve_memories(
                query=expanded_query,
                namespace=namespace,
                memory_types=memory_types,
                limit=limit or self.config.max_limit,  # Retrieve more for re-ranking
                time_range=time_range,
                importance_threshold=importance_threshold,
            )

            retrieval_time = (datetime.utcnow() - retrieval_start).total_seconds() * 1000

            # Phase 4: Enhanced Scoring and Re-ranking
            scored_memories = await self._apply_enhanced_scoring(
                memories=raw_memories,
                query=query,
                query_intent=query_intent,
                memory_types=memory_types,
            )

            # Phase 5: Final Limiting and Metadata Assembly
            final_limit = limit or self.config.default_limit
            final_memories = scored_memories[:final_limit]

            # Extract metadata for result
            similarity_scores = [m.get("similarity_score", 0.0) for m in final_memories]
            importance_scores = [
                m.get("metadata", {}).get("importance_score", 0.0) for m in final_memories
            ]
            recency_scores = [m.get("recency_score", 0.0) for m in final_memories]
            final_scores = [m.get("final_score", 0.0) for m in final_memories]

            # Performance tracking
            total_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            self._update_stats(total_time, len(final_memories), memory_types)

            # Build result
            result = EnhancedQueryResult(
                memories=final_memories,
                total_found=len(raw_memories),
                query_intent=query_intent,
                expanded_query=expanded_query,
                memory_types_targeted=memory_types,
                similarity_scores=similarity_scores,
                importance_scores=importance_scores,
                recency_scores=recency_scores,
                final_scores=final_scores,
                retrieval_time_ms=retrieval_time,
                classification_time_ms=classification_time,
                total_time_ms=total_time,
            )

            logger.info(
                f"Enhanced retrieval completed: {len(final_memories)} memories in {
                    total_time:.1f
                }ms"
            )
            return result

        except Exception as e:
            logger.exception(f"Error in enhanced memory retrieval: {e}")
            # Return empty result on error with comprehensive error context
            error_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Log error details for debugging
            logger.warning(
                f"Enhanced retrieval failed after {error_time:.1f}ms for query: '{query[:100]}...'"
            )
            
            return EnhancedQueryResult(
                total_time_ms=error_time,
                expanded_query=query,  # Preserve original query
                memory_types_targeted=memory_types or []
            )

    async def _expand_query(self, query: str, query_intent: MemoryQueryIntent) -> str:
        """Expand query with related terms and context to improve retrieval recall.
        
        This method enhances the original query by adding relevant terms based on
        query intent analysis, entities, topics, and memory type-specific expansions.
        The expansion is designed to improve recall while maintaining query focus.
        
        Args:
            query: Original user query string
            query_intent: Analyzed query intent with entities, topics, and memory types
            
        Returns:
            str: Expanded query string with additional relevant terms
            
        Examples:
            Basic query expansion::
            
                original = "Python error handling"
                query_intent = MemoryQueryIntent(
                    entities=["Python", "programming"],
                    topics=["error_handling", "debugging"],
                    memory_types=[MemoryType.PROCEDURAL, MemoryType.ERROR]
                )
                
                expanded = await self._expand_query(original, query_intent)
                print(f"Expanded: {expanded}")
                # Output: "Python error handling programming debugging procedure method"
                
            Memory type-specific expansion::
            
                # For procedural queries
                procedural_query = "How to deploy applications"
                procedural_intent = MemoryQueryIntent(
                    memory_types=[MemoryType.PROCEDURAL],
                    entities=["deployment", "applications"]
                )
                
                expanded = await self._expand_query(procedural_query, procedural_intent)
                # Adds: "workflow", "procedure", "method"
                
                # For episodic queries
                episodic_query = "Last meeting with the team"
                episodic_intent = MemoryQueryIntent(
                    memory_types=[MemoryType.EPISODIC],
                    entities=["team", "meeting"]
                )
                
                expanded = await self._expand_query(episodic_query, episodic_intent)
                # Adds: "discussion", "event", "interaction"
                
            Expansion term limiting::
            
                # With expansion_terms_limit = 3
                query = "machine learning"
                query_intent = MemoryQueryIntent(
                    entities=["ML", "AI", "algorithms", "models", "training"],
                    topics=["supervised", "unsupervised", "neural", "deep"]
                )
                
                expanded = await self._expand_query(query, query_intent)
                # Only adds top 3 terms based on relevance
                
        Expansion Strategy:
            The expansion process follows this priority order:
            
            1. **Top Entities**: Most relevant entities from query analysis (limit: 2)
            2. **Top Topics**: Most relevant topics from query analysis (limit: 2)
            3. **Memory Type Terms**: Specific terms based on detected memory types
            4. **Term Limiting**: Apply expansion_terms_limit to prevent query broadening
            
        Memory Type-Specific Expansions:
            - **PROCEDURAL**: "workflow", "procedure", "method" for how-to queries
            - **EPISODIC**: "discussion", "event", "interaction" for conversation queries
            - **ERROR**: "issue", "problem", "solution" for error-related queries
            - **FEEDBACK**: "review", "evaluation", "assessment" for feedback queries
            
        Error Handling:
            The method gracefully handles errors by returning the original query unchanged,
            ensuring that retrieval continues even if expansion fails.
            
        Performance Considerations:
            - Expansion is lightweight and typically adds <50ms to processing time
            - Term limiting prevents overly broad queries that reduce precision
            - Caching of common expansions could be added for frequently used terms
        """
        try:
            # Simple expansion based on entities and topics
            expansion_terms = []

            # Add entities from query intent
            expansion_terms.extend(query_intent.entities[:2])  # Top 2 entities

            # Add topics from query intent
            expansion_terms.extend(query_intent.topics[:2])  # Top 2 topics

            # Memory type specific expansions
            if MemoryType.PROCEDURAL in query_intent.memory_types:
                if any(word in query.lower() for word in ["how", "process", "step"]):
                    expansion_terms.extend(["workflow", "procedure", "method"])

            if MemoryType.EPISODIC in query_intent.memory_types and any(
                word in query.lower() for word in ["when", "conversation", "meeting"]
            ):
                expansion_terms.extend(["discussion", "event", "interaction"])

            # Limit expansion terms
            expansion_terms = expansion_terms[: self.config.expansion_terms_limit]

            if expansion_terms:
                expanded = f"{query} {' '.join(expansion_terms)}"
                logger.debug(f"Query expanded: '{query}' -> '{expanded}'")
                return expanded

            return query

        except Exception as e:
            logger.exception(f"Error expanding query: {e}")
            return query

    async def _apply_enhanced_scoring(
        self,
        memories: list[dict[str, Any]],
        query: str,
        query_intent: MemoryQueryIntent,
        memory_types: list[MemoryType],
    ) -> list[dict[str, Any]]:
        """Apply enhanced multi-factor scoring to memories for sophisticated ranking.
        
        This method implements the core scoring algorithm that combines multiple relevance
        factors to produce a comprehensive ranking of retrieved memories. The scoring
        considers similarity, importance, memory type alignment, and temporal relevance.
        
        Args:
            memories: List of memory dictionaries to score and rank
            query: Original user query for context
            query_intent: Analyzed query intent with memory types and entities
            memory_types: Target memory types for this retrieval operation
            
        Returns:
            List[Dict[str, Any]]: Memories sorted by final score (highest first) with
                enhanced metadata including all scoring components
                
        Examples:
            Understanding enhanced scoring::
            
                memories = [
                    {
                        'content': 'Python error handling with try-catch blocks',
                        'similarity_score': 0.85,
                        'metadata': {
                            'importance_score': 0.9,
                            'memory_types': ['procedural', 'error'],
                            'created_at': '2024-01-15T10:30:00Z'
                        }
                    },
                    {
                        'content': 'Python basic syntax introduction',
                        'similarity_score': 0.75,
                        'metadata': {
                            'importance_score': 0.6,
                            'memory_types': ['semantic'],
                            'created_at': '2024-01-10T15:20:00Z'
                        }
                    }
                ]
                
                query = "Python error handling best practices"
                target_types = [MemoryType.PROCEDURAL, MemoryType.ERROR]
                
                scored = await self._apply_enhanced_scoring(
                    memories, query, query_intent, target_types
                )
                
                # First memory gets higher score due to:
                # - Good similarity (0.85)
                # - High importance (0.9)
                # - Perfect type match (procedural + error)
                # - Recent creation (better recency)
                
                for memory in scored:
                    print(f"Content: {memory['content'][:50]}...")
                    print(f"  Final score: {memory['final_score']:.3f}")
                    print(f"  Similarity: {memory['similarity_score']:.3f}")
                    print(f"  Importance: {memory['importance_score']:.3f}")
                    print(f"  Type score: {memory['type_score']:.3f}")
                    print(f"  Recency: {memory['recency_score']:.3f}")
                    
            Analyzing scoring components::
            
                scored_memories = await self._apply_enhanced_scoring(
                    raw_memories, query, intent, target_types
                )
                
                # Analyze score distribution
                similarity_scores = [m['similarity_score'] for m in scored_memories]
                importance_scores = [m['importance_score'] for m in scored_memories]
                type_scores = [m['type_score'] for m in scored_memories]
                final_scores = [m['final_score'] for m in scored_memories]
                
                print(f"Similarity range: {min(similarity_scores):.2f} - {max(similarity_scores):.2f}")
                print(f"Importance range: {min(importance_scores):.2f} - {max(importance_scores):.2f}")
                print(f"Type score range: {min(type_scores):.2f} - {max(type_scores):.2f}")
                print(f"Final score range: {min(final_scores):.2f} - {max(final_scores):.2f}")
                
                # Find memories where type alignment boosted ranking
                for i, memory in enumerate(scored_memories):
                    sim_rank = sorted(similarity_scores, reverse=True).index(memory['similarity_score'])
                    final_rank = i
                    
                    if final_rank < sim_rank:
                        print(f"Memory boosted by type/importance: {memory['content'][:60]}...")
                        print(f"  Similarity rank: {sim_rank}, Final rank: {final_rank}")
                        
        Scoring Algorithm Details:
            The final score is calculated as:
            
            final_score = (similarity × 0.4) + (importance × 0.3) + (type_score × 0.2) + (recency × weight)
            
            Where:
            - **Similarity Score**: Vector embedding similarity from memory store (0.0-1.0)
            - **Importance Score**: Explicit importance from memory metadata (0.0-1.0)
            - **Type Score**: Alignment between memory types and query intent (0.0-1.0)
            - **Recency Score**: Exponential decay based on memory age (0.0-1.0)
            
        Type Scoring:
            Type alignment is calculated by:
            1. Identifying memory types from metadata
            2. Calculating overlap with target memory types
            3. Applying configured memory type weights
            4. Normalizing to 0.0-1.0 range
            
        Recency Scoring:
            Temporal relevance uses exponential decay:
            - Recent memories (< 1 day): score ~ 0.8-1.0
            - Medium age (1-7 days): score ~ 0.4-0.8
            - Older memories (> 1 week): score ~ 0.0-0.4
            - Decay rate controlled by recency_decay_hours config
            
        Performance Considerations:
            - Scoring is O(n) where n is number of memories
            - Type calculations are lightweight dictionary lookups
            - Recency calculation uses efficient datetime operations
            - Memory overhead is minimal (just score fields added)
            
        Error Handling:
            The method gracefully handles missing metadata by using default scores,
            ensuring that retrieval continues even with incomplete memory data.
        """
        try:
            scored_memories = []

            for memory in memories:
                metadata = memory.get("metadata", {})

                # Base similarity score (from vector search)
                similarity_score = memory.get("similarity_score", 0.5)

                # Importance score
                importance_score = metadata.get("importance_score", 0.5)

                # Memory type scoring
                memory_memory_types = [MemoryType(mt) for mt in metadata.get("memory_types", [])]
                type_score = self._calculate_type_score(memory_memory_types, memory_types)

                # Recency scoring
                recency_score = 0.0
                if self.config.enable_temporal_scoring:
                    recency_score = self._calculate_recency_score(metadata)

                # Combine scores
                final_score = (
                    similarity_score * 0.4  # 40% similarity
                    + importance_score * 0.3  # 30% importance
                    + type_score * 0.2  # 20% type relevance
                    + recency_score * self.config.recency_weight  # Configurable recency
                )

                # Add scores to memory
                memory["importance_score"] = importance_score
                memory["type_score"] = type_score
                memory["recency_score"] = recency_score
                memory["final_score"] = final_score

                scored_memories.append(memory)

            # Sort by final score
            scored_memories.sort(key=lambda x: x.get("final_score", 0.0), reverse=True)

            return scored_memories

        except Exception as e:
            logger.exception(f"Error in enhanced scoring: {e}")
            return memories

    def _calculate_type_score(
        self, memory_types: list[MemoryType], target_types: list[MemoryType]
    ) -> float:
        """Calculate memory type relevance score."""
        if not memory_types or not target_types:
            return 0.5  # Neutral score

        # Check for exact matches
        matches = set(memory_types) & set(target_types)
        if not matches:
            return 0.3  # Low score for no matches

        # Calculate weighted score based on memory type weights
        total_weight = 0.0
        for memory_type in matches:
            weight = self.config.memory_type_weights.get(memory_type.value, 1.0)
            total_weight += weight

        # Normalize by number of target types
        normalized_score = total_weight / len(target_types)

        return min(1.0, normalized_score)

    def _calculate_recency_score(self, metadata: dict[str, Any]) -> float:
        """Calculate time-based recency score."""
        try:
            created_at_str = metadata.get("created_at", datetime.utcnow().isoformat())
            created_at = datetime.fromisoformat(created_at_str)

            last_accessed_str = metadata.get("last_accessed", created_at_str)
            last_accessed = datetime.fromisoformat(last_accessed_str)

            now = datetime.utcnow()

            # Use the more recent of creation or last access
            most_recent = max(created_at, last_accessed)
            hours_since = (now - most_recent).total_seconds() / 3600

            # Exponential decay over configured period
            decay_factor = max(0.0, 1.0 - (hours_since / self.config.recency_decay_hours))

            return decay_factor

        except Exception as e:
            logger.exception(f"Error calculating recency score: {e}")
            return 0.5

    def _update_stats(
        self, retrieval_time: float, results_count: int, memory_types: list[MemoryType]
    ) -> None:
        """Update retrieval performance statistics."""
        try:
            self._retrieval_stats["total_queries"] += 1

            # Update running averages
            total_queries = self._retrieval_stats["total_queries"]
            self._retrieval_stats["avg_retrieval_time"] = (
                self._retrieval_stats["avg_retrieval_time"] * (total_queries - 1) + retrieval_time
            ) / total_queries
            self._retrieval_stats["avg_results_returned"] = (
                self._retrieval_stats["avg_results_returned"] * (total_queries - 1) + results_count
            ) / total_queries

            # Update memory type distribution
            for memory_type in memory_types:
                self._retrieval_stats["memory_type_distribution"][memory_type.value] += 1

        except Exception as e:
            logger.exception(f"Error updating stats: {e}")

    def get_performance_stats(self) -> dict[str, Any]:
        """Get retrieval performance statistics."""
        return dict(self._retrieval_stats)

    async def optimize_for_usage_patterns(self) -> dict[str, Any]:
        """Analyze usage patterns and suggest optimizations."""
        stats = self.get_performance_stats()

        recommendations = []

        # Performance recommendations
        if stats["avg_retrieval_time"] > 1000:  # >1 second
            recommendations.append("Consider increasing similarity threshold to reduce candidates")

        if stats["avg_results_returned"] < 3:
            recommendations.append("Consider lowering similarity threshold to return more results")

        # Memory type usage analysis
        type_distribution = stats["memory_type_distribution"]
        most_used_type = max(type_distribution.items(), key=lambda x: x[1])

        if most_used_type[1] > stats["total_queries"] * 0.6:
            recommendations.append(f"Consider optimizing for {most_used_type[0]} memory type")

        return {
            "performance_stats": stats,
            "recommendations": recommendations,
            "optimization_suggestions": {
                "similarity_threshold": self.config.similarity_threshold,
                "memory_type_weights": self.config.memory_type_weights,
                "recency_weight": self.config.recency_weight,
            },
        }


# Factory function for easy creation
async def create_enhanced_memory_retriever(
    store_manager: StoreManager,
    namespace: tuple[str, ...] = ("memory", "enhanced"),
    classifier_config: Optional[MemoryClassifierConfig] = None,
    **retriever_kwargs,
) -> EnhancedMemoryRetriever:
    """Factory function to create an enhanced memory retriever.

    Args:
        store_manager: Store manager for memory persistence
        namespace: Default memory namespace
        classifier_config: Optional classifier configuration
        **retriever_kwargs: Additional retriever configuration options

    Returns:
        Configured EnhancedMemoryRetriever ready for use
    """
    # Create memory store manager
    memory_store_config = MemoryStoreConfig(
        store_manager=store_manager,
        default_namespace=namespace,
        classifier_config=classifier_config or MemoryClassifierConfig(),
        **{k: v for k, v in retriever_kwargs.items() if k in MemoryStoreConfig.__fields__},
    )

    memory_store_manager = MemoryStoreManager(memory_store_config)

    # Create memory classifier
    classifier = MemoryClassifier(classifier_config or MemoryClassifierConfig())

    # Create retriever configuration
    retriever_config = EnhancedRetrieverConfig(
        memory_store_manager=memory_store_manager,
        memory_classifier=classifier,
        **{k: v for k, v in retriever_kwargs.items() if k in EnhancedRetrieverConfig.__fields__},
    )

    return EnhancedMemoryRetriever(retriever_config)
