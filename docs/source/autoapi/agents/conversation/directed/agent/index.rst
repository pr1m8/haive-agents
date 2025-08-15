agents.conversation.directed.agent
==================================

.. py:module:: agents.conversation.directed.agent

.. autoapi-nested-parse::

   Directed conversation agent where participants respond to mentions and direct questions.
   from typing import Any
   Uses structured output models for robust speaker selection and interaction tracking.


   .. autolink-examples:: agents.conversation.directed.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.directed.agent.logger


Classes
-------

.. autoapisummary::

   agents.conversation.directed.agent.DirectedConversation
   agents.conversation.directed.agent.DirectedConversationConfig
   agents.conversation.directed.agent.InteractionPattern
   agents.conversation.directed.agent.MentionType
   agents.conversation.directed.agent.SpeakerMention
   agents.conversation.directed.agent.SpeakerSelectionResult


Module Contents
---------------

.. py:class:: DirectedConversation

   Bases: :py:obj:`haive.agents.conversation.base.agent.BaseConversationAgent`


   Directed conversation where agents respond to mentions and questions.

   Uses structured output models for robust speaker selection and tracking.
   Participants speak when:
   - They are directly mentioned (@name)
   - A question is directed at them
   - They haven't spoken in a while (configurable)


   .. autolink-examples:: DirectedConversation
      :collapse:

   .. py:method:: _check_custom_end_conditions(state: haive.agents.conversation.directed.state.DirectedState) -> dict[str, Any] | None

      Check if everyone has participated sufficiently.


      .. autolink-examples:: _check_custom_end_conditions
         :collapse:


   .. py:method:: _extract_context(content: str, mention: str, context_size: int = 50) -> str

      Extract context around a mention.


      .. autolink-examples:: _extract_context
         :collapse:


   .. py:method:: _extract_structured_mentions(state: haive.agents.conversation.directed.state.DirectedState) -> list[SpeakerMention]

      Extract mentions as structured models.


      .. autolink-examples:: _extract_structured_mentions
         :collapse:


   .. py:method:: _get_last_speaker_name(state: haive.agents.conversation.directed.state.DirectedState) -> str | None

      Get the name of the last speaker.


      .. autolink-examples:: _get_last_speaker_name
         :collapse:


   .. py:method:: _get_mention_priority(mention_type: MentionType) -> int

      Get priority score for mention type (higher is better).


      .. autolink-examples:: _get_mention_priority
         :collapse:


   .. py:method:: _get_speaker_selection(state: haive.agents.conversation.directed.state.DirectedState) -> SpeakerSelectionResult

      Get structured speaker selection result.


      .. autolink-examples:: _get_speaker_selection
         :collapse:


   .. py:method:: _prepare_agent_input(state: haive.agents.conversation.directed.state.DirectedState, agent_name: str) -> dict[str, Any]

      Prepare input with mention context.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _sanitize_name_for_openai(name: str) -> str
      :staticmethod:


      Sanitize a name to be compatible with OpenAI's API requirements.

      OpenAI's name field must match the pattern '^[^\\s<|\\\\/>]+$'
      This means no spaces, <, |, \\, /, or >

      :param name: The original name

      :returns: Sanitized name safe for OpenAI API


      .. autolink-examples:: _sanitize_name_for_openai
         :collapse:


   .. py:method:: _select_least_active_structured(state: haive.agents.conversation.directed.state.DirectedState) -> SpeakerSelectionResult

      Select the speaker who has been least active.


      .. autolink-examples:: _select_least_active_structured
         :collapse:


   .. py:method:: _select_round_robin_structured(state: haive.agents.conversation.directed.state.DirectedState) -> SpeakerSelectionResult

      Select next speaker using round-robin.


      .. autolink-examples:: _select_round_robin_structured
         :collapse:


   .. py:method:: create_classroom(teacher_name: str = 'Teacher', student_names: list[str] | None = None, topic: str = "Today's lesson", config: DirectedConversationConfig | None = None, **kwargs)
      :classmethod:


      Create a classroom-style directed conversation.

      :param teacher_name: Name of the teacher
      :param student_names: List of student names
      :param topic: Lesson topic
      :param config: Optional configuration for directed conversation
      :param \*\*kwargs: Additional conversation arguments


      .. autolink-examples:: create_classroom
         :collapse:


   .. py:method:: get_conversation_state_schema() -> type

      Use extended state schema.


      .. autolink-examples:: get_conversation_state_schema
         :collapse:


   .. py:method:: process_response(state: haive.agents.conversation.directed.state.DirectedState) -> dict[str, Any]

      Track interaction patterns using structured models.


      .. autolink-examples:: process_response
         :collapse:


   .. py:method:: select_speaker(state: haive.agents.conversation.directed.state.DirectedState) -> dict[str, Any]

      Select speaker based on mentions and context using structured models.


      .. autolink-examples:: select_speaker
         :collapse:


   .. py:attribute:: _interaction_history
      :type:  list[InteractionPattern]
      :value: []



   .. py:attribute:: config
      :type:  DirectedConversationConfig
      :value: None



   .. py:attribute:: mode
      :type:  Literal['directed']
      :value: None



.. py:class:: DirectedConversationConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for directed conversation behavior.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DirectedConversationConfig
      :collapse:

   .. py:attribute:: allow_self_selection
      :type:  bool
      :value: None



   .. py:attribute:: avoid_self_mentions
      :type:  bool
      :value: None



   .. py:attribute:: fallback_to_round_robin
      :type:  bool
      :value: None



   .. py:attribute:: max_silence_turns
      :type:  int
      :value: None



   .. py:attribute:: mention_patterns
      :type:  list[str]
      :value: None



   .. py:attribute:: prioritize_least_active
      :type:  bool
      :value: None



.. py:class:: InteractionPattern(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Track interaction patterns between speakers.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InteractionPattern
      :collapse:

   .. py:attribute:: from_speaker
      :type:  str
      :value: None



   .. py:attribute:: mention_count
      :type:  int
      :value: None



   .. py:attribute:: mention_types
      :type:  list[MentionType]
      :value: None



   .. py:attribute:: to_speaker
      :type:  str
      :value: None



.. py:class:: MentionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of mentions detected in messages.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MentionType
      :collapse:

   .. py:attribute:: DIRECT_MENTION
      :value: 'direct_mention'



   .. py:attribute:: NAME_REFERENCE
      :value: 'name_reference'



   .. py:attribute:: NO_MENTION
      :value: 'no_mention'



   .. py:attribute:: QUESTION_TARGET
      :value: 'question_target'



.. py:class:: SpeakerMention(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured representation of a speaker mention.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SpeakerMention
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: mention_type
      :type:  MentionType
      :value: None



   .. py:attribute:: speaker_name
      :type:  str
      :value: None



.. py:class:: SpeakerSelectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for speaker selection logic.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SpeakerSelectionResult
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: mentioned_speakers
      :type:  list[str]
      :value: None



   .. py:attribute:: next_speaker
      :type:  str | None
      :value: None



   .. py:attribute:: pending_speakers
      :type:  list[str]
      :value: None



   .. py:attribute:: selection_reason
      :type:  str
      :value: None



.. py:data:: logger

