
:py:mod:`agents.planning_v2.base.tree_models`
=============================================

.. py:module:: agents.planning_v2.base.tree_models

Tree-based planning models using the enhanced tree_leaf structure.

This module provides planning models that leverage the generic tree/leaf
structure from haive-core for more flexible and type-safe planning.


.. autolink-examples:: agents.planning_v2.base.tree_models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning_v2.base.tree_models.PlanContent
   agents.planning_v2.base.tree_models.PlanResult
   agents.planning_v2.base.tree_models.PlanStatus
   agents.planning_v2.base.tree_models.TaskPlan


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanContent:

   .. graphviz::
      :align: center

      digraph inheritance_PlanContent {
        node [shape=record];
        "PlanContent" [label="PlanContent"];
        "pydantic.BaseModel" -> "PlanContent";
      }

.. autopydantic_model:: agents.planning_v2.base.tree_models.PlanContent
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

   Inheritance diagram for PlanResult:

   .. graphviz::
      :align: center

      digraph inheritance_PlanResult {
        node [shape=record];
        "PlanResult" [label="PlanResult"];
        "pydantic.BaseModel" -> "PlanResult";
      }

.. autopydantic_model:: agents.planning_v2.base.tree_models.PlanResult
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

   Inheritance diagram for PlanStatus:

   .. graphviz::
      :align: center

      digraph inheritance_PlanStatus {
        node [shape=record];
        "PlanStatus" [label="PlanStatus"];
        "str" -> "PlanStatus";
        "enum.Enum" -> "PlanStatus";
      }

.. autoclass:: agents.planning_v2.base.tree_models.PlanStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlanStatus** is an Enum defined in ``agents.planning_v2.base.tree_models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskPlan:

   .. graphviz::
      :align: center

      digraph inheritance_TaskPlan {
        node [shape=record];
        "TaskPlan" [label="TaskPlan"];
        "PlanTree" -> "TaskPlan";
      }

.. autoclass:: agents.planning_v2.base.tree_models.TaskPlan
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning_v2.base.tree_models.create_phased_plan
   agents.planning_v2.base.tree_models.create_simple_plan

.. py:function:: create_phased_plan(objective: str, phases: dict[str, list[str]]) -> TaskPlan

   Create a plan with phases (sub-plans).

   :param objective: Main plan objective
   :param phases: Dict of phase_name -> list of tasks

   .. rubric:: Example

   plan = create_phased_plan(
       "Launch Product",
       {
           "Development": ["Code", "Test", "Review"],
           "Deployment": ["Stage", "Verify", "Prod"],
           "Marketing": ["Announce", "Demo", "Feedback"]
       }
   )


   .. autolink-examples:: create_phased_plan
      :collapse:

.. py:function:: create_simple_plan(objective: str, tasks: list[str]) -> TaskPlan

   Create a simple linear plan from a list of task names.


   .. autolink-examples:: create_simple_plan
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning_v2.base.tree_models
   :collapse:
   
.. autolink-skip:: next
