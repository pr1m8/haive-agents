agents.rag.self_corr.config
===========================

.. py:module:: agents.rag.self_corr.config


Classes
-------

.. autoapisummary::

   agents.rag.self_corr.config.SelfCorrectiveRAGConfig


Module Contents
---------------

.. py:class:: SelfCorrectiveRAGConfig

   Bases: :py:obj:`haive.agents.rag.base.config.BaseRAGConfig`


   Configuration for self-corrective RAG agents that can evaluate and improve their answers.

   This RAG implementation extends the base RAG with:
   1. Answer evaluation to detect hallucinations
   2. Answer correction to fix identified issues
   3. Iterative improvement until quality threshold is met


   .. autolink-examples:: SelfCorrectiveRAGConfig
      :collapse:

   .. py:attribute:: answer_corrector_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: answer_evaluator_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: document_filter_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: max_correction_iterations
      :type:  int
      :value: None



   .. py:attribute:: minimum_answer_score
      :type:  float
      :value: None



   .. py:attribute:: relevance_threshold
      :type:  float
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



