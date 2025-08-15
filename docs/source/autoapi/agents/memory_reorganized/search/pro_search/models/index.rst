agents.memory_reorganized.search.pro_search.models
==================================================

.. py:module:: agents.memory_reorganized.search.pro_search.models

.. autoapi-nested-parse::

   Data models for Pro Search Agent.


   .. autolink-examples:: agents.memory_reorganized.search.pro_search.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.pro_search.models.ContextualInsight
   agents.memory_reorganized.search.pro_search.models.ProSearchRequest
   agents.memory_reorganized.search.pro_search.models.ProSearchResponse
   agents.memory_reorganized.search.pro_search.models.SearchRefinement


Module Contents
---------------

.. py:class:: ContextualInsight(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for contextual insights from search.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextualInsight
      :collapse:

   .. py:attribute:: insight
      :type:  str
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: source_type
      :type:  str
      :value: None



.. py:class:: ProSearchRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Request model for pro search operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ProSearchRequest
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: context
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: depth_level
      :type:  int
      :value: None



   .. py:attribute:: generate_follow_ups
      :type:  bool
      :value: None



   .. py:attribute:: include_reasoning
      :type:  bool
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: use_preferences
      :type:  bool
      :value: None



.. py:class:: ProSearchResponse

   Bases: :py:obj:`haive.agents.memory.search.base.SearchResponse`


   Response model for pro search operations.

   Extends the base SearchResponse with pro search specific fields.


   .. autolink-examples:: ProSearchResponse
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: contextual_insights
      :type:  list[ContextualInsight]
      :value: None



   .. py:attribute:: depth_level
      :type:  int
      :value: None



   .. py:attribute:: follow_up_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: refinements
      :type:  list[SearchRefinement]
      :value: None



   .. py:attribute:: search_type
      :type:  str
      :value: None



   .. py:attribute:: user_preferences_applied
      :type:  dict[str, Any]
      :value: None



.. py:class:: SearchRefinement(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for search query refinements.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchRefinement
      :collapse:

   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: refined_query
      :type:  str
      :value: None



   .. py:attribute:: refinement_reason
      :type:  str
      :value: None



