agents.memory.models
====================

.. py:module:: agents.memory.models


Classes
-------

.. autoapisummary::

   agents.memory.models.KnowledgeTriple
   agents.memory.models.MemoryItem


Module Contents
---------------

.. py:class:: KnowledgeTriple(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured knowledge triple for graph-based memory.

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



   .. py:attribute:: object_
      :type:  str


   .. py:attribute:: predicate
      :type:  str


   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: subject
      :type:  str


   .. py:attribute:: timestamp
      :type:  str | None
      :value: None



.. py:class:: MemoryItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base memory item class for structured and unstructured memories.

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


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  str | None
      :value: None



