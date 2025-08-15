agents.planning.rewoo_v3.state
==============================

.. py:module:: agents.planning.rewoo_v3.state

.. autoapi-nested-parse::

   ReWOO V3 State Schema with computed fields for dynamic prompts.

   This module defines the state schema for ReWOO V3 Agent using our proven
   MessagesState + computed fields pattern from Plan-and-Execute V3 success.


   .. autolink-examples:: agents.planning.rewoo_v3.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.state.ReWOOV3State


Module Contents
---------------

.. py:class:: ReWOOV3State

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for ReWOO V3 with computed fields for prompt templates.

   ReWOO (Reasoning WithOut Observation) separates planning, execution, and synthesis:
   1. Planner creates complete plan upfront with evidence placeholders
   2. Worker executes all tool calls to collect evidence
   3. Solver synthesizes all evidence into final answer

   This state tracks the complete ReWOO workflow with dynamic computed fields
   for prompt template variable substitution.


   .. autolink-examples:: ReWOOV3State
      :collapse:

   .. py:method:: update_execution_result(execution_result: dict[str, Any]) -> None

      Update with worker agent result.


      .. autolink-examples:: update_execution_result
         :collapse:


   .. py:method:: update_planning_result(plan_result: dict[str, Any]) -> None

      Update with planner agent result.


      .. autolink-examples:: update_planning_result
         :collapse:


   .. py:method:: update_solution_result(solution_result: dict[str, Any]) -> None

      Update with solver agent result.


      .. autolink-examples:: update_solution_result
         :collapse:


   .. py:property:: available_tools
      :type: str


      Formatted list of available tools for planner prompt.

      .. autolink-examples:: available_tools
         :collapse:


   .. py:attribute:: current_phase
      :type:  str
      :value: None



   .. py:attribute:: evidence_collection
      :type:  dict[str, Any] | None
      :value: None



   .. py:property:: evidence_summary
      :type: str


      Formatted evidence for solver agent prompt.

      .. autolink-examples:: evidence_summary
         :collapse:


   .. py:attribute:: execution_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: execution_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:property:: execution_status
      :type: str


      Current ReWOO workflow status for prompts.

      .. autolink-examples:: execution_status
         :collapse:


   .. py:attribute:: final_solution
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:property:: phase_progress
      :type: str


      Progress through ReWOO phases for prompts.

      .. autolink-examples:: phase_progress
         :collapse:


   .. py:property:: plan_summary
      :type: str


      Formatted plan for worker agent prompt.

      .. autolink-examples:: plan_summary
         :collapse:


   .. py:attribute:: planning_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: reasoning_plan
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: solving_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: started_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: tools_available
      :type:  list[str]
      :value: None



   .. py:property:: workflow_context
      :type: str


      Complete workflow context for solver synthesis.

      .. autolink-examples:: workflow_context
         :collapse:


