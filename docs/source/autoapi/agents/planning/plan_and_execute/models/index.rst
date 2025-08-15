agents.planning.plan_and_execute.models
=======================================

.. py:module:: agents.planning.plan_and_execute.models


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.models.Act
   agents.planning.plan_and_execute.models.Plan
   agents.planning.plan_and_execute.models.Response
   agents.planning.plan_and_execute.models.Step


Module Contents
---------------

.. py:class:: Act(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Action to perform.

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



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a plan containing a recursive structure of steps.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:method:: add_step(step: Step)

      Adds a new step to the plan.


      .. autolink-examples:: add_step
         :collapse:


   .. py:method:: get_last_incomplete_step() -> Step | None

      Retrieves the last incomplete step (either 'in_progress' or 'not_started').


      .. autolink-examples:: get_last_incomplete_step
         :collapse:


   .. py:method:: remove_completed_steps() -> None

      Removes steps that have been completed.


      .. autolink-examples:: remove_completed_steps
         :collapse:


   .. py:method:: update_status() -> None

      Updates the overall status of the plan based on step completion.


      .. autolink-examples:: update_status
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: status
      :type:  Literal['not_started', 'in_progress', 'complete']
      :value: 'not_started'



   .. py:attribute:: steps
      :type:  list[Step]
      :value: None



.. py:class:: Response(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response to user.

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


.. py:class:: Step(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a step that can recursively contain nested steps.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Step
      :collapse:

   .. py:method:: add_result(result: str)

      Marks the step as complete and stores the result.


      .. autolink-examples:: add_result
         :collapse:


   .. py:method:: get_last_incomplete_step(steps: list[Step]) -> Optional[Step]
      :classmethod:


      Retrieves the last step that is either 'in_progress' or 'not_started'.
      Prioritizes 'in_progress' steps to ensure they get completed first.


      .. autolink-examples:: get_last_incomplete_step
         :collapse:


   .. py:method:: is_complete() -> bool

      Check if the step and all its nested steps are complete.


      .. autolink-examples:: is_complete
         :collapse:


   .. py:method:: remove_completed_substeps() -> None

      Removes substeps that have been marked as complete.


      .. autolink-examples:: remove_completed_substeps
         :collapse:


   .. py:attribute:: description
      :type:  str


   .. py:attribute:: id
      :type:  int


   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: status
      :type:  Literal['not_started', 'in_progress', 'complete']
      :value: None



   .. py:attribute:: steps
      :type:  list[Step] | None
      :value: None



