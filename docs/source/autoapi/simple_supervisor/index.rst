
:py:mod:`simple_supervisor`
===========================

.. py:module:: simple_supervisor

Simple Supervisor Agent - Clean implementation for agent coordination.

This supervisor uses an LLM to route between multiple agents based on
the conversation context and agent capabilities.


.. autolink-examples:: simple_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   simple_supervisor.AgentInfo
   simple_supervisor.SimpleSupervisor


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

.. autopydantic_model:: simple_supervisor.AgentInfo
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

   Inheritance diagram for SimpleSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleSupervisor {
        node [shape=record];
        "SimpleSupervisor" [label="SimpleSupervisor"];
        "haive.agents.multi.agent.MultiAgent" -> "SimpleSupervisor";
      }

.. autoclass:: simple_supervisor.SimpleSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: simple_supervisor
   :collapse:
   
.. autolink-skip:: next
