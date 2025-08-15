agents.planning.plan_and_execute.state
======================================

.. py:module:: agents.planning.plan_and_execute.state


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.state.PlanAndExecuteState


Module Contents
---------------

.. py:class:: PlanAndExecuteState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Represents the state for the PlanAndExecuteAgent.


   .. autolink-examples:: PlanAndExecuteState
      :collapse:

   .. py:method:: get_next_step() -> haive.agents.planning.plan_and_execute.models.Step | None

      Finds the next step that is either 'in_progress' or 'not_started'.


      .. autolink-examples:: get_next_step
         :collapse:


   .. py:method:: is_plan_complete() -> bool

      Checks if the entire plan is complete.


      .. autolink-examples:: is_plan_complete
         :collapse:


   .. py:method:: update_past_steps(step: haive.agents.planning.plan_and_execute.models.Step)

      Adds a completed step to `past_steps` and updates the plan accordingly.


      .. autolink-examples:: update_past_steps
         :collapse:


   .. py:attribute:: input
      :type:  str
      :value: None



   .. py:attribute:: past_steps
      :type:  list[haive.agents.planning.plan_and_execute.models.Step]
      :value: None



   .. py:attribute:: plan
      :type:  haive.agents.planning.plan_and_execute.models.Plan | None
      :value: None



   .. py:attribute:: response
      :type:  str | None
      :value: None



