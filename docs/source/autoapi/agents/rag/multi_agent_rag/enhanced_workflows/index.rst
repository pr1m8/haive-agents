
:py:mod:`agents.rag.multi_agent_rag.enhanced_workflows`
=======================================================

.. py:module:: agents.rag.multi_agent_rag.enhanced_workflows

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CorrectiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CorrectiveRAGAgent {
        node [shape=record];
        "CorrectiveRAGAgent" [label="CorrectiveRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "CorrectiveRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_workflows.CorrectiveRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGradingAgent {
        node [shape=record];
        "DocumentGradingAgent" [label="DocumentGradingAgent"];
        "haive.agents.base.agent.Agent" -> "DocumentGradingAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_workflows.DocumentGradingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HYDERAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HYDERAGAgent {
        node [shape=record];
        "HYDERAGAgent" [label="HYDERAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "HYDERAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_workflows.HYDERAGAgent
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

.. autoclass:: agents.rag.multi_agent_rag.enhanced_workflows.RequeryDecisionAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfRAGAgent {
        node [shape=record];
        "SelfRAGAgent" [label="SelfRAGAgent"];
        "haive.agents.multi.base.ConditionalAgent" -> "SelfRAGAgent";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_workflows.SelfRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_workflows.create_enhanced_rag_workflow

.. py:function:: create_enhanced_rag_workflow(workflow_type: str = 'crag', documents: list[langchain_core.documents.Document] | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Factory function to create enhanced RAG workflows.

   :param workflow_type: Type of workflow ("crag", "hyde", "self_rag")
   :param documents: Documents for retrieval
   :param \*\*kwargs: Additional arguments

   :returns: Configured RAG agent


   .. autolink-examples:: create_enhanced_rag_workflow
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.enhanced_workflows
   :collapse:
   
.. autolink-skip:: next
