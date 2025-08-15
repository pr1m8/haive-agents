agents.research.open_perplexity.agent
=====================================

.. py:module:: agents.research.open_perplexity.agent


Attributes
----------

.. autoapisummary::

   agents.research.open_perplexity.agent.logger


Classes
-------

.. autoapisummary::

   agents.research.open_perplexity.agent.ResearchAgent


Module Contents
---------------

.. py:class:: ResearchAgent(config: haive.agents.research.open_perplexity.config.ResearchAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.research.open_perplexity.config.ResearchAgentConfig`\ ]


   Agent for performing deep research on any topic with dynamic document loader selection.

   Initialize the research agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchAgent
      :collapse:

   .. py:method:: _create_document_loader(loader_name: str, **kwargs) -> Any

      Create a document loader instance by name.


      .. autolink-examples:: _create_document_loader
         :collapse:


   .. py:method:: _discover_document_loaders() -> dict[str, Any]

      Discover available document loaders.


      .. autolink-examples:: _discover_document_loaders
         :collapse:


   .. py:method:: assess_confidence(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Assess confidence in research findings.


      .. autolink-examples:: assess_confidence
         :collapse:


   .. py:method:: check_section_completion(state: haive.agents.research.open_perplexity.state.ResearchState) -> str

      Check if all sections are completed or if more research is needed.


      .. autolink-examples:: check_section_completion
         :collapse:


   .. py:method:: compile_final_report(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Compile the final research report.


      .. autolink-examples:: compile_final_report
         :collapse:


   .. py:method:: consolidate_findings(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Consolidate findings from all sections.


      .. autolink-examples:: consolidate_findings
         :collapse:


   .. py:method:: evaluate_sources(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Evaluate and rate the reliability of retrieved sources.


      .. autolink-examples:: evaluate_sources
         :collapse:


   .. py:method:: execute_searches(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Execute searches using appropriate document loaders.


      .. autolink-examples:: execute_searches
         :collapse:


   .. py:method:: extract_topic(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Extract the research topic and question from user input.


      .. autolink-examples:: extract_topic
         :collapse:


   .. py:method:: generate_markdown_report(state: dict[str, Any]) -> str

      Generate a markdown report from the final state.


      .. autolink-examples:: generate_markdown_report
         :collapse:


   .. py:method:: generate_report_plan(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Generate a research report plan with appropriate sections.


      .. autolink-examples:: generate_report_plan
         :collapse:


   .. py:method:: generate_search_queries(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Generate search queries for the current section.


      .. autolink-examples:: generate_search_queries
         :collapse:


   .. py:method:: process_input(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Process the initial input and set up the research state.


      .. autolink-examples:: process_input
         :collapse:


   .. py:method:: recommend_document_loaders(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Recommend document loaders based on queries and data sources.


      .. autolink-examples:: recommend_document_loaders
         :collapse:


   .. py:method:: save_state_history(file_path: str | None = None) -> str

      Save the state history to a file.


      .. autolink-examples:: save_state_history
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the research workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the research state.


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:method:: write_section(state: haive.agents.research.open_perplexity.state.ResearchState) -> langgraph.types.Command

      Write the current section of the report.


      .. autolink-examples:: write_section
         :collapse:


   .. py:attribute:: _available_loaders


   .. py:attribute:: config


   .. py:attribute:: document_loaders


   .. py:attribute:: loaded_documents
      :value: []



   .. py:property:: rag_agent
      :type: Any


      Get the RAG agent for retrieval tasks.

      .. autolink-examples:: rag_agent
         :collapse:


   .. py:property:: react_agent
      :type: Any


      Get the ReAct agent for research tasks.

      .. autolink-examples:: react_agent
         :collapse:


   .. py:property:: retriever
      :type: Any


      Get or create the retriever from the vector store.

      .. autolink-examples:: retriever
         :collapse:


   .. py:property:: vectorstore
      :type: Any


      Get or create the vector store.

      .. autolink-examples:: vectorstore
         :collapse:


   .. py:attribute:: vectorstore_config


.. py:data:: logger

