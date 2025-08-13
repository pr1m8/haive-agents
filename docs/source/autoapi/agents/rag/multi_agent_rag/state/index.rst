
:py:mod:`agents.rag.multi_agent_rag.state`
==========================================

.. py:module:: agents.rag.multi_agent_rag.state

Enhanced RAG State Schema for Multi-Agent RAG Systems.

This module provides comprehensive state management for complex RAG workflows,
supporting document processing, grading, multi-step retrieval, and conditional routing.


.. autolink-examples:: agents.rag.multi_agent_rag.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.state.DocumentGradingResult
   agents.rag.multi_agent_rag.state.MultiAgentRAGState
   agents.rag.multi_agent_rag.state.QueryStatus
   agents.rag.multi_agent_rag.state.RAGOperationType
   agents.rag.multi_agent_rag.state.RAGStep


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGradingResult:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGradingResult {
        node [shape=record];
        "DocumentGradingResult" [label="DocumentGradingResult"];
        "pydantic.BaseModel" -> "DocumentGradingResult";
      }

.. autopydantic_model:: agents.rag.multi_agent_rag.state.DocumentGradingResult
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

   Inheritance diagram for MultiAgentRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentRAGState {
        node [shape=record];
        "MultiAgentRAGState" [label="MultiAgentRAGState"];
        "haive.core.schema.state_schema.StateSchema" -> "MultiAgentRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.state.MultiAgentRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryStatus:

   .. graphviz::
      :align: center

      digraph inheritance_QueryStatus {
        node [shape=record];
        "QueryStatus" [label="QueryStatus"];
        "str" -> "QueryStatus";
        "enum.Enum" -> "QueryStatus";
      }

.. autoclass:: agents.rag.multi_agent_rag.state.QueryStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryStatus** is an Enum defined in ``agents.rag.multi_agent_rag.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGOperationType:

   .. graphviz::
      :align: center

      digraph inheritance_RAGOperationType {
        node [shape=record];
        "RAGOperationType" [label="RAGOperationType"];
        "str" -> "RAGOperationType";
        "enum.Enum" -> "RAGOperationType";
      }

.. autoclass:: agents.rag.multi_agent_rag.state.RAGOperationType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGOperationType** is an Enum defined in ``agents.rag.multi_agent_rag.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGStep:

   .. graphviz::
      :align: center

      digraph inheritance_RAGStep {
        node [shape=record];
        "RAGStep" [label="RAGStep"];
        "pydantic.BaseModel" -> "RAGStep";
      }

.. autopydantic_model:: agents.rag.multi_agent_rag.state.RAGStep
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





.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.state
   :collapse:
   
.. autolink-skip:: next
