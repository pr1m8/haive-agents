
:py:mod:`agents.rag.self_route.agent`
=====================================

.. py:module:: agents.rag.self_route.agent

Self-Route RAG Agents.

from typing import Any
Implementation of self-routing RAG with dynamic strategy selection and iterative planning.
Uses structured output models for complex routing decisions and preprocessing.


.. autolink-examples:: agents.rag.self_route.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.self_route.agent.IterativePlan
   agents.rag.self_route.agent.IterativePlannerAgent
   agents.rag.self_route.agent.QueryAnalysis
   agents.rag.self_route.agent.QueryAnalyzerAgent
   agents.rag.self_route.agent.QueryComplexity
   agents.rag.self_route.agent.RoutingDecision
   agents.rag.self_route.agent.RoutingDecisionAgent
   agents.rag.self_route.agent.RoutingStrategy
   agents.rag.self_route.agent.SelfRouteRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativePlan:

   .. graphviz::
      :align: center

      digraph inheritance_IterativePlan {
        node [shape=record];
        "IterativePlan" [label="IterativePlan"];
        "pydantic.BaseModel" -> "IterativePlan";
      }

.. autopydantic_model:: agents.rag.self_route.agent.IterativePlan
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

   Inheritance diagram for IterativePlannerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_IterativePlannerAgent {
        node [shape=record];
        "IterativePlannerAgent" [label="IterativePlannerAgent"];
        "haive.agents.base.agent.Agent" -> "IterativePlannerAgent";
      }

.. autoclass:: agents.rag.self_route.agent.IterativePlannerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_QueryAnalysis {
        node [shape=record];
        "QueryAnalysis" [label="QueryAnalysis"];
        "pydantic.BaseModel" -> "QueryAnalysis";
      }

.. autopydantic_model:: agents.rag.self_route.agent.QueryAnalysis
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

   Inheritance diagram for QueryAnalyzerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryAnalyzerAgent {
        node [shape=record];
        "QueryAnalyzerAgent" [label="QueryAnalyzerAgent"];
        "haive.agents.base.agent.Agent" -> "QueryAnalyzerAgent";
      }

.. autoclass:: agents.rag.self_route.agent.QueryAnalyzerAgent
   :members:
   :undoc-members:
   :show-inheritance:




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

.. autoclass:: agents.rag.self_route.agent.QueryComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryComplexity** is an Enum defined in ``agents.rag.self_route.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingDecision:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingDecision {
        node [shape=record];
        "RoutingDecision" [label="RoutingDecision"];
        "pydantic.BaseModel" -> "RoutingDecision";
      }

.. autopydantic_model:: agents.rag.self_route.agent.RoutingDecision
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

   Inheritance diagram for RoutingDecisionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingDecisionAgent {
        node [shape=record];
        "RoutingDecisionAgent" [label="RoutingDecisionAgent"];
        "haive.agents.base.agent.Agent" -> "RoutingDecisionAgent";
      }

.. autoclass:: agents.rag.self_route.agent.RoutingDecisionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoutingStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingStrategy {
        node [shape=record];
        "RoutingStrategy" [label="RoutingStrategy"];
        "str" -> "RoutingStrategy";
        "enum.Enum" -> "RoutingStrategy";
      }

.. autoclass:: agents.rag.self_route.agent.RoutingStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RoutingStrategy** is an Enum defined in ``agents.rag.self_route.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfRouteRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfRouteRAGAgent {
        node [shape=record];
        "SelfRouteRAGAgent" [label="SelfRouteRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "SelfRouteRAGAgent";
      }

.. autoclass:: agents.rag.self_route.agent.SelfRouteRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.self_route.agent.create_self_route_rag_agent
   agents.rag.self_route.agent.get_self_route_rag_io_schema

.. py:function:: create_self_route_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, routing_mode: str = 'adaptive', **kwargs) -> SelfRouteRAGAgent

   Create a Self-Route RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param routing_mode: Routing mode ("conservative", "adaptive", "aggressive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Self-Route RAG agent


   .. autolink-examples:: create_self_route_rag_agent
      :collapse:

.. py:function:: get_self_route_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Self-Route RAG agents.


   .. autolink-examples:: get_self_route_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.self_route.agent
   :collapse:
   
.. autolink-skip:: next
