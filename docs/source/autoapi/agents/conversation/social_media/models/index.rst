agents.conversation.social_media.models
=======================================

.. py:module:: agents.conversation.social_media.models

.. autoapi-nested-parse::

   Social media style conversation with likes, reactions, and viral mechanics.


   .. autolink-examples:: agents.conversation.social_media.models
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.social_media.models.logger


Classes
-------

.. autoapisummary::

   agents.conversation.social_media.models.LikePostInput
   agents.conversation.social_media.models.ReplyPostInput
   agents.conversation.social_media.models.SharePostInput
   agents.conversation.social_media.models.SocialMediaState


Module Contents
---------------

.. py:class:: LikePostInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for liking a post.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LikePostInput
      :collapse:

   .. py:attribute:: post_author
      :type:  str
      :value: None



   .. py:attribute:: reason
      :type:  str | None
      :value: None



.. py:class:: ReplyPostInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for replying to a post.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReplyPostInput
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: reply_to
      :type:  str
      :value: None



.. py:class:: SharePostInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input for sharing/retweeting a post.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SharePostInput
      :collapse:

   .. py:attribute:: comment
      :type:  str | None
      :value: None



   .. py:attribute:: original_author
      :type:  str
      :value: None



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

