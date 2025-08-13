
:py:mod:`agents.rag.hyde.agent_v2`
==================================

.. py:module:: agents.rag.hyde.agent_v2

HyDE (Hypothetical Document Embeddings) RAG Agent V2.

Bridges query-document semantic gap by generating hypothetical documents.
This version properly embeds the hypothetical document for retrieval.


.. autolink-examples:: agents.rag.hyde.agent_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.hyde.agent_v2.HyDERAGAgentV2
   agents.rag.hyde.agent_v2.HyDERetrieverAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDERAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_HyDERAGAgentV2 {
        node [shape=record];
        "HyDERAGAgentV2" [label="HyDERAGAgentV2"];
        "haive.agents.multi.enhanced_sequential_agent.SequentialAgent" -> "HyDERAGAgentV2";
      }

.. autoclass:: agents.rag.hyde.agent_v2.HyDERAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDERetrieverAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HyDERetrieverAgent {
        node [shape=record];
        "HyDERetrieverAgent" [label="HyDERetrieverAgent"];
        "haive.agents.base.agent.Agent" -> "HyDERetrieverAgent";
      }

.. autoclass:: agents.rag.hyde.agent_v2.HyDERetrieverAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.hyde.agent_v2.build_graph
   agents.rag.hyde.agent_v2.transform_to_query

.. py:function:: build_graph() -> Any

   Build custom graph for HyDE workflows.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_graph
      :collapse:

.. py:function:: transform_to_query(hypothesis: str) -> str

   Transform hypothesis to query format.

   :param hypothesis: Generated hypothesis text

   :returns: Formatted query string


   .. autolink-examples:: transform_to_query
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.hyde.agent_v2
   :collapse:
   
.. autolink-skip:: next
