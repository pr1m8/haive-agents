agents.rag.multi_agent_rag.enhanced_workflows
=============================================

.. py:module:: agents.rag.multi_agent_rag.enhanced_workflows

.. autoapi-nested-parse::

   Enhanced Multi-Agent RAG Workflows.

   Implements advanced RAG patterns like CRAG, Self-RAG, HYDE, and grading workflows
   using the new multi-agent base with compatibility and enhanced state management.


   .. autolink-examples:: agents.rag.multi_agent_rag.enhanced_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_workflows.CorrectiveRAGAgent
   agents.rag.multi_agent_rag.enhanced_workflows.DocumentGradingAgent
   agents.rag.multi_agent_rag.enhanced_workflows.HYDERAGAgent
   agents.rag.multi_agent_rag.enhanced_workflows.RequeryDecisionAgent
   agents.rag.multi_agent_rag.enhanced_workflows.SelfRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_workflows.create_enhanced_rag_workflow


Module Contents
---------------

.. py:class:: CorrectiveRAGAgent(retrieval_agent: haive.agents.rag.base.agent.SimpleRAGAgent | None = None, grading_agent: DocumentGradingAgent | None = None, requery_agent: RequeryDecisionAgent | None = None, answer_agent: haive.agents.simple.agent.SimpleAgent | None = None, documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Corrective RAG (CRAG) with automatic requerying and web search fallback.

   Flow:
   1. Initial retrieval
   2. Grade documents
   3. If quality is poor -> requery or web search
   4. Generate answer with best available docs


   .. autolink-examples:: CorrectiveRAGAgent
      :collapse:

   .. py:method:: _setup_crag_routing()

      Set up CRAG conditional routing logic.


      .. autolink-examples:: _setup_crag_routing
         :collapse:


   .. py:attribute:: answer_agent
      :value: None



   .. py:attribute:: grading_agent
      :value: None



   .. py:attribute:: requery_agent
      :value: None



   .. py:attribute:: retrieval_agent
      :value: None



.. py:class:: DocumentGradingAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that grades retrieved documents for relevance.


   .. autolink-examples:: DocumentGradingAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph that grades each retrieved document.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'Document Grading Agent'



.. py:class:: HYDERAGAgent(hypothesis_agent: haive.agents.simple.agent.SimpleAgent | None = None, retrieval_agent: haive.agents.rag.base.agent.SimpleRAGAgent | None = None, answer_agent: haive.agents.simple.agent.SimpleAgent | None = None, documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   HYDE RAG agent that generates hypothetical documents before retrieval.


   .. autolink-examples:: HYDERAGAgent
      :collapse:

.. py:class:: RequeryDecisionAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that decides if requerying is needed based on document grades.


   .. autolink-examples:: RequeryDecisionAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph that analyzes grades and decides on requerying.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'Requery Decision Agent'



.. py:class:: SelfRAGAgent(retrieval_decision_agent: haive.agents.simple.agent.SimpleAgent | None = None, retrieval_agent: haive.agents.rag.base.agent.SimpleRAGAgent | None = None, relevance_agent: haive.agents.simple.agent.SimpleAgent | None = None, generation_agent: haive.agents.simple.agent.SimpleAgent | None = None, documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.ConditionalAgent`


   Self-RAG agent with reflection tokens and adaptive retrieval.


   .. autolink-examples:: SelfRAGAgent
      :collapse:

   .. py:method:: _setup_self_rag_routing()

      Set up Self-RAG routing with reflection tokens.


      .. autolink-examples:: _setup_self_rag_routing
         :collapse:


   .. py:attribute:: generation_agent
      :value: None



   .. py:attribute:: relevance_agent
      :value: None



   .. py:attribute:: retrieval_agent
      :value: None



   .. py:attribute:: retrieval_decision_agent
      :value: None



.. py:function:: create_enhanced_rag_workflow(workflow_type: str = 'crag', documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Factory function to create enhanced RAG workflows.

   :param workflow_type: Type of workflow ("crag", "hyde", "self_rag")
   :param documents: Documents for retrieval
   :param \*\*kwargs: Additional arguments

   :returns: Configured RAG agent


   .. autolink-examples:: create_enhanced_rag_workflow
      :collapse:

