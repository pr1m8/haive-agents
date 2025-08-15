agents.conversation.collaberative.agent
=======================================

.. py:module:: agents.conversation.collaberative.agent

.. autoapi-nested-parse::

   Collaborative conversation agent for building shared content.


   .. autolink-examples:: agents.conversation.collaberative.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.collaberative.agent.logger


Classes
-------

.. autoapisummary::

   agents.conversation.collaberative.agent.CollaborativeConversation


Module Contents
---------------

.. py:class:: CollaborativeConversation

   Bases: :py:obj:`haive.agents.conversation.base.agent.BaseConversationAgent`


   Collaborative conversation for building shared content.

   Features:
   - Structured document building
   - Section-based contributions
   - Review and approval process
   - Version tracking
   - Multiple output formats


   .. autolink-examples:: CollaborativeConversation
      :collapse:

   .. py:method:: _check_custom_end_conditions(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> langgraph.types.Command | None

      Check if all sections are complete.


      .. autolink-examples:: _check_custom_end_conditions
         :collapse:


   .. py:method:: _check_section_completion(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> langgraph.types.Command | None

      Check if current section is complete and move to next.


      .. autolink-examples:: _check_section_completion
         :collapse:


   .. py:method:: _compile_document(state: haive.agents.conversation.collaberative.state.CollaborativeState, sections: dict[str, str]) -> str

      Compile sections into final document.


      .. autolink-examples:: _compile_document
         :collapse:


   .. py:method:: _create_initial_message() -> langchain_core.messages.BaseMessage

      Create collaborative session introduction.


      .. autolink-examples:: _create_initial_message
         :collapse:


   .. py:method:: _custom_initialization(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> dict[str, Any]

      Initialize collaborative-specific state.


      .. autolink-examples:: _custom_initialization
         :collapse:


   .. py:method:: _finalize_document(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> langgraph.types.Command

      Finalize the collaborative document.


      .. autolink-examples:: _finalize_document
         :collapse:


   .. py:method:: _prepare_agent_input(state: haive.agents.conversation.collaberative.state.CollaborativeState, agent_name: str) -> dict[str, Any]

      Prepare input with collaboration context.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _select_least_active_overall(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> langgraph.types.Command

      Select speaker who has contributed least overall.


      .. autolink-examples:: _select_least_active_overall
         :collapse:


   .. py:method:: create_brainstorming_session(topic: str, participants: list[str], sections: list[str] | None = None, **kwargs)
      :classmethod:


      Create a brainstorming/ideation session.

      :param topic: Brainstorming topic
      :param participants: List of participant names
      :param sections: Optional custom sections
      :param \*\*kwargs: Additional configuration


      .. autolink-examples:: create_brainstorming_session
         :collapse:


   .. py:method:: create_code_review(code_description: str, reviewers: dict[str, str], **kwargs)
      :classmethod:


      Create a collaborative code review session.

      :param code_description: Description of code being reviewed
      :param reviewers: Dictionary mapping reviewer names to expertise
      :param \*\*kwargs: Additional configuration


      .. autolink-examples:: create_code_review
         :collapse:


   .. py:method:: get_conversation_state_schema() -> type

      Use collaborative state schema.


      .. autolink-examples:: get_conversation_state_schema
         :collapse:


   .. py:method:: process_response(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> langgraph.types.Command

      Process contribution and update document.


      .. autolink-examples:: process_response
         :collapse:


   .. py:method:: select_speaker(state: haive.agents.conversation.collaberative.state.CollaborativeState) -> langgraph.types.Command

      Select speaker based on contribution balance and current section.


      .. autolink-examples:: select_speaker
         :collapse:


   .. py:attribute:: allow_revisions
      :type:  bool
      :value: None



   .. py:attribute:: document_title
      :type:  str
      :value: None



   .. py:attribute:: include_attribution
      :type:  bool
      :value: None



   .. py:attribute:: min_contributions_per_section
      :type:  int
      :value: None



   .. py:attribute:: mode
      :type:  Literal['collaborative']
      :value: None



   .. py:attribute:: output_format
      :type:  Literal['markdown', 'code', 'outline', 'report']
      :value: None



   .. py:attribute:: require_approval
      :type:  bool
      :value: None



   .. py:attribute:: sections
      :type:  list[str]
      :value: None



.. py:data:: logger

