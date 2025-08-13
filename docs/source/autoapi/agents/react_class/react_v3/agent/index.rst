
:py:mod:`agents.react_class.react_v3.agent`
===========================================

.. py:module:: agents.react_class.react_v3.agent

ReactAgent implementation with tool usage and ReAct pattern.

from typing import Any, Dict
This module implements a tool-using agent that follows the ReAct pattern
(Reasoning, Acting, and Observing) for solving tasks.


.. autolink-examples:: agents.react_class.react_v3.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.react_class.react_v3.agent.ReactAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReactAgent {
        node [shape=record];
        "ReactAgent" [label="ReactAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.react_class.react_v3.config.ReactAgentConfig]" -> "ReactAgent";
      }

.. autoclass:: agents.react_class.react_v3.agent.ReactAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_v3.agent
   :collapse:
   
.. autolink-skip:: next
