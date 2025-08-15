agents.document_modifiers.kg.kg_iterative_refinement.state
==========================================================

.. py:module:: agents.document_modifiers.kg.kg_iterative_refinement.state


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_iterative_refinement.state.IterativeGraphTransformerState


Module Contents
---------------

.. py:class:: IterativeGraphTransformerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The state of the iterative graph transformer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IterativeGraphTransformerState
      :collapse:

   .. py:method:: normalize_contents(values: dict) -> dict
      :classmethod:


      Normalize all entries in `contents` to be `Document` objects.


      .. autolink-examples:: normalize_contents
         :collapse:


   .. py:method:: should_refine() -> Literal['refine_summary', '__end__']


   .. py:attribute:: contents
      :type:  list[str | langchain_core.documents.Document | langchain_core.messages.AnyMessage | dict]
      :value: None



   .. py:attribute:: graph_doc
      :type:  langchain_community.graphs.graph_document.GraphDocument | None
      :value: None



   .. py:attribute:: index
      :type:  int
      :value: None



