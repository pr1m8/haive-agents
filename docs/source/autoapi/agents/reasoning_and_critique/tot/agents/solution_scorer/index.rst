
:py:mod:`agents.reasoning_and_critique.tot.agents.solution_scorer`
==================================================================

.. py:module:: agents.reasoning_and_critique.tot.agents.solution_scorer

Solution Scorer agent for Tree of Thoughts.

This agent evaluates and scores candidate solutions in the TOT algorithm.
It provides numerical scores and reasoning for each candidate to guide
the beam search process.


.. autolink-examples:: agents.reasoning_and_critique.tot.agents.solution_scorer
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.solution_scorer.ScoredSolution
   agents.reasoning_and_critique.tot.agents.solution_scorer.SolutionScorer
   agents.reasoning_and_critique.tot.agents.solution_scorer.SolutionScoring


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ScoredSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ScoredSolution {
        node [shape=record];
        "ScoredSolution" [label="ScoredSolution"];
        "pydantic.BaseModel" -> "ScoredSolution";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.agents.solution_scorer.ScoredSolution
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

.. autoclass:: agents.reasoning_and_critique.tot.agents.solution_scorer.SolutionScorer
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

.. autopydantic_model:: agents.reasoning_and_critique.tot.agents.solution_scorer.SolutionScoring
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

.. autolink-examples:: agents.reasoning_and_critique.tot.agents.solution_scorer
   :collapse:
   
.. autolink-skip:: next
