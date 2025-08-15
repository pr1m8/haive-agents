agents.planning.plan_and_execute.v2.agent
=========================================

.. py:module:: agents.planning.plan_and_execute.v2.agent

.. autoapi-nested-parse::

   Plan and Execute Agent v2 using MultiAgent pattern.


   .. autolink-examples:: agents.planning.plan_and_execute.v2.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.v2.agent.PlanAndExecuteAgent


Module Contents
---------------

.. py:class:: PlanAndExecuteAgent

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Plan and Execute agent using multi-agent sequential pattern.

   Flow: Planner → Executor → Replanner (loop until complete)


   .. autolink-examples:: PlanAndExecuteAgent
      :collapse:

   .. py:method:: create_default(tools: list | None = None, **kwargs)
      :classmethod:


      Create P&E agent with default configuration.


      .. autolink-examples:: create_default
         :collapse:


   .. py:method:: get_next_action(state: haive.agents.planning.plan_and_execute.v2.state.PlanAndExecuteState) -> str

      Determine next action based on current state.


      .. autolink-examples:: get_next_action
         :collapse:


   .. py:method:: process_execution_result(state: haive.agents.planning.plan_and_execute.v2.state.PlanAndExecuteState, result: haive.agents.planning.plan_and_execute.v2.models.ExecutionResult) -> haive.agents.planning.plan_and_execute.v2.state.PlanAndExecuteState

      Process execution result and update state.


      .. autolink-examples:: process_execution_result
         :collapse:


   .. py:method:: process_replan_result(state: haive.agents.planning.plan_and_execute.v2.state.PlanAndExecuteState, result: haive.agents.planning.plan_and_execute.v2.models.Act) -> haive.agents.planning.plan_and_execute.v2.state.PlanAndExecuteState

      Process replanning result and update state.


      .. autolink-examples:: process_replan_result
         :collapse:


   .. py:method:: should_continue_execution(state: haive.agents.planning.plan_and_execute.v2.state.PlanAndExecuteState) -> bool

      Check if execution should continue based on state.


      .. autolink-examples:: should_continue_execution
         :collapse:


