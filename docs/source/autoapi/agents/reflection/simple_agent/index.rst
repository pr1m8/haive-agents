
:py:mod:`agents.reflection.simple_agent`
========================================

.. py:module:: agents.reflection.simple_agent

Simple Reflection Agent using clean MultiAgent pattern.


.. autolink-examples:: agents.reflection.simple_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.simple_agent.ReflectionAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReflectionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionAgent {
        node [shape=record];
        "ReflectionAgent" [label="ReflectionAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "ReflectionAgent";
      }

.. autoclass:: agents.reflection.simple_agent.ReflectionAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reflection.simple_agent.create
   agents.reflection.simple_agent.enhance_agent

.. py:function:: create(*args, **kwargs) -> ReflectionAgent

   Create a simple reflection agent.


   .. autolink-examples:: create
      :collapse:

.. py:function:: enhance_agent(base_agent: Any, **kwargs) -> ReflectionAgent

   Enhance any agent with reflection capability.


   .. autolink-examples:: enhance_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.simple_agent
   :collapse:
   
.. autolink-skip:: next
