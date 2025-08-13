
:py:mod:`agents.dynamic_supervisor.models`
==========================================

.. py:module:: agents.dynamic_supervisor.models

Data models for dynamic supervisor agent.

This module contains Pydantic models used by the dynamic supervisor for
agent metadata, routing information, and configuration.

Classes:
    AgentInfo: Metadata container for agents (v1 with exclusion)
    AgentInfoV2: Experimental version with full serialization
    AgentRequest: Model for agent addition requests
    RoutingDecision: Model for routing decisions

.. rubric:: Example

Creating agent metadata::

    info = AgentInfo(
        agent=search_agent,
        name="search",
        description="Web search specialist",
        active=True
    )


.. autolink-examples:: agents.dynamic_supervisor.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.dynamic_supervisor.models.AgentInfo
   agents.dynamic_supervisor.models.AgentInfoV2
   agents.dynamic_supervisor.models.AgentRequest
   agents.dynamic_supervisor.models.RoutingDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentInfo:

   .. graphviz::
      :align: center

      digraph inheritance_AgentInfo {
        node [shape=record];
        "AgentInfo" [label="AgentInfo"];
        "pydantic.BaseModel" -> "AgentInfo";
      }

.. autopydantic_model:: agents.dynamic_supervisor.models.AgentInfo
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

   Inheritance diagram for AgentInfoV2:

   .. graphviz::
      :align: center

      digraph inheritance_AgentInfoV2 {
        node [shape=record];
        "AgentInfoV2" [label="AgentInfoV2"];
        "pydantic.BaseModel" -> "AgentInfoV2";
      }

.. autopydantic_model:: agents.dynamic_supervisor.models.AgentInfoV2
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

   Inheritance diagram for AgentRequest:

   .. graphviz::
      :align: center

      digraph inheritance_AgentRequest {
        node [shape=record];
        "AgentRequest" [label="AgentRequest"];
        "pydantic.BaseModel" -> "AgentRequest";
      }

.. autopydantic_model:: agents.dynamic_supervisor.models.AgentRequest
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

   Inheritance diagram for RoutingDecision:

   .. graphviz::
      :align: center

      digraph inheritance_RoutingDecision {
        node [shape=record];
        "RoutingDecision" [label="RoutingDecision"];
        "pydantic.BaseModel" -> "RoutingDecision";
      }

.. autopydantic_model:: agents.dynamic_supervisor.models.RoutingDecision
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

.. autolink-examples:: agents.dynamic_supervisor.models
   :collapse:
   
.. autolink-skip:: next
