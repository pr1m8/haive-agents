
:py:mod:`agents.planning.plan_execute_v3.agent`
===============================================

.. py:module:: agents.planning.plan_execute_v3.agent

Plan-and-Execute V3 Agent - Enhanced MultiAgent V3 Implementation.

This agent implements the Plan-and-Execute methodology using Enhanced MultiAgent V3,
separating planning, execution, evaluation, and replanning into distinct sub-agents.

Key Features:
- SimpleAgent for planning with structured output (ExecutionPlan)
- ReactAgent for step execution with tools
- SimpleAgent for evaluation and decision-making (PlanEvaluation)
- SimpleAgent for replanning when needed (RevisedPlan)
- Enhanced MultiAgent V3 for coordination
- Real component testing (no mocks)


.. autolink-examples:: agents.planning.plan_execute_v3.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.agent.ExecutionPlan
   agents.planning.plan_execute_v3.agent.PlanEvaluation
   agents.planning.plan_execute_v3.agent.PlanExecuteInput
   agents.planning.plan_execute_v3.agent.PlanExecuteOutput
   agents.planning.plan_execute_v3.agent.PlanExecuteV3Agent
   agents.planning.plan_execute_v3.agent.PlanExecuteV3State
   agents.planning.plan_execute_v3.agent.RevisedPlan
   agents.planning.plan_execute_v3.agent.StepExecution


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

.. autopydantic_model:: agents.planning.plan_execute_v3.agent.ExecutionPlan
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

.. autopydantic_model:: agents.planning.plan_execute_v3.agent.PlanEvaluation
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

   Inheritance diagram for PlanExecuteInput:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteInput {
        node [shape=record];
        "PlanExecuteInput" [label="PlanExecuteInput"];
        "pydantic.BaseModel" -> "PlanExecuteInput";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.agent.PlanExecuteInput
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

   Inheritance diagram for PlanExecuteOutput:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteOutput {
        node [shape=record];
        "PlanExecuteOutput" [label="PlanExecuteOutput"];
        "pydantic.BaseModel" -> "PlanExecuteOutput";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.agent.PlanExecuteOutput
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

.. autoclass:: agents.planning.plan_execute_v3.agent.PlanExecuteV3Agent
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanExecuteV3State:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteV3State {
        node [shape=record];
        "PlanExecuteV3State" [label="PlanExecuteV3State"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "PlanExecuteV3State";
      }

.. autoclass:: agents.planning.plan_execute_v3.agent.PlanExecuteV3State
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RevisedPlan:

   .. graphviz::
      :align: center

      digraph inheritance_RevisedPlan {
        node [shape=record];
        "RevisedPlan" [label="RevisedPlan"];
        "pydantic.BaseModel" -> "RevisedPlan";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.agent.RevisedPlan
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

   Inheritance diagram for StepExecution:

   .. graphviz::
      :align: center

      digraph inheritance_StepExecution {
        node [shape=record];
        "StepExecution" [label="StepExecution"];
        "pydantic.BaseModel" -> "StepExecution";
      }

.. autopydantic_model:: agents.planning.plan_execute_v3.agent.StepExecution
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

.. autolink-examples:: agents.planning.plan_execute_v3.agent
   :collapse:
   
.. autolink-skip:: next
