
:py:mod:`agents.memory.multi_agent_coordinator`
===============================================

.. py:module:: agents.memory.multi_agent_coordinator

Multi-Agent Memory Coordinator using MetaStateSchema patterns.

This module provides a comprehensive coordinator that orchestrates multiple
memory agents using the MetaStateSchema pattern for proper state management
and agent composition.


.. autolink-examples:: agents.memory.multi_agent_coordinator
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.multi_agent_coordinator.MemoryAgentCapabilities
   agents.memory.multi_agent_coordinator.MemoryTask
   agents.memory.multi_agent_coordinator.MultiAgentCoordinatorConfig
   agents.memory.multi_agent_coordinator.MultiAgentMemoryCoordinator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryAgentCapabilities:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryAgentCapabilities {
        node [shape=record];
        "MemoryAgentCapabilities" [label="MemoryAgentCapabilities"];
        "pydantic.BaseModel" -> "MemoryAgentCapabilities";
      }

.. autopydantic_model:: agents.memory.multi_agent_coordinator.MemoryAgentCapabilities
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

   Inheritance diagram for MemoryTask:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryTask {
        node [shape=record];
        "MemoryTask" [label="MemoryTask"];
        "pydantic.BaseModel" -> "MemoryTask";
      }

.. autopydantic_model:: agents.memory.multi_agent_coordinator.MemoryTask
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

   Inheritance diagram for MultiAgentCoordinatorConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentCoordinatorConfig {
        node [shape=record];
        "MultiAgentCoordinatorConfig" [label="MultiAgentCoordinatorConfig"];
        "pydantic.BaseModel" -> "MultiAgentCoordinatorConfig";
      }

.. autopydantic_model:: agents.memory.multi_agent_coordinator.MultiAgentCoordinatorConfig
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

   Inheritance diagram for MultiAgentMemoryCoordinator:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgentMemoryCoordinator {
        node [shape=record];
        "MultiAgentMemoryCoordinator" [label="MultiAgentMemoryCoordinator"];
      }

.. autoclass:: agents.memory.multi_agent_coordinator.MultiAgentMemoryCoordinator
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory.multi_agent_coordinator
   :collapse:
   
.. autolink-skip:: next
