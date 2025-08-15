models.task_analysis.solvability
================================

.. py:module:: models.task_analysis.solvability

.. autoapi-nested-parse::

   Task solvability and readiness assessment.

   This module analyzes whether tasks are currently solvable, what barriers exist,
   and what would be required to make unsolvable tasks solvable.


   .. autolink-examples:: models.task_analysis.solvability
      :collapse:


Classes
-------

.. autoapisummary::

   models.task_analysis.solvability.SolvabilityAssessment
   models.task_analysis.solvability.SolvabilityBarrier


Module Contents
---------------

.. py:class:: SolvabilityAssessment(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive assessment of task solvability and readiness.

   Analyzes whether a task can be solved with current capabilities,
   what barriers exist, and what would be required to overcome them.

   .. attribute:: solvability_status

      Current solvability classification

   .. attribute:: is_currently_solvable

      Whether task can be solved right now

   .. attribute:: confidence_level

      Confidence in the solvability assessment

   .. attribute:: primary_barriers

      Main obstacles preventing solution

   .. attribute:: secondary_barriers

      Additional challenges that may arise

   .. attribute:: enabling_factors

      Factors that make the task more solvable

   .. attribute:: breakthrough_requirements

      What breakthroughs would be needed

   .. attribute:: estimated_time_to_solvable

      Time until task becomes solvable

   .. attribute:: alternative_approaches

      Possible alternative solution paths

   .. rubric:: Example

   .. code-block:: python

       # Simple factual lookup - highly solvable
       assessment = SolvabilityAssessment(
       solvability_status=SolvabilityStatus.READY,
       is_currently_solvable=True,
       confidence_level=0.95,
       primary_barriers=[],
       enabling_factors=["web_search", "public_databases"],
       estimated_time_to_solvable=timedelta(0)
       )

       # Cancer cure - major breakthrough required
       assessment = SolvabilityAssessment(
       solvability_status=SolvabilityStatus.THEORETICAL,
       is_currently_solvable=False,
       confidence_level=0.7,
       primary_barriers=[
       SolvabilityBarrier.KNOWLEDGE_GAP,
       SolvabilityBarrier.TECHNOLOGY_LIMITATION,
       SolvabilityBarrier.RESOURCE_CONSTRAINT
       ],
       breakthrough_requirements=[
       "fundamental_understanding_of_cancer_biology",
       "advanced_genetic_engineering_tools",
       "personalized_medicine_capabilities"
       ],
       estimated_time_to_solvable=timedelta(days=7300)  # ~20 years
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SolvabilityAssessment
      :collapse:

   .. py:method:: estimate_breakthrough_timeline() -> dict[str, Any]

      Estimate timeline for required breakthroughs.

      :returns: Dictionary with breakthrough timeline analysis


      .. autolink-examples:: estimate_breakthrough_timeline
         :collapse:


   .. py:method:: generate_solvability_report() -> str

      Generate a comprehensive solvability report.

      :returns: Formatted report string


      .. autolink-examples:: generate_solvability_report
         :collapse:


   .. py:method:: get_addressable_barriers() -> list[SolvabilityBarrier]

      Get barriers that could potentially be addressed.

      :returns: List of barriers that might be overcome


      .. autolink-examples:: get_addressable_barriers
         :collapse:


   .. py:method:: get_immediate_actions() -> list[str]

      Get recommended immediate actions to improve solvability.

      :returns: List of actionable recommendations


      .. autolink-examples:: get_immediate_actions
         :collapse:


   .. py:method:: get_solvability_score() -> float

      Get solvability as a normalized score (0.0-1.0).

      :returns: Normalized solvability score


      .. autolink-examples:: get_solvability_score
         :collapse:


   .. py:method:: has_showstopper_barriers() -> bool

      Check if task has barriers that are absolute showstoppers.

      :returns: True if task has insurmountable barriers


      .. autolink-examples:: has_showstopper_barriers
         :collapse:


   .. py:method:: validate_solvability_consistency() -> SolvabilityAssessment

      Validate that solvability assessment is internally consistent.

      :returns: Self if validation passes

      :raises ValueError: If assessment has inconsistencies


      .. autolink-examples:: validate_solvability_consistency
         :collapse:


   .. py:attribute:: alternative_approaches
      :type:  list[str]
      :value: None



   .. py:attribute:: breakthrough_requirements
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence_level
      :type:  float
      :value: None



   .. py:attribute:: enabling_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: estimated_time_to_solvable
      :type:  datetime.timedelta | None
      :value: None



   .. py:attribute:: is_currently_solvable
      :type:  bool
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: primary_barriers
      :type:  list[SolvabilityBarrier]
      :value: None



   .. py:attribute:: secondary_barriers
      :type:  list[SolvabilityBarrier]
      :value: None



   .. py:attribute:: solvability_status
      :type:  haive.agents.common.models.task_analysis.base.SolvabilityStatus
      :value: None



   .. py:attribute:: success_probability
      :type:  float
      :value: None



.. py:class:: SolvabilityBarrier

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of barriers that prevent task solvability.

   .. attribute:: KNOWLEDGE_GAP

      Missing fundamental knowledge or understanding

   .. attribute:: TECHNOLOGY_LIMITATION

      Current technology is insufficient

   .. attribute:: RESOURCE_CONSTRAINT

      Insufficient computational, financial, or material resources

   .. attribute:: THEORETICAL_IMPOSSIBILITY

      Task violates known physical or logical laws

   .. attribute:: REGULATORY_BARRIER

      Legal, ethical, or regulatory constraints

   .. attribute:: COORDINATION_COMPLEXITY

      Too complex to coordinate effectively

   .. attribute:: TIME_CONSTRAINT

      Not enough time available given current methods

   .. attribute:: DATA_UNAVAILABILITY

      Required data doesn't exist or isn't accessible

   .. attribute:: EXPERT_UNAVAILABILITY

      Required human expertise not available

   .. attribute:: INFRASTRUCTURE_LIMITATION

      Missing necessary infrastructure or systems

   .. attribute:: ETHICAL_CONCERN

      Ethical issues prevent pursuit of solution

   .. attribute:: SAFETY_RISK

      Safety risks are too high to attempt

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SolvabilityBarrier
      :collapse:

   .. py:attribute:: COORDINATION_COMPLEXITY
      :value: 'coordination_complexity'



   .. py:attribute:: DATA_UNAVAILABILITY
      :value: 'data_unavailability'



   .. py:attribute:: ETHICAL_CONCERN
      :value: 'ethical_concern'



   .. py:attribute:: EXPERT_UNAVAILABILITY
      :value: 'expert_unavailability'



   .. py:attribute:: INFRASTRUCTURE_LIMITATION
      :value: 'infrastructure_limitation'



   .. py:attribute:: KNOWLEDGE_GAP
      :value: 'knowledge_gap'



   .. py:attribute:: REGULATORY_BARRIER
      :value: 'regulatory_barrier'



   .. py:attribute:: RESOURCE_CONSTRAINT
      :value: 'resource_constraint'



   .. py:attribute:: SAFETY_RISK
      :value: 'safety_risk'



   .. py:attribute:: TECHNOLOGY_LIMITATION
      :value: 'technology_limitation'



   .. py:attribute:: THEORETICAL_IMPOSSIBILITY
      :value: 'theoretical_impossibility'



   .. py:attribute:: TIME_CONSTRAINT
      :value: 'time_constraint'



