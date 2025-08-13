
:py:mod:`agents.rag.agentic_router.agent_chain`
===============================================

.. py:module:: agents.rag.agentic_router.agent_chain

Agentic RAG Router using ChainAgent.

Simplified version using the new ChainAgent approach.


.. autolink-examples:: agents.rag.agentic_router.agent_chain
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.agentic_router.agent_chain.RAGStrategy
   agents.rag.agentic_router.agent_chain.StrategyDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RAGStrategy {
        node [shape=record];
        "RAGStrategy" [label="RAGStrategy"];
        "str" -> "RAGStrategy";
        "enum.Enum" -> "RAGStrategy";
      }

.. autoclass:: agents.rag.agentic_router.agent_chain.RAGStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGStrategy** is an Enum defined in ``agents.rag.agentic_router.agent_chain``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StrategyDecision:

   .. graphviz::
      :align: center

      digraph inheritance_StrategyDecision {
        node [shape=record];
        "StrategyDecision" [label="StrategyDecision"];
        "pydantic.BaseModel" -> "StrategyDecision";
      }

.. autopydantic_model:: agents.rag.agentic_router.agent_chain.StrategyDecision
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.rag.agentic_router.agent_chain.create_agentic_rag_router_chain
   agents.rag.agentic_router.agent_chain.create_agentic_router_multi_agent
   agents.rag.agentic_router.agent_chain.create_simple_rag_router_chain
   agents.rag.agentic_router.agent_chain.get_agentic_router_chain_io_schema

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.agentic_router.agent_chain
   :collapse:
   
.. autolink-skip:: next
