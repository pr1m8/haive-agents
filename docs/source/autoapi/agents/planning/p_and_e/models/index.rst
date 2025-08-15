agents.planning.p_and_e.models
==============================

.. py:module:: agents.planning.p_and_e.models

.. autoapi-nested-parse::

   Models for Plan and Execute Agent System.

   This module defines the data models for planning, execution, and replanning
   in the Plan and Execute agent architecture.


   .. autolink-examples:: agents.planning.p_and_e.models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.p_and_e.models.ReplanAction


Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.models.Act
   agents.planning.p_and_e.models.ExecutionResult
   agents.planning.p_and_e.models.Plan
   agents.planning.p_and_e.models.PlanStep
   agents.planning.p_and_e.models.ReplanDecision
   agents.planning.p_and_e.models.Response
   agents.planning.p_and_e.models.StepStatus
   agents.planning.p_and_e.models.StepType


Module Contents
---------------

.. py:class:: Act(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Action to perform - either respond with answer or continue with plan.

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



   .. py:property:: is_final_response
      :type: bool


      Check if this is a final response.

      .. autolink-examples:: is_final_response
         :collapse:


   .. py:property:: is_plan
      :type: bool


      Check if this is a plan to execute.

      .. autolink-examples:: is_plan
         :collapse:


.. py:class:: ExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from executing a single step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionResult
      :collapse:

   .. py:method:: to_prompt_format() -> str

      Format result for inclusion in prompts.


      .. autolink-examples:: to_prompt_format
         :collapse:


   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time
      :type:  float | None
      :value: None



   .. py:attribute:: output
      :type:  str
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete execution plan with steps and metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:method:: get_step(step_id: int) -> PlanStep | None

      Get a specific step by ID.


      .. autolink-examples:: get_step
         :collapse:


   .. py:method:: serialize_datetime(dt: datetime.datetime) -> str

      Serialize datetime fields to ISO format.


      .. autolink-examples:: serialize_datetime
         :collapse:


   .. py:method:: to_prompt_format() -> str

      Format plan for inclusion in prompts.


      .. autolink-examples:: to_prompt_format
         :collapse:


   .. py:method:: update_step_status(step_id: int, status: StepStatus, result: str | None = None, error: str | None = None) -> bool

      Update the status of a specific step.


      .. autolink-examples:: update_step_status
         :collapse:


   .. py:method:: update_total_steps() -> Plan

      Ensure total_steps matches actual step count.


      .. autolink-examples:: update_total_steps
         :collapse:


   .. py:method:: validate_dependencies(steps: list[PlanStep]) -> list[PlanStep]
      :classmethod:


      Ensure dependencies reference valid step IDs.


      .. autolink-examples:: validate_dependencies
         :collapse:


   .. py:method:: validate_step_ids(steps: list[PlanStep]) -> list[PlanStep]
      :classmethod:


      Ensure step IDs are sequential starting from 1.


      .. autolink-examples:: validate_step_ids
         :collapse:


   .. py:property:: completed_steps
      :type: list[PlanStep]


      Get all completed steps.

      .. autolink-examples:: completed_steps
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:property:: failed_steps
      :type: list[PlanStep]


      Get all failed steps.

      .. autolink-examples:: failed_steps
         :collapse:


   .. py:property:: has_failures
      :type: bool


      Check if any steps have failed.

      .. autolink-examples:: has_failures
         :collapse:


   .. py:property:: is_complete
      :type: bool


      Check if all steps are completed.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:property:: next_step
      :type: PlanStep | None


      Get the next step ready for execution.

      .. autolink-examples:: next_step
         :collapse:


   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:property:: pending_steps
      :type: list[PlanStep]


      Get all pending steps.

      .. autolink-examples:: pending_steps
         :collapse:


   .. py:property:: progress_percentage
      :type: float


      Calculate completion percentage.

      .. autolink-examples:: progress_percentage
         :collapse:


   .. py:attribute:: steps
      :type:  list[PlanStep]
      :value: None



   .. py:attribute:: total_steps
      :type:  int
      :value: None



   .. py:attribute:: updated_at
      :type:  datetime.datetime
      :value: None



.. py:class:: PlanStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in an execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanStep
      :collapse:

   .. py:method:: serialize_datetime(dt: datetime.datetime | None) -> str | None

      Serialize datetime fields to ISO format.


      .. autolink-examples:: serialize_datetime
         :collapse:


   .. py:method:: to_prompt_format() -> str

      Format step for inclusion in prompts.


      .. autolink-examples:: to_prompt_format
         :collapse:


   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: dependencies
      :type:  list[int]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:property:: execution_time
      :type: float | None


      Calculate execution time in seconds.

      .. autolink-examples:: execution_time
         :collapse:


   .. py:attribute:: expected_output
      :type:  str
      :value: None



   .. py:property:: is_ready
      :type: bool


      Check if step is ready to execute (all dependencies completed).

      .. autolink-examples:: is_ready
         :collapse:


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: started_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: status
      :type:  StepStatus
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



.. py:class:: ReplanDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Decision on whether to replan or provide final answer.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReplanDecision
      :collapse:

   .. py:method:: validate_decision_fields() -> ReplanDecision

      Ensure required fields are present based on decision.


      .. autolink-examples:: validate_decision_fields
         :collapse:


   .. py:attribute:: decision
      :type:  Literal['continue', 'replan', 'answer']
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: replan_instructions
      :type:  str | None
      :value: None



   .. py:attribute:: skip_steps
      :type:  list[int] | None
      :value: None



.. py:class:: Response(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response to user with final answer.

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



.. py:class:: StepStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of a plan step.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepStatus
      :collapse:

   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: SKIPPED
      :value: 'skipped'



.. py:class:: StepType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Type of plan step.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepType
      :collapse:

   .. py:attribute:: ACTION
      :value: 'action'



   .. py:attribute:: ANALYSIS
      :value: 'analysis'



   .. py:attribute:: DECISION
      :value: 'decision'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: SYNTHESIS
      :value: 'synthesis'



   .. py:attribute:: VALIDATION
      :value: 'validation'



.. py:data:: ReplanAction

