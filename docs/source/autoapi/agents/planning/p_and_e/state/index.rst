agents.planning.p_and_e.state
=============================

.. py:module:: agents.planning.p_and_e.state

.. autoapi-nested-parse::

   State schemas for Plan and Execute Agent System.

   This module defines the state schemas used by the planning, execution,
   and replanning agents.


   .. autolink-examples:: agents.planning.p_and_e.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.state.PlanExecuteState


Module Contents
---------------

.. py:class:: PlanExecuteState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_state.MessagesState`


   Main state schema for the Plan and Execute agent system.

   This state is shared across planning, execution, and replanning agents
   to maintain the full context of the operation.


   .. autolink-examples:: PlanExecuteState
      :collapse:

   .. py:attribute:: __shared_fields__
      :value: ['messages', 'objective', 'plan', 'execution_results', 'final_answer']



   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:property:: current_step
      :type: str | None


      Get the current step formatted for the executor.

      .. autolink-examples:: current_step
         :collapse:


   .. py:attribute:: current_step_id
      :type:  int | None
      :value: None



   .. py:attribute:: errors
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: execution_results
      :type:  list[haive.agents.planning.p_and_e.models.ExecutionResult]
      :value: None



   .. py:property:: execution_time
      :type: float | None


      Total execution time in seconds.

      .. autolink-examples:: execution_time
         :collapse:


   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:property:: objective
      :type: str


      Get the objective from the plan or messages.

      .. autolink-examples:: objective
         :collapse:


   .. py:attribute:: plan
      :type:  haive.agents.planning.p_and_e.models.Plan | None
      :value: None



   .. py:property:: plan_status
      :type: str


      Get the plan status formatted for the executor.

      .. autolink-examples:: plan_status
         :collapse:


   .. py:property:: previous_results
      :type: str


      Get previous execution results formatted for the executor.

      .. autolink-examples:: previous_results
         :collapse:


   .. py:attribute:: replan_count
      :type:  int
      :value: None



   .. py:attribute:: replan_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:property:: should_replan
      :type: bool


      Determine if replanning is needed.

      .. autolink-examples:: should_replan
         :collapse:


   .. py:attribute:: started_at
      :type:  datetime.datetime
      :value: None



