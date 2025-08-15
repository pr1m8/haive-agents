agents.rag.agentic
==================

.. py:module:: agents.rag.agentic

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: agents.rag.agentic
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/rag/agentic/agent/index
   /autoapi/agents/rag/agentic/agentic_rag_agent/index
   /autoapi/agents/rag/agentic/document_grader/index
   /autoapi/agents/rag/agentic/query_rewriter/index
   /autoapi/agents/rag/agentic/react_rag_agent/index


Classes
-------

.. autoapisummary::

   agents.rag.agentic.AgenticRAGAgent
   agents.rag.agentic.AgenticRAGState
   agents.rag.agentic.DocumentGrade
   agents.rag.agentic.QueryRewrite
   agents.rag.agentic.ReactRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.agentic.create_agentic_rag_agent
   agents.rag.agentic.create_document_grader_agent
   agents.rag.agentic.create_memory_aware_agentic_rag
   agents.rag.agentic.create_query_rewriter_agent


Package Contents
----------------

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



.. py:class:: DocumentGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Grade for document relevance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentGrade
      :collapse:

   .. py:attribute:: binary_score
      :type:  Literal['yes', 'no']
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: QueryRewrite(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Rewritten query for better retrieval.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryRewrite
      :collapse:

   .. py:attribute:: changes_made
      :type:  str
      :value: None



   .. py:attribute:: rewritten_query
      :type:  str
      :value: None



.. py:class:: ReactRAGAgent

   Bases: :py:obj:`haive.agents.react.ReactAgent`


   Enhanced ReactAgent with a dedicated retrieval node and intelligent routing.

   This agent extends ReactAgent by adding a retrieval node to the graph that works
   alongside regular tool nodes. The agent can route between:
   1. Regular tool execution (calculator, web search, etc.)
   2. Retrieval from vector store/knowledge base
   3. Both in combination

   The routing is handled by the LLM through a special retriever tool that triggers
   the retrieval node when called.

   .. rubric:: Example

   .. code-block:: python

       # Create ReactRAG agent with both types of tools
       agent = ReactRAGAgent.create_default(
       name="react_rag",
       retriever_config=vector_store_config,
       tools=[calculator_tool, web_search_tool],
       temperature=0.1
       )

       # The agent will intelligently decide whether to:
       # 1. Use retriever for knowledge queries
       # 2. Use tools for computational/action queries
       # 3. Use both when needed

       result = await agent.arun("What is the capital of France?")  # Uses retriever
       result = await agent.arun("Calculate 15 * 23")  # Uses calculator tool
       result = await agent.arun("Search for Python tutorials")  # Uses web search


   .. autolink-examples:: ReactRAGAgent
      :collapse:

   .. py:method:: _create_retriever_tool(retriever_config: haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig) -> langchain_core.tools.Tool
      :staticmethod:


      Create a retriever tool that triggers the retrieval node.

      This tool doesn't actually perform retrieval - it just signals
      that retrieval should happen via the dedicated retrieval node.

      :param retriever_config: The retriever or vector store configuration

      :returns: Tool that triggers the retrieval node


      .. autolink-examples:: _create_retriever_tool
         :collapse:


   .. py:method:: _route_to_retrieval_or_tools(state) -> str

      Route to retrieval node, tool node, or end based on agent output.


      .. autolink-examples:: _route_to_retrieval_or_tools
         :collapse:


   .. py:method:: add_retriever_tool(retriever_config: haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig) -> None

      Add or update the retriever tool and rebuild graph.

      :param retriever_config: New retriever configuration


      .. autolink-examples:: add_retriever_tool
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the enhanced React graph with retrieval node.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_default(**kwargs) -> ReactRAGAgent
      :classmethod:


      Create a default ReactRAG agent with retriever and tools.

      :param \*\*kwargs: Configuration options
                         - name: Agent name
                         - retriever_config: Retriever or vector store config
                         - tools: List of regular tools
                         - temperature: LLM temperature
                         - routing_strategy: How to route between retriever and tools
                         - engine: Custom AugLLMConfig if needed

      :returns: ReactRAGAgent configured for RAG with tools


      .. autolink-examples:: create_default
         :collapse:


   .. py:method:: from_vectorstore(vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, **kwargs) -> ReactRAGAgent
      :classmethod:


      Create ReactRAG agent from a vector store configuration.

      :param vector_store_config: Vector store configuration
      :param \*\*kwargs: Additional agent configuration

      :returns: ReactRAGAgent with retriever tool


      .. autolink-examples:: from_vectorstore
         :collapse:


   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig | None
      :value: None



   .. py:attribute:: routing_strategy
      :type:  str
      :value: None



   .. py:attribute:: use_retriever_for_knowledge
      :type:  bool
      :value: None



.. py:function:: create_agentic_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, embedding_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG agent with sensible defaults.


   .. autolink-examples:: create_agentic_rag_agent
      :collapse:

.. py:function:: create_document_grader_agent(name: str = 'document_grader', temperature: float = 0.0, **kwargs) -> haive.agents.simple.SimpleAgent

   Create a document grader agent using direct SimpleAgent instantiation.

   :param name: Agent name (default: "document_grader")
   :param temperature: LLM temperature (default: 0.0 for consistency)
   :param \*\*kwargs: Additional configuration options

   :returns: SimpleAgent configured for document grading

   .. rubric:: Example

   .. code-block:: python

       # Create grader agent
       grader = create_document_grader_agent(
       name="doc_grader",
       temperature=0.0
       )

       # Grade documents
       result = await grader.arun({
       "query": "What is quantum computing?",
       "documents": [
       {"content": "Quantum computing uses quantum mechanics...", "id": "doc1"},
       {"content": "Classical computing uses binary digits...", "id": "doc2"}
       ]
       })

       # Access results
       for decision in result.document_decisions:
       print(f"Document {decision.document_id}: {decision.decision}")
       print(f"Reason: {decision.justification}")


   .. autolink-examples:: create_document_grader_agent
      :collapse:

.. py:function:: create_memory_aware_agentic_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig, memory_config: Any | None = None, **kwargs) -> AgenticRAGAgent

   Create agentic RAG with long-term memory capabilities.


   .. autolink-examples:: create_memory_aware_agentic_rag
      :collapse:

.. py:function:: create_query_rewriter_agent(name: str = 'query_rewriter', temperature: float = 0.7, **kwargs) -> haive.agents.simple.SimpleAgent

   Create a query rewriter agent using direct SimpleAgent instantiation.

   :param name: Agent name (default: "query_rewriter")
   :param temperature: LLM temperature (default: 0.7 for creativity)
   :param \*\*kwargs: Additional configuration options

   :returns: SimpleAgent configured for query refinement

   .. rubric:: Example

   .. code-block:: python

       # Create query rewriter agent
       rewriter = create_query_rewriter_agent(
       name="query_rewriter",
       temperature=0.7
       )

       # Rewrite a query
       result = await rewriter.arun({
       "query": "quantum computing basics"
       })

       # Access results
       print(f"Original: {result.original_query}")
       print(f"Best rewrite: {result.best_refined_query}")
       for suggestion in result.refinement_suggestions:
       print(f"- {suggestion.refined_query} ({suggestion.improvement_type})")


   .. autolink-examples:: create_query_rewriter_agent
      :collapse:

