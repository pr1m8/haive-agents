agents.planning.llm_compiler_v3.config
======================================

.. py:module:: agents.planning.llm_compiler_v3.config

.. autoapi-nested-parse::

   Configuration models for LLM Compiler V3 Agent.


   .. autolink-examples:: agents.planning.llm_compiler_v3.config
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler_v3.config.LLMCompilerV3Config
   agents.planning.llm_compiler_v3.config.ToolExecutionConfig


Module Contents
---------------

.. py:class:: LLMCompilerV3Config(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for LLM Compiler V3 Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LLMCompilerV3Config
      :collapse:

   .. py:method:: create_execution_config() -> dict[str, Any]

      Create configuration dictionary for execution.


      .. autolink-examples:: create_execution_config
         :collapse:


   .. py:method:: get_engine_for_agent(agent_name: str) -> haive.core.engine.aug_llm.AugLLMConfig

      Get the engine configuration for a specific agent.


      .. autolink-examples:: get_engine_for_agent
         :collapse:


   .. py:method:: get_tool_priority(tool_name: str) -> int

      Get priority for a tool (higher = more preferred).


      .. autolink-examples:: get_tool_priority
         :collapse:


   .. py:method:: should_enable_tool(tool_name: str) -> bool

      Check if a tool should be enabled based on configuration.


      .. autolink-examples:: should_enable_tool
         :collapse:


   .. py:attribute:: custom_settings
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: enable_auto_replan
      :type:  bool
      :value: None



   .. py:attribute:: enable_detailed_logging
      :type:  bool
      :value: None



   .. py:attribute:: enable_execution_tracing
      :type:  bool
      :value: None



   .. py:attribute:: enable_smart_batching
      :type:  bool
      :value: None



   .. py:attribute:: enable_task_caching
      :type:  bool
      :value: None



   .. py:attribute:: exclude_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: execution_mode
      :type:  haive.agents.planning.llm_compiler_v3.models.ExecutionMode
      :value: None



   .. py:attribute:: executor_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: joiner_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: log_task_timings
      :type:  bool
      :value: None



   .. py:attribute:: max_parallel_tasks
      :type:  int
      :value: None



   .. py:attribute:: max_replan_attempts
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parallel_efficiency_target
      :type:  float
      :value: None



   .. py:attribute:: planner_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: replan_on_failure_threshold
      :type:  float
      :value: None



   .. py:attribute:: task_fetcher_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: task_timeout
      :type:  float
      :value: None



   .. py:attribute:: tool_names
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_priorities
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: total_timeout
      :type:  float
      :value: None



.. py:class:: ToolExecutionConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for individual tool execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolExecutionConfig
      :collapse:

   .. py:attribute:: custom_args
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: enable_caching
      :type:  bool
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: retry_attempts
      :type:  int
      :value: None



   .. py:attribute:: timeout
      :type:  float
      :value: None



   .. py:attribute:: tool_name
      :type:  str
      :value: None



