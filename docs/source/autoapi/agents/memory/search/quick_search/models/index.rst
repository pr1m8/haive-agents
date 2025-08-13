
:py:mod:`agents.memory.search.quick_search.models`
==================================================

.. py:module:: agents.memory.search.quick_search.models

Data models for Quick Search Agent.


.. autolink-examples:: agents.memory.search.quick_search.models
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.search.quick_search.models.Config
   agents.memory.search.quick_search.models.QuickSearchRequest
   agents.memory.search.quick_search.models.QuickSearchResponse


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

.. autopydantic_model:: agents.memory.search.quick_search.models.Config
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

   Inheritance diagram for QuickSearchRequest:

   .. graphviz::
      :align: center

      digraph inheritance_QuickSearchRequest {
        node [shape=record];
        "QuickSearchRequest" [label="QuickSearchRequest"];
        "pydantic.BaseModel" -> "QuickSearchRequest";
      }

.. autopydantic_model:: agents.memory.search.quick_search.models.QuickSearchRequest
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

   Inheritance diagram for QuickSearchResponse:

   .. graphviz::
      :align: center

      digraph inheritance_QuickSearchResponse {
        node [shape=record];
        "QuickSearchResponse" [label="QuickSearchResponse"];
        "haive.agents.memory.search.base.SearchResponse" -> "QuickSearchResponse";
      }

.. autoclass:: agents.memory.search.quick_search.models.QuickSearchResponse
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory.search.quick_search.models
   :collapse:
   
.. autolink-skip:: next
