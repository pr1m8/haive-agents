agents.research.open_perplexity.react_agent_config
==================================================

.. py:module:: agents.research.open_perplexity.react_agent_config


Functions
---------

.. autoapisummary::

   agents.research.open_perplexity.react_agent_config.create_research_rag_agent_config
   agents.research.open_perplexity.react_agent_config.create_research_rag_engine
   agents.research.open_perplexity.react_agent_config.create_research_react_agent_config


Module Contents
---------------

.. py:function:: create_research_rag_agent_config(vectorstore_config: haive.core.models.vectorstore.base.VectorStoreConfig, name: str | None = None, llm_model: str = 'gpt-4o', temperature: float = 0.2) -> haive.agents.rag.base.config.BaseRAGConfig

   Create a BaseRAGConfig for research document retrieval tasks.
   This function requires a vectorstore_config with loaded documents.

   :param vectorstore_config: Vector store configuration with loaded documents
   :param name: Optional name for the agent
   :param llm_model: Model to use (default: gpt-4o)
   :param temperature: Temperature setting (default: 0.2)

   :returns: Configured BaseRAGConfig


   .. autolink-examples:: create_research_rag_agent_config
      :collapse:

.. py:function:: create_research_rag_engine(name: str | None = None, llm_model: str = 'gpt-4o', temperature: float = 0.2) -> haive.core.engine.aug_llm.AugLLMConfig

   Create an AugLLMConfig for research document retrieval tasks.

   :param name: Optional name for the engine
   :param llm_model: Model to use (default: gpt-4o)
   :param temperature: Temperature setting (default: 0.2)

   :returns: Configured AugLLMConfig for RAG


   .. autolink-examples:: create_research_rag_engine
      :collapse:

.. py:function:: create_research_react_agent_config(name: str | None = None, llm_model: str = 'gpt-4o', temperature: float = 0.2) -> haive.agents.react.config.ReactAgentConfig

   Create a ReactAgentConfig specifically for deep research tasks.

   :param name: Optional name for the agent
   :param llm_model: Model to use (default: gpt-4o)
   :param temperature: Temperature setting (default: 0.2)

   :returns: Configured ReactAgentConfig


   .. autolink-examples:: create_research_react_agent_config
      :collapse:

