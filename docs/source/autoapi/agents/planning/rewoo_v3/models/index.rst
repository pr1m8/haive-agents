
:py:mod:`agents.planning.rewoo_v3.models`
=========================================

.. py:module:: agents.planning.rewoo_v3.models

Pydantic models for ReWOO V3 Agent.

This module defines structured output models for the ReWOO (Reasoning without Observation)
methodology using Enhanced MultiAgent V3.

Key Models:
- ReWOOPlan: Planner agent structured output with evidence placeholders
- EvidenceItem: Individual evidence collected by worker
- EvidenceCollection: Worker agent structured output with all evidence
- ReWOOSolution: Solver agent final answer with reasoning


.. autolink-examples:: agents.planning.rewoo_v3.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.models.EvidenceCollection
   agents.planning.rewoo_v3.models.EvidenceItem
   agents.planning.rewoo_v3.models.EvidenceStatus
   agents.planning.rewoo_v3.models.PlanStep
   agents.planning.rewoo_v3.models.ReWOOPlan
   agents.planning.rewoo_v3.models.ReWOOSolution
   agents.planning.rewoo_v3.models.ReWOOV3Input
   agents.planning.rewoo_v3.models.ReWOOV3Output


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EvidenceCollection:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceCollection {
        node [shape=record];
        "EvidenceCollection" [label="EvidenceCollection"];
        "pydantic.BaseModel" -> "EvidenceCollection";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.EvidenceCollection
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

   Inheritance diagram for EvidenceItem:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceItem {
        node [shape=record];
        "EvidenceItem" [label="EvidenceItem"];
        "pydantic.BaseModel" -> "EvidenceItem";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.EvidenceItem
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

   Inheritance diagram for EvidenceStatus:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceStatus {
        node [shape=record];
        "EvidenceStatus" [label="EvidenceStatus"];
        "str" -> "EvidenceStatus";
        "enum.Enum" -> "EvidenceStatus";
      }

.. autoclass:: agents.planning.rewoo_v3.models.EvidenceStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **EvidenceStatus** is an Enum defined in ``agents.planning.rewoo_v3.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanStep:

   .. graphviz::
      :align: center

      digraph inheritance_PlanStep {
        node [shape=record];
        "PlanStep" [label="PlanStep"];
        "pydantic.BaseModel" -> "PlanStep";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.PlanStep
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

   Inheritance diagram for ReWOOPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlan {
        node [shape=record];
        "ReWOOPlan" [label="ReWOOPlan"];
        "pydantic.BaseModel" -> "ReWOOPlan";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.ReWOOPlan
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

   Inheritance diagram for ReWOOSolution:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOSolution {
        node [shape=record];
        "ReWOOSolution" [label="ReWOOSolution"];
        "pydantic.BaseModel" -> "ReWOOSolution";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.ReWOOSolution
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

   Inheritance diagram for ReWOOV3Input:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Input {
        node [shape=record];
        "ReWOOV3Input" [label="ReWOOV3Input"];
        "pydantic.BaseModel" -> "ReWOOV3Input";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.ReWOOV3Input
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

   Inheritance diagram for ReWOOV3Output:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3Output {
        node [shape=record];
        "ReWOOV3Output" [label="ReWOOV3Output"];
        "pydantic.BaseModel" -> "ReWOOV3Output";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.models.ReWOOV3Output
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

.. autolink-examples:: agents.planning.rewoo_v3.models
   :collapse:
   
.. autolink-skip:: next
