
:py:mod:`dynamic_activation_supervisor`
=======================================

.. py:module:: dynamic_activation_supervisor

Dynamic Activation Supervisor for Component Management.

This module provides DynamicActivationSupervisor, a supervisor agent that can
dynamically activate components based on task requirements using the Dynamic
Activation Pattern with MetaStateSchema integration.

Based on:
- @project_docs/active/patterns/dynamic_activation_pattern.md
- @packages/haive-agents/examples/supervisor/advanced/dynamic_activation_example.py

Implementation Notes:
- Uses factory methods for complex initialization (no __init__ override)
- Private attributes for internal state (_discovery_agent)
- MetaStateSchema for component wrapping
- DynamicActivationState as state schema
- Proper Pydantic patterns throughout


.. autolink-examples:: dynamic_activation_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_activation_supervisor.DynamicActivationSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicActivationSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicActivationSupervisor {
        node [shape=record];
        "DynamicActivationSupervisor" [label="DynamicActivationSupervisor"];
        "haive.agents.base.agent.Agent" -> "DynamicActivationSupervisor";
      }

.. autoclass:: dynamic_activation_supervisor.DynamicActivationSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: dynamic_activation_supervisor
   :collapse:
   
.. autolink-skip:: next
