
:py:mod:`agents.base.universal_agent`
=====================================

.. py:module:: agents.base.universal_agent

Universal Agent - Simplified base class for all agent types.

This module provides a simplified Agent base class that maintains familiar
naming while providing clear type-based capabilities and proper separation
of concerns through agent types rather than complex inheritance hierarchies.


.. autolink-examples:: agents.base.universal_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.universal_agent.Agent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Agent:

   .. graphviz::
      :align: center

      digraph inheritance_Agent {
        node [shape=record];
        "Agent" [label="Agent"];
        "pydantic.BaseModel" -> "Agent";
        "abc.ABC" -> "Agent";
      }

.. autopydantic_model:: agents.base.universal_agent.Agent
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



Functions
---------

.. autoapisummary::

   agents.base.universal_agent.get_agent_capabilities
   agents.base.universal_agent.is_orchestration_agent
   agents.base.universal_agent.is_processing_agent
   agents.base.universal_agent.is_reasoning_agent

.. py:function:: get_agent_capabilities(agent_type: haive.core.engine.base.agent_types.AgentType) -> dict[str, bool]

   Get capabilities for agent type.


   .. autolink-examples:: get_agent_capabilities
      :collapse:

.. py:function:: is_orchestration_agent(agent_type: haive.core.engine.base.agent_types.AgentType) -> bool

   Check if agent type orchestrates other agents.


   .. autolink-examples:: is_orchestration_agent
      :collapse:

.. py:function:: is_processing_agent(agent_type: haive.core.engine.base.agent_types.AgentType) -> bool

   Check if agent type is for deterministic processing.


   .. autolink-examples:: is_processing_agent
      :collapse:

.. py:function:: is_reasoning_agent(agent_type: haive.core.engine.base.agent_types.AgentType) -> bool

   Check if agent type has reasoning capabilities.


   .. autolink-examples:: is_reasoning_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.base.universal_agent
   :collapse:
   
.. autolink-skip:: next
