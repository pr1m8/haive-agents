agents.long_term_memory.models
==============================

.. py:module:: agents.long_term_memory.models


Classes
-------

.. autoapisummary::

   agents.long_term_memory.models.KnowledgeTriple


Module Contents
---------------

.. py:class:: KnowledgeTriple(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A knowledge triple is a tuple of (subject, predicate, object).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeTriple
      :collapse:

   .. py:attribute:: object_
      :type:  str
      :value: None



   .. py:attribute:: predicate
      :type:  str
      :value: None



   .. py:attribute:: subject
      :type:  str
      :value: None



