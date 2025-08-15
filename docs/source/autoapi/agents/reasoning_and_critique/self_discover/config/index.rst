agents.reasoning_and_critique.self_discover.config
==================================================

.. py:module:: agents.reasoning_and_critique.self_discover.config


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.config.SelfDiscoverAgentConfig


Module Contents
---------------

.. py:class:: SelfDiscoverAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a SelfDiscover agent.

   This configuration defines all parameters needed to create a SelfDiscover agent:
   - Engines for each stage of the reasoning process
   - State schema for tracking reasoning progress
   - Library of reasoning modules to use


   .. autolink-examples:: SelfDiscoverAgentConfig
      :collapse:

   .. py:method:: _get_default_reasoning_modules() -> list[str]
      :staticmethod:


      Return a default list of reasoning modules.


      .. autolink-examples:: _get_default_reasoning_modules
         :collapse:


   .. py:method:: from_defaults(model: str = 'gpt-4o', temperature: float = 0.0, name: str | None = None, reasoning_modules: list[str] | None = None, select_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, adapt_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, structure_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, reasoning_prompt: str | langchain_core.prompts.ChatPromptTemplate | None = None, **kwargs) -> SelfDiscoverAgentConfig
      :classmethod:


      Create a SelfDiscoverAgentConfig with default settings.

      :param model: Model name to use for all engines
      :param temperature: Temperature setting for all engines
      :param name: Optional name for the agent
      :param reasoning_modules: Optional list of reasoning modules
      :param select_prompt: Optional custom prompt for selection stage
      :param adapt_prompt: Optional custom prompt for adaptation stage
      :param structure_prompt: Optional custom prompt for structure stage
      :param reasoning_prompt: Optional custom prompt for reasoning stage
      :param \*\*kwargs: Additional configuration parameters

      :returns: SelfDiscoverAgentConfig instance


      .. autolink-examples:: from_defaults
         :collapse:


   .. py:attribute:: adapt_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: reasoning_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: reasoning_modules
      :type:  list[str]
      :value: None



   .. py:attribute:: select_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structure_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



