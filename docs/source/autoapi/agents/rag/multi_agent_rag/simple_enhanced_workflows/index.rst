
:py:mod:`agents.rag.multi_agent_rag.simple_enhanced_workflows`
==============================================================

.. py:module:: agents.rag.multi_agent_rag.simple_enhanced_workflows

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGradingAgent {
        node [shape=record];
        "DocumentGradingAgent" [label="DocumentGradingAgent"];
        "haive.agents.base.agent.Agent" -> "DocumentGradingAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.simple_enhanced_workflows.DocumentGradingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RequeryDecisionAgent:

   .. graphviz::
      :align: center

      digraph inheritance_RequeryDecisionAgent {
        node [shape=record];
        "RequeryDecisionAgent" [label="RequeryDecisionAgent"];
        "haive.agents.base.agent.Agent" -> "RequeryDecisionAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.simple_enhanced_workflows.RequeryDecisionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleCorrectiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleCorrectiveRAGAgent {
        node [shape=record];
        "SimpleCorrectiveRAGAgent" [label="SimpleCorrectiveRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "SimpleCorrectiveRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.simple_enhanced_workflows.SimpleCorrectiveRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleHYDERAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleHYDERAGAgent {
        node [shape=record];
        "SimpleHYDERAGAgent" [label="SimpleHYDERAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "SimpleHYDERAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.simple_enhanced_workflows.SimpleHYDERAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.simple_enhanced_workflows.create_simple_rag_workflow

.. py:function:: create_simple_rag_workflow(workflow_type: str = 'crag', documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Factory function to create simple RAG workflows.

   :param workflow_type: Type of workflow ("crag", "hyde")
   :param documents: Documents for retrieval
   :param \*\*kwargs: Additional arguments

   :returns: Configured RAG agent


   .. autolink-examples:: create_simple_rag_workflow
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.simple_enhanced_workflows
   :collapse:
   
.. autolink-skip:: next
