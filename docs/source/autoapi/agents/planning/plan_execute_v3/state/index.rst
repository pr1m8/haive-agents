
:py:mod:`agents.planning.plan_execute_v3.state`
===============================================

.. py:module:: agents.planning.plan_execute_v3.state

State schema for Plan-and-Execute V3 Agent.

This module defines the state schema used by the Plan-and-Execute V3 agent,
extending MessagesState with computed fields for plan tracking.


.. autolink-examples:: agents.planning.plan_execute_v3.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.state.ExecutionPlan
   agents.planning.plan_execute_v3.state.PlanEvaluation
   agents.planning.plan_execute_v3.state.PlanExecuteV3State
   agents.planning.plan_execute_v3.state.StepExecution


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExecutionPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionPlan {
        node [shape=record];
        "ExecutionPlan" [label="ExecutionPlan"];
        "pydantic.BaseModel" -> "ExecutionPlan";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.state.ExecutionPlan
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

   Inheritance diagram for PlanEvaluation:

   .. graphviz::
      :align: center

      digraph inheritance_PlanEvaluation {
        node [shape=record];
        "PlanEvaluation" [label="PlanEvaluation"];
        "pydantic.BaseModel" -> "PlanEvaluation";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.state.PlanEvaluation
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

   Inheritance diagram for PlanExecuteV3State:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteV3State {
        node [shape=record];
        "PlanExecuteV3State" [label="PlanExecuteV3State"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "PlanExecuteV3State";
      }

.. autoclass:: agents.planning.plan_execute_v3.state.PlanExecuteV3State
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepExecution:

   .. graphviz::
      :align: center

      digraph inheritance_StepExecution {
        node [shape=record];
        "StepExecution" [label="StepExecution"];
        "pydantic.BaseModel" -> "StepExecution";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.state.StepExecution
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

.. autolink-examples:: agents.planning.plan_execute_v3.state
   :collapse:
   
.. autolink-skip:: next
