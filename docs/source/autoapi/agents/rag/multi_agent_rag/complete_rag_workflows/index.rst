agents.rag.multi_agent_rag.complete_rag_workflows
=================================================

.. py:module:: agents.rag.multi_agent_rag.complete_rag_workflows

.. autoapi-nested-parse::

   Complete RAG Workflows Implementation.

   Implements all RAG architectures from rag-architectures-flows.md including:
   - Corrective RAG with web search fallback
   - Self-RAG with reflection tokens
   - Adaptive RAG with complexity routing
   - Multi-Query RAG and RAG Fusion
   - HYDE and Step-Back prompting
   - Hallucination detection and requerying


   .. autolink-examples:: agents.rag.multi_agent_rag.complete_rag_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.complete_rag_workflows.AdaptiveRAGAgent
   agents.rag.multi_agent_rag.complete_rag_workflows.CorrectiveRAGAgent
   agents.rag.multi_agent_rag.complete_rag_workflows.HYDERAGAgent
   agents.rag.multi_agent_rag.complete_rag_workflows.RAGQuality
   agents.rag.multi_agent_rag.complete_rag_workflows.ReflectionToken
   agents.rag.multi_agent_rag.complete_rag_workflows.SelfRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.complete_rag_workflows.crag_relevance_check
   agents.rag.multi_agent_rag.complete_rag_workflows.create_complete_rag_workflow
   agents.rag.multi_agent_rag.complete_rag_workflows.hallucination_detection
   agents.rag.multi_agent_rag.complete_rag_workflows.web_search_fallback


Module Contents
---------------

.. py:class:: AdaptiveRAGAgent(documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Adaptive RAG with complexity-based routing.


   .. autolink-examples:: AdaptiveRAGAgent
      :collapse:

   .. py:method:: _build_analyzer_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


   .. py:method:: _create_multi_query_agent(documents: list[langchain_core.documents.Document] | None) -> haive.agents.base.agent.Agent

      Create multi-query RAG agent.


      .. autolink-examples:: _create_multi_query_agent
         :collapse:


   .. py:method:: _setup_adaptive_routing()

      Set up adaptive routing based on complexity.


      .. autolink-examples:: _setup_adaptive_routing
         :collapse:


   .. py:attribute:: analyzer_agent


   .. py:attribute:: complex_rag_agent


   .. py:attribute:: direct_agent


   .. py:attribute:: multi_query_agent


   .. py:attribute:: simple_rag_agent


.. py:class:: CorrectiveRAGAgent(documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Full Corrective RAG implementation with web search fallback.


   .. autolink-examples:: CorrectiveRAGAgent
      :collapse:

   .. py:method:: _build_relevance_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


   .. py:method:: _build_web_search_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


   .. py:method:: _setup_crag_routing()

      Set up CRAG conditional routing.


      .. autolink-examples:: _setup_crag_routing
         :collapse:


   .. py:attribute:: answer_agent


   .. py:attribute:: relevance_agent


   .. py:attribute:: retrieval_agent


   .. py:attribute:: web_search_agent


.. py:class:: HYDERAGAgent(documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Enhanced HYDE RAG with hypothesis generation.


   .. autolink-examples:: HYDERAGAgent
      :collapse:

   .. py:method:: _build_hypothesis_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


.. py:class:: RAGQuality

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Quality assessment for retrieved documents.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGQuality
      :collapse:

   .. py:attribute:: AMBIGUOUS
      :value: 'ambiguous'



   .. py:attribute:: CORRECT
      :value: 'correct'



   .. py:attribute:: INCORRECT
      :value: 'incorrect'



.. py:class:: ReflectionToken

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Self-RAG reflection tokens.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionToken
      :collapse:

   .. py:attribute:: ISREL_NOT_RELEVANT
      :value: '[ISREL] Not Relevant'



   .. py:attribute:: ISREL_RELEVANT
      :value: '[ISREL] Relevant'



   .. py:attribute:: ISSUP_NOT_SUPPORTED
      :value: '[ISSUP] Not Supported'



   .. py:attribute:: ISSUP_SUPPORTED
      :value: '[ISSUP] Supported'



   .. py:attribute:: ISUSE_NOT_USEFUL
      :value: '[ISUSE] Not Useful'



   .. py:attribute:: ISUSE_USEFUL
      :value: '[ISUSE] Useful'



   .. py:attribute:: NO_RETRIEVAL
      :value: '[No Retrieval]'



   .. py:attribute:: RETRIEVAL_YES
      :value: '[Retrieval]'



.. py:class:: SelfRAGAgent(documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Self-RAG with reflection tokens and adaptive retrieval.


   .. autolink-examples:: SelfRAGAgent
      :collapse:

   .. py:method:: _build_decision_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


   .. py:method:: _build_hallucination_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


   .. py:method:: _build_relevance_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph


   .. py:method:: _setup_self_rag_routing()

      Set up Self-RAG routing with reflection tokens.


      .. autolink-examples:: _setup_self_rag_routing
         :collapse:


   .. py:attribute:: decision_agent


   .. py:attribute:: generation_agent


   .. py:attribute:: hallucination_agent


   .. py:attribute:: relevance_agent


   .. py:attribute:: retrieval_agent


.. py:function:: crag_relevance_check(input_data: dict) -> dict

   CRAG relevance checking with three-way classification.


   .. autolink-examples:: crag_relevance_check
      :collapse:

.. py:function:: create_complete_rag_workflow(workflow_type: str, documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Factory for creating complete RAG workflows.

   Available types:
   - 'crag': Corrective RAG with web search
   - 'self_rag': Self-RAG with reflection tokens
   - 'adaptive': Adaptive RAG with complexity routing
   - 'hyde': HYDE RAG with hypothesis generation
   - 'multi_query': Multi-Query RAG with query variations


   .. autolink-examples:: create_complete_rag_workflow
      :collapse:

.. py:function:: hallucination_detection(input_data: dict) -> dict

   Detect hallucination in generated response.


   .. autolink-examples:: hallucination_detection
      :collapse:

.. py:function:: web_search_fallback(input_data: dict) -> dict

   Web search fallback for when documents are insufficient.


   .. autolink-examples:: web_search_fallback
      :collapse:

