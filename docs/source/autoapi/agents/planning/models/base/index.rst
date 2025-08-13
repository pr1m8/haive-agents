
:py:mod:`agents.planning.models.base`
=====================================

.. py:module:: agents.planning.models.base

Base models for the unified planning system.

This module provides the foundation for a flexible planning system that can support
various planning patterns including Plan-and-Execute, ReWOO, LLM Compiler, FLARE RAG,
and recursive planning capabilities.

Key Design Principles:
1. Composable: Different planning patterns can mix and match components
2. Extensible: Easy to add new step types and planning patterns
3. Type-safe: Comprehensive validation and type checking
4. Resource-aware: Built-in support for resource tracking and constraints


.. autolink-examples:: agents.planning.models.base
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.models.base.ActionStep
   agents.planning.models.base.AdaptivePlan
   agents.planning.models.base.BasePlan
   agents.planning.models.base.BaseStep
   agents.planning.models.base.ConditionalStep
   agents.planning.models.base.DAGPlan
   agents.planning.models.base.Dependency
   agents.planning.models.base.DependencyType
   agents.planning.models.base.ExecutionMode
   agents.planning.models.base.ParallelStep
   agents.planning.models.base.RecursiveStep
   agents.planning.models.base.ResearchStep
   agents.planning.models.base.SequentialPlan
   agents.planning.models.base.StepMetadata
   agents.planning.models.base.StepStatus
   agents.planning.models.base.StepType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ActionStep:

   .. graphviz::
      :align: center

      digraph inheritance_ActionStep {
        node [shape=record];
        "ActionStep" [label="ActionStep"];
        "BaseStep" -> "ActionStep";
      }

.. autoclass:: agents.planning.models.base.ActionStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptivePlan:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptivePlan {
        node [shape=record];
        "AdaptivePlan" [label="AdaptivePlan"];
        "BasePlan" -> "AdaptivePlan";
      }

.. autoclass:: agents.planning.models.base.AdaptivePlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BasePlan:

   .. graphviz::
      :align: center

      digraph inheritance_BasePlan {
        node [shape=record];
        "BasePlan" [label="BasePlan"];
        "pydantic.BaseModel" -> "BasePlan";
      }

.. autopydantic_model:: agents.planning.models.base.BasePlan
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

   Inheritance diagram for BaseStep:

   .. graphviz::
      :align: center

      digraph inheritance_BaseStep {
        node [shape=record];
        "BaseStep" [label="BaseStep"];
        "pydantic.BaseModel" -> "BaseStep";
      }

.. autopydantic_model:: agents.planning.models.base.BaseStep
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

   Inheritance diagram for ConditionalStep:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalStep {
        node [shape=record];
        "ConditionalStep" [label="ConditionalStep"];
        "BaseStep" -> "ConditionalStep";
      }

.. autoclass:: agents.planning.models.base.ConditionalStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DAGPlan:

   .. graphviz::
      :align: center

      digraph inheritance_DAGPlan {
        node [shape=record];
        "DAGPlan" [label="DAGPlan"];
        "BasePlan" -> "DAGPlan";
      }

.. autoclass:: agents.planning.models.base.DAGPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Dependency:

   .. graphviz::
      :align: center

      digraph inheritance_Dependency {
        node [shape=record];
        "Dependency" [label="Dependency"];
        "pydantic.BaseModel" -> "Dependency";
      }

.. autopydantic_model:: agents.planning.models.base.Dependency
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

   Inheritance diagram for DependencyType:

   .. graphviz::
      :align: center

      digraph inheritance_DependencyType {
        node [shape=record];
        "DependencyType" [label="DependencyType"];
        "str" -> "DependencyType";
        "enum.Enum" -> "DependencyType";
      }

.. autoclass:: agents.planning.models.base.DependencyType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **DependencyType** is an Enum defined in ``agents.planning.models.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionMode:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionMode {
        node [shape=record];
        "ExecutionMode" [label="ExecutionMode"];
        "str" -> "ExecutionMode";
        "enum.Enum" -> "ExecutionMode";
      }

.. autoclass:: agents.planning.models.base.ExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionMode** is an Enum defined in ``agents.planning.models.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelStep:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelStep {
        node [shape=record];
        "ParallelStep" [label="ParallelStep"];
        "BaseStep" -> "ParallelStep";
      }

.. autoclass:: agents.planning.models.base.ParallelStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RecursiveStep:

   .. graphviz::
      :align: center

      digraph inheritance_RecursiveStep {
        node [shape=record];
        "RecursiveStep" [label="RecursiveStep"];
        "BaseStep" -> "RecursiveStep";
      }

.. autoclass:: agents.planning.models.base.RecursiveStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchStep:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchStep {
        node [shape=record];
        "ResearchStep" [label="ResearchStep"];
        "BaseStep" -> "ResearchStep";
      }

.. autoclass:: agents.planning.models.base.ResearchStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialPlan:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialPlan {
        node [shape=record];
        "SequentialPlan" [label="SequentialPlan"];
        "BasePlan" -> "SequentialPlan";
      }

.. autoclass:: agents.planning.models.base.SequentialPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_StepMetadata {
        node [shape=record];
        "StepMetadata" [label="StepMetadata"];
        "pydantic.BaseModel" -> "StepMetadata";
      }

.. autopydantic_model:: agents.planning.models.base.StepMetadata
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

   Inheritance diagram for StepStatus:

   .. graphviz::
      :align: center

      digraph inheritance_StepStatus {
        node [shape=record];
        "StepStatus" [label="StepStatus"];
        "str" -> "StepStatus";
        "enum.Enum" -> "StepStatus";
      }

.. autoclass:: agents.planning.models.base.StepStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **StepStatus** is an Enum defined in ``agents.planning.models.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepType:

   .. graphviz::
      :align: center

      digraph inheritance_StepType {
        node [shape=record];
        "StepType" [label="StepType"];
        "str" -> "StepType";
        "enum.Enum" -> "StepType";
      }

.. autoclass:: agents.planning.models.base.StepType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **StepType** is an Enum defined in ``agents.planning.models.base``.





.. rubric:: Related Links

.. autolink-examples:: agents.planning.models.base
   :collapse:
   
.. autolink-skip:: next
