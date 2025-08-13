
:py:mod:`pro_search.models`
===========================

.. py:module:: pro_search.models

Pydantic models for Perplexity-style quick search workflow.
from typing import Any
These models support a multi-stage search process with reasoning, query generation,
parallel search execution, and synthesis.


.. autolink-examples:: pro_search.models
   :collapse:

Classes
-------

.. autoapisummary::

   pro_search.models.ContentAnalysis
   pro_search.models.PerplexitySearchState
   pro_search.models.QueryBatch
   pro_search.models.QueryIntent
   pro_search.models.QueryReasoning
   pro_search.models.SearchContext
   pro_search.models.SearchQueryConfig
   pro_search.models.SearchQueryResult
   pro_search.models.SearchResult
   pro_search.models.SearchSynthesis


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ContentAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ContentAnalysis {
        node [shape=record];
        "ContentAnalysis" [label="ContentAnalysis"];
        "pydantic.BaseModel" -> "ContentAnalysis";
      }

.. autopydantic_model:: pro_search.models.ContentAnalysis
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

   Inheritance diagram for PerplexitySearchState:

   .. graphviz::
      :align: center

      digraph inheritance_PerplexitySearchState {
        node [shape=record];
        "PerplexitySearchState" [label="PerplexitySearchState"];
        "pydantic.BaseModel" -> "PerplexitySearchState";
      }

.. autopydantic_model:: pro_search.models.PerplexitySearchState
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

   Inheritance diagram for QueryBatch:

   .. graphviz::
      :align: center

      digraph inheritance_QueryBatch {
        node [shape=record];
        "QueryBatch" [label="QueryBatch"];
        "pydantic.BaseModel" -> "QueryBatch";
      }

.. autopydantic_model:: pro_search.models.QueryBatch
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

   Inheritance diagram for QueryIntent:

   .. graphviz::
      :align: center

      digraph inheritance_QueryIntent {
        node [shape=record];
        "QueryIntent" [label="QueryIntent"];
        "pydantic.BaseModel" -> "QueryIntent";
      }

.. autopydantic_model:: pro_search.models.QueryIntent
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

   Inheritance diagram for QueryReasoning:

   .. graphviz::
      :align: center

      digraph inheritance_QueryReasoning {
        node [shape=record];
        "QueryReasoning" [label="QueryReasoning"];
        "pydantic.BaseModel" -> "QueryReasoning";
      }

.. autopydantic_model:: pro_search.models.QueryReasoning
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

   Inheritance diagram for SearchContext:

   .. graphviz::
      :align: center

      digraph inheritance_SearchContext {
        node [shape=record];
        "SearchContext" [label="SearchContext"];
        "pydantic.BaseModel" -> "SearchContext";
      }

.. autopydantic_model:: pro_search.models.SearchContext
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

   Inheritance diagram for SearchQueryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SearchQueryConfig {
        node [shape=record];
        "SearchQueryConfig" [label="SearchQueryConfig"];
        "pydantic.BaseModel" -> "SearchQueryConfig";
      }

.. autopydantic_model:: pro_search.models.SearchQueryConfig
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

   Inheritance diagram for SearchQueryResult:

   .. graphviz::
      :align: center

      digraph inheritance_SearchQueryResult {
        node [shape=record];
        "SearchQueryResult" [label="SearchQueryResult"];
        "pydantic.BaseModel" -> "SearchQueryResult";
      }

.. autopydantic_model:: pro_search.models.SearchQueryResult
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

   Inheritance diagram for SearchResult:

   .. graphviz::
      :align: center

      digraph inheritance_SearchResult {
        node [shape=record];
        "SearchResult" [label="SearchResult"];
        "pydantic.BaseModel" -> "SearchResult";
      }

.. autopydantic_model:: pro_search.models.SearchResult
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

   Inheritance diagram for SearchSynthesis:

   .. graphviz::
      :align: center

      digraph inheritance_SearchSynthesis {
        node [shape=record];
        "SearchSynthesis" [label="SearchSynthesis"];
        "pydantic.BaseModel" -> "SearchSynthesis";
      }

.. autopydantic_model:: pro_search.models.SearchSynthesis
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

.. autolink-examples:: pro_search.models
   :collapse:
   
.. autolink-skip:: next
