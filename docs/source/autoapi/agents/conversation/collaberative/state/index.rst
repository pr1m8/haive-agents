
:py:mod:`agents.conversation.collaberative.state`
=================================================

.. py:module:: agents.conversation.collaberative.state

State for collaborative conversation agents.


.. autolink-examples:: agents.conversation.collaberative.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.conversation.collaberative.state.CollaborativeState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CollaborativeState:

   .. graphviz::
      :align: center

      digraph inheritance_CollaborativeState {
        node [shape=record];
        "CollaborativeState" [label="CollaborativeState"];
        "haive.agents.conversation.base.state.ConversationState" -> "CollaborativeState";
      }

.. autoclass:: agents.conversation.collaberative.state.CollaborativeState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.conversation.collaberative.state.merge_contribution_counts
   agents.conversation.collaberative.state.merge_document_sections

.. py:function:: merge_contribution_counts(current: dict[str, int], update: dict[str, int]) -> dict[str, int]

   Merge contribution counts by summing values.


   .. autolink-examples:: merge_contribution_counts
      :collapse:

.. py:function:: merge_document_sections(current: dict[str, str], update: dict[str, str]) -> dict[str, str]

   Merge document sections, preserving existing content.


   .. autolink-examples:: merge_document_sections
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.conversation.collaberative.state
   :collapse:
   
.. autolink-skip:: next
