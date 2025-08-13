
:py:mod:`agents.supervisor.models`
==================================

.. py:module:: agents.supervisor.models

Data models for Dynamic Supervisor V2.

This module contains all the Pydantic models and enums used by the dynamic supervisor
for agent specifications, capabilities, and configuration.


.. autolink-examples:: agents.supervisor.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.supervisor.models.AgentCapability
   agents.supervisor.models.AgentDiscoveryMode
   agents.supervisor.models.AgentSpec
   agents.supervisor.models.DiscoveryConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentCapability:

   .. graphviz::
      :align: center

      digraph inheritance_AgentCapability {
        node [shape=record];
        "AgentCapability" [label="AgentCapability"];
        "pydantic.BaseModel" -> "AgentCapability";
      }

.. autopydantic_model:: agents.supervisor.models.AgentCapability
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

   Inheritance diagram for AgentDiscoveryMode:

   .. graphviz::
      :align: center

      digraph inheritance_AgentDiscoveryMode {
        node [shape=record];
        "AgentDiscoveryMode" [label="AgentDiscoveryMode"];
        "str" -> "AgentDiscoveryMode";
        "enum.Enum" -> "AgentDiscoveryMode";
      }

.. autoclass:: agents.supervisor.models.AgentDiscoveryMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **AgentDiscoveryMode** is an Enum defined in ``agents.supervisor.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentSpec:

   .. graphviz::
      :align: center

      digraph inheritance_AgentSpec {
        node [shape=record];
        "AgentSpec" [label="AgentSpec"];
        "pydantic.BaseModel" -> "AgentSpec";
      }

.. autopydantic_model:: agents.supervisor.models.AgentSpec
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

   Inheritance diagram for DiscoveryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_DiscoveryConfig {
        node [shape=record];
        "DiscoveryConfig" [label="DiscoveryConfig"];
        "pydantic.BaseModel" -> "DiscoveryConfig";
      }

.. autopydantic_model:: agents.supervisor.models.DiscoveryConfig
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

.. autolink-examples:: agents.supervisor.models
   :collapse:
   
.. autolink-skip:: next
