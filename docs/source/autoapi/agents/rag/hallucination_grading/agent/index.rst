agents.rag.hallucination_grading.agent
======================================

.. py:module:: agents.rag.hallucination_grading.agent

.. autoapi-nested-parse::

   Hallucination Grading Agents.

   Modular agents for detecting and grading hallucinations in RAG responses.
   Can be plugged into any workflow with compatible I/O schemas.


   .. autolink-examples:: agents.rag.hallucination_grading.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.hallucination_grading.agent.ADVANCED_HALLUCINATION_PROMPT
   agents.rag.hallucination_grading.agent.BASIC_HALLUCINATION_PROMPT
   agents.rag.hallucination_grading.agent.REALTIME_HALLUCINATION_PROMPT
   agents.rag.hallucination_grading.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.hallucination_grading.agent.AdvancedHallucinationGrade
   agents.rag.hallucination_grading.agent.AdvancedHallucinationGraderAgent
   agents.rag.hallucination_grading.agent.HallucinationGrade
   agents.rag.hallucination_grading.agent.HallucinationGraderAgent
   agents.rag.hallucination_grading.agent.RealtimeHallucinationCheck
   agents.rag.hallucination_grading.agent.RealtimeHallucinationGraderAgent


Functions
---------

.. autoapisummary::

   agents.rag.hallucination_grading.agent.create_hallucination_grader
   agents.rag.hallucination_grading.agent.get_hallucination_grader_io_schema


Module Contents
---------------

.. py:class:: AdvancedHallucinationGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Advanced hallucination assessment with detailed analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdvancedHallucinationGrade
      :collapse:

   .. py:attribute:: action_needed
      :type:  Literal['none', 'review', 'revise', 'regenerate', 'reject']
      :value: None



   .. py:attribute:: contextual_consistency
      :type:  float
      :value: None



   .. py:attribute:: contradictions
      :type:  list[str]
      :value: None



   .. py:attribute:: detailed_reasoning
      :type:  str
      :value: None



   .. py:attribute:: fabricated_facts
      :type:  list[str]
      :value: None



   .. py:attribute:: factual_accuracy
      :type:  float
      :value: None



   .. py:attribute:: hallucination_types
      :type:  list[str]
      :value: None



   .. py:attribute:: has_hallucination
      :type:  bool
      :value: None



   .. py:attribute:: improvement_suggestions
      :type:  list[str]
      :value: None



   .. py:attribute:: logical_coherence
      :type:  float
      :value: None



   .. py:attribute:: overall_confidence
      :type:  float
      :value: None



   .. py:attribute:: severity_level
      :type:  Literal['none', 'low', 'medium', 'high', 'critical']
      :value: None



   .. py:attribute:: source_attribution
      :type:  float
      :value: None



   .. py:attribute:: unsupported_claims
      :type:  list[str]
      :value: None



.. py:class:: AdvancedHallucinationGraderAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_context_expansion: bool = True, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Advanced hallucination grading with detailed analysis.

   Initialize advanced hallucination grader.

   :param llm_config: LLM configuration
   :param enable_context_expansion: Whether to use additional context sources
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdvancedHallucinationGraderAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build advanced hallucination analysis graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: enable_context_expansion
      :value: True



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Advanced Hallucination Grader'



.. py:class:: HallucinationGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Single hallucination assessment.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationGrade
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: hallucination_type
      :type:  Literal['factual', 'contextual', 'logical', 'none']
      :value: None



   .. py:attribute:: has_hallucination
      :type:  bool
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: severity
      :type:  Literal['low', 'medium', 'high', 'critical']
      :value: None



.. py:class:: HallucinationGraderAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, threshold: float = 0.7, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Basic hallucination grading agent.

   Initialize hallucination grader.

   :param llm_config: LLM configuration
   :param threshold: Confidence threshold for flagging hallucinations
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationGraderAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build hallucination grading graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Hallucination Grader'



   .. py:attribute:: threshold
      :value: 0.7



.. py:class:: RealtimeHallucinationCheck(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Quick hallucination check for real-time applications.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RealtimeHallucinationCheck
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: is_safe
      :type:  bool
      :value: None



   .. py:attribute:: quick_flags
      :type:  list[str]
      :value: None



   .. py:attribute:: risk_level
      :type:  Literal['very_low', 'low', 'medium', 'high', 'very_high']
      :value: None



.. py:class:: RealtimeHallucinationGraderAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, safety_threshold: float = 0.8, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Fast hallucination checker for real-time applications.

   Initialize realtime hallucination grader.

   :param llm_config: LLM configuration
   :param safety_threshold: Threshold for considering response safe
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RealtimeHallucinationGraderAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build realtime hallucination check graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Realtime Hallucination Grader'



   .. py:attribute:: safety_threshold
      :value: 0.8



.. py:function:: create_hallucination_grader(grader_type: Literal['basic', 'advanced', 'realtime'] = 'basic', llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create a hallucination grader agent.

   :param grader_type: Type of grader to create
   :param llm_config: LLM configuration
   :param \*\*kwargs: Additional arguments

   :returns: Configured hallucination grader agent


   .. autolink-examples:: create_hallucination_grader
      :collapse:

.. py:function:: get_hallucination_grader_io_schema() -> dict[str, list[str]]

   Get I/O schema for hallucination graders for compatibility checking.


   .. autolink-examples:: get_hallucination_grader_io_schema
      :collapse:

.. py:data:: ADVANCED_HALLUCINATION_PROMPT

.. py:data:: BASIC_HALLUCINATION_PROMPT

.. py:data:: REALTIME_HALLUCINATION_PROMPT

.. py:data:: logger

