
:py:mod:`agents.experiments.static_supervisor_with_sync`
========================================================

.. py:module:: agents.experiments.static_supervisor_with_sync

Static supervisor inheriting from ReactAgent with tool node modifications.

This supervisor uses ReactAgent's looping behavior but modifies the tool node
to execute agent handoffs stored in state.


.. autolink-examples:: agents.experiments.static_supervisor_with_sync
   :collapse:

Classes
-------

.. autoapisummary::

   agents.experiments.static_supervisor_with_sync.AgentEntry
   agents.experiments.static_supervisor_with_sync.StaticSupervisor
   agents.experiments.static_supervisor_with_sync.SupervisorReactState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentEntry:

   .. graphviz::
      :align: center

      digraph inheritance_AgentEntry {
        node [shape=record];
        "AgentEntry" [label="AgentEntry"];
        "pydantic.BaseModel" -> "AgentEntry";
      }

.. autopydantic_model:: agents.experiments.static_supervisor_with_sync.AgentEntry
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

   Inheritance diagram for StaticSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_StaticSupervisor {
        node [shape=record];
        "StaticSupervisor" [label="StaticSupervisor"];
        "haive.agents.react.agent.ReactAgent" -> "StaticSupervisor";
      }

.. autoclass:: agents.experiments.static_supervisor_with_sync.StaticSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorReactState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorReactState {
        node [shape=record];
        "SupervisorReactState" [label="SupervisorReactState"];
        "haive.core.schema.state_schema.StateSchema" -> "SupervisorReactState";
      }

.. autoclass:: agents.experiments.static_supervisor_with_sync.SupervisorReactState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.experiments.static_supervisor_with_sync
   :collapse:
   
.. autolink-skip:: next
