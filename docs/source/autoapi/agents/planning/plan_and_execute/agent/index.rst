agents.planning.plan_and_execute.agent
======================================

.. py:module:: agents.planning.plan_and_execute.agent


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.agent.PlanAndExecuteAgent


Module Contents
---------------

.. py:class:: PlanAndExecuteAgent(config: haive.agents.planning.plan_and_execute.config.PlanAndExecuteConfig = PlanAndExecuteConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.planning.plan_and_execute.config.PlanAndExecuteConfig`\ ]


   .. py:method:: arun(input_text: str | None = None, input_dict: dict[str, Any] | None = None)
      :async:



   .. py:method:: execute_step(state: PlanAndExecuteState)
      :async:


      Executes the next step in the plan.


      .. autolink-examples:: execute_step
         :collapse:


   .. py:method:: planner(state: PlanAndExecuteState)
      :async:



   .. py:method:: replan_step(state: PlanAndExecuteState)
      :async:


      Replans the steps based on completed progress.


      .. autolink-examples:: replan_step
         :collapse:


   .. py:method:: setup_workflow() -> None


   .. py:method:: should_end(state: PlanAndExecuteState)

      Determines if the process should end.

      :param state: The current state.
      :type state: PlanAndExecuteState

      :returns: "END" if finished, otherwise continue to the next node.
      :rtype: str


      .. autolink-examples:: should_end
         :collapse:


   .. py:attribute:: agent_executor_runnable


   .. py:attribute:: config


   .. py:attribute:: planner_runnable


   .. py:attribute:: replanner_runnable


