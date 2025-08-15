agents.memory.memory_utils
==========================

.. py:module:: agents.memory.memory_utils


Attributes
----------

.. autoapisummary::

   agents.memory.memory_utils.logger


Functions
---------

.. autoapisummary::

   agents.memory.memory_utils.create_memory_tools
   agents.memory.memory_utils.create_memory_vectorstore
   agents.memory.memory_utils.get_user_id_from_state
   agents.memory.memory_utils.retrieve_memories
   agents.memory.memory_utils.save_structured_memories
   agents.memory.memory_utils.save_unstructured_memories


Module Contents
---------------

.. py:function:: create_memory_tools(vector_store: langchain_core.vectorstores.VectorStore)

   Create memory tools for saving and retrieving memories.

   :param vector_store: Vector store for memory storage/retrieval

   :returns: Dictionary of memory tool functions


   .. autolink-examples:: create_memory_tools
      :collapse:

.. py:function:: create_memory_vectorstore(embedding_model: langchain_core.embeddings.Embeddings | None = None) -> langchain_core.vectorstores.VectorStore

   Create a vector store for storing memories.

   :param embedding_model: Optional embedding model

   :returns: Vector store instance


   .. autolink-examples:: create_memory_vectorstore
      :collapse:

.. py:function:: get_user_id_from_state(state: dict[str, Any]) -> str

   Get the user ID from state or config.

   :param state: Current state

   :returns: User ID string


   .. autolink-examples:: get_user_id_from_state
      :collapse:

.. py:function:: retrieve_memories(query: str, vector_store: langchain_core.vectorstores.VectorStore, user_id: str, limit: int = 5, filter_fn: collections.abc.Callable[[langchain_core.documents.Document], bool] | None = None) -> list[str]

   Retrieve relevant memories from vector store.

   :param query: Query string
   :param vector_store: Vector store containing memories
   :param user_id: User ID to filter memories
   :param limit: Maximum number of memories to retrieve
   :param filter_fn: Optional custom filter function

   :returns: List of relevant memory strings


   .. autolink-examples:: retrieve_memories
      :collapse:

.. py:function:: save_structured_memories(memories: list[dict[str, Any] | haive.agents.memory.models.KnowledgeTriple], vector_store: langchain_core.vectorstores.VectorStore, user_id: str) -> list[dict[str, Any]]

   Save structured memories (knowledge triples) to vector store.

   :param memories: List of knowledge triples
   :param vector_store: Vector store for storage
   :param user_id: User ID to associate with memories

   :returns: List of saved triple dictionaries


   .. autolink-examples:: save_structured_memories
      :collapse:

.. py:function:: save_unstructured_memories(memories: list[str | haive.agents.memory.models.MemoryItem], vector_store: langchain_core.vectorstores.VectorStore, user_id: str) -> list[str]

   Save unstructured memories to vector store.

   :param memories: List of memory strings or MemoryItem objects
   :param vector_store: Vector store for storage
   :param user_id: User ID to associate with memories

   :returns: List of saved memory contents


   .. autolink-examples:: save_unstructured_memories
      :collapse:

.. py:data:: logger

