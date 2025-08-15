agents.rag.multi_agent_rag.specialized_workflows
================================================

.. py:module:: agents.rag.multi_agent_rag.specialized_workflows

.. autoapi-nested-parse::

   Specialized RAG Workflows - FLARE, Dynamic RAG, and Debate RAG.

   This module implements advanced RAG architectures including Forward-Looking Active REtrieval (FLARE),
   Dynamic RAG with add/remove retrievers, and Debate-based RAG for multi-perspective reasoning.


   .. autolink-examples:: agents.rag.multi_agent_rag.specialized_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows.AdaptiveThresholdRAGAgent
   agents.rag.multi_agent_rag.specialized_workflows.DebateRAGAgent
   agents.rag.multi_agent_rag.specialized_workflows.DebateRAGState
   agents.rag.multi_agent_rag.specialized_workflows.DynamicRAGAgent
   agents.rag.multi_agent_rag.specialized_workflows.DynamicRAGState
   agents.rag.multi_agent_rag.specialized_workflows.FLAREAgent
   agents.rag.multi_agent_rag.specialized_workflows.FLAREState


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows.build_custom_graph


Module Contents
---------------

.. py:class:: AdaptiveThresholdRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Adaptive Threshold RAG - dynamically adjusts retrieval thresholds.
   based on query difficulty and answer confidence.


   .. autolink-examples:: AdaptiveThresholdRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for Adaptive Threshold RAG workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: DebateRAGAgent(debate_positions: list[str] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Debate RAG - multiple agents with different perspectives debate.
   to reach a comprehensive answer through dialectical reasoning.


   .. autolink-examples:: DebateRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for Debate RAG workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _debate_positions
      :value: None



.. py:class:: DebateRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state for Debate-based RAG.


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



   .. py:attribute:: evidence_by_position
      :type:  dict[str, list[str]]


   .. py:attribute:: final_answer
      :type:  str
      :value: ''



   .. py:attribute:: synthesis_attempts
      :type:  list[str]
      :value: []



.. py:class:: DynamicRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Dynamic RAG with add/remove retrievers - adapts retrieval strategy.
   based on query characteristics and retriever performance.


   .. autolink-examples:: DynamicRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for Dynamic RAG workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: DynamicRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state for Dynamic RAG with configurable retrievers.


   .. autolink-examples:: DynamicRAGState
      :collapse:

   .. py:attribute:: active_retrievers
      :type:  dict[str, dict[str, Any]]


   .. py:attribute:: adaptive_threshold
      :type:  float
      :value: 0.7



   .. py:attribute:: document_sources
      :type:  dict[str, list[str]]


   .. py:attribute:: retriever_configurations
      :type:  dict[str, Any]


   .. py:attribute:: retriever_performance
      :type:  dict[str, float]


.. py:class:: FLAREAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Forward-Looking Active REtrieval (FLARE) - generates text while actively.
   predicting when retrieval would be beneficial.


   .. autolink-examples:: FLAREAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for FLARE workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: FLAREState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state for Forward-Looking Active REtrieval.


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



   .. py:attribute:: retrieval_triggers
      :type:  list[str]
      :value: []



   .. py:attribute:: uncertainty_tokens
      :type:  list[str]
      :value: []



.. py:function:: build_custom_graph() -> Any

   Build custom graph for specialized workflows.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

