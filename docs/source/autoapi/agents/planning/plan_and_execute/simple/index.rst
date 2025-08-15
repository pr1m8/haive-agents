agents.planning.plan_and_execute.simple
=======================================

.. py:module:: agents.planning.plan_and_execute.simple

.. autoapi-nested-parse::

   Simple Plan and Execute Agent - clean and proper.


   .. autolink-examples:: agents.planning.plan_and_execute.simple
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.simple.PlanAndExecuteAgent


Module Contents
---------------

.. py:class:: PlanAndExecuteAgent

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Plan and Execute using MultiAgent with proper graph building.


   .. autolink-examples:: PlanAndExecuteAgent
      :collapse:

   .. py:method:: build_graph() -> haive.agents.planning.plan_and_execute.v2.prompts.Any

      Build the plan-execute-replan graph using BaseGraph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create(tools: list | None = None, name: str = 'plan_and_execute', **kwargs) -> PlanAndExecuteAgent
      :classmethod:


      Create Plan and Execute agent with planner, executor, replanner.


      .. autolink-examples:: create
         :collapse:


