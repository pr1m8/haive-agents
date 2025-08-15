agents.rag.filtered.config
==========================

.. py:module:: agents.rag.filtered.config


Classes
-------

.. autoapisummary::

   agents.rag.filtered.config.FilteredRAGConfig


Module Contents
---------------

.. py:class:: FilteredRAGConfig

   Bases: :py:obj:`haive.agents.rag.base.config.BaseRAGConfig`


   Configuration for RAG agents with document filtering capabilities.

   This RAG implementation extends the base RAG with:
   1. Document filtering based on relevance to the query
   2. Configurable relevance threshold to filter out irrelevant documents


   .. autolink-examples:: FilteredRAGConfig
      :collapse:

   .. py:attribute:: answer_generator_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: document_filter_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: relevance_threshold
      :type:  float
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



