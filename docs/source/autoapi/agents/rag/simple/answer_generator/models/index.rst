agents.rag.simple.answer_generator.models
=========================================

.. py:module:: agents.rag.simple.answer_generator.models

.. autoapi-nested-parse::

   Answer generator models for SimpleRAG.


   .. autolink-examples:: agents.rag.simple.answer_generator.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple.answer_generator.models.RAGAnswer


Module Contents
---------------

.. py:class:: RAGAnswer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output model for RAG answer generation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGAnswer
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



