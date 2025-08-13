
:py:mod:`agents.experiments.supervisor.base_supervisor`
=======================================================

.. py:module:: agents.experiments.supervisor.base_supervisor

Base supervisor implementation for multi-agent systems.

This module provides the core supervisor classes that can manage multiple agents,
handle tool synchronization, and support dynamic agent creation.


.. autolink-examples:: agents.experiments.supervisor.base_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   agents.experiments.supervisor.base_supervisor.AgentMetadata
   agents.experiments.supervisor.base_supervisor.BaseSupervisor
   agents.experiments.supervisor.base_supervisor.DynamicSupervisor
   agents.experiments.supervisor.base_supervisor.SupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_AgentMetadata {
        node [shape=record];
        "AgentMetadata" [label="AgentMetadata"];
        "pydantic.BaseModel" -> "AgentMetadata";
      }

.. autopydantic_model:: agents.experiments.supervisor.base_supervisor.AgentMetadata
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_BaseSupervisor {
        node [shape=record];
        "BaseSupervisor" [label="BaseSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "BaseSupervisor";
      }

.. autoclass:: agents.experiments.supervisor.base_supervisor.BaseSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisor {
        node [shape=record];
        "DynamicSupervisor" [label="DynamicSupervisor"];
        "BaseSupervisor" -> "DynamicSupervisor";
      }

.. autoclass:: agents.experiments.supervisor.base_supervisor.DynamicSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorState {
        node [shape=record];
        "SupervisorState" [label="SupervisorState"];
        "pydantic.BaseModel" -> "SupervisorState";
      }

.. autopydantic_model:: agents.experiments.supervisor.base_supervisor.SupervisorState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: agents.experiments.supervisor.base_supervisor
   :collapse:
   
.. autolink-skip:: next
