
:py:mod:`agents.memory_v2.standalone_rag_memory`
================================================

.. py:module:: agents.memory_v2.standalone_rag_memory

Standalone RAG-based Memory Agent using BaseRAGAgent with retrievers.

This module provides memory-capable agents built on BaseRAGAgent without
dependencies on the broken memory module. All models are defined here.

Key features:
1. ConversationMemoryAgent - conversation history with time-weighting
2. FactualMemoryAgent - factual information storage and retrieval
3. PreferencesMemoryAgent - user preferences with generation
4. UnifiedMemoryRAGAgent - coordinates all memory types
5. Real BaseRAGAgent integration with different retrievers
6. Vector store persistence across different backends

NO MOCKS - All components use real BaseRAGAgent with real retrievers.


.. autolink-examples:: agents.memory_v2.standalone_rag_memory
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.standalone_rag_memory.ConversationMemoryAgent
   agents.memory_v2.standalone_rag_memory.FactualMemoryAgent
   agents.memory_v2.standalone_rag_memory.ImportanceLevel
   agents.memory_v2.standalone_rag_memory.MemoryRAGConfig
   agents.memory_v2.standalone_rag_memory.MemoryType
   agents.memory_v2.standalone_rag_memory.MessageDocumentConverter
   agents.memory_v2.standalone_rag_memory.PreferencesMemoryAgent
   agents.memory_v2.standalone_rag_memory.StandaloneMemoryItem
   agents.memory_v2.standalone_rag_memory.UnifiedMemoryRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConversationMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConversationMemoryAgent {
        node [shape=record];
        "ConversationMemoryAgent" [label="ConversationMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.ConversationMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FactualMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_FactualMemoryAgent {
        node [shape=record];
        "FactualMemoryAgent" [label="FactualMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.FactualMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ImportanceLevel:

   .. graphviz::
      :align: center

      digraph inheritance_ImportanceLevel {
        node [shape=record];
        "ImportanceLevel" [label="ImportanceLevel"];
        "str" -> "ImportanceLevel";
        "enum.Enum" -> "ImportanceLevel";
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.standalone_rag_memory``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRAGConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRAGConfig {
        node [shape=record];
        "MemoryRAGConfig" [label="MemoryRAGConfig"];
        "pydantic.BaseModel" -> "MemoryRAGConfig";
      }

.. autopydantic_model:: agents.memory_v2.standalone_rag_memory.MemoryRAGConfig
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

   Inheritance diagram for MemoryType:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryType {
        node [shape=record];
        "MemoryType" [label="MemoryType"];
        "str" -> "MemoryType";
        "enum.Enum" -> "MemoryType";
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_v2.standalone_rag_memory``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageDocumentConverter:

   .. graphviz::
      :align: center

      digraph inheritance_MessageDocumentConverter {
        node [shape=record];
        "MessageDocumentConverter" [label="MessageDocumentConverter"];
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.MessageDocumentConverter
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PreferencesMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PreferencesMemoryAgent {
        node [shape=record];
        "PreferencesMemoryAgent" [label="PreferencesMemoryAgent"];
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.PreferencesMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StandaloneMemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_StandaloneMemoryItem {
        node [shape=record];
        "StandaloneMemoryItem" [label="StandaloneMemoryItem"];
        "pydantic.BaseModel" -> "StandaloneMemoryItem";
      }

.. autopydantic_model:: agents.memory_v2.standalone_rag_memory.StandaloneMemoryItem
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

   Inheritance diagram for UnifiedMemoryRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_UnifiedMemoryRAGAgent {
        node [shape=record];
        "UnifiedMemoryRAGAgent" [label="UnifiedMemoryRAGAgent"];
      }

.. autoclass:: agents.memory_v2.standalone_rag_memory.UnifiedMemoryRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.standalone_rag_memory.create_conversation_memory_agent
   agents.memory_v2.standalone_rag_memory.create_unified_memory_agent
   agents.memory_v2.standalone_rag_memory.demo

.. py:function:: create_conversation_memory_agent(vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2', enable_time_weighting: bool = True, name: str = 'conversation_memory') -> ConversationMemoryAgent

   Factory function to create conversation memory agent.


   .. autolink-examples:: create_conversation_memory_agent
      :collapse:

.. py:function:: create_unified_memory_agent(user_id: str | None = None, llm_config: haive.core.engine.aug_llm.AugLLMConfig = None, vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2') -> UnifiedMemoryRAGAgent

   Factory function to create unified memory agent.


   .. autolink-examples:: create_unified_memory_agent
      :collapse:

.. py:function:: demo()
   :async:




.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.standalone_rag_memory
   :collapse:
   
.. autolink-skip:: next
