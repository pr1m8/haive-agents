
:py:mod:`agents.dynamic_supervisor.state`
=========================================

.. py:module:: agents.dynamic_supervisor.state

State schemas for dynamic supervisor agent.

from typing import Any
This module defines the state management for the dynamic supervisor, including
agent registry, routing control, and tool generation. Two versions are provided:
- SupervisorState: Uses exclude=True for agent serialization (v1)
- SupervisorStateV2: Attempts full agent serialization (experimental)

Classes:
    SupervisorState: Base supervisor state with agent registry
    SupervisorStateWithTools: Extends base with dynamic tool generation
    SupervisorStateV2: Experimental version with full serialization

.. rubric:: Example

Creating and managing supervisor state::

    state = SupervisorState()
    state.add_agent("search", search_agent, "Search specialist")
    state.activate_agent("search")

    # List active agents
    active = state.list_active_agents()


.. autolink-examples:: agents.dynamic_supervisor.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.dynamic_supervisor.state.SupervisorState
   agents.dynamic_supervisor.state.SupervisorStateV2
   agents.dynamic_supervisor.state.SupervisorStateWithTools


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorState {
        node [shape=record];
        "SupervisorState" [label="SupervisorState"];
        "haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage" -> "SupervisorState";
      }

.. autoclass:: agents.dynamic_supervisor.state.SupervisorState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorStateV2:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorStateV2 {
        node [shape=record];
        "SupervisorStateV2" [label="SupervisorStateV2"];
        "haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage" -> "SupervisorStateV2";
      }

.. autoclass:: agents.dynamic_supervisor.state.SupervisorStateV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorStateWithTools:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorStateWithTools {
        node [shape=record];
        "SupervisorStateWithTools" [label="SupervisorStateWithTools"];
        "SupervisorState" -> "SupervisorStateWithTools";
      }

.. autoclass:: agents.dynamic_supervisor.state.SupervisorStateWithTools
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.dynamic_supervisor.state
   :collapse:
   
.. autolink-skip:: next
