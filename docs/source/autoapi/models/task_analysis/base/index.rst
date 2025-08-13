
:py:mod:`models.task_analysis.base`
===================================

.. py:module:: models.task_analysis.base

Base classes and enums for task complexity analysis.

This module defines the fundamental building blocks for task complexity analysis
including task representations, dependency types, and complexity classifications.


.. autolink-examples:: models.task_analysis.base
   :collapse:

Classes
-------

.. autoapisummary::

   models.task_analysis.base.ComplexityLevel
   models.task_analysis.base.ComputationalComplexity
   models.task_analysis.base.DependencyNode
   models.task_analysis.base.DependencyType
   models.task_analysis.base.KnowledgeComplexity
   models.task_analysis.base.ResourceType
   models.task_analysis.base.SolvabilityStatus
   models.task_analysis.base.Task
   models.task_analysis.base.TaskStep
   models.task_analysis.base.TaskType
   models.task_analysis.base.TimeComplexity


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ComplexityLevel:

   .. graphviz::
      :align: center

      digraph inheritance_ComplexityLevel {
        node [shape=record];
        "ComplexityLevel" [label="ComplexityLevel"];
        "str" -> "ComplexityLevel";
        "enum.Enum" -> "ComplexityLevel";
      }

.. autoclass:: models.task_analysis.base.ComplexityLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ComplexityLevel** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ComputationalComplexity:

   .. graphviz::
      :align: center

      digraph inheritance_ComputationalComplexity {
        node [shape=record];
        "ComputationalComplexity" [label="ComputationalComplexity"];
        "str" -> "ComputationalComplexity";
        "enum.Enum" -> "ComputationalComplexity";
      }

.. autoclass:: models.task_analysis.base.ComputationalComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ComputationalComplexity** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DependencyNode:

   .. graphviz::
      :align: center

      digraph inheritance_DependencyNode {
        node [shape=record];
        "DependencyNode" [label="DependencyNode"];
        "pydantic.BaseModel" -> "DependencyNode";
      }

.. autopydantic_model:: models.task_analysis.base.DependencyNode
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

.. autoclass:: models.task_analysis.base.DependencyType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **DependencyType** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KnowledgeComplexity:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeComplexity {
        node [shape=record];
        "KnowledgeComplexity" [label="KnowledgeComplexity"];
        "str" -> "KnowledgeComplexity";
        "enum.Enum" -> "KnowledgeComplexity";
      }

.. autoclass:: models.task_analysis.base.KnowledgeComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **KnowledgeComplexity** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResourceType:

   .. graphviz::
      :align: center

      digraph inheritance_ResourceType {
        node [shape=record];
        "ResourceType" [label="ResourceType"];
        "str" -> "ResourceType";
        "enum.Enum" -> "ResourceType";
      }

.. autoclass:: models.task_analysis.base.ResourceType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ResourceType** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SolvabilityStatus:

   .. graphviz::
      :align: center

      digraph inheritance_SolvabilityStatus {
        node [shape=record];
        "SolvabilityStatus" [label="SolvabilityStatus"];
        "str" -> "SolvabilityStatus";
        "enum.Enum" -> "SolvabilityStatus";
      }

.. autoclass:: models.task_analysis.base.SolvabilityStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SolvabilityStatus** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Task:

   .. graphviz::
      :align: center

      digraph inheritance_Task {
        node [shape=record];
        "Task" [label="Task"];
        "pydantic.BaseModel" -> "Task";
      }

.. autopydantic_model:: models.task_analysis.base.Task
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

   Inheritance diagram for TaskStep:

   .. graphviz::
      :align: center

      digraph inheritance_TaskStep {
        node [shape=record];
        "TaskStep" [label="TaskStep"];
        "pydantic.BaseModel" -> "TaskStep";
      }

.. autopydantic_model:: models.task_analysis.base.TaskStep
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

   Inheritance diagram for TaskType:

   .. graphviz::
      :align: center

      digraph inheritance_TaskType {
        node [shape=record];
        "TaskType" [label="TaskType"];
        "str" -> "TaskType";
        "enum.Enum" -> "TaskType";
      }

.. autoclass:: models.task_analysis.base.TaskType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskType** is an Enum defined in ``models.task_analysis.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TimeComplexity:

   .. graphviz::
      :align: center

      digraph inheritance_TimeComplexity {
        node [shape=record];
        "TimeComplexity" [label="TimeComplexity"];
        "str" -> "TimeComplexity";
        "enum.Enum" -> "TimeComplexity";
      }

.. autoclass:: models.task_analysis.base.TimeComplexity
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TimeComplexity** is an Enum defined in ``models.task_analysis.base``.





.. rubric:: Related Links

.. autolink-examples:: models.task_analysis.base
   :collapse:
   
.. autolink-skip:: next
