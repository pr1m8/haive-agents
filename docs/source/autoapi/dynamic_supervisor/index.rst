
:py:mod:`dynamic_supervisor`
============================

.. py:module:: dynamic_supervisor

Dynamic LangGraph-style Supervisor Implementation.

This module provides a dynamic supervisor agent that can add/remove agents at runtime,
adapt agent responses, and handle complex multi-agent coordination patterns similar
to LangGraph's supervisor package but with enhanced Haive-specific functionality.


.. autolink-examples:: dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   dynamic_supervisor.DynamicSupervisorAgent
   dynamic_supervisor.PerformanceMonitor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorAgent {
        node [shape=record];
        "DynamicSupervisorAgent" [label="DynamicSupervisorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisorAgent";
      }

.. autoclass:: dynamic_supervisor.DynamicSupervisorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PerformanceMonitor:

   .. graphviz::
      :align: center

      digraph inheritance_PerformanceMonitor {
        node [shape=record];
        "PerformanceMonitor" [label="PerformanceMonitor"];
      }

.. autoclass:: dynamic_supervisor.PerformanceMonitor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
