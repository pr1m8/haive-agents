
:py:mod:`agents.rag.multi_agent_rag.additional_workflows`
=========================================================

.. py:module:: agents.rag.multi_agent_rag.additional_workflows

Additional RAG Workflows - Extended Multi-Agent RAG Implementations.

from typing import Any
This module implements additional RAG architectures beyond the simple enhanced workflows,
including memory-based, multi-query, fusion, and advanced reasoning patterns.


.. autolink-examples:: agents.rag.multi_agent_rag.additional_workflows
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.additional_workflows.MemoryRAGState
   agents.rag.multi_agent_rag.additional_workflows.MultiQueryRAGAgent
   agents.rag.multi_agent_rag.additional_workflows.MultiQueryRAGState
   agents.rag.multi_agent_rag.additional_workflows.QueryDecompositionRAGAgent
   agents.rag.multi_agent_rag.additional_workflows.RAGFusionAgent
   agents.rag.multi_agent_rag.additional_workflows.SelfRAGAgent
   agents.rag.multi_agent_rag.additional_workflows.SelfRAGState
   agents.rag.multi_agent_rag.additional_workflows.SimpleRAGWithMemoryAgent
   agents.rag.multi_agent_rag.additional_workflows.StepBackPromptingRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryRAGState {
        node [shape=record];
        "MemoryRAGState" [label="MemoryRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "MemoryRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.MemoryRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiQueryRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiQueryRAGAgent {
        node [shape=record];
        "MultiQueryRAGAgent" [label="MultiQueryRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "MultiQueryRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.MultiQueryRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiQueryRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiQueryRAGState {
        node [shape=record];
        "MultiQueryRAGState" [label="MultiQueryRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "MultiQueryRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.MultiQueryRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryDecompositionRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryDecompositionRAGAgent {
        node [shape=record];
        "QueryDecompositionRAGAgent" [label="QueryDecompositionRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "QueryDecompositionRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.QueryDecompositionRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGFusionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RAGFusionAgent {
        node [shape=record];
        "RAGFusionAgent" [label="RAGFusionAgent"];
        "haive.agents.multi.base.MultiAgent" -> "RAGFusionAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.RAGFusionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfRAGAgent {
        node [shape=record];
        "SelfRAGAgent" [label="SelfRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "SelfRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.SelfRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_SelfRAGState {
        node [shape=record];
        "SelfRAGState" [label="SelfRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "SelfRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.SelfRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleRAGWithMemoryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleRAGWithMemoryAgent {
        node [shape=record];
        "SimpleRAGWithMemoryAgent" [label="SimpleRAGWithMemoryAgent"];
        "haive.agents.multi.base.MultiAgent" -> "SimpleRAGWithMemoryAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.SimpleRAGWithMemoryAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepBackPromptingRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StepBackPromptingRAGAgent {
        node [shape=record];
        "StepBackPromptingRAGAgent" [label="StepBackPromptingRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "StepBackPromptingRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.additional_workflows.StepBackPromptingRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.additional_workflows.build_custom_graph

.. py:function:: build_custom_graph() -> Any

   Build custom graph for additional workflows.

   This is a utility function for creating custom graphs for
   advanced RAG workflows in this module.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.additional_workflows
   :collapse:
   
.. autolink-skip:: next
