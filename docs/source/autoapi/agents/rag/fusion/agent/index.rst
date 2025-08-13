
:py:mod:`agents.rag.fusion.agent`
=================================

.. py:module:: agents.rag.fusion.agent

RAG Fusion Agents.

from typing import Any
Implementation of RAG Fusion with reciprocal rank fusion for enhanced retrieval.
Based on the architecture pattern from rag-architectures-flows.md.


.. autolink-examples:: agents.rag.fusion.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.fusion.agent.FusionResult
   agents.rag.fusion.agent.MultiQueryRetrievalAgent
   agents.rag.fusion.agent.QueryVariationsFusion
   agents.rag.fusion.agent.RAGFusionAgent
   agents.rag.fusion.agent.ReciprocalRankFusionAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FusionResult:

   .. graphviz::
      :align: center

      digraph inheritance_FusionResult {
        node [shape=record];
        "FusionResult" [label="FusionResult"];
        "pydantic.BaseModel" -> "FusionResult";
      }

.. autopydantic_model:: agents.rag.fusion.agent.FusionResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiQueryRetrievalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiQueryRetrievalAgent {
        node [shape=record];
        "MultiQueryRetrievalAgent" [label="MultiQueryRetrievalAgent"];
        "haive.agents.base.agent.Agent" -> "MultiQueryRetrievalAgent";
      }

.. autoclass:: agents.rag.fusion.agent.MultiQueryRetrievalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryVariationsFusion:

   .. graphviz::
      :align: center

      digraph inheritance_QueryVariationsFusion {
        node [shape=record];
        "QueryVariationsFusion" [label="QueryVariationsFusion"];
        "pydantic.BaseModel" -> "QueryVariationsFusion";
      }

.. autopydantic_model:: agents.rag.fusion.agent.QueryVariationsFusion
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGFusionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RAGFusionAgent {
        node [shape=record];
        "RAGFusionAgent" [label="RAGFusionAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "RAGFusionAgent";
      }

.. autoclass:: agents.rag.fusion.agent.RAGFusionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReciprocalRankFusionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReciprocalRankFusionAgent {
        node [shape=record];
        "ReciprocalRankFusionAgent" [label="ReciprocalRankFusionAgent"];
        "haive.agents.base.agent.Agent" -> "ReciprocalRankFusionAgent";
      }

.. autoclass:: agents.rag.fusion.agent.ReciprocalRankFusionAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.fusion.agent.create_multi_query_retrieval_callable
   agents.rag.fusion.agent.create_rag_fusion_agent
   agents.rag.fusion.agent.get_rag_fusion_io_schema

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.fusion.agent
   :collapse:
   
.. autolink-skip:: next
