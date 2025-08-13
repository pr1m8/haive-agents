
:py:mod:`agents.document_modifiers.kg.kg_base.models`
=====================================================

.. py:module:: agents.document_modifiers.kg.kg_base.models

Core models for knowledge graph document transformation.

This module provides the fundamental GraphTransformer class for converting
documents into knowledge graphs using LLM-based extraction techniques.


.. autolink-examples:: agents.document_modifiers.kg.kg_base.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.kg.kg_base.models.GraphTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_GraphTransformer {
        node [shape=record];
        "GraphTransformer" [label="GraphTransformer"];
        "langchain_core.documents.BaseDocumentTransformer" -> "GraphTransformer";
      }

.. autoclass:: agents.document_modifiers.kg.kg_base.models.GraphTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.kg.kg_base.models
   :collapse:
   
.. autolink-skip:: next
