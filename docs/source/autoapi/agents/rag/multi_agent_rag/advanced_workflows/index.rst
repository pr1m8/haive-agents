
:py:mod:`agents.rag.multi_agent_rag.advanced_workflows`
=======================================================

.. py:module:: agents.rag.multi_agent_rag.advanced_workflows

Advanced RAG Workflows - Graph RAG and Agentic RAG Patterns.

This module implements the most sophisticated RAG architectures including
Graph RAG, Agentic routing, speculative execution, and self-routing patterns.


.. autolink-examples:: agents.rag.multi_agent_rag.advanced_workflows
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.advanced_workflows.AgenticGraphRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.AgenticRAGRouterAgent
   agents.rag.multi_agent_rag.advanced_workflows.AgenticRAGState
   agents.rag.multi_agent_rag.advanced_workflows.GraphRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.GraphRAGState
   agents.rag.multi_agent_rag.advanced_workflows.QueryPlanningAgenticRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.SelfReflectiveAgenticRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.SelfRouteRAGAgent
   agents.rag.multi_agent_rag.advanced_workflows.SpeculativeRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticGraphRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticGraphRAGAgent {
        node [shape=record];
        "AgenticGraphRAGAgent" [label="AgenticGraphRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "AgenticGraphRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.AgenticGraphRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGRouterAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGRouterAgent {
        node [shape=record];
        "AgenticRAGRouterAgent" [label="AgenticRAGRouterAgent"];
        "haive.agents.multi.base.MultiAgent" -> "AgenticRAGRouterAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.AgenticRAGRouterAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGState {
        node [shape=record];
        "AgenticRAGState" [label="AgenticRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "AgenticRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.AgenticRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GraphRAGAgent {
        node [shape=record];
        "GraphRAGAgent" [label="GraphRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "GraphRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.GraphRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_GraphRAGState {
        node [shape=record];
        "GraphRAGState" [label="GraphRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "GraphRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.GraphRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryPlanningAgenticRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryPlanningAgenticRAGAgent {
        node [shape=record];
        "QueryPlanningAgenticRAGAgent" [label="QueryPlanningAgenticRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "QueryPlanningAgenticRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.QueryPlanningAgenticRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfReflectiveAgenticRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfReflectiveAgenticRAGAgent {
        node [shape=record];
        "SelfReflectiveAgenticRAGAgent" [label="SelfReflectiveAgenticRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "SelfReflectiveAgenticRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.SelfReflectiveAgenticRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfRouteRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfRouteRAGAgent {
        node [shape=record];
        "SelfRouteRAGAgent" [label="SelfRouteRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "SelfRouteRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.SelfRouteRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SpeculativeRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SpeculativeRAGAgent {
        node [shape=record];
        "SpeculativeRAGAgent" [label="SpeculativeRAGAgent"];
        "haive.agents.multi.base.MultiAgent" -> "SpeculativeRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.advanced_workflows.SpeculativeRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.advanced_workflows.build_custom_graph

.. py:function:: build_custom_graph() -> Any

   Build custom graph for advanced workflows.

   This is a utility function for creating custom graphs for
   advanced RAG workflows in this module.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.advanced_workflows
   :collapse:
   
.. autolink-skip:: next
