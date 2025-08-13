
:py:mod:`agents.document_modifiers.kg.kg_map_merge.engines`
===========================================================

.. py:module:: agents.document_modifiers.kg.kg_map_merge.engines



Functions
---------

.. autoapisummary::

   agents.document_modifiers.kg.kg_map_merge.engines.create_graph_extraction_config
   agents.document_modifiers.kg.kg_map_merge.engines.create_graph_merger_config
   agents.document_modifiers.kg.kg_map_merge.engines.create_node_extraction_config
   agents.document_modifiers.kg.kg_map_merge.engines.create_parallel_kg_transformer_configs
   agents.document_modifiers.kg.kg_map_merge.engines.create_relationship_extraction_config
   agents.document_modifiers.kg.kg_map_merge.engines.kg_extraction_engine
   agents.document_modifiers.kg.kg_map_merge.engines.main
   agents.document_modifiers.kg.kg_map_merge.engines.merge_analysis_engine
   agents.document_modifiers.kg.kg_map_merge.engines.schema_extraction_engine

.. py:function:: create_graph_extraction_config(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create an AugLLMConfig for comprehensive knowledge graph extraction.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for graph extraction


   .. autolink-examples:: create_graph_extraction_config
      :collapse:

.. py:function:: create_graph_merger_config(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create an AugLLMConfig for merging knowledge graphs.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for graph merging


   .. autolink-examples:: create_graph_merger_config
      :collapse:

.. py:function:: create_node_extraction_config(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create an AugLLMConfig for entity node extraction.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for node extraction


   .. autolink-examples:: create_node_extraction_config
      :collapse:

.. py:function:: create_parallel_kg_transformer_configs() -> dict

   Create a comprehensive set of configurations for the Parallel KG Transformer.

   :returns: Dictionary of AugLLMConfigs


   .. autolink-examples:: create_parallel_kg_transformer_configs
      :collapse:

.. py:function:: create_relationship_extraction_config(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create an AugLLMConfig for relationship extraction.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for relationship extraction


   .. autolink-examples:: create_relationship_extraction_config
      :collapse:

.. py:function:: kg_extraction_engine(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create a comprehensive knowledge graph extraction engine.

   This is the main function for creating a complete KG extraction configuration.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for comprehensive KG extraction


   .. autolink-examples:: kg_extraction_engine
      :collapse:

.. py:function:: main() -> None

.. py:function:: merge_analysis_engine(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create a merge analysis engine for knowledge graph merging.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for merge analysis


   .. autolink-examples:: merge_analysis_engine
      :collapse:

.. py:function:: schema_extraction_engine(model: str = 'gpt-4o', temperature: float = 0.7) -> haive.core.engine.aug_llm.AugLLMConfig

   Create a schema extraction engine for knowledge graph schema analysis.

   :param model: LLM model to use
   :param temperature: Sampling temperature for generation

   :returns: Configured AugLLMConfig for schema extraction


   .. autolink-examples:: schema_extraction_engine
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.kg.kg_map_merge.engines
   :collapse:
   
.. autolink-skip:: next
