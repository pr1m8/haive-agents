hallucination_graders
=====================

.. py:module:: hallucination_graders

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: hallucination_graders
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/hallucination_graders/models/index
   /autoapi/hallucination_graders/prompts/index


Classes
-------

.. autoapisummary::

   hallucination_graders.HallucinationBinaryResponse
   hallucination_graders.HallucinationClaim
   hallucination_graders.HallucinationDetectionResponse
   hallucination_graders.HallucinationType


Package Contents
----------------

.. py:class:: HallucinationBinaryResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Binary hallucination detection response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationBinaryResponse
      :collapse:

   .. py:attribute:: generated_answer
      :type:  str
      :value: None



   .. py:attribute:: hallucination_detected
      :type:  bool
      :value: None



   .. py:attribute:: justification
      :type:  str
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: severity_level
      :type:  Literal['none', 'minor', 'moderate', 'major', 'severe']
      :value: None



   .. py:attribute:: specific_issues
      :type:  list[str]
      :value: None



.. py:class:: HallucinationClaim(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual claim analysis for hallucination detection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationClaim
      :collapse:

   .. py:attribute:: claim
      :type:  str
      :value: None



   .. py:attribute:: hallucination_type
      :type:  HallucinationType | None
      :value: None



   .. py:attribute:: is_supported
      :type:  bool
      :value: None



   .. py:attribute:: severity
      :type:  float
      :value: None



   .. py:attribute:: source_reference
      :type:  str | None
      :value: None



   .. py:attribute:: support_type
      :type:  str
      :value: None



.. py:class:: HallucinationDetectionResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive hallucination detection response.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationDetectionResponse
      :collapse:

   .. py:attribute:: claim_analysis
      :type:  list[HallucinationClaim]
      :value: None



   .. py:attribute:: contradictory_claims
      :type:  list[str]
      :value: None



   .. py:attribute:: generated_answer
      :type:  str
      :value: None



   .. py:attribute:: overall_hallucination_score
      :type:  float
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: supported_claims
      :type:  list[str]
      :value: None



   .. py:attribute:: unsupported_claims
      :type:  list[str]
      :value: None



.. py:class:: HallucinationType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of hallucinations detected.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationType
      :collapse:

   .. py:attribute:: ATTRIBUTIONAL
      :value: 'attributional'



   .. py:attribute:: CAUSAL
      :value: 'causal'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: INFERENTIAL
      :value: 'inferential'



   .. py:attribute:: QUANTITATIVE
      :value: 'quantitative'



   .. py:attribute:: TEMPORAL
      :value: 'temporal'



