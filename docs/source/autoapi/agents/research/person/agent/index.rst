agents.research.person.agent
============================

.. py:module:: agents.research.person.agent

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   agents.research.person.agent.TAVILY_AVAILABLE
   agents.research.person.agent.logger


Classes
-------

.. autoapisummary::

   agents.research.person.agent.PersonResearchAgent


Module Contents
---------------

.. py:class:: PersonResearchAgent(config: haive.agents.research.person.config.PersonResearchAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.research.person.config.PersonResearchAgentConfig`\ ]


   Advanced person research agent with iterative information gathering capabilities.

   This agent implements a sophisticated research workflow that systematically
   gathers, processes, and structures information about individuals using web
   search, content extraction, and iterative refinement techniques.

   The agent follows a multi-stage research process:
   1. Query Generation: Creates targeted search queries based on the person
      and desired information schema
   2. Web Search: Executes searches using the Tavily API for high-quality results
   3. Content Extraction: Processes search results and extracts relevant notes
   4. Structured Extraction: Converts notes into structured data following
      user-defined schemas
   5. Reflection: Evaluates information completeness and quality
   6. Iteration: Repeats the process with refined queries until satisfactory
      results are achieved or maximum iterations are reached

   The agent is designed to be highly configurable and can adapt to different
   research requirements by modifying the extraction schema, search parameters,
   and quality thresholds.

   .. attribute:: tavily_client

      Optional Tavily API client for web searches.

   .. attribute:: state_schema

      Pydantic model defining the agent's internal state.

   .. attribute:: input_schema

      Pydantic model defining expected input format.

   .. attribute:: output_schema

      Pydantic model defining output format.

   .. rubric:: Example

   >>> config = PersonResearchAgentConfig(
   ...     name="researcher",
   ...     extraction_schema={"name": "Full name", "role": "Current position"}
   ... )
   >>> agent = PersonResearchAgent(config)
   >>> result = await agent.ainvoke({"person": "John Doe"})

   Initialize the person research agent with configuration and external services.

   Sets up the agent with the provided configuration, initializes the Tavily
   web search client if available, and prepares the agent for research operations.

   :param config: Configuration object containing agent settings, API keys,
                  extraction schemas, and operational parameters.

   :raises ValueError: If required configuration parameters are missing.
   :raises ConnectionError: If external service initialization fails.

   .. note::

      The Tavily client is optional - the agent will log a warning and
      continue with limited functionality if the API key is not available.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PersonResearchAgent
      :collapse:

   .. py:method:: _extract_json_from_text(text: str) -> str | None

      Extract a JSON object from text.

      :param text: Text to extract JSON from

      :returns: JSON string or None if not found


      .. autolink-examples:: _extract_json_from_text
         :collapse:


   .. py:method:: gather_notes_extract_schema(state: haive.agents.research.person.state.PersonResearchState) -> dict[str, Any]

      Gather notes from the web search and extract the schema fields.

      :param state: Current state

      :returns: Dict with info field


      .. autolink-examples:: gather_notes_extract_schema
         :collapse:


   .. py:method:: generate_queries(state: haive.agents.research.person.state.PersonResearchState, config: langchain_core.runnables.RunnableConfig) -> dict[str, Any]

      Generate search queries based on the user input and extraction schema.

      :param state: Current state
      :param config: Runnable configuration

      :returns: Dict with search_queries field


      .. autolink-examples:: generate_queries
         :collapse:


   .. py:method:: reflection(state: haive.agents.research.person.state.PersonResearchState) -> dict[str, Any]

      Reflect on the extracted information and generate search queries to find missing information.

      :param state: Current state

      :returns: Dict with is_satisfactory field and optionally search_queries


      .. autolink-examples:: reflection
         :collapse:


   .. py:method:: research_person(state: haive.agents.research.person.state.PersonResearchState, config: langchain_core.runnables.RunnableConfig) -> dict[str, Any]
      :async:


      Execute a multi-step web search and information extraction process.

      :param state: Current state
      :param config: Runnable configuration

      :returns: Dict with completed_notes field


      .. autolink-examples:: research_person
         :collapse:


   .. py:method:: route_from_reflection(state: haive.agents.research.person.state.PersonResearchState, config: langchain_core.runnables.RunnableConfig) -> Literal[langgraph.graph.END, 'research_person']

      Route the graph based on the reflection output.

      :param state: Current state
      :param config: Runnable configuration

      :returns: Next node to route to


      .. autolink-examples:: route_from_reflection
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the workflow graph for this agent.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: tavily_client
      :value: None



.. py:data:: TAVILY_AVAILABLE
   :value: True


.. py:data:: logger

