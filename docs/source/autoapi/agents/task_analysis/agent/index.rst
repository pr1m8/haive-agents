
:py:mod:`agents.task_analysis.agent`
====================================

.. py:module:: agents.task_analysis.agent


Classes
-------

.. autoapisummary::

   agents.task_analysis.agent.TaskAnalysisAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskAnalysisAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TaskAnalysisAgent {
        node [shape=record];
        "TaskAnalysisAgent" [label="TaskAnalysisAgent"];
        "haive.agents.base.agent.Agent" -> "TaskAnalysisAgent";
      }

.. autoclass:: agents.task_analysis.agent.TaskAnalysisAgent
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: agents.task_analysis.agent
   :collapse:
   
.. autolink-skip:: next
