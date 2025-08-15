agents.rag.multi_agent_rag.simple_enhanced_workflows
====================================================

.. py:module:: agents.rag.multi_agent_rag.simple_enhanced_workflows

.. autoapi-nested-parse::

   Simple Enhanced Multi-Agent RAG Workflows.

   Clean implementation of advanced RAG patterns without complex dependencies.


   .. autolink-examples:: agents.rag.multi_agent_rag.simple_enhanced_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.simple_enhanced_workflows.DocumentGradingAgent
   agents.rag.multi_agent_rag.simple_enhanced_workflows.RequeryDecisionAgent
   agents.rag.multi_agent_rag.simple_enhanced_workflows.SimpleCorrectiveRAGAgent
   agents.rag.multi_agent_rag.simple_enhanced_workflows.SimpleHYDERAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.simple_enhanced_workflows.create_simple_rag_workflow


Module Contents
---------------

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



.. py:class:: SimpleCorrectiveRAGAgent(documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Simple Corrective RAG implementation using sequential processing.


   .. autolink-examples:: SimpleCorrectiveRAGAgent
      :collapse:

.. py:class:: SimpleHYDERAGAgent(documents: list[langchain_core.documents.Document] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Simple HYDE RAG agent that generates hypothetical documents before retrieval.


   .. autolink-examples:: SimpleHYDERAGAgent
      :collapse:

.. py:function:: create_simple_rag_workflow(workflow_type: str = 'crag', documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Factory function to create simple RAG workflows.

   :param workflow_type: Type of workflow ("crag", "hyde")
   :param documents: Documents for retrieval
   :param \*\*kwargs: Additional arguments

   :returns: Configured RAG agent


   .. autolink-examples:: create_simple_rag_workflow
      :collapse:

