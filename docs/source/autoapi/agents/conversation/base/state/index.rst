agents.conversation.base.state
==============================

.. py:module:: agents.conversation.base.state


Attributes
----------

.. autoapisummary::

   agents.conversation.base.state.ConversationMode
   agents.conversation.base.state.ConversationTopic
   agents.conversation.base.state.ProgressPercentage
   agents.conversation.base.state.RoundNumber
   agents.conversation.base.state.SpeakerList
   agents.conversation.base.state.SpeakerName
   agents.conversation.base.state.TurnCount
   agents.conversation.base.state.logger


Classes
-------

.. autoapisummary::

   agents.conversation.base.state.ConversationState


Module Contents
---------------

.. py:class:: ConversationState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   Base conversation state schema with automatic tracking and progress calculations.

   This state schema extends MessagesState with specialized fields and reducers for
   tracking multi-agent conversations. It provides automatic management of turns,
   rounds, speaker history, and conversation progress through a combination of
   Pydantic fields, reducers, and computed properties.

   The state uses reducer functions for automatic field updates. When a turn is taken,
   the turn_count and speaker_history are automatically updated through reducers,
   allowing for clean state updates without manual tracking complexity.

   .. attribute:: messages

      Conversation messages (inherited from MessagesState)

      :type: List[BaseMessage]

   .. attribute:: current_speaker

      The currently active speaker

      :type: Optional[SpeakerName]

   .. attribute:: speakers

      List of all participant speaker names

      :type: SpeakerList

   .. attribute:: turn_count

      Total number of speaking turns taken (auto-incremented)

      :type: TurnCount

   .. attribute:: max_rounds

      Maximum number of conversation rounds allowed

      :type: int

   .. attribute:: topic

      The conversation topic or subject

      :type: Optional[ConversationTopic]

   .. attribute:: conversation_ended

      Flag indicating if conversation is complete

      :type: bool

   .. attribute:: mode

      Conversation mode identifier (e.g., "round_robin", "debate")

      :type: ConversationMode

   .. attribute:: speaker_history

      Chronological history of speakers (auto-appended)

      :type: SpeakerList

   Computed Properties:
       round_number (RoundNumber): Current round number calculated from turns and speakers
       current_round_speakers (SpeakerList): Speakers who have spoken in current round
       remaining_speakers_this_round (SpeakerList): Speakers yet to speak in current round
       should_end_by_rounds (bool): Whether round limit has been reached
       turns_per_round (int): Number of turns in a complete round
       conversation_progress (ProgressPercentage): Progress from 0.0 to 1.0

   Reducer Functions:
       turn_count: operator.add - Auto-increment turns when state is updated
       speaker_history: operator.add - Append new speakers to chronological history
       messages: inherited from MessagesState - Accumulate conversation messages

   .. rubric:: Examples

   Basic usage with automatic tracking::\n

       state = ConversationState(
           speakers=["Alice", "Bob", "Charlie"],
           topic="Future of AI",
           max_rounds=5
       )

       # State automatically tracks progress
       print(f"Round {state.round_number}, Turn {state.turn_count}")
       print(f"Progress: {state.conversation_progress:.1%}")

   State updates via reducers::\n

       # Turn count automatically increments
       new_state = state.model_copy(update={"turn_count": 1})

       # Speaker history automatically appends
       new_state = new_state.model_copy(update={"speaker_history": ["Alice"]})

       # Computed properties automatically update
       print(f"Remaining: {new_state.remaining_speakers_this_round}")

   .. note::

      This state uses reducer functions for automatic field updates. The reducers
      ensure consistent state evolution without manual tracking complexity, making
      it easier to build robust conversation orchestration systems.


   .. autolink-examples:: ConversationState
      :collapse:

   .. py:attribute:: __reducer_fields__
      :type:  dict[str, Any]


   .. py:attribute:: conversation_ended
      :type:  bool
      :value: None



   .. py:property:: conversation_progress
      :type: ProgressPercentage


      Calculate conversation progress as percentage.

      Computes the progress of the conversation as a percentage from 0.0 to 1.0
      based on the current round number and maximum rounds.

      :returns: Progress from 0.0 to 1.0 (0% to 100%)

      .. rubric:: Examples

      With max_rounds=5 and current round 3::\n

          conversation_progress = 3 / 5 = 0.6  # 60% complete

      .. autolink-examples:: conversation_progress
         :collapse:


   .. py:property:: current_round_speakers
      :type: SpeakerList


      Get list of speakers who have already spoken in current round.

      Analyzes the speaker history to determine which speakers have taken
      turns in the current round, based on round boundaries.

      :returns: List of speaker names who have spoken in the current round

      .. rubric:: Examples

      With 3 speakers in round 2, turn 5::\n

          # Round 1: speakers 0-2, Round 2: speakers 3-4
          current_round_speakers = speaker_history[3:5]

      .. autolink-examples:: current_round_speakers
         :collapse:


   .. py:attribute:: current_speaker
      :type:  SpeakerName | None
      :value: None



   .. py:attribute:: max_rounds
      :type:  int
      :value: None



   .. py:attribute:: mode
      :type:  ConversationMode
      :value: None



   .. py:property:: remaining_speakers_this_round
      :type: SpeakerList


      Get speakers who haven't spoken yet in current round.

      Determines which speakers from the participant list have not yet
      taken their turn in the current round.

      :returns: List of speaker names who have not yet spoken in current round

      .. rubric:: Examples

      With speakers ["Alice", "Bob", "Charlie"] and current speakers ["Alice"]::\n

          remaining_speakers_this_round = ["Bob", "Charlie"]

      .. autolink-examples:: remaining_speakers_this_round
         :collapse:


   .. py:property:: round_number
      :type: RoundNumber


      Compute current round based on turn count and number of speakers.

      Calculates the current round number using turn count and speaker count.
      Returns 0 if no speakers or no turns have been taken.

      :returns: Current round number (1-based indexing)

      .. rubric:: Examples

      With 3 speakers and 7 turns taken::\n

          # Round 1: turns 1-3, Round 2: turns 4-6, Round 3: turn 7
          round_number = (7 - 1) // 3 + 1 = 3

      .. autolink-examples:: round_number
         :collapse:


   .. py:property:: should_end_by_rounds
      :type: bool


      Check if conversation should end based on round limit.

      Determines if the conversation has reached or exceeded the maximum
      number of rounds and should be terminated.

      :returns: True if round limit has been reached or exceeded

      .. rubric:: Examples

      With max_rounds=5 and current round 5::\n

          should_end_by_rounds = True  # Conversation should end

      .. autolink-examples:: should_end_by_rounds
         :collapse:


   .. py:attribute:: speaker_history
      :type:  SpeakerList
      :value: None



   .. py:attribute:: speakers
      :type:  SpeakerList
      :value: None



   .. py:attribute:: topic
      :type:  ConversationTopic | None
      :value: None



   .. py:attribute:: turn_count
      :type:  TurnCount
      :value: None



   .. py:property:: turns_per_round
      :type: int


      Calculate expected turns per round.

      Determines the number of turns that constitute a complete round
      based on the number of speakers.

      :returns: Number of turns in a complete round (equals number of speakers)

      .. rubric:: Examples

      With 3 speakers::\n

          turns_per_round = 3  # Each speaker gets one turn per round

      .. autolink-examples:: turns_per_round
         :collapse:


.. py:type:: ConversationMode
   :canonical: str


.. py:type:: ConversationTopic
   :canonical: str


.. py:type:: ProgressPercentage
   :canonical: float


.. py:type:: RoundNumber
   :canonical: int


.. py:type:: SpeakerList
   :canonical: list[SpeakerName]


.. py:type:: SpeakerName
   :canonical: str


.. py:type:: TurnCount
   :canonical: int


.. py:data:: logger

