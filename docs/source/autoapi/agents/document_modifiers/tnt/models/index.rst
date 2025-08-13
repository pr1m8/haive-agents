
:py:mod:`agents.document_modifiers.tnt.models`
==============================================

.. py:module:: agents.document_modifiers.tnt.models

Data models for taxonomy generation.

This module defines the core data structures used in the taxonomy generation process,
particularly the document model that represents individual pieces of content being
processed.

.. rubric:: Example

Basic usage of document model::

    doc = Doc(
        id="doc1",
        content="Sample text",
        summary="Brief summary",
        explanation="Summary rationale",
        category="Technology"
    )


.. autolink-examples:: agents.document_modifiers.tnt.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.tnt.models.Doc


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Doc:

   .. graphviz::
      :align: center

      digraph inheritance_Doc {
        node [shape=record];
        "Doc" [label="Doc"];
        "pydantic.BaseModel" -> "Doc";
      }

.. autopydantic_model:: agents.document_modifiers.tnt.models.Doc
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

.. autolink-examples:: agents.document_modifiers.tnt.models
   :collapse:
   
.. autolink-skip:: next
