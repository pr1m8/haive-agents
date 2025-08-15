agents.planning.plan_execute_v3.models
======================================

.. py:module:: agents.planning.plan_execute_v3.models

.. autoapi-nested-parse::

   Plan-and-Execute V3 Models - Structured Output Models for the agent.

   Based on the Plan-and-Execute methodology where planning and execution
   are separated into distinct phases with structured outputs.


   .. autolink-examples:: agents.planning.plan_execute_v3.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.models.ExecutionPlan
   agents.planning.plan_execute_v3.models.Plan
   agents.planning.plan_execute_v3.models.PlanEvaluation
   agents.planning.plan_execute_v3.models.PlanExecuteInput
   agents.planning.plan_execute_v3.models.PlanExecuteOutput
   agents.planning.plan_execute_v3.models.PlanStep
   agents.planning.plan_execute_v3.models.RevisedPlan
   agents.planning.plan_execute_v3.models.StepExecution
   agents.planning.plan_execute_v3.models.StepStatus


Module Contents
---------------

.. py:class:: ExecutionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete execution plan with metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPlan
      :collapse:

   .. py:method:: get_next_step() -> PlanStep | None

      Get the next step ready for execution.


      .. autolink-examples:: get_next_step
         :collapse:


   .. py:method:: get_progress_percentage() -> float

      Calculate completion percentage.


      .. autolink-examples:: get_progress_percentage
         :collapse:


   .. py:method:: has_failures() -> bool

      Check if any steps have failed.


      .. autolink-examples:: has_failures
         :collapse:


   .. py:method:: is_complete() -> bool

      Check if all steps are completed.


      .. autolink-examples:: is_complete
         :collapse:


   .. py:method:: update_total_steps()

      Ensure total_steps matches actual step count.


      .. autolink-examples:: update_total_steps
         :collapse:


   .. py:method:: validate_step_ids(v)
      :classmethod:


      Ensure step IDs are sequential starting from 1.


      .. autolink-examples:: validate_step_ids
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: estimated_duration
      :type:  str | None
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[PlanStep]
      :value: None



   .. py:attribute:: total_steps
      :type:  int
      :value: None



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simple plan model for basic planning operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:method:: from_execution_plan(execution_plan: ExecutionPlan) -> Plan
      :classmethod:


      Create a simple Plan from an ExecutionPlan.


      .. autolink-examples:: from_execution_plan
         :collapse:


   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



   .. py:attribute:: steps
      :type:  list[str]
      :value: None



.. py:class:: PlanEvaluation(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Evaluation of current plan progress and decision on next action.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanEvaluation
      :collapse:

   .. py:method:: validate_decision_fields()

      Ensure required fields are present based on decision.


      .. autolink-examples:: validate_decision_fields
         :collapse:


   .. py:attribute:: current_progress
      :type:  str
      :value: None



   .. py:attribute:: decision
      :type:  str
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: plan_status
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: revision_notes
      :type:  str | None
      :value: None



.. py:class:: PlanExecuteInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input format for the Plan-and-Execute agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanExecuteInput
      :collapse:

   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: max_steps
      :type:  int
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: time_limit
      :type:  int | None
      :value: None



.. py:class:: PlanExecuteOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final output from the Plan-and-Execute agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanExecuteOutput
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: execution_summary
      :type:  str
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: key_findings
      :type:  list[str]
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: revisions_made
      :type:  int
      :value: None



   .. py:attribute:: steps_completed
      :type:  int
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



   .. py:attribute:: total_steps
      :type:  int
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

   .. py:method:: validate_dependencies(v, info)
      :classmethod:


      Ensure dependencies are valid step IDs.


      .. autolink-examples:: validate_dependencies
         :collapse:


   .. py:attribute:: dependencies
      :type:  list[int]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time
      :type:  float | None
      :value: None



   .. py:attribute:: expected_output
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: status
      :type:  StepStatus
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



   .. py:attribute:: tools_required
      :type:  list[str]
      :value: None



.. py:class:: RevisedPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Revised execution plan based on evaluation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RevisedPlan
      :collapse:

   .. py:attribute:: changes_made
      :type:  str
      :value: None



   .. py:attribute:: new_plan
      :type:  ExecutionPlan
      :value: None



   .. py:attribute:: original_objective
      :type:  str
      :value: None



   .. py:attribute:: retained_results
      :type:  list[str]
      :value: None



   .. py:attribute:: revision_reason
      :type:  str
      :value: None



.. py:class:: StepExecution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from executing a single step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepExecution
      :collapse:

   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: observations
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  str
      :value: None



   .. py:attribute:: step_description
      :type:  str
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
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



