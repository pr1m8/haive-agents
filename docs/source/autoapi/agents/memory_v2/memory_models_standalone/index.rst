agents.memory_v2.memory_models_standalone
=========================================

.. py:module:: agents.memory_v2.memory_models_standalone

.. autoapi-nested-parse::

   Standalone memory models to avoid broken imports.


   .. autolink-examples:: agents.memory_v2.memory_models_standalone
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_v2.memory_models_standalone.EnhancedMemoryItem
   agents.memory_v2.memory_models_standalone.ImportanceLevel
   agents.memory_v2.memory_models_standalone.KnowledgeTriple
   agents.memory_v2.memory_models_standalone.MemoryItem
   agents.memory_v2.memory_models_standalone.MemoryType


Module Contents
---------------

.. py:class:: EnhancedMemoryItem(/, **data: Any)

   Bases: :py:obj:`MemoryItem`


   Enhanced memory item with V2 features.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EnhancedMemoryItem
      :collapse:

   .. py:attribute:: access_count
      :type:  int
      :value: 0



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: embedding
      :type:  list[float] | None
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  ImportanceLevel
      :value: None



   .. py:attribute:: last_accessed
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: relevance_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: source
      :type:  str | None
      :value: None



   .. py:attribute:: tags
      :type:  list[str]
      :value: None



   .. py:attribute:: user_id
      :type:  str | None
      :value: None



   .. py:attribute:: vector_id
      :type:  str | None
      :value: None



.. py:class:: ImportanceLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Importance levels for memory prioritization.

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



.. py:class:: KnowledgeTriple(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Knowledge graph triple.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeTriple
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: object
      :type:  str


   .. py:attribute:: predicate
      :type:  str


   .. py:attribute:: subject
      :type:  str


.. py:class:: MemoryItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual memory item.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryItem
      :collapse:

   .. py:attribute:: content
      :type:  str


   .. py:attribute:: importance
      :type:  float
      :value: None



   .. py:attribute:: memory_type
      :type:  MemoryType


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: MemoryType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of memory.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryType
      :collapse:

   .. py:attribute:: CONVERSATIONAL
      :value: 'conversational'



   .. py:attribute:: EPISODIC
      :value: 'episodic'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: PROCEDURAL
      :value: 'procedural'



   .. py:attribute:: SEMANTIC
      :value: 'semantic'



