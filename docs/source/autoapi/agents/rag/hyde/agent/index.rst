
:py:mod:`agents.rag.hyde.agent`
===============================

.. py:module:: agents.rag.hyde.agent

HyDE (Hypothetical Document Embeddings) RAG Agent.

from typing import Any
Bridges query-document semantic gap by generating hypothetical documents.
Implements architecture from rag-architectures-flows.md:
Query -> Generate Hypothetical Doc -> Embed -> Retrieve Real Docs -> Generate


.. autolink-examples:: agents.rag.hyde.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.hyde.agent.HyDERAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDERAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HyDERAGAgent {
        node [shape=record];
        "HyDERAGAgent" [label="HyDERAGAgent"];
        "haive.agents.multi.MultiAgent" -> "HyDERAGAgent";
      }

.. autoclass:: agents.rag.hyde.agent.HyDERAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.hyde.agent
   :collapse:
   
.. autolink-skip:: next
