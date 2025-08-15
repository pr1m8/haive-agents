agents.memory_v2.memory_state
=============================

.. py:module:: agents.memory_v2.memory_state

.. autoapi-nested-parse::

   Memory state models for Memory V2 system using original Haive memory models.

   This module integrates the proven memory models from haive.agents.memory.models
   and haive.agents.ltm.memory_schemas with our V2 enhancements for token tracking,
   graph integration, and advanced memory management.


   .. autolink-examples:: agents.memory_v2.memory_state
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.memory_state.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.memory_state.MemoryEntry
   agents.memory_v2.memory_state.MemoryMetadata
   agents.memory_v2.memory_state.MemoryState
   agents.memory_v2.memory_state.MemoryStats


Module Contents
---------------

.. py:class:: MemoryEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A single memory entry with content and metadata.

   Represents a complete memory item that can be stored, retrieved,
   and analyzed by memory agents.

   .. attribute:: id

      Unique identifier for the memory

   .. attribute:: content

      The actual memory content

   .. attribute:: metadata

      Structured metadata about the memory

   .. attribute:: embedding

      Optional vector embedding for similarity search

   .. attribute:: similarity_score

      Similarity score when retrieved (populated during retrieval)

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryEntry
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: embedding
      :type:  list[float] | None
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  MemoryMetadata
      :value: None



   .. py:attribute:: similarity_score
      :type:  float | None
      :value: None



.. py:class:: MemoryMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Metadata for a single memory entry.

   Tracks essential information about stored memories including
   type classification, importance, timestamps, and source information.

   .. attribute:: memory_type

      Type of memory (semantic, episodic, procedural)

   .. attribute:: importance

      Importance level (critical, high, medium, low, transient)

   .. attribute:: confidence

      Confidence score for the memory (0.0-1.0)

   .. attribute:: timestamp

      When the memory was created

   .. attribute:: source

      Source of the memory (user_input, agent_inference, system)

   .. attribute:: tags

      List of tags for categorization

   .. attribute:: entities

      Named entities mentioned in the memory

   .. attribute:: relationships

      Relationships extracted from the memory

   .. attribute:: context_id

      ID linking related memories

   .. attribute:: retrieval_count

      How many times this memory has been retrieved

   .. attribute:: last_accessed

      When the memory was last accessed

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryMetadata
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: context_id
      :type:  str | None
      :value: None



   .. py:attribute:: entities
      :type:  list[str]
      :value: None



   .. py:attribute:: importance
      :type:  str
      :value: None



   .. py:attribute:: last_accessed
      :type:  str | None
      :value: None



   .. py:attribute:: memory_type
      :type:  str
      :value: None



   .. py:attribute:: relationships
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: retrieval_count
      :type:  int
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: timestamp
      :type:  str | None
      :value: None



.. py:class:: MemoryState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for memory agent operations.

   Extends MessagesState with memory-specific fields for tracking
   current memories, metadata, statistics, and operation results.

   This state schema is used by all memory agents to maintain
   consistent state management and enable proper coordination
   between different memory strategies.

   .. attribute:: current_memories

      List of memory entries currently being processed

   .. attribute:: retrieved_memories

      List of memories retrieved in the last operation

   .. attribute:: memory_metadata

      General metadata about the memory session

   .. attribute:: memory_stats

      Performance and usage statistics

   .. attribute:: token_usage

      Token usage tracking for memory operations

   .. attribute:: last_operation

      Information about the last memory operation performed

   .. attribute:: memory_context

      Context information for memory operations

   .. attribute:: active_filters

      Currently active filters for memory search/retrieval


   .. autolink-examples:: MemoryState
      :collapse:

   .. py:method:: add_memory(memory: MemoryEntry) -> None

      Add a memory entry to current memories.


      .. autolink-examples:: add_memory
         :collapse:


   .. py:method:: get_memory_summary() -> dict[str, Any]

      Get a comprehensive summary of the current memory state.


      .. autolink-examples:: get_memory_summary
         :collapse:


   .. py:method:: update_retrieval_stats(memories: list[MemoryEntry], retrieval_time: float) -> None

      Update statistics after memory retrieval.


      .. autolink-examples:: update_retrieval_stats
         :collapse:


   .. py:attribute:: active_filters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: current_memories
      :type:  list[MemoryEntry]
      :value: None



   .. py:attribute:: last_operation
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: memory_cache
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: memory_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: memory_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: memory_stats
      :type:  MemoryStats
      :value: None



   .. py:attribute:: memory_storage_path
      :type:  str | None
      :value: None



   .. py:attribute:: retrieved_memories
      :type:  list[MemoryEntry]
      :value: None



   .. py:attribute:: token_usage
      :type:  dict[str, Any]
      :value: None



.. py:class:: MemoryStats(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Statistics about memory operations and performance.

   Tracks memory system performance, usage patterns, and optimization metrics.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryStats
      :collapse:

   .. py:attribute:: avg_retrieval_time
      :type:  float
      :value: None



   .. py:attribute:: avg_search_time
      :type:  float
      :value: None



   .. py:attribute:: avg_storage_time
      :type:  float
      :value: None



   .. py:attribute:: cache_hit_rate
      :type:  float
      :value: None



   .. py:attribute:: memories_by_importance
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: memories_by_type
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: tokens_for_classification
      :type:  int
      :value: None



   .. py:attribute:: tokens_for_retrieval
      :type:  int
      :value: None



   .. py:attribute:: tokens_for_storage
      :type:  int
      :value: None



   .. py:attribute:: total_memories
      :type:  int
      :value: None



   .. py:attribute:: total_retrievals
      :type:  int
      :value: None



   .. py:attribute:: total_searches
      :type:  int
      :value: None



   .. py:attribute:: total_tokens_used
      :type:  int
      :value: None



.. py:data:: logger

