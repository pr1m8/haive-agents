
:py:mod:`agents.reflection.models`
==================================

.. py:module:: agents.reflection.models

Models for reflection agent outputs and configurations.


.. autolink-examples:: agents.reflection.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.reflection.models.Critique
   agents.reflection.models.ExpertiseConfig
   agents.reflection.models.GradingResult
   agents.reflection.models.Improvement
   agents.reflection.models.ImprovementSuggestion
   agents.reflection.models.QualityScore
   agents.reflection.models.ReflectionConfig
   agents.reflection.models.ReflectionOutput
   agents.reflection.models.ReflectionResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Critique:

   .. graphviz::
      :align: center

      digraph inheritance_Critique {
        node [shape=record];
        "Critique" [label="Critique"];
        "pydantic.BaseModel" -> "Critique";
      }

.. autopydantic_model:: agents.reflection.models.Critique
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

   Inheritance diagram for ExpertiseConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ExpertiseConfig {
        node [shape=record];
        "ExpertiseConfig" [label="ExpertiseConfig"];
        "pydantic.BaseModel" -> "ExpertiseConfig";
      }

.. autopydantic_model:: agents.reflection.models.ExpertiseConfig
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

   Inheritance diagram for GradingResult:

   .. graphviz::
      :align: center

      digraph inheritance_GradingResult {
        node [shape=record];
        "GradingResult" [label="GradingResult"];
        "pydantic.BaseModel" -> "GradingResult";
      }

.. autopydantic_model:: agents.reflection.models.GradingResult
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

   Inheritance diagram for Improvement:

   .. graphviz::
      :align: center

      digraph inheritance_Improvement {
        node [shape=record];
        "Improvement" [label="Improvement"];
        "pydantic.BaseModel" -> "Improvement";
      }

.. autopydantic_model:: agents.reflection.models.Improvement
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

   Inheritance diagram for ImprovementSuggestion:

   .. graphviz::
      :align: center

      digraph inheritance_ImprovementSuggestion {
        node [shape=record];
        "ImprovementSuggestion" [label="ImprovementSuggestion"];
        "pydantic.BaseModel" -> "ImprovementSuggestion";
      }

.. autopydantic_model:: agents.reflection.models.ImprovementSuggestion
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

   Inheritance diagram for QualityScore:

   .. graphviz::
      :align: center

      digraph inheritance_QualityScore {
        node [shape=record];
        "QualityScore" [label="QualityScore"];
        "pydantic.BaseModel" -> "QualityScore";
      }

.. autopydantic_model:: agents.reflection.models.QualityScore
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

   Inheritance diagram for ReflectionConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionConfig {
        node [shape=record];
        "ReflectionConfig" [label="ReflectionConfig"];
        "pydantic.BaseModel" -> "ReflectionConfig";
      }

.. autopydantic_model:: agents.reflection.models.ReflectionConfig
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

   Inheritance diagram for ReflectionOutput:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionOutput {
        node [shape=record];
        "ReflectionOutput" [label="ReflectionOutput"];
        "pydantic.BaseModel" -> "ReflectionOutput";
      }

.. autopydantic_model:: agents.reflection.models.ReflectionOutput
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

   Inheritance diagram for ReflectionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionResult {
        node [shape=record];
        "ReflectionResult" [label="ReflectionResult"];
        "pydantic.BaseModel" -> "ReflectionResult";
      }

.. autopydantic_model:: agents.reflection.models.ReflectionResult
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

   agents.reflection.models.to_prompt
   agents.reflection.models.validate_grade_matches_score

.. py:function:: to_prompt(obj) -> str

   Convert object to prompt string.


   .. autolink-examples:: to_prompt
      :collapse:

.. py:function:: validate_grade_matches_score(*args, **kwargs)

   Validate grade matches score (compatibility function).


   .. autolink-examples:: validate_grade_matches_score
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.models
   :collapse:
   
.. autolink-skip:: next
