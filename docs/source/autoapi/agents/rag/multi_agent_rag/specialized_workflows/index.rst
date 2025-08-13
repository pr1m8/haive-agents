
:py:mod:`agents.rag.multi_agent_rag.specialized_workflows`
==========================================================

.. py:module:: agents.rag.multi_agent_rag.specialized_workflows

Specialized RAG Workflows - FLARE, Dynamic RAG, and Debate RAG.

This module implements advanced RAG architectures including Forward-Looking Active REtrieval (FLARE),
Dynamic RAG with add/remove retrievers, and Debate-based RAG for multi-perspective reasoning.


.. autolink-examples:: agents.rag.multi_agent_rag.specialized_workflows
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows.AdaptiveThresholdRAGAgent
   agents.rag.multi_agent_rag.specialized_workflows.DebateRAGAgent
   agents.rag.multi_agent_rag.specialized_workflows.DebateRAGState
   agents.rag.multi_agent_rag.specialized_workflows.DynamicRAGAgent
   agents.rag.multi_agent_rag.specialized_workflows.DynamicRAGState
   agents.rag.multi_agent_rag.specialized_workflows.FLAREAgent
   agents.rag.multi_agent_rag.specialized_workflows.FLAREState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveThresholdRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveThresholdRAGAgent {
        node [shape=record];
        "AdaptiveThresholdRAGAgent" [label="AdaptiveThresholdRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "AdaptiveThresholdRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.AdaptiveThresholdRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DebateRAGAgent {
        node [shape=record];
        "DebateRAGAgent" [label="DebateRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "DebateRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.DebateRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_DebateRAGState {
        node [shape=record];
        "DebateRAGState" [label="DebateRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "DebateRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.DebateRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicRAGAgent {
        node [shape=record];
        "DynamicRAGAgent" [label="DynamicRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "DynamicRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.DynamicRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicRAGState {
        node [shape=record];
        "DynamicRAGState" [label="DynamicRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "DynamicRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.DynamicRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREAgent:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREAgent {
        node [shape=record];
        "FLAREAgent" [label="FLAREAgent"];
        "haive.agents.multi.base.MultiAgent" -> "FLAREAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.FLAREAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREState:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREState {
        node [shape=record];
        "FLAREState" [label="FLAREState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "FLAREState";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows.FLAREState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows.build_custom_graph

.. py:function:: build_custom_graph() -> Any

   Build custom graph for specialized workflows.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.specialized_workflows
   :collapse:
   
.. autolink-skip:: next
