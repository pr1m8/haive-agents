
:py:mod:`agents.discovery.component_discovery_agent`
====================================================

.. py:module:: agents.discovery.component_discovery_agent

Component Discovery Agent for Dynamic Activation.

This module provides ComponentDiscoveryAgent, a RAG-based agent for discovering
components from documentation. It uses MetaStateSchema for tracking and follows
the Dynamic Activation Pattern.

Based on: @project_docs/active/patterns/dynamic_activation_pattern.md


.. autolink-examples:: agents.discovery.component_discovery_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.discovery.component_discovery_agent.ComponentDiscoveryAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ComponentDiscoveryAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ComponentDiscoveryAgent {
        node [shape=record];
        "ComponentDiscoveryAgent" [label="ComponentDiscoveryAgent"];
        "pydantic.BaseModel" -> "ComponentDiscoveryAgent";
      }

.. autopydantic_model:: agents.discovery.component_discovery_agent.ComponentDiscoveryAgent
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

.. autolink-examples:: agents.discovery.component_discovery_agent
   :collapse:
   
.. autolink-skip:: next
