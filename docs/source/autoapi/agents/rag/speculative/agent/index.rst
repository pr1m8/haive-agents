agents.rag.speculative.agent
============================

.. py:module:: agents.rag.speculative.agent

.. autoapi-nested-parse::

   Speculative RAG Agents.

   from typing import Any
   Implementation of speculative RAG with parallel hypothesis generation and verification.
   Uses structured output models for hypothesis planning and iterative refinement.


   .. autolink-examples:: agents.rag.speculative.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.speculative.agent.HYPOTHESIS_GENERATION_PROMPT
   agents.rag.speculative.agent.HYPOTHESIS_VERIFICATION_PROMPT
   agents.rag.speculative.agent.SPECULATIVE_SYNTHESIS_PROMPT
   agents.rag.speculative.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.speculative.agent.Hypothesis
   agents.rag.speculative.agent.HypothesisConfidence
   agents.rag.speculative.agent.HypothesisGeneratorAgent
   agents.rag.speculative.agent.ParallelVerificationAgent
   agents.rag.speculative.agent.SpeculativeExecutionPlan
   agents.rag.speculative.agent.SpeculativeRAGAgent
   agents.rag.speculative.agent.SpeculativeResult
   agents.rag.speculative.agent.VerificationStatus


Functions
---------

.. autoapisummary::

   agents.rag.speculative.agent.create_speculative_rag_agent
   agents.rag.speculative.agent.get_speculative_rag_io_schema


Module Contents
---------------

.. py:class:: Hypothesis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual hypothesis with structured metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Hypothesis
      :collapse:

   .. py:attribute:: confidence
      :type:  HypothesisConfidence
      :value: None



   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: generation_method
      :type:  str
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: key_assumptions
      :type:  list[str]
      :value: None



   .. py:attribute:: plausibility
      :type:  float
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: related_hypotheses
      :type:  list[str]
      :value: None



   .. py:attribute:: required_evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: supporting_evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: text
      :type:  str
      :value: None



   .. py:attribute:: verification_complexity
      :type:  str
      :value: None



   .. py:attribute:: verification_criteria
      :type:  list[str]
      :value: None



   .. py:attribute:: verification_evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: verification_reasoning
      :type:  str | None
      :value: None



   .. py:attribute:: verification_score
      :type:  float | None
      :value: None



   .. py:attribute:: verification_status
      :type:  VerificationStatus
      :value: None



.. py:class:: HypothesisConfidence

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Confidence levels for hypotheses.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HypothesisConfidence
      :collapse:

   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: VERY_HIGH
      :value: 'very_high'



.. py:class:: HypothesisGeneratorAgent(llm_config: haive.core.models.llm.base.LLMConfig | None = None, num_hypotheses: int = 5, hypothesis_diversity: str = 'high', **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that generates multiple hypotheses for speculative reasoning.

   Initialize hypothesis generator.

   :param llm_config: LLM configuration
   :param num_hypotheses: Number of hypotheses to generate
   :param hypothesis_diversity: Diversity level ("low", "medium", "high")
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HypothesisGeneratorAgent
      :collapse:

   .. py:method:: _extract_domain_info(query: str) -> str

      Extract domain information for hypothesis generation.


      .. autolink-examples:: _extract_domain_info
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build hypothesis generation graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: hypothesis_diversity
      :value: 'high'



   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Hypothesis Generator'



   .. py:attribute:: num_hypotheses
      :value: 5



.. py:class:: ParallelVerificationAgent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, verification_depth: str = 'thorough', **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that performs parallel hypothesis verification.

   Initialize parallel verifier.

   :param documents: Documents for evidence gathering
   :param llm_config: LLM configuration
   :param verification_depth: Depth of verification ("basic", "thorough", "comprehensive")
   :param \*\*kwargs: Additional agent arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelVerificationAgent
      :collapse:

   .. py:method:: _gather_evidence_for_hypothesis(hypothesis: Hypothesis, query: str) -> str

      Gather evidence for hypothesis verification.


      .. autolink-examples:: _gather_evidence_for_hypothesis
         :collapse:


   .. py:method:: _verify_hypothesis_batch(hypotheses: list[Hypothesis], query: str) -> dict[str, Hypothesis]

      Verify a batch of hypotheses.


      .. autolink-examples:: _verify_hypothesis_batch
         :collapse:


   .. py:method:: _verify_single_hypothesis(hypothesis: Hypothesis, evidence: str, query: str) -> Hypothesis

      Verify a single hypothesis with evidence.


      .. autolink-examples:: _verify_single_hypothesis
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build parallel verification graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: base_retriever


   .. py:attribute:: documents


   .. py:attribute:: llm_config


   .. py:attribute:: name
      :type:  str
      :value: 'Parallel Verifier'



   .. py:attribute:: verification_depth
      :value: 'thorough'



.. py:class:: SpeculativeExecutionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Plan for executing speculative retrieval and verification.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SpeculativeExecutionPlan
      :collapse:

   .. py:attribute:: batch_size
      :type:  int
      :value: None



   .. py:attribute:: convergence_criteria
      :type:  str
      :value: None



   .. py:attribute:: evidence_gathering_depth
      :type:  str
      :value: None



   .. py:attribute:: execution_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: max_verification_rounds
      :type:  int
      :value: None



   .. py:attribute:: minimum_verification_score
      :type:  float
      :value: None



   .. py:attribute:: parallel_batches
      :type:  int
      :value: None



   .. py:attribute:: refinement_enabled
      :type:  bool
      :value: None



   .. py:attribute:: required_consensus_level
      :type:  float
      :value: None



   .. py:attribute:: time_budget_per_hypothesis
      :type:  str
      :value: None



   .. py:attribute:: total_hypotheses
      :type:  int
      :value: None



   .. py:attribute:: verification_strategy
      :type:  str
      :value: None



   .. py:attribute:: verification_thoroughness
      :type:  str
      :value: None



.. py:class:: SpeculativeRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete Speculative RAG agent with parallel hypothesis processing.


   .. autolink-examples:: SpeculativeRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, num_hypotheses: int = 5, verification_depth: str = 'thorough', **kwargs)
      :classmethod:


      Create Speculative RAG agent from documents.

      :param documents: Documents to index
      :param llm_config: LLM configuration
      :param num_hypotheses: Number of hypotheses to generate
      :param verification_depth: Depth of verification process
      :param \*\*kwargs: Additional arguments

      :returns: SpeculativeRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: SpeculativeResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Results from speculative RAG processing.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SpeculativeResult
      :collapse:

   .. py:attribute:: confidence_distribution
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: conflicting_evidence
      :type:  list[str]
      :value: None



   .. py:attribute:: consensus_level
      :type:  float
      :value: None



   .. py:attribute:: evidence_quality_score
      :type:  float
      :value: None



   .. py:attribute:: inconclusive_hypotheses
      :type:  list[Hypothesis]
      :value: None



   .. py:attribute:: key_insights
      :type:  list[str]
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: overall_confidence
      :type:  float
      :value: None



   .. py:attribute:: processing_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: refuted_hypotheses
      :type:  list[Hypothesis]
      :value: None



   .. py:attribute:: synthesized_answer
      :type:  str
      :value: None



   .. py:attribute:: total_hypotheses_generated
      :type:  int
      :value: None



   .. py:attribute:: verification_success_rate
      :type:  float
      :value: None



   .. py:attribute:: verified_hypotheses
      :type:  list[Hypothesis]
      :value: None



.. py:class:: VerificationStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of hypothesis verification.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: VerificationStatus
      :collapse:

   .. py:attribute:: INCONCLUSIVE
      :value: 'inconclusive'



   .. py:attribute:: NEEDS_MORE_DATA
      :value: 'needs_more_data'



   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: REFUTED
      :value: 'refuted'



   .. py:attribute:: VERIFIED
      :value: 'verified'



.. py:function:: create_speculative_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, speculation_mode: str = 'balanced', **kwargs) -> SpeculativeRAGAgent

   Create a Speculative RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param speculation_mode: Mode ("conservative", "balanced", "aggressive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Speculative RAG agent


   .. autolink-examples:: create_speculative_rag_agent
      :collapse:

.. py:function:: get_speculative_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Speculative RAG agents.


   .. autolink-examples:: get_speculative_rag_io_schema
      :collapse:

.. py:data:: HYPOTHESIS_GENERATION_PROMPT

.. py:data:: HYPOTHESIS_VERIFICATION_PROMPT

.. py:data:: SPECULATIVE_SYNTHESIS_PROMPT

.. py:data:: logger

