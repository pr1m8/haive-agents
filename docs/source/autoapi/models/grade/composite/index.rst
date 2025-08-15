models.grade.composite
======================

.. py:module:: models.grade.composite

.. autoapi-nested-parse::

   Composite grading model for combining multiple grade types.

   This module implements a composite grading system that combines multiple
   different grade types into a single comprehensive evaluation.


   .. autolink-examples:: models.grade.composite
      :collapse:


Classes
-------

.. autoapisummary::

   models.grade.composite.CompositeGrade


Module Contents
---------------

.. py:class:: CompositeGrade

   Bases: :py:obj:`haive.agents.common.models.grade.base.Grade`


   Composite grading model for combining multiple grade types.

   This grade model combines multiple individual grades of different types
   into a single comprehensive assessment. It supports weighted averaging,
   statistical analysis, and consensus building across different grading approaches.

   .. attribute:: grades

      List of individual grades to combine

   .. attribute:: weights

      Optional weights for each grade (auto-normalized)

   .. attribute:: combination_method

      Method for combining grades

   .. attribute:: primary_grade_index

      Index of the primary/most important grade

   .. attribute:: consensus_threshold

      Threshold for consensus analysis

   .. rubric:: Example

   .. code-block:: python

       # Individual grades
       binary_grade = BinaryGrade(value=True, justification="Meets requirements")
       numeric_grade = NumericGrade(value=8.5, max_value=10, justification="High quality work")
       letter_grade = LetterGrade(value="B+", justification="Good performance overall")

       # Composite grade
       composite = CompositeGrade(
       grades=[binary_grade, numeric_grade, letter_grade],
       weights=[0.2, 0.5, 0.3],  # Different importance levels
       combination_method="weighted_average",
       justification="Combined assessment across multiple criteria"
       )

       # Equal weight composite
       composite_equal = CompositeGrade(
       grades=[binary_grade, numeric_grade, letter_grade],
       combination_method="simple_average",
       justification="Balanced multi-perspective evaluation"
       )


   .. autolink-examples:: CompositeGrade
      :collapse:

   .. py:method:: create_consensus_grade(grades: list[haive.agents.common.models.grade.base.Grade], justification: str, consensus_threshold: float = 0.8, **kwargs) -> CompositeGrade
      :classmethod:


      Create a CompositeGrade focused on consensus building.

      :param grades: List of Grade instances to combine
      :param justification: Overall justification
      :param consensus_threshold: Threshold for consensus detection
      :param \*\*kwargs: Additional parameters

      :returns: CompositeGrade configured for consensus analysis


      .. autolink-examples:: create_consensus_grade
         :collapse:


   .. py:method:: create_from_grades(grades: list[haive.agents.common.models.grade.base.Grade], justification: str, weights: list[float] | None = None, method: str = 'weighted_average', **kwargs) -> CompositeGrade
      :classmethod:


      Create a CompositeGrade from a list of existing grades.

      :param grades: List of Grade instances to combine
      :param justification: Overall justification for the composite
      :param weights: Optional weights for each grade
      :param method: Combination method to use
      :param \*\*kwargs: Additional parameters

      :returns: CompositeGrade instance


      .. autolink-examples:: create_from_grades
         :collapse:


   .. py:method:: get_consensus_analysis() -> dict[str, Any]

      Get detailed consensus analysis.

      :returns: Dictionary with consensus analysis information


      .. autolink-examples:: get_consensus_analysis
         :collapse:


   .. py:method:: get_grade_breakdown() -> list[dict[str, Any]]

      Get detailed breakdown of individual grades.

      :returns: List of dictionaries with information about each grade


      .. autolink-examples:: get_grade_breakdown
         :collapse:


   .. py:method:: get_grade_statistics() -> dict[str, float]

      Get statistical analysis of the individual grades.

      :returns: Dictionary containing statistical measures


      .. autolink-examples:: get_grade_statistics
         :collapse:


   .. py:method:: get_normalized_score() -> float

      Get the composite grade as a normalized score between 0.0 and 1.0.

      Uses the specified combination method to compute the final score.

      :returns: Combined normalized score across all grades


      .. autolink-examples:: get_normalized_score
         :collapse:


   .. py:method:: get_normalized_score_using_method(method: str) -> float

      Get normalized score using a specific combination method.

      :param method: Combination method to use

      :returns: Normalized score using the specified method


      .. autolink-examples:: get_normalized_score_using_method
         :collapse:


   .. py:method:: get_normalized_weights() -> list[float]

      Get normalized weights that sum to 1.0.

      :returns: List of normalized weights (equal weights if none provided)


      .. autolink-examples:: get_normalized_weights
         :collapse:


   .. py:method:: get_outlier_grades(threshold: float = 0.3) -> list[int]

      Identify grades that are outliers compared to the group.

      :param threshold: Deviation threshold for considering a grade an outlier

      :returns: List of indices of grades that are outliers


      .. autolink-examples:: get_outlier_grades
         :collapse:


   .. py:method:: has_consensus() -> bool

      Check if there's consensus among the individual grades.

      :returns: True if the variance in normalized scores is below consensus threshold


      .. autolink-examples:: has_consensus
         :collapse:


   .. py:method:: is_passing(threshold: float | None = None) -> bool

      Determine if the composite grade represents a passing score.

      :param threshold: Custom threshold for passing (0.0 to 1.0).
                        If None, uses 0.6 as default

      :returns: True if the composite score meets or exceeds the threshold


      .. autolink-examples:: is_passing
         :collapse:


   .. py:method:: to_display_string() -> str

      Convert grade to a human-readable display string.

      :returns: Formatted string representation of the composite grade


      .. autolink-examples:: to_display_string
         :collapse:


   .. py:method:: validate_combination_method(v: str) -> str
      :classmethod:


      Validate that combination method is supported.

      :param v: Combination method string

      :returns: Validated combination method

      :raises ValueError: If combination method is not supported


      .. autolink-examples:: validate_combination_method
         :collapse:


   .. py:method:: validate_grade_value(value: Any) -> bool

      Validate that a value represents valid composite grade data.

      :param value: The value to validate (should be list of grades)

      :returns: True if the value can be converted to valid grades, False otherwise


      .. autolink-examples:: validate_grade_value
         :collapse:


   .. py:method:: validate_weights_and_indices() -> CompositeGrade

      Validate weights match grades count and indices are valid.

      :returns: Self if validation passes

      :raises ValueError: If weights or indices are invalid


      .. autolink-examples:: validate_weights_and_indices
         :collapse:


   .. py:attribute:: combination_method
      :type:  str
      :value: None



   .. py:attribute:: consensus_threshold
      :type:  float
      :value: None



   .. py:attribute:: grade_type
      :type:  haive.agents.common.models.grade.base.GradeType
      :value: None



   .. py:attribute:: grades
      :type:  list[haive.agents.common.models.grade.base.Grade]
      :value: None



   .. py:attribute:: primary_grade_index
      :type:  int | None
      :value: None



   .. py:attribute:: weights
      :type:  list[float] | None
      :value: None



