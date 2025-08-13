
:py:mod:`agents.reasoning_and_critique.logic.models`
====================================================

.. py:module:: agents.reasoning_and_critique.logic.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.logic.models.ArgumentStrength
   agents.reasoning_and_critique.logic.models.ArgumentStructure
   agents.reasoning_and_critique.logic.models.Assumption
   agents.reasoning_and_critique.logic.models.BiasAssessment
   agents.reasoning_and_critique.logic.models.BiasType
   agents.reasoning_and_critique.logic.models.CertaintyLevel
   agents.reasoning_and_critique.logic.models.CounterArgument
   agents.reasoning_and_critique.logic.models.Evidence
   agents.reasoning_and_critique.logic.models.EvidenceType
   agents.reasoning_and_critique.logic.models.FallacyDetection
   agents.reasoning_and_critique.logic.models.LogicalFallacy
   agents.reasoning_and_critique.logic.models.LogicalStep
   agents.reasoning_and_critique.logic.models.Premise
   agents.reasoning_and_critique.logic.models.ReasoningAnalysis
   agents.reasoning_and_critique.logic.models.ReasoningChain
   agents.reasoning_and_critique.logic.models.ReasoningQuality
   agents.reasoning_and_critique.logic.models.ReasoningReport
   agents.reasoning_and_critique.logic.models.ReasoningType
   agents.reasoning_and_critique.logic.models.UncertaintyAnalysis


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ArgumentStrength:

   .. graphviz::
      :align: center

      digraph inheritance_ArgumentStrength {
        node [shape=record];
        "ArgumentStrength" [label="ArgumentStrength"];
        "str" -> "ArgumentStrength";
        "enum.Enum" -> "ArgumentStrength";
      }

.. autoclass:: agents.reasoning_and_critique.logic.models.ArgumentStrength
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ArgumentStrength** is an Enum defined in ``agents.reasoning_and_critique.logic.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ArgumentStructure:

   .. graphviz::
      :align: center

      digraph inheritance_ArgumentStructure {
        node [shape=record];
        "ArgumentStructure" [label="ArgumentStructure"];
        "pydantic.BaseModel" -> "ArgumentStructure";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.ArgumentStructure
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

   Inheritance diagram for Assumption:

   .. graphviz::
      :align: center

      digraph inheritance_Assumption {
        node [shape=record];
        "Assumption" [label="Assumption"];
        "pydantic.BaseModel" -> "Assumption";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.Assumption
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

   Inheritance diagram for BiasAssessment:

   .. graphviz::
      :align: center

      digraph inheritance_BiasAssessment {
        node [shape=record];
        "BiasAssessment" [label="BiasAssessment"];
        "pydantic.BaseModel" -> "BiasAssessment";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.BiasAssessment
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

   Inheritance diagram for BiasType:

   .. graphviz::
      :align: center

      digraph inheritance_BiasType {
        node [shape=record];
        "BiasType" [label="BiasType"];
        "str" -> "BiasType";
        "enum.Enum" -> "BiasType";
      }

.. autoclass:: agents.reasoning_and_critique.logic.models.BiasType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **BiasType** is an Enum defined in ``agents.reasoning_and_critique.logic.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CertaintyLevel:

   .. graphviz::
      :align: center

      digraph inheritance_CertaintyLevel {
        node [shape=record];
        "CertaintyLevel" [label="CertaintyLevel"];
        "str" -> "CertaintyLevel";
        "enum.Enum" -> "CertaintyLevel";
      }

.. autoclass:: agents.reasoning_and_critique.logic.models.CertaintyLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CertaintyLevel** is an Enum defined in ``agents.reasoning_and_critique.logic.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CounterArgument:

   .. graphviz::
      :align: center

      digraph inheritance_CounterArgument {
        node [shape=record];
        "CounterArgument" [label="CounterArgument"];
        "pydantic.BaseModel" -> "CounterArgument";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.CounterArgument
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

   Inheritance diagram for Evidence:

   .. graphviz::
      :align: center

      digraph inheritance_Evidence {
        node [shape=record];
        "Evidence" [label="Evidence"];
        "pydantic.BaseModel" -> "Evidence";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.Evidence
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

   Inheritance diagram for EvidenceType:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceType {
        node [shape=record];
        "EvidenceType" [label="EvidenceType"];
        "str" -> "EvidenceType";
        "enum.Enum" -> "EvidenceType";
      }

.. autoclass:: agents.reasoning_and_critique.logic.models.EvidenceType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **EvidenceType** is an Enum defined in ``agents.reasoning_and_critique.logic.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FallacyDetection:

   .. graphviz::
      :align: center

      digraph inheritance_FallacyDetection {
        node [shape=record];
        "FallacyDetection" [label="FallacyDetection"];
        "pydantic.BaseModel" -> "FallacyDetection";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.FallacyDetection
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

   Inheritance diagram for LogicalFallacy:

   .. graphviz::
      :align: center

      digraph inheritance_LogicalFallacy {
        node [shape=record];
        "LogicalFallacy" [label="LogicalFallacy"];
        "str" -> "LogicalFallacy";
        "enum.Enum" -> "LogicalFallacy";
      }

.. autoclass:: agents.reasoning_and_critique.logic.models.LogicalFallacy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **LogicalFallacy** is an Enum defined in ``agents.reasoning_and_critique.logic.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LogicalStep:

   .. graphviz::
      :align: center

      digraph inheritance_LogicalStep {
        node [shape=record];
        "LogicalStep" [label="LogicalStep"];
        "pydantic.BaseModel" -> "LogicalStep";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.LogicalStep
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

   Inheritance diagram for Premise:

   .. graphviz::
      :align: center

      digraph inheritance_Premise {
        node [shape=record];
        "Premise" [label="Premise"];
        "pydantic.BaseModel" -> "Premise";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.Premise
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

   Inheritance diagram for ReasoningAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningAnalysis {
        node [shape=record];
        "ReasoningAnalysis" [label="ReasoningAnalysis"];
        "pydantic.BaseModel" -> "ReasoningAnalysis";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.ReasoningAnalysis
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

   Inheritance diagram for ReasoningChain:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningChain {
        node [shape=record];
        "ReasoningChain" [label="ReasoningChain"];
        "pydantic.BaseModel" -> "ReasoningChain";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.ReasoningChain
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

   Inheritance diagram for ReasoningQuality:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningQuality {
        node [shape=record];
        "ReasoningQuality" [label="ReasoningQuality"];
        "pydantic.BaseModel" -> "ReasoningQuality";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.ReasoningQuality
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

   Inheritance diagram for ReasoningReport:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningReport {
        node [shape=record];
        "ReasoningReport" [label="ReasoningReport"];
        "pydantic.BaseModel" -> "ReasoningReport";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.ReasoningReport
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

   Inheritance diagram for ReasoningType:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningType {
        node [shape=record];
        "ReasoningType" [label="ReasoningType"];
        "str" -> "ReasoningType";
        "enum.Enum" -> "ReasoningType";
      }

.. autoclass:: agents.reasoning_and_critique.logic.models.ReasoningType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ReasoningType** is an Enum defined in ``agents.reasoning_and_critique.logic.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UncertaintyAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_UncertaintyAnalysis {
        node [shape=record];
        "UncertaintyAnalysis" [label="UncertaintyAnalysis"];
        "pydantic.BaseModel" -> "UncertaintyAnalysis";
      }

.. autopydantic_model:: agents.reasoning_and_critique.logic.models.UncertaintyAnalysis
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

.. autolink-examples:: agents.reasoning_and_critique.logic.models
   :collapse:
   
.. autolink-skip:: next
