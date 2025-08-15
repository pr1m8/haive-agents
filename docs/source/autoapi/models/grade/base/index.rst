models.grade.base
=================

.. py:module:: models.grade.base

.. autoapi-nested-parse::

   Base classes for grade models.

   This module defines the fundamental abstractions for all grading models
   including the grade type enumeration and abstract base class.


   .. autolink-examples:: models.grade.base
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.base.Grade
   models.grade.base.GradeType


Module Contents
---------------

.. py:class:: Grade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`abc.ABC`


   Abstract base class for all grade models.

   This class provides the common interface and functionality that all
   grade models must implement. It includes metadata, validation,
   and utility methods.

   .. attribute:: grade_type

      The type of grade model

   .. attribute:: justification

      Explanation for the grade assigned

   .. attribute:: confidence

      Confidence level in the grade (0.0 to 1.0)

   .. attribute:: metadata

      Additional metadata about the grading

   .. attribute:: grader_id

      Identifier of the grader (agent, human, etc.)

   .. attribute:: timestamp

      When the grade was assigned

   .. rubric:: Example

   .. code-block:: python

       # This is an abstract class, use concrete implementations
       grade = BinaryGrade(
       value=True,
       justification="Response meets all criteria",
       confidence=0.95
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Grade
      :collapse:

   .. py:method:: _generate_comparison_summary(other: Grade) -> str

      Generate a human-readable comparison summary.

      :param other: Another Grade instance to compare against

      :returns: String summary of the comparison


      .. autolink-examples:: _generate_comparison_summary
         :collapse:


   .. py:method:: compare_to(other: Grade) -> dict[str, float | str]

      Compare this grade to another grade.

      :param other: Another Grade instance to compare against

      :returns: Dictionary containing comparison information

      :raises TypeError: If other is not a Grade instance


      .. autolink-examples:: compare_to
         :collapse:


   .. py:method:: get_grade_summary() -> dict[str, Any]

      Get a summary of the grade information.

      :returns: Dictionary containing key grade information for display


      .. autolink-examples:: get_grade_summary
         :collapse:


   .. py:method:: get_normalized_score() -> float
      :abstractmethod:


      Get the grade as a normalized score between 0.0 and 1.0.

      This method must be implemented by all concrete grade classes
      to provide a common way to compare grades across different types.

      :returns: A float between 0.0 and 1.0 representing the normalized grade


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool
      :abstractmethod:


      Determine if the grade represents a passing score.

      :param threshold: Optional custom threshold for passing.
                        If None, uses grade type default.

      :returns: True if the grade is considered passing, False otherwise


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a grade value is appropriate for this grade type.

      This method should be overridden by concrete classes to provide
      type-specific validation.

      :param value: The value to validate

      :returns: True if valid, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:method:: validate_justification(v: str) -> str
      :classmethod:


      Validate that justification is meaningful.

      :param v: The justification string to validate

      :returns: The validated justification string

      :raises ValueError: If justification is empty, too short, or meaningless


      .. autolink-examples:: validate_justification
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: grade_type
      :type:  GradeType
      :value: None



   .. py:attribute:: grader_id
      :type:  str | None
      :value: None



   .. py:attribute:: justification
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: GradeType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of grade models available.

   .. attribute:: BINARY

      Simple pass/fail or yes/no grading

   .. attribute:: NUMERIC

      Numeric scoring with configurable ranges

   .. attribute:: PERCENTAGE

      Percentage-based scoring (0-100%)

   .. attribute:: LETTER

      Traditional letter-based grading (A-F)

   .. attribute:: RUBRIC

      Multi-criteria rubric-based evaluation

   .. attribute:: QUALITATIVE

      Text-based qualitative assessment

   .. attribute:: SCALE

      Likert-scale or custom scale grading

   .. attribute:: COMPOSITE

      Combination of multiple grade types

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GradeType
      :collapse:

   .. py:attribute:: BINARY
      :value: 'binary'



   .. py:attribute:: COMPOSITE
      :value: 'composite'



   .. py:attribute:: LETTER
      :value: 'letter'



   .. py:attribute:: NUMERIC
      :value: 'numeric'



   .. py:attribute:: PERCENTAGE
      :value: 'percentage'



   .. py:attribute:: QUALITATIVE
      :value: 'qualitative'



   .. py:attribute:: RUBRIC
      :value: 'rubric'



   .. py:attribute:: SCALE
      :value: 'scale'



