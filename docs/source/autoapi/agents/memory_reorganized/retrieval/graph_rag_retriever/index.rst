agents.memory_reorganized.retrieval.graph_rag_retriever
=======================================================

.. py:module:: agents.memory_reorganized.retrieval.graph_rag_retriever

.. autoapi-nested-parse::

   Graph RAG Retriever for Memory System.

   This module implements a Graph RAG retriever that combines knowledge graph traversal
   with vector similarity search to provide comprehensive memory retrieval with
   relationship context and semantic understanding.


   .. autolink-examples:: agents.memory_reorganized.retrieval.graph_rag_retriever
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.retrieval.graph_rag_retriever.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGResult
   agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGRetriever
   agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGRetrieverConfig


Module Contents
---------------

.. py:class:: GraphRAGResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive result from Graph RAG retrieval combining knowledge graph and vector.
   search.

   This class encapsulates all information from a Graph RAG retrieval operation,
   including retrieved memories, graph traversal results, scoring information,
   and performance metrics for analysis and optimization.

   .. attribute:: query

      Original user query that was processed

   .. attribute:: memories

      Retrieved memories from both vector and graph sources

   .. attribute:: start_entities

      Initial entities identified in the query for graph traversal

   .. attribute:: traversed_entities

      All entities explored during graph traversal

   .. attribute:: relationship_paths

      Relationship paths discovered during graph traversal

   .. attribute:: graph_nodes_explored

      Number of graph nodes explored (for testing compatibility)

   .. attribute:: graph_paths

      Alias for relationship_paths (for backward compatibility)

   .. attribute:: similarity_scores

      Vector similarity scores for each memory

   .. attribute:: graph_scores

      Graph centrality scores for each memory

   .. attribute:: final_scores

      Combined final scores used for ranking

   .. attribute:: total_time_ms

      Total processing time for the entire operation

   .. attribute:: graph_traversal_time_ms

      Time spent on graph traversal

   .. attribute:: vector_search_time_ms

      Time spent on vector search

   .. attribute:: query_intent

      Analyzed query intent and characteristics

   .. attribute:: expansion_terms

      Query expansion terms used for enhanced retrieval

   .. rubric:: Examples

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

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphRAGResult
      :collapse:

   .. py:method:: get_top_memories(limit: int = 10) -> list[dict[str, Any]]

      Get top memories by final score with ranking.

      :param limit: Maximum number of memories to return

      :returns: Top memories sorted by final score
      :rtype: List[Dict[str, Any]]

      .. rubric:: Examples

      Get top memories::

          result = await retriever.retrieve_memories("Python programming")
          top_memories = result.get_top_memories(limit=5)

          for i, memory in enumerate(top_memories):
              print(f"Top {i+1}: {memory['content'][:50]}...")


      .. autolink-examples:: get_top_memories
         :collapse:


   .. py:attribute:: expansion_terms
      :type:  list[str]
      :value: None



   .. py:attribute:: final_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: graph_nodes_explored
      :type:  int
      :value: None



   .. py:attribute:: graph_paths
      :type:  list[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphRelationship]]
      :value: None



   .. py:attribute:: graph_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: graph_traversal_time_ms
      :type:  float
      :value: None



   .. py:attribute:: memories
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: query_intent
      :type:  haive.agents.memory.kg_generator_agent.Optional[haive.agents.memory.core.types.MemoryQueryIntent]
      :value: None



   .. py:attribute:: relationship_paths
      :type:  list[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphRelationship]]
      :value: None



   .. py:attribute:: similarity_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: start_entities
      :type:  list[haive.agents.memory.kg_generator_agent.KnowledgeGraphNode]
      :value: None



   .. py:attribute:: total_time_ms
      :type:  float
      :value: None



   .. py:attribute:: traversed_entities
      :type:  list[haive.agents.memory.kg_generator_agent.KnowledgeGraphNode]
      :value: None



   .. py:attribute:: vector_search_time_ms
      :type:  float
      :value: None



.. py:class:: GraphRAGRetriever(config: GraphRAGRetrieverConfig)

   Advanced Graph RAG retriever that combines knowledge graph traversal with vector.
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

   .. attribute:: config

      Configuration object with all retrieval settings

   .. attribute:: memory_store

      Memory store manager for basic storage operations

   .. attribute:: classifier

      Memory classifier for query intent analysis

   .. attribute:: kg_generator

      Knowledge graph generator for entity and relationship data

   .. attribute:: llm

      LLM runnable for query analysis and entity identification

   .. attribute:: entity_identification_prompt

      Prompt template for entity identification

   .. attribute:: relationship_path_analysis_prompt

      Prompt template for path analysis

   .. rubric:: Examples

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

   .. note::

      The retriever automatically balances graph traversal depth and performance
      based on the configuration. For large knowledge graphs, consider reducing
      max_traversal_depth and increasing min_relationship_confidence for better
      performance.

   Initialize the Graph RAG retriever with comprehensive configuration.

   Sets up all components needed for Graph RAG retrieval including memory stores,
   knowledge graph generators, LLM for query analysis, and prompt templates.

   :param config: GraphRAGRetrieverConfig with all necessary components and settings

   :raises ValueError: If required components are missing in config

   .. rubric:: Examples

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

   .. note::

      The retriever validates all required components during initialization
      and sets up optimized prompt templates for entity identification and
      relationship path analysis.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphRAGRetriever
      :collapse:

   .. py:method:: _build_expanded_query(original_query: str, expansion_terms: list[str]) -> str

      Build expanded query with additional terms.


      .. autolink-examples:: _build_expanded_query
         :collapse:


   .. py:method:: _calculate_graph_centrality_score(memory: dict[str, Any], entity_lookup: dict[str, haive.agents.memory.kg_generator_agent.KnowledgeGraphNode], relationship_paths: list[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphRelationship]]) -> float

      Calculate graph centrality score for a memory.


      .. autolink-examples:: _calculate_graph_centrality_score
         :collapse:


   .. py:method:: _combine_memories(vector_memories: list[dict[str, Any]], graph_memories: list[dict[str, Any]]) -> list[dict[str, Any]]

      Combine and deduplicate memories from vector and graph sources.


      .. autolink-examples:: _combine_memories
         :collapse:


   .. py:method:: _fallback_entity_identification(query: str, known_entities: list[str]) -> dict[str, Any]

      Fallback entity identification using simple matching.


      .. autolink-examples:: _fallback_entity_identification
         :collapse:


   .. py:method:: _get_memories_from_graph_entities(entities: list[haive.agents.memory.kg_generator_agent.KnowledgeGraphNode], namespace: tuple[str, Ellipsis] | None) -> list[dict[str, Any]]
      :async:


      Get memories associated with graph entities.


      .. autolink-examples:: _get_memories_from_graph_entities
         :collapse:


   .. py:method:: _identify_query_entities(query: str) -> dict[str, Any]
      :async:


      Identify entities mentioned in the query.


      .. autolink-examples:: _identify_query_entities
         :collapse:


   .. py:method:: _parse_json_response(response: str) -> dict[str, Any] | None

      Parse JSON response from LLM.


      .. autolink-examples:: _parse_json_response
         :collapse:


   .. py:method:: _perform_graph_traversal(direct_entities: list[str], related_entities: list[str], max_depth: int) -> tuple[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphNode], list[haive.agents.memory.kg_generator_agent.KnowledgeGraphNode], list[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphRelationship]]]
      :async:


      Perform graph traversal to find related entities.


      .. autolink-examples:: _perform_graph_traversal
         :collapse:


   .. py:method:: _score_memories(memories: list[dict[str, Any]], query: str, graph_entities: list[haive.agents.memory.kg_generator_agent.KnowledgeGraphNode], relationship_paths: list[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphRelationship]]) -> tuple[list[dict[str, Any]], list[float], list[float], list[float]]
      :async:


      Score memories using combined vector similarity and graph centrality.


      .. autolink-examples:: _score_memories
         :collapse:


   .. py:method:: _setup_prompts() -> None

      Setup prompts for query analysis and expansion.


      .. autolink-examples:: _setup_prompts
         :collapse:


   .. py:method:: find_relationship_paths(entity1: str, entity2: str, max_depth: int = 3) -> list[list[haive.agents.memory.kg_generator_agent.KnowledgeGraphRelationship]]
      :async:


      Find relationship paths between two entities in the knowledge graph.

      This method performs a breadth-first search to discover all possible relationship
      paths connecting two entities within the specified depth limit. It's useful for
      understanding how entities are connected and for providing context about their
      relationships in query responses.

      :param entity1: Name of the first entity (source entity)
      :param entity2: Name of the second entity (target entity)
      :param max_depth: Maximum path length to explore (default: 3)

      :returns:

                List of relationship paths, where each
                    path is a list of KnowledgeGraphRelationship objects representing the
                    sequence of relationships connecting the two entities. Limited to 10 paths
                    to prevent excessive computation.
      :rtype: List[List[KnowledgeGraphRelationship]]

      .. rubric:: Examples

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

      .. note::

         The search is limited to 10 paths to prevent excessive computation on
         highly connected graphs. Paths are found using breadth-first search,
         so shorter paths are discovered first. For very large knowledge graphs,
         consider reducing max_depth for better performance.


      .. autolink-examples:: find_relationship_paths
         :collapse:


   .. py:method:: get_entity_context(entity_name: str) -> dict[str, Any]
      :async:


      Get comprehensive context information for a specific entity in the knowledge.
      graph.

      This method provides detailed information about an entity including its neighborhood,
      associated memories, and connection statistics. It's useful for understanding the
      role and importance of an entity within the knowledge graph structure.

      :param entity_name: Name of the entity to get context for (e.g., "Python", "Machine Learning")

      :returns:

                Comprehensive entity context containing:
                    - entity: The KnowledgeGraphNode object with entity details
                    - neighborhood: Dictionary with entity's neighborhood structure by depth levels
                    - associated_memories: List of memories directly associated with this entity
                    - total_connections: Number of entities connected to this entity
                    - memory_count: Number of memories referencing this entity
                    - error: Error message if entity not found
      :rtype: Dict[str, Any]

      .. rubric:: Examples

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

      .. note::

         This method explores the entity's neighborhood to depth 2 by default,
         which provides a good balance between comprehensiveness and performance.
         For very large knowledge graphs, consider the performance implications
         of deep neighborhood exploration.


      .. autolink-examples:: get_entity_context
         :collapse:


   .. py:method:: retrieve_memories(query: str, limit: haive.agents.memory.kg_generator_agent.Optional[int] = None, memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None, namespace: tuple[str, Ellipsis] | None = None, enable_graph_traversal: bool = True, max_graph_depth: haive.agents.memory.kg_generator_agent.Optional[int] = None) -> GraphRAGResult
      :async:


      Retrieve memories using Graph RAG approach.

      :param query: User query
      :param limit: Maximum number of memories to retrieve
      :param memory_types: Specific memory types to focus on
      :param namespace: Memory namespace to search
      :param enable_graph_traversal: Whether to use graph traversal
      :param max_graph_depth: Maximum depth for graph traversal (overrides config)

      :returns: GraphRAGResult with retrieved memories and graph context


      .. autolink-examples:: retrieve_memories
         :collapse:


   .. py:attribute:: classifier


   .. py:attribute:: config


   .. py:attribute:: kg_generator


   .. py:attribute:: llm


   .. py:attribute:: memory_store


.. py:class:: GraphRAGRetrieverConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Graph RAG retriever with comprehensive customization options.

   This configuration class defines all parameters needed to create and configure
   a GraphRAGRetriever, including core components, graph traversal settings,
   scoring weights, and query expansion parameters.

   .. attribute:: memory_store_manager

      Manager for memory storage and retrieval operations

   .. attribute:: memory_classifier

      Classifier for analyzing query intent and memory types

   .. attribute:: kg_generator

      Knowledge graph generator for entity and relationship extraction

   .. attribute:: default_limit

      Default number of memories to retrieve per query

   .. attribute:: max_limit

      Maximum number of memories that can be retrieved

   .. attribute:: max_traversal_depth

      Maximum depth for graph traversal (prevents infinite loops)

   .. attribute:: min_relationship_confidence

      Minimum confidence score for relationships to traverse

   .. attribute:: enable_bidirectional_traversal

      Whether to traverse relationships in both directions

   .. attribute:: similarity_weight

      Weight for vector similarity score in final ranking (0.0-1.0)

   .. attribute:: graph_weight

      Weight for graph centrality score in final ranking (0.0-1.0)

   .. attribute:: importance_weight

      Weight for memory importance score in final ranking (0.0-1.0)

   .. attribute:: recency_weight

      Weight for memory recency score in final ranking (0.0-1.0)

   .. attribute:: enable_query_expansion

      Whether to enable query expansion with related terms

   .. attribute:: max_expansion_terms

      Maximum number of terms to add during query expansion

   .. attribute:: llm_config

      LLM configuration for query analysis and entity identification

   .. rubric:: Examples

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

   .. note::

      The scoring weights (similarity_weight, graph_weight, importance_weight, recency_weight)
      should sum to 1.0 for optimal result ranking. The system will normalize them if needed.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphRAGRetrieverConfig
      :collapse:

   .. py:attribute:: default_limit
      :type:  int
      :value: None



   .. py:attribute:: enable_bidirectional_traversal
      :type:  bool
      :value: None



   .. py:attribute:: enable_query_expansion
      :type:  bool
      :value: None



   .. py:attribute:: graph_weight
      :type:  float
      :value: None



   .. py:attribute:: importance_weight
      :type:  float
      :value: None



   .. py:attribute:: kg_generator
      :type:  haive.agents.memory.kg_generator_agent.KGGeneratorAgent
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_expansion_terms
      :type:  int
      :value: None



   .. py:attribute:: max_limit
      :type:  int
      :value: None



   .. py:attribute:: max_traversal_depth
      :type:  int
      :value: None



   .. py:attribute:: memory_classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: memory_store_manager
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: min_relationship_confidence
      :type:  float
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: recency_weight
      :type:  float
      :value: None



   .. py:attribute:: similarity_weight
      :type:  float
      :value: None



.. py:data:: logger

