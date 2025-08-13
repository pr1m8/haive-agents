
:py:mod:`agents.memory_v2.rag_memory_agent`
===========================================

.. py:module:: agents.memory_v2.rag_memory_agent

RAG-based Memory Agent using BaseRAGAgent with advanced retrievers.

This module provides memory-capable agents built on BaseRAGAgent with:
1. Time-weighted retrieval for temporal memory access
2. Multi-modal memory storage (conversation, preferences, facts)
3. Knowledge graph-enhanced retrieval
4. Real-time memory updates and ingestion
5. Vector store persistence across different backends

All built using BaseRAGAgent as the foundation with custom retrievers.


.. autolink-examples:: agents.memory_v2.rag_memory_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.rag_memory_agent.ConversationMemoryAgent
   agents.memory_v2.rag_memory_agent.EnhancedMemoryItem
   agents.memory_v2.rag_memory_agent.FactualMemoryAgent
   agents.memory_v2.rag_memory_agent.ImportanceLevel
   agents.memory_v2.rag_memory_agent.MemoryRAGConfig
   agents.memory_v2.rag_memory_agent.MemoryType
   agents.memory_v2.rag_memory_agent.MessageDocumentConverter
   agents.memory_v2.rag_memory_agent.PreferencesMemoryAgent
   agents.memory_v2.rag_memory_agent.TimeWeightConfig
   agents.memory_v2.rag_memory_agent.TimeWeightedRetriever
   agents.memory_v2.rag_memory_agent.UnifiedMemoryRAGAgent


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

.. autoclass:: agents.memory_v2.rag_memory_agent.ConversationMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMemoryItem {
        node [shape=record];
        "EnhancedMemoryItem" [label="EnhancedMemoryItem"];
        "MemoryItem" -> "EnhancedMemoryItem";
      }

.. autoclass:: agents.memory_v2.rag_memory_agent.EnhancedMemoryItem
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

.. autoclass:: agents.memory_v2.rag_memory_agent.FactualMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



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

.. autoclass:: agents.memory_v2.rag_memory_agent.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.rag_memory_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRAGConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRAGConfig {
        node [shape=record];
        "MemoryRAGConfig" [label="MemoryRAGConfig"];
        "pydantic.BaseModel" -> "MemoryRAGConfig";
      }

.. autopydantic_model:: agents.memory_v2.rag_memory_agent.MemoryRAGConfig
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


:orphan:



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

.. autoclass:: agents.memory_v2.rag_memory_agent.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_v2.rag_memory_agent``.


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageDocumentConverter:

   .. graphviz::
      :align: center

      digraph inheritance_MessageDocumentConverter {
        node [shape=record];
        "MessageDocumentConverter" [label="MessageDocumentConverter"];
      }

.. autoclass:: agents.memory_v2.rag_memory_agent.MessageDocumentConverter
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

.. autoclass:: agents.memory_v2.rag_memory_agent.PreferencesMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TimeWeightConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TimeWeightConfig {
        node [shape=record];
        "TimeWeightConfig" [label="TimeWeightConfig"];
        "pydantic.BaseModel" -> "TimeWeightConfig";
      }

.. autopydantic_model:: agents.memory_v2.rag_memory_agent.TimeWeightConfig
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TimeWeightedRetriever:

   .. graphviz::
      :align: center

      digraph inheritance_TimeWeightedRetriever {
        node [shape=record];
        "TimeWeightedRetriever" [label="TimeWeightedRetriever"];
        "langchain_core.retrievers.BaseRetriever" -> "TimeWeightedRetriever";
      }

.. autoclass:: agents.memory_v2.rag_memory_agent.TimeWeightedRetriever
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UnifiedMemoryRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_UnifiedMemoryRAGAgent {
        node [shape=record];
        "UnifiedMemoryRAGAgent" [label="UnifiedMemoryRAGAgent"];
      }

.. autoclass:: agents.memory_v2.rag_memory_agent.UnifiedMemoryRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.rag_memory_agent.create_conversation_memory_agent
   agents.memory_v2.rag_memory_agent.create_factual_memory_agent
   agents.memory_v2.rag_memory_agent.create_postgresql_memory_agent
   agents.memory_v2.rag_memory_agent.create_supabase_memory_agent
   agents.memory_v2.rag_memory_agent.create_unified_memory_agent
   agents.memory_v2.rag_memory_agent.demo

.. py:function:: create_conversation_memory_agent(vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2', enable_time_weighting: bool = True, name: str = 'conversation_memory') -> ConversationMemoryAgent

   Factory function to create conversation memory agent.


   .. autolink-examples:: create_conversation_memory_agent
      :collapse:

.. py:function:: create_factual_memory_agent(vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2', similarity_threshold: float = 0.7, name: str = 'factual_memory') -> FactualMemoryAgent

   Factory function to create factual memory agent.


   .. autolink-examples:: create_factual_memory_agent
      :collapse:

.. py:function:: create_postgresql_memory_agent(connection_string: str, user_id: str | None = None, table_name: str = 'user_memories') -> UnifiedMemoryRAGAgent

   Create memory agent with PostgreSQL persistence.


   .. autolink-examples:: create_postgresql_memory_agent
      :collapse:

.. py:function:: create_supabase_memory_agent(supabase_url: str, supabase_key: str, user_id: str | None = None) -> UnifiedMemoryRAGAgent

   Create memory agent with Supabase persistence.


   .. autolink-examples:: create_supabase_memory_agent
      :collapse:

.. py:function:: create_unified_memory_agent(user_id: str | None = None, llm_config: haive.core.engine.aug_llm.AugLLMConfig = None, vector_store_provider: haive.core.engine.vectorstore.VectorStoreProvider = VectorStoreProvider.FAISS, embedding_model: str = 'sentence-transformers/all-mpnet-base-v2') -> UnifiedMemoryRAGAgent

   Factory function to create unified memory agent.


   .. autolink-examples:: create_unified_memory_agent
      :collapse:

.. py:function:: demo()
   :async:




.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.rag_memory_agent
   :collapse:
   
.. autolink-skip:: next
