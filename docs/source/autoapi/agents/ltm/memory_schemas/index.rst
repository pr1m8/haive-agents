agents.ltm.memory_schemas
=========================

.. py:module:: agents.ltm.memory_schemas

.. autoapi-nested-parse::

   Memory schemas for LTM agent using LangMem patterns.

   These schemas define the structure of memories that will be extracted
   and managed by the LTM agent.


   .. autolink-examples:: agents.ltm.memory_schemas
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.ltm.memory_schemas.DEFAULT_MEMORY_SCHEMAS
   agents.ltm.memory_schemas.EXTENDED_MEMORY_SCHEMAS
   agents.ltm.memory_schemas.MINIMAL_MEMORY_SCHEMAS


Classes
-------

.. autoapisummary::

   agents.ltm.memory_schemas.ConversationalMemory
   agents.ltm.memory_schemas.FactualMemory
   agents.ltm.memory_schemas.Memory
   agents.ltm.memory_schemas.PersonalContext
   agents.ltm.memory_schemas.UserPreference


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

