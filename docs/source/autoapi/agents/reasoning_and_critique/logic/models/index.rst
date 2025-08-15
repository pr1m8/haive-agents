agents.reasoning_and_critique.logic.models
==========================================

.. py:module:: agents.reasoning_and_critique.logic.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.logic.models.ArgumentStrength
   agents.reasoning_and_critique.logic.models.ArgumentStructure
   agents.reasoning_and_critique.logic.models.Assumption
   agents.reasoning_and_critique.logic.models.BiasAssessment
   agents.reasoning_and_critique.logic.models.BiasType
   agents.reasoning_and_critique.logic.models.CertaintyLevel
   agents.reasoning_and_critique.logic.models.CounterArgument
   agents.reasoning_and_critique.logic.models.Evidence
   agents.reasoning_and_critique.logic.models.EvidenceType
   agents.reasoning_and_critique.logic.models.FallacyDetection
   agents.reasoning_and_critique.logic.models.LogicalFallacy
   agents.reasoning_and_critique.logic.models.LogicalStep
   agents.reasoning_and_critique.logic.models.Premise
   agents.reasoning_and_critique.logic.models.ReasoningAnalysis
   agents.reasoning_and_critique.logic.models.ReasoningChain
   agents.reasoning_and_critique.logic.models.ReasoningQuality
   agents.reasoning_and_critique.logic.models.ReasoningReport
   agents.reasoning_and_critique.logic.models.ReasoningType
   agents.reasoning_and_critique.logic.models.UncertaintyAnalysis


Module Contents
---------------

.. py:class:: ArgumentStrength

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Strength of logical arguments.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ArgumentStrength
      :collapse:

   .. py:attribute:: CONCLUSIVE
      :value: 'conclusive'



   .. py:attribute:: FALLACIOUS
      :value: 'fallacious'



   .. py:attribute:: MODERATE
      :value: 'moderate'



   .. py:attribute:: STRONG
      :value: 'strong'



   .. py:attribute:: VERY_STRONG
      :value: 'very_strong'



   .. py:attribute:: VERY_WEAK
      :value: 'very_weak'



   .. py:attribute:: WEAK
      :value: 'weak'



.. py:class:: ArgumentStructure(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structure analysis of an argument.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ArgumentStructure
      :collapse:

   .. py:attribute:: breadth
      :type:  int
      :value: None



   .. py:attribute:: circular_dependencies
      :type:  list[list[int]]
      :value: None



   .. py:attribute:: critical_premises
      :type:  list[int]
      :value: None



   .. py:attribute:: depth
      :type:  int
      :value: None



   .. py:attribute:: premise_count
      :type:  int
      :value: None



   .. py:attribute:: premise_dependencies
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: reasoning_patterns
      :type:  list[str]
      :value: None



   .. py:attribute:: structure_type
      :type:  Literal['deductive', 'inductive', 'abductive', 'analogical', 'pragmatic', 'mixed']
      :value: None



.. py:class:: Assumption(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An assumption made during reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Assumption
      :collapse:

   .. py:attribute:: alternatives
      :type:  list[str]
      :value: None



   .. py:attribute:: impact
      :type:  Literal['critical', 'significant', 'moderate', 'minor']
      :value: None



   .. py:attribute:: justification
      :type:  str
      :value: None



   .. py:attribute:: statement
      :type:  str
      :value: None



   .. py:attribute:: testable
      :type:  bool
      :value: None



.. py:class:: BiasAssessment(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Assessment of potential biases.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BiasAssessment
      :collapse:

   .. py:attribute:: bias_type
      :type:  BiasType


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: mitigation
      :type:  str
      :value: None



   .. py:attribute:: severity
      :type:  Literal['high', 'medium', 'low']
      :value: None



.. py:class:: BiasType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Common cognitive biases that affect reasoning.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BiasType
      :collapse:

   .. py:attribute:: ANCHORING
      :value: 'anchoring'



   .. py:attribute:: AVAILABILITY
      :value: 'availability'



   .. py:attribute:: CONFIRMATION
      :value: 'confirmation'



   .. py:attribute:: DUNNING_KRUGER
      :value: 'dunning_kruger'



   .. py:attribute:: FRAMING
      :value: 'framing'



   .. py:attribute:: HINDSIGHT
      :value: 'hindsight'



   .. py:attribute:: SELECTION
      :value: 'selection'



   .. py:attribute:: SUNK_COST
      :value: 'sunk_cost'



.. py:class:: CertaintyLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Degree of certainty in conclusions.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CertaintyLevel
      :collapse:

   .. py:attribute:: CERTAIN
      :value: 'certain'



   .. py:attribute:: HIGHLY_LIKELY
      :value: 'highly_likely'



   .. py:attribute:: HIGHLY_UNLIKELY
      :value: 'highly_unlikely'



   .. py:attribute:: IMPOSSIBLE
      :value: 'impossible'



   .. py:attribute:: LIKELY
      :value: 'likely'



   .. py:attribute:: POSSIBLE
      :value: 'possible'



   .. py:attribute:: UNLIKELY
      :value: 'unlikely'



.. py:class:: CounterArgument(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A counter-argument to consider.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CounterArgument
      :collapse:

   .. py:attribute:: argument
      :type:  str
      :value: None



   .. py:attribute:: rebuttal
      :type:  str | None
      :value: None



   .. py:attribute:: strength
      :type:  ArgumentStrength
      :value: None



   .. py:attribute:: unresolved
      :type:  bool
      :value: None



.. py:class:: Evidence(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Evidence supporting a claim or premise.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Evidence
      :collapse:

   .. py:attribute:: date_collected
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: evidence_type
      :type:  EvidenceType


   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: relevance
      :type:  float
      :value: None



   .. py:attribute:: reliability
      :type:  float
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: strength
      :type:  ArgumentStrength
      :value: None



.. py:class:: EvidenceType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of evidence that support reasoning.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceType
      :collapse:

   .. py:attribute:: ANALOGICAL
      :value: 'analogical'



   .. py:attribute:: DOCUMENTARY
      :value: 'documentary'



   .. py:attribute:: EMPIRICAL
      :value: 'empirical'



   .. py:attribute:: EXPERIENTIAL
      :value: 'experiential'



   .. py:attribute:: LOGICAL
      :value: 'logical'



   .. py:attribute:: STATISTICAL
      :value: 'statistical'



   .. py:attribute:: TESTIMONIAL
      :value: 'testimonial'



   .. py:attribute:: THEORETICAL
      :value: 'theoretical'



.. py:class:: FallacyDetection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Detection of logical fallacies.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FallacyDetection
      :collapse:

   .. py:attribute:: correction
      :type:  str
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: fallacy_type
      :type:  LogicalFallacy


   .. py:attribute:: impact
      :type:  ArgumentStrength
      :value: None



   .. py:attribute:: location
      :type:  str
      :value: None



.. py:class:: LogicalFallacy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Common logical fallacies to detect.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LogicalFallacy
      :collapse:

   .. py:attribute:: AD_HOMINEM
      :value: 'ad_hominem'



   .. py:attribute:: APPEAL_TO_AUTHORITY
      :value: 'appeal_to_authority'



   .. py:attribute:: BANDWAGON
      :value: 'bandwagon'



   .. py:attribute:: CIRCULAR_REASONING
      :value: 'circular_reasoning'



   .. py:attribute:: FALSE_CAUSE
      :value: 'false_cause'



   .. py:attribute:: FALSE_DILEMMA
      :value: 'false_dilemma'



   .. py:attribute:: HASTY_GENERALIZATION
      :value: 'hasty_generalization'



   .. py:attribute:: POST_HOC
      :value: 'post_hoc'



   .. py:attribute:: SLIPPERY_SLOPE
      :value: 'slippery_slope'



   .. py:attribute:: STRAW_MAN
      :value: 'straw_man'



.. py:class:: LogicalStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A single step in a reasoning chain.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LogicalStep
      :collapse:

   .. py:attribute:: alternative_conclusions
      :type:  list[str]
      :value: None



   .. py:attribute:: conclusion
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: from_premises
      :type:  list[int]
      :value: None



   .. py:attribute:: inference_rule
      :type:  str
      :value: None



   .. py:attribute:: reasoning_type
      :type:  ReasoningType
      :value: None



   .. py:attribute:: step_number
      :type:  int
      :value: None



.. py:class:: Premise(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A single premise in a logical argument.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Premise
      :collapse:

   .. py:attribute:: certainty
      :type:  CertaintyLevel
      :value: None



   .. py:attribute:: evidence
      :type:  list[Evidence]
      :value: None



   .. py:attribute:: is_contested
      :type:  bool
      :value: None



   .. py:attribute:: premise_type
      :type:  Literal['fact', 'assumption', 'axiom', 'hypothesis']
      :value: None



   .. py:attribute:: source
      :type:  str | None
      :value: None



   .. py:attribute:: statement
      :type:  str
      :value: None



.. py:class:: ReasoningAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete analysis of a reasoning chain.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningAnalysis
      :collapse:

   .. py:attribute:: additional_evidence_needed
      :type:  list[str]
      :value: None



   .. py:attribute:: alternative_framings
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: argument_structure
      :type:  ArgumentStructure
      :value: None



   .. py:attribute:: detected_biases
      :type:  list[BiasAssessment]
      :value: None



   .. py:attribute:: detected_fallacies
      :type:  list[FallacyDetection]
      :value: None



   .. py:attribute:: dialectical_synthesis
      :type:  str | None
      :value: None



   .. py:attribute:: missing_considerations
      :type:  list[str]
      :value: None



   .. py:attribute:: quality_assessment
      :type:  ReasoningQuality
      :value: None



   .. py:attribute:: reasoning_chain
      :type:  ReasoningChain
      :value: None



   .. py:attribute:: strengthening_suggestions
      :type:  list[str]
      :value: None



   .. py:attribute:: uncertainty_analysis
      :type:  UncertaintyAnalysis
      :value: None



.. py:class:: ReasoningChain(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A complete chain of reasoning from premises to conclusion.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningChain
      :collapse:

   .. py:attribute:: alternative_conclusions
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: assumptions
      :type:  list[Assumption]
      :value: None



   .. py:attribute:: certainty_level
      :type:  CertaintyLevel
      :value: None



   .. py:attribute:: chain_id
      :type:  str
      :value: None



   .. py:attribute:: completeness
      :type:  float
      :value: None



   .. py:attribute:: conclusion
      :type:  str
      :value: None



   .. py:attribute:: conclusion_strength
      :type:  ArgumentStrength
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: counter_arguments
      :type:  list[CounterArgument]
      :value: None



   .. py:attribute:: logical_steps
      :type:  list[LogicalStep]
      :value: None



   .. py:attribute:: logical_validity
      :type:  bool
      :value: None



   .. py:property:: max_inference_chain
      :type: int


      Longest chain of inferences.

      .. autolink-examples:: max_inference_chain
         :collapse:


   .. py:property:: num_steps
      :type: int


      Number of reasoning steps.

      .. autolink-examples:: num_steps
         :collapse:


   .. py:attribute:: premises
      :type:  list[Premise]
      :value: None



   .. py:attribute:: question
      :type:  str
      :value: None



   .. py:attribute:: soundness
      :type:  bool | None
      :value: None



.. py:class:: ReasoningQuality(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Overall quality assessment of reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningQuality
      :collapse:

   .. py:attribute:: alternative_exploration
      :type:  float
      :value: None



   .. py:attribute:: bias_score
      :type:  float
      :value: None



   .. py:attribute:: confidence_in_assessment
      :type:  float
      :value: None



   .. py:attribute:: consideration_breadth
      :type:  float
      :value: None



   .. py:attribute:: evidence_coverage
      :type:  float
      :value: None



   .. py:attribute:: evidence_quality
      :type:  float
      :value: None



   .. py:attribute:: fallacy_score
      :type:  float
      :value: None



   .. py:attribute:: overall_quality
      :type:  float
      :value: None



   .. py:attribute:: soundness_score
      :type:  float
      :value: None



   .. py:attribute:: validity_score
      :type:  float
      :value: None



.. py:class:: ReasoningReport(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive reasoning analysis report.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningReport
      :collapse:

   .. py:attribute:: alternative_chains
      :type:  list[ReasoningChain]
      :value: None



   .. py:attribute:: analysis
      :type:  ReasoningAnalysis
      :value: None



   .. py:attribute:: confidence_level
      :type:  CertaintyLevel
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: decision_recommendation
      :type:  str
      :value: None



   .. py:attribute:: executive_summary
      :type:  str
      :value: None



   .. py:attribute:: follow_up_questions
      :type:  list[str]
      :value: None



   .. py:attribute:: key_insights
      :type:  list[str]
      :value: None



   .. py:attribute:: key_uncertainties
      :type:  list[str]
      :value: None



   .. py:attribute:: primary_chain
      :type:  ReasoningChain
      :value: None



   .. py:attribute:: question
      :type:  str
      :value: None



   .. py:attribute:: synthesized_conclusion
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: ReasoningType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Fundamental patterns of reasoning.

   These represent core ways humans and AI systems process information:
   - DEDUCTIVE: From general principles to specific conclusions
   - INDUCTIVE: From specific observations to general principles
   - ABDUCTIVE: Best explanation for observations
   - ANALOGICAL: Reasoning by comparison/similarity
   - CAUSAL: Understanding cause-effect relationships
   - PROBABILISTIC: Reasoning under uncertainty
   - COUNTERFACTUAL: What-if analysis
   - DIALECTICAL: Thesis-antithesis-synthesis

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReasoningType
      :collapse:

   .. py:attribute:: ABDUCTIVE
      :value: 'abductive'



   .. py:attribute:: ANALOGICAL
      :value: 'analogical'



   .. py:attribute:: CAUSAL
      :value: 'causal'



   .. py:attribute:: COUNTERFACTUAL
      :value: 'counterfactual'



   .. py:attribute:: DEDUCTIVE
      :value: 'deductive'



   .. py:attribute:: DIALECTICAL
      :value: 'dialectical'



   .. py:attribute:: INDUCTIVE
      :value: 'inductive'



   .. py:attribute:: PROBABILISTIC
      :value: 'probabilistic'



.. py:class:: UncertaintyAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of uncertainty in reasoning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: UncertaintyAnalysis
      :collapse:

   .. py:attribute:: aleatory_uncertainty
      :type:  float
      :value: None



   .. py:attribute:: conclusion_uncertainty
      :type:  float
      :value: None



   .. py:attribute:: confidence_interval
      :type:  tuple[float, float]
      :value: None



   .. py:attribute:: epistemic_uncertainty
      :type:  float
      :value: None



   .. py:attribute:: inference_uncertainty
      :type:  dict[int, float]
      :value: None



   .. py:attribute:: premise_uncertainty
      :type:  dict[int, float]
      :value: None



   .. py:attribute:: robustness_score
      :type:  float
      :value: None



   .. py:attribute:: sensitive_assumptions
      :type:  list[str]
      :value: None



