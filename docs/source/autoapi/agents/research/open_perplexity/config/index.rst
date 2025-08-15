agents.research.open_perplexity.config
======================================

.. py:module:: agents.research.open_perplexity.config

.. autoapi-nested-parse::

   Configuration for the open_perplexity research agent.

   from typing import Any
   This module defines the configuration class and factory methods for creating
   research agent configurations. It includes settings for LLM engines, tools,
   vector stores, and research parameters.


   .. autolink-examples:: agents.research.open_perplexity.config
      :collapse:


Classes
-------

.. autoapisummary::

   agents.research.open_perplexity.config.ResearchAgentConfig


Module Contents
---------------

.. py:class:: ResearchAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for open_perplexity research agent.

   Defines all configuration parameters for the research agent, including
   state schemas, engines, tools, and research parameters.

   .. attribute:: state_schema

      Schema for the agent state

   .. attribute:: input_schema

      Schema for input to the agent

   .. attribute:: output_schema

      Schema for agent output

   .. attribute:: engines

      Dictionary of AugLLM engines for different tasks

   .. attribute:: tools

      Tools for research and analysis

   .. attribute:: vectorstore_config

      Vector store configuration for document storage

   .. attribute:: react_agent_name

      Name of the configured ReAct agent

   .. attribute:: rag_agent_name

      Name of the configured RAG agent

   .. attribute:: report_format

      Format for the final report

   .. attribute:: research_depth

      Depth of research (1-5, higher means more thorough)

   .. attribute:: max_sources_per_query

      Maximum number of sources to use per query

   .. attribute:: concurrent_searches

      Number of concurrent searches to perform

   .. attribute:: default_report_sections

      Default sections for the research report


   .. autolink-examples:: ResearchAgentConfig
      :collapse:

   .. py:method:: from_scratch(name: str | None = None, llm_model: str = 'gpt-4o', **kwargs)
      :classmethod:


      Create a research agent configuration from scratch.

      Factory method to create a fully configured research agent with all
      necessary engines, tools, and settings.

      :param name: Optional name for the agent (defaults to timestamped name)
      :param llm_model: Model to use for the agent (default: "gpt-4o")
      :param \*\*kwargs: Additional configuration parameters

      :returns: A fully configured research agent configuration
      :rtype: ResearchAgentConfig


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:attribute:: concurrent_searches
      :type:  int
      :value: None



   .. py:attribute:: default_report_sections
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: max_sources_per_query
      :type:  int
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: rag_agent_name
      :type:  str | None
      :value: None



   .. py:attribute:: react_agent_name
      :type:  str | None
      :value: None



   .. py:attribute:: report_format
      :type:  str
      :value: None



   .. py:attribute:: research_depth
      :type:  int
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: vectorstore_config
      :type:  haive.core.models.vectorstore.base.VectorStoreConfig | None
      :value: None



