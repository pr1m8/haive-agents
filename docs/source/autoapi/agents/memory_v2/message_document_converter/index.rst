
:py:mod:`agents.memory_v2.message_document_converter`
=====================================================

.. py:module:: agents.memory_v2.message_document_converter

Message to Document Converter for Memory V2 System.

This module converts conversation messages into timestamped documents
following LangChain patterns for long-term memory agents and graph construction.

Based on: https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/


.. autolink-examples:: agents.memory_v2.message_document_converter
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.message_document_converter.ConversationDocumentBatch
   agents.memory_v2.message_document_converter.EnhancedMemoryItem
   agents.memory_v2.message_document_converter.ImportanceLevel
   agents.memory_v2.message_document_converter.MessageDocumentConverter
   agents.memory_v2.message_document_converter.MessageMetadata
   agents.memory_v2.message_document_converter.TimestampedDocument


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConversationDocumentBatch:

   .. graphviz::
      :align: center

      digraph inheritance_ConversationDocumentBatch {
        node [shape=record];
        "ConversationDocumentBatch" [label="ConversationDocumentBatch"];
      }

.. autoclass:: agents.memory_v2.message_document_converter.ConversationDocumentBatch
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

.. autoclass:: agents.memory_v2.message_document_converter.EnhancedMemoryItem
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

.. autoclass:: agents.memory_v2.message_document_converter.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.message_document_converter``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageDocumentConverter:

   .. graphviz::
      :align: center

      digraph inheritance_MessageDocumentConverter {
        node [shape=record];
        "MessageDocumentConverter" [label="MessageDocumentConverter"];
      }

.. autoclass:: agents.memory_v2.message_document_converter.MessageDocumentConverter
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_MessageMetadata {
        node [shape=record];
        "MessageMetadata" [label="MessageMetadata"];
        "pydantic.BaseModel" -> "MessageMetadata";
      }

.. autopydantic_model:: agents.memory_v2.message_document_converter.MessageMetadata
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

   Inheritance diagram for TimestampedDocument:

   .. graphviz::
      :align: center

      digraph inheritance_TimestampedDocument {
        node [shape=record];
        "TimestampedDocument" [label="TimestampedDocument"];
        "langchain_core.documents.Document" -> "TimestampedDocument";
      }

.. autoclass:: agents.memory_v2.message_document_converter.TimestampedDocument
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.message_document_converter.create_document_index
   agents.memory_v2.message_document_converter.extract_documents_by_timeframe
   agents.memory_v2.message_document_converter.sort_documents_by_relevance_and_time

.. py:function:: create_document_index(documents: list[TimestampedDocument]) -> dict[str, Any]

   Create searchable index of documents.

   :param documents: Documents to index

   :returns: Index with metadata and statistics


   .. autolink-examples:: create_document_index
      :collapse:

.. py:function:: extract_documents_by_timeframe(documents: list[TimestampedDocument], hours_back: float = 24) -> list[TimestampedDocument]

   Extract documents from specific timeframe.

   :param documents: List of timestamped documents
   :param hours_back: How many hours back to include

   :returns: Filtered list of documents


   .. autolink-examples:: extract_documents_by_timeframe
      :collapse:

.. py:function:: sort_documents_by_relevance_and_time(documents: list[TimestampedDocument], time_weight: float = 0.3, recency_decay: float = 0.1) -> list[TimestampedDocument]

   Sort documents by relevance and recency.

   :param documents: Documents to sort
   :param time_weight: Weight given to recency (0.0 to 1.0)
   :param recency_decay: How quickly relevance decays with time

   :returns: Sorted documents (most relevant first)


   .. autolink-examples:: sort_documents_by_relevance_and_time
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.message_document_converter
   :collapse:
   
.. autolink-skip:: next
