models.task_analysis.parallelization
====================================

.. py:module:: models.task_analysis.parallelization

.. autoapi-nested-parse::

   Parallelization analysis for task execution planning.

   This module analyzes task dependencies to identify parallelization opportunities,
   execution phases, join points, and optimal execution strategies.


   .. autolink-examples:: models.task_analysis.parallelization
      :collapse:


Classes
-------

.. autoapisummary::

   models.task_analysis.parallelization.ExecutionPhase
   models.task_analysis.parallelization.ExecutionStrategy
   models.task_analysis.parallelization.JoinPoint
   models.task_analysis.parallelization.ParallelGroup
   models.task_analysis.parallelization.ParallelizationAnalysis
   models.task_analysis.parallelization.ParallelizationAnalyzer


Module Contents
---------------

.. py:class:: ExecutionPhase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a phase in the overall task execution plan.

   Execution phases organize the task execution into sequential stages,
   where each phase must complete before the next phase can begin.

   .. attribute:: phase_number

      Sequential phase number

   .. attribute:: name

      Descriptive name for this phase

   .. attribute:: parallel_groups

      Groups of tasks that can run in parallel within this phase

   .. attribute:: dependencies

      What this phase depends on

   .. attribute:: estimated_duration_minutes

      Total time for this phase

   .. attribute:: critical_path_tasks

      Tasks on the critical path within this phase

   .. rubric:: Example

   .. code-block:: python

       phase = ExecutionPhase(
       phase_number=1,
       name="Data Collection Phase",
       parallel_groups=[research_group, survey_group],
       estimated_duration_minutes=180
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPhase
      :collapse:

   .. py:method:: calculate_sequential_duration() -> float

      Calculate duration if all tasks ran sequentially.

      :returns: Sequential execution duration in minutes


      .. autolink-examples:: calculate_sequential_duration
         :collapse:


   .. py:method:: get_max_parallelism() -> int

      Get maximum number of tasks that can run simultaneously.

      :returns: Maximum parallelism level


      .. autolink-examples:: get_max_parallelism
         :collapse:


   .. py:method:: get_parallelization_benefit() -> float

      Calculate benefit from parallelization as a ratio.

      :returns: Parallelization benefit (sequential_time / parallel_time)


      .. autolink-examples:: get_parallelization_benefit
         :collapse:


   .. py:method:: get_total_task_count() -> int

      Get total number of tasks across all parallel groups.

      :returns: Total task count


      .. autolink-examples:: get_total_task_count
         :collapse:


   .. py:attribute:: can_start_early
      :type:  bool
      :value: None



   .. py:attribute:: critical_path_tasks
      :type:  list[str]
      :value: None



   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parallel_groups
      :type:  list[ParallelGroup]
      :value: None



   .. py:attribute:: phase_number
      :type:  int
      :value: None



   .. py:attribute:: resource_utilization
      :type:  dict[str, float]
      :value: None



.. py:class:: ExecutionStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Strategies for executing parallel tasks.

   .. attribute:: SEQUENTIAL

      Execute all tasks one after another

   .. attribute:: MAX_PARALLEL

      Execute as many tasks in parallel as possible

   .. attribute:: RESOURCE_CONSTRAINED

      Parallel execution limited by resource availability

   .. attribute:: PRIORITY_BASED

      Execute high-priority tasks first, parallelize when possible

   .. attribute:: BALANCED

      Balance between parallelization and resource usage

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionStrategy
      :collapse:

   .. py:attribute:: BALANCED
      :value: 'balanced'



   .. py:attribute:: MAX_PARALLEL
      :value: 'max_parallel'



   .. py:attribute:: PRIORITY_BASED
      :value: 'priority_based'



   .. py:attribute:: RESOURCE_CONSTRAINED
      :value: 'resource_constrained'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



.. py:class:: JoinPoint(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a point where multiple parallel tasks must synchronize.

   Join points are critical for understanding where parallel execution
   must wait for all dependencies to complete before proceeding.

   .. attribute:: id

      Unique identifier for this join point

   .. attribute:: name

      Descriptive name for the join point

   .. attribute:: input_task_ids

      IDs of tasks that must complete before this join

   .. attribute:: output_task_ids

      IDs of tasks that can start after this join

   .. attribute:: join_type

      Type of join operation

   .. attribute:: estimated_wait_time

      Expected time to wait for all inputs

   .. attribute:: is_critical_path

      Whether this join point is on the critical path

   .. rubric:: Example

   .. code-block:: python

       join_point = JoinPoint(
       id="analysis_join",
       name="Combine Analysis Results",
       input_task_ids=["data_collection", "background_research"],
       output_task_ids=["final_report"],
       join_type="synchronous"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: JoinPoint
      :collapse:

   .. py:method:: get_input_count() -> int

      Get the number of input tasks for this join point.

      :returns: Number of input tasks


      .. autolink-examples:: get_input_count
         :collapse:


   .. py:method:: get_output_count() -> int

      Get the number of output tasks from this join point.

      :returns: Number of output tasks


      .. autolink-examples:: get_output_count
         :collapse:


   .. py:method:: is_merge_point() -> bool

      Check if this is a merge point (multiple inputs, single output).

      :returns: True if multiple inputs merge to single output


      .. autolink-examples:: is_merge_point
         :collapse:


   .. py:method:: is_split_point() -> bool

      Check if this is a split point (single input, multiple outputs).

      :returns: True if single input splits to multiple outputs


      .. autolink-examples:: is_split_point
         :collapse:


   .. py:attribute:: bottleneck_probability
      :type:  float
      :value: None



   .. py:attribute:: estimated_wait_time_minutes
      :type:  float
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: input_task_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: is_critical_path
      :type:  bool
      :value: None



   .. py:attribute:: join_type
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_task_ids
      :type:  list[str]
      :value: None



.. py:class:: ParallelGroup(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a group of tasks that can execute in parallel.

   Parallel groups identify sets of tasks that have no blocking
   dependencies between them and can therefore run simultaneously.

   .. attribute:: group_id

      Unique identifier for this parallel group

   .. attribute:: task_ids

      IDs of tasks in this parallel group

   .. attribute:: estimated_duration_minutes

      Time for the longest task in the group

   .. attribute:: resource_requirements

      Combined resource requirements

   .. attribute:: can_be_interleaved

      Whether tasks can be interleaved or must run fully parallel

   .. attribute:: priority

      Priority level for this group

   .. attribute:: phase

      Execution phase this group belongs to

   .. rubric:: Example

   .. code-block:: python

       parallel_group = ParallelGroup(
       group_id="research_phase",
       task_ids=["web_research", "library_research", "expert_interviews"],
       estimated_duration_minutes=120,
       resource_requirements={"researchers": 3, "internet": True}
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelGroup
      :collapse:

   .. py:method:: calculate_actual_duration(sequential_duration: float) -> float

      Calculate actual duration considering parallelization.

      :param sequential_duration: Duration if tasks ran sequentially

      :returns: Actual duration with parallelization


      .. autolink-examples:: calculate_actual_duration
         :collapse:


   .. py:method:: get_task_count() -> int

      Get the number of tasks in this parallel group.

      :returns: Number of tasks in the group


      .. autolink-examples:: get_task_count
         :collapse:


   .. py:method:: get_theoretical_speedup() -> float

      Calculate theoretical speedup from parallelization.

      :returns: Theoretical speedup factor


      .. autolink-examples:: get_theoretical_speedup
         :collapse:


   .. py:attribute:: can_be_interleaved
      :type:  bool
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: group_id
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: parallelization_efficiency
      :type:  float
      :value: None



   .. py:attribute:: phase
      :type:  int
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: resource_requirements
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: task_ids
      :type:  list[str]
      :value: None



.. py:class:: ParallelizationAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete analysis of parallelization opportunities for a task.

   This is the main result of parallelization analysis, containing
   all the information needed to optimize task execution.

   .. attribute:: execution_phases

      Sequential phases of execution

   .. attribute:: parallel_groups

      All identified parallel groups

   .. attribute:: join_points

      Critical synchronization points

   .. attribute:: critical_path

      Tasks on the critical path

   .. attribute:: execution_strategy

      Recommended execution strategy

   .. attribute:: estimated_speedup

      Expected speedup from parallelization

   .. attribute:: resource_requirements

      Peak resource requirements

   .. attribute:: bottlenecks

      Identified bottlenecks and constraints

   .. rubric:: Example

   .. code-block:: python

       analysis = ParallelizationAnalysis(
       execution_phases=[phase1, phase2, phase3],
       parallel_groups=[group1, group2],
       join_points=[join1, join2],
       critical_path=["task_1", "task_3", "task_5"],
       estimated_speedup=2.5
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelizationAnalysis
      :collapse:

   .. py:method:: calculate_time_savings() -> float

      Calculate time savings from parallelization.

      :returns: Time savings in minutes


      .. autolink-examples:: calculate_time_savings
         :collapse:


   .. py:method:: get_critical_path_duration() -> float

      Get duration of the critical path.

      :returns: Critical path duration in minutes


      .. autolink-examples:: get_critical_path_duration
         :collapse:


   .. py:method:: get_efficiency_percentage() -> float

      Get parallelization efficiency as a percentage.

      :returns: Efficiency percentage (0-100)


      .. autolink-examples:: get_efficiency_percentage
         :collapse:


   .. py:method:: get_max_parallelism() -> int

      Get maximum parallelism across all phases.

      :returns: Maximum number of tasks that can run simultaneously


      .. autolink-examples:: get_max_parallelism
         :collapse:


   .. py:method:: get_total_phases() -> int

      Get total number of execution phases.

      :returns: Number of phases


      .. autolink-examples:: get_total_phases
         :collapse:


   .. py:method:: is_worth_parallelizing(min_speedup: float = 1.2) -> bool

      Determine if parallelization is worthwhile.

      :param min_speedup: Minimum speedup required to justify parallelization

      :returns: True if parallelization provides sufficient benefit


      .. autolink-examples:: is_worth_parallelizing
         :collapse:


   .. py:attribute:: bottlenecks
      :type:  list[str]
      :value: None



   .. py:attribute:: coordination_overhead_minutes
      :type:  float
      :value: None



   .. py:attribute:: critical_path
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_speedup
      :type:  float
      :value: None



   .. py:attribute:: execution_phases
      :type:  list[ExecutionPhase]
      :value: None



   .. py:attribute:: execution_strategy
      :type:  ExecutionStrategy
      :value: None



   .. py:attribute:: join_points
      :type:  list[JoinPoint]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: parallel_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: parallel_groups
      :type:  list[ParallelGroup]
      :value: None



   .. py:attribute:: parallelization_efficiency
      :type:  float
      :value: None



   .. py:attribute:: resource_requirements
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: sequential_duration_minutes
      :type:  float
      :value: None



.. py:class:: ParallelizationAnalyzer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analyzer for identifying parallelization opportunities in tasks.

   This class performs sophisticated analysis of task dependencies to identify
   optimal parallelization strategies, execution phases, and resource requirements.

   .. attribute:: max_parallel_tasks

      Maximum number of tasks to run in parallel

   .. attribute:: resource_constraints

      Resource limitations that affect parallelization

   .. attribute:: prefer_balanced_groups

      Whether to prefer balanced parallel groups

   .. attribute:: include_coordination_overhead

      Whether to include coordination overhead

   .. rubric:: Example

   .. code-block:: python

       analyzer = ParallelizationAnalyzer(
       max_parallel_tasks=8,
       resource_constraints={"cpu_cores": 4, "memory_gb": 16}
       )

       analysis = analyzer.analyze_task(complex_task)
       print(f"Recommended speedup: {analysis.estimated_speedup:.1f}x")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelizationAnalyzer
      :collapse:

   .. py:method:: _build_dependency_graph(items: list[haive.agents.common.models.task_analysis.base.Task | haive.agents.common.models.task_analysis.base.TaskStep], dependencies: list[haive.agents.common.models.task_analysis.base.DependencyNode]) -> dict[str, dict[str, Any]]

      Build a dependency graph from items and dependencies.


      .. autolink-examples:: _build_dependency_graph
         :collapse:


   .. py:method:: _calculate_critical_path(dependency_graph: dict[str, dict[str, Any]]) -> list[str]

      Calculate the critical path through the dependency graph.


      .. autolink-examples:: _calculate_critical_path
         :collapse:


   .. py:method:: _calculate_parallel_duration(phases: list[ExecutionPhase]) -> float

      Calculate total duration with parallel execution.


      .. autolink-examples:: _calculate_parallel_duration
         :collapse:


   .. py:method:: _calculate_peak_resources(parallel_groups: list[ParallelGroup]) -> dict[str, Any]

      Calculate peak resource requirements.


      .. autolink-examples:: _calculate_peak_resources
         :collapse:


   .. py:method:: _calculate_sequential_duration(items: list[haive.agents.common.models.task_analysis.base.Task | haive.agents.common.models.task_analysis.base.TaskStep]) -> float

      Calculate total duration if all tasks run sequentially.


      .. autolink-examples:: _calculate_sequential_duration
         :collapse:


   .. py:method:: _create_execution_phases(parallel_groups: list[ParallelGroup], dependencies: list[haive.agents.common.models.task_analysis.base.DependencyNode]) -> list[ExecutionPhase]

      Create execution phases from parallel groups.


      .. autolink-examples:: _create_execution_phases
         :collapse:


   .. py:method:: _determine_execution_strategy(parallel_groups: list[ParallelGroup], resource_constraints: dict[str, Any]) -> ExecutionStrategy

      Determine the best execution strategy.


      .. autolink-examples:: _determine_execution_strategy
         :collapse:


   .. py:method:: _extract_all_items(tree: haive.core.common.structures.tree.AutoTree) -> list[haive.agents.common.models.task_analysis.base.Task | haive.agents.common.models.task_analysis.base.TaskStep]

      Extract all tasks and steps from the tree.


      .. autolink-examples:: _extract_all_items
         :collapse:


   .. py:method:: _extract_dependencies(task: haive.agents.common.models.task_analysis.base.Task) -> list[haive.agents.common.models.task_analysis.base.DependencyNode]

      Extract all dependencies from task hierarchy.


      .. autolink-examples:: _extract_dependencies
         :collapse:


   .. py:method:: _find_longest_path(node: str, graph: dict[str, dict[str, Any]], visited: list[str]) -> tuple[list[str], float]

      Find the longest path from a given node.


      .. autolink-examples:: _find_longest_path
         :collapse:


   .. py:method:: _has_blocking_dependency(task_a: str, task_b: str, dependency_graph: dict[str, dict[str, Any]]) -> bool

      Check if there's a blocking dependency between two tasks.


      .. autolink-examples:: _has_blocking_dependency
         :collapse:


   .. py:method:: _identify_bottlenecks(parallel_groups: list[ParallelGroup], resource_constraints: dict[str, Any]) -> list[str]

      Identify potential bottlenecks.


      .. autolink-examples:: _identify_bottlenecks
         :collapse:


   .. py:method:: _identify_join_points(dependency_graph: dict[str, dict[str, Any]]) -> list[JoinPoint]

      Identify join points where multiple tasks synchronize.


      .. autolink-examples:: _identify_join_points
         :collapse:


   .. py:method:: _identify_parallel_groups(dependency_graph: dict[str, dict[str, Any]]) -> list[ParallelGroup]

      Identify groups of tasks that can run in parallel.


      .. autolink-examples:: _identify_parallel_groups
         :collapse:


   .. py:method:: analyze_task(task: haive.agents.common.models.task_analysis.base.Task) -> ParallelizationAnalysis

      Analyze a task for parallelization opportunities.

      :param task: Task to analyze

      :returns: Complete parallelization analysis


      .. autolink-examples:: analyze_task
         :collapse:


   .. py:attribute:: coordination_overhead_per_task_minutes
      :type:  float
      :value: None



   .. py:attribute:: include_coordination_overhead
      :type:  bool
      :value: None



   .. py:attribute:: max_parallel_tasks
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: prefer_balanced_groups
      :type:  bool
      :value: None



   .. py:attribute:: resource_constraints
      :type:  dict[str, Any]
      :value: None



