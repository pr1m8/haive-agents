
:py:mod:`agents.rag.models`
===========================

.. py:module:: agents.rag.models

RAG Agent Models.

This module contains all Pydantic models used by RAG agents for structured
data validation and type safety. These models represent different outputs
and intermediate results from various RAG patterns.

.. rubric:: Example

>>> from haive.agents.rag.models import HyDEResult
>>> result = HyDEResult(
...     hypothetical_doc="Generated document content...",
...     refined_query="Refined query text",
...     confidence=0.85
... )

Typical usage:
    - Import specific models for agent implementations
    - Use for structured output from LLM engines
    - Validate intermediate results in RAG pipelines
    - Type hints for function parameters and returns


.. autolink-examples:: agents.rag.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.models.BranchResult
   agents.rag.models.EnhancedResponse
   agents.rag.models.FusionResult
   agents.rag.models.HyDEResult
   agents.rag.models.MemoryAnalysis
   agents.rag.models.MemoryEntry
   agents.rag.models.MemoryType
   agents.rag.models.MergedResult
   agents.rag.models.QueryClassification
   agents.rag.models.QueryPlan
   agents.rag.models.QueryType
   agents.rag.models.RAGModuleType
   agents.rag.models.ReActStep
   agents.rag.models.ReActStepResult
   agents.rag.models.SpeculativeResult
   agents.rag.models.StepBackResult
   agents.rag.models.StrategyDecision
   agents.rag.models.SubQueryResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BranchResult:

   .. graphviz::
      :align: center

      digraph inheritance_BranchResult {
        node [shape=record];
        "BranchResult" [label="BranchResult"];
        "pydantic.BaseModel" -> "BranchResult";
      }

.. autopydantic_model:: agents.rag.models.BranchResult
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

   Inheritance diagram for EnhancedResponse:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedResponse {
        node [shape=record];
        "EnhancedResponse" [label="EnhancedResponse"];
        "pydantic.BaseModel" -> "EnhancedResponse";
      }

.. autopydantic_model:: agents.rag.models.EnhancedResponse
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

   Inheritance diagram for FusionResult:

   .. graphviz::
      :align: center

      digraph inheritance_FusionResult {
        node [shape=record];
        "FusionResult" [label="FusionResult"];
        "pydantic.BaseModel" -> "FusionResult";
      }

.. autopydantic_model:: agents.rag.models.FusionResult
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

   Inheritance diagram for HyDEResult:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEResult {
        node [shape=record];
        "HyDEResult" [label="HyDEResult"];
        "pydantic.BaseModel" -> "HyDEResult";
      }

.. autopydantic_model:: agents.rag.models.HyDEResult
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

   Inheritance diagram for MemoryAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryAnalysis {
        node [shape=record];
        "MemoryAnalysis" [label="MemoryAnalysis"];
        "pydantic.BaseModel" -> "MemoryAnalysis";
      }

.. autopydantic_model:: agents.rag.models.MemoryAnalysis
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

   Inheritance diagram for MemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryEntry {
        node [shape=record];
        "MemoryEntry" [label="MemoryEntry"];
        "pydantic.BaseModel" -> "MemoryEntry";
      }

.. autopydantic_model:: agents.rag.models.MemoryEntry
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

   Inheritance diagram for MemoryType:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryType {
        node [shape=record];
        "MemoryType" [label="MemoryType"];
        "str" -> "MemoryType";
        "enum.Enum" -> "MemoryType";
      }

.. autoclass:: agents.rag.models.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.rag.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MergedResult:

   .. graphviz::
      :align: center

      digraph inheritance_MergedResult {
        node [shape=record];
        "MergedResult" [label="MergedResult"];
        "pydantic.BaseModel" -> "MergedResult";
      }

.. autopydantic_model:: agents.rag.models.MergedResult
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

   Inheritance diagram for QueryClassification:

   .. graphviz::
      :align: center

      digraph inheritance_QueryClassification {
        node [shape=record];
        "QueryClassification" [label="QueryClassification"];
        "pydantic.BaseModel" -> "QueryClassification";
      }

.. autopydantic_model:: agents.rag.models.QueryClassification
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

   Inheritance diagram for QueryPlan:

   .. graphviz::
      :align: center

      digraph inheritance_QueryPlan {
        node [shape=record];
        "QueryPlan" [label="QueryPlan"];
        "pydantic.BaseModel" -> "QueryPlan";
      }

.. autopydantic_model:: agents.rag.models.QueryPlan
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

   Inheritance diagram for QueryType:

   .. graphviz::
      :align: center

      digraph inheritance_QueryType {
        node [shape=record];
        "QueryType" [label="QueryType"];
        "str" -> "QueryType";
        "enum.Enum" -> "QueryType";
      }

.. autoclass:: agents.rag.models.QueryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **QueryType** is an Enum defined in ``agents.rag.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGModuleType:

   .. graphviz::
      :align: center

      digraph inheritance_RAGModuleType {
        node [shape=record];
        "RAGModuleType" [label="RAGModuleType"];
        "str" -> "RAGModuleType";
        "enum.Enum" -> "RAGModuleType";
      }

.. autoclass:: agents.rag.models.RAGModuleType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGModuleType** is an Enum defined in ``agents.rag.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReActStep:

   .. graphviz::
      :align: center

      digraph inheritance_ReActStep {
        node [shape=record];
        "ReActStep" [label="ReActStep"];
        "str" -> "ReActStep";
        "enum.Enum" -> "ReActStep";
      }

.. autoclass:: agents.rag.models.ReActStep
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ReActStep** is an Enum defined in ``agents.rag.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReActStepResult:

   .. graphviz::
      :align: center

      digraph inheritance_ReActStepResult {
        node [shape=record];
        "ReActStepResult" [label="ReActStepResult"];
        "pydantic.BaseModel" -> "ReActStepResult";
      }

.. autopydantic_model:: agents.rag.models.ReActStepResult
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

   Inheritance diagram for SpeculativeResult:

   .. graphviz::
      :align: center

      digraph inheritance_SpeculativeResult {
        node [shape=record];
        "SpeculativeResult" [label="SpeculativeResult"];
        "pydantic.BaseModel" -> "SpeculativeResult";
      }

.. autopydantic_model:: agents.rag.models.SpeculativeResult
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

   Inheritance diagram for StepBackResult:

   .. graphviz::
      :align: center

      digraph inheritance_StepBackResult {
        node [shape=record];
        "StepBackResult" [label="StepBackResult"];
        "pydantic.BaseModel" -> "StepBackResult";
      }

.. autopydantic_model:: agents.rag.models.StepBackResult
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

   Inheritance diagram for StrategyDecision:

   .. graphviz::
      :align: center

      digraph inheritance_StrategyDecision {
        node [shape=record];
        "StrategyDecision" [label="StrategyDecision"];
        "pydantic.BaseModel" -> "StrategyDecision";
      }

.. autopydantic_model:: agents.rag.models.StrategyDecision
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

   Inheritance diagram for SubQueryResult:

   .. graphviz::
      :align: center

      digraph inheritance_SubQueryResult {
        node [shape=record];
        "SubQueryResult" [label="SubQueryResult"];
        "pydantic.BaseModel" -> "SubQueryResult";
      }

.. autopydantic_model:: agents.rag.models.SubQueryResult
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

.. autolink-examples:: agents.rag.models
   :collapse:
   
.. autolink-skip:: next
