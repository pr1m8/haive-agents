agents.reasoning_and_critique.tot
=================================

.. py:module:: agents.reasoning_and_critique.tot

.. autoapi-nested-parse::

   Tree of Thoughts (TOT) reasoning module for Haive.

   This module implements the Tree of Thoughts algorithm using a multi-agent
   approach with MultiAgent. The implementation uses two specialized
   agents:

   1. CandidateGenerator - Generates diverse solution candidates
   2. SolutionScorer - Evaluates and scores candidates

   The TreeOfThoughtsOrchestrator coordinates these agents to perform
   beam search through the solution space.

   .. rubric:: Example

   ```python
   from haive.agents.reasoning_and_critique.tot import create_tot_solver

   # Create a TOT solver
   solver = await create_tot_solver(
       beam_width=5,
       max_iterations=3
   )

   # Solve a problem
   result = await solver.solve(
       problem="Use numbers 3, 3, 8, 8 to make 24",
       context="Each number must be used exactly once"
   )

   print(f"Best solution: {result.best_solution}")
   print(f"Score: {result.score}")
   ```


   .. autolink-examples:: agents.reasoning_and_critique.tot
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/reasoning_and_critique/tot/agent/index
   /autoapi/agents/reasoning_and_critique/tot/agents/index
   /autoapi/agents/reasoning_and_critique/tot/config/index
   /autoapi/agents/reasoning_and_critique/tot/engines/index
   /autoapi/agents/reasoning_and_critique/tot/example/index
   /autoapi/agents/reasoning_and_critique/tot/models/index
   /autoapi/agents/reasoning_and_critique/tot/modular/index
   /autoapi/agents/reasoning_and_critique/tot/orchestrator/index
   /autoapi/agents/reasoning_and_critique/tot/state/index
   /autoapi/agents/reasoning_and_critique/tot/tot_multi_agent/index
   /autoapi/agents/reasoning_and_critique/tot/tree_of_thoughts_agent/index
   /autoapi/agents/reasoning_and_critique/tot/v2/index


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.ToTAgent


Package Contents
----------------

.. py:data:: ToTAgent
   :value: None


