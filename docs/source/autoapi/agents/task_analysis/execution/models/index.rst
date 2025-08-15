agents.task_analysis.execution.models
=====================================

.. py:module:: agents.task_analysis.execution.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.execution.models.ExecutionPhase
   agents.task_analysis.execution.models.ExecutionPlan
   agents.task_analysis.execution.models.JoinPoint
   agents.task_analysis.execution.models.ResourceAllocation
   agents.task_analysis.execution.models.ResourceType


Module Contents
---------------

.. py:class:: ExecutionPhase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A phase in the execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPhase
      :collapse:

   .. py:method:: add_task(task_id: str, group_index: int | None = None)

      Add a task to this phase.


      .. autolink-examples:: add_task
         :collapse:


   .. py:attribute:: can_start_early
      :type:  bool
      :value: None



   .. py:attribute:: completion_criteria
      :type:  list[str]
      :value: None



   .. py:attribute:: depends_on_phases
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: earliest_start_minutes
      :type:  float | None
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parallel_groups
      :type:  list[list[str]]
      :value: None



   .. py:attribute:: phase_id
      :type:  str
      :value: None



   .. py:attribute:: phase_number
      :type:  int
      :value: None



   .. py:attribute:: required_resources
      :type:  dict[ResourceType, float]
      :value: None



   .. py:attribute:: task_ids
      :type:  list[str]
      :value: None



.. py:class:: ExecutionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete execution plan for a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPlan
      :collapse:

   .. py:method:: add_phase(phase: ExecutionPhase)

      Add a phase to the plan.


      .. autolink-examples:: add_phase
         :collapse:


   .. py:method:: calculate_critical_path() -> list[str]

      Calculate and return the critical path.


      .. autolink-examples:: calculate_critical_path
         :collapse:


   .. py:method:: get_phase_by_task(task_id: str) -> ExecutionPhase | None

      Find which phase contains a task.


      .. autolink-examples:: get_phase_by_task
         :collapse:


   .. py:attribute:: bottlenecks
      :type:  list[str]
      :value: None



   .. py:attribute:: can_checkpoint
      :type:  bool
      :value: None



   .. py:attribute:: checkpoint_phases
      :type:  list[str]
      :value: None



   .. py:attribute:: critical_path_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: critical_path_task_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: join_points
      :type:  list[JoinPoint]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: optimization_opportunities
      :type:  list[str]
      :value: None



   .. py:attribute:: parallel_efficiency
      :type:  float
      :value: None



   .. py:attribute:: peak_resource_usage
      :type:  dict[ResourceType, float]
      :value: None



   .. py:attribute:: phase_dependencies
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: phases
      :type:  list[ExecutionPhase]
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: resource_timeline
      :type:  list[ResourceAllocation]
      :value: None



   .. py:attribute:: total_duration_minutes
      :type:  float
      :value: None



.. py:class:: JoinPoint(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents where parallel execution paths converge.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: JoinPoint
      :collapse:

   .. py:attribute:: custom_logic
      :type:  str | None
      :value: None



   .. py:attribute:: fallback_strategy
      :type:  str | None
      :value: None



   .. py:attribute:: input_task_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: join_function
      :type:  str
      :value: None



   .. py:attribute:: join_id
      :type:  str
      :value: None



   .. py:attribute:: join_type
      :type:  Literal['aggregate', 'merge', 'select', 'custom']
      :value: None



   .. py:attribute:: on_partial_failure
      :type:  Literal['fail', 'continue', 'retry']
      :value: None



   .. py:attribute:: output_task_id
      :type:  str
      :value: None



   .. py:attribute:: timeout_minutes
      :type:  float | None
      :value: None



   .. py:attribute:: wait_for_all
      :type:  bool
      :value: None



.. py:class:: ResourceAllocation(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Resource allocation over time.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResourceAllocation
      :collapse:

   .. py:attribute:: amount
      :type:  float


   .. py:attribute:: availability
      :type:  float | None
      :value: None



   .. py:attribute:: cost_per_unit
      :type:  float | None
      :value: None



   .. py:attribute:: duration_minutes
      :type:  float


   .. py:attribute:: phase_id
      :type:  str


   .. py:attribute:: resource_type
      :type:  ResourceType


   .. py:attribute:: start_time_minutes
      :type:  float


.. py:class:: ResourceType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of resources needed for execution.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResourceType
      :collapse:

   .. py:attribute:: API
      :value: 'api'



   .. py:attribute:: COMPUTE
      :value: 'compute'



   .. py:attribute:: DATA
      :value: 'data'



   .. py:attribute:: HUMAN
      :value: 'human'



   .. py:attribute:: NETWORK
      :value: 'network'



   .. py:attribute:: STORAGE
      :value: 'storage'



   .. py:attribute:: TOOL
      :value: 'tool'



