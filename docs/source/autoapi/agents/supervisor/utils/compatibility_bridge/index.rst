
:py:mod:`agents.supervisor.utils.compatibility_bridge`
======================================================

.. py:module:: agents.supervisor.utils.compatibility_bridge

Compatibility Bridge for Dynamic Supervisor with Existing Multi-Agent Architecture.

This module provides integration between the new dynamic supervisor system
and the existing multi-agent base classes, ensuring seamless interoperability.


.. autolink-examples:: agents.supervisor.utils.compatibility_bridge
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.utils.compatibility_bridge.DynamicMultiAgentSupervisor
   agents.supervisor.utils.compatibility_bridge.ReactMultiAgentSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicMultiAgentSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicMultiAgentSupervisor {
        node [shape=record];
        "DynamicMultiAgentSupervisor" [label="DynamicMultiAgentSupervisor"];
        "haive.agents.multi.compatibility.MultiAgent" -> "DynamicMultiAgentSupervisor";
      }

.. autoclass:: agents.supervisor.utils.compatibility_bridge.DynamicMultiAgentSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReactMultiAgentSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_ReactMultiAgentSupervisor {
        node [shape=record];
        "ReactMultiAgentSupervisor" [label="ReactMultiAgentSupervisor"];
        "DynamicMultiAgentSupervisor" -> "ReactMultiAgentSupervisor";
      }

.. autoclass:: agents.supervisor.utils.compatibility_bridge.ReactMultiAgentSupervisor
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.supervisor.utils.compatibility_bridge.create_compatible_supervisor
   agents.supervisor.utils.compatibility_bridge.migrate_from_multi_agent

.. py:function:: create_compatible_supervisor(agents: collections.abc.Sequence[haive.agents.base.agent.Agent], name: str = 'Compatible Supervisor', enable_dynamic: bool = True, supervisor_engine: Any = None) -> DynamicMultiAgentSupervisor | haive.agents.multi.compatibility.MultiAgent

   Factory function to create compatible supervisor based on requirements.

   :param agents: List of agents to manage
   :param name: Name of the supervisor system
   :param enable_dynamic: Whether to enable dynamic capabilities
   :param supervisor_engine: Engine for supervisor decisions

   :returns: Either DynamicMultiAgentSupervisor or standard MultiAgent


   .. autolink-examples:: create_compatible_supervisor
      :collapse:

.. py:function:: migrate_from_multi_agent(multi_agent: haive.agents.multi.compatibility.MultiAgent) -> DynamicMultiAgentSupervisor

   Migrate existing MultiAgent to dynamic supervisor version.

   :param multi_agent: Existing MultiAgent instance

   :returns: DynamicMultiAgentSupervisor with same configuration


   .. autolink-examples:: migrate_from_multi_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.utils.compatibility_bridge
   :collapse:
   
.. autolink-skip:: next
