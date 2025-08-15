agents.conversation.base.example
================================

.. py:module:: agents.conversation.base.example

.. autoapi-nested-parse::

   Base Conversation Agent Example.

   This example demonstrates how to create custom conversation agents by extending
   the BaseConversationAgent class and implementing core conversation patterns.


   .. autolink-examples:: agents.conversation.base.example
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.base.example.logger


Exceptions
----------

.. autoapisummary::

   agents.conversation.base.example.ConversationError


Classes
-------

.. autoapisummary::

   agents.conversation.base.example.CustomConversationAgent
   agents.conversation.base.example.CustomConversationState


Functions
---------

.. autoapisummary::

   agents.conversation.base.example.main


Module Contents
---------------

.. py:exception:: ConversationError

   Bases: :py:obj:`Exception`


   Placeholder for conversation errors.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationError
      :collapse:

.. py:class:: CustomConversationAgent(*args, **kwargs)

   Bases: :py:obj:`haive.agents.conversation.base.BaseConversationAgent`


   Custom conversation agent demonstrating extension patterns.

   This example shows how to:
   - Implement custom speaker selection logic
   - Add conversation quality assessment
   - Handle errors gracefully
   - Track custom metrics

   Initialize with custom configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CustomConversationAgent
      :collapse:

   .. py:method:: _assess_response_quality(response: str) -> float

      Simplified quality assessment based on response characteristics.

      In a real implementation, this could use:
      - Sentiment analysis
      - Relevance scoring
      - Coherence metrics
      - Fact checking


      .. autolink-examples:: _assess_response_quality
         :collapse:


   .. py:method:: _get_termination_reason(state: CustomConversationState) -> str

      Determine why the conversation ended.


      .. autolink-examples:: _get_termination_reason
         :collapse:


   .. py:method:: execute_agent(agent: Any, input_data: str, state: CustomConversationState) -> str
      :async:


      Execute agent with quality assessment and error handling.


      .. autolink-examples:: execute_agent
         :collapse:


   .. py:method:: get_conversation_summary() -> dict[str, Any]

      Generate comprehensive conversation summary.


      .. autolink-examples:: get_conversation_summary
         :collapse:


   .. py:method:: select_next_speaker(state: CustomConversationState) -> str | None

      Custom speaker selection with engagement-based prioritization.

      Selects speakers based on:
      1. Who hasn't spoken in the current round
      2. Engagement level preferences
      3. Balanced participation


      .. autolink-examples:: select_next_speaker
         :collapse:


   .. py:method:: should_end_conversation(state: CustomConversationState) -> bool

      Enhanced termination logic with quality considerations.

      Ends conversation if:
      - Round limit reached
      - Quality drops below threshold
      - Engagement is too low
      - Explicit end flag set


      .. autolink-examples:: should_end_conversation
         :collapse:


   .. py:attribute:: conversation_metrics


   .. py:attribute:: speaker_preferences


.. py:class:: CustomConversationState

   Bases: :py:obj:`haive.agents.conversation.base.ConversationState`


   Extended conversation state with quality tracking.


   .. autolink-examples:: CustomConversationState
      :collapse:

   .. py:attribute:: __reducer_fields__


   .. py:property:: average_quality
      :type: float


      Calculate average conversation quality.

      .. autolink-examples:: average_quality
         :collapse:


   .. py:attribute:: engagement_level
      :type:  float
      :value: None



   .. py:attribute:: quality_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: sentiment_scores
      :type:  dict[str, float]
      :value: None



.. py:function:: main()
   :async:


   Demonstrate custom conversation agent usage.


   .. autolink-examples:: main
      :collapse:

.. py:data:: logger

