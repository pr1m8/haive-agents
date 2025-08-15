agents.memory_reorganized.search.deep_research.agent
====================================================

.. py:module:: agents.memory_reorganized.search.deep_research.agent

.. autoapi-nested-parse::

   Deep Research Agent implementation.

   Provides comprehensive research with multiple sources and detailed analysis. Similar to
   Perplexity's Deep Research feature that performs dozens of searches and reads hundreds
   of sources.


   .. autolink-examples:: agents.memory_reorganized.search.deep_research.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.search.deep_research.agent.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.search.deep_research.agent.DeepResearchAgent


Module Contents
---------------

.. py:class:: DeepResearchAgent(name: str = 'deep_research_agent', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, search_tools: list[langchain_core.tools.Tool] | None = None, enable_kg: bool = False, kg_transformer: Any | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.memory.search.base.BaseSearchAgent`


   Agent for comprehensive research with multiple sources and detailed analysis.

   Mimics Perplexity's Deep Research feature by performing multiple searches,
   analyzing hundreds of sources, and generating comprehensive reports.

   Features:
   - Multi-stage research process
   - Comprehensive source analysis
   - Structured report generation
   - Knowledge graph integration
   - Fact checking and validation
   - Evidence synthesis

   Research Process:
   1. Query decomposition and planning
   2. Background research queries
   3. Specific deep-dive queries
   4. Source evaluation and ranking
   5. Content synthesis and analysis
   6. Report generation and structuring

   .. rubric:: Examples

   Basic usage::

       agent = DeepResearchAgent(
           name="deep_research",
           engine=AugLLMConfig(temperature=0.2)
       )

       response = await agent.process_deep_research(
           "What are the environmental impacts of electric vehicles?",
           research_depth=4
       )

   With knowledge graph integration::

       agent = DeepResearchAgent(
           name="deep_research",
           enable_kg=True,
           kg_transformer=IterativeGraphTransformer()
       )

       response = await agent.process_deep_research(
           "Impact of AI on healthcare outcomes",
           focus_areas=["diagnostic accuracy", "treatment efficiency"]
       )

   Initialize the Deep Research Agent.

   :param name: Agent identifier
   :param engine: LLM configuration (defaults to optimized settings)
   :param search_tools: Optional search tools
   :param enable_kg: Enable knowledge graph integration
   :param kg_transformer: Knowledge graph transformer instance (optional)
   :param \*\*kwargs: Additional arguments passed to parent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DeepResearchAgent
      :collapse:

   .. py:method:: decompose_research_query(query: str, focus_areas: list[str] | None = None) -> list[str]

      Decompose a complex research query into specific sub-queries.

      :param query: Main research query
      :param focus_areas: Specific areas to focus on

      :returns: List of specific research queries


      .. autolink-examples:: decompose_research_query
         :collapse:


   .. py:method:: evaluate_source_credibility(source: dict[str, Any]) -> float

      Evaluate the credibility of a source.

      :param source: Source information

      :returns: Credibility score (0.0-1.0)


      .. autolink-examples:: evaluate_source_credibility
         :collapse:


   .. py:method:: execute_research_query(query: str, query_type: str = 'general') -> haive.agents.memory.search.deep_research.models.ResearchQuery
      :async:


      Execute a single research query and track results.

      :param query: Research query to execute
      :param query_type: Type of query (background, specific, validation)

      :returns: Research query result with metadata


      .. autolink-examples:: execute_research_query
         :collapse:


   .. py:method:: generate_executive_summary(sections: list[haive.agents.memory.search.deep_research.models.ResearchSection]) -> str

      Generate an executive summary from research sections.

      :param sections: Research sections

      :returns: Executive summary text


      .. autolink-examples:: generate_executive_summary
         :collapse:


   .. py:method:: get_response_model() -> type[haive.agents.memory.search.base.SearchResponse]

      Get the response model for deep research.


      .. autolink-examples:: get_response_model
         :collapse:


   .. py:method:: get_search_instructions() -> str

      Get specific search instructions for deep research.


      .. autolink-examples:: get_search_instructions
         :collapse:


   .. py:method:: get_system_prompt() -> str

      Get the system prompt for deep research operations.


      .. autolink-examples:: get_system_prompt
         :collapse:


   .. py:method:: organize_findings_by_theme(findings: list[dict[str, Any]]) -> list[haive.agents.memory.search.deep_research.models.ResearchSection]

      Organize research findings into thematic sections.

      :param findings: List of research findings

      :returns: List of organized research sections


      .. autolink-examples:: organize_findings_by_theme
         :collapse:


   .. py:method:: process_deep_research(query: str, research_depth: int = 3, focus_areas: list[str] | None = None, max_sources: int = 50, include_fact_checking: bool = True, save_to_memory: bool = True) -> haive.agents.memory.search.deep_research.models.DeepResearchResponse
      :async:


      Process a deep research query with comprehensive analysis.

      :param query: Research query
      :param research_depth: Research depth level (1-5)
      :param focus_areas: Specific areas to focus on
      :param max_sources: Maximum sources to examine
      :param include_fact_checking: Include fact checking
      :param save_to_memory: Save results to memory

      :returns: Deep research response


      .. autolink-examples:: process_deep_research
         :collapse:


   .. py:method:: process_search(query: str, context: dict[str, Any] | None = None, save_to_memory: bool = True) -> haive.agents.memory.search.deep_research.models.DeepResearchResponse
      :async:


      Process a search query with default deep research settings.

      :param query: Search query
      :param context: Optional context
      :param save_to_memory: Whether to save to memory

      :returns: Deep research response


      .. autolink-examples:: process_search
         :collapse:


   .. py:attribute:: enable_kg
      :value: False



   .. py:attribute:: kg_transformer
      :value: None



.. py:data:: logger

