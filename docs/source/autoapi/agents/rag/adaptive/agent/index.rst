
:py:mod:`agents.rag.adaptive.agent`
===================================

.. py:module:: agents.rag.adaptive.agent

Adaptive RAG Agent.

Dynamic strategy selection based on query complexity.
Routes queries to appropriate RAG strategies.


.. autolink-examples:: agents.rag.adaptive.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.adaptive.agent.AdaptiveRAGAgent
   agents.rag.adaptive.agent.QueryAnalysis


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveRAGAgent {
        node [shape=record];
        "AdaptiveRAGAgent" [label="AdaptiveRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "AdaptiveRAGAgent";
      }

.. autoclass:: agents.rag.adaptive.agent.AdaptiveRAGAgent
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

.. autopydantic_model:: agents.rag.adaptive.agent.QueryAnalysis
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

.. autolink-examples:: agents.rag.adaptive.agent
   :collapse:
   
.. autolink-skip:: next
