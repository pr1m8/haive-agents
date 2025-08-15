agents.conversation.social_media.agent
======================================

.. py:module:: agents.conversation.social_media.agent


Attributes
----------

.. autoapisummary::

   agents.conversation.social_media.agent.logger


Classes
-------

.. autoapisummary::

   agents.conversation.social_media.agent.SocialMediaConversation


Module Contents
---------------

.. py:class:: SocialMediaConversation

   Bases: :py:obj:`haive.agents.conversation.base.agent.BaseConversationAgent`


   Social media style conversation with engagement mechanics.

   Features:
   - Likes and reactions
   - Replies and threads
   - Shares/retweets
   - Viral mechanics
   - Hashtag tracking


   .. autolink-examples:: SocialMediaConversation
      :collapse:

   .. py:method:: _add_social_tools_to_agents()

      Add social media interaction tools to agents.


      .. autolink-examples:: _add_social_tools_to_agents
         :collapse:


   .. py:method:: _check_custom_end_conditions(state: haive.agents.conversation.social_media.state.SocialMediaState) -> dict[str, Any] | None

      Check for viral threshold.


      .. autolink-examples:: _check_custom_end_conditions
         :collapse:


   .. py:method:: _compile_participants()

      Compile participants with social media tools.


      .. autolink-examples:: _compile_participants
         :collapse:


   .. py:method:: _create_conclusion(state: haive.agents.conversation.social_media.state.SocialMediaState, reason: str) -> dict[str, Any]

      Create social media style conclusion.


      .. autolink-examples:: _create_conclusion
         :collapse:


   .. py:method:: _create_initial_message() -> langchain_core.messages.BaseMessage

      Create platform-specific initial message.


      .. autolink-examples:: _create_initial_message
         :collapse:


   .. py:method:: _create_orchestrator_engine() -> haive.core.engine.aug_llm.AugLLMConfig

      Create orchestrator with social media context.


      .. autolink-examples:: _create_orchestrator_engine
         :collapse:


   .. py:method:: _like_post_handler(post_author: str, reason: str | None = None) -> str

      Handler for like_post tool.


      .. autolink-examples:: _like_post_handler
         :collapse:


   .. py:method:: _prepare_agent_input(state: haive.agents.conversation.social_media.state.SocialMediaState, agent_name: str) -> dict[str, Any]

      Prepare input with social media context.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: _reply_post_handler(reply_to: str, content: str) -> str

      Handler for reply_to_post tool.


      .. autolink-examples:: _reply_post_handler
         :collapse:


   .. py:method:: _share_post_handler(original_author: str, comment: str | None = None) -> str

      Handler for share_post tool.


      .. autolink-examples:: _share_post_handler
         :collapse:


   .. py:method:: create_twitter_thread(topic: str, personas: dict[str, str], viral_threshold: int = 10, **kwargs)
      :classmethod:


      Create a Twitter-style conversation thread.

      :param topic: Thread topic
      :param personas: Dictionary mapping names to persona descriptions
      :param viral_threshold: Likes needed to go viral
      :param \*\*kwargs: Additional configuration


      .. autolink-examples:: create_twitter_thread
         :collapse:


   .. py:method:: get_conversation_state_schema() -> type

      Use social media state schema.


      .. autolink-examples:: get_conversation_state_schema
         :collapse:


   .. py:method:: process_response(state: haive.agents.conversation.social_media.state.SocialMediaState) -> dict[str, Any]

      Process social media engagement.


      .. autolink-examples:: process_response
         :collapse:


   .. py:method:: select_speaker(state: haive.agents.conversation.social_media.state.SocialMediaState) -> dict[str, Any]

      Select speakers based on engagement dynamics.


      .. autolink-examples:: select_speaker
         :collapse:


   .. py:attribute:: char_limits
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: enable_likes
      :type:  bool
      :value: None



   .. py:attribute:: enable_reactions
      :type:  bool
      :value: None



   .. py:attribute:: enable_shares
      :type:  bool
      :value: None



   .. py:attribute:: max_posts_per_round
      :type:  int
      :value: None



   .. py:attribute:: mode
      :type:  Literal['social_media']
      :value: None



   .. py:attribute:: platform_type
      :type:  Literal['twitter', 'instagram', 'tiktok', 'generic']
      :value: None



   .. py:attribute:: viral_threshold
      :type:  int
      :value: None



.. py:data:: logger

