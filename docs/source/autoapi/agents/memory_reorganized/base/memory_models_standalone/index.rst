agents.memory_reorganized.base.memory_models_standalone
=======================================================

.. py:module:: agents.memory_reorganized.base.memory_models_standalone

.. autoapi-nested-parse::

   Standalone memory models for the reorganized memory system.

   This module provides core memory models that are used throughout the memory system,
   designed to be standalone without heavy dependencies to avoid circular imports.


   .. autolink-examples:: agents.memory_reorganized.base.memory_models_standalone
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem
   agents.memory_reorganized.base.memory_models_standalone.ImportanceLevel
   agents.memory_reorganized.base.memory_models_standalone.KnowledgeTriple
   agents.memory_reorganized.base.memory_models_standalone.MemoryItem
   agents.memory_reorganized.base.memory_models_standalone.MemoryType


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.base.memory_models_standalone.create_knowledge_triple
   agents.memory_reorganized.base.memory_models_standalone.create_memory_item
   agents.memory_reorganized.base.memory_models_standalone.merge_memory_items


Module Contents
---------------

.. py:class:: EnhancedMemoryItem(/, **data: Any)

   Bases: :py:obj:`MemoryItem`


   Enhanced memory item with additional capabilities.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedMemoryItem
      :collapse:

   .. py:method:: add_child_memory(child_id: str) -> None

      Add a child memory ID.


      .. autolink-examples:: add_child_memory
         :collapse:


   .. py:method:: add_related_memory(memory_id: str) -> None

      Add a related memory ID.


      .. autolink-examples:: add_related_memory
         :collapse:


   .. py:method:: calculate_composite_score() -> float

      Calculate composite relevance score.


      .. autolink-examples:: calculate_composite_score
         :collapse:


   .. py:method:: extract_fact(fact: str) -> None

      Add an extracted fact.


      .. autolink-examples:: extract_fact
         :collapse:


   .. py:method:: from_dict(data: dict[str, Any]) -> EnhancedMemoryItem
      :classmethod:


      Create from dictionary.


      .. autolink-examples:: from_dict
         :collapse:


   .. py:method:: from_memory_item(memory_item: MemoryItem) -> EnhancedMemoryItem
      :classmethod:


      Create enhanced memory from basic memory item.


      .. autolink-examples:: from_memory_item
         :collapse:


   .. py:method:: set_parent_memory(parent_id: str) -> None

      Set parent memory ID.


      .. autolink-examples:: set_parent_memory
         :collapse:


   .. py:method:: to_dict() -> dict[str, Any]

      Convert to dictionary including enhanced fields.


      .. autolink-examples:: to_dict
         :collapse:


   .. py:method:: update_retrieval(context: str = '') -> None

      Update retrieval tracking.


      .. autolink-examples:: update_retrieval
         :collapse:


   .. py:attribute:: child_memories
      :type:  list[str]
      :value: None



   .. py:attribute:: embedding
      :type:  list[float] | None
      :value: None



   .. py:attribute:: extracted_facts
      :type:  list[str]
      :value: None



   .. py:attribute:: last_retrieved
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: parent_memory
      :type:  str | None
      :value: None



   .. py:attribute:: processing_status
      :type:  str
      :value: None



   .. py:attribute:: quality_score
      :type:  float
      :value: None



   .. py:attribute:: related_memories
      :type:  list[str]
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: retrieval_contexts
      :type:  list[str]
      :value: None



   .. py:attribute:: retrieval_count
      :type:  int
      :value: None



   .. py:attribute:: sentiment
      :type:  str | None
      :value: None



   .. py:attribute:: summary
      :type:  str | None
      :value: None



.. py:class:: ImportanceLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Importance levels for memory items.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ImportanceLevel
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: TRIVIAL
      :value: 'trivial'



.. py:class:: KnowledgeTriple(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Knowledge graph triple structure (subject-predicate-object).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeTriple
      :collapse:

   .. py:method:: from_dict(data: dict[str, Any]) -> KnowledgeTriple
      :classmethod:


      Create from dictionary.


      .. autolink-examples:: from_dict
         :collapse:


   .. py:method:: to_dict() -> dict[str, Any]

      Convert to dictionary for storage.


      .. autolink-examples:: to_dict
         :collapse:


   .. py:method:: to_string() -> str

      Convert triple to readable string.


      .. autolink-examples:: to_string
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: object
      :type:  str
      :value: None



   .. py:attribute:: predicate
      :type:  str
      :value: None



   .. py:attribute:: source
      :type:  str | None
      :value: None



   .. py:attribute:: subject
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: MemoryItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Basic memory item with core attributes.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryItem
      :collapse:

   .. py:method:: add_entity(entity: str) -> None

      Add an entity to the memory.


      .. autolink-examples:: add_entity
         :collapse:


   .. py:method:: add_relation(relation: KnowledgeTriple) -> None

      Add a knowledge relation.


      .. autolink-examples:: add_relation
         :collapse:


   .. py:method:: add_tag(tag: str) -> None

      Add a tag to the memory.


      .. autolink-examples:: add_tag
         :collapse:


   .. py:method:: from_dict(data: dict[str, Any]) -> MemoryItem
      :classmethod:


      Create from dictionary.


      .. autolink-examples:: from_dict
         :collapse:


   .. py:method:: remove_tag(tag: str) -> bool

      Remove a tag from the memory.


      .. autolink-examples:: remove_tag
         :collapse:


   .. py:method:: to_dict() -> dict[str, Any]

      Convert to dictionary for storage.


      .. autolink-examples:: to_dict
         :collapse:


   .. py:method:: update_access() -> None

      Update access tracking.


      .. autolink-examples:: update_access
         :collapse:


   .. py:method:: validate_content(v: str) -> str
      :classmethod:


      Validate content is not empty.


      .. autolink-examples:: validate_content
         :collapse:


   .. py:method:: validate_tags(v: list[str]) -> list[str]
      :classmethod:


      Validate and normalize tags.


      .. autolink-examples:: validate_tags
         :collapse:


   .. py:attribute:: access_count
      :type:  int
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: context_id
      :type:  str | None
      :value: None



   .. py:attribute:: entities
      :type:  list[str]
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  ImportanceLevel
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: memory_type
      :type:  MemoryType
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: relations
      :type:  list[KnowledgeTriple]
      :value: None



   .. py:attribute:: source
      :type:  str | None
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of memory for classification.

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



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



.. py:function:: create_knowledge_triple(subject: str, predicate: str, object: str, confidence: float = 1.0, source: str | None = None) -> KnowledgeTriple

   Create a knowledge triple.


   .. autolink-examples:: create_knowledge_triple
      :collapse:

.. py:function:: create_memory_item(content: str, memory_type: MemoryType = MemoryType.SEMANTIC, importance: ImportanceLevel = ImportanceLevel.MEDIUM, tags: list[str] | None = None, context_id: str | None = None, user_id: str | None = None, source: str | None = None, enhanced: bool = False) -> MemoryItem | EnhancedMemoryItem

   Create a memory item with the specified parameters.


   .. autolink-examples:: create_memory_item
      :collapse:

.. py:function:: merge_memory_items(items: list[MemoryItem]) -> EnhancedMemoryItem

   Merge multiple memory items into one enhanced memory item.


   .. autolink-examples:: merge_memory_items
      :collapse:

