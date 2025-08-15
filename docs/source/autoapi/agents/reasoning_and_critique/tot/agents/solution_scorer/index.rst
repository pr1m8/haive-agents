agents.reasoning_and_critique.tot.agents.solution_scorer
========================================================

.. py:module:: agents.reasoning_and_critique.tot.agents.solution_scorer

.. autoapi-nested-parse::

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

.. py:class:: ScoredSolution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual scored solution with reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ScoredSolution
      :collapse:

   .. py:attribute:: has_errors
      :type:  bool
      :value: None



   .. py:attribute:: is_complete
      :type:  bool
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



   .. py:attribute:: solution
      :type:  str
      :value: None



.. py:class:: SolutionScorer(name: str = 'solution_scorer', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, temperature: float = 0.3)

   Agent that scores candidate solutions for Tree of Thoughts.

   Initialize the Solution Scorer agent.

   :param name: Agent name
   :param engine: LLM configuration
   :param temperature: Temperature for generation (lower = more consistent)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SolutionScorer
      :collapse:

   .. py:method:: _parse_scoring_output(output: str, candidates: list[str]) -> SolutionScoring

      Parse scoring output as fallback.


      .. autolink-examples:: _parse_scoring_output
         :collapse:


   .. py:method:: get_best_solutions(problem: str, candidates: list[str], top_k: int = 3, context: str = '') -> list[tuple[str, float]]
      :async:


      Get the top-k best solutions with their scores.

      :param problem: The original problem
      :param candidates: List of candidate solutions
      :param top_k: Number of top solutions to return
      :param context: Additional context

      :returns: List of (solution, score) tuples, sorted by score descending


      .. autolink-examples:: get_best_solutions
         :collapse:


   .. py:method:: score_solutions(problem: str, candidates: list[str], context: str = '') -> SolutionScoring
      :async:


      Score a list of candidate solutions.

      :param problem: The original problem statement
      :param candidates: List of candidate solutions to score
      :param context: Additional context or constraints

      :returns: SolutionScoring with scores and reasoning


      .. autolink-examples:: score_solutions
         :collapse:


   .. py:attribute:: agent


.. py:class:: SolutionScoring(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for solution scoring.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SolutionScoring
      :collapse:

   .. py:attribute:: problem_understanding
      :type:  str
      :value: None



   .. py:attribute:: ranking_rationale
      :type:  str
      :value: None



   .. py:attribute:: scored_solutions
      :type:  list[ScoredSolution]
      :value: None



