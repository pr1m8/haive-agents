agents.rag.simple.answer_generator
==================================

.. py:module:: agents.rag.simple.answer_generator

.. autoapi-nested-parse::

   Answer generator components for SimpleRAG.


   .. autolink-examples:: agents.rag.simple.answer_generator
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/rag/simple/answer_generator/models/index
   /autoapi/agents/rag/simple/answer_generator/prompts/index


Attributes
----------

.. autoapisummary::

   agents.rag.simple.answer_generator.RAG_CHAT_TEMPLATE


Classes
-------

.. autoapisummary::

   agents.rag.simple.answer_generator.RAGAnswer


Package Contents
----------------

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



.. py:data:: RAG_CHAT_TEMPLATE

