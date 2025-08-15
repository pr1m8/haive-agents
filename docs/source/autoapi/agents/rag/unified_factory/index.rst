agents.rag.unified_factory
==========================

.. py:module:: agents.rag.unified_factory

.. autoapi-nested-parse::

   Unified RAG Factory.

   from typing import Any, Dict
   Create any RAG agent using either traditional or ChainAgent approach.
   Integrates with multi-agent system.


   .. autolink-examples:: agents.rag.unified_factory
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.unified_factory.logger


Classes
-------

.. autoapisummary::

   agents.rag.unified_factory.RAGFactory
   agents.rag.unified_factory.RAGStyle
   agents.rag.unified_factory.RAGType


Functions
---------

.. autoapisummary::

   agents.rag.unified_factory.create_rag
   agents.rag.unified_factory.create_rag_chain
   agents.rag.unified_factory.create_rag_multi
   agents.rag.unified_factory.create_rag_pipeline
   agents.rag.unified_factory.example_usage


Module Contents
---------------

.. py:class:: RAGFactory

   Unified factory for creating RAG agents.


   .. autolink-examples:: RAGFactory
      :collapse:

   .. py:method:: _create_chain(rag_type: RAGType, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, name: str, **kwargs) -> haive.agents.chain.ChainAgent
      :staticmethod:



   .. py:method:: _create_multi(rag_type: RAGType, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, name: str, **kwargs) -> haive.agents.chain.multi_integration.ChainMultiAgent
      :staticmethod:



   .. py:method:: _create_traditional(rag_type: RAGType, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, name: str, **kwargs) -> haive.agents.base.agent.Agent
      :staticmethod:



   .. py:method:: create(rag_type: RAGType, documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, style: RAGStyle = RAGStyle.CHAIN, name: str | None = None, **kwargs) -> haive.agents.base.agent.Agent | haive.agents.chain.ChainAgent
      :staticmethod:


      Create any RAG agent.

      :param rag_type: Type of RAG to create
      :param documents: Documents for retrieval
      :param llm_config: LLM configuration
      :param style: Implementation style
      :param name: Agent name
      :param \*\*kwargs: Additional arguments

      :returns: The created RAG agent


      .. autolink-examples:: create
         :collapse:


.. py:class:: RAGStyle

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Implementation style.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGStyle
      :collapse:

   .. py:attribute:: CHAIN
      :value: 'chain'



   .. py:attribute:: MULTI
      :value: 'multi'



   .. py:attribute:: TRADITIONAL
      :value: 'traditional'



.. py:class:: RAGType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available RAG types.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGType
      :collapse:

   .. py:attribute:: ADAPTIVE_TOOLS
      :value: 'adaptive_tools'



   .. py:attribute:: AGENTIC_ROUTER
      :value: 'agentic_router'



   .. py:attribute:: CORRECTIVE
      :value: 'corrective'



   .. py:attribute:: FLARE
      :value: 'flare'



   .. py:attribute:: FUSION
      :value: 'fusion'



   .. py:attribute:: HYDE
      :value: 'hyde'



   .. py:attribute:: MEMORY_AWARE
      :value: 'memory_aware'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: QUERY_PLANNING
      :value: 'query_planning'



   .. py:attribute:: SELF_REFLECTIVE
      :value: 'self_reflective'



   .. py:attribute:: SELF_ROUTE
      :value: 'self_route'



   .. py:attribute:: SIMPLE
      :value: 'simple'



   .. py:attribute:: SPECULATIVE
      :value: 'speculative'



   .. py:attribute:: STEP_BACK
      :value: 'step_back'



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

.. py:data:: logger

