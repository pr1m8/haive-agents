
:py:mod:`agents.long_term_memory.tools`
=======================================

.. py:module:: agents.long_term_memory.tools



Functions
---------

.. autoapisummary::

   agents.long_term_memory.tools.save_recall_memory
   agents.long_term_memory.tools.save_structured_recall_memory
   agents.long_term_memory.tools.search_recall_memories

.. py:function:: save_recall_memory(memory: str, config: langchain_core.runnables.RunnableConfig, vs_config: haive.core.models.vectorstore.base.VectorStoreConfig) -> str

   Save memory to vectorstore for later semantic retrieval.


   .. autolink-examples:: save_recall_memory
      :collapse:

.. py:function:: save_structured_recall_memory(config: langchain_core.runnables.RunnableConfig, vs_config: haive.core.models.vectorstore.base.VectorStoreConfig, memories: list[pydantic.BaseModel] | None = None) -> str

   Save memory to vectorstore for later semantic retrieval.


   .. autolink-examples:: save_structured_recall_memory
      :collapse:

.. py:function:: search_recall_memories(query: str, config: langchain_core.runnables.RunnableConfig, vs_config: haive.core.models.vectorstore.base.VectorStoreConfig) -> list[str]

   Search for relevant memories.


   .. autolink-examples:: search_recall_memories
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.long_term_memory.tools
   :collapse:
   
.. autolink-skip:: next
