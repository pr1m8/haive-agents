
:py:mod:`agents.discovery.semantic_discovery`
=============================================

.. py:module:: agents.discovery.semantic_discovery

Semantic Discovery Engine with Vector-Based Tool Selection.

This module implements semantic discovery capabilities inspired by LangGraph's
many-tools pattern, using vector embeddings to match tools and components
based on query content and semantic similarity.

Key Features:
- Vector-based tool discovery and ranking
- Semantic capability matching
- Query analysis and tool recommendation
- Dynamic tool binding and selection
- Context-aware component matching


.. autolink-examples:: agents.discovery.semantic_discovery
   :collapse:

Classes
-------

.. autoapisummary::

   agents.discovery.semantic_discovery.CapabilityMatcher
   agents.discovery.semantic_discovery.DiscoveryMode
   agents.discovery.semantic_discovery.QueryAnalysis
   agents.discovery.semantic_discovery.QueryAnalyzer
   agents.discovery.semantic_discovery.SemanticDiscoveryEngine
   agents.discovery.semantic_discovery.ToolSelectionStrategy
   agents.discovery.semantic_discovery.VectorBasedToolSelector


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CapabilityMatcher:

   .. graphviz::
      :align: center

      digraph inheritance_CapabilityMatcher {
        node [shape=record];
        "CapabilityMatcher" [label="CapabilityMatcher"];
        "pydantic.BaseModel" -> "CapabilityMatcher";
      }

.. autopydantic_model:: agents.discovery.semantic_discovery.CapabilityMatcher
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

   Inheritance diagram for DiscoveryMode:

   .. graphviz::
      :align: center

      digraph inheritance_DiscoveryMode {
        node [shape=record];
        "DiscoveryMode" [label="DiscoveryMode"];
        "str" -> "DiscoveryMode";
        "enum.Enum" -> "DiscoveryMode";
      }

.. autoclass:: agents.discovery.semantic_discovery.DiscoveryMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **DiscoveryMode** is an Enum defined in ``agents.discovery.semantic_discovery``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_QueryAnalysis {
        node [shape=record];
        "QueryAnalysis" [label="QueryAnalysis"];
      }

.. autoclass:: agents.discovery.semantic_discovery.QueryAnalysis
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QueryAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_QueryAnalyzer {
        node [shape=record];
        "QueryAnalyzer" [label="QueryAnalyzer"];
        "pydantic.BaseModel" -> "QueryAnalyzer";
      }

.. autopydantic_model:: agents.discovery.semantic_discovery.QueryAnalyzer
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

   Inheritance diagram for SemanticDiscoveryEngine:

   .. graphviz::
      :align: center

      digraph inheritance_SemanticDiscoveryEngine {
        node [shape=record];
        "SemanticDiscoveryEngine" [label="SemanticDiscoveryEngine"];
        "pydantic.BaseModel" -> "SemanticDiscoveryEngine";
      }

.. autopydantic_model:: agents.discovery.semantic_discovery.SemanticDiscoveryEngine
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

   Inheritance diagram for ToolSelectionStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_ToolSelectionStrategy {
        node [shape=record];
        "ToolSelectionStrategy" [label="ToolSelectionStrategy"];
        "str" -> "ToolSelectionStrategy";
        "enum.Enum" -> "ToolSelectionStrategy";
      }

.. autoclass:: agents.discovery.semantic_discovery.ToolSelectionStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ToolSelectionStrategy** is an Enum defined in ``agents.discovery.semantic_discovery``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for VectorBasedToolSelector:

   .. graphviz::
      :align: center

      digraph inheritance_VectorBasedToolSelector {
        node [shape=record];
        "VectorBasedToolSelector" [label="VectorBasedToolSelector"];
        "pydantic.BaseModel" -> "VectorBasedToolSelector";
      }

.. autopydantic_model:: agents.discovery.semantic_discovery.VectorBasedToolSelector
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

   agents.discovery.semantic_discovery._lazy_import_strategies
   agents.discovery.semantic_discovery.create_component_registry
   agents.discovery.semantic_discovery.create_semantic_discovery

.. py:function:: _lazy_import_strategies()

   Lazy import to avoid circular imports.


   .. autolink-examples:: _lazy_import_strategies
      :collapse:

.. py:function:: create_component_registry(**kwargs)

.. py:function:: create_semantic_discovery() -> SemanticDiscoveryEngine

   Create a semantic discovery engine with default configuration.


   .. autolink-examples:: create_semantic_discovery
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.discovery.semantic_discovery
   :collapse:
   
.. autolink-skip:: next
