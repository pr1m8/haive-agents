models.task_analysis.analysis
=============================

.. py:module:: models.task_analysis.analysis

.. autoapi-nested-parse::

   Main task analysis model combining all analysis components.

   This module provides the comprehensive TaskAnalysis model that combines
   complexity assessment, solvability analysis, task decomposition, and
   execution strategy recommendations.


   .. autolink-examples:: models.task_analysis.analysis
      :collapse:


Attributes
----------

.. autoapisummary::

   models.task_analysis.analysis.ComplexityType


Classes
-------

.. autoapisummary::

   models.task_analysis.analysis.AnalysisMethod
   models.task_analysis.analysis.ExecutionStrategy
   models.task_analysis.analysis.PlanningRequirement
   models.task_analysis.analysis.TaskAnalysis
   models.task_analysis.analysis.TaskComplexity
   models.task_analysis.analysis.TaskDimension


Module Contents
---------------

.. py:class:: AnalysisMethod

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Methods for analyzing task complexity and requirements.

   .. attribute:: HEURISTIC

      Rule-based heuristic analysis

   .. attribute:: PATTERN_MATCHING

      Pattern matching against known task types

   .. attribute:: DECOMPOSITION

      Bottom-up analysis through task decomposition

   .. attribute:: EXPERT_SYSTEM

      Expert system with domain knowledge

   .. attribute:: MACHINE_LEARNING

      ML-based complexity prediction

   .. attribute:: HYBRID

      Combination of multiple methods

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnalysisMethod
      :collapse:

   .. py:attribute:: DECOMPOSITION
      :value: 'decomposition'



   .. py:attribute:: EXPERT_SYSTEM
      :value: 'expert_system'



   .. py:attribute:: HEURISTIC
      :value: 'heuristic'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: MACHINE_LEARNING
      :value: 'machine_learning'



   .. py:attribute:: PATTERN_MATCHING
      :value: 'pattern_matching'



.. py:class:: ExecutionStrategy(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Recommended execution strategy for a task.

   Provides specific recommendations for how to approach task execution
   based on the complexity and solvability analysis.

   .. attribute:: strategy_type

      Primary execution approach

   .. attribute:: priority_level

      Urgency/priority level for the task

   .. attribute:: recommended_approach

      Detailed approach description

   .. attribute:: resource_allocation

      How to allocate resources

   .. attribute:: timeline_strategy

      How to manage timing and sequencing

   .. attribute:: risk_mitigation

      Risk mitigation strategies

   .. attribute:: success_factors

      Key factors for success

   .. attribute:: fallback_options

      Alternative approaches if primary fails

   .. rubric:: Example

   .. code-block:: python

       strategy = ExecutionStrategy(
       strategy_type="parallel_execution",
       priority_level="high",
       recommended_approach="Execute independent branches in parallel while managing dependencies",
       resource_allocation={"computational": 0.4, "human_expert": 0.3, "time": 0.3},
       timeline_strategy="front_load_critical_path",
       risk_mitigation=["backup_data_sources", "expert_consultation", "iterative_validation"],
       success_factors=["clear_requirements", "adequate_resources", "expert_oversight"]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionStrategy
      :collapse:

   .. py:method:: validate_resource_allocation(v: dict[str, float]) -> dict[str, float]
      :classmethod:


      Validate that resource allocation proportions sum to approximately 1.0.

      :param v: Resource allocation dictionary

      :returns: Validated resource allocation

      :raises ValueError: If proportions don't sum to approximately 1.0


      .. autolink-examples:: validate_resource_allocation
         :collapse:


   .. py:attribute:: fallback_options
      :type:  list[str]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: priority_level
      :type:  str
      :value: None



   .. py:attribute:: recommended_approach
      :type:  str
      :value: None



   .. py:attribute:: resource_allocation
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: risk_mitigation
      :type:  list[str]
      :value: None



   .. py:attribute:: strategy_type
      :type:  str
      :value: None



   .. py:attribute:: success_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: timeline_strategy
      :type:  str
      :value: None



.. py:class:: PlanningRequirement(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for planning requirements.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanningRequirement
      :collapse:

   .. py:attribute:: constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: planning_horizon
      :type:  str
      :value: None



.. py:class:: TaskAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive task analysis combining all analysis components.

   This is the main model that brings together complexity assessment,
   solvability analysis, task decomposition, and execution recommendations
   into a unified analysis.

   .. attribute:: task_description

      Original task description

   .. attribute:: domain

      Task domain or field

   .. attribute:: analysis_method

      Method used for analysis

   .. attribute:: complexity

      Complexity assessment

   .. attribute:: solvability

      Solvability assessment

   .. attribute:: decomposition

      Task decomposition (optional)

   .. attribute:: planning

      Planning requirements

   .. attribute:: execution_strategy

      Recommended execution approach

   .. attribute:: analysis_timestamp

      When analysis was performed

   .. attribute:: analysis_confidence

      Overall confidence in the analysis

   .. rubric:: Example

   .. code-block:: python

       # Analyze a simple research task
       analysis = TaskAnalysis.analyze_task(
       task_description="Find the birthday of the most recent Wimbledon winner",
       domain="sports_research",
       context="Factual lookup requiring web search"
       )

       # Analyze a complex research problem
       analysis = TaskAnalysis.analyze_task(
       task_description="Develop a cure for cancer through novel therapeutic approaches",
       domain="medical_research",
       context="Breakthrough research requiring novel discoveries"
       )

       print(f"Complexity: {analysis.complexity.overall_complexity}")
       print(f"Solvable: {analysis.solvability.is_currently_solvable}")
       print(f"Strategy: {analysis.execution_strategy.strategy_type}")

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskAnalysis
      :collapse:

   .. py:method:: _analyze_complexity(task_description: str, domain: str, context: str | None) -> TaskComplexity
      :classmethod:


      Analyze task complexity using heuristics.


      .. autolink-examples:: _analyze_complexity
         :collapse:


   .. py:method:: _analyze_solvability(task_description: str, domain: str, complexity: TaskComplexity) -> haive.agents.common.models.task_analysis.solvability.SolvabilityAssessment
      :classmethod:


      Analyze task solvability.


      .. autolink-examples:: _analyze_solvability
         :collapse:


   .. py:method:: _generate_decomposition(task_description: str, complexity: TaskComplexity) -> haive.agents.common.models.task_analysis.branching.TaskDecomposition | None
      :classmethod:


      Generate basic task decomposition.


      .. autolink-examples:: _generate_decomposition
         :collapse:


   .. py:method:: _generate_execution_strategy(complexity: TaskComplexity, solvability: haive.agents.common.models.task_analysis.solvability.SolvabilityAssessment, planning: PlanningRequirement) -> ExecutionStrategy
      :classmethod:


      Generate execution strategy.


      .. autolink-examples:: _generate_execution_strategy
         :collapse:


   .. py:method:: _generate_planning_requirements(complexity: TaskComplexity, solvability: haive.agents.common.models.task_analysis.solvability.SolvabilityAssessment) -> PlanningRequirement
      :classmethod:


      Generate planning requirements based on complexity and solvability.


      .. autolink-examples:: _generate_planning_requirements
         :collapse:


   .. py:method:: _infer_domain(task_description: str) -> str
      :classmethod:


      Infer task domain from description.


      .. autolink-examples:: _infer_domain
         :collapse:


   .. py:method:: analyze_task(task_description: str, domain: str | None = None, context: str | None = None, analysis_method: AnalysisMethod = AnalysisMethod.HYBRID) -> TaskAnalysis
      :classmethod:


      Analyze a task and return comprehensive analysis.

      This is the main entry point for task analysis. It performs
      heuristic analysis based on task characteristics.

      :param task_description: Description of the task to analyze
      :param domain: Optional domain specification
      :param context: Optional additional context
      :param analysis_method: Method to use for analysis

      :returns: Complete TaskAnalysis instance


      .. autolink-examples:: analyze_task
         :collapse:


   .. py:method:: generate_executive_summary() -> str

      Generate an executive summary of the analysis.

      :returns: Formatted executive summary


      .. autolink-examples:: generate_executive_summary
         :collapse:


   .. py:method:: get_execution_recommendations() -> list[str]

      Get prioritized execution recommendations.

      :returns: List of actionable recommendations


      .. autolink-examples:: get_execution_recommendations
         :collapse:


   .. py:method:: get_overall_assessment() -> dict[str, Any]

      Get overall assessment summary.

      :returns: Dictionary with key assessment metrics


      .. autolink-examples:: get_overall_assessment
         :collapse:


   .. py:method:: validate_analysis_consistency() -> TaskAnalysis

      Validate that all analysis components are consistent.

      :returns: Self if validation passes

      :raises ValueError: If analysis components are inconsistent


      .. autolink-examples:: validate_analysis_consistency
         :collapse:


   .. py:attribute:: analysis_confidence
      :type:  float
      :value: None



   .. py:attribute:: analysis_method
      :type:  AnalysisMethod
      :value: None



   .. py:attribute:: analysis_timestamp
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: complexity
      :type:  TaskComplexity
      :value: None



   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: decomposition
      :type:  haive.agents.common.models.task_analysis.branching.TaskDecomposition | None
      :value: None



   .. py:attribute:: domain
      :type:  str
      :value: None



   .. py:attribute:: execution_strategy
      :type:  ExecutionStrategy
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: planning
      :type:  PlanningRequirement
      :value: None



   .. py:attribute:: solvability
      :type:  haive.agents.common.models.task_analysis.solvability.SolvabilityAssessment
      :value: None



   .. py:attribute:: task_description
      :type:  str
      :value: None



.. py:class:: TaskComplexity(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for task complexity assessment.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskComplexity
      :collapse:

   .. py:method:: get_complexity_score() -> float

      Get overall complexity score.


      .. autolink-examples:: get_complexity_score
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: dimensions
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: overall_complexity
      :type:  ComplexityType
      :value: None



.. py:class:: TaskDimension

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Task dimensions for complexity assessment.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskDimension
      :collapse:

   .. py:attribute:: BREADTH
      :value: 'breadth'



   .. py:attribute:: COORDINATION
      :value: 'coordination'



   .. py:attribute:: DEPTH
      :value: 'depth'



   .. py:attribute:: KNOWLEDGE
      :value: 'knowledge'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: RESOURCE
      :value: 'resource'



   .. py:attribute:: TEMPORAL
      :value: 'temporal'



   .. py:attribute:: UNCERTAINTY
      :value: 'uncertainty'



.. py:data:: ComplexityType

