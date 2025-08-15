document_graders.models
=======================

.. py:module:: document_graders.models

.. autoapi-nested-parse::

   RAG Structured Output Models.

   Pydantic models for structured outputs from RAG evaluation agents.


   .. autolink-examples:: document_graders.models
      :collapse:


Classes
-------

.. autoapisummary::

   document_graders.models.DocumentBinaryGrading
   document_graders.models.DocumentBinaryResponse
   document_graders.models.DocumentGradingResponse
   document_graders.models.DocumentRelevanceScore


Module Contents
---------------

.. py:class:: DocumentBinaryGrading(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Binary pass/fail document grading.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentBinaryGrading
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: decision
      :type:  Literal['pass', 'fail']


   .. py:attribute:: document_id
      :type:  str
      :value: None



   .. py:attribute:: justification
      :type:  str
      :value: None



.. py:class:: DocumentBinaryResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response for binary document grading.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentBinaryResponse
      :collapse:

   .. py:attribute:: document_decisions
      :type:  list[DocumentBinaryGrading]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:class:: DocumentGradingResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive document grading response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentGradingResponse
      :collapse:

   .. py:attribute:: coverage_analysis
      :type:  str
      :value: None



   .. py:attribute:: document_scores
      :type:  list[DocumentRelevanceScore]
      :value: None



   .. py:attribute:: overall_assessment
      :type:  str
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



.. py:class:: DocumentRelevanceScore(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual document relevance assessment.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentRelevanceScore
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: document_id
      :type:  str
      :value: None



   .. py:attribute:: document_title
      :type:  str | None
      :value: None



   .. py:attribute:: justification
      :type:  str
      :value: None



   .. py:attribute:: key_information
      :type:  list[str]
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



