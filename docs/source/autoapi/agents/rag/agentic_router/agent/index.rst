
:py:mod:`agents.rag.agentic_router.agent`
=========================================

.. py:module:: agents.rag.agentic_router.agent

Agentic RAG Router with ReAct Pattern Agents.

from typing import Any
Implementation of autonomous RAG routing using ReAct (Reason + Act) patterns.
Provides intelligent agent selection, strategy planning, and execution coordination.


.. autolink-examples:: agents.rag.agentic_router.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.agentic_router.agent.AgenticRAGRouterAgent
   agents.rag.agentic_router.agent.AgenticRouterResult
   agents.rag.agentic_router.agent.ExecutionResult
   agents.rag.agentic_router.agent.RAGStrategy
   agents.rag.agentic_router.agent.ReActPlan
   agents.rag.agentic_router.agent.ReasoningStep


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGRouterAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGRouterAgent {
        node [shape=record];
        "AgenticRAGRouterAgent" [label="AgenticRAGRouterAgent"];
        "haive.agents.base.agent.Agent" -> "AgenticRAGRouterAgent";
      }

.. autoclass:: agents.rag.agentic_router.agent.AgenticRAGRouterAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRouterResult:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRouterResult {
        node [shape=record];
        "AgenticRouterResult" [label="AgenticRouterResult"];
        "pydantic.BaseModel" -> "AgenticRouterResult";
      }

.. autopydantic_model:: agents.rag.agentic_router.agent.AgenticRouterResult
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

   Inheritance diagram for ExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionResult {
        node [shape=record];
        "ExecutionResult" [label="ExecutionResult"];
        "pydantic.BaseModel" -> "ExecutionResult";
      }

.. autopydantic_model:: agents.rag.agentic_router.agent.ExecutionResult
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

   Inheritance diagram for RAGStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RAGStrategy {
        node [shape=record];
        "RAGStrategy" [label="RAGStrategy"];
        "str" -> "RAGStrategy";
        "enum.Enum" -> "RAGStrategy";
      }

.. autoclass:: agents.rag.agentic_router.agent.RAGStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGStrategy** is an Enum defined in ``agents.rag.agentic_router.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReActPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReActPlan {
        node [shape=record];
        "ReActPlan" [label="ReActPlan"];
        "pydantic.BaseModel" -> "ReActPlan";
      }

.. autopydantic_model:: agents.rag.agentic_router.agent.ReActPlan
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

   Inheritance diagram for ReasoningStep:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningStep {
        node [shape=record];
        "ReasoningStep" [label="ReasoningStep"];
        "pydantic.BaseModel" -> "ReasoningStep";
      }

.. autopydantic_model:: agents.rag.agentic_router.agent.ReasoningStep
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

   agents.rag.agentic_router.agent.create_agentic_rag_router_agent
   agents.rag.agentic_router.agent.get_agentic_rag_router_io_schema

.. py:function:: create_agentic_rag_router_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, routing_mode: str = 'autonomous', **kwargs) -> AgenticRAGRouterAgent

   Create an Agentic RAG Router agent.

   :param documents: Documents for RAG strategies
   :param llm_config: LLM configuration
   :param routing_mode: Routing mode ("conservative", "balanced", "autonomous")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Agentic RAG Router agent


   .. autolink-examples:: create_agentic_rag_router_agent
      :collapse:

.. py:function:: get_agentic_rag_router_io_schema() -> dict[str, list[str]]

   Get I/O schema for Agentic RAG Router agents.


   .. autolink-examples:: get_agentic_rag_router_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic_router.agent
   :collapse:
   
.. autolink-skip:: next
