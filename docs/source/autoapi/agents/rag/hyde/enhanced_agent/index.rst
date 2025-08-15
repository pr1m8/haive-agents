agents.rag.hyde.enhanced_agent
==============================

.. py:module:: agents.rag.hyde.enhanced_agent

.. autoapi-nested-parse::

   Enhanced HyDE RAG Agent using Structured Output Pattern.

   from typing import Any, Dict
   This demonstrates the new pattern where any agent can be enhanced with structured
   output by appending a SimpleAgent. This approach is more modular and follows the
   principle of separation of concerns.


   .. autolink-examples:: agents.rag.hyde.enhanced_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent.ENHANCED_HYDE_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent.EnhancedHyDERAGAgent
   agents.rag.hyde.enhanced_agent.EnhancedHyDERetriever


Functions
---------

.. autoapisummary::

   agents.rag.hyde.enhanced_agent.adaptive_retrieval
   agents.rag.hyde.enhanced_agent.build_graph
   agents.rag.hyde.enhanced_agent.create_enhanced_hyde_agent
   agents.rag.hyde.enhanced_agent.create_hyde_enhancer
   agents.rag.hyde.enhanced_agent.demonstrate_enhancement_vs_traditional


Module Contents
---------------

.. py:class:: EnhancedHyDERAGAgent

   Bases: :py:obj:`haive.agents.multi.enhanced_sequential_agent.SequentialAgent`


   Enhanced HyDE RAG Agent using the structured output enhancement pattern.

   This agent demonstrates the new modular approach where:
   1. Base agents handle core functionality (generation, retrieval)
   2. Enhancement agents add structured output processing
   3. The pattern is reusable across different RAG types

   Benefits:
   - Separation of concerns between generation and structure
   - Reusable enhancement pattern
   - Easier testing and debugging
   - Better maintainability


   .. autolink-examples:: EnhancedHyDERAGAgent
      :collapse:

   .. py:method:: _create_traditional_pattern(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_model: str | None = None, **kwargs)
      :classmethod:


      Create using traditional pattern for comparison.


      .. autolink-examples:: _create_traditional_pattern
         :collapse:


   .. py:method:: _create_with_enhancement_pattern(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_model: str | None = None, **kwargs)
      :classmethod:


      Create using the new structured output enhancement pattern.


      .. autolink-examples:: _create_with_enhancement_pattern
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, embedding_model: str | None = None, use_enhancement_pattern: bool = True, **kwargs)
      :classmethod:


      Create Enhanced HyDE RAG from documents.

      :param documents: Documents to index
      :param llm_config: Optional LLM configuration
      :param embedding_model: Optional embedding model for vector store
      :param use_enhancement_pattern: Whether to use the new enhancement pattern
      :param \*\*kwargs: Additional arguments

      :returns: EnhancedHyDERAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: EnhancedHyDERetriever(documents: list[langchain_core.documents.Document], embedding_model: str | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Enhanced retriever that handles both enhancement pattern and traditional outputs.


   .. autolink-examples:: EnhancedHyDERetriever
      :collapse:

   .. py:method:: build_graph() -> Any

      Build graph that adapts to both enhancement and traditional patterns.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: embedding_model
      :type:  str | None
      :value: None



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

.. py:data:: ENHANCED_HYDE_PROMPT

