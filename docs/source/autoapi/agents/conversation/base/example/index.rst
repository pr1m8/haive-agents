
:py:mod:`agents.conversation.base.example`
==========================================

.. py:module:: agents.conversation.base.example

Base Conversation Agent Example.

This example demonstrates how to create custom conversation agents by extending
the BaseConversationAgent class and implementing core conversation patterns.


.. autolink-examples:: agents.conversation.base.example
   :collapse:

Classes
-------

.. autoapisummary::

   agents.conversation.base.example.CustomConversationAgent
   agents.conversation.base.example.CustomConversationState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CustomConversationAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CustomConversationAgent {
        node [shape=record];
        "CustomConversationAgent" [label="CustomConversationAgent"];
        "haive.agents.conversation.base.BaseConversationAgent" -> "CustomConversationAgent";
      }

.. autoclass:: agents.conversation.base.example.CustomConversationAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CustomConversationState:

   .. graphviz::
      :align: center

      digraph inheritance_CustomConversationState {
        node [shape=record];
        "CustomConversationState" [label="CustomConversationState"];
        "haive.agents.conversation.base.ConversationState" -> "CustomConversationState";
      }

.. autoclass:: agents.conversation.base.example.CustomConversationState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.conversation.base.example.main

.. py:function:: main()
   :async:


   Demonstrate custom conversation agent usage.


   .. autolink-examples:: main
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.conversation.base.example
   :collapse:
   
.. autolink-skip:: next
