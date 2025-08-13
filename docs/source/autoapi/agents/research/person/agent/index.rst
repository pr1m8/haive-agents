
:py:mod:`agents.research.person.agent`
======================================

.. py:module:: agents.research.person.agent

Person research agent for comprehensive person information gathering.

This module implements a sophisticated person research agent that combines web search,
structured extraction, and iterative refinement to gather comprehensive information
about individuals. The agent is particularly useful for research tasks requiring
detailed personal profiles, biographical information, or professional backgrounds.

The agent workflow includes:
1. Query generation based on the target person and desired information schema
2. Web search execution using multiple search engines (Tavily integration)
3. Information extraction and note-taking from search results
4. Structured data extraction according to user-defined schemas
5. Reflection and completeness assessment
6. Iterative refinement until information quality meets requirements

Key Features:
- Configurable extraction schemas for different research needs
- Multi-source web search with relevance ranking
- Iterative research process with reflection and self-correction
- Structured output generation with validation
- Source attribution and credibility assessment
- Rate limiting and API quota management

Usage:
    .. code-block:: python

        from haive.agents.research.person import PersonResearchAgent, PersonResearchAgentConfig

        # Configure the agent
        config = PersonResearchAgentConfig(
        name="person_researcher",
        target_person="Dr. Jane Smith",
        extraction_schema={
        "name": "Full name",
        "profession": "Current profession or role",
        "education": "Educational background",
        "achievements": "Notable achievements or awards"
        }
        )

        # Create and run the agent
        agent = PersonResearchAgent(config)
        result = await agent.ainvoke({
        "person": "Dr. Jane Smith, AI researcher",
        "research_depth": "comprehensive"
        })

        print(result.extracted_info)


The agent integrates with external services (Tavily) for web search and requires
appropriate API keys to function fully. It includes comprehensive error handling
and graceful degradation when external services are unavailable.


.. autolink-examples:: agents.research.person.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.research.person.agent.PersonResearchAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PersonResearchAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PersonResearchAgent {
        node [shape=record];
        "PersonResearchAgent" [label="PersonResearchAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.research.person.config.PersonResearchAgentConfig]" -> "PersonResearchAgent";
      }

.. autoclass:: agents.research.person.agent.PersonResearchAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.research.person.agent
   :collapse:
   
.. autolink-skip:: next
