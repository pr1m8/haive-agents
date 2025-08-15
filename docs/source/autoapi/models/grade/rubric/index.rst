models.grade.rubric
===================

.. py:module:: models.grade.rubric

.. autoapi-nested-parse::

   Rubric grading model for multi-criteria evaluations.

   This module implements a rubric-based grading system that evaluates
   multiple criteria with individual scores and weights.


   .. autolink-examples:: models.grade.rubric
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.rubric.RubricCriterion
   models.grade.rubric.RubricGrade


Module Contents
---------------

.. py:class:: RubricCriterion(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual criterion within a rubric.

   Represents a single evaluation criterion with its own score,
   weight, and justification.

   .. attribute:: name

      Name of the criterion

   .. attribute:: score

      Score for this criterion

   .. attribute:: max_score

      Maximum possible score for this criterion

   .. attribute:: weight

      Relative weight of this criterion (default 1.0)

   .. attribute:: justification

      Explanation for the score given

   .. rubric:: Example

   .. code-block:: python

       criterion = RubricCriterion(
       name="Content Quality",
       score=8.5,
       max_score=10,
       weight=0.4,
       justification="Strong content with minor gaps in coverage"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RubricCriterion
      :collapse:

   .. py:method:: get_normalized_score() -> float

      Get the criterion score as a normalized value (0.0 to 1.0).

      :returns: Normalized score (score / max_score)


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: get_percentage_score() -> float

      Get the criterion score as a percentage.

      :returns: Percentage score (normalized score * 100)


      .. autolink-examples:: get_percentage_score
         :collapse:


   .. py:method:: get_weighted_max_score() -> float

      Get the weighted maximum score for this criterion.

      :returns: Max score multiplied by weight


      .. autolink-examples:: get_weighted_max_score
         :collapse:


   .. py:method:: get_weighted_score() -> float

      Get the weighted score for this criterion.

      :returns: Score multiplied by weight


      .. autolink-examples:: get_weighted_score
         :collapse:


   .. py:method:: validate_score_range(v: int | float, info) -> int | float
      :classmethod:


      Validate that score is within valid range.

      :param v: The score value
      :param info: Validation context containing other field values

      :returns: Validated score

      :raises ValueError: If score is outside valid range


      .. autolink-examples:: validate_score_range
         :collapse:


   .. py:method:: validate_score_within_max() -> RubricCriterion

      Validate that score does not exceed max_score.

      :returns: Self if validation passes

      :raises ValueError: If score exceeds max_score


      .. autolink-examples:: validate_score_within_max
         :collapse:


   .. py:attribute:: justification
      :type:  str
      :value: None



   .. py:attribute:: max_score
      :type:  int | float
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  int | float
      :value: None



   .. py:attribute:: weight
      :type:  float
      :value: None



.. py:class:: RubricGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Rubric grading model for multi-criteria evaluations.

   This grade model evaluates multiple criteria, each with their own
   scores, weights, and justifications, then combines them into an
   overall grade.

   .. attribute:: criteria

      List of individual rubric criteria

   .. attribute:: grade_type

      Always GradeType.RUBRIC

   .. attribute:: overall_justification

      Overall summary justification

   .. rubric:: Example

   .. code-block:: python

       criteria = [
       RubricCriterion(
       name="Content Quality",
       score=8.5,
       max_score=10,
       weight=0.4,
       justification="Strong content with comprehensive coverage"
       ),
       RubricCriterion(
       name="Organization",
       score=7.0,
       max_score=10,
       weight=0.3,
       justification="Good structure but some transitions unclear"
       ),
       RubricCriterion(
       name="Grammar",
       score=9.0,
       max_score=10,
       weight=0.3,
       justification="Excellent grammar with only minor errors"
       )
       ]

       grade = RubricGrade(
       criteria=criteria,
       justification="Overall strong performance with room for improvement in organization"
       )


   .. autolink-examples:: RubricGrade
      :collapse:

   .. py:method:: create_simple_rubric(criteria_scores: dict[str, float | dict[str, Any]], justification: str, max_score: float = 10.0, **kwargs) -> RubricGrade
      :classmethod:


      Create a simple rubric with equal weights.

      :param criteria_scores: Dict mapping criterion names to scores or score dicts
      :param justification: Overall justification
      :param max_score: Maximum score for all criteria (default 10.0)
      :param \*\*kwargs: Additional parameters for the grade

      :returns: RubricGrade instance with equal-weighted criteria

      .. rubric:: Example

      .. code-block:: python

          grade = RubricGrade.create_simple_rubric(
          criteria_scores={
          "Content": 8.5,
          "Style": {"score": 7.0, "justification": "Good style overall"},
          "Accuracy": 9.0
          },
          justification="Strong overall performance",
          max_score=10
          )


      .. autolink-examples:: create_simple_rubric
         :collapse:


   .. py:method:: get_criteria_summary() -> dict[str, dict[str, Any]]

      Get a summary of all criteria performance.

      :returns: Dictionary mapping criterion names to their summary info


      .. autolink-examples:: get_criteria_summary
         :collapse:


   .. py:method:: get_criterion_by_name(name: str) -> RubricCriterion | None

      Get a specific criterion by name.

      :param name: Name of the criterion to find

      :returns: RubricCriterion if found, None otherwise


      .. autolink-examples:: get_criterion_by_name
         :collapse:


   .. py:method:: get_improvement_suggestions() -> list[str]

      Generate improvement suggestions based on weakest criteria.

      :returns: List of suggestions for improvement


      .. autolink-examples:: get_improvement_suggestions
         :collapse:


   .. py:method:: get_max_weighted_score() -> float

      Get the maximum possible weighted score.

      :returns: Sum of all weighted maximum scores


      .. autolink-examples:: get_max_weighted_score
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the overall grade as a normalized score between 0.0 and 1.0.

      Calculates weighted average of all criteria scores.

      :returns: Weighted normalized score across all criteria


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: get_raw_weighted_score() -> float

      Get the total raw weighted score.

      :returns: Sum of all weighted scores


      .. autolink-examples:: get_raw_weighted_score
         :collapse:


   .. py:method:: get_strongest_criteria(count: int = 3) -> list[RubricCriterion]

      Get the criteria with the highest normalized scores.

      :param count: Number of strongest criteria to return

      :returns: List of criteria sorted by normalized score (highest first)


      .. autolink-examples:: get_strongest_criteria
         :collapse:


   .. py:method:: get_weakest_criteria(count: int = 3) -> list[RubricCriterion]

      Get the criteria with the lowest normalized scores.

      :param count: Number of weakest criteria to return

      :returns: List of criteria sorted by normalized score (lowest first)


      .. autolink-examples:: get_weakest_criteria
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool

      Determine if the rubric grade represents a passing score.

      :param threshold: Custom threshold for passing (0.0 to 1.0).
                        If None, uses 0.7 (70%) as default

      :returns: True if the overall score meets or exceeds the threshold


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the rubric grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_criteria_names_unique(v: list[RubricCriterion]) -> list[RubricCriterion]
      :classmethod:


      Validate that all criterion names are unique.

      :param v: List of criteria to validate

      :returns: Validated criteria list

      :raises ValueError: If criterion names are not unique


      .. autolink-examples:: validate_criteria_names_unique
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value represents valid rubric criteria.

      :param value: The value to validate (should be list of criteria)

      :returns: True if the value can be converted to valid criteria, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:attribute:: criteria
      :type:  list[RubricCriterion]
      :value: None



   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



