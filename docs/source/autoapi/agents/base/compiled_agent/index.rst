
:py:mod:`agents.base.compiled_agent`
====================================

.. py:module:: agents.base.compiled_agent

CompiledAgent - Agent class based on CompiledStateGraph architecture.

This module provides the new CompiledAgent class that inherits from CompiledStateGraph
while maintaining compatibility with the existing Agent interface. This class represents
the future direction for agent architecture in the Haive framework.


.. autolink-examples:: agents.base.compiled_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.compiled_agent.CompiledAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompiledAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CompiledAgent {
        node [shape=record];
        "CompiledAgent" [label="CompiledAgent"];
        "haive.core.graph.state_graph.compiled_state_graph.CompiledStateGraph" -> "CompiledAgent";
        "haive.agents.base.mixins.execution_mixin.ExecutionMixin" -> "CompiledAgent";
        "haive.agents.base.mixins.state_mixin.StateMixin" -> "CompiledAgent";
        "haive.agents.base.mixins.persistence_mixin.PersistenceMixin" -> "CompiledAgent";
        "haive.agents.base.serialization_mixin.SerializationMixin" -> "CompiledAgent";
      }

.. autoclass:: agents.base.compiled_agent.CompiledAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.base.compiled_agent
   :collapse:
   
.. autolink-skip:: next
