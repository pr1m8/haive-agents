models.grade.qualitative
========================

.. py:module:: models.grade.qualitative

.. autoapi-nested-parse::

   Qualitative grading model for text-based evaluations.

   This module implements a qualitative grading system that provides
   text-based assessments with sentiment analysis and quality indicators.


   .. autolink-examples:: models.grade.qualitative
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.qualitative.QualitativeGrade
   models.grade.qualitative.QualityLevel
   models.grade.qualitative.SentimentType


Module Contents
---------------

.. py:class:: QualitativeGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Qualitative grading model for text-based evaluations.

   This grade model provides detailed text-based assessments with
   quality levels, sentiment analysis, and structured feedback
   including strengths, weaknesses, and recommendations.

   .. attribute:: quality_level

      Overall quality assessment

   .. attribute:: sentiment

      Sentiment of the feedback

   .. attribute:: strengths

      List of identified strengths

   .. attribute:: weaknesses

      List of identified weaknesses

   .. attribute:: recommendations

      List of improvement recommendations

   .. attribute:: detailed_feedback

      Extended qualitative feedback

   .. rubric:: Example

   .. code-block:: python

       grade = QualitativeGrade(
       quality_level=QualityLevel.GOOD,
       sentiment=SentimentType.POSITIVE,
       strengths=[
       "Clear logical structure",
       "Strong supporting evidence",
       "Engaging writing style"
       ],
       weaknesses=[
       "Minor grammatical errors",
       "Could use more varied sentence structure"
       ],
       recommendations=[
       "Proofread for grammatical accuracy",
       "Vary sentence length and structure for better flow"
       ],
       justification="Well-written piece with strong content but needs polish",
       detailed_feedback="This work demonstrates a solid understanding..."
       )


   .. autolink-examples:: QualitativeGrade
      :collapse:

   .. py:method:: _calculate_feedback_balance() -> str

      Calculate the balance between positive and negative feedback.

      :returns: String describing the feedback balance


      .. autolink-examples:: _calculate_feedback_balance
         :collapse:


   .. py:method:: create_constructive_feedback(justification: str, strengths: list[str], weaknesses: list[str], recommendations: list[str], quality_level: QualityLevel = QualityLevel.FAIR, **kwargs) -> QualitativeGrade
      :classmethod:


      Create balanced constructive feedback.

      :param justification: Main justification
      :param strengths: List of strengths
      :param weaknesses: List of weaknesses
      :param recommendations: List of improvement recommendations
      :param quality_level: Quality level (default FAIR)
      :param \*\*kwargs: Additional parameters

      :returns: QualitativeGrade with balanced feedback


      .. autolink-examples:: create_constructive_feedback
         :collapse:


   .. py:method:: create_positive_feedback(justification: str, strengths: list[str], minor_improvements: list[str] | None = None, quality_level: QualityLevel = QualityLevel.GOOD, **kwargs) -> QualitativeGrade
      :classmethod:


      Create predominantly positive qualitative feedback.

      :param justification: Main justification
      :param strengths: List of strengths to highlight
      :param minor_improvements: Optional minor areas for improvement
      :param quality_level: Quality level (default GOOD)
      :param \*\*kwargs: Additional parameters

      :returns: QualitativeGrade with positive sentiment


      .. autolink-examples:: create_positive_feedback
         :collapse:


   .. py:method:: generate_narrative_summary() -> str

      Generate a narrative summary of the qualitative assessment.

      :returns: Human-readable narrative summary


      .. autolink-examples:: generate_narrative_summary
         :collapse:


   .. py:method:: get_feedback_summary() -> dict[str, Any]

      Get a structured summary of all feedback.

      :returns: Dictionary containing organized feedback information


      .. autolink-examples:: get_feedback_summary
         :collapse:


   .. py:method:: get_improvement_priority() -> list[str]

      Get prioritized improvement recommendations.

      Returns top weaknesses with corresponding recommendations.

      :returns: List of prioritized improvement items


      .. autolink-examples:: get_improvement_priority
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the grade as a normalized score between 0.0 and 1.0.

      Based on quality level mapping to numeric equivalents.

      :returns: Normalized score based on quality level


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool

      Determine if the grade represents a passing score.

      :param threshold: Custom threshold for passing (0.0 to 1.0).
                        If None, uses 0.6 (equivalent to "fair" quality)

      :returns: True if the quality level meets or exceeds the threshold


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the qualitative grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_feedback_consistency() -> QualitativeGrade

      Validate that feedback is consistent with quality level.

      :returns: Self if validation passes

      :raises ValueError: If feedback is inconsistent with quality level


      .. autolink-examples:: validate_feedback_consistency
         :collapse:


   .. py:method:: validate_feedback_items(v: list[str]) -> list[str]
      :classmethod:


      Validate that feedback items are meaningful.

      :param v: List of feedback items to validate

      :returns: Validated list of feedback items

      :raises ValueError: If items are empty or too vague


      .. autolink-examples:: validate_feedback_items
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value can be converted to a quality level.

      :param value: The value to validate

      :returns: True if the value can be converted to QualityLevel, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:attribute:: detailed_feedback
      :type:  str | None
      :value: None



   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: quality_level
      :type:  QualityLevel
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: sentiment
      :type:  SentimentType
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: None



.. py:class:: QualityLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Quality levels for qualitative assessment.

   .. attribute:: EXCEPTIONAL

      Outstanding quality, exceeds expectations

   .. attribute:: EXCELLENT

      High quality, meets all expectations

   .. attribute:: GOOD

      Satisfactory quality, meets most expectations

   .. attribute:: FAIR

      Adequate quality, meets basic expectations

   .. attribute:: POOR

      Below expectations, significant issues

   .. attribute:: UNACCEPTABLE

      Does not meet minimum standards

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QualityLevel
      :collapse:

   .. py:attribute:: EXCELLENT
      :value: 'excellent'



   .. py:attribute:: EXCEPTIONAL
      :value: 'exceptional'



   .. py:attribute:: FAIR
      :value: 'fair'



   .. py:attribute:: GOOD
      :value: 'good'



   .. py:attribute:: POOR
      :value: 'poor'



   .. py:attribute:: UNACCEPTABLE
      :value: 'unacceptable'



.. py:class:: SentimentType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Sentiment types for qualitative feedback.

   .. attribute:: VERY_POSITIVE

      Highly positive feedback

   .. attribute:: POSITIVE

      Generally positive feedback

   .. attribute:: NEUTRAL

      Balanced or neutral feedback

   .. attribute:: NEGATIVE

      Generally negative feedback

   .. attribute:: VERY_NEGATIVE

      Highly negative feedback

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SentimentType
      :collapse:

   .. py:attribute:: NEGATIVE
      :value: 'negative'



   .. py:attribute:: NEUTRAL
      :value: 'neutral'



   .. py:attribute:: POSITIVE
      :value: 'positive'



   .. py:attribute:: VERY_NEGATIVE
      :value: 'very_negative'



   .. py:attribute:: VERY_POSITIVE
      :value: 'very_positive'



