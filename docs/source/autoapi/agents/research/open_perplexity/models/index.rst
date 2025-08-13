
:py:mod:`agents.research.open_perplexity.models`
================================================

.. py:module:: agents.research.open_perplexity.models

Models for the open_perplexity research agent.

from typing import Any
This module defines data models used for representing, tracking, and evaluating
research sources, findings, and summaries. It includes enumerations for categorizing
data source types, content reliability, freshness, and research depth.


.. autolink-examples:: agents.research.open_perplexity.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.research.open_perplexity.models.ContentFreshness
   agents.research.open_perplexity.models.ContentReliability
   agents.research.open_perplexity.models.DataSourceConfig
   agents.research.open_perplexity.models.DataSourceType
   agents.research.open_perplexity.models.ResearchDepth
   agents.research.open_perplexity.models.ResearchFinding
   agents.research.open_perplexity.models.ResearchSource
   agents.research.open_perplexity.models.ResearchSummary


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContentFreshness:

   .. graphviz::
      :align: center

      digraph inheritance_ContentFreshness {
        node [shape=record];
        "ContentFreshness" [label="ContentFreshness"];
        "str" -> "ContentFreshness";
        "enum.Enum" -> "ContentFreshness";
      }

.. autoclass:: agents.research.open_perplexity.models.ContentFreshness
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ContentFreshness** is an Enum defined in ``agents.research.open_perplexity.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContentReliability:

   .. graphviz::
      :align: center

      digraph inheritance_ContentReliability {
        node [shape=record];
        "ContentReliability" [label="ContentReliability"];
        "str" -> "ContentReliability";
        "enum.Enum" -> "ContentReliability";
      }

.. autoclass:: agents.research.open_perplexity.models.ContentReliability
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ContentReliability** is an Enum defined in ``agents.research.open_perplexity.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DataSourceConfig:

   .. graphviz::
      :align: center

      digraph inheritance_DataSourceConfig {
        node [shape=record];
        "DataSourceConfig" [label="DataSourceConfig"];
        "pydantic.BaseModel" -> "DataSourceConfig";
      }

.. autopydantic_model:: agents.research.open_perplexity.models.DataSourceConfig
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

   Inheritance diagram for DataSourceType:

   .. graphviz::
      :align: center

      digraph inheritance_DataSourceType {
        node [shape=record];
        "DataSourceType" [label="DataSourceType"];
        "str" -> "DataSourceType";
        "enum.Enum" -> "DataSourceType";
      }

.. autoclass:: agents.research.open_perplexity.models.DataSourceType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **DataSourceType** is an Enum defined in ``agents.research.open_perplexity.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchDepth:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchDepth {
        node [shape=record];
        "ResearchDepth" [label="ResearchDepth"];
        "str" -> "ResearchDepth";
        "enum.Enum" -> "ResearchDepth";
      }

.. autoclass:: agents.research.open_perplexity.models.ResearchDepth
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ResearchDepth** is an Enum defined in ``agents.research.open_perplexity.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchFinding:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchFinding {
        node [shape=record];
        "ResearchFinding" [label="ResearchFinding"];
        "pydantic.BaseModel" -> "ResearchFinding";
      }

.. autopydantic_model:: agents.research.open_perplexity.models.ResearchFinding
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

   Inheritance diagram for ResearchSource:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchSource {
        node [shape=record];
        "ResearchSource" [label="ResearchSource"];
        "pydantic.BaseModel" -> "ResearchSource";
      }

.. autopydantic_model:: agents.research.open_perplexity.models.ResearchSource
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

   Inheritance diagram for ResearchSummary:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchSummary {
        node [shape=record];
        "ResearchSummary" [label="ResearchSummary"];
        "pydantic.BaseModel" -> "ResearchSummary";
      }

.. autopydantic_model:: agents.research.open_perplexity.models.ResearchSummary
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

.. autolink-examples:: agents.research.open_perplexity.models
   :collapse:
   
.. autolink-skip:: next
