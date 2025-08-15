agents.rag.typed.config
=======================

.. py:module:: agents.rag.typed.config


Classes
-------

.. autoapisummary::

   agents.rag.typed.config.TypedRAGConfig


Module Contents
---------------

.. py:class:: TypedRAGConfig

   Bases: :py:obj:`haive.agents.rag.base.config.BaseRAGConfig`


   Configuration for Typed-RAG with specialized handlers.


   .. autolink-examples:: TypedRAGConfig
      :collapse:

   .. py:attribute:: enable_subqueries
      :type:  bool
      :value: None



   .. py:attribute:: query_classifier_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: retriever_mapping
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: type_handlers
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



