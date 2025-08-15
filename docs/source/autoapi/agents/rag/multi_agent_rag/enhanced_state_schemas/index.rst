agents.rag.multi_agent_rag.enhanced_state_schemas
=================================================

.. py:module:: agents.rag.multi_agent_rag.enhanced_state_schemas

.. autoapi-nested-parse::

   Enhanced State Schemas with Configuration Support.

   This module provides state schemas that include configuration fields,
   solving the issue of storing agent-specific configuration in a clean way.


   .. autolink-examples:: agents.rag.multi_agent_rag.enhanced_state_schemas
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_state_schemas.AdaptiveThresholdRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.ConfigurableRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.DebateRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.DynamicRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.FLAREState
   agents.rag.multi_agent_rag.enhanced_state_schemas.GradedRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_state_schemas.create_configured_state


Module Contents
---------------

.. py:class:: AdaptiveThresholdRAGState

   Bases: :py:obj:`DynamicRAGState`


   Adaptive threshold state extending Dynamic RAG state.


   .. autolink-examples:: AdaptiveThresholdRAGState
      :collapse:

   .. py:attribute:: initial_threshold
      :type:  float
      :value: None



   .. py:attribute:: max_threshold
      :type:  float
      :value: None



   .. py:attribute:: min_threshold
      :type:  float
      :value: None



   .. py:attribute:: query_complexity_score
      :type:  float
      :value: 0.0



   .. py:attribute:: retrieval_rounds
      :type:  int
      :value: 0



   .. py:attribute:: threshold_adjustments
      :type:  list[float]
      :value: []



   .. py:attribute:: threshold_step
      :type:  float
      :value: None



.. py:class:: ConfigurableRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   Base RAG state with configuration support.


   .. autolink-examples:: ConfigurableRAGState
      :collapse:

   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: max_documents
      :type:  int
      :value: None



   .. py:attribute:: relevance_threshold
      :type:  float
      :value: None



   .. py:attribute:: workflow_type
      :type:  str
      :value: None



.. py:class:: DebateRAGState

   Bases: :py:obj:`ConfigurableRAGState`


   Debate RAG state with configuration support.


   .. autolink-examples:: DebateRAGState
      :collapse:

   .. py:attribute:: arguments_by_position
      :type:  dict[str, list[str]]


   .. py:attribute:: consensus_reached
      :type:  bool
      :value: False



   .. py:attribute:: debate_positions
      :type:  dict[str, str]


   .. py:attribute:: debate_rounds
      :type:  int
      :value: 0



   .. py:attribute:: debate_winner
      :type:  str | None
      :value: None



   .. py:attribute:: enable_judge
      :type:  bool
      :value: None



   .. py:attribute:: evidence_by_position
      :type:  dict[str, list[str]]


   .. py:attribute:: final_answer
      :type:  str
      :value: ''



   .. py:attribute:: max_debate_rounds
      :type:  int
      :value: None



   .. py:attribute:: position_names
      :type:  list[str]
      :value: None



   .. py:attribute:: require_consensus
      :type:  bool
      :value: None



   .. py:attribute:: synthesis_attempts
      :type:  list[str]
      :value: []



.. py:class:: DynamicRAGState

   Bases: :py:obj:`ConfigurableRAGState`


   Dynamic RAG state with configuration support.


   .. autolink-examples:: DynamicRAGState
      :collapse:

   .. py:attribute:: active_retrievers
      :type:  dict[str, dict[str, Any]]


   .. py:attribute:: adaptive_threshold
      :type:  float
      :value: 0.7



   .. py:attribute:: document_sources
      :type:  dict[str, list[str]]


   .. py:attribute:: max_retrievers
      :type:  int
      :value: None



   .. py:attribute:: min_retrievers
      :type:  int
      :value: None



   .. py:attribute:: performance_threshold
      :type:  float
      :value: None



   .. py:attribute:: retriever_configurations
      :type:  dict[str, Any]


   .. py:attribute:: retriever_performance
      :type:  dict[str, float]


.. py:class:: FLAREState

   Bases: :py:obj:`ConfigurableRAGState`


   FLARE state with configuration support.


   .. autolink-examples:: FLAREState
      :collapse:

   .. py:attribute:: active_retrieval_points
      :type:  list[int]
      :value: []



   .. py:attribute:: confidence_scores
      :type:  list[float]
      :value: []



   .. py:attribute:: current_generation
      :type:  str
      :value: ''



   .. py:attribute:: generation_segments
      :type:  list[str]
      :value: []



   .. py:attribute:: max_retrieval_rounds
      :type:  int
      :value: None



   .. py:attribute:: retrieval_triggers
      :type:  list[str]
      :value: []



   .. py:attribute:: uncertainty_threshold
      :type:  float
      :value: None



   .. py:attribute:: uncertainty_tokens
      :type:  list[str]
      :value: []



.. py:class:: GradedRAGState

   Bases: :py:obj:`ConfigurableRAGState`


   RAG state with grading information and configuration.


   .. autolink-examples:: GradedRAGState
      :collapse:

   .. py:attribute:: answer_grade
      :type:  haive.agents.rag.multi_agent_rag.grading_components.AnswerGrade | None
      :value: None



   .. py:attribute:: document_grades
      :type:  list[haive.agents.rag.multi_agent_rag.grading_components.DocumentGrade]
      :value: []



   .. py:attribute:: filtered_documents
      :type:  list[str]
      :value: []



   .. py:attribute:: grading_criteria
      :type:  list[str]
      :value: None



   .. py:attribute:: grading_weights
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: hallucination_grade
      :type:  haive.agents.rag.multi_agent_rag.grading_components.HallucinationGrade | None
      :value: None



   .. py:attribute:: improvement_suggestions
      :type:  list[str]
      :value: []



   .. py:attribute:: key_entities
      :type:  list[str]
      :value: []



   .. py:attribute:: overall_score
      :type:  float
      :value: 0.0



   .. py:attribute:: priority_ranking
      :type:  dict[str, float]


   .. py:attribute:: query_complexity
      :type:  str
      :value: ''



   .. py:attribute:: query_type
      :type:  str
      :value: ''



.. py:class:: StateConfigMixin

   Mixin to help MultiAgent classes work with configured states.


   .. autolink-examples:: StateConfigMixin
      :collapse:

   .. py:method:: get_state_config(state: ConfigurableRAGState) -> dict[str, Any]

      Extract configuration from state.


      .. autolink-examples:: get_state_config
         :collapse:


   .. py:method:: update_state_config(state: ConfigurableRAGState, **updates) -> None

      Update configuration in state.


      .. autolink-examples:: update_state_config
         :collapse:


.. py:function:: create_configured_state(state_class: type[ConfigurableRAGState], agent_name: str, workflow_type: str, **config_kwargs) -> ConfigurableRAGState

   Create a state instance with configuration.


   .. autolink-examples:: create_configured_state
      :collapse:

