
:py:mod:`agents.planning.llm_compiler_v3.models`
================================================

.. py:module:: agents.planning.llm_compiler_v3.models

Pydantic models for LLM Compiler V3 Agent.

This module defines structured data models for the LLM Compiler pattern
optimized for Enhanced MultiAgent V3 architecture.


.. autolink-examples:: agents.planning.llm_compiler_v3.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler_v3.models.CompilerInput
   agents.planning.llm_compiler_v3.models.CompilerOutput
   agents.planning.llm_compiler_v3.models.CompilerPlan
   agents.planning.llm_compiler_v3.models.CompilerTask
   agents.planning.llm_compiler_v3.models.ExecutionMode
   agents.planning.llm_compiler_v3.models.ParallelExecutionResult
   agents.planning.llm_compiler_v3.models.ReplanRequest
   agents.planning.llm_compiler_v3.models.TaskDependency


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompilerInput:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerInput {
        node [shape=record];
        "CompilerInput" [label="CompilerInput"];
        "pydantic.BaseModel" -> "CompilerInput";
      }

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.CompilerInput
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

   Inheritance diagram for CompilerOutput:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerOutput {
        node [shape=record];
        "CompilerOutput" [label="CompilerOutput"];
        "pydantic.BaseModel" -> "CompilerOutput";
      }

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.CompilerOutput
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

   Inheritance diagram for CompilerPlan:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerPlan {
        node [shape=record];
        "CompilerPlan" [label="CompilerPlan"];
        "pydantic.BaseModel" -> "CompilerPlan";
      }

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.CompilerPlan
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

   Inheritance diagram for CompilerTask:

   .. graphviz::
      :align: center

      digraph inheritance_CompilerTask {
        node [shape=record];
        "CompilerTask" [label="CompilerTask"];
        "pydantic.BaseModel" -> "CompilerTask";
      }

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.CompilerTask
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

   Inheritance diagram for ExecutionMode:

   .. graphviz::
      :align: center

      digraph inheritance_ExecutionMode {
        node [shape=record];
        "ExecutionMode" [label="ExecutionMode"];
        "str" -> "ExecutionMode";
        "enum.Enum" -> "ExecutionMode";
      }

.. autoclass:: agents.planning.llm_compiler_v3.models.ExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExecutionMode** is an Enum defined in ``agents.planning.llm_compiler_v3.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelExecutionResult {
        node [shape=record];
        "ParallelExecutionResult" [label="ParallelExecutionResult"];
        "pydantic.BaseModel" -> "ParallelExecutionResult";
      }

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.ParallelExecutionResult
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

   Inheritance diagram for ReplanRequest:

   .. graphviz::
      :align: center

      digraph inheritance_ReplanRequest {
        node [shape=record];
        "ReplanRequest" [label="ReplanRequest"];
        "pydantic.BaseModel" -> "ReplanRequest";
      }

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.ReplanRequest
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

.. autopydantic_model:: agents.planning.llm_compiler_v3.models.TaskDependency
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

.. autolink-examples:: agents.planning.llm_compiler_v3.models
   :collapse:
   
.. autolink-skip:: next
