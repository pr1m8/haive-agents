agents.planning.plan_execute_v3.config
======================================

.. py:module:: agents.planning.plan_execute_v3.config

.. autoapi-nested-parse::

   Configuration for Plan-and-Execute V3 Agent.

   This module defines configuration options for the Plan-and-Execute V3 agent.


   .. autolink-examples:: agents.planning.plan_execute_v3.config
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.config.PlanExecuteV3Config


Module Contents
---------------

.. py:class:: PlanExecuteV3Config(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Plan-and-Execute V3 agent.

   .. attribute:: max_steps

      Maximum number of steps allowed in a plan

   .. attribute:: max_retries

      Maximum retry attempts per step

   .. attribute:: timeout_per_step

      Timeout in seconds for each step

   .. attribute:: parallel_execution

      Enable parallel step execution

   .. attribute:: validate_plan

      Validate plan before execution

   .. attribute:: replan_on_failure

      Automatically replan on execution failure

   .. attribute:: enable_monitoring

      Enable execution monitoring

   .. attribute:: max_replanning_attempts

      Maximum replanning attempts

   .. attribute:: verbose

      Enable verbose logging

   .. attribute:: save_execution_history

      Save execution history to state

   .. attribute:: step_result_in_context

      Store step results in shared context

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanExecuteV3Config
      :collapse:

   .. py:method:: get_execution_temperature(default: float) -> float

      Get execution temperature or use default.


      .. autolink-examples:: get_execution_temperature
         :collapse:


   .. py:method:: get_planning_temperature(default: float) -> float

      Get planning temperature or use default.


      .. autolink-examples:: get_planning_temperature
         :collapse:


   .. py:attribute:: enable_monitoring
      :type:  bool
      :value: None



   .. py:attribute:: execution_temperature
      :type:  float | None
      :value: None



   .. py:attribute:: max_replanning_attempts
      :type:  int
      :value: None



   .. py:attribute:: max_retries
      :type:  int
      :value: None



   .. py:attribute:: max_steps
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: parallel_execution
      :type:  bool
      :value: None



   .. py:attribute:: planning_temperature
      :type:  float | None
      :value: None



   .. py:attribute:: prefer_parallel_tools
      :type:  bool
      :value: None



   .. py:attribute:: replan_on_failure
      :type:  bool
      :value: None



   .. py:attribute:: save_execution_history
      :type:  bool
      :value: None



   .. py:attribute:: step_result_in_context
      :type:  bool
      :value: None



   .. py:attribute:: timeout_per_step
      :type:  float
      :value: None



   .. py:attribute:: tool_timeout_override
      :type:  float | None
      :value: None



   .. py:attribute:: validate_plan
      :type:  bool
      :value: None



   .. py:attribute:: verbose
      :type:  bool
      :value: None



