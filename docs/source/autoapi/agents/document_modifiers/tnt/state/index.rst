
:py:mod:`agents.document_modifiers.tnt.state`
=============================================

.. py:module:: agents.document_modifiers.tnt.state

State management for taxonomy generation workflow.

This module defines the state schema used throughout the taxonomy generation process.
It provides a structured way to track documents, their groupings into minibatches,
and the evolution of taxonomy clusters over multiple iterations.

.. rubric:: Example

Basic usage of the state class::

    state = TaxonomyGenerationState(
        documents=[Doc(id="1", content="text")],
        minibatches=[[0]],
        clusters=[[{"id": 1, "name": "Category"}]]
    )


.. autolink-examples:: agents.document_modifiers.tnt.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.tnt.state.TaxonomyGenerationState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaxonomyGenerationState:

   .. graphviz::
      :align: center

      digraph inheritance_TaxonomyGenerationState {
        node [shape=record];
        "TaxonomyGenerationState" [label="TaxonomyGenerationState"];
        "pydantic.BaseModel" -> "TaxonomyGenerationState";
      }

.. autopydantic_model:: agents.document_modifiers.tnt.state.TaxonomyGenerationState
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

.. autolink-examples:: agents.document_modifiers.tnt.state
   :collapse:
   
.. autolink-skip:: next
