agents.memory.enhanced_retriever
================================

.. py:module:: agents.memory.enhanced_retriever

.. autoapi-nested-parse::

   Enhanced Self-Query Retriever with Memory Context.

   This module implements Phase 2 of the incremental memory system: Enhanced Self-Query
   retriever that integrates memory classification with sophisticated retrieval strategies.

   The enhanced retriever builds on the memory classification system to provide:
   - Memory-type aware retrieval (semantic, episodic, procedural, etc.)
   - Context-aware query expansion
   - Memory importance weighting
   - Time-based relevance scoring
   - Self-query with metadata filtering

   This is the next phase after the foundational memory classification system,
   bridging toward full Graph RAG implementation.


   .. autolink-examples:: agents.memory.enhanced_retriever
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory.enhanced_retriever.logger


Classes
-------

.. autoapisummary::

   agents.memory.enhanced_retriever.EnhancedMemoryRetriever
   agents.memory.enhanced_retriever.EnhancedQueryResult
   agents.memory.enhanced_retriever.EnhancedRetrieverConfig


Functions
---------

.. autoapisummary::

   agents.memory.enhanced_retriever.create_enhanced_memory_retriever


Module Contents
---------------

.. py:class:: EnhancedMemoryRetriever(config: EnhancedRetrieverConfig)

   Enhanced self-query retriever with memory-aware context and sophisticated scoring.

   This retriever implements Phase 2 of the incremental memory system, building on
   the memory classification foundation to provide intelligent, context-aware retrieval.

   Key features:
   - Memory type classification and targeting
   - Query intent analysis and expansion
   - Multi-factor scoring (similarity + importance + recency + type)
   - Metadata filtering and self-query capabilities
   - Performance monitoring and optimization

   Initialize enhanced memory retriever.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedMemoryRetriever
      :collapse:

   .. py:method:: _apply_enhanced_scoring(memories: list[dict[str, Any]], query: str, query_intent: haive.agents.memory.core.types.MemoryQueryIntent, memory_types: list[haive.agents.memory.core.types.MemoryType]) -> list[dict[str, Any]]
      :async:


      Apply enhanced multi-factor scoring to memories.


      .. autolink-examples:: _apply_enhanced_scoring
         :collapse:


   .. py:method:: _calculate_recency_score(metadata: dict[str, Any]) -> float

      Calculate time-based recency score.


      .. autolink-examples:: _calculate_recency_score
         :collapse:


   .. py:method:: _calculate_type_score(memory_types: list[haive.agents.memory.core.types.MemoryType], target_types: list[haive.agents.memory.core.types.MemoryType]) -> float

      Calculate memory type relevance score.


      .. autolink-examples:: _calculate_type_score
         :collapse:


   .. py:method:: _expand_query(query: str, query_intent: haive.agents.memory.core.types.MemoryQueryIntent) -> str
      :async:


      Expand query with related terms and context.


      .. autolink-examples:: _expand_query
         :collapse:


   .. py:method:: _update_stats(retrieval_time: float, results_count: int, memory_types: list[haive.agents.memory.core.types.MemoryType]) -> None

      Update retrieval performance statistics.


      .. autolink-examples:: _update_stats
         :collapse:


   .. py:method:: get_performance_stats() -> dict[str, Any]

      Get retrieval performance statistics.


      .. autolink-examples:: get_performance_stats
         :collapse:


   .. py:method:: optimize_for_usage_patterns() -> dict[str, Any]
      :async:


      Analyze usage patterns and suggest optimizations.


      .. autolink-examples:: optimize_for_usage_patterns
         :collapse:


   .. py:method:: retrieve_memories(query: str, memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None, importance_threshold: float | None = None, time_range: tuple[datetime.datetime, datetime.datetime] | None = None, limit: int | None = None, include_metadata: bool = True, namespace: tuple[str, Ellipsis] | None = None) -> EnhancedQueryResult
      :async:


      Retrieve memories using enhanced self-query with memory context.

      :param query: Natural language query
      :param memory_types: Specific memory types to target (auto-detected if None)
      :param importance_threshold: Minimum importance score filter
      :param time_range: Optional time range filter
      :param limit: Maximum results to return
      :param include_metadata: Whether to include detailed metadata
      :param namespace: Memory namespace to search

      :returns: EnhancedQueryResult with memories and detailed metadata


      .. autolink-examples:: retrieve_memories
         :collapse:


   .. py:attribute:: _retrieval_stats


   .. py:attribute:: classifier


   .. py:attribute:: config


   .. py:attribute:: memory_store


.. py:class:: EnhancedQueryResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of enhanced memory retrieval with detailed metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedQueryResult
      :collapse:

   .. py:attribute:: classification_time_ms
      :type:  float
      :value: None



   .. py:attribute:: expanded_query
      :type:  str | None
      :value: None



   .. py:attribute:: final_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: importance_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: memories
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: memory_types_targeted
      :type:  list[haive.agents.memory.core.types.MemoryType]
      :value: None



   .. py:attribute:: query_intent
      :type:  haive.agents.memory.core.types.MemoryQueryIntent | None
      :value: None



   .. py:attribute:: recency_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: retrieval_time_ms
      :type:  float
      :value: None



   .. py:attribute:: similarity_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: total_found
      :type:  int
      :value: None



   .. py:attribute:: total_time_ms
      :type:  float
      :value: None



.. py:class:: EnhancedRetrieverConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for enhanced memory retriever with self-query capabilities.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedRetrieverConfig
      :collapse:

   .. py:attribute:: default_limit
      :type:  int
      :value: None



   .. py:attribute:: enable_importance_filtering
      :type:  bool
      :value: None



   .. py:attribute:: enable_metadata_filtering
      :type:  bool
      :value: None



   .. py:attribute:: enable_query_expansion
      :type:  bool
      :value: None



   .. py:attribute:: enable_temporal_scoring
      :type:  bool
      :value: None



   .. py:attribute:: expansion_terms_limit
      :type:  int
      :value: None



   .. py:attribute:: max_limit
      :type:  int
      :value: None



   .. py:attribute:: memory_classifier
      :type:  haive.agents.memory.core.classifier.MemoryClassifier
      :value: None



   .. py:attribute:: memory_store_manager
      :type:  haive.agents.memory.core.stores.MemoryStoreManager
      :value: None



   .. py:attribute:: memory_type_weights
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: recency_decay_hours
      :type:  float
      :value: None



   .. py:attribute:: recency_weight
      :type:  float
      :value: None



   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



.. py:function:: create_enhanced_memory_retriever(store_manager: haive.core.tools.store_tools.StoreManager, namespace: tuple[str, Ellipsis] = ('memory', 'enhanced'), classifier_config: haive.agents.memory.core.classifier.MemoryClassifierConfig | None = None, **retriever_kwargs) -> EnhancedMemoryRetriever
   :async:


   Factory function to create an enhanced memory retriever.

   :param store_manager: Store manager for memory persistence
   :param namespace: Default memory namespace
   :param classifier_config: Optional classifier configuration
   :param \*\*retriever_kwargs: Additional retriever configuration options

   :returns: Configured EnhancedMemoryRetriever ready for use


   .. autolink-examples:: create_enhanced_memory_retriever
      :collapse:

.. py:data:: logger

