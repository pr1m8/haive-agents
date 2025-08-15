agents.document_modifiers.summarizer.iterative_refinement.state
===============================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement.state


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerInput
   agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerOutput
   agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState


Module Contents
---------------

.. py:class:: IterativeSummarizerInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for the summarizer – supports string, Document, message, or dict content.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeSummarizerInput
      :collapse:

   .. py:method:: normalize_contents(value: str)
      :classmethod:


      Ensure all items are string representations.


      .. autolink-examples:: normalize_contents
         :collapse:


   .. py:attribute:: contents
      :type:  list[str | langchain_core.documents.Document | langchain_core.messages.BaseMessage | dict[str, Any]]
      :value: None



.. py:class:: IterativeSummarizerOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output for the summarizer – stores the final summary result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeSummarizerOutput
      :collapse:

   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:class:: IterativeSummarizerState(/, **data: Any)

   Bases: :py:obj:`IterativeSummarizerInput`, :py:obj:`IterativeSummarizerOutput`


   Full state for the iterative summarizer agent – tracks progress and summary.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeSummarizerState
      :collapse:

   .. py:method:: should_refine() -> Literal['refine_summary', '__end__']


   .. py:attribute:: index
      :type:  int
      :value: None



