
:py:mod:`agents.memory.search.pro_search.agent`
===============================================

.. py:module:: agents.memory.search.pro_search.agent

Pro Search Agent implementation.

Provides deep, contextual search with user preferences and advanced reasoning.
Similar to Perplexity's Pro Search feature that goes deeper and considers user context.


.. autolink-examples:: agents.memory.search.pro_search.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.search.pro_search.agent.ProSearchAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ProSearchAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ProSearchAgent {
        node [shape=record];
        "ProSearchAgent" [label="ProSearchAgent"];
        "haive.agents.memory.search.base.BaseSearchAgent" -> "ProSearchAgent";
      }

.. autoclass:: agents.memory.search.pro_search.agent.ProSearchAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory.search.pro_search.agent.extract_contextual_insights
   agents.memory.search.pro_search.agent.generate_follow_up_questions
   agents.memory.search.pro_search.agent.generate_reasoning_steps
   agents.memory.search.pro_search.agent.get_response_model
   agents.memory.search.pro_search.agent.get_search_instructions
   agents.memory.search.pro_search.agent.get_system_prompt
   agents.memory.search.pro_search.agent.refine_query

.. py:function:: extract_contextual_insights(content: str, context: dict[str, Any]) -> list[haive.agents.memory.search.pro_search.models.ContextualInsight]

   Extract contextual insights from search content.


   .. autolink-examples:: extract_contextual_insights
      :collapse:

.. py:function:: generate_follow_up_questions(query: str, insights: list[haive.agents.memory.search.pro_search.models.ContextualInsight]) -> list[str]

   Generate follow-up questions based on insights.


   .. autolink-examples:: generate_follow_up_questions
      :collapse:

.. py:function:: generate_reasoning_steps(query: str, refinement: haive.agents.memory.search.pro_search.models.SearchRefinement) -> list[str]

   Generate reasoning steps for complex queries.


   .. autolink-examples:: generate_reasoning_steps
      :collapse:

.. py:function:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

   Get the response model for pro search operations.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get specific search instructions for pro search operations.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get the system prompt for pro search operations.


   .. autolink-examples:: get_system_prompt
      :collapse:

.. py:function:: refine_query(query: str, context: dict[str, Any]) -> haive.agents.memory.search.pro_search.models.SearchRefinement

   Refine a query based on context and preferences.


   .. autolink-examples:: refine_query
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory.search.pro_search.agent
   :collapse:
   
.. autolink-skip:: next
