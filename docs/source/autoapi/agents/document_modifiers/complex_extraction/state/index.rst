agents.document_modifiers.complex_extraction.state
==================================================

.. py:module:: agents.document_modifiers.complex_extraction.state


Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.state.ComplexExtractionInput
   agents.document_modifiers.complex_extraction.state.ComplexExtractionOutput
   agents.document_modifiers.complex_extraction.state.ComplexExtractionState


Module Contents
---------------

.. py:class:: ComplexExtractionInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The input for the complex extraction agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexExtractionInput
      :collapse:

   .. py:attribute:: messages
      :type:  Annotated[list, haive.agents.document_modifiers.complex_extraction.utils.add_or_overwrite_messages]
      :value: None



.. py:class:: ComplexExtractionOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The output for the complex extraction agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexExtractionOutput
      :collapse:

   .. py:attribute:: extracted_data
      :type:  list[langchain_core.messages.AnyMessage] | None
      :value: None



.. py:class:: ComplexExtractionState(/, **data: Any)

   Bases: :py:obj:`ComplexExtractionInput`, :py:obj:`ComplexExtractionOutput`


   State for complex extraction.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexExtractionState
      :collapse:

   .. py:attribute:: attempt_number
      :type:  Annotated[int, operator.add]
      :value: None



   .. py:attribute:: initial_num_messages
      :type:  int | None
      :value: None



   .. py:attribute:: input_format
      :type:  Literal['list', 'dict']
      :value: None



