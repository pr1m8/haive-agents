agents.reflection.models
========================

.. py:module:: agents.reflection.models

.. autoapi-nested-parse::

   Models for reflection agent outputs and configurations.


   .. autolink-examples:: agents.reflection.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.reflection.models.Critique
   agents.reflection.models.ExpertiseConfig
   agents.reflection.models.GradingResult
   agents.reflection.models.Improvement
   agents.reflection.models.ImprovementSuggestion
   agents.reflection.models.QualityScore
   agents.reflection.models.ReflectionConfig
   agents.reflection.models.ReflectionOutput
   agents.reflection.models.ReflectionResult


Functions
---------

.. autoapisummary::

   agents.reflection.models.to_prompt
   agents.reflection.models.validate_grade_matches_score


Module Contents
---------------

.. py:class:: Critique(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured critique of an output (for structured output pattern).

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



.. py:class:: ExpertiseConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for expert agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExpertiseConfig
      :collapse:

   .. py:method:: to_prompt() -> str

      Convert to prompt string.


      .. autolink-examples:: to_prompt
         :collapse:


   .. py:attribute:: additional_context
      :type:  str | None
      :value: None



   .. py:attribute:: domain
      :type:  str
      :value: None



   .. py:attribute:: expertise_level
      :type:  Literal['beginner', 'intermediate', 'expert', 'world-class']
      :value: None



   .. py:attribute:: style
      :type:  str | None
      :value: None



.. py:class:: GradingResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive grading result for a response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GradingResult
      :collapse:

   .. py:method:: _score_to_grade(score: float) -> str
      :staticmethod:


      Convert numerical score to letter grade.


      .. autolink-examples:: _score_to_grade
         :collapse:


   .. py:method:: validate_grade_matches_score(v) -> Any
      :classmethod:


      Ensure letter grade matches overall score.


      .. autolink-examples:: validate_grade_matches_score
         :collapse:


   .. py:attribute:: accuracy_score
      :type:  float
      :value: None



   .. py:attribute:: clarity_score
      :type:  float
      :value: None



   .. py:attribute:: completeness_score
      :type:  float
      :value: None



   .. py:attribute:: improved_response
      :type:  str | None
      :value: None



   .. py:attribute:: improvements
      :type:  list[ImprovementSuggestion]
      :value: None



   .. py:attribute:: letter_grade
      :type:  str
      :value: None



   .. py:attribute:: overall_score
      :type:  QualityScore
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: None



.. py:class:: Improvement(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An improvement to a response based on reflection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Improvement
      :collapse:

   .. py:attribute:: category
      :type:  str
      :value: None



   .. py:attribute:: improved_text
      :type:  str | None
      :value: None



   .. py:attribute:: suggestion
      :type:  str
      :value: None



.. py:class:: ImprovementSuggestion(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A specific improvement suggestion.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ImprovementSuggestion
      :collapse:

   .. py:attribute:: category
      :type:  str
      :value: None



   .. py:attribute:: example
      :type:  str | None
      :value: None



   .. py:attribute:: priority
      :type:  Literal['high', 'medium', 'low']
      :value: None



   .. py:attribute:: suggestion
      :type:  str
      :value: None



.. py:class:: QualityScore(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simple quality score for respo, field_validatorses.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QualityScore
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  float
      :value: None



.. py:class:: ReflectionConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for reflection process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionConfig
      :collapse:

   .. py:attribute:: confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: force_iterations
      :type:  int | None
      :value: None



   .. py:attribute:: include_reasoning
      :type:  bool
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: min_score_threshold
      :type:  float
      :value: None



   .. py:attribute:: reflection_mode
      :type:  Literal['improve', 'critique', 'both']
      :value: None



   .. py:attribute:: stop_on_decline
      :type:  bool
      :value: None



.. py:class:: ReflectionOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output from reflection process (unstructured).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionOutput
      :collapse:

   .. py:attribute:: changes_made
      :type:  list[str]
      :value: None



   .. py:attribute:: iterations
      :type:  int
      :value: None



   .. py:attribute:: reflected_response
      :type:  str
      :value: None



   .. py:attribute:: reflection_notes
      :type:  str | None
      :value: None



.. py:class:: ReflectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete reflection analysis (for structured output pattern).

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



   .. py:attribute:: summary
      :type:  str
      :value: None



.. py:function:: to_prompt(obj) -> str

   Convert object to prompt string.


   .. autolink-examples:: to_prompt
      :collapse:

.. py:function:: validate_grade_matches_score(*args, **kwargs)

   Validate grade matches score (compatibility function).


   .. autolink-examples:: validate_grade_matches_score
      :collapse:

