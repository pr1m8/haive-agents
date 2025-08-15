agents.planning.plan_and_execute.v2.state
=========================================

.. py:module:: agents.planning.plan_and_execute.v2.state

.. autoapi-nested-parse::

   State schema for Plan and Execute Agent v2.


   .. autolink-examples:: agents.planning.plan_and_execute.v2.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.v2.state.PlanAndExecuteState


Module Contents
---------------

.. py:class:: PlanAndExecuteState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   State for Plan and Execute Agent v2.


   .. autolink-examples:: PlanAndExecuteState
      :collapse:

   .. py:method:: get_next_step() -> haive.agents.planning.plan_and_execute.v2.models.Step | None

      Get the next incomplete step.


      .. autolink-examples:: get_next_step
         :collapse:


   .. py:method:: is_plan_complete() -> bool

      Check if the plan is complete.


      .. autolink-examples:: is_plan_complete
         :collapse:


   .. py:method:: update_past_steps(step: haive.agents.planning.plan_and_execute.v2.models.Step) -> None

      Add completed step to past_steps.


      .. autolink-examples:: update_past_steps
         :collapse:


   .. py:attribute:: final_response
      :type:  str | None
      :value: None



   .. py:attribute:: input
      :type:  str
      :value: None



   .. py:attribute:: past_steps
      :type:  list[haive.agents.planning.plan_and_execute.v2.models.Step]
      :value: None



   .. py:attribute:: plan
      :type:  haive.agents.planning.plan_and_execute.v2.models.Plan | None
      :value: None



   .. py:attribute:: response
      :type:  str | None
      :value: None



