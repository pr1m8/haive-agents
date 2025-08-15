agents.reasoning_and_critique.tot.v2.state
==========================================

.. py:module:: agents.reasoning_and_critique.tot.v2.state


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.state.ExpansionState
   agents.reasoning_and_critique.tot.v2.state.ToTState


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.tot.v2.state.update_candidates


Module Contents
---------------

.. py:class:: ExpansionState

   Bases: :py:obj:`ToTState`


   State for expansion with seed candidate.


   .. autolink-examples:: ExpansionState
      :collapse:

   .. py:attribute:: seed
      :type:  haive.agents.reasoning_and_critique.tot.v2.models.ScoredCandidate | None
      :value: None



.. py:class:: ToTState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   Base Tree of Thoughts state.


   .. autolink-examples:: ToTState
      :collapse:

   .. py:method:: convert_candidates(data: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Convert raw candidate data to proper Candidate/ScoredCandidate objects.


      .. autolink-examples:: convert_candidates
         :collapse:


   .. py:method:: get_candidate_by_id(candidate_id: str) -> haive.agents.reasoning_and_critique.tot.v2.models.Candidate | haive.agents.reasoning_and_critique.tot.v2.models.ScoredCandidate | None

      Find a candidate by ID in any list.


      .. autolink-examples:: get_candidate_by_id
         :collapse:


   .. py:attribute:: all_candidates_history
      :type:  Annotated[list[haive.agents.reasoning_and_critique.tot.v2.models.Candidate | haive.agents.reasoning_and_critique.tot.v2.models.ScoredCandidate], operator.add]
      :value: None



   .. py:attribute:: beam_size
      :type:  int
      :value: None



   .. py:property:: best_candidates_summary
      :type: str


      Summary of best candidates found so far.

      .. autolink-examples:: best_candidates_summary
         :collapse:


   .. py:property:: best_score
      :type: float


      Best score found so far.

      .. autolink-examples:: best_score
         :collapse:


   .. py:attribute:: best_solution
      :type:  haive.agents.reasoning_and_critique.tot.v2.models.ScoredCandidate | None
      :value: None



   .. py:property:: candidate_for_scoring
      :type: str


      Format current candidate for scoring prompt.

      .. autolink-examples:: candidate_for_scoring
         :collapse:


   .. py:attribute:: candidates
      :type:  Annotated[list[haive.agents.reasoning_and_critique.tot.v2.models.Candidate], update_candidates]
      :value: None



   .. py:property:: candidates_for_expansion
      :type: str


      Format selected candidates for expansion prompts.

      .. autolink-examples:: candidates_for_expansion
         :collapse:


   .. py:attribute:: current_candidate_id
      :type:  str | None
      :value: None



   .. py:attribute:: depth
      :type:  Annotated[int, operator.add]
      :value: None



   .. py:attribute:: expansion_factor
      :type:  int
      :value: None



   .. py:attribute:: max_depth
      :type:  int
      :value: None



   .. py:property:: problem
      :type: str


      Extract the problem from the first human message.

      .. autolink-examples:: problem
         :collapse:


   .. py:attribute:: problem_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: problem_type
      :type:  str | None
      :value: None



   .. py:attribute:: scored_candidates
      :type:  Annotated[list[haive.agents.reasoning_and_critique.tot.v2.models.ScoredCandidate], update_candidates]
      :value: None



   .. py:property:: scored_candidates_summary
      :type: str


      Summary of scored candidates for pruning decisions.

      .. autolink-examples:: scored_candidates_summary
         :collapse:


   .. py:property:: search_progress
      :type: str


      Current search progress description.

      .. autolink-examples:: search_progress
         :collapse:


   .. py:attribute:: search_strategy
      :type:  Literal['breadth_first', 'best_first', 'adaptive']
      :value: None



   .. py:attribute:: selected_candidates
      :type:  list[haive.agents.reasoning_and_critique.tot.v2.models.ScoredCandidate]
      :value: None



   .. py:attribute:: should_terminate
      :type:  bool
      :value: None



   .. py:attribute:: termination_reason
      :type:  str | None
      :value: None



   .. py:attribute:: threshold
      :type:  float
      :value: None



.. py:function:: update_candidates(existing: list | None = None, updates: list | Literal['clear'] | None = None) -> list

   Custom reducer for candidates.


   .. autolink-examples:: update_candidates
      :collapse:

