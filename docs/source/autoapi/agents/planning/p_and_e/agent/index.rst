agents.planning.p_and_e.agent
=============================

.. py:module:: agents.planning.p_and_e.agent


Attributes
----------

.. autoapisummary::

   agents.planning.p_and_e.agent.logger


Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.agent.PlanAndExecuteAgent


Functions
---------

.. autoapisummary::

   agents.planning.p_and_e.agent.check_plan_complete
   agents.planning.p_and_e.agent.route_after_evaluation


Module Contents
---------------

.. py:class:: PlanAndExecuteAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Plan and Execute agent that orchestrates planning, execution, and replanning.


   .. autolink-examples:: PlanAndExecuteAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the plan-execute-replan graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the three engines required for plan-execute-replan workflow.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: state_schema
      :type:  type
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: use_prebuilt_base
      :type:  bool
      :value: None



.. py:function:: check_plan_complete(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

   Check if plan execution is complete or needs more steps.


   .. autolink-examples:: check_plan_complete
      :collapse:

.. py:function:: route_after_evaluation(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

   Route based on evaluation decision.


   .. autolink-examples:: route_after_evaluation
      :collapse:

.. py:data:: logger

