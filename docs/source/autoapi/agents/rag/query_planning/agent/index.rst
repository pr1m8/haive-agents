
:py:mod:`agents.rag.query_planning.agent`
=========================================

.. py:module:: agents.rag.query_planning.agent

Query Planning Agentic RAG Agent.

from typing import Any
Implementation of query planning RAG with structured decomposition and execution.
Provides intelligent query analysis, planning, and multi-stage retrieval strategies.


.. autolink-examples:: agents.rag.query_planning.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.query_planning.agent.QueryComplexity
   agents.rag.query_planning.agent.QueryPlan
   agents.rag.query_planning.agent.QueryPlanningRAGAgent
   agents.rag.query_planning.agent.QueryPlanningResult
   agents.rag.query_planning.agent.QueryType
   agents.rag.query_planning.agent.SubQuery
   agents.rag.query_planning.agent.SubQueryResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryComplexity:

   .. graphviz::
      :align: center

      digraph inheritance_QueryComplexity {
        node [shape=record];
        "QueryComplexity" [label="QueryComplexity"];
        "str" -> "QueryComplexity";
        "enum.Enum" -> "QueryComplexity";
      }

.. autoclass:: agents.rag.query_planning.agent.QueryComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryComplexity** is an Enum defined in ``agents.rag.query_planning.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryPlan:

   .. graphviz::
      :align: center

      digraph inheritance_QueryPlan {
        node [shape=record];
        "QueryPlan" [label="QueryPlan"];
        "pydantic.BaseModel" -> "QueryPlan";
      }

.. autopydantic_model:: agents.rag.query_planning.agent.QueryPlan
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

   Inheritance diagram for QueryPlanningRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryPlanningRAGAgent {
        node [shape=record];
        "QueryPlanningRAGAgent" [label="QueryPlanningRAGAgent"];
        "haive.agents.base.agent.Agent" -> "QueryPlanningRAGAgent";
      }

.. autoclass:: agents.rag.query_planning.agent.QueryPlanningRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryPlanningResult:

   .. graphviz::
      :align: center

      digraph inheritance_QueryPlanningResult {
        node [shape=record];
        "QueryPlanningResult" [label="QueryPlanningResult"];
        "pydantic.BaseModel" -> "QueryPlanningResult";
      }

.. autopydantic_model:: agents.rag.query_planning.agent.QueryPlanningResult
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

   Inheritance diagram for QueryType:

   .. graphviz::
      :align: center

      digraph inheritance_QueryType {
        node [shape=record];
        "QueryType" [label="QueryType"];
        "str" -> "QueryType";
        "enum.Enum" -> "QueryType";
      }

.. autoclass:: agents.rag.query_planning.agent.QueryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryType** is an Enum defined in ``agents.rag.query_planning.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SubQuery:

   .. graphviz::
      :align: center

      digraph inheritance_SubQuery {
        node [shape=record];
        "SubQuery" [label="SubQuery"];
        "pydantic.BaseModel" -> "SubQuery";
      }

.. autopydantic_model:: agents.rag.query_planning.agent.SubQuery
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

.. autopydantic_model:: agents.rag.query_planning.agent.SubQueryResult
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

   agents.rag.query_planning.agent.create_query_planning_rag_agent
   agents.rag.query_planning.agent.get_query_planning_rag_io_schema

.. py:function:: create_query_planning_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, planning_mode: str = 'comprehensive', **kwargs) -> QueryPlanningRAGAgent

   Create a Query Planning RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param planning_mode: Planning mode ("simple", "moderate", "comprehensive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Query Planning RAG agent


   .. autolink-examples:: create_query_planning_rag_agent
      :collapse:

.. py:function:: get_query_planning_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Query Planning RAG agents.


   .. autolink-examples:: get_query_planning_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.query_planning.agent
   :collapse:
   
.. autolink-skip:: next
