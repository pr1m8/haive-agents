agents.conversation.collaberative.state
=======================================

.. py:module:: agents.conversation.collaberative.state

.. autoapi-nested-parse::

   State for collaborative conversation agents.


   .. autolink-examples:: agents.conversation.collaberative.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.conversation.collaberative.state.CollaborativeState


Functions
---------

.. autoapisummary::

   agents.conversation.collaberative.state.merge_contribution_counts
   agents.conversation.collaberative.state.merge_document_sections


Module Contents
---------------

.. py:class:: CollaborativeState

   Bases: :py:obj:`haive.agents.conversation.base.state.ConversationState`


   Extended state for collaborative conversations.


   .. autolink-examples:: CollaborativeState
      :collapse:

   .. py:attribute:: __reducer_fields__


   .. py:attribute:: approvals
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: completed_sections
      :type:  list[str]
      :value: None



   .. py:attribute:: contribution_count
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: contributions
      :type:  list[tuple[str, str, str]]
      :value: None



   .. py:attribute:: current_section
      :type:  str | None
      :value: None



   .. py:attribute:: document_sections
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: output_format
      :type:  Literal['markdown', 'code', 'outline', 'report']
      :value: None



   .. py:attribute:: pending_reviews
      :type:  list[tuple[str, str]]
      :value: None



   .. py:attribute:: sections_order
      :type:  list[str]
      :value: None



   .. py:attribute:: shared_document
      :type:  str
      :value: None



.. py:function:: merge_contribution_counts(current: dict[str, int], update: dict[str, int]) -> dict[str, int]

   Merge contribution counts by summing values.


   .. autolink-examples:: merge_contribution_counts
      :collapse:

.. py:function:: merge_document_sections(current: dict[str, str], update: dict[str, str]) -> dict[str, str]

   Merge document sections, preserving existing content.


   .. autolink-examples:: merge_document_sections
      :collapse:

