
:py:mod:`agents.planning.base`
==============================

.. py:module:: agents.planning.base

Planning Base Models - Advanced planning system with generics, indexing, and intelligent tree structures.

This module provides a sophisticated planning framework with:
- Maximum flexibility generics: Plan[Union[Step, Plan, Callable, str, Any]]
- Intelligent tree traversal with cycle detection
- Event-driven modifiable sequences with undo/redo
- Auto-propagating status management
- Smart field validation and auto-completion
- Dynamic model adaptation based on content


.. autolink-examples:: agents.planning.base
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.base.BasePlan
   agents.planning.base.BasePlannerAgent
   agents.planning.base.BaseStep
   agents.planning.base.ChangeEvent
   agents.planning.base.ConditionalPlan
   agents.planning.base.EventEmitter
   agents.planning.base.FlexiblePlan
   agents.planning.base.IntelligentSequence
   agents.planning.base.IntelligentStatusMixin
   agents.planning.base.ParallelPlan
   agents.planning.base.Priority
   agents.planning.base.SequentialPlan
   agents.planning.base.Task
   agents.planning.base.TaskStatus
   agents.planning.base.TraversalMode


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

.. autoclass:: agents.planning.base.BasePlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BasePlannerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BasePlannerAgent {
        node [shape=record];
        "BasePlannerAgent" [label="BasePlannerAgent"];
        "SimpleAgentV3" -> "BasePlannerAgent";
      }

.. autoclass:: agents.planning.base.BasePlannerAgent
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

.. autoclass:: agents.planning.base.BaseStep
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChangeEvent:

   .. graphviz::
      :align: center

      digraph inheritance_ChangeEvent {
        node [shape=record];
        "ChangeEvent" [label="ChangeEvent"];
        "pydantic.BaseModel" -> "ChangeEvent";
      }

.. autopydantic_model:: agents.planning.base.ChangeEvent
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConditionalPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ConditionalPlan {
        node [shape=record];
        "ConditionalPlan" [label="ConditionalPlan"];
        "BasePlan[Union[BaseStep, BasePlan, collections.abc.Callable]]" -> "ConditionalPlan";
      }

.. autoclass:: agents.planning.base.ConditionalPlan
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EventEmitter:

   .. graphviz::
      :align: center

      digraph inheritance_EventEmitter {
        node [shape=record];
        "EventEmitter" [label="EventEmitter"];
      }

.. autoclass:: agents.planning.base.EventEmitter
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlexiblePlan:

   .. graphviz::
      :align: center

      digraph inheritance_FlexiblePlan {
        node [shape=record];
        "FlexiblePlan" [label="FlexiblePlan"];
        "BasePlan[PlanContent]" -> "FlexiblePlan";
      }

.. autoclass:: agents.planning.base.FlexiblePlan
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

.. autoclass:: agents.planning.base.IntelligentSequence
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

.. autopydantic_model:: agents.planning.base.IntelligentStatusMixin
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelPlan {
        node [shape=record];
        "ParallelPlan" [label="ParallelPlan"];
        "BasePlan[Union[BaseStep, BasePlan]]" -> "ParallelPlan";
      }

.. autoclass:: agents.planning.base.ParallelPlan
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

.. autoclass:: agents.planning.base.Priority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Priority** is an Enum defined in ``agents.planning.base``.


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialPlan:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialPlan {
        node [shape=record];
        "SequentialPlan" [label="SequentialPlan"];
        "BasePlan[Union[BaseStep, BasePlan]]" -> "SequentialPlan";
      }

.. autoclass:: agents.planning.base.SequentialPlan
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

.. autoclass:: agents.planning.base.Task
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

.. autoclass:: agents.planning.base.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskStatus** is an Enum defined in ``agents.planning.base``.





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

.. autoclass:: agents.planning.base.TraversalMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TraversalMode** is an Enum defined in ``agents.planning.base``.



Functions
---------

.. autoapisummary::

   agents.planning.base.create_base_planner
   agents.planning.base.create_conversation_summary_planner

.. py:function:: create_base_planner(name: str = 'base_planner', model: str = 'gpt-4o-mini', temperature: float = 0.3, structured_output_model=None) -> BasePlannerAgent

   Create a base planner agent with default configuration.

   :param name: Name for the planner agent
   :param model: LLM model to use for planning
   :param temperature: Sampling temperature for planning (lower = more focused)
   :param structured_output_model: Custom output model (defaults to BasePlan)

   :returns: Configured planner ready for use
   :rtype: BasePlannerAgent

   .. rubric:: Examples

   Basic planner:

       planner = create_base_planner()

   Custom planner:

       planner = create_base_planner(
           name="strategic_planner",
           model="gpt-4",
           temperature=0.2
       )


   .. autolink-examples:: create_base_planner
      :collapse:

.. py:function:: create_conversation_summary_planner(name: str = 'conversation_planner') -> BasePlannerAgent

   Create a specialized planner for conversation summary tasks.

   This creates a planner specifically tuned for analyzing conversations
   and creating detailed summaries with strategic planning approach.

   :returns: Planner optimized for conversation analysis
   :rtype: BasePlannerAgent


   .. autolink-examples:: create_conversation_summary_planner
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.base
   :collapse:
   
.. autolink-skip:: next
