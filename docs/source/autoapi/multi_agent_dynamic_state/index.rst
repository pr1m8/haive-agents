
:py:mod:`multi_agent_dynamic_state`
===================================

.. py:module:: multi_agent_dynamic_state

Enhanced Multi-Agent State with Dynamic Agent Management.

This module extends the DynamicSupervisorState to include multi-agent coordination
capabilities, agent registry management, and dynamic choice model integration.


.. autolink-examples:: multi_agent_dynamic_state
   :collapse:

Classes
-------

.. autoapisummary::

   multi_agent_dynamic_state.AgentRegistryState
   multi_agent_dynamic_state.MultiAgentCoordinationState
   multi_agent_dynamic_state.MultiAgentDynamicSupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentRegistryState:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRegistryState {
        node [shape=record];
        "AgentRegistryState" [label="AgentRegistryState"];
        "pydantic.BaseModel" -> "AgentRegistryState";
      }

.. autopydantic_model:: multi_agent_dynamic_state.AgentRegistryState
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

   Inheritance diagram for MultiAgentCoordinationState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentCoordinationState {
        node [shape=record];
        "MultiAgentCoordinationState" [label="MultiAgentCoordinationState"];
        "pydantic.BaseModel" -> "MultiAgentCoordinationState";
      }

.. autopydantic_model:: multi_agent_dynamic_state.MultiAgentCoordinationState
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

   Inheritance diagram for MultiAgentDynamicSupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentDynamicSupervisorState {
        node [shape=record];
        "MultiAgentDynamicSupervisorState" [label="MultiAgentDynamicSupervisorState"];
        "haive.agents.supervisor.dynamic_state.DynamicSupervisorState" -> "MultiAgentDynamicSupervisorState";
      }

.. autoclass:: multi_agent_dynamic_state.MultiAgentDynamicSupervisorState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: multi_agent_dynamic_state
   :collapse:
   
.. autolink-skip:: next
