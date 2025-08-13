
:py:mod:`agents.memory_reorganized.retrieval.graph_rag_retriever`
=================================================================

.. py:module:: agents.memory_reorganized.retrieval.graph_rag_retriever

Graph RAG Retriever for Memory System.

This module implements a Graph RAG retriever that combines knowledge graph traversal
with vector similarity search to provide comprehensive memory retrieval with
relationship context and semantic understanding.


.. autolink-examples:: agents.memory_reorganized.retrieval.graph_rag_retriever
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGResult
   agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGRetriever
   agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGRetrieverConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphRAGResult:

   .. graphviz::
      :align: center

      digraph inheritance_GraphRAGResult {
        node [shape=record];
        "GraphRAGResult" [label="GraphRAGResult"];
        "pydantic.BaseModel" -> "GraphRAGResult";
      }

.. autopydantic_model:: agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGResult
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphRAGRetriever:

   .. graphviz::
      :align: center

      digraph inheritance_GraphRAGRetriever {
        node [shape=record];
        "GraphRAGRetriever" [label="GraphRAGRetriever"];
      }

.. autoclass:: agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGRetriever
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphRAGRetrieverConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GraphRAGRetrieverConfig {
        node [shape=record];
        "GraphRAGRetrieverConfig" [label="GraphRAGRetrieverConfig"];
        "pydantic.BaseModel" -> "GraphRAGRetrieverConfig";
      }

.. autopydantic_model:: agents.memory_reorganized.retrieval.graph_rag_retriever.GraphRAGRetrieverConfig
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

.. autolink-examples:: agents.memory_reorganized.retrieval.graph_rag_retriever
   :collapse:
   
.. autolink-skip:: next
