agents.conversation.directed.state
==================================

.. py:module:: agents.conversation.directed.state

.. autoapi-nested-parse::

   Directed conversation agent where participants respond to mentions and direct questions.


   .. autolink-examples:: agents.conversation.directed.state
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.directed.state.logger


Classes
-------

.. autoapisummary::

   agents.conversation.directed.state.DirectedState


Module Contents
---------------

.. py:class:: DirectedState

   Bases: :py:obj:`haive.agents.conversation.base.state.ConversationState`


   Extended state for directed conversations.


   .. autolink-examples:: DirectedState
      :collapse:

   .. py:attribute:: interaction_count
      :type:  dict[str, dict[str, int]]
      :value: None



   .. py:attribute:: mentioned_speakers
      :type:  list[str]
      :value: None



   .. py:attribute:: pending_speakers
      :type:  list[str]
      :value: None



.. py:data:: logger

