agents.reasoning_and_critique.lats.config
=========================================

.. py:module:: agents.reasoning_and_critique.lats.config

.. autoapi-nested-parse::

   Configuration for Language Agent Tree Search (LATS) agent.


   .. autolink-examples:: agents.reasoning_and_critique.lats.config
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.config.LATSAgentConfig


Module Contents
---------------

.. py:class:: LATSAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for Language Agent Tree Search (LATS) agent.

   This agent implements a Monte Carlo Tree Search approach to generate
   high-quality responses through exploration and exploitation of different
   action trajectories.


   .. autolink-examples:: LATSAgentConfig
      :collapse:

   .. py:method:: from_llms(reflection_llm: haive.core.engine.aug_llm.AugLLMConfig, action_llm: haive.core.engine.aug_llm.AugLLMConfig, tools: list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool] | None = None, **kwargs) -> LATSAgentConfig
      :classmethod:


      Create a LATS agent configuration from LLM configs.

      :param reflection_llm: LLM configuration for reflection
      :param action_llm: LLM configuration for action generation
      :param tools: Optional list of tools
      :param \*\*kwargs: Additional configuration parameters

      :returns: LATSAgentConfig instance


      .. autolink-examples:: from_llms
         :collapse:


   .. py:attribute:: action_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: exploration_weight
      :type:  float
      :value: None



   .. py:attribute:: input_schema_name
      :type:  str | None
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: n_candidates
      :type:  int
      :value: None



   .. py:attribute:: output_schema_name
      :type:  str | None
      :value: None



   .. py:attribute:: reflection_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool]
      :value: None



