
:py:mod:`agents.multi.base.agent`
=================================

.. py:module:: agents.multi.base.agent

Base MultiAgent implementation.

This module provides the base multi-agent class that other multi-agent
implementations can inherit from or use directly.


.. autolink-examples:: agents.multi.base.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.base.agent.SequentialAgent
   agents.multi.base.agent.SequentialAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgent {
        node [shape=record];
        "SequentialAgent" [label="SequentialAgent"];
        "haive.core.engine.agent.Agent" -> "SequentialAgent";
      }

.. autoclass:: agents.multi.base.agent.SequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgentConfig {
        node [shape=record];
        "SequentialAgentConfig" [label="SequentialAgentConfig"];
        "haive.core.engine.agent.AgentConfig" -> "SequentialAgentConfig";
      }

.. autoclass:: agents.multi.base.agent.SequentialAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.base.agent
   :collapse:
   
.. autolink-skip:: next
