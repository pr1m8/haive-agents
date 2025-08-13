
:py:mod:`agents.simple.state.v2`
================================

.. py:module:: agents.simple.state.v2

State core module.

This module provides state functionality for the Haive framework.

Classes:
    SimpleAgentState: SimpleAgentState implementation.

Functions:
    add_human_message: Add Human Message functionality.
    add_ai_message: Add Ai Message functionality.
    extract_last_message_content: Extract Last Message Content functionality.


.. autolink-examples:: agents.simple.state.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.state.v2.SimpleAgentState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgentState {
        node [shape=record];
        "SimpleAgentState" [label="SimpleAgentState"];
        "haive.core.schema.state_schema.StateSchema" -> "SimpleAgentState";
      }

.. autoclass:: agents.simple.state.v2.SimpleAgentState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.state.v2
   :collapse:
   
.. autolink-skip:: next
