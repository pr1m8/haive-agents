agents.rag.memory_aware.agent
=============================

.. py:module:: agents.rag.memory_aware.agent

.. autoapi-nested-parse::

   Memory-Aware RAG Agents.

   from typing import Any
   Memory-aware RAG with persistent context and iterative learning.
   Uses structured output models for memory management.


   .. autolink-examples:: agents.rag.memory_aware.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.memory_aware.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.memory_aware.agent.MemoryAwareRAGAgent
   agents.rag.memory_aware.agent.MemoryImportance
   agents.rag.memory_aware.agent.MemoryItem
   agents.rag.memory_aware.agent.MemoryRetrievalAgent
   agents.rag.memory_aware.agent.MemoryType


Functions
---------

.. autoapisummary::

   agents.rag.memory_aware.agent.create_memory_aware_rag_agent
   agents.rag.memory_aware.agent.get_memory_aware_rag_io_schema


Module Contents
---------------

.. py:class:: MemoryAwareRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete Memory-Aware RAG agent with persistent learning.


   .. autolink-examples:: MemoryAwareRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_memories: int = 100, **kwargs)
      :classmethod:


      Create Memory-Aware RAG agent from documents.


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: MemoryImportance

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Importance levels for memory items.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryImportance
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



.. py:class:: MemoryItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual memory item with metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryItem
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  MemoryImportance
      :value: None



   .. py:attribute:: keywords
      :type:  list[str]
      :value: None



   .. py:attribute:: memory_type
      :type:  MemoryType
      :value: None



.. py:class:: MemoryRetrievalAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_memories: int = 10, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that retrieves relevant memories for context enhancement.

   Initialize memory retrieval agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryRetrievalAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build memory retrieval graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config


   .. py:attribute:: max_memories
      :value: 10



   .. py:attribute:: memory_store
      :type:  dict[str, MemoryItem]


   .. py:attribute:: name
      :type:  str
      :value: 'Memory Retrieval'



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of memory in the system.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: CONTEXTUAL
      :value: 'contextual'



   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: FEEDBACK
      :value: 'feedback'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



.. py:function:: create_memory_aware_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, memory_mode: str = 'adaptive', **kwargs) -> MemoryAwareRAGAgent

   Create a Memory-Aware RAG agent.


   .. autolink-examples:: create_memory_aware_rag_agent
      :collapse:

.. py:function:: get_memory_aware_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Memory-Aware RAG agents.


   .. autolink-examples:: get_memory_aware_rag_io_schema
      :collapse:

.. py:data:: logger

