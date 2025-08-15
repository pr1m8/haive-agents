agents.planning.plan_and_execute.v2.models
==========================================

.. py:module:: agents.planning.plan_and_execute.v2.models

.. autoapi-nested-parse::

   Models for Plan and Execute Agent v2.


   .. autolink-examples:: agents.planning.plan_and_execute.v2.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.v2.models.Act
   agents.planning.plan_and_execute.v2.models.ExecutionResult
   agents.planning.plan_and_execute.v2.models.Plan
   agents.planning.plan_and_execute.v2.models.Response
   agents.planning.plan_and_execute.v2.models.Step


Module Contents
---------------

.. py:class:: Act(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Action to take - either respond or create new plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Act
      :collapse:

   .. py:attribute:: action
      :type:  Response | Plan
      :value: None



.. py:class:: ExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of executing a step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionResult
      :collapse:

   .. py:attribute:: result
      :type:  str
      :value: None



   .. py:attribute:: step_completed
      :type:  bool
      :value: None



   .. py:attribute:: step_id
      :type:  int | None
      :value: None



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A plan containing steps to execute.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:method:: get_next_step() -> Step | None

      Get the next incomplete step.


      .. autolink-examples:: get_next_step
         :collapse:


   .. py:method:: update_status() -> None

      Update plan status based on step completion.


      .. autolink-examples:: update_status
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: status
      :type:  Literal['not_started', 'in_progress', 'complete']
      :value: None



   .. py:attribute:: steps
      :type:  list[Step]
      :value: None



.. py:class:: Response(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final response to user.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Response
      :collapse:

   .. py:attribute:: response
      :type:  str
      :value: None



.. py:class:: Step(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A step in the plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Step
      :collapse:

   .. py:method:: add_result(result: str) -> None

      Add result and mark step as complete.


      .. autolink-examples:: add_result
         :collapse:


   .. py:method:: is_complete() -> bool

      Check if step is complete.


      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: id
      :type:  int
      :value: None



   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: status
      :type:  Literal['not_started', 'in_progress', 'complete']
      :value: None



