agents.structured_output.models
===============================

.. py:module:: agents.structured_output.models

.. autoapi-nested-parse::

   Common structured output models for various agent patterns.


   .. autolink-examples:: agents.structured_output.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.structured_output.models.Analysis
   agents.structured_output.models.Critique
   agents.structured_output.models.Decision
   agents.structured_output.models.ExtractedData
   agents.structured_output.models.Improvement
   agents.structured_output.models.Intent
   agents.structured_output.models.QualityCheck
   agents.structured_output.models.ReflectionResult
   agents.structured_output.models.Response
   agents.structured_output.models.SearchQuery
   agents.structured_output.models.SearchResult
   agents.structured_output.models.Summary
   agents.structured_output.models.TaskResult
   agents.structured_output.models.ValidationResult


Module Contents
---------------

.. py:class:: Analysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured analysis result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Analysis
      :collapse:

   .. py:attribute:: conclusions
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence_level
      :type:  str
      :value: None



   .. py:attribute:: data_points
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: insights
      :type:  list[str]
      :value: None



   .. py:attribute:: key_points
      :type:  list[str]
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



.. py:class:: Critique(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured critique of an output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Critique
      :collapse:

   .. py:attribute:: needs_revision
      :type:  bool
      :value: None



   .. py:attribute:: overall_quality
      :type:  float
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



   .. py:attribute:: suggestions
      :type:  list[str]
      :value: None



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: None



.. py:class:: Decision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured decision output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Decision
      :collapse:

   .. py:attribute:: alternatives
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: decision
      :type:  str
      :value: None



   .. py:attribute:: next_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: risks
      :type:  list[str]
      :value: None



.. py:class:: ExtractedData(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Extracted structured data.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExtractedData
      :collapse:

   .. py:attribute:: entities
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: facts
      :type:  list[str]
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: relationships
      :type:  list[dict[str, str]]
      :value: None



   .. py:attribute:: source_text
      :type:  str | None
      :value: None



.. py:class:: Improvement(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured improvement suggestions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Improvement
      :collapse:

   .. py:attribute:: expected_impact
      :type:  str
      :value: None



   .. py:attribute:: implementation_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: original_issue
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  str
      :value: None



   .. py:attribute:: proposed_solution
      :type:  str
      :value: None



.. py:class:: Intent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   User intent classification.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Intent
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: entities
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: primary_intent
      :type:  str
      :value: None



   .. py:attribute:: secondary_intents
      :type:  list[str]
      :value: None



   .. py:attribute:: suggested_action
      :type:  str
      :value: None



.. py:class:: QualityCheck(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Quality assessment result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QualityCheck
      :collapse:

   .. py:attribute:: accuracy
      :type:  float
      :value: None



   .. py:attribute:: clarity
      :type:  float
      :value: None



   .. py:attribute:: completeness
      :type:  float
      :value: None



   .. py:attribute:: feedback
      :type:  str
      :value: None



   .. py:attribute:: meets_requirements
      :type:  bool
      :value: None



   .. py:attribute:: overall_quality
      :type:  float
      :value: None



   .. py:attribute:: relevance
      :type:  float
      :value: None



.. py:class:: ReflectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete reflection analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionResult
      :collapse:

   .. py:attribute:: action_items
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: critique
      :type:  Critique
      :value: None



   .. py:attribute:: improvements
      :type:  list[Improvement]
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:class:: Response(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Response
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: follow_up
      :type:  str | None
      :value: None



   .. py:attribute:: sources
      :type:  list[str]
      :value: None



   .. py:attribute:: type
      :type:  str
      :value: None



.. py:class:: SearchQuery(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured search query.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchQuery
      :collapse:

   .. py:attribute:: filters
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: include_fields
      :type:  list[str]
      :value: None



   .. py:attribute:: limit
      :type:  int
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: sort_by
      :type:  str | None
      :value: None



.. py:class:: SearchResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured search result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchResult
      :collapse:

   .. py:attribute:: facets
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: next_page_token
      :type:  str | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: results
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: total_results
      :type:  int
      :value: None



.. py:class:: Summary(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured summary.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Summary
      :collapse:

   .. py:attribute:: action_items
      :type:  list[str]
      :value: None



   .. py:attribute:: details
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: executive_summary
      :type:  str
      :value: None



   .. py:attribute:: main_points
      :type:  list[str]
      :value: None



   .. py:attribute:: title
      :type:  str
      :value: None



   .. py:attribute:: word_count
      :type:  int
      :value: None



.. py:class:: TaskResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of task execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskResult
      :collapse:

   .. py:attribute:: duration_ms
      :type:  int | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: result
      :type:  Any
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: None



   .. py:attribute:: task_id
      :type:  str
      :value: None



.. py:class:: ValidationResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of validation check.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ValidationResult
      :collapse:

   .. py:attribute:: details
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: errors
      :type:  list[str]
      :value: None



   .. py:attribute:: is_valid
      :type:  bool
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



   .. py:attribute:: warnings
      :type:  list[str]
      :value: None



