pro_search.tasks.models
=======================

.. py:module:: pro_search.tasks.models

.. autoapi-nested-parse::

   Pydantic models for recursive conditional planning with tree-based task decomposition.
   Supports dynamic planning, parallel execution, and adaptive replanning.


   .. autolink-examples:: pro_search.tasks.models
      :collapse:


Classes
-------

.. autoapisummary::

   pro_search.tasks.models.ExecutionPlan
   pro_search.tasks.models.PlanningState
   pro_search.tasks.models.PlanningStrategy
   pro_search.tasks.models.ReplanningAnalysis
   pro_search.tasks.models.TaskDecomposition
   pro_search.tasks.models.TaskDependency
   pro_search.tasks.models.TaskMetadata
   pro_search.tasks.models.TaskNode
   pro_search.tasks.models.TaskPriority
   pro_search.tasks.models.TaskResource
   pro_search.tasks.models.TaskStatus


Module Contents
---------------

.. py:class:: ExecutionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Execution plan for a set of tasks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPlan
      :collapse:

   .. py:method:: calculate_resource_requirements() -> ExecutionPlan

      Calculate total resource requirements.


      .. autolink-examples:: calculate_resource_requirements
         :collapse:


   .. py:property:: can_parallelize
      :type: bool


      Check if any parallelization is possible.

      .. autolink-examples:: can_parallelize
         :collapse:


   .. py:attribute:: estimated_duration
      :type:  int
      :value: None



   .. py:attribute:: execution_strategy
      :type:  Literal['parallel', 'sequential', 'mixed']
      :value: None



   .. py:attribute:: parallel_groups
      :type:  list[list[str]]
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: resource_requirements
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: tasks_to_execute
      :type:  list[TaskNode]
      :value: None



.. py:class:: PlanningState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for recursive planning workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanningState
      :collapse:

   .. py:method:: add_task(task: TaskNode, parent_id: str | None = None) -> None

      Add a task to the tree.


      .. autolink-examples:: add_task
         :collapse:


   .. py:method:: update_task_status(task_id: str, status: TaskStatus, result: dict[str, Any] | None = None) -> None

      Update task status and handle state transitions.


      .. autolink-examples:: update_task_status
         :collapse:


   .. py:attribute:: active_tasks
      :type:  set[str]
      :value: None



   .. py:attribute:: all_tasks
      :type:  dict[str, TaskNode]
      :value: None



   .. py:attribute:: completed_tasks
      :type:  set[str]
      :value: None



   .. py:property:: completion_percentage
      :type: float


      Calculate completion percentage.

      .. autolink-examples:: completion_percentage
         :collapse:


   .. py:attribute:: constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:property:: critical_path
      :type: list[str]


      Get current critical path.

      .. autolink-examples:: critical_path
         :collapse:


   .. py:property:: executable_tasks
      :type: list[TaskNode]


      Get tasks ready for execution.

      .. autolink-examples:: executable_tasks
         :collapse:


   .. py:attribute:: failed_tasks
      :type:  set[str]
      :value: None



   .. py:attribute:: goal
      :type:  str
      :value: None



   .. py:property:: is_complete
      :type: bool


      Check if planning goal is achieved.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:property:: needs_replanning
      :type: bool


      Check if replanning is needed.

      .. autolink-examples:: needs_replanning
         :collapse:


   .. py:attribute:: planning_iterations
      :type:  int
      :value: None



   .. py:attribute:: replanning_triggers
      :type:  list[str]
      :value: None



   .. py:attribute:: resource_usage
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: root_task
      :type:  TaskNode | None
      :value: None



   .. py:attribute:: strategy
      :type:  PlanningStrategy
      :value: None



.. py:class:: PlanningStrategy(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategy configuration for the planning process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanningStrategy
      :collapse:

   .. py:method:: validate_strategy_coherence() -> PlanningStrategy

      Ensure strategy settings are coherent.


      .. autolink-examples:: validate_strategy_coherence
         :collapse:


   .. py:attribute:: allow_dynamic_replanning
      :type:  bool
      :value: None



   .. py:attribute:: decomposition_strategy
      :type:  Literal['breadth_first', 'depth_first', 'balanced', 'adaptive']
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: max_width
      :type:  int
      :value: None



   .. py:attribute:: optimization_goals
      :type:  list[Literal['minimize_time', 'minimize_resources', 'maximize_parallelism', 'maximize_reliability', 'balanced']]
      :value: None



   .. py:attribute:: parallelization_threshold
      :type:  int
      :value: None



   .. py:attribute:: resource_constraints
      :type:  dict[str, int]
      :value: None



.. py:class:: ReplanningAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis for replanning decision.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReplanningAnalysis
      :collapse:

   .. py:attribute:: adjusted_estimates
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: failure_analysis
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: new_constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: replanning_strategy
      :type:  Literal['full_replan', 'partial_replan', 'retry_failed', 'adjust_strategy']
      :value: None



   .. py:attribute:: should_replan
      :type:  bool
      :value: None



   .. py:attribute:: tasks_to_modify
      :type:  list[str]
      :value: None



   .. py:attribute:: trigger_reason
      :type:  str
      :value: None



.. py:class:: TaskDecomposition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of decomposing a high-level task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskDecomposition
      :collapse:

   .. py:method:: calculate_critical_path() -> TaskDecomposition

      Calculate critical path if not provided.


      .. autolink-examples:: calculate_critical_path
         :collapse:


   .. py:attribute:: critical_path
      :type:  list[str]
      :value: None



   .. py:attribute:: decomposition_reasoning
      :type:  str
      :value: None



   .. py:attribute:: estimated_total_duration
      :type:  int
      :value: None



   .. py:attribute:: execution_order
      :type:  Literal['sequential', 'parallel', 'mixed']
      :value: None



   .. py:attribute:: original_task
      :type:  str
      :value: None



   .. py:property:: parallelizable_groups
      :type: list[list[str]]


      Identify groups of tasks that can run in parallel.

      .. autolink-examples:: parallelizable_groups
         :collapse:


   .. py:attribute:: subtasks
      :type:  list[TaskNode]
      :value: None



.. py:class:: TaskDependency(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Dependency relationship between tasks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskDependency
      :collapse:

   .. py:attribute:: condition
      :type:  str | None
      :value: None



   .. py:attribute:: dependency_type
      :type:  Literal['requires', 'blocks', 'relates_to']
      :value: None



   .. py:attribute:: is_strict
      :type:  bool
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



.. py:class:: TaskMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Metadata for task tracking and optimization.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskMetadata
      :collapse:

   .. py:attribute:: actual_duration_seconds
      :type:  int | None
      :value: None



   .. py:property:: can_retry
      :type: bool


      Check if task can be retried.

      .. autolink-examples:: can_retry
         :collapse:


   .. py:property:: efficiency_ratio
      :type: float | None


      Calculate efficiency ratio (estimated vs actual).

      .. autolink-examples:: efficiency_ratio
         :collapse:


   .. py:attribute:: estimated_duration_seconds
      :type:  int
      :value: None



   .. py:attribute:: last_error
      :type:  str | None
      :value: None



   .. py:attribute:: max_retries
      :type:  int
      :value: None



   .. py:attribute:: retry_count
      :type:  int
      :value: None



   .. py:attribute:: tags
      :type:  set[str]
      :value: None



.. py:class:: TaskNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual task node in the planning tree.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskNode
      :collapse:

   .. py:method:: can_start(completed_tasks: set[str]) -> bool

      Check if all dependencies are satisfied.


      .. autolink-examples:: can_start
         :collapse:


   .. py:method:: validate_children_for_type(v, info) -> Any
      :classmethod:


      Validate children based on task type.


      .. autolink-examples:: validate_children_for_type
         :collapse:


   .. py:attribute:: action
      :type:  str | None
      :value: None



   .. py:attribute:: children
      :type:  list[str]
      :value: None



   .. py:attribute:: decision_criteria
      :type:  str | None
      :value: None



   .. py:attribute:: dependencies
      :type:  list[TaskDependency]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:property:: is_complete
      :type: bool


      Check if task is complete.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:property:: is_executable
      :type: bool


      Check if task can be executed.

      .. autolink-examples:: is_executable
         :collapse:


   .. py:property:: is_leaf
      :type: bool


      Check if this is a leaf node.

      .. autolink-examples:: is_leaf
         :collapse:


   .. py:attribute:: loop_condition
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  TaskMetadata
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parent_id
      :type:  str | None
      :value: None



   .. py:attribute:: priority
      :type:  TaskPriority
      :value: None



   .. py:attribute:: required_resources
      :type:  list[TaskResource]
      :value: None



   .. py:attribute:: result
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: status
      :type:  TaskStatus
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



   .. py:attribute:: task_type
      :type:  Literal['action', 'decision', 'parallel', 'sequential', 'loop']
      :value: None



.. py:class:: TaskPriority

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Priority levels for tasks.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskPriority
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: OPTIONAL
      :value: 'optional'



.. py:class:: TaskResource(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Resource requirements for a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskResource
      :collapse:

   .. py:attribute:: is_exclusive
      :type:  bool
      :value: None



   .. py:attribute:: quantity
      :type:  float
      :value: None



   .. py:attribute:: resource_id
      :type:  str
      :value: None



   .. py:property:: resource_key
      :type: str


      Unique key for this resource requirement.

      .. autolink-examples:: resource_key
         :collapse:


   .. py:attribute:: resource_type
      :type:  Literal['tool', 'data', 'model', 'api', 'human']
      :value: None



.. py:class:: TaskStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of a task in the planning tree.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskStatus
      :collapse:

   .. py:attribute:: BLOCKED
      :value: 'blocked'



   .. py:attribute:: CANCELLED
      :value: 'cancelled'



   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: DEFERRED
      :value: 'deferred'



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: PENDING
      :value: 'pending'



