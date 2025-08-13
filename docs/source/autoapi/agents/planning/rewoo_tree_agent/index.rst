
:py:mod:`agents.planning.rewoo_tree_agent`
==========================================

.. py:module:: agents.planning.rewoo_tree_agent

ReWOO Tree-based Planning Agent with Parallelizable Execution.

This agent implements the ReWOO (Reasoning without Observation) methodology
with tree-based planning for parallelizable execution. It features:

- Hierarchical tree planning with recursive decomposition
- Parallelizable node execution with proper dependencies
- Tool aliasing and forced tool choice
- Structured output models with field validators
- Plan-and-execute pattern with dynamic recompilation
- LLM Compiler inspired parallelization

Reference:
- ReWOO: https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/#solver
- LLM Compiler: https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/


.. autolink-examples:: agents.planning.rewoo_tree_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_tree_agent.PlanNode
   agents.planning.rewoo_tree_agent.PlanTree
   agents.planning.rewoo_tree_agent.ReWOOTreeAgent
   agents.planning.rewoo_tree_agent.ReWOOTreeAgentState
   agents.planning.rewoo_tree_agent.ReWOOTreeExecutorOutput
   agents.planning.rewoo_tree_agent.ReWOOTreePlannerOutput
   agents.planning.rewoo_tree_agent.TaskPriority
   agents.planning.rewoo_tree_agent.TaskStatus
   agents.planning.rewoo_tree_agent.TaskType
   agents.planning.rewoo_tree_agent.ToolAlias


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanNode:

   .. graphviz::
      :align: center

      digraph inheritance_PlanNode {
        node [shape=record];
        "PlanNode" [label="PlanNode"];
        "pydantic.BaseModel" -> "PlanNode";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent.PlanNode
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

   Inheritance diagram for PlanTree:

   .. graphviz::
      :align: center

      digraph inheritance_PlanTree {
        node [shape=record];
        "PlanTree" [label="PlanTree"];
        "pydantic.BaseModel" -> "PlanTree";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent.PlanTree
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

   Inheritance diagram for ReWOOTreeAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeAgent {
        node [shape=record];
        "ReWOOTreeAgent" [label="ReWOOTreeAgent"];
        "haive.agents.base.agent.Agent" -> "ReWOOTreeAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent.ReWOOTreeAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOTreeAgentState:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeAgentState {
        node [shape=record];
        "ReWOOTreeAgentState" [label="ReWOOTreeAgentState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "ReWOOTreeAgentState";
      }

.. autoclass:: agents.planning.rewoo_tree_agent.ReWOOTreeAgentState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOTreeExecutorOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeExecutorOutput {
        node [shape=record];
        "ReWOOTreeExecutorOutput" [label="ReWOOTreeExecutorOutput"];
        "pydantic.BaseModel" -> "ReWOOTreeExecutorOutput";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent.ReWOOTreeExecutorOutput
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

   Inheritance diagram for ReWOOTreePlannerOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreePlannerOutput {
        node [shape=record];
        "ReWOOTreePlannerOutput" [label="ReWOOTreePlannerOutput"];
        "pydantic.BaseModel" -> "ReWOOTreePlannerOutput";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent.ReWOOTreePlannerOutput
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

.. autoclass:: agents.planning.rewoo_tree_agent.TaskPriority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskPriority** is an Enum defined in ``agents.planning.rewoo_tree_agent``.





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

.. autoclass:: agents.planning.rewoo_tree_agent.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskStatus** is an Enum defined in ``agents.planning.rewoo_tree_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskType:

   .. graphviz::
      :align: center

      digraph inheritance_TaskType {
        node [shape=record];
        "TaskType" [label="TaskType"];
        "str" -> "TaskType";
        "enum.Enum" -> "TaskType";
      }

.. autoclass:: agents.planning.rewoo_tree_agent.TaskType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskType** is an Enum defined in ``agents.planning.rewoo_tree_agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolAlias:

   .. graphviz::
      :align: center

      digraph inheritance_ToolAlias {
        node [shape=record];
        "ToolAlias" [label="ToolAlias"];
        "pydantic.BaseModel" -> "ToolAlias";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent.ToolAlias
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

.. autolink-examples:: agents.planning.rewoo_tree_agent
   :collapse:
   
.. autolink-skip:: next
