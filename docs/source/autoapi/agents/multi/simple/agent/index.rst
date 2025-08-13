
:py:mod:`agents.multi.simple.agent`
===================================

.. py:module:: agents.multi.simple.agent

Simple Multi-Agent implementation for basic multi-agent coordination.

This module provides a simplified multi-agent system that focuses on ease of use
and straightforward coordination patterns without complex orchestration.


.. autolink-examples:: agents.multi.simple.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.simple.agent.SimpleMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleMultiAgent {
        node [shape=record];
        "SimpleMultiAgent" [label="SimpleMultiAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "SimpleMultiAgent";
      }

.. autoclass:: agents.multi.simple.agent.SimpleMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.multi.simple.agent.create_simple_conditional
   agents.multi.simple.agent.create_simple_parallel
   agents.multi.simple.agent.create_simple_sequential

.. py:function:: create_simple_conditional(*agents: haive.core.engine.agent.Agent, name: str = 'simple_conditional') -> SimpleMultiAgent

   Create a simple conditional multi-agent using enhanced pattern.


   .. autolink-examples:: create_simple_conditional
      :collapse:

.. py:function:: create_simple_parallel(*agents: haive.core.engine.agent.Agent, name: str = 'simple_parallel') -> SimpleMultiAgent

   Create a simple parallel multi-agent using enhanced pattern.


   .. autolink-examples:: create_simple_parallel
      :collapse:

.. py:function:: create_simple_sequential(*agents: haive.core.engine.agent.Agent, name: str = 'simple_sequential') -> SimpleMultiAgent

   Create a simple sequential multi-agent using enhanced pattern.


   .. autolink-examples:: create_simple_sequential
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.multi.simple.agent
   :collapse:
   
.. autolink-skip:: next
