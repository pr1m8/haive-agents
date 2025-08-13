
:py:mod:`models.task_analysis.analysis`
=======================================

.. py:module:: models.task_analysis.analysis

Main task analysis model combining all analysis components.

This module provides the comprehensive TaskAnalysis model that combines
complexity assessment, solvability analysis, task decomposition, and
execution strategy recommendations.


.. autolink-examples:: models.task_analysis.analysis
   :collapse:

Classes
-------

.. autoapisummary::

   models.task_analysis.analysis.AnalysisMethod
   models.task_analysis.analysis.ExecutionStrategy
   models.task_analysis.analysis.PlanningRequirement
   models.task_analysis.analysis.TaskAnalysis
   models.task_analysis.analysis.TaskComplexity
   models.task_analysis.analysis.TaskDimension


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AnalysisMethod:

   .. graphviz::
      :align: center

      digraph inheritance_AnalysisMethod {
        node [shape=record];
        "AnalysisMethod" [label="AnalysisMethod"];
        "str" -> "AnalysisMethod";
        "enum.Enum" -> "AnalysisMethod";
      }

.. autoclass:: models.task_analysis.analysis.AnalysisMethod
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **AnalysisMethod** is an Enum defined in ``models.task_analysis.analysis``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionStrategy {
        node [shape=record];
        "ExecutionStrategy" [label="ExecutionStrategy"];
        "pydantic.BaseModel" -> "ExecutionStrategy";
      }

.. autopydantic_model:: models.task_analysis.analysis.ExecutionStrategy
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

   Inheritance diagram for PlanningRequirement:

   .. graphviz::
      :align: center

      digraph inheritance_PlanningRequirement {
        node [shape=record];
        "PlanningRequirement" [label="PlanningRequirement"];
        "pydantic.BaseModel" -> "PlanningRequirement";
      }

.. autopydantic_model:: models.task_analysis.analysis.PlanningRequirement
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

   Inheritance diagram for TaskAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_TaskAnalysis {
        node [shape=record];
        "TaskAnalysis" [label="TaskAnalysis"];
        "pydantic.BaseModel" -> "TaskAnalysis";
      }

.. autopydantic_model:: models.task_analysis.analysis.TaskAnalysis
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

   Inheritance diagram for TaskComplexity:

   .. graphviz::
      :align: center

      digraph inheritance_TaskComplexity {
        node [shape=record];
        "TaskComplexity" [label="TaskComplexity"];
        "pydantic.BaseModel" -> "TaskComplexity";
      }

.. autopydantic_model:: models.task_analysis.analysis.TaskComplexity
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

   Inheritance diagram for TaskDimension:

   .. graphviz::
      :align: center

      digraph inheritance_TaskDimension {
        node [shape=record];
        "TaskDimension" [label="TaskDimension"];
        "str" -> "TaskDimension";
        "enum.Enum" -> "TaskDimension";
      }

.. autoclass:: models.task_analysis.analysis.TaskDimension
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskDimension** is an Enum defined in ``models.task_analysis.analysis``.





.. rubric:: Related Links

.. autolink-examples:: models.task_analysis.analysis
   :collapse:
   
.. autolink-skip:: next
