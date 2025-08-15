agents.rag.agentic.agentic_rag_agent
====================================

.. py:module:: agents.rag.agentic.agentic_rag_agent

.. autoapi-nested-parse::

   Agentic RAG Multi-Agent System.

   This implements an advanced RAG system with document grading, query rewriting,
   and conditional routing between retrieval and web search.


   .. autolink-examples:: agents.rag.agentic.agentic_rag_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.agentic.agentic_rag_agent.AgenticRAGAgent
   agents.rag.agentic.agentic_rag_agent.AgenticRAGState


Module Contents
---------------

.. py:class:: AgenticRAGAgent

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Advanced Agentic RAG system with document grading and query refinement.

   This agent implements a sophisticated RAG workflow that includes:
   1. Initial retrieval from vector store
   2. Document relevance grading
   3. Query rewriting if documents aren't relevant
   4. Web search fallback
   5. Final answer generation

   .. rubric:: Example

   .. code-block:: python

       # Create agentic RAG agent
       agent = AgenticRAGAgent.create_default(
       name="agentic_rag",
       retriever_config=vector_store_config,
       use_web_search=True
       )

       # Process a query
       result = await agent.arun("What are the latest advances in quantum computing?")

       # The agent will:
       # 1. Retrieve documents from vector store
       # 2. Grade them for relevance
       # 3. Rewrite query if needed
       # 4. Use web search if local docs aren't sufficient
       # 5. Generate comprehensive answer


   .. autolink-examples:: AgenticRAGAgent
      :collapse:

   .. py:method:: _create_web_search_tool()
      :staticmethod:


      Create a mock web search tool for demonstration.


      .. autolink-examples:: _create_web_search_tool
         :collapse:


   .. py:method:: _generate_answer(state: AgenticRAGState) -> dict[str, Any]
      :async:


      Generate final answer using all available information.


      .. autolink-examples:: _generate_answer
         :collapse:


   .. py:method:: _grade_documents(state: AgenticRAGState) -> dict[str, Any]
      :async:


      Grade retrieved documents for relevance.


      .. autolink-examples:: _grade_documents
         :collapse:


   .. py:method:: _retrieve_documents(state: AgenticRAGState) -> dict[str, Any]
      :async:


      Retrieve documents using the RAG agent.


      .. autolink-examples:: _retrieve_documents
         :collapse:


   .. py:method:: _rewrite_query(state: AgenticRAGState) -> dict[str, Any]
      :async:


      Rewrite the query for better retrieval.


      .. autolink-examples:: _rewrite_query
         :collapse:


   .. py:method:: _route_after_grading(state: AgenticRAGState) -> str

      Determine next step after document grading.


      .. autolink-examples:: _route_after_grading
         :collapse:


   .. py:method:: _web_search(state: AgenticRAGState) -> dict[str, Any]
      :async:


      Perform web search as fallback.


      .. autolink-examples:: _web_search
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the Agentic RAG workflow graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_default(**kwargs) -> AgenticRAGAgent
      :classmethod:


      Create a default Agentic RAG agent.

      :param \*\*kwargs: Configuration options
                         - name: Agent name
                         - retriever_config: Retriever or vector store config (required)
                         - use_web_search: Whether to enable web search fallback
                         - temperature: LLM temperature
                         - engine: Custom AugLLMConfig if needed

      :returns: AgenticRAGAgent configured for advanced RAG


      .. autolink-examples:: create_default
         :collapse:


   .. py:attribute:: generator_agent
      :type:  haive.agents.simple.SimpleAgent | None
      :value: None



   .. py:attribute:: grader_agent
      :type:  Any | None
      :value: None



   .. py:attribute:: max_query_rewrites
      :type:  int
      :value: None



   .. py:attribute:: relevance_threshold
      :type:  float
      :value: None



   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig
      :value: None



   .. py:attribute:: rewriter_agent
      :type:  Any | None
      :value: None



   .. py:attribute:: use_web_search
      :type:  bool
      :value: None



   .. py:attribute:: web_search_agent
      :type:  haive.agents.rag.agentic.react_rag_agent.ReactRAGAgent | None
      :value: None



.. py:class:: AgenticRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State for the Agentic RAG workflow.


   .. autolink-examples:: AgenticRAGState
      :collapse:

   .. py:attribute:: all_documents_relevant
      :type:  bool
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: graded_documents
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: query_rewrite_count
      :type:  int
      :value: None



   .. py:attribute:: refined_query
      :type:  str
      :value: None



   .. py:attribute:: relevant_documents
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: use_web_search
      :type:  bool
      :value: None



   .. py:attribute:: web_search_results
      :type:  list[dict[str, Any]]
      :value: None



