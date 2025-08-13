
:py:mod:`agents.rag.memory_aware.agent`
=======================================

.. py:module:: agents.rag.memory_aware.agent

Memory-Aware RAG Agents.

from typing import Any
Memory-aware RAG with persistent context and iterative learning.
Uses structured output models for memory management.


.. autolink-examples:: agents.rag.memory_aware.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.memory_aware.agent.MemoryAwareRAGAgent
   agents.rag.memory_aware.agent.MemoryImportance
   agents.rag.memory_aware.agent.MemoryItem
   agents.rag.memory_aware.agent.MemoryRetrievalAgent
   agents.rag.memory_aware.agent.MemoryType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryAwareRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryAwareRAGAgent {
        node [shape=record];
        "MemoryAwareRAGAgent" [label="MemoryAwareRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "MemoryAwareRAGAgent";
      }

.. autoclass:: agents.rag.memory_aware.agent.MemoryAwareRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryImportance:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryImportance {
        node [shape=record];
        "MemoryImportance" [label="MemoryImportance"];
        "str" -> "MemoryImportance";
        "enum.Enum" -> "MemoryImportance";
      }

.. autoclass:: agents.rag.memory_aware.agent.MemoryImportance
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryImportance** is an Enum defined in ``agents.rag.memory_aware.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryItem {
        node [shape=record];
        "MemoryItem" [label="MemoryItem"];
        "pydantic.BaseModel" -> "MemoryItem";
      }

.. autopydantic_model:: agents.rag.memory_aware.agent.MemoryItem
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRetrievalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRetrievalAgent {
        node [shape=record];
        "MemoryRetrievalAgent" [label="MemoryRetrievalAgent"];
        "haive.agents.base.agent.Agent" -> "MemoryRetrievalAgent";
      }

.. autoclass:: agents.rag.memory_aware.agent.MemoryRetrievalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryType:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryType {
        node [shape=record];
        "MemoryType" [label="MemoryType"];
        "str" -> "MemoryType";
        "enum.Enum" -> "MemoryType";
      }

.. autoclass:: agents.rag.memory_aware.agent.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.rag.memory_aware.agent``.



Functions
---------

.. autoapisummary::

   agents.rag.memory_aware.agent.create_memory_aware_rag_agent
   agents.rag.memory_aware.agent.get_memory_aware_rag_io_schema

.. py:function:: create_memory_aware_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, memory_mode: str = 'adaptive', **kwargs) -> MemoryAwareRAGAgent

   Create a Memory-Aware RAG agent.


   .. autolink-examples:: create_memory_aware_rag_agent
      :collapse:

.. py:function:: get_memory_aware_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Memory-Aware RAG agents.


   .. autolink-examples:: get_memory_aware_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.memory_aware.agent
   :collapse:
   
.. autolink-skip:: next
