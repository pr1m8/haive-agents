agents.research
===============

.. py:module:: agents.research

.. autoapi-nested-parse::

   Research Agents - Advanced research and information gathering agents.

   This module provides specialized agents for conducting research, gathering information,
   and generating comprehensive reports on various topics.

   Available Agents:
       - PersonResearchAgent: Comprehensive person research with multi-source data
       - OpenPerplexityAgent: Web search and research capabilities
       - STORMAgent: Structured research methodology (in development)

   .. rubric:: Example

   Basic research usage::

       from haive.agents.research.person import PersonResearchAgent

       agent = PersonResearchAgent(
           name="researcher",
           research_topic="AI Safety"
       )

       result = await agent.ainvoke({"query": "Recent developments in AI safety"})


   .. autolink-examples:: agents.research
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/research/open_perplexity/index
   /autoapi/agents/research/person/index
   /autoapi/agents/research/storm/index


