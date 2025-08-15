agents.memory_reorganized.integrations.langmem_schemas
======================================================

.. py:module:: agents.memory_reorganized.integrations.langmem_schemas

.. autoapi-nested-parse::

   Memory_Schemas schema module.

   This module provides memory schemas functionality for the Haive framework.

   Classes:
       Memory: Memory implementation.
       UserPreference: UserPreference implementation.
       FactualMemory: FactualMemory implementation.


   .. autolink-examples:: agents.memory_reorganized.integrations.langmem_schemas
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.integrations.langmem_schemas.DEFAULT_MEMORY_SCHEMAS
   agents.memory_reorganized.integrations.langmem_schemas.EXTENDED_MEMORY_SCHEMAS
   agents.memory_reorganized.integrations.langmem_schemas.MINIMAL_MEMORY_SCHEMAS


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.integrations.langmem_schemas.ConversationalMemory
   agents.memory_reorganized.integrations.langmem_schemas.FactualMemory
   agents.memory_reorganized.integrations.langmem_schemas.Memory
   agents.memory_reorganized.integrations.langmem_schemas.PersonalContext
   agents.memory_reorganized.integrations.langmem_schemas.UserPreference


Module Contents
---------------

.. py:class:: ConversationalMemory(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   General conversational memory.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationalMemory
      :collapse:

   .. py:attribute:: action_items
      :type:  list[str]
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: emotional_tone
      :type:  str | None
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



.. py:class:: FactualMemory(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Factual information memory.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FactualMemory
      :collapse:

   .. py:attribute:: domain
      :type:  str
      :value: None



   .. py:attribute:: fact
      :type:  str
      :value: None



   .. py:attribute:: source
      :type:  str | None
      :value: None



   .. py:attribute:: verification_level
      :type:  str
      :value: None



.. py:class:: Memory(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Basic memory schema following LangMem patterns.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Memory
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



.. py:class:: PersonalContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Personal context and relationship memory.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonalContext
      :collapse:

   .. py:attribute:: context
      :type:  str
      :value: None



   .. py:attribute:: importance
      :type:  str
      :value: None



   .. py:attribute:: person
      :type:  str
      :value: None



   .. py:attribute:: relationship
      :type:  str
      :value: None



.. py:class:: UserPreference(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   User preference memory.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: UserPreference
      :collapse:

   .. py:attribute:: category
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: context
      :type:  str
      :value: None



   .. py:attribute:: preference
      :type:  str
      :value: None



.. py:data:: DEFAULT_MEMORY_SCHEMAS

.. py:data:: EXTENDED_MEMORY_SCHEMAS

.. py:data:: MINIMAL_MEMORY_SCHEMAS

