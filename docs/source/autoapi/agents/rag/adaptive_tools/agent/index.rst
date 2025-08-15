agents.rag.adaptive_tools.agent
===============================

.. py:module:: agents.rag.adaptive_tools.agent

.. autoapi-nested-parse::

   Adaptive RAG with Tools Integration Agents.

   from typing import Any
   Implementation of adaptive RAG with tool integration and ReAct patterns.
   Includes Google Search integration, tool selection, and dynamic routing based on query needs.


   .. autolink-examples:: agents.rag.adaptive_tools.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.adaptive_tools.agent.ADAPTIVE_SYNTHESIS_PROMPT
   agents.rag.adaptive_tools.agent.GOOGLE_SEARCH_PROMPT
   agents.rag.adaptive_tools.agent.TOOL_SELECTION_PROMPT
   agents.rag.adaptive_tools.agent.logger


Classes
-------

.. autoapisummary::

   agents.rag.adaptive_tools.agent.AdaptiveToolsRAGAgent
   agents.rag.adaptive_tools.agent.AdaptiveToolsResult
   agents.rag.adaptive_tools.agent.QueryNeed
   agents.rag.adaptive_tools.agent.SearchIntegrationAgent
   agents.rag.adaptive_tools.agent.SearchResult
   agents.rag.adaptive_tools.agent.ToolSelection
   agents.rag.adaptive_tools.agent.ToolSelectionAgent
   agents.rag.adaptive_tools.agent.ToolType


Functions
---------

.. autoapisummary::

   agents.rag.adaptive_tools.agent.create_adaptive_synthesis_callable
   agents.rag.adaptive_tools.agent.create_adaptive_tools_rag_agent
   agents.rag.adaptive_tools.agent.create_google_search_callable
   agents.rag.adaptive_tools.agent.create_tool_selector_callable
   agents.rag.adaptive_tools.agent.get_adaptive_tools_rag_io_schema


Module Contents
---------------

.. py:class:: AdaptiveToolsRAGAgent

   Bases: :py:obj:`haive.agents.multi.base.SequentialAgent`


   Complete Adaptive RAG agent with tools integration and ReAct patterns.


   .. autolink-examples:: AdaptiveToolsRAGAgent
      :collapse:

   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, enable_google_search: bool = True, enable_local_retrieval: bool = True, **kwargs)
      :classmethod:


      Create Adaptive Tools RAG agent from documents.

      :param documents: Documents to index for local retrieval
      :param llm_config: LLM configuration
      :param enable_google_search: Whether to enable Google Search integration
      :param enable_local_retrieval: Whether to enable local document retrieval
      :param \*\*kwargs: Additional arguments

      :returns: AdaptiveToolsRAGAgent instance


      .. autolink-examples:: from_documents
         :collapse:


.. py:class:: AdaptiveToolsResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete result from adaptive tools RAG.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptiveToolsResult
      :collapse:

   .. py:attribute:: external_sources
      :type:  int
      :value: None



   .. py:attribute:: fallback_used
      :type:  bool
      :value: None



   .. py:attribute:: final_response
      :type:  str
      :value: None



   .. py:attribute:: information_freshness
      :type:  float
      :value: None



   .. py:attribute:: local_sources
      :type:  int
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: primary_tool_success
      :type:  bool
      :value: None



   .. py:attribute:: processing_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: react_iterations
      :type:  int
      :value: None



   .. py:attribute:: reasoning_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: response_confidence
      :type:  float
      :value: None



   .. py:attribute:: source_diversity
      :type:  float
      :value: None



   .. py:attribute:: tools_used
      :type:  list[ToolType]
      :value: None



   .. py:attribute:: total_searches
      :type:  int
      :value: None



.. py:class:: QueryNeed

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Query need categories for tool selection.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryNeed
      :collapse:

   .. py:attribute:: COMMON_KNOWLEDGE
      :value: 'common_knowledge'



   .. py:attribute:: COMPLEX_REASONING
      :value: 'complex_reasoning'



   .. py:attribute:: CURRENT_EVENTS
      :value: 'current_events'



   .. py:attribute:: DOCUMENT_SPECIFIC
      :value: 'document_specific'



   .. py:attribute:: FACTUAL_LOOKUP
      :value: 'factual_lookup'



   .. py:attribute:: TECHNICAL_RESEARCH
      :value: 'technical_research'



.. py:class:: SearchIntegrationAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that integrates external search tools.


   .. autolink-examples:: SearchIntegrationAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build search integration graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Search Integration'



.. py:class:: SearchResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Results from search tools.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SearchResult
      :collapse:

   .. py:attribute:: authority_score
      :type:  float
      :value: None



   .. py:attribute:: completeness
      :type:  float
      :value: None



   .. py:attribute:: content_freshness
      :type:  float
      :value: None



   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: query_used
      :type:  str
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



   .. py:attribute:: results_count
      :type:  int
      :value: None



   .. py:attribute:: search_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: search_quality
      :type:  float
      :value: None



   .. py:attribute:: source_urls
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_used
      :type:  ToolType
      :value: None



.. py:class:: ToolSelection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Tool selection analysis and recommendations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolSelection
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: expected_result_type
      :type:  str
      :value: None



   .. py:attribute:: fallback_tools
      :type:  list[ToolType]
      :value: None



   .. py:attribute:: primary_tool
      :type:  ToolType
      :value: None



   .. py:attribute:: query_need
      :type:  QueryNeed
      :value: None



   .. py:attribute:: react_strategy
      :type:  str
      :value: None



   .. py:attribute:: search_terms
      :type:  list[str]
      :value: None



   .. py:attribute:: specificity
      :type:  float
      :value: None



   .. py:attribute:: tool_justification
      :type:  str
      :value: None



   .. py:attribute:: urgency
      :type:  float
      :value: None



.. py:class:: ToolSelectionAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Agent that selects optimal tools based on query analysis.


   .. autolink-examples:: ToolSelectionAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build tool selection graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Tool Selection'



.. py:class:: ToolType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available tool types for adaptive RAG.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolType
      :collapse:

   .. py:attribute:: ARXIV
      :value: 'arxiv'



   .. py:attribute:: DIRECT_ANSWER
      :value: 'direct_answer'



   .. py:attribute:: GOOGLE_SEARCH
      :value: 'google_search'



   .. py:attribute:: HYDE
      :value: 'hyde'



   .. py:attribute:: LOCAL_RETRIEVAL
      :value: 'local_retrieval'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: WIKIPEDIA
      :value: 'wikipedia'



.. py:function:: create_adaptive_synthesis_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for adaptive synthesis.


   .. autolink-examples:: create_adaptive_synthesis_callable
      :collapse:

.. py:function:: create_adaptive_tools_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, tools_mode: str = 'full', **kwargs) -> AdaptiveToolsRAGAgent

   Create an Adaptive Tools RAG agent.

   :param documents: Documents for local retrieval
   :param llm_config: LLM configuration
   :param tools_mode: Tools mode ("full", "search_only", "local_only")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Adaptive Tools RAG agent


   .. autolink-examples:: create_adaptive_tools_rag_agent
      :collapse:

.. py:function:: create_google_search_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for Google search integration.


   .. autolink-examples:: create_google_search_callable
      :collapse:

.. py:function:: create_tool_selector_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for tool selection.


   .. autolink-examples:: create_tool_selector_callable
      :collapse:

.. py:function:: get_adaptive_tools_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Adaptive Tools RAG agents.


   .. autolink-examples:: get_adaptive_tools_rag_io_schema
      :collapse:

.. py:data:: ADAPTIVE_SYNTHESIS_PROMPT

.. py:data:: GOOGLE_SEARCH_PROMPT

.. py:data:: TOOL_SELECTION_PROMPT

.. py:data:: logger

