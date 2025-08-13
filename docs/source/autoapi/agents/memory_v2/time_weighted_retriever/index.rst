
:py:mod:`agents.memory_v2.time_weighted_retriever`
==================================================

.. py:module:: agents.memory_v2.time_weighted_retriever

Time-weighted retriever for Memory V2 system.

Based on LangChain's time-weighted retriever patterns for long-term memory agents.
Combines semantic similarity with recency weighting for optimal memory retrieval.

Reference: https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/


.. autolink-examples:: agents.memory_v2.time_weighted_retriever
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.time_weighted_retriever.MemoryRetrievalSession
   agents.memory_v2.time_weighted_retriever.TimestampedDocument
   agents.memory_v2.time_weighted_retriever.TimeWeightConfig
   agents.memory_v2.time_weighted_retriever.TimeWeightedRetriever


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRetrievalSession:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRetrievalSession {
        node [shape=record];
        "MemoryRetrievalSession" [label="MemoryRetrievalSession"];
      }

.. autoclass:: agents.memory_v2.time_weighted_retriever.MemoryRetrievalSession
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TimeWeightConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TimeWeightConfig {
        node [shape=record];
        "TimeWeightConfig" [label="TimeWeightConfig"];
        "pydantic.BaseModel" -> "TimeWeightConfig";
      }

.. autopydantic_model:: agents.memory_v2.time_weighted_retriever.TimeWeightConfig
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

   Inheritance diagram for TimeWeightedRetriever:

   .. graphviz::
      :align: center

      digraph inheritance_TimeWeightedRetriever {
        node [shape=record];
        "TimeWeightedRetriever" [label="TimeWeightedRetriever"];
        "langchain_core.retrievers.BaseRetriever" -> "TimeWeightedRetriever";
      }

.. autoclass:: agents.memory_v2.time_weighted_retriever.TimeWeightedRetriever
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TimestampedDocument:

   .. graphviz::
      :align: center

      digraph inheritance_TimestampedDocument {
        node [shape=record];
        "TimestampedDocument" [label="TimestampedDocument"];
        "langchain_core.documents.Document" -> "TimestampedDocument";
      }

.. autoclass:: agents.memory_v2.time_weighted_retriever.TimestampedDocument
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.time_weighted_retriever.create_memory_focused_retriever
   agents.memory_v2.time_weighted_retriever.create_time_weighted_retriever
   agents.memory_v2.time_weighted_retriever.prepare_documents_for_time_retrieval

.. py:function:: create_memory_focused_retriever(vectorstore: langchain_core.vectorstores.VectorStore) -> TimeWeightedRetriever

   Create retriever optimized for memory retrieval.

   :param vectorstore: Vector store with memory documents

   :returns: Memory-optimized TimeWeightedRetriever


   .. autolink-examples:: create_memory_focused_retriever
      :collapse:

.. py:function:: create_time_weighted_retriever(vectorstore: langchain_core.vectorstores.VectorStore, decay_rate: float = 0.01, recency_weight: float = 0.3, k: int = 5) -> TimeWeightedRetriever

   Factory function to create configured time-weighted retriever.

   :param vectorstore: Vector store containing timestamped documents
   :param decay_rate: How quickly relevance decays per hour
   :param recency_weight: Weight of recency vs similarity (0.0-1.0)
   :param k: Number of documents to retrieve

   :returns: Configured TimeWeightedRetriever


   .. autolink-examples:: create_time_weighted_retriever
      :collapse:

.. py:function:: prepare_documents_for_time_retrieval(documents: list[agents.memory_v2.message_document_converter.TimestampedDocument]) -> list[langchain_core.documents.Document]

   Prepare timestamped documents for time-weighted retrieval.

   :param documents: List of timestamped documents

   :returns: List of documents ready for vector store ingestion


   .. autolink-examples:: prepare_documents_for_time_retrieval
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.time_weighted_retriever
   :collapse:
   
.. autolink-skip:: next
