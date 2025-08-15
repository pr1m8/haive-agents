agents.reasoning_and_critique.reflection.models
===============================================

.. py:module:: agents.reasoning_and_critique.reflection.models

.. autoapi-nested-parse::

   Models for the Reflection Agent.


   .. autolink-examples:: agents.reasoning_and_critique.reflection.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflection.models.ReflectionOutput
   agents.reasoning_and_critique.reflection.models.ReflectionResult
   agents.reasoning_and_critique.reflection.models.SearchQuery


Module Contents
---------------

.. py:class:: ReflectionOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for the output of the reflection step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionOutput
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: reflection
      :type:  ReflectionResult
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str]
      :value: None



.. py:class:: ReflectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for structured reflection output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionResult
      :collapse:

   .. py:method:: as_message() -> dict[str, Any]

      Convert to a message format.


      .. autolink-examples:: as_message
         :collapse:


   .. py:attribute:: found_solution
      :type:  bool
      :value: None



   .. py:attribute:: missing
      :type:  str
      :value: None



   .. py:property:: normalized_score
      :type: float


      Return the score normalized to 0-1.

      .. autolink-examples:: normalized_score
         :collapse:


   .. py:attribute:: reflection
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  int
      :value: None



   .. py:attribute:: superfluous
      :type:  str
      :value: None



.. py:class:: SearchQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a search query.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchQuery
      :collapse:

   .. py:method:: __str__() -> str


   .. py:attribute:: query
      :type:  str
      :value: None



