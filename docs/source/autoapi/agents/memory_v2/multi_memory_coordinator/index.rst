agents.memory_v2.multi_memory_coordinator
=========================================

.. py:module:: agents.memory_v2.multi_memory_coordinator

.. autoapi-nested-parse::

   Multi-Memory Agent Coordinator - Orchestrates all memory systems.

   This is the top-level coordinator that manages all memory agents:
   - SimpleMemoryAgent (pre-hook system)
   - ReactMemoryAgent (tool-based memory)
   - LongTermMemoryAgent (persistent memory)
   - GraphMemoryAgent (structured knowledge)
   - AdvancedRAGMemoryAgent (multi-stage retrieval)

   The coordinator intelligently routes operations to the most appropriate
   memory system and can combine results from multiple systems.


   .. autolink-examples:: agents.memory_v2.multi_memory_coordinator
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.multi_memory_coordinator.HAS_ADVANCED_RAG
   agents.memory_v2.multi_memory_coordinator.HAS_GRAPH_MEMORY
   agents.memory_v2.multi_memory_coordinator.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.multi_memory_coordinator.CoordinationMode
   agents.memory_v2.multi_memory_coordinator.MemorySystemType
   agents.memory_v2.multi_memory_coordinator.MultiMemoryConfig
   agents.memory_v2.multi_memory_coordinator.MultiMemoryCoordinator


Functions
---------

.. autoapisummary::

   agents.memory_v2.multi_memory_coordinator.demo_multi_memory_coordinator


Module Contents
---------------

.. py:class:: CoordinationMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Memory coordination modes.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CoordinationMode
      :collapse:

   .. py:attribute:: CONSENSUS
      :value: 'consensus'



   .. py:attribute:: EXPLICIT
      :value: 'explicit'



   .. py:attribute:: HIERARCHICAL
      :value: 'hierarchical'



   .. py:attribute:: INTELLIGENT
      :value: 'intelligent'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



.. py:class:: MemorySystemType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available memory system types.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemorySystemType
      :collapse:

   .. py:attribute:: ADVANCED_RAG
      :value: 'rag'



   .. py:attribute:: ALL
      :value: 'all'



   .. py:attribute:: GRAPH
      :value: 'graph'



   .. py:attribute:: LONGTERM
      :value: 'longterm'



   .. py:attribute:: REACT
      :value: 'react'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: MultiMemoryConfig

   Configuration for Multi-Memory Coordinator.


   .. autolink-examples:: MultiMemoryConfig
      :collapse:

   .. py:method:: __post_init__()


   .. py:attribute:: base_storage_path
      :type:  str | None
      :value: None



   .. py:attribute:: consensus_threshold
      :type:  int
      :value: 2



   .. py:attribute:: default_mode
      :type:  CoordinationMode


   .. py:attribute:: enable_advanced_rag
      :type:  bool
      :value: True



   .. py:attribute:: enable_graph
      :type:  bool
      :value: False



   .. py:attribute:: enable_longterm
      :type:  bool
      :value: True



   .. py:attribute:: enable_react
      :type:  bool
      :value: True



   .. py:attribute:: enable_simple
      :type:  bool
      :value: True



   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: graph_config
      :type:  haive.agents.memory_v2.graph_memory_agent.GraphMemoryConfig | None
      :value: None



   .. py:attribute:: longterm_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: parallel_timeout
      :type:  float
      :value: 30.0



   .. py:attribute:: rag_config
      :type:  haive.agents.memory_v2.advanced_rag_memory_agent.AdvancedRAGConfig | None
      :value: None



   .. py:attribute:: react_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: simple_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: user_id
      :type:  str
      :value: 'default_user'



.. py:class:: MultiMemoryCoordinator(config: MultiMemoryConfig)

   Coordinates multiple memory systems for comprehensive memory management.

   This coordinator provides:
   - Intelligent routing to appropriate memory systems
   - Parallel querying across multiple systems
   - Result combination and synthesis
   - Memory system analytics and optimization
   - Cross-system memory migration


   .. autolink-examples:: MultiMemoryCoordinator
      :collapse:

   .. py:method:: _combine_query_results(query: str, individual_results: dict[str, Any]) -> str
      :async:


      Combine results from multiple memory systems.


      .. autolink-examples:: _combine_query_results
         :collapse:


   .. py:method:: _create_router() -> haive.agents.react.agent.ReactAgent

      Create intelligent memory system router.


      .. autolink-examples:: _create_router
         :collapse:


   .. py:method:: _create_synthesizer() -> haive.agents.react.agent.ReactAgent

      Create result synthesis agent.


      .. autolink-examples:: _create_synthesizer
         :collapse:


   .. py:method:: _init_advanced_rag_memory()

      Initialize advanced RAG memory agent.


      .. autolink-examples:: _init_advanced_rag_memory
         :collapse:


   .. py:method:: _init_graph_memory()

      Initialize graph memory agent.


      .. autolink-examples:: _init_graph_memory
         :collapse:


   .. py:method:: _init_longterm_memory()

      Initialize long-term memory agent.


      .. autolink-examples:: _init_longterm_memory
         :collapse:


   .. py:method:: _init_memory_systems()

      Initialize all enabled memory systems.


      .. autolink-examples:: _init_memory_systems
         :collapse:


   .. py:method:: _init_react_memory()

      Initialize React memory agent.


      .. autolink-examples:: _init_react_memory
         :collapse:


   .. py:method:: _init_simple_memory()

      Initialize simple memory agent.


      .. autolink-examples:: _init_simple_memory
         :collapse:


   .. py:method:: _query_single_system(system_type: MemorySystemType, query: str) -> Any
      :async:


      Query a single memory system.


      .. autolink-examples:: _query_single_system
         :collapse:


   .. py:method:: create_comprehensive_system(user_id: str, enable_graph: bool = False, neo4j_config: dict[str, Any] | None = None, storage_path: str | None = None) -> MultiMemoryCoordinator
      :classmethod:


      Create a comprehensive memory system with all components.


      .. autolink-examples:: create_comprehensive_system
         :collapse:


   .. py:method:: get_system_analytics() -> dict[str, Any]
      :async:


      Get analytics across all memory systems.


      .. autolink-examples:: get_system_analytics
         :collapse:


   .. py:method:: migrate_memories(from_system: MemorySystemType, to_system: MemorySystemType, filter_criteria: dict[str, Any] | None = None) -> dict[str, Any]
      :async:


      Migrate memories between systems.


      .. autolink-examples:: migrate_memories
         :collapse:


   .. py:method:: query_memory(query: str, systems: list[MemorySystemType] | None = None, mode: CoordinationMode | None = None, combine_results: bool = True) -> dict[str, Any]
      :async:


      Query memory across systems.

      :param query: Query string
      :param systems: Specific systems to query
      :param mode: Coordination mode
      :param combine_results: Whether to combine results

      :returns: Query results


      .. autolink-examples:: query_memory
         :collapse:


   .. py:method:: store_memory(content: str, systems: list[MemorySystemType] | None = None, mode: CoordinationMode | None = None, metadata: dict[str, Any] | None = None, importance: str = 'normal') -> dict[str, Any]
      :async:


      Store memory across appropriate systems.

      :param content: Memory content to store
      :param systems: Specific systems to use (None for intelligent routing)
      :param mode: Coordination mode
      :param metadata: Optional metadata
      :param importance: Importance level

      :returns: Storage results from all used systems


      .. autolink-examples:: store_memory
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: logger


   .. py:attribute:: memory_systems
      :type:  dict[MemorySystemType, Any]


   .. py:attribute:: operation_history
      :type:  list[dict[str, Any]]
      :value: []



   .. py:attribute:: router


   .. py:attribute:: synthesizer


.. py:function:: demo_multi_memory_coordinator()
   :async:


   Demonstrate the multi-memory coordinator.


   .. autolink-examples:: demo_multi_memory_coordinator
      :collapse:

.. py:data:: HAS_ADVANCED_RAG
   :value: True


.. py:data:: HAS_GRAPH_MEMORY
   :value: True


.. py:data:: logger

