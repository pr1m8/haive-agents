agents.rag.multi_strategy.config
================================

.. py:module:: agents.rag.multi_strategy.config


Classes
-------

.. autoapisummary::

   agents.rag.multi_strategy.config.MultiStrategyRAGConfig


Module Contents
---------------

.. py:class:: MultiStrategyRAGConfig

   Bases: :py:obj:`haive.agents.rag.self_corr.config.SelfCorrectiveRAGConfig`


   Configuration for multi-strategy RAG agents.


   .. autolink-examples:: MultiStrategyRAGConfig
      :collapse:

   .. py:attribute:: query_analyzer_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: query_rewriter_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: retriever_strategies
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.agents.rag.multi_strategy.state.MultiStrategyRAGState]
      :value: None



