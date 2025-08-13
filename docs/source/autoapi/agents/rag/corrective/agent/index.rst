
:py:mod:`agents.rag.corrective.agent`
=====================================

.. py:module:: agents.rag.corrective.agent

Corrective RAG (CRAG) Agent.

from typing import Any, Dict
Self-correcting retrieval with quality assessment.
Implements architecture from rag-architectures-flows.md:
Retrieval → Relevance Check → Knowledge Refinement/Web Search/Combine


.. autolink-examples:: agents.rag.corrective.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.corrective.agent.CorrectiveRAGAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CorrectiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CorrectiveRAGAgent {
        node [shape=record];
        "CorrectiveRAGAgent" [label="CorrectiveRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "CorrectiveRAGAgent";
      }

.. autoclass:: agents.rag.corrective.agent.CorrectiveRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.corrective.agent
   :collapse:
   
.. autolink-skip:: next
