models.task_analysis.branching
==============================

.. py:module:: models.task_analysis.branching

.. autoapi-nested-parse::

   Task branching and decomposition analysis.

   This module analyzes how tasks can be broken down into subtasks, identifying
   parallel execution opportunities, sequential dependencies, and optimal
   decomposition strategies.


   .. autolink-examples:: models.task_analysis.branching
      :collapse:


Classes
-------

.. autoapisummary::

   models.task_analysis.branching.BranchType
   models.task_analysis.branching.TaskBranch
   models.task_analysis.branching.TaskDecomposition


Module Contents
---------------

.. py:class:: BranchType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of task branches and execution patterns.

   .. attribute:: SEQUENTIAL

      Tasks that must be executed in order

   .. attribute:: PARALLEL

      Tasks that can be executed simultaneously

   .. attribute:: CONDITIONAL

      Tasks that depend on conditions or outcomes

   .. attribute:: ITERATIVE

      Tasks that repeat with feedback loops

   .. attribute:: CONVERGENT

      Multiple branches that merge into one

   .. attribute:: DIVERGENT

      One task that splits into multiple branches

   .. attribute:: INDEPENDENT

      Completely independent execution streams

   .. attribute:: DEPENDENT

      Branches with complex interdependencies

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BranchType
      :collapse:

   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: CONVERGENT
      :value: 'convergent'



   .. py:attribute:: DEPENDENT
      :value: 'dependent'



   .. py:attribute:: DIVERGENT
      :value: 'divergent'



   .. py:attribute:: INDEPENDENT
      :value: 'independent'



   .. py:attribute:: ITERATIVE
      :value: 'iterative'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



.. py:class:: TaskBranch(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual branch in task decomposition.

   Represents a single execution path or subtask within a larger task
   decomposition, including its dependencies, requirements, and characteristics.

   .. attribute:: branch_id

      Unique identifier for this branch

   .. attribute:: name

      Human-readable name for the branch

   .. attribute:: description

      Detailed description of what this branch accomplishes

   .. attribute:: branch_type

      Type of execution pattern for this branch

   .. attribute:: estimated_effort

      Relative effort required (1-10 scale)

   .. attribute:: estimated_duration

      Expected time to complete

   .. attribute:: prerequisites

      Other branches that must complete first

   .. attribute:: enables

      Branches that this branch enables

   .. attribute:: resources_needed

      Specific resources required for this branch

   .. attribute:: parallel_compatible

      Whether this can run in parallel with others

   .. rubric:: Example

   .. code-block:: python

       # Finding Wimbledon winner's birthday - first branch
       winner_branch = TaskBranch(
       branch_id="find_winner",
       name="Find Recent Wimbledon Winner",
       description="Look up the most recent Wimbledon championship winner",
       branch_type=BranchType.SEQUENTIAL,
       estimated_effort=3,
       estimated_duration=timedelta(minutes=5),
       prerequisites=[],
       enables=["find_birthday"],
       resources_needed=["web_search", "sports_database"]
       )

       # Cancer research - complex branch
       research_branch = TaskBranch(
       branch_id="mechanism_research",
       name="Research Cancer Mechanisms",
       description="Deep investigation into cellular mechanisms of cancer development",
       branch_type=BranchType.ITERATIVE,
       estimated_effort=10,
       estimated_duration=timedelta(weeks=52),
       prerequisites=["literature_review", "lab_setup"],
       resources_needed=["research_lab", "expert_oncologists", "funding"]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskBranch
      :collapse:

   .. py:method:: get_duration_category() -> str

      Get duration category classification.

      :returns: String describing duration category


      .. autolink-examples:: get_duration_category
         :collapse:


   .. py:method:: get_effort_category() -> str

      Get effort category classification.

      :returns: String describing effort category


      .. autolink-examples:: get_effort_category
         :collapse:


   .. py:method:: has_dependencies() -> bool

      Check if this branch has prerequisite dependencies.

      :returns: True if branch has prerequisites


      .. autolink-examples:: has_dependencies
         :collapse:


   .. py:method:: is_enabling() -> bool

      Check if this branch enables other branches.

      :returns: True if branch enables others


      .. autolink-examples:: is_enabling
         :collapse:


   .. py:method:: is_high_risk() -> bool

      Check if this is a high-risk branch.

      :returns: True if risk level is 4 or 5


      .. autolink-examples:: is_high_risk
         :collapse:


   .. py:method:: is_likely_to_succeed(threshold: float = 0.7) -> bool

      Check if branch is likely to succeed.

      :param threshold: Minimum probability for "likely"

      :returns: True if success probability exceeds threshold


      .. autolink-examples:: is_likely_to_succeed
         :collapse:


   .. py:attribute:: branch_id
      :type:  str
      :value: None



   .. py:attribute:: branch_type
      :type:  BranchType
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: enables
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_duration
      :type:  datetime.timedelta
      :value: None



   .. py:attribute:: estimated_effort
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parallel_compatible
      :type:  bool
      :value: None



   .. py:attribute:: prerequisites
      :type:  list[str]
      :value: None



   .. py:attribute:: resources_needed
      :type:  list[str]
      :value: None



   .. py:attribute:: risk_level
      :type:  int
      :value: None



   .. py:attribute:: success_probability
      :type:  float
      :value: None



.. py:class:: TaskDecomposition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete task breakdown into subtasks and execution branches.

   Analyzes how a complex task can be decomposed into manageable subtasks,
   identifying execution patterns, dependencies, and optimization opportunities.

   .. attribute:: task_description

      Original task being decomposed

   .. attribute:: branches

      List of individual execution branches

   .. attribute:: execution_pattern

      Overall execution pattern

   .. attribute:: critical_path

      Sequence of branches on the critical path

   .. attribute:: parallelization_opportunities

      Groups of branches that can run in parallel

   .. attribute:: bottlenecks

      Branches that are likely to be bottlenecks

   .. attribute:: total_estimated_effort

      Sum of all branch efforts

   .. attribute:: estimated_duration_sequential

      Duration if executed sequentially

   .. attribute:: estimated_duration_optimal

      Duration with optimal parallelization

   .. rubric:: Example

   .. code-block:: python

       # Simple factual lookup task
       decomposition = TaskDecomposition.decompose_task(
       task_description="Find the birthday of the most recent Wimbledon winner",
       complexity_hint="simple_research"
       )

       # Complex research task
       decomposition = TaskDecomposition.decompose_task(
       task_description="Develop a cure for cancer",
       complexity_hint="breakthrough_research"
       )

       print(f"Branches: {len(decomposition.branches)}")
       print(f"Critical path: {decomposition.critical_path}")
       print(f"Parallelizable: {decomposition.parallelization_opportunities}")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskDecomposition
      :collapse:

   .. py:method:: calculate_parallelization_speedup() -> float

      Calculate potential speedup from parallelization.

      :returns: Speedup ratio (sequential_time / optimal_time)


      .. autolink-examples:: calculate_parallelization_speedup
         :collapse:


   .. py:method:: create_simple_sequential(task_description: str, branch_descriptions: list[str], effort_estimates: list[int] | None = None, duration_estimates: list[datetime.timedelta] | None = None) -> TaskDecomposition
      :classmethod:


      Create a simple sequential task decomposition.

      :param task_description: Description of the overall task
      :param branch_descriptions: List of branch descriptions
      :param effort_estimates: Optional effort estimates (defaults to 3 for all)
      :param duration_estimates: Optional duration estimates (defaults to 1 hour each)

      :returns: TaskDecomposition with sequential branches


      .. autolink-examples:: create_simple_sequential
         :collapse:


   .. py:method:: find_independent_branches() -> list[str]

      Find branches with no dependencies.

      :returns: List of branch IDs that can start immediately


      .. autolink-examples:: find_independent_branches
         :collapse:


   .. py:method:: find_terminal_branches() -> list[str]

      Find branches that don't enable anything else.

      :returns: List of branch IDs that are endpoints


      .. autolink-examples:: find_terminal_branches
         :collapse:


   .. py:method:: get_complexity_metrics() -> dict[str, Any]

      Get various complexity metrics for the decomposition.

      :returns: Dictionary of complexity metrics


      .. autolink-examples:: get_complexity_metrics
         :collapse:


   .. py:method:: get_dependency_graph() -> dict[str, list[str]]

      Get dependency graph as adjacency list.

      :returns: Dictionary mapping branch IDs to their dependencies


      .. autolink-examples:: get_dependency_graph
         :collapse:


   .. py:method:: get_enables_graph() -> dict[str, list[str]]

      Get enables graph as adjacency list.

      :returns: Dictionary mapping branch IDs to branches they enable


      .. autolink-examples:: get_enables_graph
         :collapse:


   .. py:method:: get_execution_recommendations() -> list[str]

      Get recommendations for optimal execution.

      :returns: List of execution recommendations


      .. autolink-examples:: get_execution_recommendations
         :collapse:


   .. py:method:: validate_decomposition_consistency() -> TaskDecomposition

      Validate that decomposition is internally consistent.

      :returns: Self if validation passes

      :raises ValueError: If decomposition has inconsistencies


      .. autolink-examples:: validate_decomposition_consistency
         :collapse:


   .. py:attribute:: bottlenecks
      :type:  list[str]
      :value: None



   .. py:attribute:: branches
      :type:  list[TaskBranch]
      :value: None



   .. py:attribute:: critical_path
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_duration_optimal
      :type:  datetime.timedelta
      :value: None



   .. py:attribute:: estimated_duration_sequential
      :type:  datetime.timedelta
      :value: None



   .. py:attribute:: execution_pattern
      :type:  str
      :value: None



   .. py:attribute:: parallelization_opportunities
      :type:  list[list[str]]
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



   .. py:attribute:: total_estimated_effort
      :type:  int
      :value: None



