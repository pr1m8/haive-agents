agents.rag.fusion.agent
=======================

.. py:module:: agents.rag.fusion.agent

.. autoapi-nested-parse::

   RAG Fusion Agents.

   from typing import Any
   Implementation of RAG Fusion with reciprocal rank fusion for enhanced retrieval.
   Based on the architecture pattern from rag-architectures-flows.md.


   .. autolink-examples:: agents.rag.fusion.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.fusion.agent.FUSION_ANSWER_PROMPT
   agents.rag.fusion.agent.QUERY_EXPANSION_FUSION_PROMPT
   agents.rag.fusion.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.fusion.agent.FusionResult
   agents.rag.fusion.agent.MultiQueryRetrievalAgent
   agents.rag.fusion.agent.QueryVariationsFusion
   agents.rag.fusion.agent.RAGFusionAgent
   agents.rag.fusion.agent.ReciprocalRankFusionAgent


Functions
---------

.. autoapisummary::

   agents.rag.fusion.agent.create_multi_query_retrieval_callable
   agents.rag.fusion.agent.create_rag_fusion_agent
   agents.rag.fusion.agent.get_rag_fusion_io_schema


Module Contents
---------------

.. py:class:: FusionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Results from reciprocal rank fusion.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FusionResult
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: consensus_level
      :type:  float
      :value: None



   .. py:attribute:: diversity_score
      :type:  float
      :value: None



   .. py:attribute:: fused_ranking
      :type:  list[str]
      :value: None



   .. py:attribute:: fusion_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: original_rankings
      :type:  dict[str, list[str]]
      :value: None



.. py:class:: MultiQueryRetrievalAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that uses a callable node for multi-query retrieval - proper Pydantic approach.


   .. autolink-examples:: MultiQueryRetrievalAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build multi-query retrieval graph with callable node using Pydantic fields.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: embedding_model
      :type:  str | None
      :value: None



   .. py:attribute:: max_docs_per_query
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Multi-Query Retrieval'



.. py:class:: QueryVariationsFusion(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Enhanced query variations for fusion.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryVariationsFusion
      :collapse:

   .. py:attribute:: context_variations
      :type:  list[str]
      :value: None



   .. py:attribute:: expected_overlap
      :type:  float
      :value: None



   .. py:attribute:: fusion_strategy
      :type:  str
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: semantic_variations
      :type:  list[str]
      :value: None



   .. py:attribute:: syntactic_variations
      :type:  list[str]
      :value: None



.. py:class:: RAGFusionAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete RAG Fusion agent with query expansion and RRF.


   .. autolink-examples:: RAGFusionAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, num_variations: int = 3, k_parameter: float = 60.0, **kwargs)
      :classmethod:


      Create RAG Fusion agent from documents.

      :param documents: Documents to index
      :param llm_config: LLM configuration
      :param embedding_model: Embedding model for retrieval
      :param num_variations: Number of query variations to generate
      :param k_parameter: RRF k parameter
      :param \*\*kwargs: Additional arguments

      :returns: RAGFusionAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: ReciprocalRankFusionAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that performs reciprocal rank fusion on multiple retrieval results.


   .. autolink-examples:: ReciprocalRankFusionAgent
      :collapse:

   .. py:method:: _build_doc_lookup(retrieval_results: dict[str, list[langchain_core.documents.Document]]) -> dict[str, langchain_core.documents.Document]

      Build lookup from doc ID to document.


      .. autolink-examples:: _build_doc_lookup
         :collapse:


   .. py:method:: _calculate_confidence(retrieval_results: dict[str, list[langchain_core.documents.Document]]) -> float

      Calculate confidence in fusion results.


      .. autolink-examples:: _calculate_confidence
         :collapse:


   .. py:method:: _calculate_consensus(retrieval_results: dict[str, list[langchain_core.documents.Document]]) -> float

      Calculate consensus level across queries.


      .. autolink-examples:: _calculate_consensus
         :collapse:


   .. py:method:: _calculate_diversity(retrieval_results: dict[str, list[langchain_core.documents.Document]]) -> float

      Calculate diversity of retrieval results.


      .. autolink-examples:: _calculate_diversity
         :collapse:


   .. py:method:: _calculate_rrf_scores(retrieval_results: dict[str, list[langchain_core.documents.Document]]) -> dict[str, float]

      Calculate RRF scores for all documents.


      .. autolink-examples:: _calculate_rrf_scores
         :collapse:


   .. py:method:: _doc_id(doc: langchain_core.documents.Document) -> str

      Generate unique ID for document.


      .. autolink-examples:: _doc_id
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build RRF fusion graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: k_parameter
      :type:  float
      :value: None



   .. py:attribute:: min_consensus
      :type:  float
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Reciprocal Rank Fusion'



.. py:function:: create_multi_query_retrieval_callable(documents: list[langchain_core.documents.Document], embedding_model: str | None = None, max_docs_per_query: int = 10)

   Create a callable function for multi-query retrieval that can be used as a graph node.


   .. autolink-examples:: create_multi_query_retrieval_callable
      :collapse:

.. py:function:: create_rag_fusion_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, fusion_type: str = 'standard', **kwargs) -> RAGFusionAgent

   Create a RAG Fusion agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param fusion_type: Type of fusion ("standard", "aggressive", "conservative")
   :param \*\*kwargs: Additional arguments

   :returns: Configured RAG Fusion agent


   .. autolink-examples:: create_rag_fusion_agent
      :collapse:

.. py:function:: get_rag_fusion_io_schema() -> dict[str, list[str]]

   Get I/O schema for RAG Fusion agents.


   .. autolink-examples:: get_rag_fusion_io_schema
      :collapse:

.. py:data:: FUSION_ANSWER_PROMPT

.. py:data:: QUERY_EXPANSION_FUSION_PROMPT

.. py:data:: logger

