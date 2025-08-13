
:py:mod:`agents.planning.rewoo_v3.agent`
========================================

.. py:module:: agents.planning.rewoo_v3.agent

ReWOO V3 Agent using Enhanced MultiAgent V3 coordination.

This module implements the ReWOO (Reasoning WithOut Observation) methodology
using our proven patterns from Plan-and-Execute V3 success.

ReWOO Architecture:
1. Planner: Creates complete reasoning plan with evidence placeholders
2. Worker: Executes all tool calls to collect evidence
3. Solver: Synthesizes all evidence into final answer

Key advantages:
- Token efficiency (5x improvement over iterative methods)
- Parallel tool execution capability
- Robust to partial failures
- Fine-tuning friendly modular design


.. autolink-examples:: agents.planning.rewoo_v3.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.agent.EvidenceCollection
   agents.planning.rewoo_v3.agent.ReWOOPlan
   agents.planning.rewoo_v3.agent.ReWOOSolution
   agents.planning.rewoo_v3.agent.ReWOOV3Agent
   agents.planning.rewoo_v3.agent.ReWOOV3Input
   agents.planning.rewoo_v3.agent.ReWOOV3Output
   agents.planning.rewoo_v3.agent.ReWOOV3State


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EvidenceCollection:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceCollection {
        node [shape=record];
        "EvidenceCollection" [label="EvidenceCollection"];
        "pydantic.BaseModel" -> "EvidenceCollection";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.agent.EvidenceCollection
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlan {
        node [shape=record];
        "ReWOOPlan" [label="ReWOOPlan"];
        "pydantic.BaseModel" -> "ReWOOPlan";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.agent.ReWOOPlan
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOSolution {
        node [shape=record];
        "ReWOOSolution" [label="ReWOOSolution"];
        "pydantic.BaseModel" -> "ReWOOSolution";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.agent.ReWOOSolution
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

   Inheritance diagram for ReWOOV3Agent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Agent {
        node [shape=record];
        "ReWOOV3Agent" [label="ReWOOV3Agent"];
      }

.. autoclass:: agents.planning.rewoo_v3.agent.ReWOOV3Agent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOV3Input:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Input {
        node [shape=record];
        "ReWOOV3Input" [label="ReWOOV3Input"];
        "pydantic.BaseModel" -> "ReWOOV3Input";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.agent.ReWOOV3Input
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOV3Output:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Output {
        node [shape=record];
        "ReWOOV3Output" [label="ReWOOV3Output"];
        "pydantic.BaseModel" -> "ReWOOV3Output";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.agent.ReWOOV3Output
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOV3State:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3State {
        node [shape=record];
        "ReWOOV3State" [label="ReWOOV3State"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "ReWOOV3State";
      }

.. autoclass:: agents.planning.rewoo_v3.agent.ReWOOV3State
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo_v3.agent
   :collapse:
   
.. autolink-skip:: next
