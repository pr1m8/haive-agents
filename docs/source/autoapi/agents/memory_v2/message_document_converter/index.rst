agents.memory_v2.message_document_converter
===========================================

.. py:module:: agents.memory_v2.message_document_converter

.. autoapi-nested-parse::

   Message to Document Converter for Memory V2 System.

   This module converts conversation messages into timestamped documents
   following LangChain patterns for long-term memory agents and graph construction.

   Based on: https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/


   .. autolink-examples:: agents.memory_v2.message_document_converter
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.message_document_converter.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.message_document_converter.ConversationDocumentBatch
   agents.memory_v2.message_document_converter.MessageDocumentConverter
   agents.memory_v2.message_document_converter.MessageMetadata
   agents.memory_v2.message_document_converter.TimestampedDocument


Functions
---------

.. autoapisummary::

   agents.memory_v2.message_document_converter.create_document_index
   agents.memory_v2.message_document_converter.extract_documents_by_timeframe
   agents.memory_v2.message_document_converter.sort_documents_by_relevance_and_time


Module Contents
---------------

.. py:class:: ConversationDocumentBatch(conversation_id: str | None = None, user_id: str | None = None)

   Batch processor for converting entire conversations to documents.

   Initialize batch processor.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationDocumentBatch
      :collapse:

   .. py:method:: _create_chunk_summary(messages: list[langchain_core.messages.BaseMessage], chunk_num: int, total_chunks: int) -> str

      Create summary for a chunk of messages.


      .. autolink-examples:: _create_chunk_summary
         :collapse:


   .. py:method:: process_conversation(messages: list[langchain_core.messages.BaseMessage], include_summary: bool = True, chunk_size: int = 5) -> list[TimestampedDocument]

      Process entire conversation into documents.

      :param messages: Conversation messages
      :param include_summary: Whether to create summary documents
      :param chunk_size: Size of message chunks for processing

      :returns: List of all generated documents


      .. autolink-examples:: process_conversation
         :collapse:


   .. py:attribute:: conversation_id
      :value: 'batch_Instance of uuid.UUID'



   .. py:attribute:: converter


   .. py:attribute:: user_id
      :value: None



.. py:class:: MessageDocumentConverter(conversation_id: str | None = None, user_id: str | None = None, session_id: str | None = None)

   Converts conversation messages into timestamped documents for memory storage.

   Initialize converter with context.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageDocumentConverter
      :collapse:

   .. py:method:: _analyze_content(content: str, message_type: str) -> dict[str, Any]

      Analyze content for metadata extraction.


      .. autolink-examples:: _analyze_content
         :collapse:


   .. py:method:: _contains_personal_info(content: str) -> bool

      Check if content contains personal information.


      .. autolink-examples:: _contains_personal_info
         :collapse:


   .. py:method:: _contains_technical_info(content: str) -> bool

      Check if content contains technical information.


      .. autolink-examples:: _contains_technical_info
         :collapse:


   .. py:method:: _contains_temporal_info(content: str) -> bool

      Check if content contains time-sensitive information.


      .. autolink-examples:: _contains_temporal_info
         :collapse:


   .. py:method:: _determine_importance(content: str, message_type: str) -> agents.memory_v2.memory_state_original.ImportanceLevel

      Determine importance level of content.


      .. autolink-examples:: _determine_importance
         :collapse:


   .. py:method:: _determine_summary_importance(messages: list[langchain_core.messages.BaseMessage], summary: str) -> agents.memory_v2.memory_state_original.ImportanceLevel

      Determine importance of conversation summary.


      .. autolink-examples:: _determine_summary_importance
         :collapse:


   .. py:method:: _extract_content(message: langchain_core.messages.BaseMessage) -> str

      Extract content from message.


      .. autolink-examples:: _extract_content
         :collapse:


   .. py:method:: _get_message_type(message: langchain_core.messages.BaseMessage) -> str

      Determine message type from LangChain message.


      .. autolink-examples:: _get_message_type
         :collapse:


   .. py:method:: convert_message(message: langchain_core.messages.BaseMessage) -> TimestampedDocument

      Convert single message to timestamped document.

      :param message: LangChain message to convert

      :returns: TimestampedDocument with rich metadata


      .. autolink-examples:: convert_message
         :collapse:


   .. py:method:: convert_messages(messages: list[langchain_core.messages.BaseMessage]) -> list[TimestampedDocument]

      Convert multiple messages to timestamped documents.

      :param messages: List of messages to convert

      :returns: List of TimestampedDocuments


      .. autolink-examples:: convert_messages
         :collapse:


   .. py:method:: create_conversation_summary_document(messages: list[langchain_core.messages.BaseMessage], summary: str) -> TimestampedDocument

      Create summary document from conversation.

      :param messages: Original messages
      :param summary: Generated summary text

      :returns: TimestampedDocument containing the summary


      .. autolink-examples:: create_conversation_summary_document
         :collapse:


   .. py:method:: create_memory_document(memory_item: agents.memory_v2.memory_state_original.EnhancedMemoryItem) -> TimestampedDocument

      Convert memory item to timestamped document.

      :param memory_item: Memory item to convert

      :returns: TimestampedDocument for memory storage


      .. autolink-examples:: create_memory_document
         :collapse:


   .. py:attribute:: conversation_id
      :value: 'conv_Instance of uuid.UUID'



   .. py:attribute:: session_id
      :value: 'session_Instance of uuid.UUID'



   .. py:attribute:: turn_counter
      :value: 0



   .. py:attribute:: user_id
      :value: None



.. py:class:: MessageMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced metadata for message-based documents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageMetadata
      :collapse:

   .. py:attribute:: contains_personal_info
      :type:  bool
      :value: None



   .. py:attribute:: contains_technical_info
      :type:  bool
      :value: None



   .. py:attribute:: contains_temporal_info
      :type:  bool
      :value: None



   .. py:attribute:: content_length
      :type:  int
      :value: None



   .. py:attribute:: conversation_id
      :type:  str | None
      :value: None



   .. py:attribute:: estimated_tokens
      :type:  int
      :value: None



   .. py:attribute:: language
      :type:  str
      :value: None



   .. py:attribute:: memory_importance
      :type:  agents.memory_v2.memory_state_original.ImportanceLevel
      :value: None



   .. py:attribute:: message_id
      :type:  str
      :value: None



   .. py:attribute:: message_type
      :type:  str
      :value: None



   .. py:attribute:: needs_entity_extraction
      :type:  bool
      :value: None



   .. py:attribute:: needs_sentiment_analysis
      :type:  bool
      :value: None



   .. py:attribute:: processed_for_memory
      :type:  bool
      :value: None



   .. py:attribute:: session_id
      :type:  str | None
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: turn_number
      :type:  int
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



.. py:class:: TimestampedDocument(page_content: str, metadata: dict[str, Any] | None = None)

   Bases: :py:obj:`langchain_core.documents.Document`


   Document with enhanced timestamp and metadata for memory retrieval.

   Initialize with enhanced metadata.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TimestampedDocument
      :collapse:

   .. py:property:: age_days
      :type: float


      Get document age in days.

      .. autolink-examples:: age_days
         :collapse:


   .. py:property:: age_hours
      :type: float


      Get document age in hours.

      .. autolink-examples:: age_hours
         :collapse:


   .. py:property:: timestamp
      :type: datetime.datetime


      Get timestamp as datetime object.

      .. autolink-examples:: timestamp
         :collapse:


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

.. py:data:: logger

