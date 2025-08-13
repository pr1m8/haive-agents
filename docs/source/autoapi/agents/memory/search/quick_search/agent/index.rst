
:py:mod:`agents.memory.search.quick_search.agent`
=================================================

.. py:module:: agents.memory.search.quick_search.agent

Quick Search Agent implementation.

Provides fast, basic search responses optimized for speed and concise answers.
Similar to Perplexity's Quick Search feature.


.. autolink-examples:: agents.memory.search.quick_search.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.search.quick_search.agent.QuickSearchAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for QuickSearchAgent:

   .. graphviz::
      :align: center

      digraph inheritance_QuickSearchAgent {
        node [shape=record];
        "QuickSearchAgent" [label="QuickSearchAgent"];
        "haive.agents.memory.search.base.BaseSearchAgent" -> "QuickSearchAgent";
      }

.. autoclass:: agents.memory.search.quick_search.agent.QuickSearchAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory.search.quick_search.agent.determine_answer_type
   agents.memory.search.quick_search.agent.extract_keywords
   agents.memory.search.quick_search.agent.get_response_model
   agents.memory.search.quick_search.agent.get_search_instructions
   agents.memory.search.quick_search.agent.get_system_prompt

.. py:function:: determine_answer_type(query: str) -> str

   Determine the type of answer needed for a query.


   .. autolink-examples:: determine_answer_type
      :collapse:

.. py:function:: extract_keywords(query: str) -> list[str]

   Extract keywords from a query.


   .. autolink-examples:: extract_keywords
      :collapse:

.. py:function:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

   Get the response model for quick search operations.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get specific search instructions for quick search operations.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get the system prompt for quick search operations.


   .. autolink-examples:: get_system_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory.search.quick_search.agent
   :collapse:
   
.. autolink-skip:: next
