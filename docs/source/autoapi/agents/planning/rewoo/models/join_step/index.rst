agents.planning.rewoo.models.join_step
======================================

.. py:module:: agents.planning.rewoo.models.join_step

.. autoapi-nested-parse::

   Join Step - Automatic DAG and Parallelization with Auto-detection.

   Inspired by haive.core.common.structures.tree, this implements a JoinStep that
   automatically detects parallel branches and creates join points for DAG execution.

   Similar to AutoTree's pattern of automatically detecting BaseModel relationships,
   JoinStep automatically detects step dependencies and creates optimal join points
   for parallel execution.


   .. autolink-examples:: agents.planning.rewoo.models.join_step
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo.models.join_step.JoinStep
   agents.planning.rewoo.models.join_step.JoinStrategy


Module Contents
---------------

.. py:class:: JoinStep(**data)

   Bases: :py:obj:`agents.planning.rewoo.models.steps.AbstractStep`


   A step that automatically creates join points for parallel execution.

   Like AutoTree automatically detects BaseModel relationships, JoinStep
   automatically detects dependency patterns and creates optimal join points.

   This enables automatic DAG creation where parallel branches are automatically
   detected and joined at the optimal points.


   .. autolink-examples:: JoinStep
      :collapse:

   .. py:method:: _auto_detect_parallel_structure()

      Auto-detect parallel structure like AutoTree detects BaseModel relationships.

      This method analyzes the dependency structure and automatically identifies:
      - Parallel input branches
      - Critical path dependencies
      - Optimal join strategies
      - Execution metadata


      .. autolink-examples:: _auto_detect_parallel_structure
         :collapse:


   .. py:method:: _calculate_dag_complexity(steps: list[agents.planning.rewoo.models.steps.AbstractStep]) -> str
      :classmethod:


      Calculate overall DAG complexity.


      .. autolink-examples:: _calculate_dag_complexity
         :collapse:


   .. py:method:: _calculate_dependency_depth(step_map: dict[str, agents.planning.rewoo.models.steps.AbstractStep]) -> int

      Calculate maximum dependency depth for this step.


      .. autolink-examples:: _calculate_dependency_depth
         :collapse:


   .. py:method:: _calculate_parallelization_score(steps: list[agents.planning.rewoo.models.steps.AbstractStep]) -> float
      :classmethod:


      Calculate potential parallelization benefit (0.0 to 1.0).


      .. autolink-examples:: _calculate_parallelization_score
         :collapse:


   .. py:method:: _detect_parallel_opportunities(step_map: dict[str, agents.planning.rewoo.models.steps.AbstractStep]) -> list[dict[str, Any]]

      Detect opportunities for parallel execution.


      .. autolink-examples:: _detect_parallel_opportunities
         :collapse:


   .. py:method:: _estimate_parallelization_benefit() -> float

      Estimate benefit of parallelization (0.0 to 1.0).


      .. autolink-examples:: _estimate_parallelization_benefit
         :collapse:


   .. py:method:: _generate_optimization_hints() -> dict[str, Any]

      Generate optimization hints based on detected structure.


      .. autolink-examples:: _generate_optimization_hints
         :collapse:


   .. py:method:: _has_dependency_path(from_step: agents.planning.rewoo.models.steps.AbstractStep, to_step: agents.planning.rewoo.models.steps.AbstractStep, step_map: dict[str, agents.planning.rewoo.models.steps.AbstractStep]) -> bool

      Check if there's a dependency path from one step to another.


      .. autolink-examples:: _has_dependency_path
         :collapse:


   .. py:method:: _identify_critical_path_members(step_map: dict[str, agents.planning.rewoo.models.steps.AbstractStep]) -> list[str]

      Identify which dependencies are on the critical path.


      .. autolink-examples:: _identify_critical_path_members
         :collapse:


   .. py:method:: _merge_multiple_results() -> Any

      Merge multiple results efficiently.


      .. autolink-examples:: _merge_multiple_results
         :collapse:


   .. py:method:: _merge_two_results() -> Any

      Merge exactly two results.


      .. autolink-examples:: _merge_two_results
         :collapse:


   .. py:method:: _reduce_complex_results() -> Any

      Reduce complex parallel results.


      .. autolink-examples:: _reduce_complex_results
         :collapse:


   .. py:method:: _suggest_dag_optimizations(step_map: dict[str, agents.planning.rewoo.models.steps.AbstractStep]) -> list[dict[str, Any]]

      Suggest DAG-level optimizations.


      .. autolink-examples:: _suggest_dag_optimizations
         :collapse:


   .. py:method:: _suggest_join_function() -> str

      Suggest appropriate join function based on structure.


      .. autolink-examples:: _suggest_join_function
         :collapse:


   .. py:method:: _suggest_optimal_strategy() -> JoinStrategy

      Suggest optimal join strategy based on structure.


      .. autolink-examples:: _suggest_optimal_strategy
         :collapse:


   .. py:method:: analyze_dag_structure(steps: list[agents.planning.rewoo.models.steps.AbstractStep]) -> dict[str, Any]
      :classmethod:


      Analyze entire DAG structure and suggest join optimizations.

      Like AutoTree's tree analysis, this provides DAG-wide analysis.


      .. autolink-examples:: analyze_dag_structure
         :collapse:


   .. py:method:: analyze_dependency_patterns(all_steps: list[agents.planning.rewoo.models.steps.AbstractStep]) -> dict[str, Any]

      Analyze dependency patterns across all steps to detect DAG structure.

      Similar to how AutoTree analyzes type relationships, this analyzes
      step dependency relationships to detect optimal parallelization.


      .. autolink-examples:: analyze_dependency_patterns
         :collapse:


   .. py:method:: can_execute(completed_steps: set[str]) -> bool

      Check if this join step can execute based on strategy.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: create_auto_join(description: str, dependencies: list[str], strategy: JoinStrategy = JoinStrategy.WAIT_ALL, **kwargs) -> JoinStep
      :classmethod:


      Factory method to create a JoinStep with automatic detection.


      .. autolink-examples:: create_auto_join
         :collapse:


   .. py:method:: execute(context: dict[str, Any]) -> Any

      Execute the join operation.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: get_join_info() -> dict[str, Any]

      Get comprehensive information about this join step.


      .. autolink-examples:: get_join_info
         :collapse:


   .. py:property:: can_optimize_parallel
      :type: bool


      Whether this join can be optimized for parallel execution.

      .. autolink-examples:: can_optimize_parallel
         :collapse:


   .. py:property:: estimated_wait_time
      :type: float


      Estimated wait time based on join strategy and branch count.

      .. autolink-examples:: estimated_wait_time
         :collapse:


   .. py:property:: is_join_point
      :type: bool


      Whether this step is a join point (has multiple dependencies).

      .. autolink-examples:: is_join_point
         :collapse:


   .. py:property:: join_complexity
      :type: str


      Complexity classification of the join operation.

      .. autolink-examples:: join_complexity
         :collapse:


   .. py:attribute:: join_function
      :type:  str | None
      :value: None



   .. py:attribute:: join_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: join_strategy
      :type:  JoinStrategy
      :value: None



   .. py:property:: parallel_branch_count
      :type: int


      Number of parallel branches this step joins.

      .. autolink-examples:: parallel_branch_count
         :collapse:


   .. py:attribute:: parallel_inputs
      :type:  list[str]
      :value: None



   .. py:attribute:: parallel_results
      :type:  dict[str, Any]
      :value: None



.. py:class:: JoinStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Strategies for joining parallel branches.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: JoinStrategy
      :collapse:

   .. py:attribute:: WAIT_ALL
      :value: 'wait_all'



   .. py:attribute:: WAIT_ANY
      :value: 'wait_any'



   .. py:attribute:: WAIT_CRITICAL
      :value: 'wait_critical'



   .. py:attribute:: WAIT_MAJORITY
      :value: 'wait_majority'



