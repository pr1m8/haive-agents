
:py:mod:`agents.memory.search.deep_research.agent`
==================================================

.. py:module:: agents.memory.search.deep_research.agent

Deep Research Agent implementation.

Provides comprehensive research with multiple sources and detailed analysis.
Similar to Perplexity's Deep Research feature that performs dozens of searches
and reads hundreds of sources.


.. autolink-examples:: agents.memory.search.deep_research.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.search.deep_research.agent.DeepResearchAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DeepResearchAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DeepResearchAgent {
        node [shape=record];
        "DeepResearchAgent" [label="DeepResearchAgent"];
        "haive.agents.memory.search.base.BaseSearchAgent" -> "DeepResearchAgent";
      }

.. autoclass:: agents.memory.search.deep_research.agent.DeepResearchAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory.search.deep_research.agent.decompose_research_query
   agents.memory.search.deep_research.agent.evaluate_source_credibility
   agents.memory.search.deep_research.agent.generate_executive_summary
   agents.memory.search.deep_research.agent.get_response_model
   agents.memory.search.deep_research.agent.get_search_instructions
   agents.memory.search.deep_research.agent.get_system_prompt
   agents.memory.search.deep_research.agent.organize_findings_by_theme

.. py:function:: decompose_research_query(query: str, focus_areas: list[str] | None = None) -> list[str]

   Decompose a complex research query into specific sub-queries.


   .. autolink-examples:: decompose_research_query
      :collapse:

.. py:function:: evaluate_source_credibility(source: dict[str, Any]) -> float

   Evaluate the credibility of a source.


   .. autolink-examples:: evaluate_source_credibility
      :collapse:

.. py:function:: generate_executive_summary(sections: list[haive.agents.memory.search.deep_research.models.ResearchSection]) -> str

   Generate an executive summary from research sections.


   .. autolink-examples:: generate_executive_summary
      :collapse:

.. py:function:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

   Get the response model for deep research.


   .. autolink-examples:: get_response_model
      :collapse:

.. py:function:: get_search_instructions() -> str

   Get specific search instructions for deep research.


   .. autolink-examples:: get_search_instructions
      :collapse:

.. py:function:: get_system_prompt() -> str

   Get the system prompt for deep research operations.


   .. autolink-examples:: get_system_prompt
      :collapse:

.. py:function:: organize_findings_by_theme(findings: list[dict[str, Any]]) -> list[haive.agents.memory.search.deep_research.models.ResearchSection]

   Organize research findings into thematic sections.


   .. autolink-examples:: organize_findings_by_theme
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory.search.deep_research.agent
   :collapse:
   
.. autolink-skip:: next
