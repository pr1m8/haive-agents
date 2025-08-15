agents.memory_v2.standalone_memory_agent_free
=============================================

.. py:module:: agents.memory_v2.standalone_memory_agent_free

.. autoapi-nested-parse::

   Standalone memory agent using only free resources (no API keys required).

   This implementation shows how to build a functional memory agent without
   relying on paid APIs like OpenAI or Anthropic.


   .. autolink-examples:: agents.memory_v2.standalone_memory_agent_free
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_v2.standalone_memory_agent_free.FreeMemoryAgent


Functions
---------

.. autoapisummary::

   agents.memory_v2.standalone_memory_agent_free.test_free_memory_agent


Module Contents
---------------

.. py:class:: FreeMemoryAgent(user_id: str, storage_path: str | None = None, embedding_model: str = 'sentence-transformers/all-MiniLM-L6-v2', k_memories: int = 5)

   Memory agent using free embeddings and local storage.

   This agent provides:
   - Memory storage with embeddings (using HuggingFace)
   - Similarity-based retrieval
   - Persistent storage to disk
   - No API keys required

   Initialize the free memory agent.

   :param user_id: User identifier
   :param storage_path: Path to store memories (uses temp if None)
   :param embedding_model: HuggingFace model name for embeddings
   :param k_memories: Number of memories to retrieve


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FreeMemoryAgent
      :collapse:

   .. py:method:: _initialize_vector_store() -> langchain_community.vectorstores.FAISS

      Initialize or load the vector store.


      .. autolink-examples:: _initialize_vector_store
         :collapse:


   .. py:method:: add_memory(content: str, memory_type: haive.agents.memory_v2.memory_state_original.MemoryType = MemoryType.CONVERSATIONAL, importance: haive.agents.memory_v2.memory_state_original.ImportanceLevel = ImportanceLevel.MEDIUM, metadata: dict[str, Any] | None = None) -> str

      Add a new memory.

      :param content: Memory content
      :param memory_type: Type of memory
      :param importance: Importance level
      :param metadata: Optional metadata

      :returns: Memory ID


      .. autolink-examples:: add_memory
         :collapse:


   .. py:method:: get_relevant_context(query: str, k: int | None = None) -> str

      Get relevant context for a query.

      :param query: Query to find context for
      :param k: Number of memories to include

      :returns: Formatted context string


      .. autolink-examples:: get_relevant_context
         :collapse:


   .. py:method:: get_stats() -> dict[str, Any]

      Get memory statistics.


      .. autolink-examples:: get_stats
         :collapse:


   .. py:method:: process_input(user_input: str) -> str
      :async:


      Process user input - store if it's information, retrieve if it's a question.

      :param user_input: User's input text

      :returns: Response string


      .. autolink-examples:: process_input
         :collapse:


   .. py:method:: save()

      Save the vector store to disk.


      .. autolink-examples:: save
         :collapse:


   .. py:method:: search_memories(query: str, k: int | None = None, memory_type: haive.agents.memory_v2.memory_state_original.MemoryType | None = None, importance: haive.agents.memory_v2.memory_state_original.ImportanceLevel | None = None) -> list[dict[str, Any]]

      Search memories using similarity search.

      :param query: Search query
      :param k: Number of results (uses k_memories if None)
      :param memory_type: Filter by memory type
      :param importance: Filter by importance

      :returns: List of memory results with scores


      .. autolink-examples:: search_memories
         :collapse:


   .. py:attribute:: embeddings


   .. py:attribute:: k_memories
      :value: 5



   .. py:attribute:: memory_state


   .. py:attribute:: user_id


   .. py:attribute:: vector_store


   .. py:attribute:: vector_store_path


.. py:function:: test_free_memory_agent()
   :async:


   Test the free memory agent.


   .. autolink-examples:: test_free_memory_agent
      :collapse:

