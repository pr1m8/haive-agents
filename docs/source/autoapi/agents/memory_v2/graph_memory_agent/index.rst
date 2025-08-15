agents.memory_v2.graph_memory_agent
===================================

.. py:module:: agents.memory_v2.graph_memory_agent

.. autoapi-nested-parse::

   Graph Memory Agent with LLMGraphTransformer, TNT, and Graph RAG.

   This implementation combines:
   1. Graph transformation for structured knowledge extraction
   2. Text-to-Neo4j (TNT) capabilities for direct graph database storage
   3. Graph RAG for intelligent querying of the knowledge graph


   .. autolink-examples:: agents.memory_v2.graph_memory_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.graph_memory_agent.HAS_GRAPH_DB_RAG
   agents.memory_v2.graph_memory_agent.HAS_GRAPH_TRANSFORMER
   agents.memory_v2.graph_memory_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.graph_memory_agent.GraphMemoryAgent
   agents.memory_v2.graph_memory_agent.GraphMemoryConfig
   agents.memory_v2.graph_memory_agent.GraphMemoryMode


Functions
---------

.. autoapisummary::

   agents.memory_v2.graph_memory_agent.example_graph_memory


Module Contents
---------------

.. py:class:: GraphMemoryAgent(config: GraphMemoryConfig)

   Agent that manages memory using a knowledge graph.

   This agent provides:
   - Entity and relationship extraction from text
   - Direct storage to Neo4j (TNT - Text to Neo4j)
   - Graph-based retrieval using Cypher queries
   - Vector similarity search on graph nodes
   - Complex graph traversal for memory retrieval


   .. autolink-examples:: GraphMemoryAgent
      :collapse:

   .. py:method:: _create_graph_constraints()

      Create constraints and indexes for the graph.


      .. autolink-examples:: _create_graph_constraints
         :collapse:


   .. py:method:: _get_query_context(cypher_query: str) -> dict[str, Any]

      Get additional context around query results.


      .. autolink-examples:: _get_query_context
         :collapse:


   .. py:method:: _init_graph_transformer()

      Initialize the graph transformer for entity extraction.


      .. autolink-examples:: _init_graph_transformer
         :collapse:


   .. py:method:: _init_neo4j()

      Initialize Neo4j connection.


      .. autolink-examples:: _init_neo4j
         :collapse:


   .. py:method:: _init_rag_components()

      Initialize Graph RAG components.


      .. autolink-examples:: _init_rag_components
         :collapse:


   .. py:method:: _init_vector_index()

      Initialize vector index for semantic search on graph.


      .. autolink-examples:: _init_vector_index
         :collapse:


   .. py:method:: as_tool(config: GraphMemoryConfig)
      :classmethod:


      Convert to a LangChain tool for use in other agents.


      .. autolink-examples:: as_tool
         :collapse:


   .. py:method:: consolidate_memories(time_window: str | None = '1 day', min_connections: int = 2) -> dict[str, Any]
      :async:


      Consolidate related memories into higher-level concepts.

      :param time_window: Time window for consolidation
      :param min_connections: Minimum connections for consolidation

      :returns: Consolidation results


      .. autolink-examples:: consolidate_memories
         :collapse:


   .. py:method:: extract_graph_from_text(text: str, metadata: dict[str, Any] | None = None) -> list[langchain_neo4j.graphs.graph_document.GraphDocument]
      :async:


      Extract entities and relationships from text.

      :param text: Input text to process
      :param metadata: Optional metadata to attach

      :returns: List of GraphDocument objects


      .. autolink-examples:: extract_graph_from_text
         :collapse:


   .. py:method:: get_memory_subgraph(entity_name: str, max_depth: int = 2, relationship_types: list[str] | None = None) -> dict[str, Any]
      :async:


      Get a subgraph centered around an entity.

      :param entity_name: Name of the central entity
      :param max_depth: Maximum traversal depth
      :param relationship_types: Optional filter for relationship types

      :returns: Subgraph data


      .. autolink-examples:: get_memory_subgraph
         :collapse:


   .. py:method:: query_graph(query: str, query_type: str = 'natural', include_context: bool = True) -> dict[str, Any]
      :async:


      Query the graph using natural language or Cypher.

      :param query: Query string (natural language or Cypher)
      :param query_type: "natural" or "cypher"
      :param include_context: Include surrounding context in results

      :returns: Query results with optional context


      .. autolink-examples:: query_graph
         :collapse:


   .. py:method:: run(input_text: str, mode: GraphMemoryMode | None = None, auto_store: bool = True) -> dict[str, Any]
      :async:


      Main entry point for the agent.

      :param input_text: Input text to process
      :param mode: Override default mode
      :param auto_store: Automatically store extracted graph

      :returns: Processing results


      .. autolink-examples:: run
         :collapse:


   .. py:method:: search_similar_memories(query: str, node_type: str | None = None, k: int = 5) -> list[dict[str, Any]]
      :async:


      Search for similar memories using vector similarity.

      :param query: Search query
      :param node_type: Optional node type to search (Person, Concept, etc.)
      :param k: Number of results

      :returns: Similar memories with scores


      .. autolink-examples:: search_similar_memories
         :collapse:


   .. py:method:: store_graph_documents(graph_documents: list[langchain_neo4j.graphs.graph_document.GraphDocument], merge_nodes: bool = True) -> dict[str, Any]
      :async:


      Store graph documents in Neo4j (TNT - Text to Neo4j).

      :param graph_documents: Graph documents to store
      :param merge_nodes: Whether to merge with existing nodes

      :returns: Storage statistics


      .. autolink-examples:: store_graph_documents
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: logger


.. py:class:: GraphMemoryConfig

   Configuration for GraphMemoryAgent.


   .. autolink-examples:: GraphMemoryConfig
      :collapse:

   .. py:method:: __post_init__()


   .. py:attribute:: allowed_nodes
      :type:  list[str]
      :value: ['Person', 'Organization', 'Location', 'Event', 'Concept', 'Product', 'Technology', 'Date',...



   .. py:attribute:: allowed_relationships
      :type:  list[tuple[str, str, str]]
      :value: [('Person', 'WORKS_FOR', 'Organization'), ('Person', 'KNOWS', 'Person'), ('Person',...



   .. py:attribute:: database_name
      :type:  str
      :value: 'neo4j'



   .. py:attribute:: embedding_model
      :type:  str
      :value: 'openai'



   .. py:attribute:: enable_vector_index
      :type:  bool
      :value: True



   .. py:attribute:: extract_properties
      :type:  bool
      :value: True



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: mode
      :type:  GraphMemoryMode


   .. py:attribute:: neo4j_password
      :type:  str
      :value: 'password'



   .. py:attribute:: neo4j_uri
      :type:  str
      :value: 'bolt://localhost:7687'



   .. py:attribute:: neo4j_username
      :type:  str
      :value: 'neo4j'



   .. py:attribute:: node_properties
      :type:  list[str]
      :value: ['role', 'description', 'date', 'importance', 'confidence']



   .. py:attribute:: relationship_properties
      :type:  list[str]
      :value: ['since', 'until', 'strength', 'context']



   .. py:attribute:: user_id
      :type:  str
      :value: 'default_user'



.. py:class:: GraphMemoryMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Modes of operation for the graph memory agent.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphMemoryMode
      :collapse:

   .. py:attribute:: EXTRACT_AND_STORE
      :value: 'extract_and_store'



   .. py:attribute:: EXTRACT_ONLY
      :value: 'extract_only'



   .. py:attribute:: FULL
      :value: 'full'



   .. py:attribute:: QUERY_ONLY
      :value: 'query_only'



   .. py:attribute:: STORE_ONLY
      :value: 'store_only'



.. py:function:: example_graph_memory()
   :async:


   Example of using GraphMemoryAgent.


   .. autolink-examples:: example_graph_memory
      :collapse:

.. py:data:: HAS_GRAPH_DB_RAG
   :value: True


.. py:data:: HAS_GRAPH_TRANSFORMER
   :value: True


.. py:data:: logger

