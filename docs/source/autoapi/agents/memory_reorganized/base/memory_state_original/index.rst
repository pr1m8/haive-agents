agents.memory_reorganized.base.memory_state_original
====================================================

.. py:module:: agents.memory_reorganized.base.memory_state_original

.. autoapi-nested-parse::

   Memory state models for Memory V2 system using original Haive memory models.

   This module integrates the proven memory models from haive.agents.memory.models and
   haive.agents.ltm.memory_schemas with our V2 enhancements for token tracking, graph
   integration, and advanced memory management.


   .. autolink-examples:: agents.memory_reorganized.base.memory_state_original
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.memory_state_original.EnhancedKnowledgeTriple
   agents.memory_reorganized.base.memory_state_original.MemoryState
   agents.memory_reorganized.base.memory_state_original.MemoryStats
   agents.memory_reorganized.base.memory_state_original.MemoryType
   agents.memory_reorganized.base.memory_state_original.UnifiedMemoryEntry


Module Contents
---------------

.. py:class:: EnhancedKnowledgeTriple

   Bases: :py:obj:`haive.agents.memory_reorganized.base.memory_models_standalone.KnowledgeTriple`


   Enhanced KnowledgeTriple with V2 capabilities.


   .. autolink-examples:: EnhancedKnowledgeTriple
      :collapse:

   .. py:attribute:: access_count
      :type:  int
      :value: None



   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  haive.agents.memory_reorganized.base.memory_models_standalone.ImportanceLevel
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: supporting_evidence
      :type:  str | None
      :value: None



.. py:class:: MemoryState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Memory state using original models with V2 enhancements.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryState
      :collapse:

   .. py:method:: _update_stats() -> None

      Update memory statistics.


      .. autolink-examples:: _update_stats
         :collapse:


   .. py:method:: add_knowledge_triple(triple: EnhancedKnowledgeTriple) -> None

      Add a knowledge triple to the state.


      .. autolink-examples:: add_knowledge_triple
         :collapse:


   .. py:method:: add_memory_item(memory_item: haive.agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem) -> None

      Add a memory item to the state.


      .. autolink-examples:: add_memory_item
         :collapse:


   .. py:method:: add_schema_memory(schema_memory: pydantic.BaseModel, memory_type: MemoryType) -> None

      Add memory from original schema.


      .. autolink-examples:: add_schema_memory
         :collapse:


   .. py:method:: get_knowledge_triples() -> list[EnhancedKnowledgeTriple]

      Get all knowledge triples.


      .. autolink-examples:: get_knowledge_triples
         :collapse:


   .. py:method:: get_memories_by_type(memory_type: MemoryType) -> list[UnifiedMemoryEntry]

      Get memories of specific type.


      .. autolink-examples:: get_memories_by_type
         :collapse:


   .. py:method:: get_memory_items() -> list[haive.agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem]

      Get all memory items.


      .. autolink-examples:: get_memory_items
         :collapse:


   .. py:method:: search_memories(query: str, limit: int = 10) -> list[UnifiedMemoryEntry]

      Simple text-based memory search.


      .. autolink-examples:: search_memories
         :collapse:


   .. py:attribute:: auto_cleanup
      :type:  bool
      :value: None



   .. py:attribute:: current_memories
      :type:  list[UnifiedMemoryEntry]
      :value: None



   .. py:attribute:: max_memories
      :type:  int
      :value: None



   .. py:attribute:: memories
      :type:  list[UnifiedMemoryEntry]
      :value: None



   .. py:attribute:: memory_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: session_id
      :type:  str | None
      :value: None



   .. py:attribute:: stats
      :type:  MemoryStats
      :value: None



   .. py:attribute:: supported_schemas
      :type:  list[type]
      :value: None



   .. py:attribute:: token_usage
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



.. py:class:: MemoryStats(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Statistics about memory usage and performance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryStats
      :collapse:

   .. py:attribute:: average_relevance_score
      :type:  float
      :value: None



   .. py:attribute:: last_update
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: memories_by_importance
      :type:  dict[haive.agents.memory_reorganized.base.memory_models_standalone.ImportanceLevel, int]
      :value: None



   .. py:attribute:: memories_by_type
      :type:  dict[MemoryType, int]
      :value: None



   .. py:attribute:: processing_times
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: total_knowledge_triples
      :type:  int
      :value: None



   .. py:attribute:: total_memories
      :type:  int
      :value: None



   .. py:attribute:: total_memory_items
      :type:  int
      :value: None



   .. py:attribute:: total_operations
      :type:  int
      :value: None



   .. py:attribute:: total_retrievals
      :type:  int
      :value: None



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Memory types compatible with original models plus V2 enhancements.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: BASIC
      :value: 'basic'



   .. py:attribute:: CONVERSATIONAL
      :value: 'conversational'



   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: GRAPH_TRIPLE
      :value: 'graph_triple'



   .. py:attribute:: META
      :value: 'meta'



   .. py:attribute:: PERSONAL_CONTEXT
      :value: 'personal_context'



   .. py:attribute:: PREFERENCE
      :value: 'preference'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



   .. py:attribute:: SUMMARY
      :value: 'summary'



.. py:class:: UnifiedMemoryEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Unified memory entry that can hold both MemoryItem and KnowledgeTriple data.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: UnifiedMemoryEntry
      :collapse:

   .. py:method:: from_knowledge_triple(triple: EnhancedKnowledgeTriple) -> UnifiedMemoryEntry
      :classmethod:


      Create from knowledge triple.


      .. autolink-examples:: from_knowledge_triple
         :collapse:


   .. py:method:: from_memory_item(memory_item: haive.agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem) -> UnifiedMemoryEntry
      :classmethod:


      Create from memory item.


      .. autolink-examples:: from_memory_item
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:property:: content
      :type: str


      Get content regardless of entry type.

      .. autolink-examples:: content
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: entry_type
      :type:  str
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  haive.agents.memory_reorganized.base.memory_models_standalone.ImportanceLevel
      :value: None



   .. py:attribute:: knowledge_triple
      :type:  EnhancedKnowledgeTriple | None
      :value: None



   .. py:attribute:: memory_item
      :type:  haive.agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem | None
      :value: None



   .. py:attribute:: memory_type
      :type:  MemoryType
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



