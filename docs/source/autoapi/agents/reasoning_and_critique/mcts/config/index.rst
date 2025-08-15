agents.reasoning_and_critique.mcts.config
=========================================

.. py:module:: agents.reasoning_and_critique.mcts.config


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.config.MCTSAgentConfig


Module Contents
---------------

.. py:class:: MCTSAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for MCTS Agent.


   .. autolink-examples:: MCTSAgentConfig
      :collapse:

   .. py:method:: from_llm_and_tools(llm_config: haive.core.models.llm.base.LLMConfig | None = None, tools: list[langchain_core.tools.BaseTool] | None = None, system_prompt: str | None = None, **kwargs) -> MCTSAgentConfig
      :classmethod:


      Create an MCTS Agent config from LLM config and tools.


      .. autolink-examples:: from_llm_and_tools
         :collapse:


   .. py:attribute:: candidates_per_rollout
      :type:  int
      :value: None



   .. py:attribute:: expansion_prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: exploration_weight
      :type:  float
      :value: None



   .. py:attribute:: initial_prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig | None
      :value: None



   .. py:attribute:: max_rollouts
      :type:  int
      :value: None



   .. py:attribute:: reflection_prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



