
:py:mod:`proper_dynamic_supervisor`
===================================

.. py:module:: proper_dynamic_supervisor

Proper Dynamic Supervisor using correct state extraction patterns.

This implementation follows the EngineNode/AgentNode patterns for proper
state handling and dynamic agent execution without graph rebuilding.


.. autolink-examples:: proper_dynamic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   proper_dynamic_supervisor.MockAgent
   proper_dynamic_supervisor.ProperDynamicSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MockAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MockAgent {
        node [shape=record];
        "MockAgent" [label="MockAgent"];
      }

.. autoclass:: proper_dynamic_supervisor.MockAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProperDynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_ProperDynamicSupervisor {
        node [shape=record];
        "ProperDynamicSupervisor" [label="ProperDynamicSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "ProperDynamicSupervisor";
      }

.. autoclass:: proper_dynamic_supervisor.ProperDynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: proper_dynamic_supervisor
   :collapse:
   
.. autolink-skip:: next
