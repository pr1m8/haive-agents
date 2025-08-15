agents.conversation.debate.agent
================================

.. py:module:: agents.conversation.debate.agent

.. autoapi-nested-parse::

   Structured debate conversation agent with positions and formal argumentation.

   This module implements a debate conversation agent that manages structured debates
   between multiple participants with defined positions, argument tracking, and
   optional judging/scoring capabilities.


   .. autolink-examples:: agents.conversation.debate.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.debate.agent.logger


Classes
-------

.. autoapisummary::

   agents.conversation.debate.agent.DebateConversation


Module Contents
---------------

.. py:class:: DebateConversation

   Bases: :py:obj:`haive.agents.conversation.base.agent.BaseConversationAgent`


   Structured debate conversation with positions and formal argumentation.

   This agent orchestrates formal debates between participants using a
   reducer-based state system for automatic tracking and phase management.

   Features:
   - Automatic round tracking via reducers
   - Phase transitions based on computed properties
   - Structured debate format with opening/closing statements
   - Optional judging and scoring
   - Configurable argument requirements


   .. autolink-examples:: DebateConversation
      :collapse:

   .. py:method:: __repr__() -> str

      String representation of the debate conversation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _check_custom_end_conditions(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any] | None

      Check custom end conditions using computed properties.


      .. autolink-examples:: _check_custom_end_conditions
         :collapse:


   .. py:method:: _create_initial_message() -> langchain_core.messages.BaseMessage

      Create the debate introduction message.


      .. autolink-examples:: _create_initial_message
         :collapse:


   .. py:method:: _custom_initialization(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Initialize debate-specific state fields.


      .. autolink-examples:: _custom_initialization
         :collapse:


   .. py:method:: _extract_debate_winner(judge_content: str, state: haive.agents.conversation.debate.state.DebateState) -> str | None

      Extract winner from judge's decision.


      .. autolink-examples:: _extract_debate_winner
         :collapse:


   .. py:method:: _get_opponent_summary(state: haive.agents.conversation.debate.state.DebateState, agent_name: str) -> str

      Get summary of opponent arguments for rebuttal context.


      .. autolink-examples:: _get_opponent_summary
         :collapse:


   .. py:method:: _get_phase_instructions(state: haive.agents.conversation.debate.state.DebateState, agent_name: str) -> str

      Get phase-specific instructions for an agent.


      .. autolink-examples:: _get_phase_instructions
         :collapse:


   .. py:method:: _identify_rebuttal_target(content: str, state: haive.agents.conversation.debate.state.DebateState, speaker: str) -> str | None

      Identify who a rebuttal is targeting.


      .. autolink-examples:: _identify_rebuttal_target
         :collapse:


   .. py:method:: _prepare_agent_input(state: haive.agents.conversation.debate.state.DebateState, agent_name: str) -> dict[str, Any]

      Prepare input for a specific agent with debate context.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _select_argument_speaker(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Select speaker for main arguments phase.


      .. autolink-examples:: _select_argument_speaker
         :collapse:


   .. py:method:: _select_closing_speaker(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Select speaker for closing statements.


      .. autolink-examples:: _select_closing_speaker
         :collapse:


   .. py:method:: _select_opening_speaker(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Select speaker for opening statements.


      .. autolink-examples:: _select_opening_speaker
         :collapse:


   .. py:method:: _select_rebuttal_speaker(state: haive.agents.conversation.debate.state.DebateState) -> dict[str, Any]

      Select speaker for rebuttal phase.


      .. autolink-examples:: _select_rebuttal_speaker
         :collapse:


   .. py:method:: _transition_to_phase(state: haive.agents.conversation.debate.state.DebateState, new_phase: str) -> dict[str, Any]

      Create state updates for transitioning to a new phase.


      .. autolink-examples:: _transition_to_phase
         :collapse:


   .. py:method:: conclude_conversation(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

      Create debate conclusion using state statistics.


      .. autolink-examples:: conclude_conversation
         :collapse:


   .. py:method:: create_simple_debate(topic: str, position_a: tuple[str, str], position_b: tuple[str, str], enable_judge: bool = False, arguments_per_side: int = 3, temperature: float = 0.7, **kwargs) -> DebateConversation
      :classmethod:


      Create a simple two-sided debate conversation.


      .. autolink-examples:: create_simple_debate
         :collapse:


   .. py:method:: get_conversation_state_schema() -> type[haive.agents.conversation.debate.state.DebateState]

      Return the DebateState schema for this conversation.


      .. autolink-examples:: get_conversation_state_schema
         :collapse:


   .. py:method:: process_response(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

      Process agent response using reducers for automatic tracking.


      .. autolink-examples:: process_response
         :collapse:


   .. py:method:: select_speaker(state: haive.agents.conversation.debate.state.DebateState) -> langgraph.types.Command

      Select the next speaker based on debate phase and rules.


      .. autolink-examples:: select_speaker
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the debate agent with proper state schema.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_debate_setup() -> DebateConversation

      Validate debate configuration and participant setup.


      .. autolink-examples:: validate_debate_setup
         :collapse:


   .. py:attribute:: arguments_per_side
      :type:  int
      :value: None



   .. py:attribute:: debate_format
      :type:  Literal['traditional', 'oxford', 'parliamentary']
      :value: None



   .. py:attribute:: debate_positions
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: enable_closing_statements
      :type:  bool
      :value: None



   .. py:attribute:: enable_judge
      :type:  bool
      :value: None



   .. py:attribute:: enable_opening_statements
      :type:  bool
      :value: None



   .. py:attribute:: enforce_position_consistency
      :type:  bool
      :value: None



   .. py:attribute:: judge_name
      :type:  str
      :value: None



   .. py:attribute:: mode
      :type:  Literal['debate']
      :value: None



   .. py:attribute:: require_evidence
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: time_limit_per_turn
      :type:  int | None
      :value: None



.. py:data:: logger

