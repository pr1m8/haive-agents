agents.memory_reorganized.core.stores
=====================================

.. py:module:: agents.memory_reorganized.core.stores

.. autoapi-nested-parse::

   Memory store management system integrating with existing Haive store tools.

   This module provides enhanced memory storage and retrieval capabilities that build on
   the existing store tools with intelligent classification, self-query retrieval, and
   memory lifecycle management.


   .. autolink-examples:: agents.memory_reorganized.core.stores
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.core.stores.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.core.stores.MemoryStoreConfig
   agents.memory_reorganized.core.stores.MemoryStoreManager


Module Contents
---------------

.. py:class:: MemoryStoreConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for enhanced memory store management.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryStoreConfig
      :collapse:

   .. py:attribute:: auto_classify
      :type:  bool
      :value: None



   .. py:attribute:: classifier_config
      :type:  haive.agents.memory.core.classifier.MemoryClassifierConfig
      :value: None



   .. py:attribute:: consolidation_interval_hours
      :type:  int
      :value: None



   .. py:attribute:: default_namespace
      :type:  tuple[str, Ellipsis]
      :value: None



   .. py:attribute:: default_retrieval_limit
      :type:  int
      :value: None



   .. py:attribute:: enable_decay
      :type:  bool
      :value: None



   .. py:attribute:: importance_boost
      :type:  float
      :value: None



   .. py:attribute:: max_memories_per_namespace
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: store_manager
      :type:  haive.core.tools.store_tools.StoreManager
      :value: None



.. py:class:: MemoryStoreManager(config: MemoryStoreConfig)

   Enhanced memory store manager with intelligent classification and retrieval.

   This manager builds on the existing store tools to provide:
   - Automatic memory classification and metadata extraction
   - Self-query retrieval with memory context
   - Memory lifecycle management and consolidation
   - Multi-type memory retrieval strategies

   Initialize memory store manager with configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryStoreManager
      :collapse:

   .. py:method:: _are_contents_similar(content1: str, content2: str, threshold: float = 0.8) -> bool

      Check if two memory contents are similar enough to be considered duplicates.


      .. autolink-examples:: _are_contents_similar
         :collapse:


   .. py:method:: _calculate_current_weight(created_at: datetime.datetime, importance_score: float, decay_rate: float) -> float

      Calculate current weight based on age and decay.


      .. autolink-examples:: _calculate_current_weight
         :collapse:


   .. py:method:: _calculate_ranking_score(memory: dict[str, Any], query_intent: haive.agents.memory.core.types.Optional[haive.agents.memory.core.types.MemoryQueryIntent] = None) -> float

      Calculate ranking score for memory retrieval.


      .. autolink-examples:: _calculate_ranking_score
         :collapse:


   .. py:method:: _calculate_recency_boost(created_at: datetime.datetime, last_accessed: datetime.datetime) -> float

      Calculate recency boost for ranking.


      .. autolink-examples:: _calculate_recency_boost
         :collapse:


   .. py:method:: _find_duplicate_memories(memories: list[dict[str, Any]]) -> list[list[str]]

      Find groups of duplicate memories based on content similarity.


      .. autolink-examples:: _find_duplicate_memories
         :collapse:


   .. py:method:: _schedule_consolidation(namespace: tuple[str, Ellipsis]) -> None
      :async:


      Schedule background memory consolidation.


      .. autolink-examples:: _schedule_consolidation
         :collapse:


   .. py:method:: _should_consolidate() -> bool

      Check if memory consolidation should be triggered.


      .. autolink-examples:: _should_consolidate
         :collapse:


   .. py:method:: _update_access_metadata(memory_id: str) -> None
      :async:


      Update access metadata for a memory.


      .. autolink-examples:: _update_access_metadata
         :collapse:


   .. py:method:: consolidate_memories(namespace: tuple[str, Ellipsis] | None = None, max_age_hours: haive.agents.memory.core.types.Optional[int] = None, dry_run: bool = False) -> haive.agents.memory.core.types.MemoryConsolidationResult
      :async:


      Consolidate memories by removing duplicates, summarizing old memories, and.
      cleaning up.

      :param namespace: Namespace to consolidate (if None, consolidate all)
      :param max_age_hours: Maximum age of memories to keep (if None, use decay calculation)
      :param dry_run: If True, only analyze without making changes

      :returns: MemoryConsolidationResult with consolidation statistics


      .. autolink-examples:: consolidate_memories
         :collapse:


   .. py:method:: delete_memory(memory_id: str) -> bool
      :async:


      Delete a memory by ID.

      :param memory_id: Memory identifier to delete

      :returns: True if successful, False otherwise


      .. autolink-examples:: delete_memory
         :collapse:


   .. py:method:: get_memory_by_id(memory_id: str) -> dict[str, Any] | None
      :async:


      Retrieve a specific memory by ID and update access metadata.

      :param memory_id: Unique memory identifier

      :returns: Memory data with metadata or None if not found


      .. autolink-examples:: get_memory_by_id
         :collapse:


   .. py:method:: get_memory_statistics(namespace: tuple[str, Ellipsis] | None = None) -> dict[str, Any]
      :async:


      Get statistics about stored memories.

      :param namespace: Namespace to analyze (if None, analyze all)

      :returns: Dictionary with memory statistics


      .. autolink-examples:: get_memory_statistics
         :collapse:


   .. py:method:: retrieve_memories(query: str, namespace: tuple[str, Ellipsis] | None = None, memory_types: list[haive.agents.memory.core.types.MemoryType] | None = None, limit: haive.agents.memory.core.types.Optional[int] = None, time_range: tuple[datetime.datetime, datetime.datetime] | None = None, importance_threshold: haive.agents.memory.core.types.Optional[float] = None) -> list[dict[str, Any]]
      :async:


      Retrieve memories using intelligent query analysis and ranking.

      :param query: Search query (natural language)
      :param namespace: Memory namespace to search
      :param memory_types: Specific memory types to search (if None, auto-detect)
      :param limit: Maximum number of results
      :param time_range: Optional time range filter (start, end)
      :param importance_threshold: Minimum importance score

      :returns: List of retrieved memories with metadata


      .. autolink-examples:: retrieve_memories
         :collapse:


   .. py:method:: store_memory(content: str, namespace: tuple[str, Ellipsis] | None = None, user_context: dict[str, Any] | None = None, conversation_context: dict[str, Any] | None = None, force_classification: haive.agents.memory.core.types.Optional[haive.agents.memory.core.types.MemoryType] = None, importance_override: haive.agents.memory.core.types.Optional[float] = None) -> str
      :async:


      Store a memory with automatic classification and metadata extraction.

      :param content: Memory content to store
      :param namespace: Memory namespace (defaults to configured default)
      :param user_context: User-specific context for classification
      :param conversation_context: Conversation context for classification
      :param force_classification: Override automatic classification
      :param importance_override: Override automatic importance scoring

      :returns: Memory ID for later retrieval


      .. autolink-examples:: store_memory
         :collapse:


   .. py:method:: update_memory(memory_id: str, content: haive.agents.memory.core.types.Optional[str] = None, additional_metadata: dict[str, Any] | None = None, reclassify: bool = False) -> bool
      :async:


      Update an existing memory with new content or metadata.

      :param memory_id: Memory identifier
      :param content: New content (if updating content)
      :param additional_metadata: Additional metadata to merge
      :param reclassify: Whether to reclassify memory types

      :returns: True if successful, False otherwise


      .. autolink-examples:: update_memory
         :collapse:


   .. py:attribute:: _last_consolidation


   .. py:attribute:: classifier


   .. py:attribute:: config


   .. py:attribute:: store_manager


.. py:data:: logger

