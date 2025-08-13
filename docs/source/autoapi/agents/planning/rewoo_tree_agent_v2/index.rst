
:py:mod:`agents.planning.rewoo_tree_agent_v2`
=============================================

.. py:module:: agents.planning.rewoo_tree_agent_v2

ReWOO Tree-based Planning Agent V2 - Using MultiAgent Pattern.

This agent implements the ReWOO (Reasoning without Observation) methodology
using proper agent composition without manual node creation. All nodes are
created automatically by wrapping agents.

Key improvements:
- No manual node functions - everything is agents
- Uses MultiAgent pattern for composition
- Automatic parallelization through agent dependencies
- Tool aliasing and forced tool choice
- Structured output models with field validators
- Recursive planning through agent composition

Reference:
- ReWOO: https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/#solver
- LLM Compiler: https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/


.. autolink-examples:: agents.planning.rewoo_tree_agent_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v2.ParallelReWOOAgent
   agents.planning.rewoo_tree_agent_v2.PlanTask
   agents.planning.rewoo_tree_agent_v2.ReWOOExecutorAgent
   agents.planning.rewoo_tree_agent_v2.ReWOOPlan
   agents.planning.rewoo_tree_agent_v2.ReWOOPlannerAgent
   agents.planning.rewoo_tree_agent_v2.ReWOOTreeAgent
   agents.planning.rewoo_tree_agent_v2.ReWOOTreeState
   agents.planning.rewoo_tree_agent_v2.TaskPriority
   agents.planning.rewoo_tree_agent_v2.TaskStatus
   agents.planning.rewoo_tree_agent_v2.TaskType
   agents.planning.rewoo_tree_agent_v2.ToolAlias


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelReWOOAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelReWOOAgent {
        node [shape=record];
        "ParallelReWOOAgent" [label="ParallelReWOOAgent"];
        "ReWOOTreeAgent" -> "ParallelReWOOAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v2.ParallelReWOOAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanTask:

   .. graphviz::
      :align: center

      digraph inheritance_PlanTask {
        node [shape=record];
        "PlanTask" [label="PlanTask"];
        "pydantic.BaseModel" -> "PlanTask";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent_v2.PlanTask
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

   Inheritance diagram for ReWOOExecutorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOExecutorAgent {
        node [shape=record];
        "ReWOOExecutorAgent" [label="ReWOOExecutorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "ReWOOExecutorAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v2.ReWOOExecutorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlan {
        node [shape=record];
        "ReWOOPlan" [label="ReWOOPlan"];
        "pydantic.BaseModel" -> "ReWOOPlan";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent_v2.ReWOOPlan
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

   Inheritance diagram for ReWOOPlannerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlannerAgent {
        node [shape=record];
        "ReWOOPlannerAgent" [label="ReWOOPlannerAgent"];
        "haive.agents.simple.agent.SimpleAgent" -> "ReWOOPlannerAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v2.ReWOOPlannerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOTreeAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeAgent {
        node [shape=record];
        "ReWOOTreeAgent" [label="ReWOOTreeAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "ReWOOTreeAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v2.ReWOOTreeAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOTreeState:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeState {
        node [shape=record];
        "ReWOOTreeState" [label="ReWOOTreeState"];
        "haive.core.schema.prebuilt.multi_agent_state.MultiAgentState" -> "ReWOOTreeState";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v2.ReWOOTreeState
   :members:
   :undoc-members:
   :show-inheritance:




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

.. autoclass:: agents.planning.rewoo_tree_agent_v2.TaskPriority
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskPriority** is an Enum defined in ``agents.planning.rewoo_tree_agent_v2``.





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

.. autoclass:: agents.planning.rewoo_tree_agent_v2.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskStatus** is an Enum defined in ``agents.planning.rewoo_tree_agent_v2``.





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

.. autoclass:: agents.planning.rewoo_tree_agent_v2.TaskType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskType** is an Enum defined in ``agents.planning.rewoo_tree_agent_v2``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolAlias:

   .. graphviz::
      :align: center

      digraph inheritance_ToolAlias {
        node [shape=record];
        "ToolAlias" [label="ToolAlias"];
        "pydantic.BaseModel" -> "ToolAlias";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent_v2.ToolAlias
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



Functions
---------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v2.create_rewoo_agent_with_tools

.. py:function:: create_rewoo_agent_with_tools(tools: list[langchain_core.tools.BaseTool], tool_aliases: dict[str, str] | None = None, max_parallelism: int = 4) -> ReWOOTreeAgent

   Factory function to create a ReWOO agent with tools.

   :param tools: List of tools available to the agent
   :param tool_aliases: Mapping of alias names to actual tool names
   :param max_parallelism: Maximum parallel executions

   :returns: Configured ReWOOTreeAgent


   .. autolink-examples:: create_rewoo_agent_with_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo_tree_agent_v2
   :collapse:
   
.. autolink-skip:: next
