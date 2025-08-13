
:py:mod:`agents.rag.adaptive_tools.agent`
=========================================

.. py:module:: agents.rag.adaptive_tools.agent

Adaptive RAG with Tools Integration Agents.

from typing import Any
Implementation of adaptive RAG with tool integration and ReAct patterns.
Includes Google Search integration, tool selection, and dynamic routing based on query needs.


.. autolink-examples:: agents.rag.adaptive_tools.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.adaptive_tools.agent.AdaptiveToolsRAGAgent
   agents.rag.adaptive_tools.agent.AdaptiveToolsResult
   agents.rag.adaptive_tools.agent.QueryNeed
   agents.rag.adaptive_tools.agent.SearchIntegrationAgent
   agents.rag.adaptive_tools.agent.SearchResult
   agents.rag.adaptive_tools.agent.ToolSelection
   agents.rag.adaptive_tools.agent.ToolSelectionAgent
   agents.rag.adaptive_tools.agent.ToolType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveToolsRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveToolsRAGAgent {
        node [shape=record];
        "AdaptiveToolsRAGAgent" [label="AdaptiveToolsRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "AdaptiveToolsRAGAgent";
      }

.. autoclass:: agents.rag.adaptive_tools.agent.AdaptiveToolsRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveToolsResult:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveToolsResult {
        node [shape=record];
        "AdaptiveToolsResult" [label="AdaptiveToolsResult"];
        "pydantic.BaseModel" -> "AdaptiveToolsResult";
      }

.. autopydantic_model:: agents.rag.adaptive_tools.agent.AdaptiveToolsResult
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

   Inheritance diagram for QueryNeed:

   .. graphviz::
      :align: center

      digraph inheritance_QueryNeed {
        node [shape=record];
        "QueryNeed" [label="QueryNeed"];
        "str" -> "QueryNeed";
        "enum.Enum" -> "QueryNeed";
      }

.. autoclass:: agents.rag.adaptive_tools.agent.QueryNeed
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryNeed** is an Enum defined in ``agents.rag.adaptive_tools.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SearchIntegrationAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SearchIntegrationAgent {
        node [shape=record];
        "SearchIntegrationAgent" [label="SearchIntegrationAgent"];
        "haive.agents.base.agent.Agent" -> "SearchIntegrationAgent";
      }

.. autoclass:: agents.rag.adaptive_tools.agent.SearchIntegrationAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SearchResult:

   .. graphviz::
      :align: center

      digraph inheritance_SearchResult {
        node [shape=record];
        "SearchResult" [label="SearchResult"];
        "pydantic.BaseModel" -> "SearchResult";
      }

.. autopydantic_model:: agents.rag.adaptive_tools.agent.SearchResult
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

   Inheritance diagram for ToolSelection:

   .. graphviz::
      :align: center

      digraph inheritance_ToolSelection {
        node [shape=record];
        "ToolSelection" [label="ToolSelection"];
        "pydantic.BaseModel" -> "ToolSelection";
      }

.. autopydantic_model:: agents.rag.adaptive_tools.agent.ToolSelection
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

   Inheritance diagram for ToolSelectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ToolSelectionAgent {
        node [shape=record];
        "ToolSelectionAgent" [label="ToolSelectionAgent"];
        "haive.agents.base.agent.Agent" -> "ToolSelectionAgent";
      }

.. autoclass:: agents.rag.adaptive_tools.agent.ToolSelectionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolType:

   .. graphviz::
      :align: center

      digraph inheritance_ToolType {
        node [shape=record];
        "ToolType" [label="ToolType"];
        "str" -> "ToolType";
        "enum.Enum" -> "ToolType";
      }

.. autoclass:: agents.rag.adaptive_tools.agent.ToolType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ToolType** is an Enum defined in ``agents.rag.adaptive_tools.agent``.



Functions
---------

.. autoapisummary::

   agents.rag.adaptive_tools.agent.create_adaptive_synthesis_callable
   agents.rag.adaptive_tools.agent.create_adaptive_tools_rag_agent
   agents.rag.adaptive_tools.agent.create_google_search_callable
   agents.rag.adaptive_tools.agent.create_tool_selector_callable
   agents.rag.adaptive_tools.agent.get_adaptive_tools_rag_io_schema

.. py:function:: create_adaptive_synthesis_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for adaptive synthesis.


   .. autolink-examples:: create_adaptive_synthesis_callable
      :collapse:

.. py:function:: create_adaptive_tools_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, tools_mode: str = 'full', **kwargs) -> AdaptiveToolsRAGAgent

   Create an Adaptive Tools RAG agent.

   :param documents: Documents for local retrieval
   :param llm_config: LLM configuration
   :param tools_mode: Tools mode ("full", "search_only", "local_only")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Adaptive Tools RAG agent


   .. autolink-examples:: create_adaptive_tools_rag_agent
      :collapse:

.. py:function:: create_google_search_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for Google search integration.


   .. autolink-examples:: create_google_search_callable
      :collapse:

.. py:function:: create_tool_selector_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for tool selection.


   .. autolink-examples:: create_tool_selector_callable
      :collapse:

.. py:function:: get_adaptive_tools_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Adaptive Tools RAG agents.


   .. autolink-examples:: get_adaptive_tools_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.adaptive_tools.agent
   :collapse:
   
.. autolink-skip:: next
