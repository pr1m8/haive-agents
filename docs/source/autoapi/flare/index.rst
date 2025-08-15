flare
=====

.. py:module:: flare

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: flare
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/flare/models/index
   /autoapi/flare/prompt/index


Classes
-------

.. autoapisummary::

   flare.FLAREResponse
   flare.FLAREStep


Package Contents
----------------

.. py:class:: FLAREResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   FLARE (Forward-Looking Active Retrieval) response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FLAREResponse
      :collapse:

   .. py:attribute:: confidence_assessment
      :type:  str
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: generation_steps
      :type:  list[FLAREStep]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: remaining_uncertainties
      :type:  list[str]
      :value: None



   .. py:attribute:: retrieval_requests
      :type:  list[str]
      :value: None



.. py:class:: FLAREStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in FLARE generation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FLAREStep
      :collapse:

   .. py:attribute:: confidence_level
      :type:  str
      :value: None



   .. py:attribute:: generated_content
      :type:  str
      :value: None



   .. py:attribute:: information_needs
      :type:  list[str]
      :value: None



   .. py:attribute:: search_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



   .. py:attribute:: uncertainties
      :type:  list[str]
      :value: None



