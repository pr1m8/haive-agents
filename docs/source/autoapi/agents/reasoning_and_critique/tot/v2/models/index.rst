
:py:mod:`agents.reasoning_and_critique.tot.v2.models`
=====================================================

.. py:module:: agents.reasoning_and_critique.tot.v2.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.models.Candidate
   agents.reasoning_and_critique.tot.v2.models.CandidateEvaluation
   agents.reasoning_and_critique.tot.v2.models.CandidateGeneration
   agents.reasoning_and_critique.tot.v2.models.ScoredCandidate
   agents.reasoning_and_critique.tot.v2.models.SearchControl


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Candidate:

   .. graphviz::
      :align: center

      digraph inheritance_Candidate {
        node [shape=record];
        "Candidate" [label="Candidate"];
        "pydantic.BaseModel" -> "Candidate";
        "Generic[T]" -> "Candidate";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.v2.models.Candidate
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

   Inheritance diagram for CandidateEvaluation:

   .. graphviz::
      :align: center

      digraph inheritance_CandidateEvaluation {
        node [shape=record];
        "CandidateEvaluation" [label="CandidateEvaluation"];
        "pydantic.BaseModel" -> "CandidateEvaluation";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.v2.models.CandidateEvaluation
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

   Inheritance diagram for CandidateGeneration:

   .. graphviz::
      :align: center

      digraph inheritance_CandidateGeneration {
        node [shape=record];
        "CandidateGeneration" [label="CandidateGeneration"];
        "pydantic.BaseModel" -> "CandidateGeneration";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.v2.models.CandidateGeneration
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

   Inheritance diagram for ScoredCandidate:

   .. graphviz::
      :align: center

      digraph inheritance_ScoredCandidate {
        node [shape=record];
        "ScoredCandidate" [label="ScoredCandidate"];
        "Candidate[T]" -> "ScoredCandidate";
        "Generic[T]" -> "ScoredCandidate";
      }

.. autoclass:: agents.reasoning_and_critique.tot.v2.models.ScoredCandidate
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SearchControl:

   .. graphviz::
      :align: center

      digraph inheritance_SearchControl {
        node [shape=record];
        "SearchControl" [label="SearchControl"];
        "pydantic.BaseModel" -> "SearchControl";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.v2.models.SearchControl
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

.. autolink-examples:: agents.reasoning_and_critique.tot.v2.models
   :collapse:
   
.. autolink-skip:: next
