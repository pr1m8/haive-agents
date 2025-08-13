
:py:mod:`agents.rag.simple.enhanced_v3.state`
=============================================

.. py:module:: agents.rag.simple.enhanced_v3.state

Enhanced RAG State Schema for SimpleRAG V3.

This module provides enhanced state management for SimpleRAG using Enhanced MultiAgent V3
with performance tracking, debug information, and comprehensive metadata.


.. autolink-examples:: agents.rag.simple.enhanced_v3.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.state.GenerationDebugInfo
   agents.rag.simple.enhanced_v3.state.RAGMetadata
   agents.rag.simple.enhanced_v3.state.RetrievalDebugInfo
   agents.rag.simple.enhanced_v3.state.SimpleRAGState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GenerationDebugInfo:

   .. graphviz::
      :align: center

      digraph inheritance_GenerationDebugInfo {
        node [shape=record];
        "GenerationDebugInfo" [label="GenerationDebugInfo"];
        "pydantic.BaseModel" -> "GenerationDebugInfo";
      }

.. autopydantic_model:: agents.rag.simple.enhanced_v3.state.GenerationDebugInfo
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

   Inheritance diagram for RAGMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_RAGMetadata {
        node [shape=record];
        "RAGMetadata" [label="RAGMetadata"];
        "pydantic.BaseModel" -> "RAGMetadata";
      }

.. autopydantic_model:: agents.rag.simple.enhanced_v3.state.RAGMetadata
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

   Inheritance diagram for RetrievalDebugInfo:

   .. graphviz::
      :align: center

      digraph inheritance_RetrievalDebugInfo {
        node [shape=record];
        "RetrievalDebugInfo" [label="RetrievalDebugInfo"];
        "pydantic.BaseModel" -> "RetrievalDebugInfo";
      }

.. autopydantic_model:: agents.rag.simple.enhanced_v3.state.RetrievalDebugInfo
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

   Inheritance diagram for SimpleRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGState {
        node [shape=record];
        "SimpleRAGState" [label="SimpleRAGState"];
        "haive.core.schema.state_schema.StateSchema" -> "SimpleRAGState";
      }

.. autoclass:: agents.rag.simple.enhanced_v3.state.SimpleRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.simple.enhanced_v3.state
   :collapse:
   
.. autolink-skip:: next
