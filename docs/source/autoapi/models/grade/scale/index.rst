models.grade.scale
==================

.. py:module:: models.grade.scale

.. autoapi-nested-parse::

   Scale grading model for Likert-style evaluations.

   This module implements scale-based grading systems including Likert scales,
   satisfaction ratings, and custom ordinal scales.


   .. autolink-examples:: models.grade.scale
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.scale.LikertScale
   models.grade.scale.SatisfactionScale
   models.grade.scale.ScaleGrade


Module Contents
---------------

.. py:class:: LikertScale

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Standard 5-point Likert scale values.

   .. attribute:: STRONGLY_DISAGREE

      Strongly disagree (1)

   .. attribute:: DISAGREE

      Disagree (2)

   .. attribute:: NEUTRAL

      Neither agree nor disagree (3)

   .. attribute:: AGREE

      Agree (4)

   .. attribute:: STRONGLY_AGREE

      Strongly agree (5)

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LikertScale
      :collapse:

   .. py:attribute:: AGREE
      :value: 'agree'



   .. py:attribute:: DISAGREE
      :value: 'disagree'



   .. py:attribute:: NEUTRAL
      :value: 'neutral'



   .. py:attribute:: STRONGLY_AGREE
      :value: 'strongly_agree'



   .. py:attribute:: STRONGLY_DISAGREE
      :value: 'strongly_disagree'



.. py:class:: SatisfactionScale

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Standard satisfaction rating scale.

   .. attribute:: VERY_DISSATISFIED

      Very dissatisfied (1)

   .. attribute:: DISSATISFIED

      Dissatisfied (2)

   .. attribute:: NEUTRAL

      Neutral (3)

   .. attribute:: SATISFIED

      Satisfied (4)

   .. attribute:: VERY_SATISFIED

      Very satisfied (5)

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SatisfactionScale
      :collapse:

   .. py:attribute:: DISSATISFIED
      :value: 'dissatisfied'



   .. py:attribute:: NEUTRAL
      :value: 'neutral'



   .. py:attribute:: SATISFIED
      :value: 'satisfied'



   .. py:attribute:: VERY_DISSATISFIED
      :value: 'very_dissatisfied'



   .. py:attribute:: VERY_SATISFIED
      :value: 'very_satisfied'



.. py:class:: ScaleGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Scale grading model for Likert-style evaluations.

   This grade model represents ordinal scale ratings such as Likert scales,
   satisfaction ratings, or custom scales with labeled points.

   .. attribute:: scale_value

      The selected scale value

   .. attribute:: scale_labels

      List of scale labels in order from lowest to highest

   .. attribute:: scale_type

      Optional scale type identifier

   .. attribute:: numeric_value

      Numeric equivalent of the scale position

   .. rubric:: Example

   .. code-block:: python

       # Using predefined Likert scale
       grade = ScaleGrade(
       scale_value="agree",
       scale_labels=["strongly_disagree", "disagree", "neutral", "agree", "strongly_agree"],
       scale_type="likert_5",
       justification="Response shows good understanding with minor reservations"
       )

       # Custom satisfaction scale
       grade = ScaleGrade(
       scale_value="satisfied",
       scale_labels=["very_dissatisfied", "dissatisfied", "neutral", "satisfied", "very_satisfied"],
       scale_type="satisfaction",
       justification="User feedback indicates satisfaction with minor issues"
       )

       # Custom numeric scale with labels
       grade = ScaleGrade(
       scale_value="good",
       scale_labels=["poor", "fair", "good", "very_good", "excellent"],
       scale_type="quality_5",
       justification="Quality meets expectations"
       )


   .. autolink-examples:: ScaleGrade
      :collapse:

   .. py:method:: create_likert_5(value: str | LikertScale, justification: str, **kwargs) -> ScaleGrade
      :classmethod:


      Create a 5-point Likert scale grade.

      :param value: Likert scale value
      :param justification: Explanation for the rating
      :param \*\*kwargs: Additional parameters

      :returns: ScaleGrade configured as 5-point Likert scale


      .. autolink-examples:: create_likert_5
         :collapse:


   .. py:method:: create_numeric_scale(value: int, min_value: int = 1, max_value: int = 5, justification: str = '', **kwargs) -> ScaleGrade
      :classmethod:


      Create a numeric scale grade.

      :param value: Numeric value selected
      :param min_value: Minimum value of the scale
      :param max_value: Maximum value of the scale
      :param justification: Explanation for the rating
      :param \*\*kwargs: Additional parameters

      :returns: ScaleGrade configured as numeric scale


      .. autolink-examples:: create_numeric_scale
         :collapse:


   .. py:method:: create_quality_scale(value: str, justification: str, scale_size: int = 5, **kwargs) -> ScaleGrade
      :classmethod:


      Create a quality assessment scale grade.

      :param value: Quality level selected
      :param justification: Explanation for the rating
      :param scale_size: Size of the quality scale (3, 4, or 5)
      :param \*\*kwargs: Additional parameters

      :returns: ScaleGrade configured as quality scale


      .. autolink-examples:: create_quality_scale
         :collapse:


   .. py:method:: create_satisfaction_5(value: str | SatisfactionScale, justification: str, **kwargs) -> ScaleGrade
      :classmethod:


      Create a 5-point satisfaction scale grade.

      :param value: Satisfaction scale value
      :param justification: Explanation for the rating
      :param \*\*kwargs: Additional parameters

      :returns: ScaleGrade configured as 5-point satisfaction scale


      .. autolink-examples:: create_satisfaction_5
         :collapse:


   .. py:method:: distance_from_neutral() -> float

      Calculate distance from the neutral/middle point of the scale.

      :returns: Signed distance from neutral (negative = below, positive = above)


      .. autolink-examples:: distance_from_neutral
         :collapse:


   .. py:method:: get_adjacent_values() -> dict[str, str | None]

      Get the adjacent scale values (one above and one below).

      :returns: Dictionary with 'lower' and 'higher' adjacent values


      .. autolink-examples:: get_adjacent_values
         :collapse:


   .. py:method:: get_descriptive_assessment() -> str

      Get a descriptive assessment based on scale position.

      :returns: Descriptive string based on position in scale


      .. autolink-examples:: get_descriptive_assessment
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the grade as a normalized score between 0.0 and 1.0.

      Based on position within the scale range.

      :returns: Normalized score (position - 1) / (max_position - 1)


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: get_scale_percentage() -> float

      Get the scale position as a percentage.

      :returns: Percentage representing position in scale (0-100)


      .. autolink-examples:: get_scale_percentage
         :collapse:


   .. py:method:: get_scale_position() -> int

      Get the 1-indexed position of the value in the scale.

      :returns: Position of the selected value (1 = lowest, max = highest)


      .. autolink-examples:: get_scale_position
         :collapse:


   .. py:method:: is_bottom_tier(bottom_percent: float = 0.3) -> bool

      Check if the grade is in the bottom tier of the scale.

      :param bottom_percent: What percentage of the scale constitutes "bottom tier"

      :returns: True if the grade is in the bottom tier


      .. autolink-examples:: is_bottom_tier
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool

      Determine if the scale grade represents a passing score.

      :param threshold: Custom threshold (0.0 to 1.0). If None, uses
                        the middle point of the scale as threshold

      :returns: True if the scale position meets or exceeds the threshold


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: is_top_tier(top_percent: float = 0.3) -> bool

      Check if the grade is in the top tier of the scale.

      :param top_percent: What percentage of the scale constitutes "top tier"

      :returns: True if the grade is in the top tier


      .. autolink-examples:: is_top_tier
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the scale grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value exists in the scale labels.

      :param value: The value to validate

      :returns: True if the value is in scale_labels, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:method:: validate_scale_labels_unique(v: list[str]) -> list[str]
      :classmethod:


      Validate that all scale labels are unique.

      :param v: List of scale labels to validate

      :returns: Validated scale labels list

      :raises ValueError: If scale labels are not unique


      .. autolink-examples:: validate_scale_labels_unique
         :collapse:


   .. py:method:: validate_scale_value_and_set_numeric() -> ScaleGrade

      Validate scale_value is in scale_labels and set numeric_value.

      :returns: Self with numeric_value set

      :raises ValueError: If scale_value is not in scale_labels


      .. autolink-examples:: validate_scale_value_and_set_numeric
         :collapse:


   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: numeric_value
      :type:  int | None
      :value: None



   .. py:attribute:: scale_labels
      :type:  list[str]
      :value: None



   .. py:attribute:: scale_type
      :type:  str | None
      :value: None



   .. py:attribute:: scale_value
      :type:  str
      :value: None



