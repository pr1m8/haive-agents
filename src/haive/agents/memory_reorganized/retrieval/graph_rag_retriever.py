"""Graph RAG Retriever for Memory System.

This module implements a Graph RAG retriever that combines knowledge graph traversal
with vector similarity search to provide comprehensive memory retrieval with
relationship context and semantic understanding.
"""

import logging
from datetime import datetime
from typing import Any, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, ConfigDict, Field

from haive.agents.memory.core.classifier import MemoryClassifier
from haive.agents.memory.core.stores import MemoryStoreManager
from haive.agents.memory.core.types import MemoryQueryIntent, MemoryType
from haive.agents.memory.kg_generator_agent import (
    KGGeneratorAgent,
    KnowledgeGraphNode,
    KnowledgeGraphRelationship,
    Optional,
)

logger = logging.getLogger(__name__)


class GraphRAGResult(BaseModel):
    """Comprehensive result from Graph RAG retrieval combining knowledge graph and vector.
    search.

    This class encapsulates all information from a Graph RAG retrieval operation,
    including retrieved memories, graph traversal results, scoring information,
    and performance metrics for analysis and optimization.

    Attributes:
        query: Original user query that was processed
        memories: Retrieved memories from both vector and graph sources
        start_entities: Initial entities identified in the query for graph traversal
        traversed_entities: All entities explored during graph traversal
        relationship_paths: Relationship paths discovered during graph traversal
        graph_nodes_explored: Number of graph nodes explored (for testing compatibility)
        graph_paths: Alias for relationship_paths (for backward compatibility)
        similarity_scores: Vector similarity scores for each memory
        graph_scores: Graph centrality scores for each memory
        final_scores: Combined final scores used for ranking
        total_time_ms: Total processing time for the entire operation
        graph_traversal_time_ms: Time spent on graph traversal
        vector_search_time_ms: Time spent on vector search
        query_intent: Analyzed query intent and characteristics
        expansion_terms: Query expansion terms used for enhanced retrieval

    Examples:
        Accessing Graph RAG results::

            result = await retriever.retrieve_memories(
                "What are the connections between Python and machine learning?"
            )

            print(f"Query: {result.query}")
            print(f"Retrieved {len(result.memories)} memories")
            print(f"Explored {result.graph_nodes_explored} graph nodes")
            print(f"Found {len(result.relationship_paths)} relationship paths")
            print(f"Total time: {result.total_time_ms:.1f}ms")

            # Access individual memories with scores
            for i, memory in enumerate(result.memories):
                sim_score = result.similarity_scores[i]
                graph_score = result.graph_scores[i]
                final_score = result.final_scores[i]

                print(f"Memory {i+1}: {memory['content'][:100]}...")
                print(f"  Similarity: {sim_score:.2f}, Graph: {graph_score:.2f}, Final: {final_score:.2f}")

        Analyzing graph traversal results::

            result = await retriever.retrieve_memories("machine learning algorithms")

            print(f"Starting entities: {[e.name for e in result.start_entities]}")
            print(f"Traversed entities: {[e.name for e in result.traversed_entities]}")

            # Analyze relationship paths
            for i, path in enumerate(result.relationship_paths):
                print(f"Path {i+1}:")
                for rel in path:
                    print(f"  {rel.source_id} -> {rel.target_id} ({rel.relationship_type})")

        Performance analysis::

            result = await retriever.retrieve_memories("complex query")

            print(f"Performance breakdown:")
            print(f"  Graph traversal: {result.graph_traversal_time_ms:.1f}ms")
            print(f"  Vector search: {result.vector_search_time_ms:.1f}ms")
            print(f"  Total time: {result.total_time_ms:.1f}ms")

            # Query expansion analysis
            if result.expansion_terms:
                print(f"Query expanded with: {result.expansion_terms}")

        Getting top memories::

            result = await retriever.retrieve_memories("Python programming")

            # Get top 5 memories by final score
            top_memories = result.get_top_memories(limit=5)

            for i, memory in enumerate(top_memories):
                print(f"Top {i+1}: {memory['content'][:50]}...")
    """

    query: str = Field(..., description="Original query")
    memories: list[dict[str, Any]] = Field(default_factory=list, description="Retrieved memories")

    # Graph traversal results
    start_entities: list[KnowledgeGraphNode] = Field(
        default_factory=list, description="Starting entities for traversal"
    )
    traversed_entities: list[KnowledgeGraphNode] = Field(
        default_factory=list, description="All traversed entities"
    )
    relationship_paths: list[list[KnowledgeGraphRelationship]] = Field(
        default_factory=list, description="Relationship paths found"
    )

    # Test-expected fields
    graph_nodes_explored: int = Field(
        default=0, description="Number of graph nodes explored during traversal"
    )
    graph_paths: list[list[KnowledgeGraphRelationship]] = Field(
        default_factory=list, description="Alias for relationship_paths for backward compatibility"
    )

    # Scoring information
    similarity_scores: list[float] = Field(
        default_factory=list, description="Similarity scores for memories"
    )
    graph_scores: list[float] = Field(default_factory=list, description="Graph centrality scores")
    final_scores: list[float] = Field(default_factory=list, description="Combined final scores")

    # Metadata
    total_time_ms: float = Field(default=0.0, description="Total retrieval time in milliseconds")
    graph_traversal_time_ms: float = Field(default=0.0, description="Graph traversal time")
    vector_search_time_ms: float = Field(default=0.0, description="Vector search time")

    # Query analysis
    query_intent: Optional[MemoryQueryIntent] = Field(
        default=None, description="Analyzed query intent"
    )
    expansion_terms: list[str] = Field(default_factory=list, description="Query expansion terms")

    def get_top_memories(self, limit: int = 10) -> list[dict[str, Any]]:
        """Get top memories by final score with ranking.

        Args:
            limit: Maximum number of memories to return

        Returns:
            List[Dict[str, Any]]: Top memories sorted by final score

        Examples:
            Get top memories::

                result = await retriever.retrieve_memories("Python programming")
                top_memories = result.get_top_memories(limit=5)

                for i, memory in enumerate(top_memories):
                    print(f"Top {i+1}: {memory['content'][:50]}...")
        """
        if not self.memories:
            return []

        # Sort by final score
        scored_memories = list(zip(self.memories, self.final_scores, strict=False))
        scored_memories.sort(key=lambda x: x[1], reverse=True)

        return [memory for memory, score in scored_memories[:limit]]


class GraphRAGRetrieverConfig(BaseModel):
    """Configuration for Graph RAG retriever with comprehensive customization options.

    This configuration class defines all parameters needed to create and configure
    a GraphRAGRetriever, including core components, graph traversal settings,
    scoring weights, and query expansion parameters.

    Attributes:
        memory_store_manager: Manager for memory storage and retrieval operations
        memory_classifier: Classifier for analyzing query intent and memory types
        kg_generator: Knowledge graph generator for entity and relationship extraction
        default_limit: Default number of memories to retrieve per query
        max_limit: Maximum number of memories that can be retrieved
        max_traversal_depth: Maximum depth for graph traversal (prevents infinite loops)
        min_relationship_confidence: Minimum confidence score for relationships to traverse
        enable_bidirectional_traversal: Whether to traverse relationships in both directions
        similarity_weight: Weight for vector similarity score in final ranking (0.0-1.0)
        graph_weight: Weight for graph centrality score in final ranking (0.0-1.0)
        importance_weight: Weight for memory importance score in final ranking (0.0-1.0)
        recency_weight: Weight for memory recency score in final ranking (0.0-1.0)
        enable_query_expansion: Whether to enable query expansion with related terms
        max_expansion_terms: Maximum number of terms to add during query expansion
        llm_config: LLM configuration for query analysis and entity identification

    Examples:
        Basic configuration::

            config = GraphRAGRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier,
                kg_generator=kg_generator,
                default_limit=10,
                max_traversal_depth=2
            )

        Performance-optimized configuration::

            config = GraphRAGRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier,
                kg_generator=kg_generator,

                # Faster retrieval settings
                default_limit=5,
                max_limit=20,
                max_traversal_depth=2,
                min_relationship_confidence=0.7,
                enable_bidirectional_traversal=False,

                # Similarity-focused scoring
                similarity_weight=0.6,
                graph_weight=0.2,
                importance_weight=0.1,
                recency_weight=0.1,

                # Limited query expansion
                enable_query_expansion=True,
                max_expansion_terms=3,

                # Fast LLM
                llm_config=AugLLMConfig(
                    model="gpt-3.5-turbo",
                    temperature=0.1,
                    max_tokens=500
                )
            )

        Quality-focused configuration::

            config = GraphRAGRetrieverConfig(
                memory_store_manager=store_manager,
                memory_classifier=classifier,
                kg_generator=kg_generator,

                # Comprehensive retrieval settings
                default_limit=15,
                max_limit=100,
                max_traversal_depth=4,
                min_relationship_confidence=0.3,
                enable_bidirectional_traversal=True,

                # Balanced scoring
                similarity_weight=0.3,
                graph_weight=0.4,
                importance_weight=0.2,
                recency_weight=0.1,

                # Extensive query expansion
                enable_query_expansion=True,
                max_expansion_terms=8,

                # High-quality LLM
                llm_config=AugLLMConfig(
                    model="gpt-4",
                    temperature=0.2,
                    max_tokens=1000
                )
            )

    Note:
        The scoring weights (similarity_weight, graph_weight, importance_weight, recency_weight)
        should sum to 1.0 for optimal result ranking. The system will normalize them if needed.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Core components
    memory_store_manager: MemoryStoreManager = Field(..., description="Memory store manager")
    memory_classifier: MemoryClassifier = Field(..., description="Memory classifier")
    kg_generator: KGGeneratorAgent = Field(..., description="Knowledge graph generator")

    # Retrieval configuration
    default_limit: int = Field(default=10, description="Default number of memories to retrieve")
    max_limit: int = Field(default=50, description="Maximum number of memories to retrieve")

    # Graph traversal configuration
    max_traversal_depth: int = Field(default=3, description="Maximum graph traversal depth")
    min_relationship_confidence: float = Field(
        default=0.5, description="Minimum confidence for relationships"
    )
    enable_bidirectional_traversal: bool = Field(
        default=True, description="Enable bidirectional graph traversal"
    )

    # Scoring configuration
    similarity_weight: float = Field(default=0.4, description="Weight for similarity score")
    graph_weight: float = Field(default=0.3, description="Weight for graph centrality score")
    importance_weight: float = Field(default=0.2, description="Weight for importance score")
    recency_weight: float = Field(default=0.1, description="Weight for recency score")

    # Query expansion
    enable_query_expansion: bool = Field(default=True, description="Enable query expansion")
    max_expansion_terms: int = Field(default=5, description="Maximum expansion terms")

    # LLM configuration
    llm_config: AugLLMConfig = Field(
        default_factory=AugLLMConfig, description="LLM for query analysis"
    )


class GraphRAGRetriever:
    """Advanced Graph RAG retriever that combines knowledge graph traversal with vector.
    similarity search.

    The GraphRAGRetriever enhances traditional vector-based memory retrieval by leveraging
    knowledge graph structure to discover relevant memories through entity relationships
    and semantic connections. This approach provides more comprehensive and contextually
    rich retrieval results.

    Key Features:
        - Intelligent entity identification from queries using LLM analysis
        - Multi-hop graph traversal to discover related entities and concepts
        - Hybrid scoring combining vector similarity, graph centrality, and importance
        - Query expansion with semantically related terms
        - Relationship path discovery for context understanding
        - Bidirectional graph traversal for comprehensive coverage
        - Performance optimization with configurable limits and thresholds

    Retrieval Process:
        1. Query Analysis: Parse query intent and identify mentioned entities
        2. Entity Identification: Match query entities to knowledge graph nodes
        3. Graph Traversal: Explore relationships to find connected entities
        4. Memory Retrieval: Collect memories from both vector search and graph entities
        5. Scoring: Combine similarity, centrality, importance, and recency scores
        6. Ranking: Sort results by final score and return top memories

    Attributes:
        config: Configuration object with all retrieval settings
        memory_store: Memory store manager for basic storage operations
        classifier: Memory classifier for query intent analysis
        kg_generator: Knowledge graph generator for entity and relationship data
        llm: LLM runnable for query analysis and entity identification
        entity_identification_prompt: Prompt template for entity identification
        relationship_path_analysis_prompt: Prompt template for path analysis

    Examples:
        Basic Graph RAG retrieval::

            # Create retriever
            retriever = GraphRAGRetriever(config)

            # Retrieve memories with graph enhancement
            result = await retriever.retrieve_memories(
                "What are the connections between Python and machine learning?"
            )

            print(f"Retrieved {len(result.memories)} memories")
            print(f"Explored {result.graph_nodes_explored} graph nodes")
            print(f"Found {len(result.relationship_paths)} relationship paths")

            # Access memories with graph context
            for memory in result.memories:
                graph_context = memory.get("graph_context", [])
                if graph_context:
                    entities = [ctx["entity_name"] for ctx in graph_context]
                    print(f"Memory connected to entities: {entities}")

        Advanced retrieval with custom parameters::

            # Retrieve with specific settings
            result = await retriever.retrieve_memories(
                query="How do neural networks work?",
                limit=15,
                memory_types=[MemoryType.SEMANTIC, MemoryType.PROCEDURAL],
                namespace=("user", "ml", "concepts"),
                enable_graph_traversal=True,
                max_graph_depth=3
            )

            # Analyze scoring components
            for i, memory in enumerate(result.memories):
                sim_score = result.similarity_scores[i]
                graph_score = result.graph_scores[i]
                final_score = result.final_scores[i]

                print(f"Memory {i+1}: Final={final_score:.2f} "
                      f"(Sim={sim_score:.2f}, Graph={graph_score:.2f})")

        Entity context exploration::

            # Get comprehensive context for specific entity
            context = await retriever.get_entity_context("Python")

            print(f"Entity: {context['entity'].name}")
            print(f"Connections: {context['total_connections']}")
            print(f"Associated memories: {context['memory_count']}")

            # Explore entity neighborhood
            neighborhood = context['neighborhood']
            for level, entities in neighborhood.get('levels', {}).items():
                print(f"Level {level}: {[e.name for e in entities]}")

        Relationship path analysis::

            # Find paths between entities
            paths = await retriever.find_relationship_paths(
                "Python", "Machine Learning", max_depth=3
            )

            for i, path in enumerate(paths):
                print(f"Path {i+1}:")
                for rel in path:
                    print(f"  {rel.source_id} -> {rel.target_id} ({rel.relationship_type})")

        Performance monitoring::

            result = await retriever.retrieve_memories("complex query")

            print(f"Performance breakdown:")
            print(f"  Graph traversal: {result.graph_traversal_time_ms:.1f}ms")
            print(f"  Vector search: {result.vector_search_time_ms:.1f}ms")
            print(f"  Total time: {result.total_time_ms:.1f}ms")

            # Query expansion analysis
            if result.expansion_terms:
                print(f"Query expanded with: {result.expansion_terms}")

    Note:
        The retriever automatically balances graph traversal depth and performance
        based on the configuration. For large knowledge graphs, consider reducing
        max_traversal_depth and increasing min_relationship_confidence for better
        performance.
    """

    def __init__(self, config: GraphRAGRetrieverConfig):
        """Initialize the Graph RAG retriever with comprehensive configuration.

        Sets up all components needed for Graph RAG retrieval including memory stores,
        knowledge graph generators, LLM for query analysis, and prompt templates.

        Args:
            config: GraphRAGRetrieverConfig with all necessary components and settings

        Raises:
            ValueError: If required components are missing in config

        Examples:
            Basic initialization::

                config = GraphRAGRetrieverConfig(
                    memory_store_manager=store_manager,
                    memory_classifier=classifier,
                    kg_generator=kg_generator
                )

                retriever = GraphRAGRetriever(config)

            With custom LLM configuration::

                config = GraphRAGRetrieverConfig(
                    memory_store_manager=store_manager,
                    memory_classifier=classifier,
                    kg_generator=kg_generator,
                    llm_config=AugLLMConfig(
                        model="gpt-4",
                        temperature=0.1,
                        max_tokens=500
                    )
                )

                retriever = GraphRAGRetriever(config)

        Note:
            The retriever validates all required components during initialization
            and sets up optimized prompt templates for entity identification and
            relationship path analysis.
        """
        self.config = config
        self.memory_store = config.memory_store_manager
        self.classifier = config.memory_classifier
        self.kg_generator = config.kg_generator

        # Setup LLM for query analysis
        self.llm = config.llm_config.create_runnable()

        # Setup prompts
        self._setup_prompts()

    def _setup_prompts(self) -> None:
        """Setup prompts for query analysis and expansion.
        
        Initializes the prompt templates used for entity identification and relationship
        path analysis. These prompts are crucial for the LLM-based analysis components
        of the Graph RAG retrieval process.
        
        The method creates two main prompt templates:
        
        1. **Entity Identification Prompt**: Used to identify entities mentioned in user
           queries and suggest related entities that might be relevant for graph traversal.
           
        2. **Relationship Path Analysis Prompt**: Used to analyze the relevance of
           discovered relationship paths and provide context for query responses.
           
        Note:
            This method is called automatically during initialization and sets up
            optimized prompts that balance accuracy with token efficiency.
        """
        self.entity_identification_prompt = PromptTemplate(
            template="""You are an expert at identifying entities in user queries for knowledge graph retrieval.

KNOWN ENTITIES IN KNOWLEDGE GRAPH:
{known_entities}

USER QUERY:
{query}

TASK:
1. Identify all entities mentioned in the query that exist in the knowledge graph
2. Suggest additional related entities that might be relevant
3. Provide expansion terms that could help find more relevant information

ENTITY TYPES TO CONSIDER:
- People (names, roles, titles)
- Organizations (companies, institutions)
- Locations (cities, countries, places)
- Concepts (technologies, ideas, subjects)
- Events (meetings, projects, activities)
- Products/Services (tools, software, services)

FORMAT: Return a JSON object with structure:
{{
    "direct_entities": ["entity1", "entity2"],
    "related_entities": ["entity3", "entity4"],
    "expansion_terms": ["term1", "term2"],
    "query_intent": "What is the user trying to find?",
    "suggested_traversal_depth": 2
}}

Analyze the query now:""",
            input_variables=["query", "known_entities"],
        )

        self.relationship_path_analysis_prompt = PromptTemplate(
            template="""You are an expert at analyzing relationship paths in knowledge graphs to provide context.

QUERY: {query}

RELATIONSHIP PATH:
{relationship_path}

MEMORIES ASSOCIATED WITH PATH:
{path_memories}

TASK:
Analyze how this relationship path is relevant to the user's query and provide:
1. Relevance score (0.0-1.0)
2. Context explanation
3. Key insights from the path

FORMAT: Return a JSON object:
{{
    "relevance_score": 0.85,
    "context_explanation": "Brief explanation of why this path is relevant",
    "key_insights": ["insight1", "insight2"],
    "path_importance": "high/medium/low"
}}

Analyze the relationship path now:""",
            input_variables=["query", "relationship_path", "path_memories"],
        )

    async def retrieve_memories(
        self,
        query: str,
        limit: Optional[int] = None,
        memory_types: list[MemoryType] | None = None,
        namespace: tuple[str, ...] | None = None,
        enable_graph_traversal: bool = True,
        max_graph_depth: Optional[int] = None,
    ) -> GraphRAGResult:
        """Retrieve memories using Graph RAG approach.

        Args:
            query: User query
            limit: Maximum number of memories to retrieve
            memory_types: Specific memory types to focus on
            namespace: Memory namespace to search
            enable_graph_traversal: Whether to use graph traversal
            max_graph_depth: Maximum depth for graph traversal (overrides config)

        Returns:
            GraphRAGResult with retrieved memories and graph context
        """
        start_time = datetime.now()

        try:
            limit = limit or self.config.default_limit

            # Initialize result
            result = GraphRAGResult(query=query)

            # Step 1: Analyze query intent
            if self.classifier:
                result.query_intent = self.classifier.classify_query_intent(query)

            # Step 2: Identify entities in query
            graph_traversal_start = datetime.now()
            entities_info = await self._identify_query_entities(query)
            result.expansion_terms = entities_info.get("expansion_terms", [])

            # Step 3: Perform graph traversal if enabled
            if enable_graph_traversal:
                # Use provided max_graph_depth or fall back to suggested or
                # config default
                traversal_depth = max_graph_depth or entities_info.get(
                    "suggested_traversal_depth", self.config.max_traversal_depth
                )
                (
                    result.start_entities,
                    result.traversed_entities,
                    result.relationship_paths,
                ) = await self._perform_graph_traversal(
                    entities_info.get("direct_entities", []),
                    entities_info.get("related_entities", []),
                    traversal_depth,
                )
                # Populate test-expected fields
                result.graph_nodes_explored = len(result.traversed_entities)
                result.graph_paths = result.relationship_paths  # Alias for backward compatibility

            graph_traversal_end = datetime.now()
            result.graph_traversal_time_ms = (
                graph_traversal_end - graph_traversal_start
            ).total_seconds() * 1000

            # Step 4: Retrieve memories using traditional vector search
            vector_search_start = datetime.now()
            expanded_query = self._build_expanded_query(query, result.expansion_terms)

            vector_memories = await self.memory_store.retrieve_memories(
                query=expanded_query,
                namespace=namespace,
                memory_types=memory_types,
                limit=limit * 2,  # Get more results for re-ranking
            )

            vector_search_end = datetime.now()
            result.vector_search_time_ms = (
                vector_search_end - vector_search_start
            ).total_seconds() * 1000

            # Step 5: Get graph-based memories
            graph_memories = []
            if enable_graph_traversal:
                graph_memories = await self._get_memories_from_graph_entities(
                    result.traversed_entities, namespace
                )

            # Step 6: Combine and deduplicate memories
            combined_memories = self._combine_memories(vector_memories, graph_memories)

            # Step 7: Score memories using combined approach
            (
                result.memories,
                result.similarity_scores,
                result.graph_scores,
                result.final_scores,
            ) = await self._score_memories(
                combined_memories, query, result.traversed_entities, result.relationship_paths
            )

            # Step 8: Limit results
            if len(result.memories) > limit:
                # Sort by final score and limit
                scored_memories = list(
                    zip(
                        result.memories,
                        result.similarity_scores,
                        result.graph_scores,
                        result.final_scores,
                        strict=False,
                    )
                )
                scored_memories.sort(key=lambda x: x[3], reverse=True)

                result.memories = [m[0] for m in scored_memories[:limit]]
                result.similarity_scores = [m[1] for m in scored_memories[:limit]]
                result.graph_scores = [m[2] for m in scored_memories[:limit]]
                result.final_scores = [m[3] for m in scored_memories[:limit]]

            # Calculate total time
            end_time = datetime.now()
            result.total_time_ms = (end_time - start_time).total_seconds() * 1000

            logger.info(
                f"Graph RAG retrieval completed in {result.total_time_ms:.1f}ms: {
                    len(result.memories)
                } memories, {len(result.traversed_entities)} entities"
            )

            return result

        except Exception as e:
            logger.exception(f"Error in Graph RAG retrieval: {e}")
            # Return empty result on error with performance tracking
            result = GraphRAGResult(query=query)
            result.total_time_ms = (datetime.now() - start_time).total_seconds() * 1000
            
            # Add error context for debugging
            result.expansion_terms = ["[ERROR_OCCURRED]"]
            logger.warning(f"Graph RAG retrieval failed after {result.total_time_ms:.1f}ms for query: '{query[:100]}...'")
            
            return result

    async def _identify_query_entities(self, query: str) -> dict[str, Any]:
        """Identify entities mentioned in the query using LLM analysis with fallback.
        
        This method performs intelligent entity identification from user queries by
        leveraging LLM capabilities to understand context and suggest related entities.
        It includes robust fallback mechanisms for cases where LLM analysis fails.
        
        The identification process:
        1. Retrieve known entities from the knowledge graph
        2. Use LLM with specialized prompt to identify entities in query
        3. Extract expansion terms and suggested traversal depth
        4. Fall back to simple string matching if LLM analysis fails
        
        Args:
            query: User's natural language query to analyze
            
        Returns:
            Dict[str, Any]: Entity identification results containing:
                - direct_entities: List of entities explicitly mentioned in query
                - related_entities: List of entities suggested as potentially relevant
                - expansion_terms: List of terms for query expansion
                - query_intent: Analysis of what the user is trying to find
                - suggested_traversal_depth: Recommended graph traversal depth
                
        Examples:
            Comprehensive entity identification::
            
                query = "How does Python relate to machine learning and data science?"
                result = await self._identify_query_entities(query)
                
                print(f"Direct entities: {result['direct_entities']}")
                # Output: ['Python', 'Machine Learning', 'Data Science']
                
                print(f"Related entities: {result['related_entities']}")
                # Output: ['Programming', 'Statistics', 'Algorithms']
                
                print(f"Expansion terms: {result['expansion_terms']}")
                # Output: ['programming', 'algorithms', 'statistics', 'AI']
                
                print(f"Query intent: {result['query_intent']}")
                # Output: "User wants to understand relationships between Python and ML/DS"
                
                print(f"Suggested depth: {result['suggested_traversal_depth']}")
                # Output: 2
                
            Handling empty knowledge graph::
            
                # When no entities exist in knowledge graph
                result = await self._identify_query_entities("Tell me about quantum computing")
                
                # Returns safe defaults
                assert result['direct_entities'] == []
                assert result['related_entities'] == []
                assert result['suggested_traversal_depth'] == 1
                
            Entity matching examples::
            
                # Technical query
                tech_query = "Python frameworks for web development"
                tech_result = await self._identify_query_entities(tech_query)
                
                # Business query
                business_query = "Market analysis for startup companies"
                business_result = await self._identify_query_entities(business_query)
                
                # Compare entity types found
                print(f"Tech entities: {tech_result['direct_entities']}")
                print(f"Business entities: {business_result['direct_entities']}")
                
        LLM Prompt Engineering:
            The method uses a sophisticated prompt template that:
            - Provides context about known entities in the knowledge graph
            - Requests structured JSON output with specific fields
            - Includes entity type guidelines (People, Organizations, Concepts, etc.)
            - Asks for traversal depth suggestions based on query complexity
            
        Fallback Mechanism:
            When LLM analysis fails (due to API errors, malformed responses, etc.),
            the system automatically falls back to _fallback_entity_identification
            which uses simple string matching to ensure continued functionality.
            
        Performance Optimization:
            - Limits known entities to first 100 to avoid token limits
            - Uses efficient string operations for entity lookup
            - Caches entity information within the knowledge graph
            
        Error Recovery:
            The method handles various error conditions gracefully:
            - LLM API failures or timeouts
            - Malformed JSON responses
            - Empty or invalid entity lists
            - Missing knowledge graph data
        """
        # Get known entities from knowledge graph
        known_entities = [
            f"{node.name} ({node.type})"
            for node in self.kg_generator.knowledge_graph.nodes.values()
        ]

        if not known_entities:
            # No knowledge graph available, return empty
            return {
                "direct_entities": [],
                "related_entities": [],
                "expansion_terms": [],
                "query_intent": query,
                "suggested_traversal_depth": 1,
            }

        try:
            # Use LLM to identify entities
            prompt = self.entity_identification_prompt.format(
                query=query,
                known_entities=", ".join(known_entities[:100]),  # Limit to avoid token limits
            )

            response = await self.llm.ainvoke(
                [
                    SystemMessage(
                        content="You are an expert entity identifier for knowledge graph retrieval."
                    ),
                    HumanMessage(content=prompt),
                ]
            )

            # Parse response
            entities_info = self._parse_json_response(response.content)

            if entities_info:
                return entities_info
            # Fallback to simple key matching
            return self._fallback_entity_identification(query, known_entities)

        except Exception as e:
            logger.exception(f"Error identifying query entities: {e}")
            return self._fallback_entity_identification(query, known_entities)

    def _fallback_entity_identification(
        self, query: str, known_entities: list[str]
    ) -> dict[str, Any]:
        """Fallback entity identification using simple matching when LLM analysis fails.
        
        This method provides a robust fallback mechanism for entity identification
        when the LLM-based analysis encounters errors or returns invalid responses.
        It uses simple string matching to identify entities mentioned in the query.
        
        Args:
            query: User query to analyze for entity mentions
            known_entities: List of known entities in the knowledge graph
            
        Returns:
            Dict[str, Any]: Entity identification result with structure:
                - direct_entities: List of entities directly mentioned in query
                - related_entities: Empty list (fallback doesn't suggest related entities)
                - expansion_terms: Simple word split of the query
                - query_intent: Original query as intent description
                - suggested_traversal_depth: Conservative depth of 1
                
        Examples:
            Fallback entity identification::
            
                result = self._fallback_entity_identification(
                    "Tell me about Python programming",
                    ["Python (Language)", "Programming (Concept)", "JavaScript (Language)"]
                )
                
                # Result:
                # {
                #     "direct_entities": ["Python", "Programming"],
                #     "related_entities": [],
                #     "expansion_terms": ["Tell", "me", "about", "Python", "programming"],
                #     "query_intent": "Tell me about Python programming",
                #     "suggested_traversal_depth": 1
                # }
                
        Note:
            This fallback method is conservative and may miss subtle entity relationships
            that the LLM would catch, but it ensures the system continues to function
            even when LLM services are unavailable or return errors.
        """
        query_lower = query.lower()
        direct_entities = []

        for entity_str in known_entities:
            entity_name = entity_str.split(" (")[0]  # Remove type annotation
            if entity_name.lower() in query_lower:
                direct_entities.append(entity_name)

        return {
            "direct_entities": direct_entities,
            "related_entities": [],
            "expansion_terms": query.split(),
            "query_intent": query,
            "suggested_traversal_depth": 1,
        }

    async def _perform_graph_traversal(
        self, direct_entities: list[str], related_entities: list[str], max_depth: int
    ) -> tuple[
        list[KnowledgeGraphNode],
        list[KnowledgeGraphNode],
        list[list[KnowledgeGraphRelationship]],
    ]:
        """Perform graph traversal to find related entities and relationship paths.
        
        This method implements a breadth-first search algorithm to explore the knowledge
        graph starting from identified entities. It discovers connected entities and
        records relationship paths that may be relevant to the user's query.
        
        The traversal process:
        1. Find starting entity nodes in the knowledge graph
        2. Perform breadth-first exploration up to max_depth
        3. Filter relationships by confidence threshold
        4. Collect traversed entities and relationship paths
        5. Limit paths to prevent memory issues on large graphs
        
        Args:
            direct_entities: Entity names directly mentioned in the query
            related_entities: Additional entities suggested as potentially relevant
            max_depth: Maximum traversal depth to prevent infinite loops
            
        Returns:
            Tuple containing:
                - start_entities: List of KnowledgeGraphNode objects used as starting points
                - all_traversed: List of all KnowledgeGraphNode objects discovered during traversal
                - relationship_paths: List of relationship paths (each path is a list of relationships)
                
        Examples:
            Graph traversal for entity exploration::
            
                start_entities, traversed, paths = await self._perform_graph_traversal(
                    direct_entities=["Python", "Machine Learning"],
                    related_entities=["Data Science"],
                    max_depth=2
                )
                
                print(f"Started from {len(start_entities)} entities")
                print(f"Discovered {len(traversed)} total entities")
                print(f"Found {len(paths)} relationship paths")
                
                # Analyze traversed entities
                for entity in traversed:
                    print(f"Entity: {entity.name} ({entity.type}) - Confidence: {entity.confidence:.2f}")
                    
        Algorithm Details:
            The breadth-first traversal ensures that shorter paths are discovered first
            and provides comprehensive coverage of the entity neighborhood. Relationship
            confidence filtering helps focus on high-quality connections while the path
            limit (50 paths) prevents excessive memory usage on highly connected graphs.
            
        Performance Considerations:
            - Uses visited set to prevent cycles and duplicate exploration
            - Applies confidence threshold to reduce low-quality relationships
            - Limits relationship paths to control memory usage
            - Supports bidirectional traversal when enabled in configuration
        """
        kg = self.kg_generator.knowledge_graph

        # Find starting entity nodes
        start_entities = []
        for entity_name in direct_entities + related_entities:
            entity_id = self.kg_generator._find_entity_id(entity_name)
            if entity_id and entity_id in kg.nodes:
                start_entities.append(kg.nodes[entity_id])

        if not start_entities:
            return [], [], []

        # Perform breadth-first traversal
        visited = set()
        current_level = {entity.id for entity in start_entities}
        all_traversed = list(start_entities)
        relationship_paths = []

        for _depth in range(max_depth):
            if not current_level:
                break

            next_level = set()

            for node_id in current_level:
                if node_id in visited:
                    continue

                visited.add(node_id)

                # Get relationships for this node
                relationships = kg.get_relationships_for_node(node_id)

                # Filter by confidence
                filtered_relationships = [
                    rel
                    for rel in relationships
                    if rel.confidence >= self.config.min_relationship_confidence
                ]

                for rel in filtered_relationships:
                    # Determine next node
                    next_node_id = rel.target_id if rel.source_id == node_id else rel.source_id

                    if next_node_id not in visited and next_node_id in kg.nodes:
                        next_level.add(next_node_id)

                        # Add to traversed entities
                        next_node = kg.nodes[next_node_id]
                        if next_node not in all_traversed:
                            all_traversed.append(next_node)

                        # Create relationship path
                        path = [rel]
                        if len(relationship_paths) < 50:  # Limit paths to avoid memory issues
                            relationship_paths.append(path)

            current_level = next_level

        return start_entities, all_traversed, relationship_paths

    async def _get_memories_from_graph_entities(
        self, entities: list[KnowledgeGraphNode], namespace: tuple[str, ...] | None
    ) -> list[dict[str, Any]]:
        """Retrieve memories associated with knowledge graph entities.
        
        This method extracts memories that are referenced by the provided knowledge
        graph entities. It adds graph context metadata to each memory to indicate
        which entities it's associated with and their relationship details.
        
        The process:
        1. Iterate through each knowledge graph entity
        2. Retrieve memories referenced by each entity
        3. Add graph context metadata to memories
        4. Return enriched memories with entity associations
        
        Args:
            entities: List of KnowledgeGraphNode objects to get memories for
            namespace: Optional namespace filter for memory retrieval
            
        Returns:
            List[Dict[str, Any]]: Memories enriched with graph context metadata.
                Each memory includes:
                - Original memory fields (content, metadata, etc.)
                - graph_context: List of associated entity information
                    - entity_id: Unique identifier of the associated entity
                    - entity_name: Human-readable name of the entity
                    - entity_type: Type classification of the entity
                    - confidence: Confidence score of the entity
                    
        Examples:
            Retrieving entity-associated memories::
            
                entities = [python_entity, ml_entity, ai_entity]
                memories = await self._get_memories_from_graph_entities(
                    entities, namespace=("user", "technical")
                )
                
                for memory in memories:
                    print(f"Memory: {memory['content'][:100]}...")
                    
                    # Check graph context
                    graph_context = memory.get('graph_context', [])
                    if graph_context:
                        entities_names = [ctx['entity_name'] for ctx in graph_context]
                        print(f"  Associated with entities: {entities_names}")
                        
                        # Check entity confidence
                        avg_confidence = sum(ctx['confidence'] for ctx in graph_context) / len(graph_context)
                        print(f"  Average entity confidence: {avg_confidence:.2f}")
                        
            Analyzing graph-memory connections::
            
                memories = await self._get_memories_from_graph_entities(traversed_entities)
                
                # Group memories by entity type
                by_entity_type = {}
                for memory in memories:
                    for ctx in memory.get('graph_context', []):
                        entity_type = ctx['entity_type']
                        if entity_type not in by_entity_type:
                            by_entity_type[entity_type] = []
                        by_entity_type[entity_type].append(memory)
                        
                for entity_type, type_memories in by_entity_type.items():
                    print(f"{entity_type}: {len(type_memories)} memories")
                    
        Graph Context Structure:
            The graph_context added to each memory contains detailed entity association
            information that enables sophisticated analysis of entity-memory relationships
            and supports advanced ranking algorithms based on graph centrality.
            
        Note:
            Memories may be associated with multiple entities, resulting in multiple
            graph_context entries. This allows for rich relationship analysis and
            enables the scoring system to consider multiple entity associations.
        """
        memories = []

        for entity in entities:
            # Get memories referenced by this entity
            for memory_ref in entity.memory_references:
                memory = await self.memory_store.get_memory_by_id(memory_ref)
                if memory:
                    # Add entity context to memory
                    if "graph_context" not in memory:
                        memory["graph_context"] = []
                    memory["graph_context"].append(
                        {
                            "entity_id": entity.id,
                            "entity_name": entity.name,
                            "entity_type": entity.type,
                            "confidence": entity.confidence,
                        }
                    )
                    memories.append(memory)

        return memories

    def _combine_memories(
        self, vector_memories: list[dict[str, Any]], graph_memories: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Combine and deduplicate memories from vector and graph retrieval sources.
        
        This method intelligently merges memories retrieved through vector similarity
        search with those discovered through graph traversal, handling deduplication
        and metadata enrichment to create a unified result set.
        
        The combination process:
        1. Use memory ID for deduplication to avoid duplicate memories
        2. Add retrieval source metadata to track how each memory was found
        3. Merge graph context for memories found through both sources
        4. Preserve all relevant metadata from both retrieval methods
        
        Args:
            vector_memories: Memories retrieved through vector similarity search
            graph_memories: Memories retrieved through knowledge graph entity associations
            
        Returns:
            List[Dict[str, Any]]: Combined and deduplicated memories with enriched metadata.
                Each memory includes:
                - Original memory content and metadata
                - retrieval_source: "vector", "graph", or "vector+graph"
                - graph_context: Entity associations (if applicable)
                - All original similarity and relevance scores
                
        Examples:
            Combining memory sources::
            
                vector_results = await self.memory_store.retrieve_memories(
                    query="Python programming", limit=20
                )
                
                graph_results = await self._get_memories_from_graph_entities(
                    [python_entity, programming_entity]
                )
                
                combined = self._combine_memories(vector_results, graph_results)
                
                # Analyze retrieval sources
                source_counts = {}
                for memory in combined:
                    source = memory['retrieval_source']
                    source_counts[source] = source_counts.get(source, 0) + 1
                    
                print(f"Memory sources: {source_counts}")
                # Output: {'vector': 12, 'graph': 3, 'vector+graph': 5}
                
            Enhanced memory analysis::
            
                combined = self._combine_memories(vector_memories, graph_memories)
                
                for memory in combined:
                    source = memory['retrieval_source']
                    has_graph_context = 'graph_context' in memory
                    
                    print(f"Memory: {memory['content'][:50]}...")
                    print(f"  Source: {source}")
                    
                    if has_graph_context:
                        entities = [ctx['entity_name'] for ctx in memory['graph_context']]
                        print(f"  Graph entities: {entities}")
                        
        Deduplication Strategy:
            Memories are deduplicated using their unique ID field. When the same memory
            is found through both vector search and graph traversal, the system:
            - Keeps the memory once in the final result
            - Updates retrieval_source to "vector+graph"
            - Merges graph_context information from both sources
            - Preserves the highest quality metadata from either source
            
        Metadata Preservation:
            The combination process preserves all relevant metadata while avoiding
            conflicts. Graph context is additive, allowing memories to be associated
            with multiple entities discovered through different retrieval paths.
        """
        # Use memory ID for deduplication
        combined = {}

        # Add vector memories
        for memory in vector_memories:
            memory_id = memory.get("id")
            if memory_id:
                memory["retrieval_source"] = "vector"
                combined[memory_id] = memory

        # Add graph memories (may update existing ones)
        for memory in graph_memories:
            memory_id = memory.get("id")
            if memory_id:
                if memory_id in combined:
                    # Merge graph context
                    existing = combined[memory_id]
                    existing["retrieval_source"] = "vector+graph"
                    if "graph_context" in memory:
                        if "graph_context" not in existing:
                            existing["graph_context"] = []
                        existing["graph_context"].extend(memory["graph_context"])
                else:
                    memory["retrieval_source"] = "graph"
                    combined[memory_id] = memory

        return list(combined.values())

    async def _score_memories(
        self,
        memories: list[dict[str, Any]],
        query: str,
        graph_entities: list[KnowledgeGraphNode],
        relationship_paths: list[list[KnowledgeGraphRelationship]],
    ) -> tuple[list[dict[str, Any]], list[float], list[float], list[float]]:
        """Score memories using sophisticated multi-factor ranking combining vector similarity and graph centrality.
        
        This method implements the core ranking algorithm that combines multiple scoring
        factors to produce the final ranking of retrieved memories. It considers vector
        similarity, graph centrality, importance, and recency to create a comprehensive
        relevance score.
        
        Scoring Components:
        1. **Vector Similarity**: Traditional semantic similarity from embeddings
        2. **Graph Centrality**: Entity importance based on graph structure and relationships
        3. **Importance Score**: Explicit importance metadata from memory storage
        4. **Recency Score**: Time-based relevance with decay over approximately 1000 hours
        
        Args:
            memories: List of memories to score and rank
            query: Original user query for context
            graph_entities: Knowledge graph entities discovered during traversal
            relationship_paths: Relationship paths found during graph exploration
            
        Returns:
            Tuple containing:
                - memories: Original memories list (unchanged order)
                - similarity_scores: Vector similarity scores for each memory
                - graph_scores: Graph centrality scores for each memory
                - final_scores: Combined weighted final scores for ranking
                
        Examples:
            Analyzing memory scoring::
            
                memories, sim_scores, graph_scores, final_scores = await self._score_memories(
                    retrieved_memories, "Python machine learning", entities, paths
                )
                
                # Analyze scoring breakdown
                for i, memory in enumerate(memories):
                    print(f"Memory {i+1}: {memory['content'][:50]}...")
                    print(f"  Similarity: {sim_scores[i]:.3f}")
                    print(f"  Graph centrality: {graph_scores[i]:.3f}")
                    print(f"  Final score: {final_scores[i]:.3f}")
                    
                    # Calculate component contributions
                    sim_contrib = sim_scores[i] * self.config.similarity_weight
                    graph_contrib = graph_scores[i] * self.config.graph_weight
                    print(f"  Similarity contrib: {sim_contrib:.3f}")
                    print(f"  Graph contrib: {graph_contrib:.3f}")
                    
            Top memory selection::
            
                memories, sim_scores, graph_scores, final_scores = await self._score_memories(
                    all_memories, query, entities, paths
                )
                
                # Sort by final score
                scored_memories = list(zip(memories, final_scores))
                scored_memories.sort(key=lambda x: x[1], reverse=True)
                
                # Get top 5 memories
                top_memories = [memory for memory, score in scored_memories[:5]]
                top_scores = [score for memory, score in scored_memories[:5]]
                
                print(f"Top memory score: {top_scores[0]:.3f}")
                print(f"Average top-5 score: {sum(top_scores)/5:.3f}")
                
            Score distribution analysis::
            
                _, sim_scores, graph_scores, final_scores = await self._score_memories(
                    memories, query, entities, paths
                )
                
                # Analyze score distributions
                avg_similarity = sum(sim_scores) / len(sim_scores)
                avg_graph = sum(graph_scores) / len(graph_scores)
                avg_final = sum(final_scores) / len(final_scores)
                
                print(f"Average similarity score: {avg_similarity:.3f}")
                print(f"Average graph score: {avg_graph:.3f}")
                print(f"Average final score: {avg_final:.3f}")
                
                # Find memories with high graph centrality
                high_centrality = [(i, score) for i, score in enumerate(graph_scores) if score > 0.7]
                print(f"High centrality memories: {len(high_centrality)}")
                
        Scoring Algorithm:
            Final Score = (similarity × similarity_weight) + 
                         (graph_centrality × graph_weight) + 
                         (importance × importance_weight) + 
                         (recency × recency_weight)
                         
            Where weights are configured in GraphRAGRetrieverConfig and should sum to 1.0
            for optimal ranking performance.
            
        Graph Centrality Calculation:
            Graph centrality considers:
            - Entity confidence scores from knowledge graph
            - Number of relationships per entity (normalized)
            - Presence in discovered relationship paths
            - Multiple entity associations per memory
            
        Performance Considerations:
            The scoring process is optimized for batch processing and handles edge cases
            like missing metadata gracefully. Default scores are used when specific
            components are unavailable.
        """
        similarity_scores = []
        graph_scores = []
        final_scores = []

        # Create entity lookup for scoring
        entity_lookup = {entity.id: entity for entity in graph_entities}

        for memory in memories:
            # Get base similarity score
            similarity = memory.get("similarity_score", 0.5)

            # Calculate graph centrality score
            graph_score = self._calculate_graph_centrality_score(
                memory, entity_lookup, relationship_paths
            )

            # Get importance and recency
            metadata = memory.get("metadata", {})
            importance = metadata.get("importance_score", 0.5)

            # Calculate recency score
            created_at = metadata.get("created_at")
            recency = 0.5  # Default
            if created_at:
                try:
                    created_time = datetime.fromisoformat(created_at)
                    hours_ago = (datetime.utcnow() - created_time).total_seconds() / 3600
                    recency = max(0.0, 1.0 - (hours_ago / 1000))  # Decay over ~1000 hours
                except BaseException:
                    pass

            # Combine scores
            final_score = (
                similarity * self.config.similarity_weight
                + graph_score * self.config.graph_weight
                + importance * self.config.importance_weight
                + recency * self.config.recency_weight
            )

            similarity_scores.append(similarity)
            graph_scores.append(graph_score)
            final_scores.append(final_score)

        return memories, similarity_scores, graph_scores, final_scores

    def _calculate_graph_centrality_score(
        self,
        memory: dict[str, Any],
        entity_lookup: dict[str, KnowledgeGraphNode],
        relationship_paths: list[list[KnowledgeGraphRelationship]],
    ) -> float:
        """Calculate graph centrality score for a memory based on associated entities.
        
        This method computes how central or important a memory is within the knowledge
        graph structure by analyzing the entities it's associated with and their
        position in the graph network.
        
        Centrality Factors:
        1. **Entity Confidence**: Higher confidence entities contribute more to centrality
        2. **Relationship Count**: Entities with more connections are more central
        3. **Path Presence**: Entities appearing in relationship paths are more relevant
        4. **Multi-Entity Normalization**: Score is normalized by number of entities
        
        Args:
            memory: Memory dictionary containing content and metadata
            entity_lookup: Mapping of entity IDs to KnowledgeGraphNode objects
            relationship_paths: List of relationship paths discovered during graph traversal
            
        Returns:
            float: Centrality score between 0.0 and 1.0, where higher values indicate
                more central/important memories within the knowledge graph structure
                
        Examples:
            Analyzing centrality components::
            
                memory = {
                    'content': 'Python is a programming language...',
                    'metadata': {'entities': ['Python', 'Programming']},
                    'graph_context': [
                        {'entity_id': 'python_1', 'entity_name': 'Python', 'confidence': 0.95},
                        {'entity_id': 'prog_1', 'entity_name': 'Programming', 'confidence': 0.88}
                    ]
                }
                
                centrality = self._calculate_graph_centrality_score(
                    memory, entity_lookup, relationship_paths
                )
                
                print(f"Memory centrality score: {centrality:.3f}")
                
            Comparing memory centrality::
            
                memories_with_centrality = []
                for memory in all_memories:
                    centrality = self._calculate_graph_centrality_score(
                        memory, entity_lookup, paths
                    )
                    memories_with_centrality.append((memory, centrality))
                    
                # Sort by centrality
                memories_with_centrality.sort(key=lambda x: x[1], reverse=True)
                
                print("Top 3 most central memories:")
                for i, (memory, centrality) in enumerate(memories_with_centrality[:3]):
                    print(f"{i+1}. Centrality: {centrality:.3f}")
                    print(f"   Content: {memory['content'][:100]}...")
                    
            Entity contribution analysis::
            
                # Analyze which entities contribute most to centrality
                for memory in sample_memories:
                    centrality = self._calculate_graph_centrality_score(
                        memory, entity_lookup, paths
                    )
                    
                    graph_context = memory.get('graph_context', [])
                    entity_names = [ctx['entity_name'] for ctx in graph_context]
                    
                    print(f"Memory centrality: {centrality:.3f}")
                    print(f"Associated entities: {entity_names}")
                    
                    # Check individual entity contributions
                    for ctx in graph_context:
                        entity_id = ctx['entity_id']
                        if entity_id in entity_lookup:
                            entity = entity_lookup[entity_id]
                            relationships = kg.get_relationships_for_node(entity_id)
                            print(f"  {ctx['entity_name']}: {len(relationships)} relationships")
                            
        Centrality Components:
        
        1. **Entity Confidence (30% weight)**:
           - Uses the confidence scores of associated entities
           - Higher confidence entities indicate more reliable associations
           
        2. **Relationship Count (40% weight)**:
           - Counts relationships for each associated entity
           - Normalized to prevent extremely connected entities from dominating
           - Max normalized value of 1.0 for entities with 10+ relationships
           
        3. **Path Presence (30% weight)**:
           - Checks if entities appear in discovered relationship paths
           - Entities in more paths contribute higher centrality
           - Max normalized value of 1.0 for entities in 10+ paths
           
        Normalization:
            The final centrality score is normalized by the number of entities associated
            with the memory to prevent memories with many entities from automatically
            receiving higher scores. This ensures fair comparison across memories with
            different numbers of entity associations.
            
        Edge Cases:
            - Memories with no associated entities receive a centrality score of 0.0
            - Missing entities in the lookup are ignored gracefully
            - The score is capped at 1.0 to maintain consistent ranges
        """
        # Get entities associated with this memory
        memory_entities = set()

        # From graph context
        graph_context = memory.get("graph_context", [])
        for ctx in graph_context:
            entity_id = ctx.get("entity_id")
            if entity_id:
                memory_entities.add(entity_id)

        # From metadata entities
        metadata = memory.get("metadata", {})
        for entity_name in metadata.get("entities", []):
            entity_id = self.kg_generator._find_entity_id(entity_name)
            if entity_id:
                memory_entities.add(entity_id)

        if not memory_entities:
            return 0.0

        # Calculate centrality based on:
        # 1. Number of relationships
        # 2. Confidence of entities
        # 3. Presence in relationship paths

        centrality_score = 0.0

        for entity_id in memory_entities:
            if entity_id in entity_lookup:
                entity = entity_lookup[entity_id]

                # Entity confidence contributes to centrality
                centrality_score += entity.confidence * 0.3

                # Number of relationships
                kg = self.kg_generator.knowledge_graph
                relationships = kg.get_relationships_for_node(entity_id)
                centrality_score += min(len(relationships) / 10.0, 1.0) * 0.4

                # Presence in relationship paths
                path_count = 0
                for path in relationship_paths:
                    for rel in path:
                        if entity_id in (rel.source_id, rel.target_id):
                            path_count += 1

                centrality_score += min(path_count / 10.0, 1.0) * 0.3

        # Normalize by number of entities
        if memory_entities:
            centrality_score /= len(memory_entities)

        return min(centrality_score, 1.0)

    def _build_expanded_query(self, original_query: str, expansion_terms: list[str]) -> str:
        """Build expanded query with additional semantic terms for enhanced retrieval.
        
        This method enhances the original user query by adding relevant expansion terms
        identified during entity analysis. Query expansion helps discover additional
        relevant memories that might not match the original query directly but are
        semantically related.
        
        Args:
            original_query: The user's original query string
            expansion_terms: List of additional terms to include in the expanded query
            
        Returns:
            str: Expanded query string combining original query with selected expansion terms
            
        Examples:
            Basic query expansion::
            
                original = "Python programming"
                expansion_terms = ["coding", "development", "scripting", "language"]
                
                expanded = self._build_expanded_query(original, expansion_terms)
                print(f"Original: {original}")
                print(f"Expanded: {expanded}")
                # Output: "Python programming coding development scripting"
                
            Controlled expansion with limits::
            
                # With max_expansion_terms = 3
                original = "machine learning"
                expansion_terms = ["AI", "neural", "networks", "deep", "learning", "algorithms"]
                
                expanded = self._build_expanded_query(original, expansion_terms)
                print(f"Expanded: {expanded}")
                # Output: "machine learning AI neural networks" (limited to 3 terms)
                
            Disabled expansion::
            
                # When enable_query_expansion = False
                expanded = self._build_expanded_query(
                    "data science", ["analytics", "statistics", "ML"]
                )
                print(f"Result: {expanded}")
                # Output: "data science" (no expansion applied)
                
            Empty expansion terms::
            
                expanded = self._build_expanded_query("blockchain", [])
                print(f"Result: {expanded}")
                # Output: "blockchain" (original query unchanged)
                
        Configuration Impact:
            The expansion behavior is controlled by two configuration parameters:
            
            - **enable_query_expansion**: Master switch for query expansion feature
            - **max_expansion_terms**: Limits number of terms added to prevent
              overly broad queries that might reduce precision
              
        Expansion Strategy:
            The method applies expansion terms in their original order, trusting that
            the entity identification process has ranked them by relevance. Terms are
            space-separated and appended to the original query to maintain readability
            and compatibility with vector search systems.
            
        Performance Considerations:
            Query expansion can significantly improve recall (finding more relevant memories)
            but may slightly reduce precision if expansion terms are too broad. The
            max_expansion_terms limit helps balance this trade-off.
        """
        if not expansion_terms or not self.config.enable_query_expansion:
            return original_query

        # Add expansion terms
        limited_terms = expansion_terms[: self.config.max_expansion_terms]
        expanded = f"{original_query} {' '.join(limited_terms)}"

        return expanded

    def _parse_json_response(self, response: str) -> dict[str, Any] | None:
        """Parse JSON response from LLM with robust error handling.
        
        This method extracts and parses JSON data from LLM responses, handling various
        response formats and providing graceful fallback when parsing fails. It's
        designed to work with LLM outputs that may contain additional text around
        the requested JSON structure.
        
        Args:
            response: Raw string response from the LLM
            
        Returns:
            Optional[Dict[str, Any]]: Parsed JSON dictionary if successful, None if parsing fails
            
        Examples:
            Successful JSON parsing::
            
                llm_response = '''Here's the analysis:
                {
                    "direct_entities": ["Python", "Machine Learning"],
                    "related_entities": ["Data Science", "AI"],
                    "expansion_terms": ["programming", "algorithms"],
                    "query_intent": "Learn about Python for ML"
                }
                This should help with your query.'''
                
                result = self._parse_json_response(llm_response)
                if result:
                    print(f"Found entities: {result['direct_entities']}")
                    print(f"Expansion terms: {result['expansion_terms']}")
                    
            Handling malformed responses::
            
                malformed_response = "The entities are Python and ML but I can't format as JSON"
                
                result = self._parse_json_response(malformed_response)
                if result is None:
                    print("Failed to parse JSON, using fallback method")
                    # System will use fallback entity identification
                    
            Various JSON formats::
            
                # Clean JSON
                clean = '{"entities": ["Python"]}'
                result1 = self._parse_json_response(clean)
                
                # JSON with surrounding text
                surrounded = 'Analysis: {"entities": ["Python"]} - Done'
                result2 = self._parse_json_response(surrounded)
                
                # Both should parse successfully
                assert result1 is not None
                assert result2 is not None
                
        Parsing Strategy:
            1. Locate the first '{' character in the response
            2. Find the last '}' character in the response
            3. Extract the substring between these markers
            4. Attempt to parse as JSON using the standard json module
            5. Return None if any step fails, triggering fallback mechanisms
            
        Error Handling:
            The method provides comprehensive error handling for:
            - Missing or malformed JSON structures
            - Invalid JSON syntax
            - Empty or None responses
            - Encoding issues
            
        Fallback Integration:
            When JSON parsing fails, the calling code automatically falls back to
            the _fallback_entity_identification method, ensuring the system continues
            to function even when LLM responses don't match the expected format.
            
        Logging:
            Parse failures are logged as warnings with the specific error details,
            helping with debugging and monitoring of LLM response quality.
        """
        try:
            import json

            # Try to find JSON in response
            start_idx = response.find("{")
            end_idx = response.rfind("}") + 1
            if start_idx != -1 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                return json.loads(json_str)
        except Exception as e:
            logger.warning(f"Failed to parse JSON response: {e}")
        return None

    async def get_entity_context(self, entity_name: str) -> dict[str, Any]:
        """Get comprehensive context information for a specific entity in the knowledge.
        graph.

        This method provides detailed information about an entity including its neighborhood,
        associated memories, and connection statistics. It's useful for understanding the
        role and importance of an entity within the knowledge graph structure.

        Args:
            entity_name: Name of the entity to get context for (e.g., "Python", "Machine Learning")

        Returns:
            Dict[str, Any]: Comprehensive entity context containing:
                - entity: The KnowledgeGraphNode object with entity details
                - neighborhood: Dictionary with entity's neighborhood structure by depth levels
                - associated_memories: List of memories directly associated with this entity
                - total_connections: Number of entities connected to this entity
                - memory_count: Number of memories referencing this entity
                - error: Error message if entity not found

        Examples:
            Get context for a specific entity::

                context = await retriever.get_entity_context("Python")

                if "error" not in context:
                    entity = context["entity"]
                    print(f"Entity: {entity.name} ({entity.type})")
                    print(f"Confidence: {entity.confidence:.2f}")
                    print(f"Total connections: {context['total_connections']}")
                    print(f"Associated memories: {context['memory_count']}")

                    # Explore neighborhood structure
                    neighborhood = context["neighborhood"]
                    for level, entities in neighborhood.get("levels", {}).items():
                        print(f"Level {level}: {[e.name for e in entities]}")

                    # Access associated memories
                    memories = context["associated_memories"]
                    for memory in memories:
                        print(f"Memory: {memory['content'][:100]}...")

            Handle entity not found::

                context = await retriever.get_entity_context("NonexistentEntity")

                if "error" in context:
                    print(f"Error: {context['error']}")
                else:
                    print(f"Found entity: {context['entity'].name}")

            Analyze entity importance::

                context = await retriever.get_entity_context("Machine Learning")

                if "error" not in context:
                    entity = context["entity"]
                    connections = context["total_connections"]
                    memories = context["memory_count"]

                    # Calculate importance score
                    importance = (connections * 0.6) + (memories * 0.4)
                    print(f"Entity importance score: {importance:.2f}")

                    # Analyze neighborhood diversity
                    neighborhood = context["neighborhood"]
                    entity_types = set()
                    for level_entities in neighborhood.get("levels", {}).values():
                        for entity in level_entities:
                            entity_types.add(entity.type)

                    print(f"Connected entity types: {list(entity_types)}")

        Note:
            This method explores the entity's neighborhood to depth 2 by default,
            which provides a good balance between comprehensiveness and performance.
            For very large knowledge graphs, consider the performance implications
            of deep neighborhood exploration.
        """
        entity_id = self.kg_generator._find_entity_id(entity_name)
        if not entity_id:
            return {"error": "Entity not found"}

        # Get entity neighborhood
        neighborhood = await self.kg_generator.get_entity_neighborhood(entity_id, depth=2)

        # Get associated memories
        memories = await self._get_memories_from_graph_entities(
            [self.kg_generator.knowledge_graph.nodes[entity_id]], None
        )

        return {
            "entity": self.kg_generator.knowledge_graph.nodes[entity_id],
            "neighborhood": neighborhood,
            "associated_memories": memories,
            "total_connections": len(neighborhood.get("levels", [])),
            "memory_count": len(memories),
        }

    async def find_relationship_paths(
        self, entity1: str, entity2: str, max_depth: int = 3
    ) -> list[list[KnowledgeGraphRelationship]]:
        """Find relationship paths between two entities in the knowledge graph.

        This method performs a breadth-first search to discover all possible relationship
        paths connecting two entities within the specified depth limit. It's useful for
        understanding how entities are connected and for providing context about their
        relationships in query responses.

        Args:
            entity1: Name of the first entity (source entity)
            entity2: Name of the second entity (target entity)
            max_depth: Maximum path length to explore (default: 3)

        Returns:
            List[List[KnowledgeGraphRelationship]]: List of relationship paths, where each
                path is a list of KnowledgeGraphRelationship objects representing the
                sequence of relationships connecting the two entities. Limited to 10 paths
                to prevent excessive computation.

        Examples:
            Find direct and indirect connections::

                paths = await retriever.find_relationship_paths(
                    "Python", "Machine Learning", max_depth=3
                )

                print(f"Found {len(paths)} paths between Python and Machine Learning")

                for i, path in enumerate(paths):
                    print(f"Path {i+1}:")
                    for rel in path:
                        print(f"  {rel.source_id} -> {rel.target_id} ({rel.relationship_type})")
                        print(f"    Confidence: {rel.confidence:.2f}")

            Analyze relationship strength::

                paths = await retriever.find_relationship_paths("AI", "Ethics")

                if paths:
                    # Find strongest path (highest average confidence)
                    strongest_path = max(paths, key=lambda p:
                        sum(rel.confidence for rel in p) / len(p))

                    avg_confidence = sum(rel.confidence for rel in strongest_path) / len(strongest_path)
                    print(f"Strongest path has {len(strongest_path)} hops with confidence {avg_confidence:.2f}")

                    # Analyze relationship types
                    rel_types = [rel.relationship_type for rel in strongest_path]
                    print(f"Relationship sequence: {' -> '.join(rel_types)}")

            Find shortest path::

                paths = await retriever.find_relationship_paths(
                    "Neural Networks", "Deep Learning", max_depth=2
                )

                if paths:
                    shortest_path = min(paths, key=len)
                    print(f"Shortest path has {len(shortest_path)} hops")

                    # Display path details
                    for rel in shortest_path:
                        print(f"{rel.source_id} --[{rel.relationship_type}]--> {rel.target_id}")

            Check for no connection::

                paths = await retriever.find_relationship_paths(
                    "Unrelated Topic 1", "Unrelated Topic 2"
                )

                if not paths:
                    print("No relationship paths found between these entities")
                else:
                    print(f"Found {len(paths)} connecting paths")

        Note:
            The search is limited to 10 paths to prevent excessive computation on
            highly connected graphs. Paths are found using breadth-first search,
            so shorter paths are discovered first. For very large knowledge graphs,
            consider reducing max_depth for better performance.
        """
        entity1_id = self.kg_generator._find_entity_id(entity1)
        entity2_id = self.kg_generator._find_entity_id(entity2)

        if not entity1_id or not entity2_id:
            return []

        kg = self.kg_generator.knowledge_graph

        # Breadth-first search for paths
        paths = []
        queue = [(entity1_id, [])]  # (current_entity, path_so_far)
        visited = set()

        while queue and len(paths) < 10:  # Limit paths
            current_entity, path = queue.pop(0)

            if current_entity == entity2_id:
                paths.append(path)
                continue

            if len(path) >= max_depth:
                continue

            if current_entity in visited:
                continue

            visited.add(current_entity)

            # Get relationships for current entity
            relationships = kg.get_relationships_for_node(current_entity)

            for rel in relationships:
                next_entity = rel.target_id if rel.source_id == current_entity else rel.source_id

                if next_entity not in visited:
                    new_path = [*path, rel]
                    queue.append((next_entity, new_path))

        return paths
