
:py:mod:`agents.reasoning_and_critique.tot.models`
==================================================

.. py:module:: agents.reasoning_and_critique.tot.models

Tree of Thoughts (ToT) models and data structures.

This module defines the core data models for the Tree of Thoughts reasoning algorithm,
including candidate solutions and structured output models.


.. autolink-examples:: agents.reasoning_and_critique.tot.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.models.Candidate
   agents.reasoning_and_critique.tot.models.CandidateEvaluation
   agents.reasoning_and_critique.tot.models.CandidateGeneration
   agents.reasoning_and_critique.tot.models.Equation
   agents.reasoning_and_critique.tot.models.EquationGeneration
   agents.reasoning_and_critique.tot.models.Score
   agents.reasoning_and_critique.tot.models.ScoredCandidate


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

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.Candidate
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

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.CandidateEvaluation
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
        "Generic[T]" -> "CandidateGeneration";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.CandidateGeneration
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

   Inheritance diagram for Equation:

   .. graphviz::
      :align: center

      digraph inheritance_Equation {
        node [shape=record];
        "Equation" [label="Equation"];
        "pydantic.BaseModel" -> "Equation";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.Equation
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

   Inheritance diagram for EquationGeneration:

   .. graphviz::
      :align: center

      digraph inheritance_EquationGeneration {
        node [shape=record];
        "EquationGeneration" [label="EquationGeneration"];
        "pydantic.BaseModel" -> "EquationGeneration";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.EquationGeneration
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

   Inheritance diagram for Score:

   .. graphviz::
      :align: center

      digraph inheritance_Score {
        node [shape=record];
        "Score" [label="Score"];
        "pydantic.BaseModel" -> "Score";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.Score
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
        "pydantic.BaseModel" -> "ScoredCandidate";
        "Generic[T]" -> "ScoredCandidate";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.models.ScoredCandidate
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



Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.models.update_candidates

.. py:function:: update_candidates(existing: list[Any] | None = None, updates: list[Any] | str | None = None) -> list[Any]

   Update candidate list, handling special cases like clearing.

   :param existing: Current list of candidates
   :param updates: New candidates to add, or "clear" to empty the list

   :returns: Updated list of candidates


   .. autolink-examples:: update_candidates
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.models
   :collapse:
   
.. autolink-skip:: next
