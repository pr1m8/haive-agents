agents.research.open_perplexity.state
=====================================

.. py:module:: agents.research.open_perplexity.state

.. autoapi-nested-parse::

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

.. py:class:: ReportSection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a section in the research report.

   Tracks a single report section, including its content, research needs,
   and associated queries and sources.

   .. attribute:: name

      Section name

   .. attribute:: description

      Section description

   .. attribute:: content

      Section content

   .. attribute:: requires_research

      Whether this section requires research

   .. attribute:: queries

      Search queries for this section

   .. attribute:: sources

      Sources used in this section

   .. attribute:: status

      Section status (pending, in_progress, completed)

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReportSection
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: queries
      :type:  list[WebSearchQuery]
      :value: None



   .. py:attribute:: requires_research
      :type:  bool
      :value: None



   .. py:attribute:: sources
      :type:  list[dict]
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: None



.. py:class:: ResearchConfidenceLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Confidence level in research findings.

   Represents the overall confidence level in the research results,
   based on source quality, quantity, and consistency.

   .. attribute:: HIGH

      High confidence based on numerous reliable sources

   .. attribute:: MEDIUM

      Medium confidence with good but limited sources

   .. attribute:: LOW

      Low confidence due to limited or questionable sources

   .. attribute:: INSUFFICIENT_DATA

      Not enough data to establish confidence

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchConfidenceLevel
      :collapse:

   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: INSUFFICIENT_DATA
      :value: 'insufficient_data'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



.. py:class:: ResearchInputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input state for the research process.

   Represents the initial input to the research agent, including the
   user's query and any additional context.

   .. attribute:: messages

      Input messages including user query

   .. attribute:: input_context

      Additional context provided for the research

   .. attribute:: research_parameters

      Optional parameters to customize the research process

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchInputState
      :collapse:

   .. py:attribute:: input_context
      :type:  str | None
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: research_parameters
      :type:  dict[str, Any] | None
      :value: None



.. py:class:: ResearchOutputState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output state for the research process.

   Represents the final output from the research agent, including
   the completed report and confidence assessment.

   .. attribute:: final_report

      Complete research report in markdown format

   .. attribute:: confidence_level

      Confidence level in the research findings

   .. attribute:: sources

      Sources used in the research

   .. attribute:: messages

      Conversation history including the assistant's final response

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchOutputState
      :collapse:

   .. py:attribute:: confidence_level
      :type:  ResearchConfidenceLevel
      :value: None



   .. py:attribute:: final_report
      :type:  str
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: sources
      :type:  list[dict[str, Any]]
      :value: None



.. py:class:: ResearchState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State schema for the open_perplexity research agent.

   Comprehensive state object that tracks all aspects of the research process,
   including messages, research parameters, report sections, sources, and findings.

   .. attribute:: messages

      Conversation messages

   .. attribute:: research_topic

      Main topic of research

   .. attribute:: research_question

      Specific research question

   .. attribute:: input_context

      Additional context provided by the user

   .. attribute:: search_parameters

      Parameters for search and research customization

   .. attribute:: report_sections

      Sections of the research report

   .. attribute:: current_section_index

      Index of the current section being researched

   .. attribute:: search_queries

      List of search queries to execute

   .. attribute:: query

      Current search query

   .. attribute:: retrieved_documents

      Documents retrieved from search

   .. attribute:: sources

      Sources used in the research

   .. attribute:: data_sources

      Data sources available and used

   .. attribute:: vectorstore_documents

      Documents loaded into vector store

   .. attribute:: research_findings

      Key findings from the research

   .. attribute:: confidence_level

      Overall confidence level in research findings

   .. attribute:: confidence_explanation

      Explanation for the confidence level assessment

   .. attribute:: final_report

      Final research report content

   .. attribute:: current_step

      Current step in the workflow

   .. attribute:: error

      Error message if any step fails

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchState
      :collapse:

   .. py:attribute:: confidence_explanation
      :type:  str | None
      :value: None



   .. py:attribute:: confidence_level
      :type:  ResearchConfidenceLevel | None
      :value: None



   .. py:attribute:: current_section_index
      :type:  int | None
      :value: None



   .. py:attribute:: current_step
      :type:  str
      :value: None



   .. py:attribute:: data_sources
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: final_report
      :type:  str | None
      :value: None



   .. py:attribute:: input_context
      :type:  str | None
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[collections.abc.Sequence[langchain_core.messages.BaseMessage], langgraph.graph.add_messages]
      :value: None



   .. py:attribute:: query
      :type:  str | None
      :value: None



   .. py:attribute:: report_sections
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: research_findings
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: research_question
      :type:  str | None
      :value: None



   .. py:attribute:: research_topic
      :type:  str | None
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: search_parameters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: search_queries
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: sources
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: vectorstore_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



.. py:class:: WebSearchQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a web search query for retrieving information.

   Tracks a single search query, its purpose, execution status, and results.

   .. attribute:: query

      The search query text

   .. attribute:: purpose

      Purpose of this search query

   .. attribute:: data_source

      Data source to query (web, github, academic, news, etc.)

   .. attribute:: completed

      Whether this query has been executed

   .. attribute:: results

      Search results

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WebSearchQuery
      :collapse:

   .. py:attribute:: completed
      :type:  bool
      :value: None



   .. py:attribute:: data_source
      :type:  str
      :value: None



   .. py:attribute:: purpose
      :type:  str
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: results
      :type:  list[dict]
      :value: None



