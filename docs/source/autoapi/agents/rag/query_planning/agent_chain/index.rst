
:py:mod:`agents.rag.query_planning.agent_chain`
===============================================

.. py:module:: agents.rag.query_planning.agent_chain

Query Planning RAG using ChainAgent.

Simplified version using the new ChainAgent approach.


.. autolink-examples:: agents.rag.query_planning.agent_chain
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.query_planning.agent_chain.QueryPlan
   agents.rag.query_planning.agent_chain.SubQueryResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryPlan:

   .. graphviz::
      :align: center

      digraph inheritance_QueryPlan {
        node [shape=record];
        "QueryPlan" [label="QueryPlan"];
        "pydantic.BaseModel" -> "QueryPlan";
      }

.. autopydantic_model:: agents.rag.query_planning.agent_chain.QueryPlan
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

   Inheritance diagram for SubQueryResult:

   .. graphviz::
      :align: center

      digraph inheritance_SubQueryResult {
        node [shape=record];
        "SubQueryResult" [label="SubQueryResult"];
        "pydantic.BaseModel" -> "SubQueryResult";
      }

.. autopydantic_model:: agents.rag.query_planning.agent_chain.SubQueryResult
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



Functions
---------

.. autoapisummary::

   agents.rag.query_planning.agent_chain.create_adaptive_planning_chain
   agents.rag.query_planning.agent_chain.create_query_planning_chain
   agents.rag.query_planning.agent_chain.create_simple_decomposition_chain
   agents.rag.query_planning.agent_chain.get_query_planning_chain_io_schema

.. py:function:: create_adaptive_planning_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Adaptive planning based on query complexity.


   .. autolink-examples:: create_adaptive_planning_chain
      :collapse:

.. py:function:: create_query_planning_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Query Planning RAG') -> haive.agents.chain.ChainAgent

   Create query planning RAG using ChainAgent.


   .. autolink-examples:: create_query_planning_chain
      :collapse:

.. py:function:: create_simple_decomposition_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Even simpler version - just decompose and answer.


   .. autolink-examples:: create_simple_decomposition_chain
      :collapse:

.. py:function:: get_query_planning_chain_io_schema() -> dict[str, list[str]]

   Get I/O schema for query planning chain.


   .. autolink-examples:: get_query_planning_chain_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.query_planning.agent_chain
   :collapse:
   
.. autolink-skip:: next
