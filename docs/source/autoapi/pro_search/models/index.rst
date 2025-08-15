pro_search.models
=================

.. py:module:: pro_search.models

.. autoapi-nested-parse::

   Pydantic models for Perplexity-style quick search workflow.
   from typing import Any
   These models support a multi-stage search process with reasoning, query generation,
   parallel search execution, and synthesis.


   .. autolink-examples:: pro_search.models
      :collapse:


Classes
-------

.. autoapisummary::

   pro_search.models.ContentAnalysis
   pro_search.models.PerplexitySearchState
   pro_search.models.QueryBatch
   pro_search.models.QueryIntent
   pro_search.models.QueryReasoning
   pro_search.models.SearchContext
   pro_search.models.SearchQueryConfig
   pro_search.models.SearchQueryResult
   pro_search.models.SearchResult
   pro_search.models.SearchSynthesis


Module Contents
---------------

.. py:class:: ContentAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of search results content.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContentAnalysis
      :collapse:

   .. py:method:: adjust_confidence_by_contradictions() -> ContentAnalysis

      Adjust confidence based on contradictions.


      .. autolink-examples:: adjust_confidence_by_contradictions
         :collapse:


   .. py:attribute:: common_themes
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence_level
      :type:  Literal['high', 'medium', 'low']
      :value: None



   .. py:attribute:: contradictions
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: gaps_identified
      :type:  list[str]
      :value: None



   .. py:attribute:: key_findings
      :type:  list[str]
      :value: None



.. py:class:: PerplexitySearchState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete state for Perplexity-style search workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PerplexitySearchState
      :collapse:

   .. py:attribute:: context
      :type:  SearchContext
      :value: None



   .. py:property:: is_complete
      :type: bool


      Check if search workflow is complete.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:property:: next_action
      :type: Literal['reason', 'generate_queries', 'search', 'synthesize', 'complete']


      Determine next action in workflow.

      .. autolink-examples:: next_action
         :collapse:


   .. py:attribute:: query_batch
      :type:  QueryBatch | None
      :value: None



   .. py:attribute:: reasoning
      :type:  QueryReasoning | None
      :value: None



   .. py:attribute:: search_results
      :type:  list[SearchQueryResult]
      :value: None



   .. py:attribute:: synthesis
      :type:  SearchSynthesis | None
      :value: None



   .. py:attribute:: user_query
      :type:  str
      :value: None



.. py:class:: QueryBatch(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Batch of queries to execute in parallel.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryBatch
      :collapse:

   .. py:method:: validate_query_diversity() -> QueryBatch

      Ensure queries are diverse and non-redundant.


      .. autolink-examples:: validate_query_diversity
         :collapse:


   .. py:attribute:: execution_strategy
      :type:  Literal['parallel', 'sequential', 'priority']
      :value: None



   .. py:property:: primary_queries
      :type: list[SearchQueryConfig]


      Get primary queries only.

      .. autolink-examples:: primary_queries
         :collapse:


   .. py:attribute:: queries
      :type:  list[SearchQueryConfig]
      :value: None



   .. py:attribute:: reasoning
      :type:  QueryReasoning
      :value: None



   .. py:property:: total_expected_results
      :type: int


      Calculate total expected results based on queries.

      .. autolink-examples:: total_expected_results
         :collapse:


.. py:class:: QueryIntent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analyzed intent and characteristics of a search query.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryIntent
      :collapse:

   .. py:method:: adjust_sources_by_complexity(v, info) -> Any
      :classmethod:


      Adjust required sources based on complexity.


      .. autolink-examples:: adjust_sources_by_complexity
         :collapse:


   .. py:attribute:: complexity_level
      :type:  Literal['simple', 'moderate', 'complex']
      :value: None



   .. py:attribute:: intent_type
      :type:  Literal['factual', 'comparison', 'how-to', 'definition', 'current_events', 'analysis', 'recommendation', 'navigation']
      :value: None



   .. py:attribute:: key_entities
      :type:  list[str]
      :value: None



   .. py:attribute:: related_concepts
      :type:  list[str]
      :value: None



   .. py:attribute:: required_sources
      :type:  int
      :value: None



   .. py:attribute:: temporal_scope
      :type:  Literal['historical', 'current', 'future', 'timeless']
      :value: None



.. py:class:: QueryReasoning(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Reasoning output for query understanding and expansion.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryReasoning
      :collapse:

   .. py:method:: validate_reasoning_completeness() -> QueryReasoning

      Ensure reasoning provides actionable insights.


      .. autolink-examples:: validate_reasoning_completeness
         :collapse:


   .. py:attribute:: expansion_rationale
      :type:  str
      :value: None



   .. py:attribute:: intent_analysis
      :type:  QueryIntent
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: potential_challenges
      :type:  list[str]
      :value: None



   .. py:attribute:: search_strategy
      :type:  str
      :value: None



   .. py:attribute:: understanding
      :type:  str
      :value: None



.. py:class:: SearchContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Context information for search query understanding.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchContext
      :collapse:

   .. py:method:: _get_relative_time() -> str

      Get relative time context (morning, afternoon, etc.).


      .. autolink-examples:: _get_relative_time
         :collapse:


   .. py:attribute:: current_date
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: domain_preferences
      :type:  set[str]
      :value: None



   .. py:attribute:: search_history
      :type:  list[str]
      :value: None



   .. py:property:: temporal_context
      :type: dict[str, str]


      Generate temporal context strings.

      .. autolink-examples:: temporal_context
         :collapse:


   .. py:attribute:: user_location
      :type:  str | None
      :value: None



.. py:class:: SearchQueryConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for individual search queries.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchQueryConfig
      :collapse:

   .. py:method:: clean_query_text(v) -> Any
      :classmethod:


      Clean and validate query text.


      .. autolink-examples:: clean_query_text
         :collapse:


   .. py:attribute:: expected_result_type
      :type:  Literal['facts', 'list', 'explanation', 'comparison', 'tutorial', 'mixed']
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: query_text
      :type:  str
      :value: None



   .. py:attribute:: query_type
      :type:  Literal['primary', 'supporting', 'verification', 'expansion']
      :value: None



   .. py:attribute:: target_source_types
      :type:  list[Literal['web', 'academic', 'news', 'wiki', 'social', 'video', 'image']]
      :value: None



.. py:class:: SearchQueryResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Results for a single search query.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchQueryResult
      :collapse:

   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time_ms
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  SearchQueryConfig
      :value: None



   .. py:attribute:: results
      :type:  list[SearchResult]
      :value: None



   .. py:property:: success
      :type: bool


      Check if query executed successfully.

      .. autolink-examples:: success
         :collapse:


   .. py:property:: top_results
      :type: list[SearchResult]


      Get top 3 results by relevance.

      .. autolink-examples:: top_results
         :collapse:


.. py:class:: SearchResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual search result with metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchResult
      :collapse:

   .. py:property:: age_days
      :type: int | None


      Calculate age of content in days.

      .. autolink-examples:: age_days
         :collapse:


   .. py:property:: is_recent
      :type: bool


      Check if content is recent (< 30 days).

      .. autolink-examples:: is_recent
         :collapse:


   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: publish_date
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: snippet
      :type:  str
      :value: None



   .. py:attribute:: source_type
      :type:  Literal['web', 'academic', 'news', 'wiki', 'social', 'video', 'image']
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



   .. py:attribute:: url
      :type:  str
      :value: None



.. py:class:: SearchSynthesis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final synthesis of search results.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchSynthesis
      :collapse:

   .. py:method:: ensure_citations() -> SearchSynthesis

      Ensure citations are provided for summary.


      .. autolink-examples:: ensure_citations
         :collapse:


   .. py:attribute:: analysis
      :type:  ContentAnalysis
      :value: None



   .. py:attribute:: answer_completeness
      :type:  float
      :value: None



   .. py:attribute:: citations
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: follow_up_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: query_batch
      :type:  QueryBatch
      :value: None



   .. py:property:: requires_follow_up
      :type: bool


      Determine if follow-up search is needed.

      .. autolink-examples:: requires_follow_up
         :collapse:


   .. py:attribute:: search_results
      :type:  list[SearchQueryResult]
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



   .. py:property:: total_sources_used
      :type: int


      Count total unique sources used.

      .. autolink-examples:: total_sources_used
         :collapse:


