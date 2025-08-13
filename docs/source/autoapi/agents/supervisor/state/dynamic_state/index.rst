
:py:mod:`agents.supervisor.state.dynamic_state`
===============================================

.. py:module:: agents.supervisor.state.dynamic_state

Enhanced state schema for dynamic supervisor operations.

This module provides an enhanced state management system for dynamic supervisor
agents that can add/remove agents at runtime and adapt their responses based
on agent configuration and execution context.


.. autolink-examples:: agents.supervisor.state.dynamic_state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.state.dynamic_state.AgentExecutionConfig
   agents.supervisor.state.dynamic_state.AgentExecutionResult
   agents.supervisor.state.dynamic_state.DynamicSupervisorState
   agents.supervisor.state.dynamic_state.SupervisorDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentExecutionConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AgentExecutionConfig {
        node [shape=record];
        "AgentExecutionConfig" [label="AgentExecutionConfig"];
        "pydantic.BaseModel" -> "AgentExecutionConfig";
      }

.. autopydantic_model:: agents.supervisor.state.dynamic_state.AgentExecutionConfig
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

   Inheritance diagram for AgentExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_AgentExecutionResult {
        node [shape=record];
        "AgentExecutionResult" [label="AgentExecutionResult"];
        "pydantic.BaseModel" -> "AgentExecutionResult";
      }

.. autopydantic_model:: agents.supervisor.state.dynamic_state.AgentExecutionResult
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

   Inheritance diagram for DynamicSupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorState {
        node [shape=record];
        "DynamicSupervisorState" [label="DynamicSupervisorState"];
        "haive.core.schema.state_schema.StateSchema" -> "DynamicSupervisorState";
      }

.. autoclass:: agents.supervisor.state.dynamic_state.DynamicSupervisorState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorDecision:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorDecision {
        node [shape=record];
        "SupervisorDecision" [label="SupervisorDecision"];
        "pydantic.BaseModel" -> "SupervisorDecision";
      }

.. autopydantic_model:: agents.supervisor.state.dynamic_state.SupervisorDecision
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

.. autolink-examples:: agents.supervisor.state.dynamic_state
   :collapse:
   
.. autolink-skip:: next
