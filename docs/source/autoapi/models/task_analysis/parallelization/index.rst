
:py:mod:`models.task_analysis.parallelization`
==============================================

.. py:module:: models.task_analysis.parallelization

Parallelization analysis for task execution planning.

This module analyzes task dependencies to identify parallelization opportunities,
execution phases, join points, and optimal execution strategies.


.. autolink-examples:: models.task_analysis.parallelization
   :collapse:

Classes
-------

.. autoapisummary::

   models.task_analysis.parallelization.ExecutionPhase
   models.task_analysis.parallelization.ExecutionStrategy
   models.task_analysis.parallelization.JoinPoint
   models.task_analysis.parallelization.ParallelGroup
   models.task_analysis.parallelization.ParallelizationAnalysis
   models.task_analysis.parallelization.ParallelizationAnalyzer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionPhase:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionPhase {
        node [shape=record];
        "ExecutionPhase" [label="ExecutionPhase"];
        "pydantic.BaseModel" -> "ExecutionPhase";
      }

.. autopydantic_model:: models.task_analysis.parallelization.ExecutionPhase
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

   Inheritance diagram for ExecutionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionStrategy {
        node [shape=record];
        "ExecutionStrategy" [label="ExecutionStrategy"];
        "str" -> "ExecutionStrategy";
        "enum.Enum" -> "ExecutionStrategy";
      }

.. autoclass:: models.task_analysis.parallelization.ExecutionStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionStrategy** is an Enum defined in ``models.task_analysis.parallelization``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JoinPoint:

   .. graphviz::
      :align: center

      digraph inheritance_JoinPoint {
        node [shape=record];
        "JoinPoint" [label="JoinPoint"];
        "pydantic.BaseModel" -> "JoinPoint";
      }

.. autopydantic_model:: models.task_analysis.parallelization.JoinPoint
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

   Inheritance diagram for ParallelGroup:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelGroup {
        node [shape=record];
        "ParallelGroup" [label="ParallelGroup"];
        "pydantic.BaseModel" -> "ParallelGroup";
      }

.. autopydantic_model:: models.task_analysis.parallelization.ParallelGroup
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

   Inheritance diagram for ParallelizationAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelizationAnalysis {
        node [shape=record];
        "ParallelizationAnalysis" [label="ParallelizationAnalysis"];
        "pydantic.BaseModel" -> "ParallelizationAnalysis";
      }

.. autopydantic_model:: models.task_analysis.parallelization.ParallelizationAnalysis
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

   Inheritance diagram for ParallelizationAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelizationAnalyzer {
        node [shape=record];
        "ParallelizationAnalyzer" [label="ParallelizationAnalyzer"];
        "pydantic.BaseModel" -> "ParallelizationAnalyzer";
      }

.. autopydantic_model:: models.task_analysis.parallelization.ParallelizationAnalyzer
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

.. autolink-examples:: models.task_analysis.parallelization
   :collapse:
   
.. autolink-skip:: next
