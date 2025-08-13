
:py:mod:`agents.base.agent_with_token_tracking`
===============================================

.. py:module:: agents.base.agent_with_token_tracking

Agent base class with integrated token usage tracking.

This module provides an enhanced Agent base class that automatically tracks
token usage for all LLM interactions, providing cost analysis and capacity
monitoring capabilities.


.. autolink-examples:: agents.base.agent_with_token_tracking
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.agent_with_token_tracking.TokenTrackingAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TokenTrackingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TokenTrackingAgent {
        node [shape=record];
        "TokenTrackingAgent" [label="TokenTrackingAgent"];
        "haive.agents.base.agent.Agent" -> "TokenTrackingAgent";
      }

.. autoclass:: agents.base.agent_with_token_tracking.TokenTrackingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.base.agent_with_token_tracking
   :collapse:
   
.. autolink-skip:: next
