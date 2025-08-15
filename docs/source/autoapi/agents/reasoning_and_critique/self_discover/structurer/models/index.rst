agents.reasoning_and_critique.self_discover.structurer.models
=============================================================

.. py:module:: agents.reasoning_and_critique.self_discover.structurer.models

.. autoapi-nested-parse::

   Models for the Self-Discover Structurer Agent.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.structurer.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.structurer.models.ReasoningStep
   agents.reasoning_and_critique.self_discover.structurer.models.ReasoningStructure


Module Contents
---------------

.. py:class:: ReasoningStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A single step in the structured reasoning process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStep
      :collapse:

   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: expected_output
      :type:  str
      :value: None



   .. py:attribute:: guiding_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: step_name
      :type:  str
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



.. py:class:: ReasoningStructure(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The complete structured reasoning plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningStructure
      :collapse:

   .. py:attribute:: execution_notes
      :type:  str
      :value: None



   .. py:attribute:: integration_approach
      :type:  str
      :value: None



   .. py:attribute:: reasoning_steps
      :type:  list[ReasoningStep]
      :value: None



   .. py:attribute:: success_criteria
      :type:  list[str]
      :value: None



   .. py:attribute:: task_context
      :type:  str
      :value: None



