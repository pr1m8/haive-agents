agents.planning.models.base
===========================

.. py:module:: agents.planning.models.base

.. autoapi-nested-parse::

   Base models for the unified planning system.

   This module provides the foundation for a flexible planning system that can support
   various planning patterns including Plan-and-Execute, ReWOO, LLM Compiler, FLARE RAG,
   and recursive planning capabilities.

   Key Design Principles:
   1. Composable: Different planning patterns can mix and match components
   2. Extensible: Easy to add new step types and planning patterns
   3. Type-safe: Comprehensive validation and type checking
   4. Resource-aware: Built-in support for resource tracking and constraints


   .. autolink-examples:: agents.planning.models.base
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.models.base.AnyStep
   agents.planning.models.base.TPlan


Classes
-------

.. autoapisummary::

   agents.planning.models.base.ActionStep
   agents.planning.models.base.AdaptivePlan
   agents.planning.models.base.BasePlan
   agents.planning.models.base.BaseStep
   agents.planning.models.base.ConditionalStep
   agents.planning.models.base.DAGPlan
   agents.planning.models.base.Dependency
   agents.planning.models.base.DependencyType
   agents.planning.models.base.ExecutionMode
   agents.planning.models.base.ParallelStep
   agents.planning.models.base.RecursiveStep
   agents.planning.models.base.ResearchStep
   agents.planning.models.base.SequentialPlan
   agents.planning.models.base.StepMetadata
   agents.planning.models.base.StepStatus
   agents.planning.models.base.StepType


Module Contents
---------------

.. py:class:: ActionStep(/, **data: Any)

   Bases: :py:obj:`BaseStep`


   Step that performs a specific action or tool call.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionStep
      :collapse:

   .. py:attribute:: expected_output_schema
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



   .. py:attribute:: tool_args
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: tool_name
      :type:  str | None
      :value: None



.. py:class:: AdaptivePlan(/, **data: Any)

   Bases: :py:obj:`BasePlan`


   Plan that can adapt during execution (FLARE style).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptivePlan
      :collapse:

   .. py:method:: adapt(context: dict[str, Any]) -> None

      Adapt plan based on execution context.


      .. autolink-examples:: adapt
         :collapse:


   .. py:method:: should_adapt(context: dict[str, Any]) -> bool

      Check if plan should adapt based on context.


      .. autolink-examples:: should_adapt
         :collapse:


   .. py:attribute:: adaptation_count
      :type:  int
      :value: None



   .. py:attribute:: adaptation_triggers
      :type:  list[str]
      :value: None



   .. py:attribute:: max_adaptations
      :type:  int
      :value: None



.. py:class:: BasePlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for all planning patterns.

   This provides core planning functionality while allowing different
   planning strategies to extend and customize behavior.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BasePlan
      :collapse:

   .. py:method:: add_step(step: AnyStep) -> None

      Add a step to the plan.


      .. autolink-examples:: add_step
         :collapse:


   .. py:method:: get_execution_order() -> list[list[AnyStep]]

      Get steps organized by execution order (batches for parallel execution).


      .. autolink-examples:: get_execution_order
         :collapse:


   .. py:method:: get_step(step_id: str) -> AnyStep | None

      Get step by ID.


      .. autolink-examples:: get_step
         :collapse:


   .. py:method:: to_mermaid() -> str

      Generate Mermaid diagram of plan.


      .. autolink-examples:: to_mermaid
         :collapse:


   .. py:method:: to_prompt_format() -> str

      Format plan for inclusion in prompts.


      .. autolink-examples:: to_prompt_format
         :collapse:


   .. py:method:: update_ready_steps() -> list[AnyStep]

      Update and return steps that are ready to execute.


      .. autolink-examples:: update_ready_steps
         :collapse:


   .. py:property:: completed_steps
      :type: list[AnyStep]


      Get completed steps.

      .. autolink-examples:: completed_steps
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:property:: failed_steps
      :type: list[AnyStep]


      Get failed steps.

      .. autolink-examples:: failed_steps
         :collapse:


   .. py:property:: has_failures
      :type: bool


      Check if any steps failed.

      .. autolink-examples:: has_failures
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:property:: is_complete
      :type: bool


      Check if plan is complete.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:property:: pending_steps
      :type: list[AnyStep]


      Get pending steps.

      .. autolink-examples:: pending_steps
         :collapse:


   .. py:property:: progress_percentage
      :type: float


      Calculate completion percentage.

      .. autolink-examples:: progress_percentage
         :collapse:


   .. py:property:: ready_steps
      :type: list[AnyStep]


      Get steps ready to execute.

      .. autolink-examples:: ready_steps
         :collapse:


   .. py:attribute:: steps
      :type:  list[AnyStep]
      :value: None



   .. py:property:: total_steps
      :type: int


      Total number of steps.

      .. autolink-examples:: total_steps
         :collapse:


   .. py:attribute:: updated_at
      :type:  datetime.datetime
      :value: None



.. py:class:: BaseStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for all planning steps.

   This provides the core functionality that all step types share,
   while being flexible enough to support various planning patterns.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseStep
      :collapse:

   .. py:method:: add_dependency(step_id: str, dependency_type: DependencyType = DependencyType.HARD, condition: str | None = None, required_output: str | None = None) -> None

      Add a dependency to this step.


      .. autolink-examples:: add_dependency
         :collapse:


   .. py:method:: is_ready(completed_steps: dict[str, Any]) -> bool

      Check if all dependencies are satisfied.


      .. autolink-examples:: is_ready
         :collapse:


   .. py:method:: mark_completed(output: dict[str, Any] | None = None) -> None

      Mark step as completed.


      .. autolink-examples:: mark_completed
         :collapse:


   .. py:method:: mark_failed(error: str) -> None

      Mark step as failed.


      .. autolink-examples:: mark_failed
         :collapse:


   .. py:method:: mark_in_progress() -> None

      Mark step as in progress.


      .. autolink-examples:: mark_in_progress
         :collapse:


   .. py:method:: mark_ready() -> None

      Mark step as ready to execute.


      .. autolink-examples:: mark_ready
         :collapse:


   .. py:method:: to_prompt_format() -> str

      Format step for inclusion in prompts.


      .. autolink-examples:: to_prompt_format
         :collapse:


   .. py:method:: validate_unique_dependencies(v: list[Dependency]) -> list[Dependency]
      :classmethod:


      Ensure no duplicate dependencies.


      .. autolink-examples:: validate_unique_dependencies
         :collapse:


   .. py:attribute:: dependencies
      :type:  list[Dependency]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: input_data
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: metadata
      :type:  StepMetadata
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_data
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: status
      :type:  StepStatus
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



.. py:class:: ConditionalStep(/, **data: Any)

   Bases: :py:obj:`BaseStep`


   Step with conditional execution paths.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConditionalStep
      :collapse:

   .. py:attribute:: condition
      :type:  str
      :value: None



   .. py:attribute:: else_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



   .. py:attribute:: then_steps
      :type:  list[str]
      :value: None



.. py:class:: DAGPlan(/, **data: Any)

   Bases: :py:obj:`BasePlan`


   Plan with explicit DAG structure (LLM Compiler style).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DAGPlan
      :collapse:

   .. py:method:: validate_dag() -> bool

      Validate that plan forms a valid DAG (no cycles).


      .. autolink-examples:: validate_dag
         :collapse:


.. py:class:: Dependency(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a dependency between steps.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Dependency
      :collapse:

   .. py:method:: is_satisfied(step_results: dict[str, Any]) -> bool

      Check if this dependency is satisfied.


      .. autolink-examples:: is_satisfied
         :collapse:


   .. py:attribute:: condition
      :type:  str | None
      :value: None



   .. py:attribute:: dependency_type
      :type:  DependencyType
      :value: None



   .. py:attribute:: required_output
      :type:  str | None
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



.. py:class:: DependencyType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Type of dependency between steps.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DependencyType
      :collapse:

   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: DATA
      :value: 'data'



   .. py:attribute:: HARD
      :value: 'hard'



   .. py:attribute:: SOFT
      :value: 'soft'



.. py:class:: ExecutionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   How a step should be executed.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionMode
      :collapse:

   .. py:attribute:: BATCH
      :value: 'batch'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



   .. py:attribute:: STREAM
      :value: 'stream'



.. py:class:: ParallelStep(/, **data: Any)

   Bases: :py:obj:`BaseStep`


   Container for steps that can execute in parallel.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelStep
      :collapse:

   .. py:attribute:: join_strategy
      :type:  str
      :value: None



   .. py:attribute:: parallel_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



.. py:class:: RecursiveStep(/, **data: Any)

   Bases: :py:obj:`BaseStep`


   Step that can spawn sub-plans recursively.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RecursiveStep
      :collapse:

   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



   .. py:attribute:: sub_objective
      :type:  str
      :value: None



   .. py:attribute:: sub_plan_id
      :type:  str | None
      :value: None



.. py:class:: ResearchStep(/, **data: Any)

   Bases: :py:obj:`BaseStep`


   Step for information gathering and research.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchStep
      :collapse:

   .. py:attribute:: max_results
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



   .. py:attribute:: step_type
      :type:  StepType
      :value: None



.. py:class:: SequentialPlan(/, **data: Any)

   Bases: :py:obj:`BasePlan`


   Traditional sequential execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SequentialPlan
      :collapse:

   .. py:method:: add_sequential_step(step: AnyStep, depends_on_previous: bool = True) -> None

      Add step with automatic dependency on previous step.


      .. autolink-examples:: add_sequential_step
         :collapse:


.. py:class:: StepMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Metadata for tracking step execution and debugging.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepMetadata
      :collapse:

   .. py:attribute:: api_calls_made
      :type:  int | None
      :value: None



   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: custom_data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: error_count
      :type:  int
      :value: None



   .. py:property:: execution_time
      :type: float | None


      Calculate execution time in seconds.

      .. autolink-examples:: execution_time
         :collapse:


   .. py:attribute:: last_error
      :type:  str | None
      :value: None



   .. py:attribute:: retry_count
      :type:  int
      :value: None



   .. py:attribute:: started_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: tags
      :type:  set[str]
      :value: None



   .. py:attribute:: tokens_used
      :type:  int | None
      :value: None



   .. py:attribute:: updated_at
      :type:  datetime.datetime
      :value: None



.. py:class:: StepStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Universal status for any plan step.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepStatus
      :collapse:

   .. py:attribute:: BLOCKED
      :value: 'blocked'



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



   .. py:attribute:: READY
      :value: 'ready'



   .. py:attribute:: SKIPPED
      :value: 'skipped'



.. py:class:: StepType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Type of plan step - extensible for different planning patterns.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepType
      :collapse:

   .. py:attribute:: ACTION
      :value: 'action'



   .. py:attribute:: ANALYSIS
      :value: 'analysis'



   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: DECISION
      :value: 'decision'



   .. py:attribute:: EVIDENCE
      :value: 'evidence'



   .. py:attribute:: GENERATION
      :value: 'generation'



   .. py:attribute:: JOIN
      :value: 'join'



   .. py:attribute:: LOOP
      :value: 'loop'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: RECURSIVE
      :value: 'recursive'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: RETRIEVAL
      :value: 'retrieval'



   .. py:attribute:: SYNTHESIS
      :value: 'synthesis'



   .. py:attribute:: TOOL_CALL
      :value: 'tool_call'



   .. py:attribute:: VALIDATION
      :value: 'validation'



.. py:data:: AnyStep

.. py:data:: TPlan

