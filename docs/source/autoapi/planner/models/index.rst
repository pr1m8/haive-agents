
:py:mod:`planner.models`
========================

.. py:module:: planner.models

Planner Models - Custom Pydantic models for strategic planning.

This module defines the structured output models used by the planner agent
for creating comprehensive, actionable task plans.


.. autolink-examples:: planner.models
   :collapse:

Classes
-------

.. autoapisummary::

   planner.models.PlanningContext
   planner.models.TaskPlan
   planner.models.TaskStep


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanningContext:

   .. graphviz::
      :align: center

      digraph inheritance_PlanningContext {
        node [shape=record];
        "PlanningContext" [label="PlanningContext"];
        "pydantic.BaseModel" -> "PlanningContext";
      }

.. autopydantic_model:: planner.models.PlanningContext
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

   Inheritance diagram for TaskPlan:

   .. graphviz::
      :align: center

      digraph inheritance_TaskPlan {
        node [shape=record];
        "TaskPlan" [label="TaskPlan"];
        "pydantic.BaseModel" -> "TaskPlan";
      }

.. autopydantic_model:: planner.models.TaskPlan
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

.. autopydantic_model:: planner.models.TaskStep
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

.. autolink-examples:: planner.models
   :collapse:
   
.. autolink-skip:: next
