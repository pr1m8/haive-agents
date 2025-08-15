agents.research.open_perplexity.models
======================================

.. py:module:: agents.research.open_perplexity.models

.. autoapi-nested-parse::

   Models for the open_perplexity research agent.

   from typing import Any
   This module defines data models used for representing, tracking, and evaluating
   research sources, findings, and summaries. It includes enumerations for categorizing
   data source types, content reliability, freshness, and research depth.


   .. autolink-examples:: agents.research.open_perplexity.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.research.open_perplexity.models.ContentFreshness
   agents.research.open_perplexity.models.ContentReliability
   agents.research.open_perplexity.models.DataSourceConfig
   agents.research.open_perplexity.models.DataSourceType
   agents.research.open_perplexity.models.ResearchDepth
   agents.research.open_perplexity.models.ResearchFinding
   agents.research.open_perplexity.models.ResearchSource
   agents.research.open_perplexity.models.ResearchSummary


Module Contents
---------------

.. py:class:: ContentFreshness

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of content freshness levels.

   Categorizes how recent or up-to-date the information content is.

   .. attribute:: VERY_RECENT

      Content from the last few days

   .. attribute:: RECENT

      Content from the last few weeks

   .. attribute:: SOMEWHAT_RECENT

      Content from the last few months

   .. attribute:: OUTDATED

      Content from years ago

   .. attribute:: UNKNOWN

      Content with unknown or unclear publication date

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContentFreshness
      :collapse:

   .. py:attribute:: OUTDATED
      :value: 'outdated'



   .. py:attribute:: RECENT
      :value: 'recent'



   .. py:attribute:: SOMEWHAT_RECENT
      :value: 'somewhat_recent'



   .. py:attribute:: UNKNOWN
      :value: 'unknown'



   .. py:attribute:: VERY_RECENT
      :value: 'very_recent'



.. py:class:: ContentReliability

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of content reliability levels.

   Categorizes the trustworthiness and reliability of information sources.

   .. attribute:: HIGH

      Highly reliable sources (peer-reviewed, authoritative)

   .. attribute:: MEDIUM

      Moderately reliable sources (reputable but not authoritative)

   .. attribute:: LOW

      Low reliability sources (potentially biased or unverified)

   .. attribute:: UNKNOWN

      Sources with unknown or unclear reliability

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContentReliability
      :collapse:

   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: UNKNOWN
      :value: 'unknown'



.. py:class:: DataSourceConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for a data source.

   Specifies parameters for interacting with a particular data source,
   including API keys and search parameters.

   .. attribute:: name

      Name of the data source

   .. attribute:: source_type

      Type of data source

   .. attribute:: enabled

      Whether this source is enabled

   .. attribute:: priority

      Priority (1-10, higher = more important)

   .. attribute:: api_key

      API key for the data source if required

   .. attribute:: max_results

      Maximum number of results to return

   .. attribute:: search_params

      Custom search parameters

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DataSourceConfig
      :collapse:

   .. py:method:: validate_priority(v) -> Any
      :classmethod:


      Ensure priority is between 1 and 10.

      :param v: The priority value to validate

      :returns: The validated priority value, clamped between 1 and 10
      :rtype: int


      .. autolink-examples:: validate_priority
         :collapse:


   .. py:attribute:: api_key
      :type:  str | None
      :value: None



   .. py:attribute:: enabled
      :type:  bool
      :value: None



   .. py:attribute:: max_results
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: search_params
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source_type
      :type:  DataSourceType
      :value: None



.. py:class:: DataSourceType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of data source types.

   Categorizes the different types of sources where research information can be found.

   .. attribute:: WEB

      General web content

   .. attribute:: GITHUB

      Code repositories and issues from GitHub

   .. attribute:: ACADEMIC

      Academic papers and research publications

   .. attribute:: NEWS

      News articles and press releases

   .. attribute:: SOCIAL_MEDIA

      Content from social media platforms

   .. attribute:: DOCUMENTS

      Uploaded or local documents

   .. attribute:: API

      Data retrieved from APIs

   .. attribute:: OTHER

      Any other source type not covered above

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DataSourceType
      :collapse:

   .. py:attribute:: ACADEMIC
      :value: 'academic'



   .. py:attribute:: API
      :value: 'api'



   .. py:attribute:: DOCUMENTS
      :value: 'documents'



   .. py:attribute:: GITHUB
      :value: 'github'



   .. py:attribute:: NEWS
      :value: 'news'



   .. py:attribute:: OTHER
      :value: 'other'



   .. py:attribute:: SOCIAL_MEDIA
      :value: 'social_media'



   .. py:attribute:: WEB
      :value: 'web'



.. py:class:: ResearchDepth

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of research depth levels.

   Categorizes the comprehensiveness and thoroughness of the research.

   .. attribute:: SUPERFICIAL

      Basic overview with minimal sources

   .. attribute:: INTERMEDIATE

      Moderate depth with several sources

   .. attribute:: DEEP

      In-depth research with many high-quality sources

   .. attribute:: COMPREHENSIVE

      Exhaustive research with extensive sources

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchDepth
      :collapse:

   .. py:attribute:: COMPREHENSIVE
      :value: 'comprehensive'



   .. py:attribute:: DEEP
      :value: 'deep'



   .. py:attribute:: INTERMEDIATE
      :value: 'intermediate'



   .. py:attribute:: SUPERFICIAL
      :value: 'superficial'



.. py:class:: ResearchFinding(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a specific research finding.

   Represents an individual insight or finding from the research,
   including supporting sources and confidence assessment.

   .. attribute:: finding

      The actual finding or insight

   .. attribute:: confidence

      Confidence level in this finding (0.0 - 1.0)

   .. attribute:: sources

      Sources supporting this finding

   .. attribute:: explanation

      Explanation of the finding's significance

   .. attribute:: related_findings

      Related findings

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchFinding
      :collapse:

   .. py:method:: validate_confidence(v) -> Any
      :classmethod:


      Ensure confidence is between 0 and 1.

      :param v: The confidence value to validate

      :returns: The validated confidence value, clamped between 0.0 and 1.0
      :rtype: float


      .. autolink-examples:: validate_confidence
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: explanation
      :type:  str | None
      :value: None



   .. py:attribute:: finding
      :type:  str
      :value: None



   .. py:attribute:: related_findings
      :type:  list[str]
      :value: None



   .. py:attribute:: sources
      :type:  list[ResearchSource]
      :value: None



.. py:class:: ResearchSource(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for tracking and evaluating research sources.

   Represents a source of information used in research, including metadata
   about its reliability, relevance, and content.

   .. attribute:: url

      URL of the source

   .. attribute:: title

      Title of the source

   .. attribute:: source_type

      Type of data source

   .. attribute:: content_snippet

      Snippet of relevant content

   .. attribute:: reliability

      Assessed reliability of the source

   .. attribute:: freshness

      Content freshness/recency

   .. attribute:: relevance_score

      Relevance score from 0.0 to 1.0

   .. attribute:: citation

      Formatted citation for the source

   .. attribute:: access_timestamp

      When the source was accessed

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchSource
      :collapse:

   .. py:method:: validate_relevance_score(v) -> Any
      :classmethod:


      Ensure relevance score is between 0 and 1.

      :param v: The relevance score to validate

      :returns: The validated relevance score, clamped between 0.0 and 1.0
      :rtype: float


      .. autolink-examples:: validate_relevance_score
         :collapse:


   .. py:attribute:: access_timestamp
      :type:  str | None
      :value: None



   .. py:attribute:: citation
      :type:  str | None
      :value: None



   .. py:attribute:: content_snippet
      :type:  str | None
      :value: None



   .. py:attribute:: freshness
      :type:  ContentFreshness
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: reliability
      :type:  ContentReliability
      :value: None



   .. py:attribute:: source_type
      :type:  DataSourceType
      :value: None



   .. py:attribute:: title
      :type:  str | None
      :value: None



   .. py:attribute:: url
      :type:  str | None
      :value: None



.. py:class:: ResearchSummary(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Summary of research findings and assessment.

   Provides an overall summary of the research, including key findings,
   assessment of source quality, and confidence evaluation.

   .. attribute:: topic

      Research topic

   .. attribute:: question

      Specific research question

   .. attribute:: key_findings

      Key findings from research

   .. attribute:: sources_count

      Total number of sources consulted

   .. attribute:: high_reliability_sources

      Number of high reliability sources

   .. attribute:: recent_sources

      Number of recent sources

   .. attribute:: research_depth

      Overall research depth

   .. attribute:: contradictions

      Contradictory findings identified

   .. attribute:: confidence_score

      Overall confidence score

   .. attribute:: limitations

      Research limitations

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchSummary
      :collapse:

   .. py:method:: assess_depth() -> ResearchDepth

      Assess research depth based on source counts and diversity.

      Evaluates the depth of research based on the number of sources
      and the proportion of high reliability sources.

      :returns: The assessed research depth level
      :rtype: ResearchDepth


      .. autolink-examples:: assess_depth
         :collapse:


   .. py:method:: validate_confidence_score(v) -> Any
      :classmethod:


      Ensure confidence score is between 0 and 1.

      :param v: The confidence score to validate

      :returns: The validated confidence score, clamped between 0.0 and 1.0
      :rtype: float


      .. autolink-examples:: validate_confidence_score
         :collapse:


   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: contradictions
      :type:  list[str]
      :value: None



   .. py:attribute:: high_reliability_sources
      :type:  int
      :value: None



   .. py:attribute:: key_findings
      :type:  list[ResearchFinding]
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: question
      :type:  str | None
      :value: None



   .. py:attribute:: recent_sources
      :type:  int
      :value: None



   .. py:attribute:: research_depth
      :type:  ResearchDepth
      :value: None



   .. py:attribute:: sources_count
      :type:  int
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



