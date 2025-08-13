
:py:mod:`agents.memory.search.pro_search.models`
================================================

.. py:module:: agents.memory.search.pro_search.models

Data models for Pro Search Agent.


.. autolink-examples:: agents.memory.search.pro_search.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.search.pro_search.models.Config
   agents.memory.search.pro_search.models.ContextualInsight
   agents.memory.search.pro_search.models.ProSearchRequest
   agents.memory.search.pro_search.models.ProSearchResponse
   agents.memory.search.pro_search.models.SearchRefinement


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Config:

   .. graphviz::
      :align: center

      digraph inheritance_Config {
        node [shape=record];
        "Config" [label="Config"];
        "pydantic.BaseModel" -> "Config";
      }

.. autopydantic_model:: agents.memory.search.pro_search.models.Config
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

   Inheritance diagram for ContextualInsight:

   .. graphviz::
      :align: center

      digraph inheritance_ContextualInsight {
        node [shape=record];
        "ContextualInsight" [label="ContextualInsight"];
        "pydantic.BaseModel" -> "ContextualInsight";
      }

.. autopydantic_model:: agents.memory.search.pro_search.models.ContextualInsight
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

   Inheritance diagram for ProSearchRequest:

   .. graphviz::
      :align: center

      digraph inheritance_ProSearchRequest {
        node [shape=record];
        "ProSearchRequest" [label="ProSearchRequest"];
        "pydantic.BaseModel" -> "ProSearchRequest";
      }

.. autopydantic_model:: agents.memory.search.pro_search.models.ProSearchRequest
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

   Inheritance diagram for ProSearchResponse:

   .. graphviz::
      :align: center

      digraph inheritance_ProSearchResponse {
        node [shape=record];
        "ProSearchResponse" [label="ProSearchResponse"];
        "haive.agents.memory.search.base.SearchResponse" -> "ProSearchResponse";
      }

.. autoclass:: agents.memory.search.pro_search.models.ProSearchResponse
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SearchRefinement:

   .. graphviz::
      :align: center

      digraph inheritance_SearchRefinement {
        node [shape=record];
        "SearchRefinement" [label="SearchRefinement"];
        "pydantic.BaseModel" -> "SearchRefinement";
      }

.. autopydantic_model:: agents.memory.search.pro_search.models.SearchRefinement
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

.. autolink-examples:: agents.memory.search.pro_search.models
   :collapse:
   
.. autolink-skip:: next
