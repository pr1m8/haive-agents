
:py:mod:`agents.experiments.supervisor.state_models`
====================================================

.. py:module:: agents.experiments.supervisor.state_models

State models for supervisor agents.

This module defines the state schemas and data models used by supervisor agents
for managing multi-agent systems.


.. autolink-examples:: agents.experiments.supervisor.state_models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.experiments.supervisor.state_models.AgentMetadata
   agents.experiments.supervisor.state_models.DynamicSupervisorState
   agents.experiments.supervisor.state_models.ExecutionContext
   agents.experiments.supervisor.state_models.SerializedAgent
   agents.experiments.supervisor.state_models.SupervisorState
   agents.experiments.supervisor.state_models.ToolMapping


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

.. autopydantic_model:: agents.experiments.supervisor.state_models.AgentMetadata
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
        "SupervisorState" -> "DynamicSupervisorState";
      }

.. autoclass:: agents.experiments.supervisor.state_models.DynamicSupervisorState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionContext:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionContext {
        node [shape=record];
        "ExecutionContext" [label="ExecutionContext"];
        "pydantic.BaseModel" -> "ExecutionContext";
      }

.. autopydantic_model:: agents.experiments.supervisor.state_models.ExecutionContext
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

   Inheritance diagram for SerializedAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SerializedAgent {
        node [shape=record];
        "SerializedAgent" [label="SerializedAgent"];
        "pydantic.BaseModel" -> "SerializedAgent";
      }

.. autopydantic_model:: agents.experiments.supervisor.state_models.SerializedAgent
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

   Inheritance diagram for SupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorState {
        node [shape=record];
        "SupervisorState" [label="SupervisorState"];
        "pydantic.BaseModel" -> "SupervisorState";
      }

.. autopydantic_model:: agents.experiments.supervisor.state_models.SupervisorState
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

   Inheritance diagram for ToolMapping:

   .. graphviz::
      :align: center

      digraph inheritance_ToolMapping {
        node [shape=record];
        "ToolMapping" [label="ToolMapping"];
        "pydantic.BaseModel" -> "ToolMapping";
      }

.. autopydantic_model:: agents.experiments.supervisor.state_models.ToolMapping
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

.. autolink-examples:: agents.experiments.supervisor.state_models
   :collapse:
   
.. autolink-skip:: next
