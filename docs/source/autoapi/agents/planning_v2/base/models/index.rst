
:py:mod:`agents.planning_v2.base.models`
========================================

.. py:module:: agents.planning_v2.base.models

Data models for planning agents.

This module contains Pydantic models for planning agent configurations,
plans, steps, and other planning-related data structures.


.. autolink-examples:: agents.planning_v2.base.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning_v2.base.models.Plan
   agents.planning_v2.base.models.Status
   agents.planning_v2.base.models.Task


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Plan:

   .. graphviz::
      :align: center

      digraph inheritance_Plan {
        node [shape=record];
        "Plan" [label="Plan"];
        "pydantic.BaseModel" -> "Plan";
        "Generic[StepType]" -> "Plan";
      }

.. autopydantic_model:: agents.planning_v2.base.models.Plan
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

   Inheritance diagram for Status:

   .. graphviz::
      :align: center

      digraph inheritance_Status {
        node [shape=record];
        "Status" [label="Status"];
        "str" -> "Status";
        "enum.Enum" -> "Status";
      }

.. autoclass:: agents.planning_v2.base.models.Status
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Status** is an Enum defined in ``agents.planning_v2.base.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Task:

   .. graphviz::
      :align: center

      digraph inheritance_Task {
        node [shape=record];
        "Task" [label="Task"];
        "pydantic.BaseModel" -> "Task";
      }

.. autopydantic_model:: agents.planning_v2.base.models.Task
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

.. autolink-examples:: agents.planning_v2.base.models
   :collapse:
   
.. autolink-skip:: next
