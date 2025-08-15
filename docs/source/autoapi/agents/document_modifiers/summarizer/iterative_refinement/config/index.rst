agents.document_modifiers.summarizer.iterative_refinement.config
================================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement.config


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.config.IterativeSummarizerConfig


Module Contents
---------------

.. py:class:: IterativeSummarizerConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   The configuration for the iterative summarizer.


   .. autolink-examples:: IterativeSummarizerConfig
      :collapse:

   .. py:attribute:: checkpoint_mode
      :type:  str
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: input_schema
      :type:  haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerInput
      :value: None



   .. py:attribute:: output_schema
      :type:  haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerOutput
      :value: None



   .. py:attribute:: state_schema
      :type:  haive.agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState
      :value: None



