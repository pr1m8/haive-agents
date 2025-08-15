agents.rag.multi_agent_rag.multi_rag
====================================

.. py:module:: agents.rag.multi_agent_rag.multi_rag

.. autoapi-nested-parse::

   Multi-Agent RAG System Implementation.

   from typing import Any
   This module provides complete multi-agent RAG workflows using the multi-agent framework
   with conditional routing, sequential processing, and parallel execution patterns.


   .. autolink-examples:: agents.rag.multi_agent_rag.multi_rag
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.multi_rag.agent_list
   agents.rag.multi_agent_rag.multi_rag.base_rag_agent


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.multi_rag.AdaptiveRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.BaseRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.ConditionalRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.IterativeRAGMultiAgent
   agents.rag.multi_agent_rag.multi_rag.ParallelRAGMultiAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.multi_rag.create_conditional_rag_system
   agents.rag.multi_agent_rag.multi_rag.create_iterative_rag_system
   agents.rag.multi_agent_rag.multi_rag.create_sequential_rag_system
   agents.rag.multi_agent_rag.multi_rag.document_quality_check
   agents.rag.multi_agent_rag.multi_rag.should_grade_documents
   agents.rag.multi_agent_rag.multi_rag.should_refine_query
   agents.rag.multi_agent_rag.multi_rag.test_agent_compatibility
   agents.rag.multi_agent_rag.multi_rag.validate_multi_agent_compatibility


Module Contents
---------------

.. py:class:: AdaptiveRAGMultiAgent(simple_rag: BaseRAGMultiAgent | None = None, complex_rag: IterativeRAGMultiAgent | None = None, consensus_rag: ParallelRAGMultiAgent | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Advanced RAG system that adapts its strategy based on query complexity and results.

   This system demonstrates sophisticated conditional routing with multiple
   decision points and fallback strategies.


   .. autolink-examples:: AdaptiveRAGMultiAgent
      :collapse:

   .. py:method:: _setup_adaptive_routing()

      Set up adaptive routing based on query complexity and results.


      .. autolink-examples:: _setup_adaptive_routing
         :collapse:


   .. py:attribute:: complex_rag


   .. py:attribute:: consensus_rag


   .. py:attribute:: simple_rag


.. py:class:: BaseRAGMultiAgent(retrieval_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAgent | None = None, grading_agent: haive.agents.rag.multi_agent_rag.agents.DocumentGradingAgent | None = None, answer_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Base multi-agent RAG system with retrieve -> grade -> generate workflow.

   This is the simple sequential RAG agent as mentioned in the user prompt.


   .. autolink-examples:: BaseRAGMultiAgent
      :collapse:

.. py:class:: ConditionalRAGMultiAgent(retrieval_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAgent | None = None, grading_agent: haive.agents.rag.multi_agent_rag.agents.DocumentGradingAgent | None = None, answer_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent | None = None, query_refiner: Any | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Conditional multi-agent RAG system with smart routing based on document quality.

   This system uses conditional routing to decide whether to grade documents,
   refine queries, or generate answers based on the current state.


   .. autolink-examples:: ConditionalRAGMultiAgent
      :collapse:

   .. py:method:: _setup_conditional_routing()

      Set up conditional edges for smart routing.


      .. autolink-examples:: _setup_conditional_routing
         :collapse:


   .. py:attribute:: answer_agent


   .. py:attribute:: grading_agent


   .. py:attribute:: query_refiner
      :value: None



   .. py:attribute:: retrieval_agent


.. py:class:: IterativeRAGMultiAgent(retrieval_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAgent | None = None, iterative_grader: haive.agents.rag.multi_agent_rag.agents.IterativeDocumentGradingAgent | None = None, answer_agent: haive.agents.rag.multi_agent_rag.agents.SimpleRAGAnswerAgent | None = None, custom_grader_callable: collections.abc.Callable | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Multi-agent RAG system with iterative document processing.

   This system demonstrates iterating over retrieved documents and processing
   each one individually, as mentioned in the user prompt.


   .. autolink-examples:: IterativeRAGMultiAgent
      :collapse:

.. py:class:: ParallelRAGMultiAgent(rag_agents: list[BaseRAGMultiAgent] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ParallelAgent`


   Parallel multi-agent RAG system for consensus-based processing.

   This system runs multiple RAG agents in parallel and aggregates their results.


   .. autolink-examples:: ParallelRAGMultiAgent
      :collapse:

.. py:function:: create_conditional_rag_system(documents: list[langchain_core.documents.Document] | None = None, custom_grader: collections.abc.Callable | None = None) -> ConditionalRAGMultiAgent

   Create a conditional RAG system with smart routing.


   .. autolink-examples:: create_conditional_rag_system
      :collapse:

.. py:function:: create_iterative_rag_system(documents: list[langchain_core.documents.Document] | None = None, custom_grader: collections.abc.Callable | None = None) -> IterativeRAGMultiAgent

   Create an iterative RAG system with document-by-document processing.


   .. autolink-examples:: create_iterative_rag_system
      :collapse:

.. py:function:: create_sequential_rag_system(documents: list[langchain_core.documents.Document] | None = None, use_grading: bool = True, use_citations: bool = False) -> haive.agents.multi.base.SequentialAgent

   Create a sequential RAG system with configurable components.


   .. autolink-examples:: create_sequential_rag_system
      :collapse:

.. py:function:: document_quality_check(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> str

   Check document quality and route accordingly.

   :returns: Documents are good enough for generation
             - "insufficient": Need more/better documents
             - "regrade": Need different grading approach
   :rtype: - "sufficient"


   .. autolink-examples:: document_quality_check
      :collapse:

.. py:function:: should_grade_documents(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> str

   Conditional routing function to determine if documents need grading.

   :returns: If documents need to be graded
             - "generate": If documents are already good enough
             - "refine": If query needs refinement
   :rtype: - "grade"


   .. autolink-examples:: should_grade_documents
      :collapse:

.. py:function:: should_refine_query(state: haive.agents.rag.multi_agent_rag.state.MultiAgentRAGState) -> str

   Conditional routing function to determine if query needs refinement.

   :returns: Try retrieval again with refined query
             - "generate": Generate answer with available documents
             - "END": Stop processing (failure case)
   :rtype: - "retrieve"


   .. autolink-examples:: should_refine_query
      :collapse:

.. py:function:: test_agent_compatibility(agent1: Any, agent2: Any) -> dict[str, Any]

   Test compatibility between two agents using the compatibility module.

   This demonstrates using the compatibility module to test if agents
   can work together as mentioned in the user prompt.


   .. autolink-examples:: test_agent_compatibility
      :collapse:

.. py:function:: validate_multi_agent_compatibility(agents: list[Any]) -> dict[str, Any]

   Validate compatibility across multiple agents in a workflow.

   Returns a comprehensive compatibility report for the agent chain.


   .. autolink-examples:: validate_multi_agent_compatibility
      :collapse:

.. py:data:: agent_list

.. py:data:: base_rag_agent

