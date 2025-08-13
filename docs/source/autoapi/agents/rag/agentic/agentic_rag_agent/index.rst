
:py:mod:`agents.rag.agentic.agentic_rag_agent`
==============================================

.. py:module:: agents.rag.agentic.agentic_rag_agent

Agentic RAG Multi-Agent System.

This implements an advanced RAG system with document grading, query rewriting,
and conditional routing between retrieval and web search.


.. autolink-examples:: agents.rag.agentic.agentic_rag_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.agentic.agentic_rag_agent.AgenticRAGAgent
   agents.rag.agentic.agentic_rag_agent.AgenticRAGState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGAgent {
        node [shape=record];
        "AgenticRAGAgent" [label="AgenticRAGAgent"];
        "haive.agents.simple.SimpleAgent" -> "AgenticRAGAgent";
      }

.. autoclass:: agents.rag.agentic.agentic_rag_agent.AgenticRAGAgent
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
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "AgenticRAGState";
      }

.. autoclass:: agents.rag.agentic.agentic_rag_agent.AgenticRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic.agentic_rag_agent
   :collapse:
   
.. autolink-skip:: next
