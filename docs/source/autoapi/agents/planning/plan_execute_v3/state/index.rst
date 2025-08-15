agents.planning.plan_execute_v3.state
=====================================

.. py:module:: agents.planning.plan_execute_v3.state

.. autoapi-nested-parse::

   State schema for Plan-and-Execute V3 Agent.

   This module defines the state schema used by the Plan-and-Execute V3 agent,
   extending MessagesState with computed fields for plan tracking.


   .. autolink-examples:: agents.planning.plan_execute_v3.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.state.PlanExecuteV3State


Module Contents
---------------

.. py:class:: PlanExecuteV3State

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for Plan-and-Execute V3 agent.

   This state is shared across the planner, executor, evaluator, and replanner
   sub-agents to maintain full context throughout the execution.


   .. autolink-examples:: PlanExecuteV3State
      :collapse:

   .. py:method:: add_evaluation(evaluation: agents.planning.plan_execute_v3.models.PlanEvaluation) -> None

      Add an evaluation result.


      .. autolink-examples:: add_evaluation
         :collapse:


   .. py:method:: add_step_execution(execution: agents.planning.plan_execute_v3.models.StepExecution) -> None

      Add a step execution result and update plan.


      .. autolink-examples:: add_step_execution
         :collapse:


   .. py:method:: revise_plan(new_plan: agents.planning.plan_execute_v3.models.ExecutionPlan) -> None

      Replace current plan with a revised version.


      .. autolink-examples:: revise_plan
         :collapse:


   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:property:: current_step
      :type: str | None


      Get the current step description for the executor.

      .. autolink-examples:: current_step
         :collapse:


   .. py:attribute:: current_step_id
      :type:  int | None
      :value: None



   .. py:attribute:: errors
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: evaluations
      :type:  list[agents.planning.plan_execute_v3.models.PlanEvaluation]
      :value: None



   .. py:property:: execution_summary
      :type: str


      Get a summary of the entire execution.

      .. autolink-examples:: execution_summary
         :collapse:


   .. py:property:: execution_time
      :type: float | None


      Total execution time in seconds.

      .. autolink-examples:: execution_time
         :collapse:


   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:property:: key_findings
      :type: list[str]


      Extract key findings from executions.

      .. autolink-examples:: key_findings
         :collapse:


   .. py:property:: objective
      :type: str


      Extract the objective from the plan or messages.

      .. autolink-examples:: objective
         :collapse:


   .. py:attribute:: plan
      :type:  agents.planning.plan_execute_v3.models.ExecutionPlan | None
      :value: None



   .. py:attribute:: plan_history
      :type:  list[agents.planning.plan_execute_v3.models.ExecutionPlan]
      :value: None



   .. py:property:: plan_status
      :type: str


      Get formatted plan status for agents.

      .. autolink-examples:: plan_status
         :collapse:


   .. py:property:: previous_results
      :type: str


      Get formatted previous step execution results.

      .. autolink-examples:: previous_results
         :collapse:


   .. py:attribute:: revision_count
      :type:  int
      :value: None



   .. py:property:: should_evaluate
      :type: bool


      Determine if we should run evaluation.

      .. autolink-examples:: should_evaluate
         :collapse:


   .. py:attribute:: started_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: step_executions
      :type:  list[agents.planning.plan_execute_v3.models.StepExecution]
      :value: None



