agents.document_modifiers.summarizer.map_branch.config
======================================================

.. py:module:: agents.document_modifiers.summarizer.map_branch.config


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.config.SummarizerAgentConfig


Module Contents
---------------

.. py:class:: SummarizerAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   .. py:method:: build_agent() -> Any


   .. py:attribute:: checkpoint_mode
      :type:  str
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: input_schema
      :type:  haive.agents.document_modifiers.summarizer.map_branch.state.InputState
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'map_reduce_summarizer_agent'



   .. py:attribute:: output_schema
      :type:  haive.agents.document_modifiers.summarizer.map_branch.state.OutputState
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState
      :value: None



   .. py:attribute:: token_max
      :type:  int
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: True



