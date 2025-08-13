
:py:mod:`agents.conversation.social_media.models`
=================================================

.. py:module:: agents.conversation.social_media.models

Social media style conversation with likes, reactions, and viral mechanics.


.. autolink-examples:: agents.conversation.social_media.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.conversation.social_media.models.LikePostInput
   agents.conversation.social_media.models.ReplyPostInput
   agents.conversation.social_media.models.SharePostInput
   agents.conversation.social_media.models.SocialMediaState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LikePostInput:

   .. graphviz::
      :align: center

      digraph inheritance_LikePostInput {
        node [shape=record];
        "LikePostInput" [label="LikePostInput"];
        "pydantic.BaseModel" -> "LikePostInput";
      }

.. autopydantic_model:: agents.conversation.social_media.models.LikePostInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReplyPostInput:

   .. graphviz::
      :align: center

      digraph inheritance_ReplyPostInput {
        node [shape=record];
        "ReplyPostInput" [label="ReplyPostInput"];
        "pydantic.BaseModel" -> "ReplyPostInput";
      }

.. autopydantic_model:: agents.conversation.social_media.models.ReplyPostInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SharePostInput:

   .. graphviz::
      :align: center

      digraph inheritance_SharePostInput {
        node [shape=record];
        "SharePostInput" [label="SharePostInput"];
        "pydantic.BaseModel" -> "SharePostInput";
      }

.. autopydantic_model:: agents.conversation.social_media.models.SharePostInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SocialMediaState:

   .. graphviz::
      :align: center

      digraph inheritance_SocialMediaState {
        node [shape=record];
        "SocialMediaState" [label="SocialMediaState"];
        "haive.agents.conversation.base.state.ConversationState" -> "SocialMediaState";
      }

.. autoclass:: agents.conversation.social_media.models.SocialMediaState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.conversation.social_media.models
   :collapse:
   
.. autolink-skip:: next
