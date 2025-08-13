
:py:mod:`agents.reasoning_and_critique.tot.tot_multi_agent`
===========================================================

.. py:module:: agents.reasoning_and_critique.tot.tot_multi_agent

Tree of Thoughts Multi-Agent Implementation.

This module implements Tree of Thoughts as a multi-agent system using MultiAgent.
Each stage of the TOT algorithm is handled by a specialized agent.


.. autolink-examples:: agents.reasoning_and_critique.tot.tot_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tot_multi_agent.BeamSelection
   agents.reasoning_and_critique.tot.tot_multi_agent.CandidateEvaluation
   agents.reasoning_and_critique.tot.tot_multi_agent.CandidateGeneration
   agents.reasoning_and_critique.tot.tot_multi_agent.FinalSolution
   agents.reasoning_and_critique.tot.tot_multi_agent.ProblemAnalysis
   agents.reasoning_and_critique.tot.tot_multi_agent.TreeOfThoughtsMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BeamSelection:

   .. graphviz::
      :align: center

      digraph inheritance_BeamSelection {
        node [shape=record];
        "BeamSelection" [label="BeamSelection"];
        "pydantic.BaseModel" -> "BeamSelection";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.tot_multi_agent.BeamSelection
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

.. autopydantic_model:: agents.reasoning_and_critique.tot.tot_multi_agent.CandidateEvaluation
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

.. autopydantic_model:: agents.reasoning_and_critique.tot.tot_multi_agent.CandidateGeneration
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

   Inheritance diagram for FinalSolution:

   .. graphviz::
      :align: center

      digraph inheritance_FinalSolution {
        node [shape=record];
        "FinalSolution" [label="FinalSolution"];
        "pydantic.BaseModel" -> "FinalSolution";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.tot_multi_agent.FinalSolution
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

   Inheritance diagram for ProblemAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ProblemAnalysis {
        node [shape=record];
        "ProblemAnalysis" [label="ProblemAnalysis"];
        "pydantic.BaseModel" -> "ProblemAnalysis";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.tot_multi_agent.ProblemAnalysis
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

   Inheritance diagram for TreeOfThoughtsMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TreeOfThoughtsMultiAgent {
        node [shape=record];
        "TreeOfThoughtsMultiAgent" [label="TreeOfThoughtsMultiAgent"];
      }

.. autoclass:: agents.reasoning_and_critique.tot.tot_multi_agent.TreeOfThoughtsMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tot_multi_agent.main
   agents.reasoning_and_critique.tot.tot_multi_agent.solve_with_tot_multi_agent

.. py:function:: main()
   :async:


.. py:function:: solve_with_tot_multi_agent(problem: str, max_depth: int = 3, beam_width: int = 3, threshold: float = 0.8) -> dict[str, Any]
   :async:


   Convenience function to solve a problem with TOT multi-agent.

   :param problem: Problem to solve
   :param max_depth: Maximum search depth
   :param beam_width: Beam width for search
   :param threshold: Solution acceptance threshold

   :returns: Solution dictionary


   .. autolink-examples:: solve_with_tot_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.tot_multi_agent
   :collapse:
   
.. autolink-skip:: next
