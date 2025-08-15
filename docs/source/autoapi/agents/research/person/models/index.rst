agents.research.person.models
=============================

.. py:module:: agents.research.person.models


Classes
-------

.. autoapisummary::

   agents.research.person.models.Queries
   agents.research.person.models.ReflectionOutput


Module Contents
---------------

.. py:class:: Queries(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structure for search queries.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Queries
      :collapse:

   .. py:attribute:: queries
      :type:  list[str]
      :value: None



.. py:class:: ReflectionOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structure for reflection output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionOutput
      :collapse:

   .. py:attribute:: is_satisfactory
      :type:  bool
      :value: None



   .. py:attribute:: missing_fields
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str]
      :value: None



