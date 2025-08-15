agents.memory_v2.kg_memory_agent
================================

.. py:module:: agents.memory_v2.kg_memory_agent

.. autoapi-nested-parse::

   Knowledge Graph Memory Agent with Graph Database Integration.

   This agent extends the existing KG transformer capabilities with:
   1. Graph database upload and storage (Neo4j, Neptune, etc.)
   2. Memory-specific knowledge graph construction
   3. Time-weighted graph retrieval
   4. Configurable storage backends

   Based on existing ParallelKGTransformer but optimized for memory workflows.


   .. autolink-examples:: agents.memory_v2.kg_memory_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.kg_memory_agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.kg_memory_agent.GraphDatabaseConnector
   agents.memory_v2.kg_memory_agent.GraphStorageBackend
   agents.memory_v2.kg_memory_agent.KGMemoryAgent
   agents.memory_v2.kg_memory_agent.KGMemoryConfig


Functions
---------

.. autoapisummary::

   agents.memory_v2.kg_memory_agent.create_memory_kg_agent
   agents.memory_v2.kg_memory_agent.create_neo4j_memory_agent


Module Contents
---------------

.. py:class:: GraphDatabaseConnector(config: KGMemoryConfig)

   Abstract connector for graph databases.

   Initialize connector with configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphDatabaseConnector
      :collapse:

   .. py:method:: _connect_file_storage() -> None
      :async:


      Initialize file-based storage.


      .. autolink-examples:: _connect_file_storage
         :collapse:


   .. py:method:: _connect_neo4j() -> None
      :async:


      Connect to Neo4j database.


      .. autolink-examples:: _connect_neo4j
         :collapse:


   .. py:method:: _store_file(graph: haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph, graph_id: str, metadata: dict[str, Any]) -> bool
      :async:


      Store graph in file.


      .. autolink-examples:: _store_file
         :collapse:


   .. py:method:: _store_memory(graph: haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph, graph_id: str, metadata: dict[str, Any]) -> bool
      :async:


      Store graph in memory.


      .. autolink-examples:: _store_memory
         :collapse:


   .. py:method:: _store_neo4j(graph: haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph, graph_id: str, metadata: dict[str, Any]) -> bool
      :async:


      Store graph in Neo4j.


      .. autolink-examples:: _store_neo4j
         :collapse:


   .. py:method:: close() -> None
      :async:


      Close database connection.


      .. autolink-examples:: close
         :collapse:


   .. py:method:: connect() -> None
      :async:


      Connect to graph database.


      .. autolink-examples:: connect
         :collapse:


   .. py:method:: retrieve_graph(graph_id: str) -> tuple[haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph, dict[str, Any]] | None
      :async:


      Retrieve knowledge graph by ID.


      .. autolink-examples:: retrieve_graph
         :collapse:


   .. py:method:: store_knowledge_graph(graph: haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph, graph_id: str, metadata: dict[str, Any] | None = None) -> bool
      :async:


      Store knowledge graph in configured backend.


      .. autolink-examples:: store_knowledge_graph
         :collapse:


   .. py:attribute:: _connection
      :value: None



   .. py:attribute:: backend


   .. py:attribute:: config


.. py:class:: GraphStorageBackend

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Supported graph database backends.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphStorageBackend
      :collapse:

   .. py:attribute:: ARANGODB
      :value: 'arango'



   .. py:attribute:: FILE
      :value: 'file'



   .. py:attribute:: MEMORY
      :value: 'memory'



   .. py:attribute:: NEO4J
      :value: 'neo4j'



   .. py:attribute:: NEPTUNE
      :value: 'neptune'



.. py:class:: KGMemoryAgent(config: KGMemoryConfig)

   Knowledge Graph Memory Agent with database integration.

   Initialize KG Memory Agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KGMemoryAgent
      :collapse:

   .. py:method:: _query_memory_entity(entity_name: str) -> list[dict[str, Any]]
      :async:


      Query memory storage for entity relationships.


      .. autolink-examples:: _query_memory_entity
         :collapse:


   .. py:method:: _query_neo4j_entity(entity_name: str) -> list[dict[str, Any]]
      :async:


      Query Neo4j for entity relationships.


      .. autolink-examples:: _query_neo4j_entity
         :collapse:


   .. py:method:: close() -> None
      :async:


      Close agent and database connections.


      .. autolink-examples:: close
         :collapse:


   .. py:method:: process_conversation_to_graph(messages: list[langchain_core.messages.BaseMessage], graph_id: str | None = None) -> tuple[str, haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph]
      :async:


      Process conversation messages into knowledge graph.

      :param messages: Conversation messages
      :param graph_id: Optional graph ID

      :returns: Tuple of (graph_id, knowledge_graph)


      .. autolink-examples:: process_conversation_to_graph
         :collapse:


   .. py:method:: process_memories_to_graph(memories: list[agents.memory_v2.memory_state_original.EnhancedMemoryItem], graph_id: str | None = None) -> tuple[str, haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph]
      :async:


      Process memories into knowledge graph and store.

      :param memories: List of memory items to process
      :param graph_id: Optional graph ID (generated if not provided)

      :returns: Tuple of (graph_id, knowledge_graph)


      .. autolink-examples:: process_memories_to_graph
         :collapse:


   .. py:method:: query_graph_by_entity(entity_name: str) -> list[dict[str, Any]]
      :async:


      Query graph database for entity and its relationships.

      :param entity_name: Name of entity to query

      :returns: List of related entities and relationships


      .. autolink-examples:: query_graph_by_entity
         :collapse:


   .. py:method:: retrieve_memory_graph(graph_id: str) -> haive.agents.document_modifiers.kg.kg_map_merge.models.KnowledgeGraph | None
      :async:


      Retrieve stored knowledge graph.

      :param graph_id: ID of graph to retrieve

      :returns: KnowledgeGraph if found, None otherwise


      .. autolink-examples:: retrieve_memory_graph
         :collapse:


   .. py:method:: setup() -> None
      :async:


      Setup agent and connections.


      .. autolink-examples:: setup
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: db_connector


   .. py:attribute:: graph_transformer


   .. py:attribute:: message_converter


.. py:class:: KGMemoryConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for KG Memory Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KGMemoryConfig
      :collapse:

   .. py:attribute:: confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: extract_properties
      :type:  bool
      :value: None



   .. py:attribute:: file_storage_path
      :type:  str | None
      :value: None



   .. py:attribute:: include_importance_weights
      :type:  bool
      :value: None



   .. py:attribute:: include_source_tracking
      :type:  bool
      :value: None



   .. py:attribute:: include_temporal_info
      :type:  bool
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: memory_node_types
      :type:  list[str]
      :value: None



   .. py:attribute:: memory_relationships
      :type:  list[str | tuple[str, str, str]]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: neo4j_database
      :type:  str
      :value: None



   .. py:attribute:: neo4j_password
      :type:  str | None
      :value: None



   .. py:attribute:: neo4j_uri
      :type:  str | None
      :value: None



   .. py:attribute:: neo4j_username
      :type:  str | None
      :value: None



   .. py:attribute:: storage_backend
      :type:  GraphStorageBackend
      :value: None



   .. py:attribute:: strict_mode
      :type:  bool
      :value: None



.. py:function:: create_memory_kg_agent(storage_backend: str = 'memory', llm_config: haive.core.engine.aug_llm.AugLLMConfig = None, **storage_kwargs) -> KGMemoryAgent

   Factory function to create KG Memory Agent.

   :param storage_backend: "memory", "neo4j", "file"
   :param llm_config: LLM configuration
   :param \*\*storage_kwargs: Backend-specific settings

   :returns: Configured KGMemoryAgent


   .. autolink-examples:: create_memory_kg_agent
      :collapse:

.. py:function:: create_neo4j_memory_agent(uri: str, username: str, password: str, database: str = 'neo4j', llm_config: haive.core.engine.aug_llm.AugLLMConfig = None) -> KGMemoryAgent

   Create KG Memory Agent with Neo4j backend.

   :param uri: Neo4j connection URI
   :param username: Database username
   :param password: Database password
   :param database: Database name
   :param llm_config: LLM configuration

   :returns: KGMemoryAgent configured for Neo4j


   .. autolink-examples:: create_neo4j_memory_agent
      :collapse:

.. py:data:: logger

