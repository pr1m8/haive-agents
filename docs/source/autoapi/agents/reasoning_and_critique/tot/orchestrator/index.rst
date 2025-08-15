agents.reasoning_and_critique.tot.orchestrator
==============================================

.. py:module:: agents.reasoning_and_critique.tot.orchestrator

.. autoapi-nested-parse::

   Tree of Thoughts Orchestrator using MultiAgent.

   This module implements the Tree of Thoughts algorithm using a multi-agent
   approach with MultiAgent coordinating the Candidate Generator
   and Solution Scorer agents.


   .. autolink-examples:: agents.reasoning_and_critique.tot.orchestrator
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.orchestrator.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.orchestrator.TOTResult
   agents.reasoning_and_critique.tot.orchestrator.TreeOfThoughtsOrchestrator


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.orchestrator.create_tot_solver


Module Contents
---------------

.. py:class:: TOTResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from Tree of Thoughts execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TOTResult
      :collapse:

   .. py:attribute:: all_solutions
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: best_solution
      :type:  str
      :value: None



   .. py:attribute:: iterations
      :type:  int
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



.. py:class:: TreeOfThoughtsOrchestrator(name: str = 'tot_orchestrator', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, beam_width: int = 5, max_iterations: int = 3, temperature_generate: float = 0.7, temperature_score: float = 0.3)

   Orchestrates Tree of Thoughts algorithm using multiple agents.

   Initialize the Tree of Thoughts orchestrator.

   :param name: Name for the orchestrator
   :param engine: LLM configuration for the coordinator
   :param beam_width: Number of top solutions to keep at each iteration
   :param max_iterations: Maximum number of expansion iterations
   :param temperature_generate: Temperature for candidate generation
   :param temperature_score: Temperature for solution scoring


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TreeOfThoughtsOrchestrator
      :collapse:

   .. py:method:: _extract_candidates(generation_result: Any) -> list[str]

      Extract candidate solutions from generator output.


      .. autolink-examples:: _extract_candidates
         :collapse:


   .. py:method:: _extract_scores(scoring_result: Any, candidates: list[str]) -> list[tuple[str, float, str]]

      Extract scores from scorer output.


      .. autolink-examples:: _extract_scores
         :collapse:


   .. py:method:: solve(problem: str, initial_seed: str | None = None, context: str = '') -> TOTResult
      :async:


      Solve a problem using Tree of Thoughts.

      :param problem: The problem to solve
      :param initial_seed: Optional initial solution seed
      :param context: Additional context or constraints

      :returns: TOTResult with the best solution found


      .. autolink-examples:: solve
         :collapse:


   .. py:attribute:: beam_width
      :value: 5



   .. py:attribute:: coordinator


   .. py:attribute:: generator


   .. py:attribute:: max_iterations
      :value: 3



   .. py:attribute:: name
      :value: 'tot_orchestrator'



   .. py:attribute:: scorer


.. py:function:: create_tot_solver(beam_width: int = 5, max_iterations: int = 3, **kwargs) -> TreeOfThoughtsOrchestrator
   :async:


   Factory function to create a Tree of Thoughts solver.

   :param beam_width: Number of solutions to keep at each iteration
   :param max_iterations: Maximum iterations to perform
   :param \*\*kwargs: Additional arguments for the orchestrator

   :returns: Configured TreeOfThoughtsOrchestrator instance


   .. autolink-examples:: create_tot_solver
      :collapse:

.. py:data:: logger

