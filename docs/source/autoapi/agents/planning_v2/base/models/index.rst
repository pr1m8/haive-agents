agents.planning_v2.base.models
==============================

.. py:module:: agents.planning_v2.base.models

.. autoapi-nested-parse::

   Data models for planning agents.

   This module contains Pydantic models for planning agent configurations,
   plans, steps, and other planning-related data structures.


   .. autolink-examples:: agents.planning_v2.base.models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning_v2.base.models.StepType


Classes
-------

.. autoapisummary::

   agents.planning_v2.base.models.Plan
   agents.planning_v2.base.models.Status
   agents.planning_v2.base.models.Task


Module Contents
---------------

.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`StepType`\ ]


   Generic plan model that can work with any step type.

   Supports both linear and tree/split structures.

   .. attribute:: objective

      What this plan aims to accomplish

   .. attribute:: steps

      List of steps (can be Tasks or nested Plans)

   .. attribute:: result

      The outcome of the plan execution

   .. attribute:: status

      Current status of the plan

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:method:: add_parallel_steps(steps: list[Union[StepType, Plan]]) -> list[Union[StepType, Plan]]

      Add multiple steps that can be executed in parallel (same parent index).


      .. autolink-examples:: add_parallel_steps
         :collapse:


   .. py:method:: add_step(step: Union[StepType, Plan]) -> Union[StepType, Plan]

      Add a step with auto-indexing.


      .. autolink-examples:: add_step
         :collapse:


   .. py:method:: create_subplan(objective: str) -> Plan

      Create a nested subplan for tree structures.


      .. autolink-examples:: create_subplan
         :collapse:


   .. py:attribute:: _index
      :type:  int
      :value: None



   .. py:attribute:: _next_index
      :type:  int
      :value: None



   .. py:attribute:: _parent_index
      :type:  int | None
      :value: None



   .. py:property:: completed_count
      :type: int


      Number of completed steps.

      .. autolink-examples:: completed_count
         :collapse:


   .. py:property:: completed_steps
      :type: list[Union[StepType, Plan]]


      List of completed steps.

      .. autolink-examples:: completed_steps
         :collapse:


   .. py:property:: current_step
      :type: Union[StepType, Plan] | None


      The current step being executed (first in_progress or pending).

      .. autolink-examples:: current_step
         :collapse:


   .. py:property:: failed_steps
      :type: list[Union[StepType, Plan]]


      List of failed steps.

      .. autolink-examples:: failed_steps
         :collapse:


   .. py:property:: has_failures
      :type: bool


      Whether any steps have failed.

      .. autolink-examples:: has_failures
         :collapse:


   .. py:property:: is_complete
      :type: bool


      Whether all steps are completed.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:property:: progress_percentage
      :type: float


      Percentage of completion (0-100).

      .. autolink-examples:: progress_percentage
         :collapse:


   .. py:property:: remaining_count
      :type: int


      Number of steps remaining.

      .. autolink-examples:: remaining_count
         :collapse:


   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: status
      :type:  Status
      :value: None



   .. py:attribute:: steps
      :type:  list[Union[StepType, Plan]]
      :value: None



   .. py:property:: steps_remaining
      :type: list[Union[StepType, Plan]]


      List of steps that haven't been completed yet.

      .. autolink-examples:: steps_remaining
         :collapse:


   .. py:property:: total_steps
      :type: int


      Total number of steps (including nested).

      .. autolink-examples:: total_steps
         :collapse:


.. py:class:: Status

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status for tasks and plans.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Status
      :collapse:

   .. py:attribute:: CANCELLED
      :value: 'cancelled'



   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: PENDING
      :value: 'pending'



.. py:class:: Task(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simple task model.

   .. attribute:: objective

      What this task aims to accomplish

   .. attribute:: result

      The outcome of the task (None if not completed)

   .. attribute:: status

      Current status of the task

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Task
      :collapse:

   .. py:attribute:: _index
      :type:  int
      :value: None



   .. py:attribute:: _parent_index
      :type:  int | None
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: status
      :type:  Status
      :value: None



.. py:data:: StepType

