agents.memory_reorganized.search.deep_research.models
=====================================================

.. py:module:: agents.memory_reorganized.search.deep_research.models

.. autoapi-nested-parse::

   Data models for Deep Research Agent.


   .. autolink-examples:: agents.memory_reorganized.search.deep_research.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.deep_research.models.DeepResearchRequest
   agents.memory_reorganized.search.deep_research.models.DeepResearchResponse
   agents.memory_reorganized.search.deep_research.models.ResearchQuery
   agents.memory_reorganized.search.deep_research.models.ResearchSection
   agents.memory_reorganized.search.deep_research.models.ResearchSource


Module Contents
---------------

.. py:class:: DeepResearchRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Request model for deep research operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DeepResearchRequest
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: focus_areas
      :type:  list[str]
      :value: None



   .. py:attribute:: generate_report
      :type:  bool
      :value: None



   .. py:attribute:: include_fact_checking
      :type:  bool
      :value: None



   .. py:attribute:: max_sources
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: research_depth
      :type:  int
      :value: None



   .. py:attribute:: source_types
      :type:  list[str]
      :value: None



   .. py:attribute:: time_period
      :type:  str | None
      :value: None



.. py:class:: DeepResearchResponse

   Bases: :py:obj:`haive.agents.memory.search.base.SearchResponse`


   Response model for deep research operations.

   Extends the base SearchResponse with deep research specific fields.


   .. autolink-examples:: DeepResearchResponse
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: executive_summary
      :type:  str
      :value: None



   .. py:attribute:: fact_checks
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: high_quality_sources
      :type:  int
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: related_topics
      :type:  list[str]
      :value: None



   .. py:attribute:: research_depth
      :type:  int
      :value: None



   .. py:attribute:: research_queries
      :type:  list[ResearchQuery]
      :value: None



   .. py:attribute:: research_sections
      :type:  list[ResearchSection]
      :value: None



   .. py:attribute:: search_type
      :type:  str
      :value: None



   .. py:attribute:: total_sources_examined
      :type:  int
      :value: None



.. py:class:: ResearchQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for individual research queries performed.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchQuery
      :collapse:

   .. py:attribute:: processing_time
      :type:  float
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: query_type
      :type:  str
      :value: None



   .. py:attribute:: results_found
      :type:  int
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



.. py:class:: ResearchSection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a section of the research report.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchSection
      :collapse:

   .. py:attribute:: confidence_level
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: key_points
      :type:  list[str]
      :value: None



   .. py:attribute:: sources
      :type:  list[ResearchSource]
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



.. py:class:: ResearchSource(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for research source with detailed metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchSource
      :collapse:

   .. py:attribute:: author
      :type:  str | None
      :value: None



   .. py:attribute:: content_snippet
      :type:  str
      :value: None



   .. py:attribute:: credibility_score
      :type:  float
      :value: None



   .. py:attribute:: domain
      :type:  str
      :value: None



   .. py:attribute:: publication_date
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: source_type
      :type:  str
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



   .. py:attribute:: url
      :type:  str
      :value: None



