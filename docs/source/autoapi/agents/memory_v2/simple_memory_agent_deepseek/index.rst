agents.memory_v2.simple_memory_agent_deepseek
=============================================

.. py:module:: agents.memory_v2.simple_memory_agent_deepseek

.. autoapi-nested-parse::

   SimpleMemoryAgent that works with DeepSeek - avoiding broken imports.

   This is a working version of SimpleMemoryAgent that:
   1. Uses DeepSeek LLM configuration
   2. Avoids the broken kg_map_merge imports
   3. Implements core memory functionality


   .. autolink-examples:: agents.memory_v2.simple_memory_agent_deepseek
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent_deepseek.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent_deepseek.SimpleMemoryAgentDeepSeek


Functions
---------

.. autoapisummary::

   agents.memory_v2.simple_memory_agent_deepseek.test_with_deepseek


Module Contents
---------------

.. py:class:: SimpleMemoryAgentDeepSeek(name: str = 'memory_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, user_id: str = 'default_user', max_memories: int = 100, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Memory-enhanced SimpleAgent that works with DeepSeek.

   This agent provides:
   - Memory storage and retrieval
   - Token-aware memory management
   - Conversation context preservation
   - Works with DeepSeek LLM

   Initialize the memory agent.

   :param name: Agent name
   :param engine: AugLLMConfig (can use DeepSeek)
   :param user_id: User identifier for memories
   :param max_memories: Maximum memories to store


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SimpleMemoryAgentDeepSeek
      :collapse:

   .. py:method:: _classify_input(user_input: str) -> dict[str, Any]

      Classify user input to determine if it's a memory operation.

      :param user_input: User's message

      :returns: Classification result


      .. autolink-examples:: _classify_input
         :collapse:


   .. py:method:: _format_memories_as_context(memories: list[agents.memory_v2.memory_state_original.EnhancedMemoryItem]) -> str

      Format memories as context for the LLM.

      :param memories: List of memories

      :returns: Formatted context string


      .. autolink-examples:: _format_memories_as_context
         :collapse:


   .. py:method:: _search_memories(query: str, k: int = 5) -> list[agents.memory_v2.memory_state_original.EnhancedMemoryItem]

      Search for relevant memories.

      :param query: Search query
      :param k: Number of results

      :returns: List of relevant memories


      .. autolink-examples:: _search_memories
         :collapse:


   .. py:method:: _store_memory(content: str, memory_type: agents.memory_v2.memory_state_original.MemoryType, importance: agents.memory_v2.memory_state_original.ImportanceLevel) -> str

      Store a memory.

      :param content: Memory content
      :param memory_type: Type of memory
      :param importance: Importance level

      :returns: Confirmation message


      .. autolink-examples:: _store_memory
         :collapse:


   .. py:method:: arun(user_input: str, **kwargs) -> str
      :async:


      Process user input with memory awareness.

      :param user_input: User's message
      :param \*\*kwargs: Additional arguments

      :returns: Agent's response


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: get_memory_stats() -> dict[str, Any]

      Get memory statistics.

      :returns: Memory statistics


      .. autolink-examples:: get_memory_stats
         :collapse:


   .. py:attribute:: memory_state


   .. py:attribute:: token_state


   .. py:attribute:: user_id
      :value: 'default_user'



.. py:function:: test_with_deepseek()
   :async:


   Test the agent with DeepSeek configuration.


   .. autolink-examples:: test_with_deepseek
      :collapse:

.. py:data:: logger

