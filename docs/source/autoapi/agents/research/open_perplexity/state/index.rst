
:py:mod:`agents.research.open_perplexity.state`
===============================================

.. py:module:: agents.research.open_perplexity.state

State schemas for the open_perplexity research agent.

This module defines the state schemas used by the research agent to track
the progress of research, manage search queries, store sources, and generate
reports. It includes schemas for input, processing state, and output.


.. autolink-examples:: agents.research.open_perplexity.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.research.open_perplexity.state.ReportSection
   agents.research.open_perplexity.state.ResearchConfidenceLevel
   agents.research.open_perplexity.state.ResearchInputState
   agents.research.open_perplexity.state.ResearchOutputState
   agents.research.open_perplexity.state.ResearchState
   agents.research.open_perplexity.state.WebSearchQuery


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReportSection:

   .. graphviz::
      :align: center

      digraph inheritance_ReportSection {
        node [shape=record];
        "ReportSection" [label="ReportSection"];
        "pydantic.BaseModel" -> "ReportSection";
      }

.. autopydantic_model:: agents.research.open_perplexity.state.ReportSection
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

   Inheritance diagram for ResearchConfidenceLevel:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchConfidenceLevel {
        node [shape=record];
        "ResearchConfidenceLevel" [label="ResearchConfidenceLevel"];
        "str" -> "ResearchConfidenceLevel";
        "enum.Enum" -> "ResearchConfidenceLevel";
      }

.. autoclass:: agents.research.open_perplexity.state.ResearchConfidenceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ResearchConfidenceLevel** is an Enum defined in ``agents.research.open_perplexity.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ResearchInputState:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchInputState {
        node [shape=record];
        "ResearchInputState" [label="ResearchInputState"];
        "pydantic.BaseModel" -> "ResearchInputState";
      }

.. autopydantic_model:: agents.research.open_perplexity.state.ResearchInputState
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

   Inheritance diagram for ResearchOutputState:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchOutputState {
        node [shape=record];
        "ResearchOutputState" [label="ResearchOutputState"];
        "pydantic.BaseModel" -> "ResearchOutputState";
      }

.. autopydantic_model:: agents.research.open_perplexity.state.ResearchOutputState
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

   Inheritance diagram for ResearchState:

   .. graphviz::
      :align: center

      digraph inheritance_ResearchState {
        node [shape=record];
        "ResearchState" [label="ResearchState"];
        "pydantic.BaseModel" -> "ResearchState";
      }

.. autopydantic_model:: agents.research.open_perplexity.state.ResearchState
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

   Inheritance diagram for WebSearchQuery:

   .. graphviz::
      :align: center

      digraph inheritance_WebSearchQuery {
        node [shape=record];
        "WebSearchQuery" [label="WebSearchQuery"];
        "pydantic.BaseModel" -> "WebSearchQuery";
      }

.. autopydantic_model:: agents.research.open_perplexity.state.WebSearchQuery
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

.. autolink-examples:: agents.research.open_perplexity.state
   :collapse:
   
.. autolink-skip:: next
