agents.planning.base.models
===========================

.. py:module:: agents.planning.base.models

.. autoapi-nested-parse::

   Planning Base Models - Advanced planning system with generics, indexing, and intelligent tree structures.

   This module provides a sophisticated planning framework with:
   - Maximum flexibility generics: Plan[Union[Step, Plan, Callable, str, Any]]
   - Intelligent tree traversal with cycle detection
   - Event-driven modifiable sequences with undo/redo
   - Auto-propagating status management
   - Smart field validation and auto-completion
   - Dynamic model adaptation based on content


   .. autolink-examples:: agents.planning.base.models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.base.models.PlanContent
   agents.planning.base.models.PlanType
   agents.planning.base.models.StepType
   agents.planning.base.models.T


Classes
-------

.. autoapisummary::

   agents.planning.base.models.BasePlan
   agents.planning.base.models.BaseStep
   agents.planning.base.models.ChangeEvent
   agents.planning.base.models.ConditionalPlan
   agents.planning.base.models.EventEmitter
   agents.planning.base.models.FlexiblePlan
   agents.planning.base.models.IntelligentSequence
   agents.planning.base.models.IntelligentStatusMixin
   agents.planning.base.models.ParallelPlan
   agents.planning.base.models.Priority
   agents.planning.base.models.SequentialPlan
   agents.planning.base.models.Task
   agents.planning.base.models.TaskStatus
   agents.planning.base.models.TraversalMode


Module Contents
---------------

.. py:class:: BasePlan(**data)

   Bases: :py:obj:`IntelligentStatusMixin`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Ultimate flexible plan supporting any content type with maximum intelligence.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BasePlan
      :collapse:

   .. py:method:: _calculate_max_depth() -> int

      Calculate maximum nesting depth.


      .. autolink-examples:: _calculate_max_depth
         :collapse:


   .. py:method:: _count_items_recursive(predicate: collections.abc.Callable[[Any], bool]) -> int

      Recursively count items matching predicate.


      .. autolink-examples:: _count_items_recursive
         :collapse:


   .. py:method:: _execute_conditional() -> dict[str, Any]
      :async:


      Execute with conditional logic.


      .. autolink-examples:: _execute_conditional
         :collapse:


   .. py:method:: _execute_flexible() -> dict[str, Any]
      :async:


      Execute using flexible strategy.


      .. autolink-examples:: _execute_flexible
         :collapse:


   .. py:method:: _execute_parallel() -> dict[str, Any]
      :async:


      Execute steps in parallel.


      .. autolink-examples:: _execute_parallel
         :collapse:


   .. py:method:: _execute_sequential() -> dict[str, Any]
      :async:


      Execute steps sequentially.


      .. autolink-examples:: _execute_sequential
         :collapse:


   .. py:method:: _is_executable_item(item: Any) -> bool

      Check if item is executable.


      .. autolink-examples:: _is_executable_item
         :collapse:


   .. py:method:: _is_item_ready(item: Any) -> bool

      Check if item is ready for execution.


      .. autolink-examples:: _is_item_ready
         :collapse:


   .. py:method:: _traverse_breadth_first() -> list[Any]

      Breadth-first traversal.


      .. autolink-examples:: _traverse_breadth_first
         :collapse:


   .. py:method:: _traverse_dependency_order() -> list[Any]

      Dependency-order traversal (topological sort).


      .. autolink-examples:: _traverse_dependency_order
         :collapse:


   .. py:method:: _traverse_depth_first() -> list[Any]

      Depth-first traversal.


      .. autolink-examples:: _traverse_depth_first
         :collapse:


   .. py:method:: _traverse_priority_first() -> list[Any]

      Priority-first traversal.


      .. autolink-examples:: _traverse_priority_first
         :collapse:


   .. py:method:: add_step(step: PlanContent) -> Self

      Add any type of content as a step.


      .. autolink-examples:: add_step
         :collapse:


   .. py:method:: add_steps(steps: list[PlanContent]) -> Self

      Add multiple steps.


      .. autolink-examples:: add_steps
         :collapse:


   .. py:method:: execute(mode: str = None) -> dict[str, Any]
      :async:


      Execute the plan using specified mode.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: find_by_id(item_id: str) -> Any | None

      Find any item by ID recursively.


      .. autolink-examples:: find_by_id
         :collapse:


   .. py:method:: find_by_predicate(predicate: collections.abc.Callable[[Any], bool]) -> list[Any]

      Find all items matching predicate.


      .. autolink-examples:: find_by_predicate
         :collapse:


   .. py:method:: get_statistics() -> dict[str, Any]

      Get comprehensive plan statistics.


      .. autolink-examples:: get_statistics
         :collapse:


   .. py:method:: traverse(mode: TraversalMode = TraversalMode.DEPTH_FIRST) -> list[Any]

      Traverse the plan tree using specified mode.


      .. autolink-examples:: traverse
         :collapse:


   .. py:attribute:: actual_duration
      :type:  str | None
      :value: None



   .. py:attribute:: assumptions
      :type:  list[str]
      :value: None



   .. py:property:: completed_items
      :type: int


      Count completed items recursively.

      .. autolink-examples:: completed_items
         :collapse:


   .. py:attribute:: complexity_level
      :type:  str
      :value: None



   .. py:property:: complexity_score
      :type: float


      Calculate overall plan complexity.

      .. autolink-examples:: complexity_score
         :collapse:


   .. py:attribute:: constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_total_duration
      :type:  str | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:property:: next_executable_items
      :type: list[BaseStep | BasePlan]


      Find all items ready for execution (supports parallel).

      .. autolink-examples:: next_executable_items
         :collapse:


   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: parallel_limit
      :type:  int | None
      :value: None



   .. py:attribute:: performance_targets
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: plan_type
      :type:  str
      :value: None



   .. py:property:: progress_percentage
      :type: float


      Intelligent progress calculation.

      .. autolink-examples:: progress_percentage
         :collapse:


   .. py:attribute:: quality_gates
      :type:  list[str]
      :value: None



   .. py:attribute:: steps
      :type:  IntelligentSequence[PlanContent]
      :value: None



   .. py:attribute:: success_criteria
      :type:  str
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



   .. py:property:: total_steps
      :type: int


      Recursively count all executable items.

      .. autolink-examples:: total_steps
         :collapse:


.. py:class:: BaseStep(**data)

   Bases: :py:obj:`IntelligentStatusMixin`


   Intelligent base step with adaptive behavior and smart validation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseStep
      :collapse:

   .. py:method:: add_feedback(feedback: str, quality_score: float | None = None) -> Self

      Add execution feedback.


      .. autolink-examples:: add_feedback
         :collapse:


   .. py:method:: execute() -> Any
      :async:


      Execute the step intelligently.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: actual_duration
      :type:  str | None
      :value: None



   .. py:attribute:: blocks
      :type:  list[str]
      :value: None



   .. py:property:: complexity_score
      :type: float


      Calculate complexity score based on various factors.

      .. autolink-examples:: complexity_score
         :collapse:


   .. py:attribute:: content
      :type:  str | collections.abc.Callable | dict[str, Any] | Any | None
      :value: None



   .. py:attribute:: depends_on
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: estimated_duration
      :type:  str | None
      :value: None



   .. py:attribute:: execution_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: expected_outcome
      :type:  str
      :value: None



   .. py:attribute:: feedback
      :type:  list[str]
      :value: None



   .. py:property:: is_executable
      :type: bool


      Intelligent executability check.

      .. autolink-examples:: is_executable
         :collapse:


   .. py:attribute:: priority
      :type:  Priority
      :value: None



   .. py:attribute:: quality_score
      :type:  float | None
      :value: None



   .. py:property:: readiness_score
      :type: float


      Calculate how ready this step is for execution.

      .. autolink-examples:: readiness_score
         :collapse:


   .. py:attribute:: resources_required
      :type:  list[str]
      :value: None



   .. py:attribute:: result
      :type:  Any | None
      :value: None



   .. py:attribute:: skills_required
      :type:  list[str]
      :value: None



   .. py:attribute:: soft_depends_on
      :type:  list[str]
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



   .. py:attribute:: tools_required
      :type:  list[str]
      :value: None



.. py:class:: ChangeEvent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Event representing a change in the planning structure.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChangeEvent
      :collapse:

   .. py:attribute:: event_type
      :type:  str


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: new_value
      :type:  Any
      :value: None



   .. py:attribute:: old_value
      :type:  Any
      :value: None



   .. py:attribute:: source_id
      :type:  str


   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: ConditionalPlan

   Bases: :py:obj:`BasePlan`\ [\ :py:obj:`Union`\ [\ :py:obj:`BaseStep`\ , :py:obj:`BasePlan`\ , :py:obj:`collections.abc.Callable`\ ]\ ]


   Conditional execution plan.


   .. autolink-examples:: ConditionalPlan
      :collapse:

   .. py:attribute:: conditions
      :type:  dict[str, collections.abc.Callable]
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: plan_type
      :type:  str
      :value: None



.. py:class:: EventEmitter

   Event system for tracking changes.


   .. autolink-examples:: EventEmitter
      :collapse:

   .. py:method:: emit(event: ChangeEvent)

      Emit an event.


      .. autolink-examples:: emit
         :collapse:


   .. py:method:: on(event_type: str, callback: collections.abc.Callable)

      Register event listener.


      .. autolink-examples:: on
         :collapse:


   .. py:attribute:: event_history
      :type:  list[ChangeEvent]
      :value: []



   .. py:attribute:: listeners
      :type:  dict[str, list[collections.abc.Callable]]


.. py:class:: FlexiblePlan

   Bases: :py:obj:`BasePlan`\ [\ :py:obj:`PlanContent`\ ]


   Maximum flexibility plan - can contain anything.


   .. autolink-examples:: FlexiblePlan
      :collapse:

   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: plan_type
      :type:  str
      :value: None



.. py:class:: IntelligentSequence(items: list[T] = None, parent: BasePlan | None = None)

   Bases: :py:obj:`list`\ [\ :py:obj:`PlanContent`\ ], :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Advanced modifiable sequence with event system, undo/redo, and cycle detection.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IntelligentSequence
      :collapse:

   .. py:method:: _contains_plan_recursive(plan: Any, target_id: str) -> bool

      Recursively check if plan contains target ID.


      .. autolink-examples:: _contains_plan_recursive
         :collapse:


   .. py:method:: _create_undo_action(operation: str, item: Any, index: int) -> collections.abc.Callable

      Create undo action for operation.


      .. autolink-examples:: _create_undo_action
         :collapse:


   .. py:method:: _emit_change(operation: str, item: Any = None, index: int = None) -> None

      Emit change event.


      .. autolink-examples:: _emit_change
         :collapse:


   .. py:method:: _raw_append(item: T) -> None

      Raw append without events or undo tracking.


      .. autolink-examples:: _raw_append
         :collapse:


   .. py:method:: _raw_insert(index: int, item: T) -> None

      Raw insert without events or undo tracking.


      .. autolink-examples:: _raw_insert
         :collapse:


   .. py:method:: _raw_pop(index: int = -1) -> T

      Raw pop without events or undo tracking.


      .. autolink-examples:: _raw_pop
         :collapse:


   .. py:method:: _raw_remove(item: T) -> None

      Raw remove without events or undo tracking.


      .. autolink-examples:: _raw_remove
         :collapse:


   .. py:method:: _reindex() -> None

      Intelligently reindex all items.


      .. autolink-examples:: _reindex
         :collapse:


   .. py:method:: _restore_state(state: list[T]) -> None

      Restore sequence to specific state.


      .. autolink-examples:: _restore_state
         :collapse:


   .. py:method:: _would_create_cycle(item: Any) -> bool

      Check if adding item would create a cycle.


      .. autolink-examples:: _would_create_cycle
         :collapse:


   .. py:method:: append(item: T) -> None

      Add item with undo support and events.


      .. autolink-examples:: append
         :collapse:


   .. py:method:: insert(index: int, item: T) -> None

      Insert item with undo support and events.


      .. autolink-examples:: insert
         :collapse:


   .. py:method:: pop(index: int = -1) -> T

      Pop item with undo support and events.


      .. autolink-examples:: pop
         :collapse:


   .. py:method:: redo() -> bool

      Redo last undone operation.


      .. autolink-examples:: redo
         :collapse:


   .. py:method:: remove(item: T) -> None

      Remove item with undo support and events.


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: undo() -> bool

      Undo last operation.


      .. autolink-examples:: undo
         :collapse:


   .. py:attribute:: _event_emitter


   .. py:attribute:: _modification_history
      :type:  list[ChangeEvent]
      :value: []



   .. py:attribute:: _redo_stack
      :type:  list[collections.abc.Callable]
      :value: []



   .. py:attribute:: _undo_stack
      :type:  list[collections.abc.Callable]
      :value: []



   .. py:attribute:: parent
      :value: None



.. py:class:: IntelligentStatusMixin(**data)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Advanced mixin with intelligent status management and auto-adaptation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: IntelligentStatusMixin
      :collapse:

   .. py:method:: _adapt_as_container() -> None

      Adapt to container behavior.


      .. autolink-examples:: _adapt_as_container
         :collapse:


   .. py:method:: _adapt_as_executable() -> None

      Adapt to executable behavior.


      .. autolink-examples:: _adapt_as_executable
         :collapse:


   .. py:method:: _adapt_model() -> None

      Dynamically adapt model based on content.


      .. autolink-examples:: _adapt_model
         :collapse:


   .. py:method:: _auto_complete_fields() -> None

      Intelligently auto-complete missing fields.


      .. autolink-examples:: _auto_complete_fields
         :collapse:


   .. py:method:: _auto_setup() -> None

      Intelligent auto-setup based on model content.


      .. autolink-examples:: _auto_setup
         :collapse:


   .. py:method:: _dependencies_met() -> bool

      Check if all dependencies are met.


      .. autolink-examples:: _dependencies_met
         :collapse:


   .. py:method:: _handle_status_change(event: ChangeEvent) -> None

      Handle status change events.


      .. autolink-examples:: _handle_status_change
         :collapse:


   .. py:method:: _setup_status_propagation() -> None

      Set up automatic status propagation.


      .. autolink-examples:: _setup_status_propagation
         :collapse:


   .. py:method:: _update_container_status() -> None

      Intelligently update container status based on children.


      .. autolink-examples:: _update_container_status
         :collapse:


   .. py:method:: update_status(new_status: TaskStatus, propagate: bool = True) -> Self

      Update status with intelligent propagation.


      .. autolink-examples:: update_status
         :collapse:


   .. py:attribute:: _children_refs
      :type:  set[str]
      :value: None



   .. py:attribute:: _event_emitter
      :type:  EventEmitter
      :value: None



   .. py:attribute:: _parent_ref
      :type:  IntelligentStatusMixin | None
      :value: None



   .. py:attribute:: adaptation_enabled
      :type:  bool
      :value: None



   .. py:attribute:: auto_field_completion
      :type:  bool
      :value: None



   .. py:attribute:: auto_status_propagation
      :type:  bool
      :value: None



   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: failed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: index
      :type:  int | None
      :value: None



   .. py:attribute:: started_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: status
      :type:  TaskStatus
      :value: None



   .. py:attribute:: updated_at
      :type:  datetime.datetime | None
      :value: None



.. py:class:: ParallelPlan

   Bases: :py:obj:`BasePlan`\ [\ :py:obj:`Union`\ [\ :py:obj:`BaseStep`\ , :py:obj:`BasePlan`\ ]\ ]


   Parallel execution plan.


   .. autolink-examples:: ParallelPlan
      :collapse:

   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: plan_type
      :type:  str
      :value: None



.. py:class:: Priority

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Priority levels with critical and emergency levels.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Priority
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: DEFERRED
      :value: 'deferred'



   .. py:attribute:: EMERGENCY
      :value: 'emergency'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



.. py:class:: SequentialPlan

   Bases: :py:obj:`BasePlan`\ [\ :py:obj:`Union`\ [\ :py:obj:`BaseStep`\ , :py:obj:`BasePlan`\ ]\ ]


   Sequential execution plan.


   .. autolink-examples:: SequentialPlan
      :collapse:

   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: plan_type
      :type:  str
      :value: None



.. py:class:: Task(**data)

   Bases: :py:obj:`IntelligentStatusMixin`


   Ultimate task model with maximum intelligence and flexibility.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Task
      :collapse:

   .. py:method:: activate_plan(plan: BasePlan) -> Self

      Intelligently activate a plan.


      .. autolink-examples:: activate_plan
         :collapse:


   .. py:method:: add_contingency(plan: BasePlan, trigger_condition: str) -> Self

      Add contingency plan with trigger condition.


      .. autolink-examples:: add_contingency
         :collapse:


   .. py:method:: execute() -> dict[str, Any]
      :async:


      Execute the primary plan intelligently.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: get_comprehensive_status() -> dict[str, Any]

      Get comprehensive status across all plans.


      .. autolink-examples:: get_comprehensive_status
         :collapse:


   .. py:attribute:: alternative_plans
      :type:  list[BasePlan]
      :value: None



   .. py:attribute:: assumptions
      :type:  list[str]
      :value: None



   .. py:attribute:: category
      :type:  str | None
      :value: None



   .. py:attribute:: complexity
      :type:  str
      :value: None



   .. py:attribute:: constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: contingency_plans
      :type:  list[BasePlan]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:property:: is_complete
      :type: bool


      Intelligent completion check.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:property:: overall_complexity
      :type: float


      Calculate overall task complexity.

      .. autolink-examples:: overall_complexity
         :collapse:


   .. py:property:: overall_progress
      :type: float


      Calculate progress across all active plans.

      .. autolink-examples:: overall_progress
         :collapse:


   .. py:attribute:: owner
      :type:  str | None
      :value: None



   .. py:attribute:: performance_metrics
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: primary_plan
      :type:  BasePlan | None
      :value: None



   .. py:attribute:: priority
      :type:  Priority
      :value: None



   .. py:attribute:: quality_targets
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: risks
      :type:  list[str]
      :value: None



   .. py:attribute:: stakeholders
      :type:  list[str]
      :value: None



   .. py:attribute:: success_criteria
      :type:  str
      :value: None



   .. py:attribute:: team
      :type:  list[str]
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



.. py:class:: TaskStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enhanced status enumeration with parallel execution support.

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



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: PARALLEL_RUNNING
      :value: 'parallel_running'



   .. py:attribute:: PAUSED
      :value: 'paused'



   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: READY
      :value: 'ready'



   .. py:attribute:: SKIPPED
      :value: 'skipped'



   .. py:attribute:: WAITING_FOR_DEPENDENCY
      :value: 'waiting_for_dependency'



.. py:class:: TraversalMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Tree traversal patterns.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TraversalMode
      :collapse:

   .. py:attribute:: BREADTH_FIRST
      :value: 'breadth_first'



   .. py:attribute:: DEPENDENCY_ORDER
      :value: 'dependency_order'



   .. py:attribute:: DEPTH_FIRST
      :value: 'depth_first'



   .. py:attribute:: PRIORITY_FIRST
      :value: 'priority_first'



.. py:data:: PlanContent

.. py:data:: PlanType

.. py:data:: StepType

.. py:data:: T

