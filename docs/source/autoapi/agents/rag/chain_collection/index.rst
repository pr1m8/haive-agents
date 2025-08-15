agents.rag.chain_collection
===========================

.. py:module:: agents.rag.chain_collection

.. autoapi-nested-parse::

   Complete Collection of RAG Agents using ChainAgent.

   from typing import Any, Dict
   This module provides a comprehensive collection of Retrieval-Augmented Generation (RAG)
   agents implemented using the ChainAgent framework. Each agent represents a different
   RAG strategy or pattern, optimized for specific use cases.

   .. rubric:: Example

   >>> from haive.agents.rag.chain_collection import RAGChainCollection
   >>> from langchain_core.documents import Document
   >>> from haive.core.models.llm.base import AzureLLMConfig
   >>>
   >>> docs = [Document(page_content="AI is transforming industries...")]
   >>> llm_config = AzureLLMConfig(deployment_name="gpt-4")
   >>> collection = RAGChainCollection()
   >>> agent = collection.create_simple_rag(docs, llm_config)

   Typical usage:
       - Create documents for retrieval
       - Choose appropriate RAG strategy
       - Configure LLM and retrieval settings
       - Build agent using collection methods
       - Execute queries through agent interface

   Available RAG Strategies:
       - Simple RAG: Basic retrieve-and-generate pattern
       - HyDE RAG: Hypothetical document generation for enhanced retrieval
       - Fusion RAG: Multi-query retrieval with reciprocal rank fusion
       - Step-Back RAG: Abstract reasoning before specific answers
       - Speculative RAG: Hypothesis generation and verification
       - Memory-Aware RAG: Conversation context integration
       - FLARE RAG: Forward-looking active retrieval with refinement


   .. autolink-examples:: agents.rag.chain_collection
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.chain_collection.RAG_TYPES
   agents.rag.chain_collection.logger


Classes
-------

.. autoapisummary::

   agents.rag.chain_collection.RAGChainCollection


Functions
---------

.. autoapisummary::

   agents.rag.chain_collection.create_rag_chain
   agents.rag.chain_collection.create_rag_pipeline


Module Contents
---------------

.. py:class:: RAGChainCollection

   Collection of all RAG agents as ChainAgents.

   This class provides static factory methods for creating different types
   of RAG agents using the ChainAgent framework. Each method builds a
   complete RAG workflow with appropriate retrieval and generation steps.

   .. rubric:: Example

   >>> collection = RAGChainCollection()
   >>> agent = collection.create_simple_rag(documents, llm_config)
   >>> response = agent.invoke({"query": "What is machine learning?"})


   .. autolink-examples:: RAGChainCollection
      :collapse:

   .. py:method:: create_flare_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      FLARE RAG - forward-looking active retrieval.


      .. autolink-examples:: create_flare_rag
         :collapse:


   .. py:method:: create_fusion_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      Fusion RAG - multiple queries with reciprocal rank fusion.


      .. autolink-examples:: create_fusion_rag
         :collapse:


   .. py:method:: create_hyde_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      HyDE RAG - generate hypothetical document first.


      .. autolink-examples:: create_hyde_rag
         :collapse:


   .. py:method:: create_memory_aware_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      Memory-Aware RAG - uses conversation memory.


      .. autolink-examples:: create_memory_aware_rag
         :collapse:


   .. py:method:: create_simple_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      Create a simple RAG agent with basic retrieve-and-generate pattern.

      This is the most straightforward RAG implementation: retrieve relevant
      documents based on the query, then generate an answer using those documents
      as context.

      :param documents: Documents to use for retrieval.
      :type documents: List[Document]
      :param llm_config: LLM configuration for generation.
      :type llm_config: LLMConfig

      :returns: A configured simple RAG agent.
      :rtype: ChainAgent

      .. rubric:: Example

      >>> from langchain_core.documents import Document
      >>> docs = [Document(page_content="AI helps solve problems...")]
      >>> agent = RAGChainCollection.create_simple_rag(docs, llm_config)


      .. autolink-examples:: create_simple_rag
         :collapse:


   .. py:method:: create_speculative_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      Speculative RAG - generate and verify hypotheses.


      .. autolink-examples:: create_speculative_rag
         :collapse:


   .. py:method:: create_step_back_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig) -> haive.agents.chain.ChainAgent
      :staticmethod:


      Step-Back RAG - abstract reasoning before specific answer.


      .. autolink-examples:: create_step_back_rag
         :collapse:


.. py:function:: create_rag_chain(rag_type: str, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.chain.ChainAgent

   Create any RAG chain by type.


   .. autolink-examples:: create_rag_chain
      :collapse:

.. py:function:: create_rag_pipeline(rag_types: list[str], documents: list[langchain_core.documents.Document], combination_strategy: str = 'sequential', llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a pipeline of multiple RAG approaches.


   .. autolink-examples:: create_rag_pipeline
      :collapse:

.. py:data:: RAG_TYPES
   :value: ['simple', 'hyde', 'fusion', 'step_back', 'speculative', 'memory_aware', 'flare']


.. py:data:: logger

