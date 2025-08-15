agents.conversation.social_media.state
======================================

.. py:module:: agents.conversation.social_media.state


Attributes
----------

.. autoapisummary::

   agents.conversation.social_media.state.logger


Classes
-------

.. autoapisummary::

   agents.conversation.social_media.state.SocialMediaState


Module Contents
---------------

.. py:class:: SocialMediaState

   Bases: :py:obj:`haive.agents.conversation.base.state.ConversationState`


   Extended state for social media conversations.


   .. autolink-examples:: SocialMediaState
      :collapse:

   .. py:attribute:: engagement_rate
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: followers
      :type:  dict[str, set[str]]
      :value: None



   .. py:attribute:: hashtags_used
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: likes
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: platform_type
      :type:  Literal['twitter', 'instagram', 'tiktok', 'generic']
      :value: None



   .. py:attribute:: posts_count
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: replies
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: shares
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: trending_topics
      :type:  list[str]
      :value: None



   .. py:attribute:: viral_posts
      :type:  list[tuple[str, str]]
      :value: None



   .. py:attribute:: viral_threshold
      :type:  int
      :value: None



.. py:data:: logger

