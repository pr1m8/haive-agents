agents.memory_reorganized.api.memory_utils
==========================================

.. py:module:: agents.memory_reorganized.api.memory_utils

.. autoapi-nested-parse::

   Memory_Utils utility module.

   This module provides memory utils functionality for the Haive framework.

   Functions:
       get_user_id_from_state: Get User Id From State functionality.
       create_memory_vectorstore: Create Memory Vectorstore functionality.
       save_unstructured_memories: Save Unstructured Memories functionality.


   .. autolink-examples:: agents.memory_reorganized.api.memory_utils
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.api.memory_utils.logger


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.api.memory_utils.create_memory_tools
   agents.memory_reorganized.api.memory_utils.create_memory_vectorstore
   agents.memory_reorganized.api.memory_utils.get_user_id_from_state
   agents.memory_reorganized.api.memory_utils.retrieve_memories
   agents.memory_reorganized.api.memory_utils.save_structured_memories
   agents.memory_reorganized.api.memory_utils.save_unstructured_memories


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

.. py:function:: save_structured_memories(memories: list[dict[str, Any] | agents.react.memory.state.KnowledgeTriple], vector_store: langchain_core.vectorstores.VectorStore, user_id: str) -> list[dict[str, Any]]

   Save structured memories (knowledge triples) to vector store.

   :param memories: List of knowledge triples
   :param vector_store: Vector store for storage
   :param user_id: User ID to associate with memories

   :returns: List of saved triple dictionaries


   .. autolink-examples:: save_structured_memories
      :collapse:

.. py:function:: save_unstructured_memories(memories: list[str | agents.react.memory.state.MemoryItem], vector_store: langchain_core.vectorstores.VectorStore, user_id: str) -> list[str]

   Save unstructured memories to vector store.

   :param memories: List of memory strings or MemoryItem objects
   :param vector_store: Vector store for storage
   :param user_id: User ID to associate with memories

   :returns: List of saved memory contents


   .. autolink-examples:: save_unstructured_memories
      :collapse:

.. py:data:: logger

