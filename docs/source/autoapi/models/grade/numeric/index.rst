models.grade.numeric
====================

.. py:module:: models.grade.numeric

.. autoapi-nested-parse::

   Numeric grading models for score-based evaluations.

   This module implements numeric grading systems including general numeric
   scores and percentage-based grading.


   .. autolink-examples:: models.grade.numeric
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.numeric.NumericGrade
   models.grade.numeric.PercentageGrade


Module Contents
---------------

.. py:class:: NumericGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Numeric grading model for score-based evaluations.

   This grade model represents numeric scores within a configurable range,
   such as 0-10, 1-5, 0-100, etc.

   .. attribute:: value

      The numeric score value

   .. attribute:: min_value

      Minimum possible score (default 0)

   .. attribute:: max_value

      Maximum possible score (default 10)

   .. attribute:: passing_threshold

      Minimum score considered passing (default 60% of range)

   .. rubric:: Example

   .. code-block:: python

       # 0-10 scale
       grade = NumericGrade(
       value=8.5,
       min_value=0,
       max_value=10,
       justification="Strong performance with minor areas for improvement"
       )

       # 1-5 scale
       grade = NumericGrade(
       value=4,
       min_value=1,
       max_value=5,
       passing_threshold=3,
       justification="Above average quality"
       )

       # Custom range
       grade = NumericGrade(
       value=850,
       min_value=200,
       max_value=800,  # This will raise an error - value exceeds max
       justification="SAT score"
       )


   .. autolink-examples:: NumericGrade
      :collapse:

   .. py:method:: distance_from_threshold(threshold: float | None = None) -> float

      Calculate distance from passing threshold.

      :param threshold: Custom threshold to use. If None, uses instance threshold

      :returns: Positive value if above threshold, negative if below


      .. autolink-examples:: distance_from_threshold
         :collapse:


   .. py:method:: get_letter_equivalent() -> str

      Get an approximate letter grade equivalent.

      Uses standard grading scale based on percentage:
      A: 90-100%, B: 80-89%, C: 70-79%, D: 60-69%, F: <60%

      :returns: Letter grade string (A, B, C, D, F)


      .. autolink-examples:: get_letter_equivalent
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the grade as a normalized score between 0.0 and 1.0.

      :returns: Normalized score calculated as (value - min) / (max - min)


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: get_percentage_score() -> float

      Get the grade as a percentage (0-100).

      :returns: Percentage score (normalized score * 100)


      .. autolink-examples:: get_percentage_score
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool

      Determine if the grade represents a passing score.

      :param threshold: Custom threshold to use. If None, uses instance threshold
                        or 60% of range as default

      :returns: True if the score meets or exceeds the passing threshold


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the numeric grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value is numeric and within range.

      :param value: The value to validate

      :returns: True if the value is valid, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:method:: validate_score_range() -> NumericGrade

      Validate that the score is within the specified range.

      :returns: Self if validation passes

      :raises ValueError: If score is outside the valid range


      .. autolink-examples:: validate_score_range
         :collapse:


   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: max_value
      :type:  int | float
      :value: None



   .. py:attribute:: min_value
      :type:  int | float
      :value: None



   .. py:attribute:: passing_threshold
      :type:  int | float | None
      :value: None



   .. py:attribute:: value
      :type:  int | float
      :value: None



.. py:class:: PercentageGrade

   Bases: :py:obj:`NumericGrade`


   Percentage-based grading model (0-100%).

   A specialized numeric grade that's always in the 0-100 range,
   representing percentage scores.

   .. attribute:: value

      Percentage value (0-100)

   .. attribute:: min_value

      Always 0

   .. attribute:: max_value

      Always 100

   .. attribute:: passing_threshold

      Minimum percentage considered passing (default 60)

   .. rubric:: Example

   .. code-block:: python

       grade = PercentageGrade(
       value=87.5,
       justification="Excellent work with minor formatting issues",
       passing_threshold=70
       )

       # Automatically validates range
       bad_grade = PercentageGrade(
       value=105,  # This will raise an error
       justification="Invalid percentage"
       )


   .. autolink-examples:: PercentageGrade
      :collapse:

   .. py:method:: get_normalized_score() -> float

      Get the grade as a normalized score between 0.0 and 1.0.

      For percentages, this is simply value / 100.

      :returns: Normalized score (percentage / 100)


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: get_percentage_score() -> float

      Get the grade as a percentage (0-100).

      For PercentageGrade, this is just the value itself.

      :returns: The percentage value


      .. autolink-examples:: get_percentage_score
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the percentage grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_max_value(v: int | float) -> int | float
      :classmethod:


      Ensure max_value is always 100 for percentages.

      :param v: The max_value to validate

      :returns: Always returns 100


      .. autolink-examples:: validate_max_value
         :collapse:


   .. py:method:: validate_min_value(v: int | float) -> int | float
      :classmethod:


      Ensure min_value is always 0 for percentages.

      :param v: The min_value to validate

      :returns: Always returns 0


      .. autolink-examples:: validate_min_value
         :collapse:


   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: max_value
      :type:  int | float
      :value: None



   .. py:attribute:: min_value
      :type:  int | float
      :value: None



   .. py:attribute:: passing_threshold
      :type:  int | float
      :value: None



   .. py:attribute:: value
      :type:  int | float
      :value: None



