agents.memory.search.quick_search.models
========================================

.. py:module:: agents.memory.search.quick_search.models

.. autoapi-nested-parse::

   Data models for Quick Search Agent.


   .. autolink-examples:: agents.memory.search.quick_search.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.memory.search.quick_search.models.Config
   agents.memory.search.quick_search.models.QuickSearchRequest
   agents.memory.search.quick_search.models.QuickSearchResponse


Module Contents
---------------

.. py:class:: Config(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for Quick Search Agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Config
      :collapse:

   .. py:attribute:: fast_mode
      :type:  bool
      :value: None



   .. py:attribute:: include_snippets
      :type:  bool
      :value: None



   .. py:attribute:: max_results
      :type:  int
      :value: None



.. py:class:: QuickSearchRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Request model for quick search operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QuickSearchRequest
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: include_sources
      :type:  bool
      :value: None



   .. py:attribute:: max_response_length
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



.. py:class:: QuickSearchResponse

   Bases: :py:obj:`haive.agents.memory.search.base.SearchResponse`


   Response model for quick search operations.

   Extends the base SearchResponse with quick search specific fields.


   .. autolink-examples:: QuickSearchResponse
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: json_schema_extra



   .. py:attribute:: answer_type
      :type:  str
      :value: None



   .. py:attribute:: keywords
      :type:  list[str]
      :value: None



   .. py:attribute:: search_type
      :type:  str
      :value: None



