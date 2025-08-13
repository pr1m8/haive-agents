
:py:mod:`agents.rag.agentic.react_rag_agent`
============================================

.. py:module:: agents.rag.agentic.react_rag_agent

Enhanced ReactAgent with Retriever Node and Routing for Agentic RAG.

This agent extends ReactAgent to add a dedicated retrieval node to the graph,
with intelligent routing between tool calls and retrieval based on the query.


.. autolink-examples:: agents.rag.agentic.react_rag_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.agentic.react_rag_agent.ReactRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactRAGAgent {
        node [shape=record];
        "ReactRAGAgent" [label="ReactRAGAgent"];
        "haive.agents.react.ReactAgent" -> "ReactRAGAgent";
      }

.. autoclass:: agents.rag.agentic.react_rag_agent.ReactRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic.react_rag_agent
   :collapse:
   
.. autolink-skip:: next
