agents.planning.plan_execute_v3.engines
=======================================

.. py:module:: agents.planning.plan_execute_v3.engines

.. autoapi-nested-parse::

   Engines for Plan-and-Execute V3 Agent.

   This module contains the specialized engines used by the Plan-and-Execute V3 agent
   for planning, validation, execution, and monitoring.


   .. autolink-examples:: agents.planning.plan_execute_v3.engines
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.engines.ExecutorEngine
   agents.planning.plan_execute_v3.engines.MonitorEngine
   agents.planning.plan_execute_v3.engines.PlannerEngine
   agents.planning.plan_execute_v3.engines.ReplannerEngine
   agents.planning.plan_execute_v3.engines.ValidatorEngine


Module Contents
---------------

.. py:class:: ExecutorEngine(llm_config: haive.core.engine.aug_llm.AugLLMConfig, tools: list[langchain_core.tools.BaseTool])

   Engine for executing individual plan steps.

   Initialize executor engine.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutorEngine
      :collapse:

   .. py:method:: execute_step(step: agents.planning.plan_execute_v3.models.Step, context: dict[str, Any], previous_results: dict[str, Any]) -> tuple[Any, str | None]
      :async:


      Execute a single plan step.

      :param step: The step to execute
      :param context: Shared execution context
      :param previous_results: Results from previous steps

      :returns: Tuple of (result, error_message)


      .. autolink-examples:: execute_step
         :collapse:


   .. py:attribute:: llm


   .. py:attribute:: tools


.. py:class:: MonitorEngine(llm_config: haive.core.engine.aug_llm.AugLLMConfig)

   Engine for monitoring plan execution.

   Initialize monitor engine.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MonitorEngine
      :collapse:

   .. py:method:: _format_execution_state(plan: agents.planning.plan_execute_v3.models.Plan) -> str

      Format execution state for monitoring.


      .. autolink-examples:: _format_execution_state
         :collapse:


   .. py:method:: analyze_execution(plan: agents.planning.plan_execute_v3.models.Plan) -> dict[str, Any]
      :async:


      Analyze plan execution progress.

      :param plan: The plan being executed

      :returns: Analysis results with metrics and suggestions


      .. autolink-examples:: analyze_execution
         :collapse:


   .. py:attribute:: llm


.. py:class:: PlannerEngine(llm_config: haive.core.engine.aug_llm.AugLLMConfig, tools: list[langchain_core.tools.BaseTool])

   Engine for generating execution plans.

   Initialize planner engine.

   :param llm_config: LLM configuration
   :param tools: Available tools for planning


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlannerEngine
      :collapse:

   .. py:method:: _format_tools_description() -> str

      Format tools description for prompts.


      .. autolink-examples:: _format_tools_description
         :collapse:


   .. py:method:: _parse_plan_response(response: str, goal: str) -> agents.planning.plan_execute_v3.models.Plan

      Parse LLM response into a Plan object.


      .. autolink-examples:: _parse_plan_response
         :collapse:


   .. py:method:: generate_plan(goal: str) -> agents.planning.plan_execute_v3.models.Plan
      :async:


      Generate an execution plan for the given goal.

      :param goal: The goal to achieve

      :returns: Generated execution plan


      .. autolink-examples:: generate_plan
         :collapse:


   .. py:attribute:: llm


   .. py:attribute:: tools


   .. py:attribute:: tools_description
      :value: ''



.. py:class:: ReplannerEngine(llm_config: haive.core.engine.aug_llm.AugLLMConfig, tools: list[langchain_core.tools.BaseTool])

   Engine for replanning when execution fails.

   Initialize replanner engine.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReplannerEngine
      :collapse:

   .. py:method:: _format_plan_status(plan: agents.planning.plan_execute_v3.models.Plan) -> str

      Format current plan status.


      .. autolink-examples:: _format_plan_status
         :collapse:


   .. py:method:: _format_tools_description() -> str

      Format tools description for prompts.


      .. autolink-examples:: _format_tools_description
         :collapse:


   .. py:method:: _parse_plan_response(response: str, goal: str) -> agents.planning.plan_execute_v3.models.Plan

      Parse LLM response into a Plan object.


      .. autolink-examples:: _parse_plan_response
         :collapse:


   .. py:method:: create_revised_plan(original_plan: agents.planning.plan_execute_v3.models.Plan, issues: list[str]) -> agents.planning.plan_execute_v3.models.Plan
      :async:


      Create a revised plan based on execution issues.

      :param original_plan: The plan that encountered issues
      :param issues: List of issues encountered

      :returns: Revised execution plan


      .. autolink-examples:: create_revised_plan
         :collapse:


   .. py:attribute:: llm


   .. py:attribute:: tools


   .. py:attribute:: tools_description
      :value: ''



.. py:class:: ValidatorEngine(llm_config: haive.core.engine.aug_llm.AugLLMConfig, tools: list[langchain_core.tools.BaseTool])

   Engine for validating and refining plans.

   Initialize validator engine.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ValidatorEngine
      :collapse:

   .. py:method:: _format_plan_for_validation(plan: agents.planning.plan_execute_v3.models.Plan) -> str

      Format plan for validation prompt.


      .. autolink-examples:: _format_plan_for_validation
         :collapse:


   .. py:method:: _format_tools_description() -> str

      Format tools description for prompts.


      .. autolink-examples:: _format_tools_description
         :collapse:


   .. py:method:: _parse_validation_response(response: str, original_plan: agents.planning.plan_execute_v3.models.Plan) -> agents.planning.plan_execute_v3.models.PlanValidationResult

      Parse validation response.


      .. autolink-examples:: _parse_validation_response
         :collapse:


   .. py:method:: validate_plan(plan: agents.planning.plan_execute_v3.models.Plan) -> agents.planning.plan_execute_v3.models.PlanValidationResult
      :async:


      Validate a plan and suggest refinements.

      :param plan: The plan to validate

      :returns: Validation result with issues and suggestions


      .. autolink-examples:: validate_plan
         :collapse:


   .. py:attribute:: llm


   .. py:attribute:: tools


   .. py:attribute:: tools_description
      :value: ''



