agents.memory_v2.time_weighted_retriever
========================================

.. py:module:: agents.memory_v2.time_weighted_retriever

.. autoapi-nested-parse::

   Time-weighted retriever for Memory V2 system.

   Based on LangChain's time-weighted retriever patterns for long-term memory agents.
   Combines semantic similarity with recency weighting for optimal memory retrieval.

   Reference: https://python.langchain.com/docs/versions/migrating_memory/long_term_memory_agent/


   .. autolink-examples:: agents.memory_v2.time_weighted_retriever
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.time_weighted_retriever.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.time_weighted_retriever.MemoryRetrievalSession
   agents.memory_v2.time_weighted_retriever.TimeWeightConfig
   agents.memory_v2.time_weighted_retriever.TimeWeightedRetriever


Functions
---------

.. autoapisummary::

   agents.memory_v2.time_weighted_retriever.create_memory_focused_retriever
   agents.memory_v2.time_weighted_retriever.create_time_weighted_retriever
   agents.memory_v2.time_weighted_retriever.prepare_documents_for_time_retrieval


Module Contents
---------------

.. py:class:: MemoryRetrievalSession(retriever: TimeWeightedRetriever, session_id: str | None = None, user_id: str | None = None)

   Session for managing retrieval with context and history.

   Initialize retrieval session.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryRetrievalSession
      :collapse:

   .. py:method:: _apply_context_boost(scored_docs: list[tuple[langchain_core.documents.Document, float]]) -> list[tuple[langchain_core.documents.Document, float]]

      Apply context-aware score boosting.


      .. autolink-examples:: _apply_context_boost
         :collapse:


   .. py:method:: get_session_stats() -> dict[str, Any]

      Get session retrieval statistics.


      .. autolink-examples:: get_session_stats
         :collapse:


   .. py:method:: retrieve_with_context(query: str, exclude_recent: bool = True, context_boost: bool = True) -> list[langchain_core.documents.Document]

      Retrieve documents with session context awareness.


      .. autolink-examples:: retrieve_with_context
         :collapse:


   .. py:attribute:: query_history
      :type:  list[dict[str, Any]]
      :value: []



   .. py:attribute:: retrieved_doc_ids
      :type:  set


   .. py:attribute:: retriever


   .. py:attribute:: session_id
      :value: 'session_Instance of uuid.UUID'



   .. py:attribute:: user_id
      :value: None



.. py:class:: TimeWeightConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for time-weighted retrieval.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TimeWeightConfig
      :collapse:

   .. py:attribute:: decay_rate
      :type:  float
      :value: None



   .. py:attribute:: importance_boost
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: k
      :type:  int
      :value: None



   .. py:attribute:: max_age_hours
      :type:  float
      :value: None



   .. py:attribute:: recency_weight
      :type:  float
      :value: None



   .. py:attribute:: score_threshold
      :type:  float
      :value: None



   .. py:attribute:: type_preferences
      :type:  dict[str, float]
      :value: None



.. py:class:: TimeWeightedRetriever(vectorstore: langchain_core.vectorstores.VectorStore, config: TimeWeightConfig = None, **kwargs)

   Bases: :py:obj:`langchain_core.retrievers.BaseRetriever`


   Time-weighted retriever combining semantic similarity with recency.

   Initialize time-weighted retriever.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TimeWeightedRetriever
      :collapse:

   .. py:class:: Config

      Pydantic config.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: _calculate_importance_score(doc: langchain_core.documents.Document) -> float

      Calculate importance-based relevance boost.


      .. autolink-examples:: _calculate_importance_score
         :collapse:


   .. py:method:: _calculate_time_score(doc: langchain_core.documents.Document, current_time: datetime.datetime) -> float

      Calculate time-based relevance score.


      .. autolink-examples:: _calculate_time_score
         :collapse:


   .. py:method:: _calculate_type_score(doc: langchain_core.documents.Document) -> float

      Calculate document type preference score.


      .. autolink-examples:: _calculate_type_score
         :collapse:


   .. py:method:: _combine_scores(similarity_score: float, time_score: float, importance_score: float, type_score: float) -> float

      Combine all scoring components into final score.


      .. autolink-examples:: _combine_scores
         :collapse:


   .. py:method:: _get_relevant_documents(query: str, *, run_manager: langchain_core.callbacks.manager.CallbackManagerForRetrieverRun) -> list[langchain_core.documents.Document]

      Retrieve documents using time-weighted scoring.


      .. autolink-examples:: _get_relevant_documents
         :collapse:


   .. py:method:: get_relevant_documents_with_scores(query: str) -> list[tuple[langchain_core.documents.Document, float]]

      Get documents with their calculated scores for debugging.


      .. autolink-examples:: get_relevant_documents_with_scores
         :collapse:


   .. py:method:: update_config(**config_updates)

      Update retriever configuration.


      .. autolink-examples:: update_config
         :collapse:


   .. py:attribute:: config
      :type:  TimeWeightConfig
      :value: None



   .. py:attribute:: document_type_field
      :type:  str
      :value: None



   .. py:attribute:: memory_importance_field
      :type:  str
      :value: None



   .. py:attribute:: timestamp_field
      :type:  str
      :value: None



   .. py:attribute:: vectorstore
      :type:  langchain_core.vectorstores.VectorStore


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

.. py:data:: logger

