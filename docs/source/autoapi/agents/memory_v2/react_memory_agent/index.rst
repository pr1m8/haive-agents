agents.memory_v2.react_memory_agent
===================================

.. py:module:: agents.memory_v2.react_memory_agent

.. autoapi-nested-parse::

   ReactAgent with memory tools for dynamic memory management.

   This implementation follows LangChain's long-term memory patterns but uses
   ReactAgent with tools for flexible memory operations.


   .. autolink-examples:: agents.memory_v2.react_memory_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_v2.react_memory_agent.ReactMemoryAgent


Functions
---------

.. autoapisummary::

   agents.memory_v2.react_memory_agent.example_basic_usage
   agents.memory_v2.react_memory_agent.example_with_custom_tools


Module Contents
---------------

.. py:class:: ReactMemoryAgent(name: str = 'react_memory_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, user_id: str | None = None, memory_store_path: str | None = None, k: int = 5, decay_rate: float = 0.01, use_time_weighting: bool = True)

   ReactAgent with memory management tools.

   This agent uses tools to:
   - Load relevant memories before responding
   - Store new memories from conversations
   - Update existing memories
   - Delete outdated memories
   - Search memories by semantic similarity
   - Search memories by time range


   .. autolink-examples:: ReactMemoryAgent
      :collapse:

   .. py:method:: _create_memory_tools() -> list[Any]

      Create memory management tools.


      .. autolink-examples:: _create_memory_tools
         :collapse:


   .. py:method:: _get_system_message() -> str

      Get system message that instructs agent on memory usage.


      .. autolink-examples:: _get_system_message
         :collapse:


   .. py:method:: arun(query: str, auto_save: bool = True, include_metadata: bool = False) -> dict[str, Any]
      :async:


      Run the ReactAgent with memory tools.

      :param query: User query
      :param auto_save: Automatically save conversation to memory
      :param include_metadata: Include metadata in response

      :returns: Agent response with optional metadata


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: create_with_custom_tools(name: str = 'custom_memory_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, custom_tools: list[Any] | None = None, **kwargs) -> ReactMemoryAgent
      :classmethod:


      Create ReactMemoryAgent with additional custom tools.

      :param name: Agent name
      :param engine: LLM configuration
      :param custom_tools: Additional tools to include
      :param \*\*kwargs: Other ReactMemoryAgent parameters

      :returns: ReactMemoryAgent with custom tools


      .. autolink-examples:: create_with_custom_tools
         :collapse:


   .. py:method:: save_vector_store(path: str)

      Save the vector store to disk.


      .. autolink-examples:: save_vector_store
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: decay_rate
      :value: 0.01



   .. py:attribute:: embeddings


   .. py:attribute:: engine


   .. py:attribute:: k
      :value: 5



   .. py:attribute:: memory_tools


   .. py:attribute:: name
      :value: 'react_memory_agent'



   .. py:attribute:: use_time_weighting
      :value: True



   .. py:attribute:: user_id
      :value: 'default_user'



.. py:function:: example_basic_usage()
   :async:


   Example of basic ReactMemoryAgent usage.


   .. autolink-examples:: example_basic_usage
      :collapse:

.. py:function:: example_with_custom_tools()
   :async:


   Example with custom tools added.


   .. autolink-examples:: example_with_custom_tools
      :collapse:

