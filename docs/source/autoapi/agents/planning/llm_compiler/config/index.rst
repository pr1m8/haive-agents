agents.planning.llm_compiler.config
===================================

.. py:module:: agents.planning.llm_compiler.config

.. autoapi-nested-parse::

   Configuration for the LLMCompiler agent using AugLLMConfig system.


   .. autolink-examples:: agents.planning.llm_compiler.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.llm_compiler.config.DEFAULT_CONFIG
   agents.planning.llm_compiler.config.default_joiner_config
   agents.planning.llm_compiler.config.default_planner_config
   agents.planning.llm_compiler.config.default_replanner_config
   agents.planning.llm_compiler.config.joiner_prompt
   agents.planning.llm_compiler.config.planner_prompt
   agents.planning.llm_compiler.config.replanner_prompt


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.config.LLMCompilerAgentConfig


Module Contents
---------------

.. py:class:: LLMCompilerAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   Configuration for the LLM Compiler Agent using AugLLMConfig system.

   The LLM Compiler agent creates a directed acyclic graph (DAG) of tasks
   and executes them in parallel when dependencies are satisfied.


   .. autolink-examples:: LLMCompilerAgentConfig
      :collapse:

   .. py:method:: validate_configs(values) -> Any

      Ensure that the configurations are valid.


      .. autolink-examples:: validate_configs
         :collapse:


   .. py:attribute:: joiner_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_execution_time
      :type:  float
      :value: None



   .. py:attribute:: max_replanning_attempts
      :type:  int
      :value: None



   .. py:attribute:: planner_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: replanner_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: tool_configs
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: tool_instances
      :type:  list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool]
      :value: None



   .. py:attribute:: visualize_graph_output_name
      :type:  str
      :value: None



.. py:data:: DEFAULT_CONFIG

.. py:data:: default_joiner_config

.. py:data:: default_planner_config

.. py:data:: default_replanner_config

.. py:data:: joiner_prompt

.. py:data:: planner_prompt

.. py:data:: replanner_prompt

