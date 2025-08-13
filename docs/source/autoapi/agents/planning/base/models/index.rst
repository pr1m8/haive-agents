
:py:mod:`agents.planning.base.models`
=====================================

.. py:module:: agents.planning.base.models

Planning Base Models - Advanced planning system with generics, indexing, and intelligent tree structures.

This module provides a sophisticated planning framework with:
- Maximum flexibility generics: Plan[Union[Step, Plan, Callable, str, Any]]
- Intelligent tree traversal with cycle detection
- Event-driven modifiable sequences with undo/redo
- Auto-propagating status management
- Smart field validation and auto-completion
- Dynamic model adaptation based on content


.. autolink-examples:: agents.planning.base.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.base.models.BasePlan
   agents.planning.base.models.BaseStep
   agents.planning.base.models.ChangeEvent
   agents.planning.base.models.ConditionalPlan
   agents.planning.base.models.EventEmitter
   agents.planning.base.models.FlexiblePlan
   agents.planning.base.models.IntelligentSequence
   agents.planning.base.models.IntelligentStatusMixin
   agents.planning.base.models.ParallelPlan
   agents.planning.base.models.Priority
   agents.planning.base.models.SequentialPlan
   agents.planning.base.models.Task
   agents.planning.base.models.TaskStatus
   agents.planning.base.models.TraversalMode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BasePlan:

   .. graphviz::
      :align: center

      digraph inheritance_BasePlan {
        node [shape=record];
        "BasePlan" [label="BasePlan"];
        "IntelligentStatusMixin" -> "BasePlan";
        "Generic[T]" -> "BasePlan";
      }

.. autoclass:: agents.planning.base.models.BasePlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseStep:

   .. graphviz::
      :align: center

      digraph inheritance_BaseStep {
        node [shape=record];
        "BaseStep" [label="BaseStep"];
        "IntelligentStatusMixin" -> "BaseStep";
      }

.. autoclass:: agents.planning.base.models.BaseStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChangeEvent:

   .. graphviz::
      :align: center

      digraph inheritance_ChangeEvent {
        node [shape=record];
        "ChangeEvent" [label="ChangeEvent"];
        "pydantic.BaseModel" -> "ChangeEvent";
      }

.. autopydantic_model:: agents.planning.base.models.ChangeEvent
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

   Inheritance diagram for ConditionalPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalPlan {
        node [shape=record];
        "ConditionalPlan" [label="ConditionalPlan"];
        "BasePlan[Union[BaseStep, BasePlan, collections.abc.Callable]]" -> "ConditionalPlan";
      }

.. autoclass:: agents.planning.base.models.ConditionalPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EventEmitter:

   .. graphviz::
      :align: center

      digraph inheritance_EventEmitter {
        node [shape=record];
        "EventEmitter" [label="EventEmitter"];
      }

.. autoclass:: agents.planning.base.models.EventEmitter
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlexiblePlan:

   .. graphviz::
      :align: center

      digraph inheritance_FlexiblePlan {
        node [shape=record];
        "FlexiblePlan" [label="FlexiblePlan"];
        "BasePlan[PlanContent]" -> "FlexiblePlan";
      }

.. autoclass:: agents.planning.base.models.FlexiblePlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IntelligentSequence:

   .. graphviz::
      :align: center

      digraph inheritance_IntelligentSequence {
        node [shape=record];
        "IntelligentSequence" [label="IntelligentSequence"];
        "list[PlanContent]" -> "IntelligentSequence";
        "Generic[T]" -> "IntelligentSequence";
      }

.. autoclass:: agents.planning.base.models.IntelligentSequence
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IntelligentStatusMixin:

   .. graphviz::
      :align: center

      digraph inheritance_IntelligentStatusMixin {
        node [shape=record];
        "IntelligentStatusMixin" [label="IntelligentStatusMixin"];
        "pydantic.BaseModel" -> "IntelligentStatusMixin";
        "abc.ABC" -> "IntelligentStatusMixin";
      }

.. autopydantic_model:: agents.planning.base.models.IntelligentStatusMixin
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

   Inheritance diagram for ParallelPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelPlan {
        node [shape=record];
        "ParallelPlan" [label="ParallelPlan"];
        "BasePlan[Union[BaseStep, BasePlan]]" -> "ParallelPlan";
      }

.. autoclass:: agents.planning.base.models.ParallelPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Priority:

   .. graphviz::
      :align: center

      digraph inheritance_Priority {
        node [shape=record];
        "Priority" [label="Priority"];
        "str" -> "Priority";
        "enum.Enum" -> "Priority";
      }

.. autoclass:: agents.planning.base.models.Priority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Priority** is an Enum defined in ``agents.planning.base.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialPlan:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialPlan {
        node [shape=record];
        "SequentialPlan" [label="SequentialPlan"];
        "BasePlan[Union[BaseStep, BasePlan]]" -> "SequentialPlan";
      }

.. autoclass:: agents.planning.base.models.SequentialPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Task:

   .. graphviz::
      :align: center

      digraph inheritance_Task {
        node [shape=record];
        "Task" [label="Task"];
        "IntelligentStatusMixin" -> "Task";
      }

.. autoclass:: agents.planning.base.models.Task
   :members:
   :undoc-members:
   :show-inheritance:




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

.. autoclass:: agents.planning.base.models.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskStatus** is an Enum defined in ``agents.planning.base.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TraversalMode:

   .. graphviz::
      :align: center

      digraph inheritance_TraversalMode {
        node [shape=record];
        "TraversalMode" [label="TraversalMode"];
        "str" -> "TraversalMode";
        "enum.Enum" -> "TraversalMode";
      }

.. autoclass:: agents.planning.base.models.TraversalMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TraversalMode** is an Enum defined in ``agents.planning.base.models``.





.. rubric:: Related Links

.. autolink-examples:: agents.planning.base.models
   :collapse:
   
.. autolink-skip:: next
