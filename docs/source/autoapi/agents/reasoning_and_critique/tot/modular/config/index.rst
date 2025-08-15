agents.reasoning_and_critique.tot.modular.config
================================================

.. py:module:: agents.reasoning_and_critique.tot.modular.config


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.config.ToTAgentConfig


Module Contents
---------------

.. py:class:: ToTAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a Tree of Thoughts agent.

   Tree of Thoughts implements a search algorithm for complex problems by:
   1. Generating multiple candidate solutions
   2. Evaluating those candidates
   3. Pruning to retain only the best candidates
   4. Repeating until a satisfactory solution is found


   .. autolink-examples:: ToTAgentConfig
      :collapse:

   .. py:method:: from_scratch(model: str = 'gpt-4o', temperature: float = 0.7, system_prompt: str = 'You are a helpful assistant solving a complex problem step by step.', expand_prompt: langchain_core.prompts.ChatPromptTemplate | None = None, score_prompt: langchain_core.prompts.ChatPromptTemplate | None = None, name: str | None = None, **kwargs) -> ToTAgentConfig
      :classmethod:


      Create a ToTAgentConfig from scratch.

      :param model: Model name to use
      :param temperature: Temperature for generation
      :param system_prompt: System prompt for the agent
      :param expand_prompt: Optional specific prompt for expansion
      :param score_prompt: Optional specific prompt for scoring
      :param name: Optional agent name
      :param \*\*kwargs: Additional kwargs for the config

      :returns: ToTAgentConfig instance


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:attribute:: beam_size
      :type:  int
      :value: None



   .. py:attribute:: candidates_per_expansion
      :type:  int
      :value: None



   .. py:attribute:: expand_llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: expand_node_name
      :type:  str
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:attribute:: prune_node_name
      :type:  str
      :value: None



   .. py:attribute:: score_function
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: score_llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: score_node_name
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: threshold
      :type:  float
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



