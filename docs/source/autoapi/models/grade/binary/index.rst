models.grade.binary
===================

.. py:module:: models.grade.binary

.. autoapi-nested-parse::

   Binary grading model for pass/fail evaluations.

   This module implements a binary grading system suitable for pass/fail,
   yes/no, correct/incorrect, and similar binary evaluations.


   .. autolink-examples:: models.grade.binary
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.binary.BinaryGrade


Module Contents
---------------

.. py:class:: BinaryGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Binary grading model for pass/fail evaluations.

   This grade model represents simple binary outcomes such as pass/fail,
   yes/no, correct/incorrect, acceptable/unacceptable, etc.

   .. attribute:: value

      The binary grade value (True for pass/yes, False for fail/no)

   .. attribute:: grade_type

      Always GradeType.BINARY

   .. rubric:: Example

   .. code-block:: python

       # Passing grade
       grade = BinaryGrade(
       value=True,
       justification="Response correctly identifies all key concepts",
       confidence=0.95
       )

       # Failing grade
       grade = BinaryGrade(
       value=False,
       justification="Response contains factual errors and misses main points",
       confidence=0.88
       )

       # Using string values (automatically converted)
       grade = BinaryGrade(
       value="pass",  # Converted to True
       justification="Meets minimum requirements"
       )


   .. autolink-examples:: BinaryGrade
      :collapse:

   .. py:method:: convert_value_to_bool(v: Any) -> bool
      :classmethod:


      Convert various representations to boolean.

      Accepts boolean values, strings, and numbers and converts them
      to appropriate boolean values for grading.

      :param v: Value to convert to boolean

      :returns: Boolean representation of the value

      :raises ValueError: If the value cannot be converted to a meaningful boolean


      .. autolink-examples:: convert_value_to_bool
         :collapse:


   .. py:method:: create_fail(justification: str, confidence: float = 1.0, **kwargs) -> BinaryGrade
      :classmethod:


      Convenience method to create a failing grade.

      :param justification: Explanation for the failing grade
      :param confidence: Confidence level (default 1.0)
      :param \*\*kwargs: Additional parameters for the grade

      :returns: BinaryGrade instance with value=False


      .. autolink-examples:: create_fail
         :collapse:


   .. py:method:: create_pass(justification: str, confidence: float = 1.0, **kwargs) -> BinaryGrade
      :classmethod:


      Convenience method to create a passing grade.

      :param justification: Explanation for the passing grade
      :param confidence: Confidence level (default 1.0)
      :param \*\*kwargs: Additional parameters for the grade

      :returns: BinaryGrade instance with value=True


      .. autolink-examples:: create_pass
         :collapse:


   .. py:method:: flip() -> BinaryGrade

      Create a new BinaryGrade with the opposite value.

      Useful for creating inverse grades or testing scenarios.

      :returns: New BinaryGrade instance with flipped value


      .. autolink-examples:: flip
         :collapse:


   .. py:method:: get_display_value() -> str

      Get a human-readable display value.

      :returns: "Pass" for True, "Fail" for False


      .. autolink-examples:: get_display_value
         :collapse:


   .. py:method:: get_emoji_representation() -> str

      Get an emoji representation of the grade.

      :returns: ✅ for pass, ❌ for fail


      .. autolink-examples:: get_emoji_representation
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the grade as a normalized score between 0.0 and 1.0.

      :returns: 1.0 for True (pass), 0.0 for False (fail)


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool

      Determine if the grade represents a passing score.

      For binary grades, this simply returns the boolean value.
      The threshold parameter is ignored for binary grades.

      :param threshold: Ignored for binary grades

      :returns: The boolean value of the grade


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the binary grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value can be converted to binary.

      :param value: The value to validate

      :returns: True if the value can be converted to boolean, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: value
      :type:  bool
      :value: None



