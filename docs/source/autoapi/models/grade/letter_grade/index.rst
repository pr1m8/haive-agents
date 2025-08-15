models.grade.letter_grade
=========================

.. py:module:: models.grade.letter_grade

.. autoapi-nested-parse::

   Letter grading model for traditional A-F evaluations.

   This module implements a traditional letter grading system with support
   for plus/minus modifiers and customizable grading scales.


   .. autolink-examples:: models.grade.letter_grade
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.letter_grade.LetterGrade
   models.grade.letter_grade.LetterValue


Module Contents
---------------

.. py:class:: LetterGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Letter grading model for traditional A-F evaluations.

   This grade model represents traditional letter grades with optional
   plus/minus modifiers. Includes conversion utilities and customizable
   grading scales.

   .. attribute:: value

      The letter grade value (A+ to F)

   .. attribute:: grade_type

      Always GradeType.LETTER

   .. attribute:: gpa_scale

      GPA scale to use (4.0 or 5.0, default 4.0)

   .. attribute:: passing_grade

      Minimum letter grade considered passing (default C-)

   .. rubric:: Example

   .. code-block:: python

       grade = LetterGrade(
       value="B+",
       justification="Strong understanding with minor gaps in analysis",
       gpa_scale=4.0
       )

       # Using enum value
       grade = LetterGrade(
       value=LetterValue.A_MINUS,
       justification="Excellent work with room for improvement"
       )

       # Custom passing threshold
       grade = LetterGrade(
       value="C",
       passing_grade="C",  # C is passing instead of default C-
       justification="Meets basic requirements"
       )


   .. autolink-examples:: LetterGrade
      :collapse:

   .. py:method:: _letter_grade_comparison(grade1: LetterValue, grade2: LetterValue) -> int

      Compare two letter grades.

      :param grade1: First letter grade
      :param grade2: Second letter grade

      :returns: Positive if grade1 > grade2, 0 if equal, negative if grade1 < grade2


      .. autolink-examples:: _letter_grade_comparison
         :collapse:


   .. py:method:: convert_to_letter_value(v: Any) -> LetterValue
      :classmethod:


      Convert string or other representations to LetterValue.

      :param v: Value to convert to LetterValue

      :returns: LetterValue enum instance

      :raises ValueError: If the value cannot be converted to a valid letter grade


      .. autolink-examples:: convert_to_letter_value
         :collapse:


   .. py:method:: from_percentage(percentage: float, justification: str, gpa_scale: float = 4.0, **kwargs) -> LetterGrade
      :classmethod:


      Create a LetterGrade from a percentage score.

      :param percentage: Percentage score (0-100)
      :param justification: Explanation for the grade
      :param gpa_scale: GPA scale to use
      :param \*\*kwargs: Additional parameters for the grade

      :returns: LetterGrade instance corresponding to the percentage

      :raises ValueError: If percentage is outside valid range


      .. autolink-examples:: from_percentage
         :collapse:


   .. py:method:: get_gpa_points() -> float

      Get GPA points for this letter grade.

      :returns: GPA points based on the configured scale


      .. autolink-examples:: get_gpa_points
         :collapse:


   .. py:method:: get_letter_quality_description() -> str

      Get a descriptive quality label for the letter grade.

      :returns: String describing the quality level of the grade


      .. autolink-examples:: get_letter_quality_description
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the grade as a normalized score between 0.0 and 1.0.

      Uses standard percentage equivalents for letter grades.

      :returns: Normalized score based on letter grade


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: is_passing(threshold: str | None = None) -> bool

      Determine if the grade represents a passing score.

      :param threshold: Custom passing threshold as letter grade string.
                        If None, uses instance passing_grade

      :returns: True if the grade meets or exceeds the passing threshold


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the letter grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_gpa_scale(v: float) -> float
      :classmethod:


      Validate GPA scale is reasonable.

      :param v: GPA scale value

      :returns: Validated GPA scale

      :raises ValueError: If GPA scale is not reasonable


      .. autolink-examples:: validate_gpa_scale
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value can be converted to a letter grade.

      :param value: The value to validate

      :returns: True if the value can be converted to LetterValue, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:attribute:: gpa_scale
      :type:  float
      :value: None



   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: passing_grade
      :type:  LetterValue
      :value: None



   .. py:attribute:: value
      :type:  LetterValue
      :value: None



.. py:class:: LetterValue

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Valid letter grade values.

   .. attribute:: A_PLUS

      Exceptional performance (A+)

   .. attribute:: A

      Excellent performance (A)

   .. attribute:: A_MINUS

      Very good performance (A-)

   .. attribute:: B_PLUS

      Good performance (B+)

   .. attribute:: B

      Satisfactory performance (B)

   .. attribute:: B_MINUS

      Below satisfactory (B-)

   .. attribute:: C_PLUS

      Acceptable performance (C+)

   .. attribute:: C

      Minimally acceptable (C)

   .. attribute:: C_MINUS

      Below acceptable (C-)

   .. attribute:: D_PLUS

      Poor performance (D+)

   .. attribute:: D

      Very poor performance (D)

   .. attribute:: D_MINUS

      Extremely poor (D-)

   .. attribute:: F

      Failing performance (F)

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LetterValue
      :collapse:

   .. py:attribute:: A
      :value: 'A'



   .. py:attribute:: A_MINUS
      :value: 'A-'



   .. py:attribute:: A_PLUS
      :value: 'A+'



   .. py:attribute:: B
      :value: 'B'



   .. py:attribute:: B_MINUS
      :value: 'B-'



   .. py:attribute:: B_PLUS
      :value: 'B+'



   .. py:attribute:: C
      :value: 'C'



   .. py:attribute:: C_MINUS
      :value: 'C-'



   .. py:attribute:: C_PLUS
      :value: 'C+'



   .. py:attribute:: D
      :value: 'D'



   .. py:attribute:: D_MINUS
      :value: 'D-'



   .. py:attribute:: D_PLUS
      :value: 'D+'



   .. py:attribute:: F
      :value: 'F'



