agents.reasoning_and_critique.tot.agents
========================================

.. py:module:: agents.reasoning_and_critique.tot.agents

.. autoapi-nested-parse::

   Tree of Thoughts specialized agents.


   .. autolink-examples:: agents.reasoning_and_critique.tot.agents
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/reasoning_and_critique/tot/agents/candidate_generator/index
   /autoapi/agents/reasoning_and_critique/tot/agents/solution_scorer/index


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.CandidateGeneration
   agents.reasoning_and_critique.tot.agents.CandidateGenerator
   agents.reasoning_and_critique.tot.agents.ScoredSolution
   agents.reasoning_and_critique.tot.agents.SolutionScorer
   agents.reasoning_and_critique.tot.agents.SolutionScoring


Package Contents
----------------

.. py:class:: CandidateGeneration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for candidate generation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateGeneration
      :collapse:

   .. py:attribute:: candidates
      :type:  list[str]
      :value: None



   .. py:attribute:: diversity_check
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: CandidateGenerator(name: str = 'candidate_generator', expansion_count: int = 5, temperature: float = 0.7, engine: haive.core.engine.aug_llm.AugLLMConfig | None = None)

   Agent that generates multiple candidate solutions using composition.

   Initialize the candidate generator.

   :param name: Agent name
   :param expansion_count: Number of candidates to generate
   :param temperature: Temperature for generation (higher = more creative)
   :param engine: Optional engine configuration


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateGenerator
      :collapse:

   .. py:method:: create(name: str = 'candidate_generator', expansion_count: int = 5, temperature: float = 0.7) -> CandidateGenerator
      :classmethod:


      Create a CandidateGenerator with proper configuration.


      .. autolink-examples:: create
         :collapse:


   .. py:method:: create_prompt(problem: str, seed_solution: str | None = None) -> str

      Create a prompt for candidate generation.

      :param problem: The problem to solve
      :param seed_solution: Optional seed solution to expand from

      :returns: Formatted prompt


      .. autolink-examples:: create_prompt
         :collapse:


   .. py:method:: expand_from_seed(problem: str, seed: str, num_candidates: int | None = None) -> CandidateGeneration
      :async:


      Expand candidates from a seed solution.

      :param problem: The problem to solve
      :param seed: Seed solution to expand from
      :param num_candidates: Override the default number of candidates

      :returns: CandidateGeneration with expanded solutions


      .. autolink-examples:: expand_from_seed
         :collapse:


   .. py:method:: generate_candidates(problem: str, num_candidates: int | None = None) -> CandidateGeneration
      :async:


      Generate candidate solutions for a problem.

      :param problem: The problem to solve
      :param num_candidates: Override the default number of candidates

      :returns: CandidateGeneration with structured output


      .. autolink-examples:: generate_candidates
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: expansion_count
      :value: 5



   .. py:attribute:: name
      :value: 'candidate_generator'



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



