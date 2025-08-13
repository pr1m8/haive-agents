
:py:mod:`rebuild_dynamic_supervisor`
====================================

.. py:module:: rebuild_dynamic_supervisor

Dynamic Supervisor with Proper Graph Rebuilding.

This implementation correctly rebuilds the graph when agents are added/removed,
following the Agent base class patterns.


.. autolink-examples:: rebuild_dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   rebuild_dynamic_supervisor.RebuildDynamicSupervisor
   rebuild_dynamic_supervisor.TestAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RebuildDynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_RebuildDynamicSupervisor {
        node [shape=record];
        "RebuildDynamicSupervisor" [label="RebuildDynamicSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "RebuildDynamicSupervisor";
      }

.. autoclass:: rebuild_dynamic_supervisor.RebuildDynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TestAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TestAgent {
        node [shape=record];
        "TestAgent" [label="TestAgent"];
      }

.. autoclass:: rebuild_dynamic_supervisor.TestAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: rebuild_dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
