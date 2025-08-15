agents.rag.self_reflective.agent
================================

.. py:module:: agents.rag.self_reflective.agent

.. autoapi-nested-parse::

   Self-Reflective Agentic RAG Agent.

   from typing import Any
   Implementation of self-reflective RAG with critique and iterative improvement.
   Uses reflection loops to assess and enhance answer quality.


   .. autolink-examples:: agents.rag.self_reflective.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.self_reflective.agent.ANSWER_IMPROVEMENT_PROMPT
   agents.rag.self_reflective.agent.IMPROVEMENT_PLANNING_PROMPT
   agents.rag.self_reflective.agent.INITIAL_ANSWER_PROMPT
   agents.rag.self_reflective.agent.REFLECTION_CRITIQUE_PROMPT
   agents.rag.self_reflective.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.self_reflective.agent.ImprovedAnswer
   agents.rag.self_reflective.agent.ReflectionCritique
   agents.rag.self_reflective.agent.ReflectionPlan
   agents.rag.self_reflective.agent.ReflectionType
   agents.rag.self_reflective.agent.SelfReflectiveRAGAgent
   agents.rag.self_reflective.agent.SelfReflectiveResult


Functions
---------

.. autoapisummary::

   agents.rag.self_reflective.agent.create_self_reflective_rag_agent
   agents.rag.self_reflective.agent.get_self_reflective_rag_io_schema


Module Contents
---------------

.. py:class:: ImprovedAnswer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of answer improvement iteration.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ImprovedAnswer
      :collapse:

   .. py:attribute:: changes_made
      :type:  list[str]
      :value: None



   .. py:attribute:: clarifications_added
      :type:  list[str]
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: improved_answer
      :type:  str
      :value: None



   .. py:attribute:: improvement_delta
      :type:  float
      :value: None



   .. py:attribute:: iteration_number
      :type:  int
      :value: None



   .. py:attribute:: new_evidence_added
      :type:  list[str]
      :value: None



   .. py:attribute:: quality_score
      :type:  float
      :value: None



   .. py:attribute:: remaining_issues
      :type:  list[str]
      :value: None



.. py:class:: ReflectionCritique(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured critique from reflection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionCritique
      :collapse:

   .. py:attribute:: current_score
      :type:  float
      :value: None



   .. py:attribute:: estimated_improvement
      :type:  float
      :value: None



   .. py:attribute:: improvement_priority
      :type:  float
      :value: None



   .. py:attribute:: improvement_suggestions
      :type:  list[str]
      :value: None



   .. py:attribute:: issues_found
      :type:  list[str]
      :value: None



   .. py:attribute:: missing_elements
      :type:  list[str]
      :value: None



   .. py:attribute:: reflection_type
      :type:  ReflectionType
      :value: None



   .. py:attribute:: requires_more_retrieval
      :type:  bool
      :value: None



   .. py:attribute:: requires_rephrasing
      :type:  bool
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: None



.. py:class:: ReflectionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Plan for iterative improvement based on reflection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionPlan
      :collapse:

   .. py:attribute:: confidence_in_plan
      :type:  float
      :value: None



   .. py:attribute:: critical_issues
      :type:  list[str]
      :value: None



   .. py:attribute:: critiques
      :type:  list[ReflectionCritique]
      :value: None



   .. py:attribute:: focus_areas
      :type:  list[str]
      :value: None



   .. py:attribute:: improvement_actions
      :type:  list[str]
      :value: None



   .. py:attribute:: improvement_strategy
      :type:  str
      :value: None



   .. py:attribute:: iteration_number
      :type:  int
      :value: None



   .. py:attribute:: needs_improvement
      :type:  bool
      :value: None



   .. py:attribute:: overall_quality
      :type:  float
      :value: None



   .. py:attribute:: retrieval_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: termination_reason
      :type:  str
      :value: None



.. py:class:: ReflectionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of reflection analysis.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionType
      :collapse:

   .. py:attribute:: ACCURACY
      :value: 'accuracy'



   .. py:attribute:: CLARITY
      :value: 'clarity'



   .. py:attribute:: COMPLETENESS
      :value: 'completeness'



   .. py:attribute:: CONSISTENCY
      :value: 'consistency'



   .. py:attribute:: EVIDENCE
      :value: 'evidence'



   .. py:attribute:: RELEVANCE
      :value: 'relevance'



.. py:class:: SelfReflectiveRAGAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Self-Reflective RAG agent with iterative improvement capabilities.

   This agent uses conditional edges to iterate through reflection loops.


   .. autolink-examples:: SelfReflectiveRAGAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the self-reflective graph with conditional edges.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, max_iterations: int = 3, quality_threshold: float = 0.85, **kwargs)
      :classmethod:


      Create Self-Reflective RAG agent from documents.

      :param documents: Documents to index for retrieval
      :param llm_config: LLM configuration
      :param max_iterations: Maximum reflection iterations
      :param quality_threshold: Quality threshold to stop iterating
      :param \*\*kwargs: Additional arguments

      :returns: SelfReflectiveRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: generate_initial_answer(state: dict[str, Any]) -> dict[str, Any]

      Generate initial answer.


      .. autolink-examples:: generate_initial_answer
         :collapse:


   .. py:method:: improve_answer(state: dict[str, Any]) -> dict[str, Any]

      Improve the answer based on reflection.


      .. autolink-examples:: improve_answer
         :collapse:


   .. py:method:: reflect_and_critique(state: dict[str, Any]) -> dict[str, Any]

      Generate critiques and plan improvements.


      .. autolink-examples:: reflect_and_critique
         :collapse:


   .. py:method:: setup_agent() -> None

      Initialize engines.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: should_continue_improving(state: dict[str, Any]) -> str

      Determine if improvement should continue.


      .. autolink-examples:: should_continue_improving
         :collapse:


   .. py:method:: synthesize_result(state: dict[str, Any]) -> dict[str, Any]

      Create final self-reflective result.


      .. autolink-examples:: synthesize_result
         :collapse:


   .. py:attribute:: critique_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: improvement_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: initial_answer_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Self-Reflective RAG Agent'



   .. py:attribute:: planning_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: quality_threshold
      :type:  float
      :value: None



   .. py:attribute:: synthesis_engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



.. py:class:: SelfReflectiveResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete result from self-reflective RAG process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelfReflectiveResult
      :collapse:

   .. py:attribute:: additional_retrievals
      :type:  int
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: final_quality
      :type:  float
      :value: None



   .. py:attribute:: initial_quality
      :type:  float
      :value: None



   .. py:attribute:: initial_retrievals
      :type:  int
      :value: None



   .. py:attribute:: iteration_history
      :type:  list[ImprovedAnswer]
      :value: None



   .. py:attribute:: iterations_performed
      :type:  int
      :value: None



   .. py:attribute:: most_effective_improvements
      :type:  list[str]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: persistent_challenges
      :type:  list[str]
      :value: None



   .. py:attribute:: processing_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: reflection_history
      :type:  list[ReflectionPlan]
      :value: None



   .. py:attribute:: termination_reason
      :type:  str
      :value: None



   .. py:attribute:: total_improvement
      :type:  float
      :value: None



   .. py:attribute:: unique_sources_used
      :type:  int
      :value: None



.. py:function:: create_self_reflective_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, reflection_mode: str = 'thorough', **kwargs) -> SelfReflectiveRAGAgent

   Create a Self-Reflective RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param reflection_mode: Mode ("quick", "balanced", "thorough")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Self-Reflective RAG agent


   .. autolink-examples:: create_self_reflective_rag_agent
      :collapse:

.. py:function:: get_self_reflective_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Self-Reflective RAG agents.


   .. autolink-examples:: get_self_reflective_rag_io_schema
      :collapse:

.. py:data:: ANSWER_IMPROVEMENT_PROMPT

.. py:data:: IMPROVEMENT_PLANNING_PROMPT

.. py:data:: INITIAL_ANSWER_PROMPT

.. py:data:: REFLECTION_CRITIQUE_PROMPT

.. py:data:: logger

