
:py:mod:`pro_search.tasks.models`
=================================

.. py:module:: pro_search.tasks.models

Pydantic models for recursive conditional planning with tree-based task decomposition.
Supports dynamic planning, parallel execution, and adaptive replanning.


.. autolink-examples:: pro_search.tasks.models
   :collapse:

Classes
-------

.. autoapisummary::

   pro_search.tasks.models.ExecutionPlan
   pro_search.tasks.models.PlanningState
   pro_search.tasks.models.PlanningStrategy
   pro_search.tasks.models.ReplanningAnalysis
   pro_search.tasks.models.TaskDecomposition
   pro_search.tasks.models.TaskDependency
   pro_search.tasks.models.TaskMetadata
   pro_search.tasks.models.TaskNode
   pro_search.tasks.models.TaskPriority
   pro_search.tasks.models.TaskResource
   pro_search.tasks.models.TaskStatus


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionPlan {
        node [shape=record];
        "ExecutionPlan" [label="ExecutionPlan"];
        "pydantic.BaseModel" -> "ExecutionPlan";
      }

.. autopydantic_model:: pro_search.tasks.models.ExecutionPlan
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

   Inheritance diagram for PlanningState:

   .. graphviz::
      :align: center

      digraph inheritance_PlanningState {
        node [shape=record];
        "PlanningState" [label="PlanningState"];
        "pydantic.BaseModel" -> "PlanningState";
      }

.. autopydantic_model:: pro_search.tasks.models.PlanningState
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

   Inheritance diagram for PlanningStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_PlanningStrategy {
        node [shape=record];
        "PlanningStrategy" [label="PlanningStrategy"];
        "pydantic.BaseModel" -> "PlanningStrategy";
      }

.. autopydantic_model:: pro_search.tasks.models.PlanningStrategy
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

   Inheritance diagram for ReplanningAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ReplanningAnalysis {
        node [shape=record];
        "ReplanningAnalysis" [label="ReplanningAnalysis"];
        "pydantic.BaseModel" -> "ReplanningAnalysis";
      }

.. autopydantic_model:: pro_search.tasks.models.ReplanningAnalysis
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

.. autopydantic_model:: pro_search.tasks.models.TaskDecomposition
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

   Inheritance diagram for TaskDependency:

   .. graphviz::
      :align: center

      digraph inheritance_TaskDependency {
        node [shape=record];
        "TaskDependency" [label="TaskDependency"];
        "pydantic.BaseModel" -> "TaskDependency";
      }

.. autopydantic_model:: pro_search.tasks.models.TaskDependency
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

   Inheritance diagram for TaskMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_TaskMetadata {
        node [shape=record];
        "TaskMetadata" [label="TaskMetadata"];
        "pydantic.BaseModel" -> "TaskMetadata";
      }

.. autopydantic_model:: pro_search.tasks.models.TaskMetadata
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

   Inheritance diagram for TaskNode:

   .. graphviz::
      :align: center

      digraph inheritance_TaskNode {
        node [shape=record];
        "TaskNode" [label="TaskNode"];
        "pydantic.BaseModel" -> "TaskNode";
      }

.. autopydantic_model:: pro_search.tasks.models.TaskNode
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

   Inheritance diagram for TaskPriority:

   .. graphviz::
      :align: center

      digraph inheritance_TaskPriority {
        node [shape=record];
        "TaskPriority" [label="TaskPriority"];
        "str" -> "TaskPriority";
        "enum.Enum" -> "TaskPriority";
      }

.. autoclass:: pro_search.tasks.models.TaskPriority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskPriority** is an Enum defined in ``pro_search.tasks.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskResource:

   .. graphviz::
      :align: center

      digraph inheritance_TaskResource {
        node [shape=record];
        "TaskResource" [label="TaskResource"];
        "pydantic.BaseModel" -> "TaskResource";
      }

.. autopydantic_model:: pro_search.tasks.models.TaskResource
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

   Inheritance diagram for TaskStatus:

   .. graphviz::
      :align: center

      digraph inheritance_TaskStatus {
        node [shape=record];
        "TaskStatus" [label="TaskStatus"];
        "str" -> "TaskStatus";
        "enum.Enum" -> "TaskStatus";
      }

.. autoclass:: pro_search.tasks.models.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskStatus** is an Enum defined in ``pro_search.tasks.models``.





.. rubric:: Related Links

.. autolink-examples:: pro_search.tasks.models
   :collapse:
   
.. autolink-skip:: next
