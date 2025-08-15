agents.document_processing.agent
================================

.. py:module:: agents.document_processing.agent

.. autoapi-nested-parse::

   Comprehensive Document Processing Agent.

   This agent provides end-to-end document processing capabilities including:
   - Document fetching with ReactAgent + search tools
   - Auto-loading with bulk processing
   - Transform/split/annotate/embed pipeline
   - Advanced RAG features (refined queries, self-query, etc.)
   - State management and persistence

   The agent integrates all existing Haive document processing components into
   a unified, powerful system for document-based AI workflows.

   .. rubric:: Examples

   Basic document processing::

       agent = DocumentProcessingAgent()
       result = agent.process_query("Load and analyze reports from https://company.com/reports")

   Advanced RAG with custom retrieval::

       config = DocumentProcessingConfig(
           retrieval_strategy="self_query",
           query_refinement=True,
           annotation_enabled=True,
           embedding_model="text-embedding-3-large"
       )
       agent = DocumentProcessingAgent(config=config)
       result = agent.process_query("Find all financial projections from Q4 2024")

   Multi-source document processing::

       sources = [
           "/path/to/local/docs/",
           "https://wiki.company.com/procedures",
           "s3://bucket/documents/",
           {"url": "https://api.service.com/docs", "headers": {"Authorization": "Bearer token"}}
       ]
       agent = DocumentProcessingAgent()
       result = agent.process_sources(sources, query="Extract key insights")

   Author: Claude (Haive AI Agent Framework)
   Version: 1.0.0


   .. autolink-examples:: agents.document_processing.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.document_processing.agent.DocumentProcessingAgent
   agents.document_processing.agent.DocumentProcessingConfig
   agents.document_processing.agent.DocumentProcessingResult
   agents.document_processing.agent.DocumentProcessingState


Module Contents
---------------

.. py:class:: DocumentProcessingAgent(config: DocumentProcessingConfig | None = None, engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, name: str = 'document_processor')

   Comprehensive document processing agent with full pipeline capabilities.

   This agent provides a complete document processing pipeline including:
   1. Document Discovery & Fetching (ReactAgent + search tools)
   2. Auto-loading with bulk processing
   3. Transform/split/annotate/embed pipeline
   4. Advanced RAG features
   5. State management and persistence

   The agent integrates all existing Haive document processing components
   into a unified, powerful system for document-based AI workflows.

   Initialize the document processing agent.

   :param config: Configuration for document processing
   :param engine: LLM engine configuration
   :param name: Agent name for identification


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentProcessingAgent
      :collapse:

   .. py:method:: _annotate_documents(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Annotate documents with metadata and context.


      .. autolink-examples:: _annotate_documents
         :collapse:


   .. py:method:: _create_rag_agent() -> haive.agents.rag.base.agent.BaseRAGAgent

      Create RAG agent based on configuration.


      .. autolink-examples:: _create_rag_agent
         :collapse:


   .. py:method:: _discover_documents(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Discover relevant documents using search capabilities.


      .. autolink-examples:: _discover_documents
         :collapse:


   .. py:method:: _extract_knowledge_graph(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Extract knowledge graph from documents.


      .. autolink-examples:: _extract_knowledge_graph
         :collapse:


   .. py:method:: _extract_sources(state: DocumentProcessingState) -> list[dict[str, Any]]

      Extract source information for result.


      .. autolink-examples:: _extract_sources
         :collapse:


   .. py:method:: _extract_sources_from_search(search_result: str) -> list[str | dict[str, Any]]

      Extract sources from search agent result.


      .. autolink-examples:: _extract_sources_from_search
         :collapse:


   .. py:method:: _format_context_for_response(state: DocumentProcessingState) -> str

      Format context information for response generation.


      .. autolink-examples:: _format_context_for_response
         :collapse:


   .. py:method:: _generate_metadata(state: DocumentProcessingState) -> dict[str, Any]

      Generate metadata for processing result.


      .. autolink-examples:: _generate_metadata
         :collapse:


   .. py:method:: _generate_response(state: DocumentProcessingState) -> str
      :async:


      Generate final response based on processed documents and RAG results.


      .. autolink-examples:: _generate_response
         :collapse:


   .. py:method:: _init_components()

      Initialize all agent components.


      .. autolink-examples:: _init_components
         :collapse:


   .. py:method:: _load_documents(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Load documents using auto-loader with bulk processing.


      .. autolink-examples:: _load_documents
         :collapse:


   .. py:method:: _process_documents(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Process documents through annotation, summarization, and other pipelines.


      .. autolink-examples:: _process_documents
         :collapse:


   .. py:method:: _rag_processing(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Process query through RAG pipeline.


      .. autolink-examples:: _rag_processing
         :collapse:


   .. py:method:: _refine_query(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Refine query for better retrieval.


      .. autolink-examples:: _refine_query
         :collapse:


   .. py:method:: _summarize_documents(state: DocumentProcessingState) -> DocumentProcessingState
      :async:


      Summarize documents using map-branch summarization.


      .. autolink-examples:: _summarize_documents
         :collapse:


   .. py:method:: get_capabilities() -> dict[str, Any]

      Get agent capabilities and configuration.


      .. autolink-examples:: get_capabilities
         :collapse:


   .. py:method:: process_query(query: str, sources: list[str | dict[str, Any]] | None = None) -> DocumentProcessingResult
      :async:


      Process a query with comprehensive document processing pipeline.

      :param query: The user query to process
      :param sources: Optional list of specific sources to use

      :returns: DocumentProcessingResult with comprehensive results


      .. autolink-examples:: process_query
         :collapse:


   .. py:method:: process_sources(sources: list[str | dict[str, Any]], query: str) -> DocumentProcessingResult
      :async:


      Process specific sources with a query.

      :param sources: List of sources to process
      :param query: Query to process against the sources

      :returns: DocumentProcessingResult with results


      .. autolink-examples:: process_sources
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: engine


   .. py:attribute:: name
      :value: 'document_processor'



.. py:class:: DocumentProcessingConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for comprehensive document processing.

   .. attribute:: # Core Processing

      

   .. attribute:: auto_loader_config

      Configuration for document auto-loading

   .. attribute:: enable_bulk_processing

      Enable concurrent bulk document processing

   .. attribute:: max_concurrent_loads

      Maximum concurrent document loads

   .. attribute:: # Search & Retrieval

      

   .. attribute:: search_enabled

      Enable web search for document discovery

   .. attribute:: search_depth

      Search depth for web queries ("basic" or "advanced")

   .. attribute:: retrieval_strategy

      Strategy for document retrieval

   .. attribute:: retrieval_config

      Configuration for retrieval components

   .. attribute:: # Query Processing

      

   .. attribute:: query_refinement

      Enable query refinement for better results

   .. attribute:: multi_query_enabled

      Enable multiple query variations

   .. attribute:: query_expansion

      Enable query expansion techniques

   .. attribute:: # Document Processing

      

   .. attribute:: annotation_enabled

      Enable document annotation

   .. attribute:: summarization_enabled

      Enable document summarization

   .. attribute:: kg_extraction_enabled

      Enable knowledge graph extraction

   .. attribute:: # RAG Configuration

      

   .. attribute:: rag_strategy

      RAG strategy to use

   .. attribute:: context_window_size

      Context window size for RAG

   .. attribute:: chunk_size

      Chunk size for document splitting

   .. attribute:: chunk_overlap

      Overlap between chunks

   .. attribute:: # Embedding & Vectorization

      

   .. attribute:: embedding_model

      Embedding model to use

   .. attribute:: vector_store_config

      Vector store configuration

   .. attribute:: # Performance

      

   .. attribute:: enable_caching

      Enable document caching

   .. attribute:: cache_ttl

      Cache time-to-live in seconds

   .. attribute:: enable_streaming

      Enable streaming responses

   .. attribute:: # Output

      

   .. attribute:: structured_output

      Enable structured output generation

   .. attribute:: response_format

      Format for agent responses

   .. attribute:: include_sources

      Include source information in responses

   .. attribute:: include_metadata

      Include processing metadata

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentProcessingConfig
      :collapse:

   .. py:attribute:: annotation_enabled
      :type:  bool
      :value: None



   .. py:attribute:: auto_loader_config
      :type:  haive.core.engine.document.loaders.auto_loader.AutoLoaderConfig | None
      :value: None



   .. py:attribute:: cache_ttl
      :type:  int
      :value: None



   .. py:attribute:: chunk_overlap
      :type:  int
      :value: None



   .. py:attribute:: chunk_size
      :type:  int
      :value: None



   .. py:attribute:: context_window_size
      :type:  int
      :value: None



   .. py:attribute:: embedding_model
      :type:  str
      :value: None



   .. py:attribute:: enable_bulk_processing
      :type:  bool
      :value: None



   .. py:attribute:: enable_caching
      :type:  bool
      :value: None



   .. py:attribute:: enable_streaming
      :type:  bool
      :value: None



   .. py:attribute:: include_metadata
      :type:  bool
      :value: None



   .. py:attribute:: include_sources
      :type:  bool
      :value: None



   .. py:attribute:: kg_extraction_enabled
      :type:  bool
      :value: None



   .. py:attribute:: max_concurrent_loads
      :type:  int
      :value: None



   .. py:attribute:: multi_query_enabled
      :type:  bool
      :value: None



   .. py:attribute:: query_expansion
      :type:  bool
      :value: None



   .. py:attribute:: query_refinement
      :type:  bool
      :value: None



   .. py:attribute:: rag_strategy
      :type:  str
      :value: None



   .. py:attribute:: response_format
      :type:  str
      :value: None



   .. py:attribute:: retrieval_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieval_strategy
      :type:  str
      :value: None



   .. py:attribute:: search_depth
      :type:  str
      :value: None



   .. py:attribute:: search_enabled
      :type:  bool
      :value: None



   .. py:attribute:: structured_output
      :type:  bool
      :value: None



   .. py:attribute:: summarization_enabled
      :type:  bool
      :value: None



   .. py:attribute:: vector_store_config
      :type:  dict[str, Any]
      :value: None



.. py:class:: DocumentProcessingResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from document processing operation.

   .. attribute:: response

      Main response content

   .. attribute:: sources

      List of source documents used

   .. attribute:: metadata

      Processing metadata

   .. attribute:: documents

      Processed documents

   .. attribute:: query_info

      Information about query processing

   .. attribute:: timing

      Timing information

   .. attribute:: statistics

      Processing statistics

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentProcessingResult
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: query_info
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: response
      :type:  str
      :value: None



   .. py:attribute:: sources
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: statistics
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: timing
      :type:  dict[str, float]
      :value: None



.. py:class:: DocumentProcessingState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State for document processing operations.

   Extends MessagesState with document-specific fields for tracking
   document processing workflows.


   .. autolink-examples:: DocumentProcessingState
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: annotation_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: context_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: current_sources
      :type:  list[str | dict[str, Any]]
      :value: None



   .. py:attribute:: document_state
      :type:  haive.core.schema.prebuilt.document_state.DocumentState
      :value: None



   .. py:attribute:: last_operation
      :type:  str
      :value: None



   .. py:attribute:: operation_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: processed_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: processing_stage
      :type:  str
      :value: None



   .. py:attribute:: refined_queries
      :type:  list[str]
      :value: None



   .. py:attribute:: retrieval_results
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: search_results
      :type:  list[dict[str, Any]]
      :value: None



