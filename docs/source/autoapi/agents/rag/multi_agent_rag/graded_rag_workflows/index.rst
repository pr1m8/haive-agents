
:py:mod:`agents.rag.multi_agent_rag.graded_rag_workflows`
=========================================================

.. py:module:: agents.rag.multi_agent_rag.graded_rag_workflows

Graded RAG Workflows - RAG with comprehensive grading and evaluation.

from typing import Any
This module implements RAG workflows with integrated document grading,
answer quality assessment, and hallucination detection.


.. autolink-examples:: agents.rag.multi_agent_rag.graded_rag_workflows
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows.AdaptiveGradedRAGAgent
   agents.rag.multi_agent_rag.graded_rag_workflows.FullyGradedRAGAgent
   agents.rag.multi_agent_rag.graded_rag_workflows.GradedRAGState
   agents.rag.multi_agent_rag.graded_rag_workflows.MultiCriteriaGradedRAGAgent
   agents.rag.multi_agent_rag.graded_rag_workflows.ReflexiveGradedRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveGradedRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveGradedRAGAgent {
        node [shape=record];
        "AdaptiveGradedRAGAgent" [label="AdaptiveGradedRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "AdaptiveGradedRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows.AdaptiveGradedRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FullyGradedRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_FullyGradedRAGAgent {
        node [shape=record];
        "FullyGradedRAGAgent" [label="FullyGradedRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "FullyGradedRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows.FullyGradedRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GradedRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_GradedRAGState {
        node [shape=record];
        "GradedRAGState" [label="GradedRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "GradedRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows.GradedRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiCriteriaGradedRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiCriteriaGradedRAGAgent {
        node [shape=record];
        "MultiCriteriaGradedRAGAgent" [label="MultiCriteriaGradedRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "MultiCriteriaGradedRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows.MultiCriteriaGradedRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflexiveGradedRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReflexiveGradedRAGAgent {
        node [shape=record];
        "ReflexiveGradedRAGAgent" [label="ReflexiveGradedRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "ReflexiveGradedRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows.ReflexiveGradedRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows.build_custom_graph

.. py:function:: build_custom_graph() -> Any

   Build custom graph for graded RAG workflows.

   This is a utility function for creating custom graphs for
   graded RAG workflows in this module.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.graded_rag_workflows
   :collapse:
   
.. autolink-skip:: next
