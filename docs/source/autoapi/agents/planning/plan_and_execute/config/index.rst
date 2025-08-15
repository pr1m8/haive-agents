agents.planning.plan_and_execute.config
=======================================

.. py:module:: agents.planning.plan_and_execute.config


Classes
-------

.. autoapisummary::

   agents.planning.plan_and_execute.config.PlanAndExecuteConfig


Module Contents
---------------

.. py:class:: PlanAndExecuteConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   .. py:attribute:: agent_executor_config
      :type:  haive.agents.react.config.ReactAgentConfig
      :value: None



   .. py:attribute:: aug_llm_configs
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: default_input_schema
      :type:  dict[str, list]


   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel] | list[pydantic.BaseModel]


