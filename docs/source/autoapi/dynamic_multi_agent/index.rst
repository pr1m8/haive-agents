
:py:mod:`dynamic_multi_agent`
=============================

.. py:module:: dynamic_multi_agent

Dynamic Multi-Agent Supervisor with Dynamic Execution Pattern.

This implementation integrates with the MultiAgent base class and uses
dynamic agent execution without graph rebuilding.


.. autolink-examples:: dynamic_multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_multi_agent.DynamicMultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicMultiAgent {
        node [shape=record];
        "DynamicMultiAgent" [label="DynamicMultiAgent"];
        "haive.agents.multi.MultiAgent" -> "DynamicMultiAgent";
      }

.. autoclass:: dynamic_multi_agent.DynamicMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   dynamic_multi_agent.create_dynamic_multi_agent

.. py:function:: create_dynamic_multi_agent(agents: list[haive.agents.base.agent.Agent], name: str = 'DynamicMultiAgent', **kwargs) -> DynamicMultiAgent

   Create a dynamic multi-agent system.

   :param agents: List of agents to include
   :param name: Name for the multi-agent system
   :param \*\*kwargs: Additional configuration

   :returns: DynamicMultiAgent instance


   .. autolink-examples:: create_dynamic_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: dynamic_multi_agent
   :collapse:
   
.. autolink-skip:: next
