agents.planning_v2.base.tree_models
===================================

.. py:module:: agents.planning_v2.base.tree_models

.. autoapi-nested-parse::

   Tree-based planning models using the enhanced tree_leaf structure.

   This module provides planning models that leverage the generic tree/leaf
   structure from haive-core for more flexible and type-safe planning.


   .. autolink-examples:: agents.planning_v2.base.tree_models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning_v2.base.tree_models.PlanLeaf
   agents.planning_v2.base.tree_models.PlanTree
   agents.planning_v2.base.tree_models.SimplePlanTree


Classes
-------

.. autoapisummary::

   agents.planning_v2.base.tree_models.PlanContent
   agents.planning_v2.base.tree_models.PlanResult
   agents.planning_v2.base.tree_models.PlanStatus
   agents.planning_v2.base.tree_models.TaskPlan


Functions
---------

.. autoapisummary::

   agents.planning_v2.base.tree_models.create_phased_plan
   agents.planning_v2.base.tree_models.create_simple_plan


Module Contents
---------------

.. py:class:: PlanContent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Content for plan nodes (both tasks and sub-plans).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanContent
      :collapse:

   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: status
      :type:  PlanStatus
      :value: None



.. py:class:: PlanResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of executing a plan node.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanResult
      :collapse:

   .. py:attribute:: artifacts
      :type:  dict
      :value: None



   .. py:attribute:: duration_seconds
      :type:  float | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: output
      :type:  str | None
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



.. py:class:: PlanStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status for plan nodes.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanStatus
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



.. py:class:: TaskPlan

   Bases: :py:obj:`PlanTree`


   A concrete plan implementation using the tree structure.

   This class extends the generic Tree to provide planning-specific
   functionality while maintaining type safety.

   .. rubric:: Example

   ```python
   # Create a plan
   plan = TaskPlan(content=PlanContent(
       objective="Deploy new feature",
       priority=4
   ))

   # Add simple tasks
   plan.add_task("Write tests", priority=5)
   plan.add_task("Code review", priority=3)

   # Add sub-plan
   deploy_plan = plan.add_subplan("Deploy to production")
   deploy_plan.add_task("Deploy to staging")
   deploy_plan.add_task("Run smoke tests")
   deploy_plan.add_task("Deploy to prod")

   # Check status
   print(f"Total tasks: {plan.total_nodes}")
   print(f"Progress: {plan.progress_percentage}%")
   ```


   .. autolink-examples:: TaskPlan
      :collapse:

   .. py:method:: add_parallel_tasks(tasks: list[tuple[str, int]]) -> list[PlanLeaf]

      Add multiple tasks that can execute in parallel.

      :param tasks: List of (objective, priority) tuples

      :returns: List of created task nodes


      .. autolink-examples:: add_parallel_tasks
         :collapse:


   .. py:method:: add_subplan(objective: str, description: str = '', priority: int = 1) -> TaskPlan

      Add a sub-plan that can contain its own tasks.


      .. autolink-examples:: add_subplan
         :collapse:


   .. py:method:: add_task(objective: str, description: str = '', priority: int = 1) -> PlanLeaf

      Add a simple task to the plan.


      .. autolink-examples:: add_task
         :collapse:


   .. py:method:: get_blocked_tasks() -> list[Union[PlanLeaf, TaskPlan]]

      Get all tasks that are blocked.


      .. autolink-examples:: get_blocked_tasks
         :collapse:


   .. py:method:: get_current_task() -> Union[PlanLeaf, TaskPlan] | None

      Get the current task to execute (first pending or in-progress).


      .. autolink-examples:: get_current_task
         :collapse:


   .. py:method:: get_tasks_by_priority(min_priority: int = 1) -> list[Union[PlanLeaf, TaskPlan]]

      Get all tasks with priority >= min_priority.


      .. autolink-examples:: get_tasks_by_priority
         :collapse:


   .. py:method:: mark_current_completed(output: str = 'Done') -> bool

      Mark the current active task as completed.


      .. autolink-examples:: mark_current_completed
         :collapse:


   .. py:method:: mark_current_failed(error: str) -> bool

      Mark the current active task as failed.


      .. autolink-examples:: mark_current_failed
         :collapse:


   .. py:method:: to_markdown(indent: int = 0) -> str

      Convert plan to markdown representation.


      .. autolink-examples:: to_markdown
         :collapse:


.. py:function:: create_phased_plan(objective: str, phases: dict[str, list[str]]) -> TaskPlan

   Create a plan with phases (sub-plans).

   :param objective: Main plan objective
   :param phases: Dict of phase_name -> list of tasks

   .. rubric:: Example

   plan = create_phased_plan(
       "Launch Product",
       {
           "Development": ["Code", "Test", "Review"],
           "Deployment": ["Stage", "Verify", "Prod"],
           "Marketing": ["Announce", "Demo", "Feedback"]
       }
   )


   .. autolink-examples:: create_phased_plan
      :collapse:

.. py:function:: create_simple_plan(objective: str, tasks: list[str]) -> TaskPlan

   Create a simple linear plan from a list of task names.


   .. autolink-examples:: create_simple_plan
      :collapse:

.. py:data:: PlanLeaf

.. py:data:: PlanTree

.. py:data:: SimplePlanTree

