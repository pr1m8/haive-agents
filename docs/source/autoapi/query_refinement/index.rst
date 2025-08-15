query_refinement
================

.. py:module:: query_refinement

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: query_refinement
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/query_refinement/models/index
   /autoapi/query_refinement/prompt/index


Classes
-------

.. autoapisummary::

   query_refinement.QueryRefinementResponse
   query_refinement.QueryRefinementSuggestion


Package Contents
----------------

.. py:class:: QueryRefinementResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Query refinement analysis and suggestions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryRefinementResponse
      :collapse:

   .. py:attribute:: best_refined_query
      :type:  str
      :value: None



   .. py:attribute:: complexity_level
      :type:  str
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: query_analysis
      :type:  str
      :value: None



   .. py:attribute:: query_type
      :type:  str
      :value: None



   .. py:attribute:: refinement_suggestions
      :type:  list[QueryRefinementSuggestion]
      :value: None



   .. py:attribute:: search_strategy_recommendations
      :type:  list[str]
      :value: None



.. py:class:: QueryRefinementSuggestion(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual query refinement suggestion.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryRefinementSuggestion
      :collapse:

   .. py:attribute:: expected_benefit
      :type:  str
      :value: None



   .. py:attribute:: improvement_type
      :type:  str
      :value: None



   .. py:attribute:: rationale
      :type:  str
      :value: None



   .. py:attribute:: refined_query
      :type:  str
      :value: None



