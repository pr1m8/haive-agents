
:py:mod:`agents.document_modifiers.summarizer.iterative_refinement.state`
=========================================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement.state


Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerInput
   agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerOutput
   agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeSummarizerInput:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeSummarizerInput {
        node [shape=record];
        "IterativeSummarizerInput" [label="IterativeSummarizerInput"];
        "pydantic.BaseModel" -> "IterativeSummarizerInput";
      }

.. autopydantic_model:: agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerInput
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

   Inheritance diagram for IterativeSummarizerOutput:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeSummarizerOutput {
        node [shape=record];
        "IterativeSummarizerOutput" [label="IterativeSummarizerOutput"];
        "pydantic.BaseModel" -> "IterativeSummarizerOutput";
      }

.. autopydantic_model:: agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerOutput
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

   Inheritance diagram for IterativeSummarizerState:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeSummarizerState {
        node [shape=record];
        "IterativeSummarizerState" [label="IterativeSummarizerState"];
        "IterativeSummarizerInput" -> "IterativeSummarizerState";
        "IterativeSummarizerOutput" -> "IterativeSummarizerState";
      }

.. autoclass:: agents.document_modifiers.summarizer.iterative_refinement.state.IterativeSummarizerState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.summarizer.iterative_refinement.state
   :collapse:
   
.. autolink-skip:: next
