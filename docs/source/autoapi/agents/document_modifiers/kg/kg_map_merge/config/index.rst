agents.document_modifiers.kg.kg_map_merge.config
================================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.config


Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.config.ParallelKGAgentConfig
   agents.document_modifiers.kg.kg_map_merge.config.ParallelKGTransformerConfig


Module Contents
---------------

.. py:class:: ParallelKGAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Parallel Knowledge Graph Agent with structured extraction.


   .. autolink-examples:: ParallelKGAgentConfig
      :collapse:

   .. py:attribute:: contents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: kg_extraction_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_parallel_workers
      :type:  int
      :value: None



   .. py:attribute:: merge_analysis_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: schema_extraction_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



.. py:class:: ParallelKGTransformerConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Parallel Knowledge Graph Transformer.


   .. autolink-examples:: ParallelKGTransformerConfig
      :collapse:

   .. py:attribute:: checkpoint_mode
      :type:  str
      :value: None



   .. py:attribute:: contents
      :type:  list[langchain_core.documents.Document]


   .. py:attribute:: graph_extraction_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: graph_merge_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



