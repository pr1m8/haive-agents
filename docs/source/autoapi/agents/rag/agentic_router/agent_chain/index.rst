agents.rag.agentic_router.agent_chain
=====================================

.. py:module:: agents.rag.agentic_router.agent_chain

.. autoapi-nested-parse::

   Agentic RAG Router using ChainAgent.

   Simplified version using the new ChainAgent approach.


   .. autolink-examples:: agents.rag.agentic_router.agent_chain
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.agentic_router.agent_chain.RAGStrategy
   agents.rag.agentic_router.agent_chain.StrategyDecision


Functions
---------

.. autoapisummary::

   agents.rag.agentic_router.agent_chain.create_agentic_rag_router_chain
   agents.rag.agentic_router.agent_chain.create_agentic_router_multi_agent
   agents.rag.agentic_router.agent_chain.create_simple_rag_router_chain
   agents.rag.agentic_router.agent_chain.get_agentic_router_chain_io_schema


Module Contents
---------------

.. py:class:: RAGStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available RAG strategies.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGStrategy
      :collapse:

   .. py:attribute:: FLARE
      :value: 'flare'



   .. py:attribute:: FUSION
      :value: 'fusion'



   .. py:attribute:: HYDE
      :value: 'hyde'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: StrategyDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategy selection result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StrategyDecision
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: strategy
      :type:  RAGStrategy
      :value: None



.. py:function:: create_agentic_rag_router_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Agentic RAG Router') -> haive.agents.chain.ChainAgent

   Create an agentic RAG router using ChainAgent.

   Super simple compared to the old implementation!


   .. autolink-examples:: create_agentic_rag_router_chain
      :collapse:

.. py:function:: create_agentic_router_multi_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.multi_integration.ChainMultiAgent

   Create as a multi-agent system.


   .. autolink-examples:: create_agentic_router_multi_agent
      :collapse:

.. py:function:: create_simple_rag_router_chain(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Ultra-simple RAG router with just basic routing.


   .. autolink-examples:: create_simple_rag_router_chain
      :collapse:

.. py:function:: get_agentic_router_chain_io_schema() -> dict[str, list[str]]

   Get I/O schema for the chain version.


   .. autolink-examples:: get_agentic_router_chain_io_schema
      :collapse:

