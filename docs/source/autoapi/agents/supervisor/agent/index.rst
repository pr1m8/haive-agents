
:py:mod:`agents.supervisor.agent`
=================================

.. py:module:: agents.supervisor.agent

Dynamic Supervisor V2 - Main agent implementation.

This module contains the core DynamicSupervisor class that orchestrates
runtime agent discovery, creation, and task routing.


.. autolink-examples:: agents.supervisor.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.agent.DynamicSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisor {
        node [shape=record];
        "DynamicSupervisor" [label="DynamicSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisor";
      }

.. autoclass:: agents.supervisor.agent.DynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.supervisor.agent.create_dynamic_supervisor

.. py:function:: create_dynamic_supervisor(name: str = 'dynamic_supervisor', agent_specs: list[haive.agents.supervisor.models.AgentSpec] | None = None, discovery_mode: haive.agents.supervisor.models.AgentDiscoveryMode = AgentDiscoveryMode.MANUAL, **kwargs) -> DynamicSupervisor

   Factory function to create a configured dynamic supervisor.

   :param name: Supervisor name
   :param agent_specs: Initial agent specifications
   :param discovery_mode: How to discover new agents
   :param \*\*kwargs: Additional configuration

   :returns: Configured DynamicSupervisor instance

   .. rubric:: Example

   >>> supervisor = create_dynamic_supervisor(
   ...     name="task_router",
   ...     agent_specs=[math_spec, research_spec],
   ...     discovery_mode="manual",
   ...     max_agents=20
   ... )


   .. autolink-examples:: create_dynamic_supervisor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.agent
   :collapse:
   
.. autolink-skip:: next
