agents.reasoning_and_critique.tot.agents.candidate_generator
============================================================

.. py:module:: agents.reasoning_and_critique.tot.agents.candidate_generator

.. autoapi-nested-parse::

   Candidate Generator Agent for Tree of Thoughts.

   This agent generates multiple candidate solutions for a given problem.


   .. autolink-examples:: agents.reasoning_and_critique.tot.agents.candidate_generator
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.candidate_generator.CandidateGeneration
   agents.reasoning_and_critique.tot.agents.candidate_generator.CandidateGenerator


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.agents.candidate_generator.create_candidate_generator


Module Contents
---------------

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



.. py:function:: create_candidate_generator(expansion_count: int = 5, temperature: float = 0.7) -> CandidateGenerator

   Create a candidate generator with default settings.

   :param expansion_count: Number of candidates to generate
   :param temperature: Generation temperature

   :returns: Configured CandidateGenerator


   .. autolink-examples:: create_candidate_generator
      :collapse:

