agents.memory_reorganized.core.types
====================================

.. py:module:: agents.memory_reorganized.core.types

.. autoapi-nested-parse::

   Memory type definitions and core data structures.

   This module defines the fundamental memory types, entry structures, and metadata schemas
   used throughout the Haive memory system.


   .. autolink-examples:: agents.memory_reorganized.core.types
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.core.types.MemoryClassificationResult
   agents.memory_reorganized.core.types.MemoryConsolidationResult
   agents.memory_reorganized.core.types.MemoryEntry
   agents.memory_reorganized.core.types.MemoryImportance
   agents.memory_reorganized.core.types.MemoryQueryIntent
   agents.memory_reorganized.core.types.MemoryType


Module Contents
---------------

.. py:class:: MemoryClassificationResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of memory classification analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryClassificationResult
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: entities
      :type:  list[str]
      :value: None



   .. py:attribute:: importance
      :type:  MemoryImportance
      :value: None



   .. py:attribute:: importance_score
      :type:  float
      :value: None



   .. py:attribute:: memory_types
      :type:  list[MemoryType]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: sentiment
      :type:  float | None
      :value: None



   .. py:attribute:: topics
      :type:  list[str]
      :value: None



.. py:class:: MemoryConsolidationResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of memory consolidation process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryConsolidationResult
      :collapse:

   .. py:attribute:: consolidated_count
      :type:  int
      :value: None



   .. py:attribute:: duplicates_removed
      :type:  int
      :value: None



   .. py:attribute:: errors_encountered
      :type:  list[str]
      :value: None



   .. py:attribute:: expired_removed
      :type:  int
      :value: None



   .. py:attribute:: memories_summarized
      :type:  int
      :value: None



   .. py:attribute:: processing_time
      :type:  float
      :value: None



   .. py:attribute:: retrieval_accuracy_change
      :type:  float
      :value: None



   .. py:attribute:: storage_efficiency_gain
      :type:  float
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:class:: MemoryEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced memory entry with multi-modal classification and lifecycle management.

   This represents a single memory with all necessary metadata for classification,
   retrieval, and lifecycle management.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryEntry
      :collapse:

   .. py:method:: add_relationship(subject: str, predicate: str, object: str) -> None

      Add an entity relationship to this memory.


      .. autolink-examples:: add_relationship
         :collapse:


   .. py:method:: calculate_current_weight() -> float

      Calculate current relevance weight based on age and decay.


      .. autolink-examples:: calculate_current_weight
         :collapse:


   .. py:method:: is_expired(expiration_threshold: float = 0.05) -> bool

      Check if memory should be considered expired.


      .. autolink-examples:: is_expired
         :collapse:


   .. py:method:: update_access() -> None

      Update access metadata when memory is retrieved.


      .. autolink-examples:: update_access
         :collapse:


   .. py:attribute:: access_count
      :type:  int
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: conversation_id
      :type:  str | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: current_weight
      :type:  float
      :value: None



   .. py:attribute:: decay_rate
      :type:  float
      :value: None



   .. py:attribute:: entities
      :type:  list[str]
      :value: None



   .. py:attribute:: importance
      :type:  MemoryImportance
      :value: None



   .. py:attribute:: importance_score
      :type:  float
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: memory_types
      :type:  list[MemoryType]
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: namespace
      :type:  str | None
      :value: None



   .. py:attribute:: relationships
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: sentiment
      :type:  float | None
      :value: None



   .. py:attribute:: session_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source_quality
      :type:  float
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: topics
      :type:  list[str]
      :value: None



   .. py:attribute:: user_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: validation_status
      :type:  str
      :value: None



.. py:class:: MemoryImportance

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Memory importance levels for retention and retrieval prioritization.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryImportance
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: TRANSIENT
      :value: 'transient'



.. py:class:: MemoryQueryIntent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of user query intent for memory retrieval.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryQueryIntent
      :collapse:

   .. py:attribute:: complexity
      :type:  str
      :value: None



   .. py:attribute:: confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: entities
      :type:  list[str]
      :value: None



   .. py:attribute:: intent_keywords
      :type:  list[str]
      :value: None



   .. py:attribute:: max_results
      :type:  int
      :value: None



   .. py:attribute:: memory_types
      :type:  list[MemoryType]
      :value: None



   .. py:attribute:: preferred_retrieval_strategy
      :type:  str
      :value: None



   .. py:attribute:: requires_reasoning
      :type:  bool
      :value: None



   .. py:attribute:: temporal_scope
      :type:  str
      :value: None



   .. py:attribute:: topics
      :type:  list[str]
      :value: None



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enhanced memory type classifications following cognitive science patterns.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: CONTEXTUAL
      :value: 'contextual'



   .. py:attribute:: EMOTIONAL
      :value: 'emotional'



   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: ERROR
      :value: 'error'



   .. py:attribute:: FEEDBACK
      :value: 'feedback'



   .. py:attribute:: META
      :value: 'meta'



   .. py:attribute:: PREFERENCE
      :value: 'preference'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



   .. py:attribute:: SYSTEM
      :value: 'system'



   .. py:attribute:: TEMPORAL
      :value: 'temporal'



