agents.rag.base.state
=====================

.. py:module:: agents.rag.base.state


Classes
-------

.. autoapisummary::

   agents.rag.base.state.BaseRAGInputState
   agents.rag.base.state.BaseRAGOutputState
   agents.rag.base.state.BaseRAGState


Module Contents
---------------

.. py:class:: BaseRAGInputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input state for RAG agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseRAGInputState
      :collapse:

   .. py:attribute:: query
      :type:  str
      :value: None



.. py:class:: BaseRAGOutputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output state for RAG agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseRAGOutputState
      :collapse:

   .. py:attribute:: retrieved_documents
      :type:  list[langchain.schema.Document] | list[str] | None
      :value: None



.. py:class:: BaseRAGState(/, **data: Any)

   Bases: :py:obj:`BaseRAGInputState`, :py:obj:`BaseRAGOutputState`


   State for RAG agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseRAGState
      :collapse:

