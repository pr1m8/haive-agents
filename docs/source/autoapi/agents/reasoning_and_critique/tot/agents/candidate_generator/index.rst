
:py:mod:`agents.reasoning_and_critique.tot.agents.candidate_generator`
======================================================================

.. py:module:: agents.reasoning_and_critique.tot.agents.candidate_generator

Candidate Generator Agent for Tree of Thoughts.

This agent generates multiple candidate solutions for a given problem.


.. autolink-examples:: agents.reasoning_and_critique.tot.agents.candidate_generator
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.candidate_generator.CandidateGeneration
   agents.reasoning_and_critique.tot.agents.candidate_generator.CandidateGenerator


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

.. autopydantic_model:: agents.reasoning_and_critique.tot.agents.candidate_generator.CandidateGeneration
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

.. autoclass:: agents.reasoning_and_critique.tot.agents.candidate_generator.CandidateGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.candidate_generator.create_candidate_generator

.. py:function:: create_candidate_generator(expansion_count: int = 5, temperature: float = 0.7) -> CandidateGenerator

   Create a candidate generator with default settings.

   :param expansion_count: Number of candidates to generate
   :param temperature: Generation temperature

   :returns: Configured CandidateGenerator


   .. autolink-examples:: create_candidate_generator
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.agents.candidate_generator
   :collapse:
   
.. autolink-skip:: next
