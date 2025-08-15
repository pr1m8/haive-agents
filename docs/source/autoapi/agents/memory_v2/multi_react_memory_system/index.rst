agents.memory_v2.multi_react_memory_system
==========================================

.. py:module:: agents.memory_v2.multi_react_memory_system

.. autoapi-nested-parse::

   Multi-ReactAgent Memory System with specialized agents.

   This advanced example shows how to coordinate multiple ReactAgents,
   each with specialized memory responsibilities.


   .. autolink-examples:: agents.memory_v2.multi_react_memory_system
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_v2.multi_react_memory_system.MemoryType
   agents.memory_v2.multi_react_memory_system.MultiReactMemorySystem


Functions
---------

.. autoapisummary::

   agents.memory_v2.multi_react_memory_system.example_advanced_memory_operations
   agents.memory_v2.multi_react_memory_system.example_multi_memory_system


Module Contents
---------------

.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of specialized memory.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



   .. py:attribute:: WORKING
      :value: 'working'



.. py:class:: MultiReactMemorySystem(user_id: str = 'default_user', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, memory_base_path: str | None = None)

   Coordinate multiple specialized ReactAgents for comprehensive memory management.

   This system uses:
   - Episodic Memory Agent: Personal experiences, events, conversations
   - Semantic Memory Agent: Facts, concepts, general knowledge
   - Procedural Memory Agent: Skills, procedures, how-to knowledge
   - Working Memory Agent: Current context, active tasks, short-term goals
   - Memory Router Agent: Determines which memory system to use


   .. autolink-examples:: MultiReactMemorySystem
      :collapse:

   .. py:method:: _combine_memory_results(results: dict[str, str], query: str) -> str

      Combine results from multiple memory systems.


      .. autolink-examples:: _combine_memory_results
         :collapse:


   .. py:method:: _create_coordinator() -> haive.agents.multi.agent.MultiAgent

      Create coordinator multi-agent.


      .. autolink-examples:: _create_coordinator
         :collapse:


   .. py:method:: _create_router_agent() -> haive.agents.react.agent.ReactAgent

      Create router agent that determines which memory system to use.


      .. autolink-examples:: _create_router_agent
         :collapse:


   .. py:method:: _initialize_memory_agents() -> dict[MemoryType, haive.agents.memory_v2.react_memory_agent.ReactMemoryAgent]

      Initialize specialized memory agents.


      .. autolink-examples:: _initialize_memory_agents
         :collapse:


   .. py:method:: consolidate_memories() -> str
      :async:


      Consolidate memories across systems (move from working to long-term).


      .. autolink-examples:: consolidate_memories
         :collapse:


   .. py:method:: get_memory_stats() -> dict[str, Any]
      :async:


      Get statistics about memory usage.


      .. autolink-examples:: get_memory_stats
         :collapse:


   .. py:method:: process_query(query: str) -> dict[str, Any]
      :async:


      Process a query using the appropriate memory systems.

      :param query: User query

      :returns: Dictionary with response and metadata


      .. autolink-examples:: process_query
         :collapse:


   .. py:method:: store_memory(content: str, memory_type: MemoryType | None = None) -> str
      :async:


      Store a memory in the appropriate system.

      :param content: Memory content to store
      :param memory_type: Optional specific memory type, otherwise auto-classified

      :returns: Confirmation message


      .. autolink-examples:: store_memory
         :collapse:


   .. py:attribute:: coordinator


   .. py:attribute:: engine


   .. py:attribute:: memory_agents


   .. py:attribute:: memory_base_path
      :value: './memories/default_user'



   .. py:attribute:: router_agent


   .. py:attribute:: user_id
      :value: 'default_user'



.. py:function:: example_advanced_memory_operations()
   :async:


   Advanced memory operations example.


   .. autolink-examples:: example_advanced_memory_operations
      :collapse:

.. py:function:: example_multi_memory_system()
   :async:


   Example of using the multi-memory system.


   .. autolink-examples:: example_multi_memory_system
      :collapse:

