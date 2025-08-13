
:py:mod:`models.task_analysis.branching`
========================================

.. py:module:: models.task_analysis.branching

Task branching and decomposition analysis.

This module analyzes how tasks can be broken down into subtasks, identifying
parallel execution opportunities, sequential dependencies, and optimal
decomposition strategies.


.. autolink-examples:: models.task_analysis.branching
   :collapse:

Classes
-------

.. autoapisummary::

   models.task_analysis.branching.BranchType
   models.task_analysis.branching.TaskBranch
   models.task_analysis.branching.TaskDecomposition


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BranchType:

   .. graphviz::
      :align: center

      digraph inheritance_BranchType {
        node [shape=record];
        "BranchType" [label="BranchType"];
        "str" -> "BranchType";
        "enum.Enum" -> "BranchType";
      }

.. autoclass:: models.task_analysis.branching.BranchType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **BranchType** is an Enum defined in ``models.task_analysis.branching``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskBranch:

   .. graphviz::
      :align: center

      digraph inheritance_TaskBranch {
        node [shape=record];
        "TaskBranch" [label="TaskBranch"];
        "pydantic.BaseModel" -> "TaskBranch";
      }

.. autopydantic_model:: models.task_analysis.branching.TaskBranch
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

   Inheritance diagram for TaskDecomposition:

   .. graphviz::
      :align: center

      digraph inheritance_TaskDecomposition {
        node [shape=record];
        "TaskDecomposition" [label="TaskDecomposition"];
        "pydantic.BaseModel" -> "TaskDecomposition";
      }

.. autopydantic_model:: models.task_analysis.branching.TaskDecomposition
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

.. autolink-examples:: models.task_analysis.branching
   :collapse:
   
.. autolink-skip:: next
