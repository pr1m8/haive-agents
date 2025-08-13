
:py:mod:`agents.planning.plan_execute_v3`
=========================================

.. py:module:: agents.planning.plan_execute_v3

Plan-and-Execute V3 Agent Package.

This package implements the Plan-and-Execute methodology using Enhanced MultiAgent V3,
providing a comprehensive solution for complex task planning and execution.

Key Components:
- PlanExecuteV3Agent: Main agent coordinator
- ExecutionPlan, StepExecution, PlanEvaluation: Structured output models
- PlanExecuteV3State: State management with computed fields
- System prompts for each sub-agent

Usage:
    from haive.agents.planning.plan_execute_v3 import PlanExecuteV3Agent

    agent = PlanExecuteV3Agent(tools=[search_tool, calculator])
    result = await agent.arun("Analyze market trends for renewable energy")


.. autolink-examples:: agents.planning.plan_execute_v3
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.ExecutionPlan
   agents.planning.plan_execute_v3.PlanEvaluation
   agents.planning.plan_execute_v3.PlanExecuteInput
   agents.planning.plan_execute_v3.PlanExecuteOutput
   agents.planning.plan_execute_v3.PlanExecuteV3Agent
   agents.planning.plan_execute_v3.PlanExecuteV3State
   agents.planning.plan_execute_v3.PlanStep
   agents.planning.plan_execute_v3.RevisedPlan
   agents.planning.plan_execute_v3.StepExecution
   agents.planning.plan_execute_v3.StepStatus


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

.. autopydantic_model:: agents.planning.plan_execute_v3.ExecutionPlan
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

.. autopydantic_model:: agents.planning.plan_execute_v3.PlanEvaluation
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

.. autopydantic_model:: agents.planning.plan_execute_v3.PlanExecuteInput
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

.. autopydantic_model:: agents.planning.plan_execute_v3.PlanExecuteOutput
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

   Inheritance diagram for PlanExecuteV3Agent:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteV3Agent {
        node [shape=record];
        "PlanExecuteV3Agent" [label="PlanExecuteV3Agent"];
      }

.. autoclass:: agents.planning.plan_execute_v3.PlanExecuteV3Agent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanExecuteV3State:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteV3State {
        node [shape=record];
        "PlanExecuteV3State" [label="PlanExecuteV3State"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "PlanExecuteV3State";
      }

.. autoclass:: agents.planning.plan_execute_v3.PlanExecuteV3State
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanStep:

   .. graphviz::
      :align: center

      digraph inheritance_PlanStep {
        node [shape=record];
        "PlanStep" [label="PlanStep"];
        "pydantic.BaseModel" -> "PlanStep";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.PlanStep
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

.. autopydantic_model:: agents.planning.plan_execute_v3.RevisedPlan
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

.. autopydantic_model:: agents.planning.plan_execute_v3.StepExecution
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

.. autoclass:: agents.planning.plan_execute_v3.StepStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **StepStatus** is an Enum defined in ``agents.planning.plan_execute_v3``.





.. rubric:: Related Links

.. autolink-examples:: agents.planning.plan_execute_v3
   :collapse:
   
.. autolink-skip:: next
