agents.task_analysis.tree.models
================================

.. py:module:: agents.task_analysis.tree.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.tree.models.TaskTree


Module Contents
---------------

.. py:class:: TaskTree(content: haive.agents.task_analysis.base.models.TaskNode, **kwargs)

   Bases: :py:obj:`haive.core.common.structures.tree.AutoTree`\ [\ :py:obj:`haive.agents.task_analysis.base.models.TaskNode`\ ]


   Enhanced AutoTree specifically for task analysis.
   Adds task-specific functionality while leveraging AutoTree's auto-building.


   .. autolink-examples:: TaskTree
      :collapse:

   .. py:method:: _analyze_structure()

      Analyze task structure after tree is built.


      .. autolink-examples:: _analyze_structure
         :collapse:


   .. py:method:: _build_dependency_map() -> dict[str, list[str]]

      Build a map of dependencies.


      .. autolink-examples:: _build_dependency_map
         :collapse:


   .. py:method:: _calculate_critical_path()

      Calculate the critical path through the task tree.


      .. autolink-examples:: _calculate_critical_path
         :collapse:


   .. py:method:: _calculate_max_depth(current_depth: int) -> int

      Calculate maximum depth from this node.


      .. autolink-examples:: _calculate_max_depth
         :collapse:


   .. py:method:: _find_incoming_tasks(task_id: str) -> list[str]

      Find all tasks that have dependencies pointing to this task.


      .. autolink-examples:: _find_incoming_tasks
         :collapse:


   .. py:method:: _get_all_task_ids() -> list[str]

      Get all task and step IDs.


      .. autolink-examples:: _get_all_task_ids
         :collapse:


   .. py:method:: _get_subtask_duration(subtask: haive.agents.task_analysis.base.models.TaskNode | haive.agents.task_analysis.base.models.ActionStep) -> float

      Get duration of a subtask.


      .. autolink-examples:: _get_subtask_duration
         :collapse:


   .. py:method:: _has_path_between(id1: str, id2: str, dep_map: dict[str, list[str]]) -> bool

      Check if there's a dependency path between two tasks.


      .. autolink-examples:: _has_path_between
         :collapse:


   .. py:method:: _identify_join_points()

      Find all join points in the task tree.


      .. autolink-examples:: _identify_join_points
         :collapse:


   .. py:method:: _identify_parallel_groups()

      Identify groups of tasks that can run in parallel.


      .. autolink-examples:: _identify_parallel_groups
         :collapse:


   .. py:method:: expand_node(node_id: str, expansion_fn: collections.abc.Callable[[haive.agents.task_analysis.base.models.TaskNode], list[haive.agents.task_analysis.base.models.TaskNode | haive.agents.task_analysis.base.models.ActionStep]]) -> bool

      Expand a specific node using the provided expansion function.
      Returns True if expansion was successful.


      .. autolink-examples:: expand_node
         :collapse:


   .. py:method:: get_analysis_summary() -> dict[str, Any]

      Get a summary of the task tree analysis.


      .. autolink-examples:: get_analysis_summary
         :collapse:


   .. py:method:: get_critical_path() -> list[str]

      Get the critical path.


      .. autolink-examples:: get_critical_path
         :collapse:


   .. py:method:: get_execution_phases() -> list[dict[str, Any]]

      Organize tasks into execution phases.
      Tasks in the same phase can run in parallel.


      .. autolink-examples:: get_execution_phases
         :collapse:


   .. py:method:: get_join_points() -> list[dict[str, Any]]

      Get all join points in the tree.


      .. autolink-examples:: get_join_points
         :collapse:


   .. py:method:: get_parallel_groups() -> list[list[str]]

      Get groups of tasks that can run in parallel.


      .. autolink-examples:: get_parallel_groups
         :collapse:


   .. py:attribute:: _critical_path
      :type:  list[str]
      :value: []



   .. py:attribute:: _join_points
      :type:  list[dict[str, Any]]
      :value: []



   .. py:attribute:: _parallel_groups
      :type:  list[list[str]]
      :value: []



