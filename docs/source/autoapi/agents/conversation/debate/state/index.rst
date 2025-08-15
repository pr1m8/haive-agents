agents.conversation.debate.state
================================

.. py:module:: agents.conversation.debate.state

.. autoapi-nested-parse::

   State schema for structured debate conversations with automatic tracking.


   .. autolink-examples:: agents.conversation.debate.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.conversation.debate.state.DebateState


Module Contents
---------------

.. py:class:: DebateState

   Bases: :py:obj:`haive.agents.conversation.base.state.ConversationState`


   Extended state schema for debate conversations with automatic tracking.

   Extends ConversationState with debate-specific fields and automatic
   computation of debate progress and statistics.


   .. autolink-examples:: DebateState
      :collapse:

   .. py:method:: get_participant_summary(participant: str) -> dict[str, Any]

      Get summary for a specific participant.


      .. autolink-examples:: get_participant_summary
         :collapse:


   .. py:attribute:: __reducer_fields__


   .. py:property:: all_arguments_complete
      :type: bool


      Check if all participants have made required arguments.

      .. autolink-examples:: all_arguments_complete
         :collapse:


   .. py:property:: all_rebuttals_complete
      :type: bool


      Check if rebuttal phase is complete.

      .. autolink-examples:: all_rebuttals_complete
         :collapse:


   .. py:attribute:: argument_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: arguments_made
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: arguments_per_side
      :type:  int
      :value: None



   .. py:attribute:: closing_statements_complete
      :type:  bool
      :value: None



   .. py:attribute:: current_phase
      :type:  str
      :value: None



   .. py:attribute:: debate_positions
      :type:  dict[str, str]
      :value: None



   .. py:property:: debate_progress
      :type: dict[str, float]


      Calculate progress for each participant.

      .. autolink-examples:: debate_progress
         :collapse:


   .. py:property:: debate_statistics
      :type: dict[str, Any]


      Get comprehensive debate statistics.

      .. autolink-examples:: debate_statistics
         :collapse:


   .. py:attribute:: debate_winner
      :type:  str
      :value: None



   .. py:property:: in_rebuttal_phase
      :type: bool


      Check if currently in rebuttal phase.

      .. autolink-examples:: in_rebuttal_phase
         :collapse:


   .. py:attribute:: judge_feedback
      :type:  list[str]
      :value: None



   .. py:property:: next_phase
      :type: str | None


      Determine what the next phase should be.

      .. autolink-examples:: next_phase
         :collapse:


   .. py:attribute:: opening_statements_complete
      :type:  bool
      :value: None



   .. py:property:: phase_should_transition
      :type: bool


      Check if current phase should transition.

      .. autolink-examples:: phase_should_transition
         :collapse:


   .. py:attribute:: phase_transitions
      :type:  list[tuple[str, int]]
      :value: None



   .. py:attribute:: rebuttals
      :type:  dict[str, list[tuple[str, str]]]
      :value: None



   .. py:property:: should_end_debate
      :type: bool


      Check if debate should end based on all conditions.

      .. autolink-examples:: should_end_debate
         :collapse:


   .. py:attribute:: total_arguments
      :type:  int
      :value: None



   .. py:attribute:: total_rebuttals
      :type:  int
      :value: None



