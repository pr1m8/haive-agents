
:py:mod:`agents.document_modifiers.summarizer.iterative_refinement`
===================================================================

.. py:module:: agents.document_modifiers.summarizer.iterative_refinement

Module exports.


.. autolink-examples:: agents.document_modifiers.summarizer.iterative_refinement
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizer
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerConfig
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerInput
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerOutput
   agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeSummarizer:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeSummarizer {
        node [shape=record];
        "IterativeSummarizer" [label="IterativeSummarizer"];
        "haive.core.engine.agent.agent.Agent[haive.agents.document_modifiers.summarizer.iterative_refinement.config.IterativeSummarizerConfig]" -> "IterativeSummarizer";
      }

.. autoclass:: agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeSummarizerConfig:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeSummarizerConfig {
        node [shape=record];
        "IterativeSummarizerConfig" [label="IterativeSummarizerConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "IterativeSummarizerConfig";
      }

.. autoclass:: agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IterativeSummarizerInput:

   .. graphviz::
      :align: center

      digraph inheritance_IterativeSummarizerInput {
        node [shape=record];
        "IterativeSummarizerInput" [label="IterativeSummarizerInput"];
        "pydantic.BaseModel" -> "IterativeSummarizerInput";
      }

.. autopydantic_model:: agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerInput
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

.. autopydantic_model:: agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerOutput
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

.. autoclass:: agents.document_modifiers.summarizer.iterative_refinement.IterativeSummarizerState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.summarizer.iterative_refinement.should_refine

.. py:function:: should_refine(state: state.IterativeSummarizerState) -> str

   Check if the iterative summarization should continue.


   .. autolink-examples:: should_refine
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.summarizer.iterative_refinement
   :collapse:
   
.. autolink-skip:: next
