
:py:mod:`agents.reasoning_and_critique.tot.agents`
==================================================

.. py:module:: agents.reasoning_and_critique.tot.agents

Tree of Thoughts specialized agents.


.. autolink-examples:: agents.reasoning_and_critique.tot.agents
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.CandidateGeneration
   agents.reasoning_and_critique.tot.agents.CandidateGenerator
   agents.reasoning_and_critique.tot.agents.ScoredSolution
   agents.reasoning_and_critique.tot.agents.SolutionScorer
   agents.reasoning_and_critique.tot.agents.SolutionScoring


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CandidateGeneration:

   .. graphviz::
      :align: center

      digraph inheritance_CandidateGeneration {
        node [shape=record];
        "CandidateGeneration" [label="CandidateGeneration"];
        "pydantic.BaseModel" -> "CandidateGeneration";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.agents.CandidateGeneration
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

   Inheritance diagram for CandidateGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_CandidateGenerator {
        node [shape=record];
        "CandidateGenerator" [label="CandidateGenerator"];
      }

.. autoclass:: agents.reasoning_and_critique.tot.agents.CandidateGenerator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ScoredSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ScoredSolution {
        node [shape=record];
        "ScoredSolution" [label="ScoredSolution"];
        "pydantic.BaseModel" -> "ScoredSolution";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.agents.ScoredSolution
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

   Inheritance diagram for SolutionScorer:

   .. graphviz::
      :align: center

      digraph inheritance_SolutionScorer {
        node [shape=record];
        "SolutionScorer" [label="SolutionScorer"];
      }

.. autoclass:: agents.reasoning_and_critique.tot.agents.SolutionScorer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SolutionScoring:

   .. graphviz::
      :align: center

      digraph inheritance_SolutionScoring {
        node [shape=record];
        "SolutionScoring" [label="SolutionScoring"];
        "pydantic.BaseModel" -> "SolutionScoring";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.agents.SolutionScoring
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

.. autolink-examples:: agents.reasoning_and_critique.tot.agents
   :collapse:
   
.. autolink-skip:: next
