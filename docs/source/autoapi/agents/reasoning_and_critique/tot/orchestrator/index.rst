
:py:mod:`agents.reasoning_and_critique.tot.orchestrator`
========================================================

.. py:module:: agents.reasoning_and_critique.tot.orchestrator

Tree of Thoughts Orchestrator using MultiAgent.

This module implements the Tree of Thoughts algorithm using a multi-agent
approach with MultiAgent coordinating the Candidate Generator
and Solution Scorer agents.


.. autolink-examples:: agents.reasoning_and_critique.tot.orchestrator
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.orchestrator.TOTResult
   agents.reasoning_and_critique.tot.orchestrator.TreeOfThoughtsOrchestrator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TOTResult:

   .. graphviz::
      :align: center

      digraph inheritance_TOTResult {
        node [shape=record];
        "TOTResult" [label="TOTResult"];
        "pydantic.BaseModel" -> "TOTResult";
      }

.. autopydantic_model:: agents.reasoning_and_critique.tot.orchestrator.TOTResult
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

   Inheritance diagram for TreeOfThoughtsOrchestrator:

   .. graphviz::
      :align: center

      digraph inheritance_TreeOfThoughtsOrchestrator {
        node [shape=record];
        "TreeOfThoughtsOrchestrator" [label="TreeOfThoughtsOrchestrator"];
      }

.. autoclass:: agents.reasoning_and_critique.tot.orchestrator.TreeOfThoughtsOrchestrator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.orchestrator.create_tot_solver

.. py:function:: create_tot_solver(beam_width: int = 5, max_iterations: int = 3, **kwargs) -> TreeOfThoughtsOrchestrator
   :async:


   Factory function to create a Tree of Thoughts solver.

   :param beam_width: Number of solutions to keep at each iteration
   :param max_iterations: Maximum iterations to perform
   :param \*\*kwargs: Additional arguments for the orchestrator

   :returns: Configured TreeOfThoughtsOrchestrator instance


   .. autolink-examples:: create_tot_solver
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.tot.orchestrator
   :collapse:
   
.. autolink-skip:: next
