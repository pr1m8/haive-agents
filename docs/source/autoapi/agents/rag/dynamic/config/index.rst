agents.rag.dynamic.config
=========================

.. py:module:: agents.rag.dynamic.config


Classes
-------

.. autoapisummary::

   agents.rag.dynamic.config.DynamicRAGConfig


Module Contents
---------------

.. py:class:: DynamicRAGConfig

   Bases: :py:obj:`haive.agents.rag.base.config.BaseRAGConfig`


   Configuration for Dynamic RAG with multiple data sources.


   .. autolink-examples:: DynamicRAGConfig
      :collapse:

   .. py:attribute:: data_sources
      :type:  dict[str, haive.agents.rag.dynamic.data_source_types.DataSourceConfig]
      :value: None



   .. py:attribute:: default_source
      :type:  str | None
      :value: None



   .. py:attribute:: enable_parallel_retrieval
      :type:  bool
      :value: None



   .. py:attribute:: max_sources_per_query
      :type:  int
      :value: None



   .. py:attribute:: query_router_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: result_merger_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



