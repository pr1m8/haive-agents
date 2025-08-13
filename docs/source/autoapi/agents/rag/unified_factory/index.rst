
:py:mod:`agents.rag.unified_factory`
====================================

.. py:module:: agents.rag.unified_factory

Unified RAG Factory.

from typing import Any, Dict
Create any RAG agent using either traditional or ChainAgent approach.
Integrates with multi-agent system.


.. autolink-examples:: agents.rag.unified_factory
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.unified_factory.RAGFactory
   agents.rag.unified_factory.RAGStyle
   agents.rag.unified_factory.RAGType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGFactory:

   .. graphviz::
      :align: center

      digraph inheritance_RAGFactory {
        node [shape=record];
        "RAGFactory" [label="RAGFactory"];
      }

.. autoclass:: agents.rag.unified_factory.RAGFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGStyle:

   .. graphviz::
      :align: center

      digraph inheritance_RAGStyle {
        node [shape=record];
        "RAGStyle" [label="RAGStyle"];
        "str" -> "RAGStyle";
        "enum.Enum" -> "RAGStyle";
      }

.. autoclass:: agents.rag.unified_factory.RAGStyle
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGStyle** is an Enum defined in ``agents.rag.unified_factory``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGType:

   .. graphviz::
      :align: center

      digraph inheritance_RAGType {
        node [shape=record];
        "RAGType" [label="RAGType"];
        "str" -> "RAGType";
        "enum.Enum" -> "RAGType";
      }

.. autoclass:: agents.rag.unified_factory.RAGType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGType** is an Enum defined in ``agents.rag.unified_factory``.



Functions
---------

.. autoapisummary::

   agents.rag.unified_factory.create_rag
   agents.rag.unified_factory.create_rag_chain
   agents.rag.unified_factory.create_rag_multi
   agents.rag.unified_factory.create_rag_pipeline
   agents.rag.unified_factory.example_usage

.. py:function:: create_rag(rag_type: str | RAGType, documents: list[langchain_core.documents.Document], style: str | RAGStyle = 'chain', **kwargs) -> haive.agents.base.agent.Agent | haive.agents.chain.ChainAgent

   Simple function to create any RAG agent.


   .. autolink-examples:: create_rag
      :collapse:

.. py:function:: create_rag_chain(rag_type: str | RAGType, documents: list[langchain_core.documents.Document], **kwargs) -> haive.agents.chain.ChainAgent

   Create a RAG agent as a ChainAgent.


   .. autolink-examples:: create_rag_chain
      :collapse:

.. py:function:: create_rag_multi(rag_type: str | RAGType, documents: list[langchain_core.documents.Document], **kwargs)

   Create a RAG agent as a MultiAgent.


   .. autolink-examples:: create_rag_multi
      :collapse:

.. py:function:: create_rag_pipeline(rag_types: list[str | RAGType], documents: list[langchain_core.documents.Document], style: RAGStyle = RAGStyle.CHAIN, **kwargs) -> haive.agents.chain.ChainAgent

   Create a pipeline of RAG agents.


   .. autolink-examples:: create_rag_pipeline
      :collapse:

.. py:function:: example_usage() -> Dict[str, Any]

   Examples of how to use the unified factory.


   .. autolink-examples:: example_usage
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.unified_factory
   :collapse:
   
.. autolink-skip:: next
