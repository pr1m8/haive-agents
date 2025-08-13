
:py:mod:`agents.rag.corrective.agent_v2`
========================================

.. py:module:: agents.rag.corrective.agent_v2

Corrective RAG (CRAG) Agent V2.

from typing import Any
Self-correcting retrieval with proper quality assessment.
Implements architecture from rag-architectures-flows.md:
Retrieval → Relevance Check → Knowledge Refinement/Web Search/Combine


.. autolink-examples:: agents.rag.corrective.agent_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.corrective.agent_v2.CorrectiveRAGAgentV2


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CorrectiveRAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_CorrectiveRAGAgentV2 {
        node [shape=record];
        "CorrectiveRAGAgentV2" [label="CorrectiveRAGAgentV2"];
        "haive.agents.multi.base.ConditionalAgent" -> "CorrectiveRAGAgentV2";
      }

.. autoclass:: agents.rag.corrective.agent_v2.CorrectiveRAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.rag.corrective.agent_v2
   :collapse:
   
.. autolink-skip:: next
