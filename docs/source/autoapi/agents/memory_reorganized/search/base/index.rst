
:py:mod:`agents.memory_reorganized.search.base`
===============================================

.. py:module:: agents.memory_reorganized.search.base

Base classes for search agents.

This module provides the foundation for all search agents in the memory system, with
common functionality for memory integration, tool management, and structured outputs.


.. autolink-examples:: agents.memory_reorganized.search.base
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.base.BaseSearchAgent
   agents.memory_reorganized.search.base.SearchResponse


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseSearchAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BaseSearchAgent {
        node [shape=record];
        "BaseSearchAgent" [label="BaseSearchAgent"];
        "haive.agents.react.agent.ReactAgent" -> "BaseSearchAgent";
        "abc.ABC" -> "BaseSearchAgent";
      }

.. autoclass:: agents.memory_reorganized.search.base.BaseSearchAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SearchResponse:

   .. graphviz::
      :align: center

      digraph inheritance_SearchResponse {
        node [shape=record];
        "SearchResponse" [label="SearchResponse"];
        "pydantic.BaseModel" -> "SearchResponse";
      }

.. autopydantic_model:: agents.memory_reorganized.search.base.SearchResponse
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

   agents.memory_reorganized.search.base.extract_memory_items
   agents.memory_reorganized.search.base.format_search_context
   agents.memory_reorganized.search.base.get_response_model
   agents.memory_reorganized.search.base.get_search_instructions
   agents.memory_reorganized.search.base.get_system_prompt

.. py:function:: extract_memory_items(memory_data: Any) -> list[str]

   Extract memory items from memory data structure.

   :param memory_data: Raw memory data from various sources

   :returns: List of formatted memory items as strings


   .. autolink-examples:: extract_memory_items
      :collapse:

.. py:function:: format_search_context(query: str, context: dict[str, Any]) -> str

   Format search context for agents (module-level utility function).

   :param query: The user's search query
   :param context: Additional context including memory, preferences, etc.

   :returns: Formatted context string for the agent


   .. autolink-examples:: format_search_context
      :collapse:

.. py:function:: get_response_model() -> type[SearchResponse]

   Get the response model for search agents.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get generic search instructions.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get generic system prompt for search agents.


   .. autolink-examples:: get_system_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.search.base
   :collapse:
   
.. autolink-skip:: next
