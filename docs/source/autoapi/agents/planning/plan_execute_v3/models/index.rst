
:py:mod:`agents.planning.plan_execute_v3.models`
================================================

.. py:module:: agents.planning.plan_execute_v3.models

Plan-and-Execute V3 Models - Structured Output Models for the agent.

Based on the Plan-and-Execute methodology where planning and execution
are separated into distinct phases with structured outputs.


.. autolink-examples:: agents.planning.plan_execute_v3.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.models.ExecutionPlan
   agents.planning.plan_execute_v3.models.Plan
   agents.planning.plan_execute_v3.models.PlanEvaluation
   agents.planning.plan_execute_v3.models.PlanExecuteInput
   agents.planning.plan_execute_v3.models.PlanExecuteOutput
   agents.planning.plan_execute_v3.models.PlanStep
   agents.planning.plan_execute_v3.models.RevisedPlan
   agents.planning.plan_execute_v3.models.StepExecution
   agents.planning.plan_execute_v3.models.StepStatus


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

.. autopydantic_model:: agents.planning.plan_execute_v3.models.ExecutionPlan
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

   Inheritance diagram for Plan:

   .. graphviz::
      :align: center

      digraph inheritance_Plan {
        node [shape=record];
        "Plan" [label="Plan"];
        "pydantic.BaseModel" -> "Plan";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.Plan
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

   Inheritance diagram for PlanEvaluation:

   .. graphviz::
      :align: center

      digraph inheritance_PlanEvaluation {
        node [shape=record];
        "PlanEvaluation" [label="PlanEvaluation"];
        "pydantic.BaseModel" -> "PlanEvaluation";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.PlanEvaluation
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

   Inheritance diagram for PlanExecuteInput:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteInput {
        node [shape=record];
        "PlanExecuteInput" [label="PlanExecuteInput"];
        "pydantic.BaseModel" -> "PlanExecuteInput";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.PlanExecuteInput
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

   Inheritance diagram for PlanExecuteOutput:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteOutput {
        node [shape=record];
        "PlanExecuteOutput" [label="PlanExecuteOutput"];
        "pydantic.BaseModel" -> "PlanExecuteOutput";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.PlanExecuteOutput
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

   Inheritance diagram for PlanStep:

   .. graphviz::
      :align: center

      digraph inheritance_PlanStep {
        node [shape=record];
        "PlanStep" [label="PlanStep"];
        "pydantic.BaseModel" -> "PlanStep";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.PlanStep
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

   Inheritance diagram for RevisedPlan:

   .. graphviz::
      :align: center

      digraph inheritance_RevisedPlan {
        node [shape=record];
        "RevisedPlan" [label="RevisedPlan"];
        "pydantic.BaseModel" -> "RevisedPlan";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.RevisedPlan
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

   Inheritance diagram for StepExecution:

   .. graphviz::
      :align: center

      digraph inheritance_StepExecution {
        node [shape=record];
        "StepExecution" [label="StepExecution"];
        "pydantic.BaseModel" -> "StepExecution";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.models.StepExecution
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

   Inheritance diagram for StepStatus:

   .. graphviz::
      :align: center

      digraph inheritance_StepStatus {
        node [shape=record];
        "StepStatus" [label="StepStatus"];
        "str" -> "StepStatus";
        "enum.Enum" -> "StepStatus";
      }

.. autoclass:: agents.planning.plan_execute_v3.models.StepStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **StepStatus** is an Enum defined in ``agents.planning.plan_execute_v3.models``.





.. rubric:: Related Links

.. autolink-examples:: agents.planning.plan_execute_v3.models
   :collapse:
   
.. autolink-skip:: next
