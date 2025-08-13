
:py:mod:`agents.rag.chain_collection`
=====================================

.. py:module:: agents.rag.chain_collection

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

Classes
-------

.. autoapisummary::

   agents.rag.chain_collection.RAGChainCollection


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGChainCollection:

   .. graphviz::
      :align: center

      digraph inheritance_RAGChainCollection {
        node [shape=record];
        "RAGChainCollection" [label="RAGChainCollection"];
      }

.. autoclass:: agents.rag.chain_collection.RAGChainCollection
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.chain_collection.create_rag_chain
   agents.rag.chain_collection.create_rag_pipeline

.. py:function:: create_rag_chain(rag_type: str, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, **kwargs) -> haive.agents.chain.ChainAgent

   Create any RAG chain by type.


   .. autolink-examples:: create_rag_chain
      :collapse:

.. py:function:: create_rag_pipeline(rag_types: list[str], documents: list[langchain_core.documents.Document], combination_strategy: str = 'sequential', llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a pipeline of multiple RAG approaches.


   .. autolink-examples:: create_rag_pipeline
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.chain_collection
   :collapse:
   
.. autolink-skip:: next
