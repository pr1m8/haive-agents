
:py:mod:`agents.conversation.base.examples.basic_state_management`
==================================================================

.. py:module:: agents.conversation.base.examples.basic_state_management

Basic State Management Example for Base Conversation Agents.

This example demonstrates the core state management capabilities of the base
conversation system, including automatic tracking, computed properties, and
reducer-based state updates.


.. autolink-examples:: agents.conversation.base.examples.basic_state_management
   :collapse:


Functions
---------

.. autoapisummary::

   agents.conversation.base.examples.basic_state_management.create_conversation_state
   agents.conversation.base.examples.basic_state_management.demonstrate_basic_state_creation
   agents.conversation.base.examples.basic_state_management.demonstrate_computed_properties
   agents.conversation.base.examples.basic_state_management.demonstrate_custom_state_fields
   agents.conversation.base.examples.basic_state_management.demonstrate_participant_validation
   agents.conversation.base.examples.basic_state_management.demonstrate_progress_tracking
   agents.conversation.base.examples.basic_state_management.demonstrate_state_updates
   agents.conversation.base.examples.basic_state_management.get_conversation_progress
   agents.conversation.base.examples.basic_state_management.main
   agents.conversation.base.examples.basic_state_management.validate_conversation_participants

.. py:function:: create_conversation_state(participants, topic, max_rounds=10)

   Create a conversation state with participants.


   .. autolink-examples:: create_conversation_state
      :collapse:

.. py:function:: demonstrate_basic_state_creation() -> Any

   Demonstrate basic conversation state creation and properties.


   .. autolink-examples:: demonstrate_basic_state_creation
      :collapse:

.. py:function:: demonstrate_computed_properties(state: haive.agents.conversation.base.ConversationState)

   Demonstrate computed properties for conversation analysis.


   .. autolink-examples:: demonstrate_computed_properties
      :collapse:

.. py:function:: demonstrate_custom_state_fields() -> Any

   Demonstrate extending ConversationState with custom fields.


   .. autolink-examples:: demonstrate_custom_state_fields
      :collapse:

.. py:function:: demonstrate_participant_validation() -> None

   Demonstrate participant validation.


   .. autolink-examples:: demonstrate_participant_validation
      :collapse:

.. py:function:: demonstrate_progress_tracking(state: haive.agents.conversation.base.ConversationState)

   Demonstrate progress tracking utilities.


   .. autolink-examples:: demonstrate_progress_tracking
      :collapse:

.. py:function:: demonstrate_state_updates(state: haive.agents.conversation.base.ConversationState)

   Demonstrate reducer-based state updates.


   .. autolink-examples:: demonstrate_state_updates
      :collapse:

.. py:function:: get_conversation_progress(state)

   Get conversation progress information.


   .. autolink-examples:: get_conversation_progress
      :collapse:

.. py:function:: main()
   :async:


   Run all state management demonstrations.


   .. autolink-examples:: main
      :collapse:

.. py:function:: validate_conversation_participants(participants)

   Validate conversation participants.


   .. autolink-examples:: validate_conversation_participants
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.conversation.base.examples.basic_state_management
   :collapse:
   
.. autolink-skip:: next
