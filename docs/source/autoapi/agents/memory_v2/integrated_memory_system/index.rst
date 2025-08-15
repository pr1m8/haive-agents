agents.memory_v2.integrated_memory_system
=========================================

.. py:module:: agents.memory_v2.integrated_memory_system

.. autoapi-nested-parse::

   Integrated Memory System combining Graph, Vector, and Time-based memory.

   This system shows how to use multiple memory strategies together:
   1. GraphMemoryAgent for structured knowledge and relationships
   2. ReactMemoryAgent for flexible tool-based memory management
   3. LongTermMemoryAgent for persistent cross-conversation memory


   .. autolink-examples:: agents.memory_v2.integrated_memory_system
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_v2.integrated_memory_system.IntegratedMemorySystem
   agents.memory_v2.integrated_memory_system.MemorySystemMode


Functions
---------

.. autoapisummary::

   agents.memory_v2.integrated_memory_system.create_research_assistant
   agents.memory_v2.integrated_memory_system.demo_integrated_memory


Module Contents
---------------

.. py:class:: IntegratedMemorySystem(user_id: str = 'default_user', neo4j_config: dict[str, Any] | None = None, vector_store_path: str | None = None, engine: haive.core.engine.aug_llm.AugLLMConfig | None = None)

   Combines multiple memory systems for comprehensive memory management.

   This system intelligently routes memory operations to the most appropriate
   subsystem based on content type and requirements.


   .. autolink-examples:: IntegratedMemorySystem
      :collapse:

   .. py:method:: _combine_query_results(query: str, results: dict[str, Any]) -> str
      :async:


      Combine results from multiple memory systems.


      .. autolink-examples:: _combine_query_results
         :collapse:


   .. py:method:: _create_coordinator() -> haive.agents.multi.simple.agent.SimpleMultiAgent

      Create coordinator that manages all memory systems.


      .. autolink-examples:: _create_coordinator
         :collapse:


   .. py:method:: _create_memory_router() -> haive.agents.react.agent.ReactAgent

      Create router agent that determines which memory system to use.


      .. autolink-examples:: _create_memory_router
         :collapse:


   .. py:method:: _init_graph_memory(neo4j_config: dict[str, Any] | None)

      Initialize graph memory for structured knowledge.


      .. autolink-examples:: _init_graph_memory
         :collapse:


   .. py:method:: _init_longterm_memory()

      Initialize long-term memory for persistence.


      .. autolink-examples:: _init_longterm_memory
         :collapse:


   .. py:method:: _init_react_memory(vector_store_path: str | None)

      Initialize React memory for flexible tool-based management.


      .. autolink-examples:: _init_react_memory
         :collapse:


   .. py:method:: consolidate_all_memories() -> dict[str, Any]
      :async:


      Consolidate memories across all systems.


      .. autolink-examples:: consolidate_all_memories
         :collapse:


   .. py:method:: get_memory_analytics() -> dict[str, Any]
      :async:


      Get analytics across all memory systems.


      .. autolink-examples:: get_memory_analytics
         :collapse:


   .. py:method:: query_memory(query: str, mode: MemorySystemMode = MemorySystemMode.INTELLIGENT, combine_results: bool = True) -> dict[str, Any]
      :async:


      Query memory using appropriate system(s).

      :param query: Query string
      :param mode: Query mode
      :param combine_results: Whether to combine results from multiple systems

      :returns: Query results


      .. autolink-examples:: query_memory
         :collapse:


   .. py:method:: store_memory(content: str, mode: MemorySystemMode = MemorySystemMode.INTELLIGENT, metadata: dict[str, Any] | None = None) -> dict[str, Any]
      :async:


      Store memory using the appropriate system(s).

      :param content: Memory content to store
      :param mode: Storage mode
      :param metadata: Optional metadata

      :returns: Storage results from all used systems


      .. autolink-examples:: store_memory
         :collapse:


   .. py:attribute:: coordinator


   .. py:attribute:: engine


   .. py:attribute:: router


   .. py:attribute:: user_id
      :value: 'default_user'



.. py:class:: MemorySystemMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Modes for the integrated memory system.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemorySystemMode
      :collapse:

   .. py:attribute:: CONVERSATIONAL
      :value: 'conversational'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: INTELLIGENT
      :value: 'intelligent'



   .. py:attribute:: PERSISTENT
      :value: 'persistent'



   .. py:attribute:: STRUCTURED
      :value: 'structured'



.. py:function:: create_research_assistant()
   :async:


   Create a research assistant with integrated memory.


   .. autolink-examples:: create_research_assistant
      :collapse:

.. py:function:: demo_integrated_memory()
   :async:


   Demonstrate the integrated memory system.


   .. autolink-examples:: demo_integrated_memory
      :collapse:

