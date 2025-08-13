
:py:mod:`agents.planning.llm_compiler`
======================================

.. py:module:: agents.planning.llm_compiler

Module exports.


.. autolink-examples:: agents.planning.llm_compiler
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.CompilerPlan
   agents.planning.llm_compiler.CompilerState
   agents.planning.llm_compiler.CompilerStep
   agents.planning.llm_compiler.CompilerTask
   agents.planning.llm_compiler.FinalResponse
   agents.planning.llm_compiler.JoinerOutput
   agents.planning.llm_compiler.LLMCompilerAgent
   agents.planning.llm_compiler.LLMCompilerAgentConfig
   agents.planning.llm_compiler.Replan
   agents.planning.llm_compiler.TaskDependency


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerPlan:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerPlan {
        node [shape=record];
        "CompilerPlan" [label="CompilerPlan"];
        "haive.agents.planning.plan_and_execute.models.Plan" -> "CompilerPlan";
      }

.. autoclass:: agents.planning.llm_compiler.CompilerPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerState:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerState {
        node [shape=record];
        "CompilerState" [label="CompilerState"];
        "pydantic.BaseModel" -> "CompilerState";
      }

.. autopydantic_model:: agents.planning.llm_compiler.CompilerState
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

   Inheritance diagram for CompilerStep:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerStep {
        node [shape=record];
        "CompilerStep" [label="CompilerStep"];
        "haive.agents.planning.plan_and_execute.models.Step" -> "CompilerStep";
      }

.. autoclass:: agents.planning.llm_compiler.CompilerStep
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerTask:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerTask {
        node [shape=record];
        "CompilerTask" [label="CompilerTask"];
        "pydantic.BaseModel" -> "CompilerTask";
      }

.. autopydantic_model:: agents.planning.llm_compiler.CompilerTask
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

   Inheritance diagram for FinalResponse:

   .. graphviz::
      :align: center

      digraph inheritance_FinalResponse {
        node [shape=record];
        "FinalResponse" [label="FinalResponse"];
        "pydantic.BaseModel" -> "FinalResponse";
      }

.. autopydantic_model:: agents.planning.llm_compiler.FinalResponse
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

   Inheritance diagram for JoinerOutput:

   .. graphviz::
      :align: center

      digraph inheritance_JoinerOutput {
        node [shape=record];
        "JoinerOutput" [label="JoinerOutput"];
        "pydantic.BaseModel" -> "JoinerOutput";
      }

.. autopydantic_model:: agents.planning.llm_compiler.JoinerOutput
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

   Inheritance diagram for LLMCompilerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerAgent {
        node [shape=record];
        "LLMCompilerAgent" [label="LLMCompilerAgent"];
        "haive.core.engine.agent.agent.AgentArchitecture" -> "LLMCompilerAgent";
      }

.. autoclass:: agents.planning.llm_compiler.LLMCompilerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LLMCompilerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_LLMCompilerAgentConfig {
        node [shape=record];
        "LLMCompilerAgentConfig" [label="LLMCompilerAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "LLMCompilerAgentConfig";
      }

.. autoclass:: agents.planning.llm_compiler.LLMCompilerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Replan:

   .. graphviz::
      :align: center

      digraph inheritance_Replan {
        node [shape=record];
        "Replan" [label="Replan"];
        "pydantic.BaseModel" -> "Replan";
      }

.. autopydantic_model:: agents.planning.llm_compiler.Replan
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

   Inheritance diagram for TaskDependency:

   .. graphviz::
      :align: center

      digraph inheritance_TaskDependency {
        node [shape=record];
        "TaskDependency" [label="TaskDependency"];
        "pydantic.BaseModel" -> "TaskDependency";
      }

.. autopydantic_model:: agents.planning.llm_compiler.TaskDependency
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

   agents.planning.llm_compiler.main
   agents.planning.llm_compiler.schedule_pending_task
   agents.planning.llm_compiler.schedule_task
   agents.planning.llm_compiler.schedule_tasks

.. py:function:: main() -> None

.. py:function:: schedule_pending_task(task: agents.planning.llm_compiler.models.Task, observations: dict[int, Any], retry_after: float = 0.2)

.. py:function:: schedule_task(task_inputs, config: dict[str, Any])

.. py:function:: schedule_tasks(scheduler_input: agents.planning.llm_compiler.models.SchedulerInput) -> list[langchain_core.messages.FunctionMessage]

   Group the tasks into a DAG schedule.


   .. autolink-examples:: schedule_tasks
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.llm_compiler
   :collapse:
   
.. autolink-skip:: next
