agents.task_analysis.base.models
================================

.. py:module:: agents.task_analysis.base.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.base.models.ActionStep
   agents.task_analysis.base.models.ActionType
   agents.task_analysis.base.models.DependencyType
   agents.task_analysis.base.models.TaskDependency
   agents.task_analysis.base.models.TaskNode
   agents.task_analysis.base.models.TaskPlan
   agents.task_analysis.base.models.TaskType


Module Contents
---------------

.. py:class:: ActionStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Atomic action that cannot be decomposed further.
   This is a leaf node in the task tree.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionStep
      :collapse:

   .. py:attribute:: action_type
      :type:  ActionType
      :value: None



   .. py:attribute:: can_parallelize
      :type:  bool
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: inputs
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: is_critical
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: outputs
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: required_context
      :type:  list[str]
      :value: None



   .. py:attribute:: required_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: success_criteria
      :type:  list[str]
      :value: None



.. py:class:: ActionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of atomic actions.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionType
      :collapse:

   .. py:attribute:: AGGREGATE
      :value: 'aggregate'



   .. py:attribute:: COMPUTE
      :value: 'compute'



   .. py:attribute:: GENERATE
      :value: 'generate'



   .. py:attribute:: RETRIEVE
      :value: 'retrieve'



   .. py:attribute:: STORE
      :value: 'store'



   .. py:attribute:: TRANSFORM
      :value: 'transform'



   .. py:attribute:: VALIDATE
      :value: 'validate'



.. py:class:: DependencyType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of dependencies between tasks.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DependencyType
      :collapse:

   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: JOIN
      :value: 'join'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



.. py:class:: TaskDependency(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Dependency between tasks.

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



   .. py:attribute:: data_flow
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: dependency_type
      :type:  DependencyType
      :value: None



   .. py:attribute:: source_id
      :type:  str
      :value: None



   .. py:attribute:: target_id
      :type:  str
      :value: None



.. py:class:: TaskNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A task that may contain subtasks or action steps.
   Designed to work perfectly with AutoTree.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskNode
      :collapse:

   .. py:method:: add_dependency(source_id: str, target_id: str, dep_type: DependencyType = DependencyType.SEQUENTIAL) -> None

      Add a dependency between child tasks.


      .. autolink-examples:: add_dependency
         :collapse:


   .. py:method:: add_subtask(subtask: Union[TaskNode, ActionStep]) -> None

      Add a subtask and assign dependencies if needed.


      .. autolink-examples:: add_subtask
         :collapse:


   .. py:method:: calculate_total_duration() -> float

      Calculate total duration including subtasks.


      .. autolink-examples:: calculate_total_duration
         :collapse:


   .. py:method:: get_all_steps() -> list[ActionStep]

      Get all ActionSteps in this task tree.


      .. autolink-examples:: get_all_steps
         :collapse:


   .. py:attribute:: can_expand
      :type:  bool
      :value: None



   .. py:attribute:: can_parallelize
      :type:  bool
      :value: None



   .. py:attribute:: complexity_score
      :type:  float
      :value: None



   .. py:attribute:: dependencies
      :type:  list[TaskDependency]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float | None
      :value: None



   .. py:attribute:: expansion_hints
      :type:  str | None
      :value: None



   .. py:attribute:: is_join_point
      :type:  bool
      :value: None



   .. py:attribute:: join_strategy
      :type:  str | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: required_capabilities
      :type:  list[str]
      :value: None



   .. py:attribute:: required_resources
      :type:  list[str]
      :value: None



   .. py:attribute:: subtasks
      :type:  list[Union[TaskNode, ActionStep]]
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



   .. py:attribute:: task_type
      :type:  TaskType
      :value: None



.. py:class:: TaskPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Root object representing a complete task plan.
   This is what we'll create from a task description.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskPlan
      :collapse:

   .. py:method:: _calculate_max_depth(tree) -> int

      Calculate maximum depth of the tree.


      .. autolink-examples:: _calculate_max_depth
         :collapse:


   .. py:method:: calculate_stats() -> None

      Calculate plan statistics.


      .. autolink-examples:: calculate_stats
         :collapse:


   .. py:attribute:: complexity_analysis
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: created_at
      :type:  str
      :value: None



   .. py:attribute:: execution_plan
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: max_depth
      :type:  int | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: original_request
      :type:  str
      :value: None



   .. py:attribute:: parallelization_analysis
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: root_task
      :type:  TaskNode
      :value: None



   .. py:attribute:: total_estimated_duration_minutes
      :type:  float | None
      :value: None



   .. py:attribute:: total_tasks
      :type:  int | None
      :value: None



.. py:class:: TaskType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Type of task - affects how it's processed.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskType
      :collapse:

   .. py:attribute:: ACTION
      :value: 'action'



   .. py:attribute:: ANALYSIS
      :value: 'analysis'



   .. py:attribute:: COMPOSITE
      :value: 'composite'



   .. py:attribute:: CREATIVE
      :value: 'creative'



   .. py:attribute:: DECISION
      :value: 'decision'



   .. py:attribute:: INTEGRATION
      :value: 'integration'



   .. py:attribute:: RESEARCH
      :value: 'research'



