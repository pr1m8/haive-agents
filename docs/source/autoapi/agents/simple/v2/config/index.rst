
:py:mod:`agents.simple.v2.config`
=================================

.. py:module:: agents.simple.v2.config

Simple agent implementation with comprehensive schema handling.

This module defines a basic single-node agent that uses AugLLMConfig for reasoning,
with support for structured outputs, schema composition, and explicit input/output schemas.


.. autolink-examples:: agents.simple.v2.config
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.v2.config.SimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgent {
        node [shape=record];
        "SimpleAgent" [label="SimpleAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.simple.config.SimpleAgentConfig]" -> "SimpleAgent";
      }

.. autoclass:: agents.simple.v2.config.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.simple.v2.config
   :collapse:
   
.. autolink-skip:: next
