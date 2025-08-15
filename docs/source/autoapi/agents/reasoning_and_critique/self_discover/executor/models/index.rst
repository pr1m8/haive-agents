agents.reasoning_and_critique.self_discover.executor.models
===========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.executor.models

.. autoapi-nested-parse::

   Models for the Self-Discover Executor Agent.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.executor.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.executor.models.ExecutionResult
   agents.reasoning_and_critique.self_discover.executor.models.StepResult


Module Contents
---------------

.. py:class:: ExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The complete execution result of the structured reasoning process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionResult
      :collapse:

   .. py:attribute:: alternative_perspectives
      :type:  list[str]
      :value: None



   .. py:attribute:: final_solution
      :type:  str
      :value: None



   .. py:attribute:: implementation_recommendations
      :type:  str
      :value: None



   .. py:attribute:: solution_confidence
      :type:  float
      :value: None



   .. py:attribute:: step_results
      :type:  list[StepResult]
      :value: None



   .. py:attribute:: success_criteria_met
      :type:  list[str]
      :value: None



   .. py:attribute:: supporting_analysis
      :type:  str
      :value: None



   .. py:attribute:: task_summary
      :type:  str
      :value: None



.. py:class:: StepResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of executing a single reasoning step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepResult
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: findings
      :type:  str
      :value: None



   .. py:attribute:: next_step_recommendations
      :type:  str | None
      :value: None



   .. py:attribute:: step_name
      :type:  str
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



