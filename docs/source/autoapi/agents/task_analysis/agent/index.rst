agents.task_analysis.agent
==========================

.. py:module:: agents.task_analysis.agent


Attributes
----------

.. autoapisummary::

   agents.task_analysis.agent.logger


Classes
-------

.. autoapisummary::

   agents.task_analysis.agent.TaskAnalysisAgent


Functions
---------

.. autoapisummary::

   agents.task_analysis.agent.join_analyses
   agents.task_analysis.agent.parallel_analysis_orchestrator
   agents.task_analysis.agent.recursive_expansion_orchestrator
   agents.task_analysis.agent.route_after_analysis
   agents.task_analysis.agent.route_after_decomposition
   agents.task_analysis.agent.route_after_validation
   agents.task_analysis.agent.route_final_decision


Module Contents
---------------

.. py:class:: TaskAnalysisAgent(**kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Comprehensive task analysis agent that orchestrates multiple analysis engines.

   This agent:
   1. Decomposes tasks hierarchically
   2. Analyzes complexity across multiple dimensions
   3. Identifies parallelization opportunities
   4. Plans execution with resource allocation
   5. Provides integrated analysis and recommendations

   Initialize with engines properly set up.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskAnalysisAgent
      :collapse:

   .. py:method:: analyze_task(task_description: str, domain: str = 'general', additional_context: str = '', max_depth: int | None = None) -> dict[str, Any]

      Analyze a task comprehensively.

      :param task_description: Natural language task description
      :param domain: Task domain (e.g., "software", "research", "creative")
      :param additional_context: Any additional context
      :param max_depth: Maximum decomposition depth (uses default if None)

      :returns: Comprehensive analysis results


      .. autolink-examples:: analyze_task
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the task analysis workflow graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_complexity_assessment(analysis_result: dict[str, Any]) -> haive.agents.task_analysis.complexity.models.ComplexityVector | None

      Extract complexity assessment from analysis results.


      .. autolink-examples:: get_complexity_assessment
         :collapse:


   .. py:method:: get_execution_plan(analysis_result: dict[str, Any]) -> haive.agents.task_analysis.execution.models.ExecutionPlan | None

      Extract execution plan from analysis results.


      .. autolink-examples:: get_execution_plan
         :collapse:


   .. py:method:: get_recommendations(analysis_result: dict[str, Any]) -> list[str]

      Extract recommendations from analysis results.


      .. autolink-examples:: get_recommendations
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the agent with schema derived from engines.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: enable_recursive_decomposition
      :type:  bool
      :value: None



   .. py:attribute:: max_decomposition_depth
      :type:  int
      :value: None



   .. py:attribute:: parallel_analysis
      :type:  bool
      :value: None



.. py:function:: join_analyses(state: dict[str, Any]) -> langgraph.types.Command[Literal['execution_planning', 'optimization', 'integrate_analysis']]

   Join parallel analyses and route next.


   .. autolink-examples:: join_analyses
      :collapse:

.. py:function:: parallel_analysis_orchestrator(state: dict[str, Any]) -> langgraph.types.Command[Literal['complexity_assessment', 'context_analysis', 'tree_analysis']]

   Orchestrate parallel analysis using Send.


   .. autolink-examples:: parallel_analysis_orchestrator
      :collapse:

.. py:function:: recursive_expansion_orchestrator(state: dict[str, Any]) -> langgraph.types.Command[Literal['recursive_decompose', 'validate_decomposition']]

   Orchestrate recursive decomposition.


   .. autolink-examples:: recursive_expansion_orchestrator
      :collapse:

.. py:function:: route_after_analysis(state: dict[str, Any]) -> str

   Route after parallel analysis completes.


   .. autolink-examples:: route_after_analysis
      :collapse:

.. py:function:: route_after_decomposition(state: dict[str, Any]) -> str

   Route after initial decomposition.


   .. autolink-examples:: route_after_decomposition
      :collapse:

.. py:function:: route_after_validation(state: dict[str, Any]) -> str

   Route after validation.


   .. autolink-examples:: route_after_validation
      :collapse:

.. py:function:: route_final_decision(state: dict[str, Any]) -> str

   Make final routing decision.


   .. autolink-examples:: route_final_decision
      :collapse:

.. py:data:: logger

