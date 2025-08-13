
:py:mod:`agents.planning.llm_compiler.models`
=============================================

.. py:module:: agents.planning.llm_compiler.models

Models for the LLM Compiler agent.

This module defines the pydantic models specific to the LLM Compiler agent,
integrating with the base Step and Plan models from the plan_and_execute agent.


.. autolink-examples:: agents.planning.llm_compiler.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.models.CompilerPlan
   agents.planning.llm_compiler.models.CompilerStep
   agents.planning.llm_compiler.models.CompilerTask
   agents.planning.llm_compiler.models.FinalResponse
   agents.planning.llm_compiler.models.JoinerOutput
   agents.planning.llm_compiler.models.Replan
   agents.planning.llm_compiler.models.TaskDependency


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

.. autoclass:: agents.planning.llm_compiler.models.CompilerPlan
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerStep:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerStep {
        node [shape=record];
        "CompilerStep" [label="CompilerStep"];
        "haive.agents.planning.plan_and_execute.models.Step" -> "CompilerStep";
      }

.. autoclass:: agents.planning.llm_compiler.models.CompilerStep
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

.. autopydantic_model:: agents.planning.llm_compiler.models.CompilerTask
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

.. autopydantic_model:: agents.planning.llm_compiler.models.FinalResponse
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

.. autopydantic_model:: agents.planning.llm_compiler.models.JoinerOutput
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

   Inheritance diagram for Replan:

   .. graphviz::
      :align: center

      digraph inheritance_Replan {
        node [shape=record];
        "Replan" [label="Replan"];
        "pydantic.BaseModel" -> "Replan";
      }

.. autopydantic_model:: agents.planning.llm_compiler.models.Replan
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

.. autopydantic_model:: agents.planning.llm_compiler.models.TaskDependency
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

.. autolink-examples:: agents.planning.llm_compiler.models
   :collapse:
   
.. autolink-skip:: next
