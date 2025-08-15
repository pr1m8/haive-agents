agents.planning.llm_compiler_v3.models
======================================

.. py:module:: agents.planning.llm_compiler_v3.models

.. autoapi-nested-parse::

   Pydantic models for LLM Compiler V3 Agent.

   This module defines structured data models for the LLM Compiler pattern
   optimized for Enhanced MultiAgent V3 architecture.


   .. autolink-examples:: agents.planning.llm_compiler_v3.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler_v3.models.CompilerInput
   agents.planning.llm_compiler_v3.models.CompilerOutput
   agents.planning.llm_compiler_v3.models.CompilerPlan
   agents.planning.llm_compiler_v3.models.CompilerTask
   agents.planning.llm_compiler_v3.models.ExecutionMode
   agents.planning.llm_compiler_v3.models.ParallelExecutionResult
   agents.planning.llm_compiler_v3.models.ReplanRequest
   agents.planning.llm_compiler_v3.models.TaskDependency


Module Contents
---------------

.. py:class:: CompilerInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input to the LLM Compiler V3 Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerInput
      :collapse:

   .. py:attribute:: available_tools
      :type:  list[str] | None
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: execution_preferences
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: query
      :type:  str
      :value: None



.. py:class:: CompilerOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final output from the LLM Compiler V3 Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerOutput
      :collapse:

   .. py:method:: get_failed_tasks() -> list[ParallelExecutionResult]

      Get only the failed tasks.


      .. autolink-examples:: get_failed_tasks
         :collapse:


   .. py:method:: get_successful_tasks() -> list[ParallelExecutionResult]

      Get only the successfully executed tasks.


      .. autolink-examples:: get_successful_tasks
         :collapse:


   .. py:attribute:: execution_plan
      :type:  CompilerPlan
      :value: None



   .. py:attribute:: execution_results
      :type:  list[ParallelExecutionResult]
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: parallel_efficiency
      :type:  float | None
      :value: None



   .. py:attribute:: reasoning_trace
      :type:  list[str]
      :value: None



   .. py:property:: success_rate
      :type: float


      Calculate the success rate of task execution.

      .. autolink-examples:: success_rate
         :collapse:


   .. py:attribute:: tasks_executed
      :type:  int
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



.. py:class:: CompilerPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Execution plan containing tasks and their dependencies.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerPlan
      :collapse:

   .. py:method:: get_executable_tasks(completed_task_ids: list[str]) -> list[CompilerTask]

      Get tasks that can be executed now (dependencies satisfied).


      .. autolink-examples:: get_executable_tasks
         :collapse:


   .. py:method:: get_join_task() -> CompilerTask | None

      Get the final join task if it exists.


      .. autolink-examples:: get_join_task
         :collapse:


   .. py:method:: get_task_by_id(task_id: str) -> CompilerTask | None

      Find task by ID.


      .. autolink-examples:: get_task_by_id
         :collapse:


   .. py:method:: validate_dependencies() -> list[str]

      Validate that all dependencies reference existing tasks.


      .. autolink-examples:: validate_dependencies
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



   .. py:attribute:: max_parallel_tasks
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: tasks
      :type:  list[CompilerTask]
      :value: None



.. py:class:: CompilerTask(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual task in the LLM Compiler execution DAG.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerTask
      :collapse:

   .. py:method:: can_execute_with_results(completed_tasks: list[str]) -> bool

      Check if all dependencies are satisfied.


      .. autolink-examples:: can_execute_with_results
         :collapse:


   .. py:method:: has_dependencies() -> bool

      Check if this task has any dependencies.


      .. autolink-examples:: has_dependencies
         :collapse:


   .. py:attribute:: arguments
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: dependencies
      :type:  list[TaskDependency]
      :value: None



   .. py:property:: dependency_ids
      :type: list[str]


      Get list of task IDs this task depends on.

      .. autolink-examples:: dependency_ids
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_duration
      :type:  float | None
      :value: None



   .. py:property:: is_join_task
      :type: bool


      Check if this is the final join task.

      .. autolink-examples:: is_join_task
         :collapse:


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



   .. py:attribute:: tool_name
      :type:  str
      :value: None



.. py:class:: ExecutionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Execution mode for tasks.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionMode
      :collapse:

   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



.. py:class:: ParallelExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from executing a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelExecutionResult
      :collapse:

   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: result
      :type:  Any
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



   .. py:attribute:: tool_name
      :type:  str
      :value: None



.. py:class:: ReplanRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Request for replanning when initial plan fails.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReplanRequest
      :collapse:

   .. py:attribute:: failed_tasks
      :type:  list[str]
      :value: None



   .. py:attribute:: feedback
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: partial_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: suggested_changes
      :type:  list[str] | None
      :value: None



.. py:class:: TaskDependency(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a dependency between tasks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskDependency
      :collapse:

   .. py:method:: resolve_reference() -> str

      Generate reference string for task dependency.


      .. autolink-examples:: resolve_reference
         :collapse:


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: output_key
      :type:  str | None
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



