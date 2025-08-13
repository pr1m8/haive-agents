
:py:mod:`agents.rag.hyde.enhanced_agent`
========================================

.. py:module:: agents.rag.hyde.enhanced_agent

Enhanced HyDE RAG Agent using Structured Output Pattern.

from typing import Any, Dict
This demonstrates the new pattern where any agent can be enhanced with structured
output by appending a SimpleAgent. This approach is more modular and follows the
principle of separation of concerns.


.. autolink-examples:: agents.rag.hyde.enhanced_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent.EnhancedHyDERAGAgent
   agents.rag.hyde.enhanced_agent.EnhancedHyDERetriever


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedHyDERAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedHyDERAGAgent {
        node [shape=record];
        "EnhancedHyDERAGAgent" [label="EnhancedHyDERAGAgent"];
        "haive.agents.multi.enhanced_sequential_agent.SequentialAgent" -> "EnhancedHyDERAGAgent";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent.EnhancedHyDERAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedHyDERetriever:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedHyDERetriever {
        node [shape=record];
        "EnhancedHyDERetriever" [label="EnhancedHyDERetriever"];
        "haive.agents.base.agent.Agent" -> "EnhancedHyDERetriever";
      }

.. autoclass:: agents.rag.hyde.enhanced_agent.EnhancedHyDERetriever
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent.adaptive_retrieval
   agents.rag.hyde.enhanced_agent.build_graph
   agents.rag.hyde.enhanced_agent.create_enhanced_hyde_agent
   agents.rag.hyde.enhanced_agent.create_hyde_enhancer
   agents.rag.hyde.enhanced_agent.demonstrate_enhancement_vs_traditional

.. py:function:: adaptive_retrieval(query: str, documents: list[langchain_core.documents.Document]) -> list[langchain_core.documents.Document]

   Perform adaptive retrieval on documents.


   .. autolink-examples:: adaptive_retrieval
      :collapse:

.. py:function:: build_graph() -> Any

   Build custom graph for enhanced HyDE workflows.


   .. autolink-examples:: build_graph
      :collapse:

.. py:function:: create_enhanced_hyde_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, use_enhancement_pattern: bool = True, **kwargs) -> EnhancedHyDERAGAgent

   Create an Enhanced HyDE RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param use_enhancement_pattern: Whether to use the new enhancement pattern
   :param \*\*kwargs: Additional arguments

   :returns: Configured Enhanced HyDE RAG agent


   .. autolink-examples:: create_enhanced_hyde_agent
      :collapse:

.. py:function:: create_hyde_enhancer()

   Stub function for create_hyde_enhancer.


   .. autolink-examples:: create_hyde_enhancer
      :collapse:

.. py:function:: demonstrate_enhancement_vs_traditional() -> dict[str, Any]

   Demonstrate the difference between enhancement and traditional patterns.


   .. autolink-examples:: demonstrate_enhancement_vs_traditional
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.hyde.enhanced_agent
   :collapse:
   
.. autolink-skip:: next
