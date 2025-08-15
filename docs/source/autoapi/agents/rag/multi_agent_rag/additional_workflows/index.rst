agents.rag.multi_agent_rag.additional_workflows
===============================================

.. py:module:: agents.rag.multi_agent_rag.additional_workflows

.. autoapi-nested-parse::

   Additional RAG Workflows - Extended Multi-Agent RAG Implementations.

   from typing import Any
   This module implements additional RAG architectures beyond the simple enhanced workflows,
   including memory-based, multi-query, fusion, and advanced reasoning patterns.


   .. autolink-examples:: agents.rag.multi_agent_rag.additional_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.additional_workflows.MemoryRAGState
   agents.rag.multi_agent_rag.additional_workflows.MultiQueryRAGAgent
   agents.rag.multi_agent_rag.additional_workflows.MultiQueryRAGState
   agents.rag.multi_agent_rag.additional_workflows.QueryDecompositionRAGAgent
   agents.rag.multi_agent_rag.additional_workflows.RAGFusionAgent
   agents.rag.multi_agent_rag.additional_workflows.SelfRAGAgent
   agents.rag.multi_agent_rag.additional_workflows.SelfRAGState
   agents.rag.multi_agent_rag.additional_workflows.SimpleRAGWithMemoryAgent
   agents.rag.multi_agent_rag.additional_workflows.StepBackPromptingRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.additional_workflows.build_custom_graph


Module Contents
---------------

.. py:class:: MemoryRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   Extended RAG state with conversation memory.


   .. autolink-examples:: MemoryRAGState
      :collapse:

   .. py:attribute:: conversation_history
      :type:  list[dict[str, str]]
      :value: []



   .. py:attribute:: memory_context
      :type:  str
      :value: ''



   .. py:attribute:: previous_queries
      :type:  list[str]
      :value: []



.. py:class:: MultiQueryRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Multi-Query RAG - generates multiple diverse queries and retrieves documents.
   for each, then synthesizes results.


   .. autolink-examples:: MultiQueryRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: MultiQueryRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state for multi-query approaches.


   .. autolink-examples:: MultiQueryRAGState
      :collapse:

   .. py:attribute:: generated_queries
      :type:  list[str]
      :value: []



   .. py:attribute:: query_results
      :type:  dict[str, list[str]]


.. py:class:: QueryDecompositionRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Query Decomposition RAG - breaks complex queries into simpler sub-questions,.
   retrieves for each, then composes the final answer.


   .. autolink-examples:: QueryDecompositionRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: RAGFusionAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   RAG Fusion - combines multiple retrieval strategies and fuses results.
   using reciprocal rank fusion and other techniques.


   .. autolink-examples:: RAGFusionAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: SelfRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Self-RAG with reflection tokens - determines whether retrieval is needed.
   and reflects on the quality of generated answers.


   .. autolink-examples:: SelfRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: SelfRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state with self-reflection capabilities.


   .. autolink-examples:: SelfRAGState
      :collapse:

   .. py:attribute:: answer_confidence
      :type:  float
      :value: 0.0



   .. py:attribute:: needs_retrieval
      :type:  bool
      :value: True



   .. py:attribute:: reflection_tokens
      :type:  list[str]
      :value: []



   .. py:attribute:: retrieval_confidence
      :type:  float
      :value: 0.0



.. py:class:: SimpleRAGWithMemoryAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Simple RAG with Memory - incorporates conversation history and previous queries.
   to provide contextually aware responses.


   .. autolink-examples:: SimpleRAGWithMemoryAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: StepBackPromptingRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Step-Back Prompting RAG - asks broader conceptual questions before.
   specific retrieval to get better context.


   .. autolink-examples:: StepBackPromptingRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for this multi-agent workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:function:: build_custom_graph() -> Any

   Build custom graph for additional workflows.

   This is a utility function for creating custom graphs for
   advanced RAG workflows in this module.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

