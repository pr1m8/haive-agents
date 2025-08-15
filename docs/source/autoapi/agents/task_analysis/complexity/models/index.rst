agents.task_analysis.complexity.models
======================================

.. py:module:: agents.task_analysis.complexity.models


Classes
-------

.. autoapisummary::

   agents.task_analysis.complexity.models.ComplexityAnalysis
   agents.task_analysis.complexity.models.ComplexityFactors
   agents.task_analysis.complexity.models.ComplexityLevel
   agents.task_analysis.complexity.models.ComplexityVector


Module Contents
---------------

.. py:class:: ComplexityAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete complexity analysis result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexityAnalysis
      :collapse:

   .. py:attribute:: analysis_confidence
      :type:  float
      :value: None



   .. py:attribute:: complexity_factors
      :type:  ComplexityFactors


   .. py:attribute:: complexity_vector
      :type:  ComplexityVector


   .. py:attribute:: confidence_factors
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: mitigation_strategies
      :type:  list[str]
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: risk_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: simplification_opportunities
      :type:  list[str]
      :value: None



.. py:class:: ComplexityFactors(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Detailed factors contributing to complexity.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexityFactors
      :collapse:

   .. py:attribute:: api_complexity
      :type:  str
      :value: None



   .. py:attribute:: coordination_points
      :type:  int
      :value: None



   .. py:attribute:: data_transformations
      :type:  int
      :value: None



   .. py:attribute:: dependency_density
      :type:  float
      :value: None



   .. py:attribute:: domain_count
      :type:  int
      :value: None



   .. py:attribute:: expertise_level
      :type:  str
      :value: None



   .. py:attribute:: external_systems
      :type:  int
      :value: None



   .. py:attribute:: join_complexity
      :type:  int
      :value: None



   .. py:attribute:: learning_curve
      :type:  str
      :value: None



   .. py:attribute:: parallelization_ratio
      :type:  float
      :value: None



   .. py:attribute:: research_components
      :type:  int
      :value: None



   .. py:attribute:: solution_confidence
      :type:  float
      :value: None



   .. py:attribute:: task_breadth
      :type:  int
      :value: None



   .. py:attribute:: task_depth
      :type:  int
      :value: None



   .. py:attribute:: total_subtasks
      :type:  int
      :value: None



   .. py:attribute:: unknown_requirements
      :type:  int
      :value: None



.. py:class:: ComplexityLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Overall complexity classification.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexityLevel
      :collapse:

   .. py:attribute:: COMPLEX
      :value: 'complex'



   .. py:attribute:: EXTREME
      :value: 'extreme'



   .. py:attribute:: HIGHLY_COMPLEX
      :value: 'highly_complex'



   .. py:attribute:: MODERATE
      :value: 'moderate'



   .. py:attribute:: SIMPLE
      :value: 'simple'



   .. py:attribute:: TRIVIAL
      :value: 'trivial'



.. py:class:: ComplexityVector(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Multi-dimensional complexity assessment.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexityVector
      :collapse:

   .. py:method:: determine_level() -> ComplexityLevel

      Determine overall complexity level from scores.


      .. autolink-examples:: determine_level
         :collapse:


   .. py:method:: total_score(weights: dict[str, float] | None = None) -> float

      Calculate weighted total complexity score.


      .. autolink-examples:: total_score
         :collapse:


   .. py:method:: validate_scores(v) -> float
      :classmethod:


      Ensure scores are within valid range.


      .. autolink-examples:: validate_scores
         :collapse:


   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: execution
      :type:  float
      :value: None



   .. py:attribute:: integration
      :type:  float
      :value: None



   .. py:attribute:: knowledge
      :type:  float
      :value: None



   .. py:attribute:: overall_level
      :type:  ComplexityLevel | None
      :value: None



   .. py:attribute:: structural
      :type:  float
      :value: None



   .. py:attribute:: uncertainty
      :type:  float
      :value: None



