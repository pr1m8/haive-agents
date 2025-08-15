agents.reasoning_and_critique.tot.tot_multi_agent
=================================================

.. py:module:: agents.reasoning_and_critique.tot.tot_multi_agent

.. autoapi-nested-parse::

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


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.tot_multi_agent.main
   agents.reasoning_and_critique.tot.tot_multi_agent.solve_with_tot_multi_agent


Module Contents
---------------

.. py:class:: BeamSelection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Selection of best candidates for next iteration.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BeamSelection
      :collapse:

   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: selected_candidates
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: should_continue
      :type:  bool
      :value: None



.. py:class:: CandidateEvaluation(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Evaluation of a single candidate.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CandidateEvaluation
      :collapse:

   .. py:attribute:: candidate
      :type:  str
      :value: None



   .. py:attribute:: feedback
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: None



.. py:class:: CandidateGeneration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Multiple candidate solutions.

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



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: FinalSolution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final synthesized solution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FinalSolution
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: explanation
      :type:  str
      :value: None



   .. py:attribute:: search_summary
      :type:  str
      :value: None



   .. py:attribute:: solution
      :type:  str
      :value: None



.. py:class:: ProblemAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of the problem to solve.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProblemAnalysis
      :collapse:

   .. py:attribute:: approach_hints
      :type:  list[str]
      :value: None



   .. py:attribute:: key_constraints
      :type:  list[str]
      :value: None



   .. py:attribute:: problem_type
      :type:  str
      :value: None



   .. py:attribute:: success_criteria
      :type:  str
      :value: None



.. py:class:: TreeOfThoughtsMultiAgent(max_depth: int = 3, beam_width: int = 3, threshold: float = 0.8, expansion_count: int = 5, temperature_config: dict[str, float] | None = None)

   Tree of Thoughts implemented as a multi-agent system.

   Initialize the TOT multi-agent system.

   :param max_depth: Maximum search depth
   :param beam_width: Number of candidates to keep at each level
   :param threshold: Score threshold for accepting a solution
   :param expansion_count: Number of new candidates to generate
   :param temperature_config: Temperature settings for each agent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TreeOfThoughtsMultiAgent
      :collapse:

   .. py:method:: _format_best_candidates() -> str

      Format the best candidates from search history.


      .. autolink-examples:: _format_best_candidates
         :collapse:


   .. py:method:: _format_candidates_for_selection(candidates: list[dict]) -> str

      Format candidates for the selector agent.


      .. autolink-examples:: _format_candidates_for_selection
         :collapse:


   .. py:method:: solve(problem: str) -> dict[str, Any]
      :async:


      Solve a problem using Tree of Thoughts multi-agent approach.

      :param problem: The problem to solve

      :returns: Dictionary containing solution and search metadata


      .. autolink-examples:: solve
         :collapse:


   .. py:method:: visualize_search_tree() -> str

      Create a simple text visualization of the search tree.


      .. autolink-examples:: visualize_search_tree
         :collapse:


   .. py:attribute:: beam_selector


   .. py:attribute:: beam_width
      :value: 3



   .. py:attribute:: best_solution
      :value: None



   .. py:attribute:: candidate_generator


   .. py:attribute:: expansion_count
      :value: 5



   .. py:attribute:: max_depth
      :value: 3



   .. py:attribute:: problem_analysis
      :value: None



   .. py:attribute:: problem_analyzer


   .. py:attribute:: search_history
      :value: []



   .. py:attribute:: solution_evaluator


   .. py:attribute:: solution_synthesizer


   .. py:attribute:: threshold
      :value: 0.8



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

