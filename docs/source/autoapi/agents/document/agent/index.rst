agents.document.agent
=====================

.. py:module:: agents.document.agent

.. autoapi-nested-parse::

   Document Agent for comprehensive document processing pipeline.

   from typing import Any
   This module provides the DocumentAgent class which implements the full document processing
   pipeline: FETCH -> LOAD -> TRANSFORM -> SPLIT -> ANNOTATE -> EMBED -> STORE -> RETRIEVE.

   The agent leverages the Document Engine from haive-core to handle 97+ document types
   and sources with advanced processing capabilities including chunking, metadata
   extraction, and parallel processing.

   Classes:
       DocumentAgent: Main agent for document processing pipeline
       DocumentProcessingResult: Structured result from document processing

   .. rubric:: Examples

   Basic usage::

       from haive.agents.document import DocumentAgent
       from haive.core.engine.document import DocumentEngineConfig

       agent = DocumentAgent(name="doc_processor")
       result = agent.process_sources(["document.pdf"])
       print(f"Processed {result.total_documents} documents")

   Advanced configuration::

       config = DocumentEngineConfig(
           chunking_strategy=ChunkingStrategy.SEMANTIC,
           parallel_processing=True,
           max_workers=8
       )
       agent = DocumentAgent(name="enterprise_processor", engine=config)
       result = agent.process_directory("/path/to/documents")

   .. seealso::

      - :class:`~haive.core.engine.document.DocumentEngine`: Core processing engine
      - :class:`~haive.agents.base.Agent`: Base agent class


   .. autolink-examples:: agents.document.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document.agent.logger


Classes
-------

.. autoapisummary::

   agents.document.agent.DocumentAgent
   agents.document.agent.DocumentProcessingResult


Module Contents
---------------

.. py:class:: DocumentAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Comprehensive Document Processing Agent.

   This agent implements the complete document processing pipeline for enterprise-grade
   document ingestion and analysis. It provides a unified interface for the full
   document lifecycle from source discovery to retrievable storage.

   ## Processing Pipeline:

   1. **FETCH**: Discover and validate document sources (files, URLs, databases, cloud)
   2. **LOAD**: Load documents using 97+ specialized loaders with auto-detection
   3. **TRANSFORM**: Normalize content, extract metadata, detect language/encoding
   4. **SPLIT**: Apply intelligent chunking strategies (recursive, semantic, paragraph)
   5. **ANNOTATE**: Extract and enrich metadata, apply content classification
   6. **EMBED**: Generate vector embeddings for semantic search (optional)
   7. **STORE**: Persist to vector databases and document stores (optional)
   8. **RETRIEVE**: Enable search and retrieval capabilities (optional)

   ## Key Features:

   - **Universal Source Support**: 97+ document sources including files, URLs, databases, cloud storage
   - **Intelligent Processing**: Auto-detection of source types and optimal processing strategies
   - **Parallel Processing**: Multi-threaded processing for high-throughput scenarios
   - **Advanced Chunking**: Multiple strategies including recursive, semantic, and paragraph-based
   - **Metadata Enrichment**: Comprehensive metadata extraction and annotation
   - **Error Resilience**: Graceful error handling with detailed reporting
   - **Extensible Pipeline**: Configurable stages for custom processing workflows

   ## Configuration Options:

   :param engine: Document engine configuration for processing pipeline
   :param # Source Configuration:
   :param source_types: List of allowed source types (files, URLs, databases, etc.)
   :param auto_detect_sources: Whether to auto-detect source types
   :param max_sources: Maximum number of sources to process
   :param # Processing Configuration:
   :param processing_strategy: Processing strategy (simple, enhanced, parallel)
   :param parallel_processing: Enable parallel processing
   :param max_workers: Maximum worker threads for parallel processing
   :param # Chunking Configuration:
   :param chunking_strategy: Strategy for document chunking
   :param chunk_size: Size of chunks in characters
   :param chunk_overlap: Overlap between consecutive chunks
   :param # Content Processing:
   :param normalize_content: Whether to normalize content (whitespace, encoding)
   :param extract_metadata: Whether to extract document metadata
   :param detect_language: Whether to detect document language
   :param # Pipeline Stages:
   :type # Pipeline Stages: optional
   :param enable_embedding: Whether to generate embeddings
   :param enable_storage: Whether to store in vector database
   :param enable_retrieval: Whether to enable retrieval capabilities
   :param # Error Handling:
   :param raise_on_error: Whether to raise exceptions on errors
   :param skip_invalid: Whether to skip invalid documents

   ## Example Usage:

   ### Basic Document Processing:
   .. code-block:: python

       from haive.agents.document import DocumentAgent
       from haive.core.engine.document import DocumentEngineConfig

       # Create agent for PDF processing
       agent = DocumentAgent(
       engine=DocumentEngineConfig(
       chunking_strategy=ChunkingStrategy.PARAGRAPH,
       chunk_size=1000,
       parallel_processing=True
       )
       )

       # Process a single document
       result = agent.invoke({
       "source": "document.pdf",
       "extract_metadata": True
       })


   ### Multi-Source Processing:
   .. code-block:: python

       # Process multiple sources with different types
       agent = DocumentAgent.create_for_enterprise()

       result = agent.process_sources([
       "documents/reports/",  # Directory
       "https://example.com/api/docs",  # Web API
       "s3://bucket/documents/",  # Cloud storage
       "postgresql://db/documents"  # Database
       ])


   ### Custom Pipeline Configuration:
   .. code-block:: python

       # Configure custom processing pipeline
       agent = DocumentAgent(
       processing_strategy=ProcessingStrategy.ENHANCED,
       chunking_strategy=ChunkingStrategy.SEMANTIC,
       chunk_size=1500,
       enable_embedding=True,
       enable_storage=True,
       normalize_content=True,
       detect_language=True
       )


   ## Document Source Types Supported:

   - **Files**: PDF, DOCX, TXT, HTML, MD, JSON, CSV, XML, YAML, and 50+ more
   - **Web**: HTTP/HTTPS URLs, APIs, web scraping, RSS feeds
   - **Cloud**: AWS S3, Google Cloud Storage, Azure Blob, Dropbox, Box
   - **Databases**: PostgreSQL, MySQL, MongoDB, Elasticsearch, and 15+ more
   - **Chat/Messaging**: Slack, Discord, WhatsApp, Telegram exports
   - **Knowledge Bases**: Notion, Confluence, Obsidian, Roam Research
   - **Version Control**: Git repositories, GitHub, GitLab
   - **Archives**: ZIP, TAR, 7Z with recursive extraction

   ## Processing Strategies:

   - **Simple**: Basic loading and chunking for development/testing
   - **Enhanced**: Full metadata extraction, content normalization, language detection
   - **Parallel**: Multi-threaded processing for high-throughput production use

   ## Chunking Strategies:

   - **None**: No chunking, process documents as whole units
   - **Fixed Size**: Fixed character-based chunks with overlap
   - **Recursive**: Hierarchical splitting using multiple separators
   - **Paragraph**: Split on paragraph boundaries with size limits
   - **Sentence**: Split on sentence boundaries with size limits
   - **Semantic**: AI-powered semantic boundary detection (experimental)

   .. note::

      This agent integrates with the haive-core Document Engine which provides
      the underlying processing capabilities. The agent adds workflow orchestration,
      error handling, and result aggregation on top of the engine.


   .. autolink-examples:: DocumentAgent
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _aggregate_results(engine_results: list[haive.core.engine.document.config.DocumentOutput], sources: list[str], total_time: float) -> DocumentProcessingResult

      Aggregate multiple engine results into a comprehensive result.


      .. autolink-examples:: _aggregate_results
         :collapse:


   .. py:method:: _convert_engine_result_to_agent_result(engine_result: haive.core.engine.document.config.DocumentOutput, sources: list[str]) -> DocumentProcessingResult

      Convert a single engine result to agent result format.


      .. autolink-examples:: _convert_engine_result_to_agent_result
         :collapse:


   .. py:method:: _get_pipeline_stages() -> list[str]

      Get list of enabled pipeline stages.


      .. autolink-examples:: _get_pipeline_stages
         :collapse:


   .. py:method:: _register_engine_in_registry() -> None

      Register the engine in EngineRegistry.


      .. autolink-examples:: _register_engine_in_registry
         :collapse:


   .. py:method:: _sync_configuration_to_engine() -> None

      Sync agent configuration to the document engine.


      .. autolink-examples:: _sync_configuration_to_engine
         :collapse:


   .. py:method:: analyze_source_structure(source: str, **kwargs) -> dict[str, Any]

      Analyze the structure of a source without full processing.

      :param source: Source to analyze
      :param \*\*kwargs: Additional analysis options

      :returns: Dictionary with source structure analysis


      .. autolink-examples:: analyze_source_structure
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the document processing graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_for_databases(name: str = 'Database Document Agent', **kwargs) -> DocumentAgent
      :classmethod:


      Create DocumentAgent optimized for database document processing.


      .. autolink-examples:: create_for_databases
         :collapse:


   .. py:method:: create_for_enterprise(name: str = 'Enterprise Document Agent', **kwargs) -> DocumentAgent
      :classmethod:


      Create DocumentAgent optimized for enterprise-scale processing.


      .. autolink-examples:: create_for_enterprise
         :collapse:


   .. py:method:: create_for_pdfs(name: str = 'PDF Document Agent', chunk_size: int = 1000, **kwargs) -> DocumentAgent
      :classmethod:


      Create DocumentAgent optimized for PDF processing.


      .. autolink-examples:: create_for_pdfs
         :collapse:


   .. py:method:: create_for_research(name: str = 'Research Document Agent', **kwargs) -> DocumentAgent
      :classmethod:


      Create DocumentAgent optimized for research document processing.


      .. autolink-examples:: create_for_research
         :collapse:


   .. py:method:: create_for_web_scraping(name: str = 'Web Scraping Agent', **kwargs) -> DocumentAgent
      :classmethod:


      Create DocumentAgent optimized for web content processing.


      .. autolink-examples:: create_for_web_scraping
         :collapse:


   .. py:method:: process_cloud_storage(cloud_paths: list[str], **kwargs) -> DocumentProcessingResult

      Process documents from cloud storage.

      :param cloud_paths: List of cloud storage paths (s3://, gs://, etc.)
      :param \*\*kwargs: Additional processing options

      :returns: DocumentProcessingResult with cloud processing results


      .. autolink-examples:: process_cloud_storage
         :collapse:


   .. py:method:: process_directory(directory_path: str, recursive: bool = True, include_patterns: list[str] | None = None, exclude_patterns: list[str] | None = None, **kwargs) -> DocumentProcessingResult

      Process all documents in a directory.

      :param directory_path: Path to directory
      :param recursive: Whether to process subdirectories
      :param include_patterns: Glob patterns for files to include
      :param exclude_patterns: Glob patterns for files to exclude
      :param \*\*kwargs: Additional processing options

      :returns: DocumentProcessingResult with directory processing results


      .. autolink-examples:: process_directory
         :collapse:


   .. py:method:: process_sources(sources: str | list[str], **kwargs) -> DocumentProcessingResult

      Process multiple document sources through the full pipeline.

      :param sources: Single source or list of sources to process
      :param \*\*kwargs: Additional processing options

      :returns: DocumentProcessingResult with comprehensive pipeline results


      .. autolink-examples:: process_sources
         :collapse:


   .. py:method:: process_urls(urls: list[str], **kwargs) -> DocumentProcessingResult

      Process documents from web URLs.

      :param urls: List of URLs to process
      :param \*\*kwargs: Additional processing options

      :returns: DocumentProcessingResult with web processing results


      .. autolink-examples:: process_urls
         :collapse:


   .. py:method:: setup_agent() -> None

      Configure the document engine with agent settings.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: validate_chunk_overlap(v, info) -> Any
      :classmethod:


      Ensure chunk overlap is less than chunk size.


      .. autolink-examples:: validate_chunk_overlap
         :collapse:


   .. py:method:: validate_engine_type(v) -> Any
      :classmethod:


      Ensure engine is DocumentEngineConfig.


      .. autolink-examples:: validate_engine_type
         :collapse:


   .. py:attribute:: allowed_source_types
      :type:  list[haive.core.engine.document.config.DocumentSourceType]
      :value: None



   .. py:attribute:: auto_detect_sources
      :type:  bool
      :value: None



   .. py:attribute:: chunk_overlap
      :type:  int
      :value: None



   .. py:attribute:: chunk_size
      :type:  int
      :value: None



   .. py:attribute:: chunking_strategy
      :type:  haive.core.engine.document.config.ChunkingStrategy
      :value: None



   .. py:attribute:: detect_language
      :type:  bool
      :value: None



   .. py:attribute:: enable_embedding
      :type:  bool
      :value: None



   .. py:attribute:: enable_retrieval
      :type:  bool
      :value: None



   .. py:attribute:: enable_storage
      :type:  bool
      :value: None



   .. py:attribute:: engine
      :type:  haive.core.engine.document.DocumentEngineConfig
      :value: None



   .. py:attribute:: extract_metadata
      :type:  bool
      :value: None



   .. py:attribute:: max_sources
      :type:  int | None
      :value: None



   .. py:attribute:: max_workers
      :type:  int
      :value: None



   .. py:attribute:: normalize_content
      :type:  bool
      :value: None



   .. py:attribute:: parallel_processing
      :type:  bool
      :value: None



   .. py:attribute:: processing_strategy
      :type:  haive.core.engine.document.config.ProcessingStrategy
      :value: None



   .. py:attribute:: raise_on_error
      :type:  bool
      :value: None



   .. py:attribute:: skip_invalid
      :type:  bool
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: DocumentProcessingResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive result of document processing pipeline.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentProcessingResult
      :collapse:

   .. py:attribute:: annotated_chunks
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: average_chunk_size
      :type:  float
      :value: None



   .. py:attribute:: chunking_strategy
      :type:  str
      :value: None



   .. py:attribute:: document_chunks
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: document_formats
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: embedded_chunks
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: failed_sources
      :type:  int
      :value: None



   .. py:attribute:: fetched_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: loaded_documents
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: pipeline_strategy
      :type:  str
      :value: None



   .. py:attribute:: processing_errors
      :type:  list[str]
      :value: None



   .. py:attribute:: processing_time
      :type:  float
      :value: None



   .. py:attribute:: source_types
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: stored_documents
      :type:  list[str]
      :value: None



   .. py:attribute:: successful_sources
      :type:  int
      :value: None



   .. py:attribute:: total_annotations
      :type:  int
      :value: None



   .. py:attribute:: total_characters
      :type:  int
      :value: None



   .. py:attribute:: total_chunks
      :type:  int
      :value: None



   .. py:attribute:: total_documents
      :type:  int
      :value: None



   .. py:attribute:: total_sources
      :type:  int
      :value: None



   .. py:attribute:: total_words
      :type:  int
      :value: None



   .. py:attribute:: transformed_documents
      :type:  list[dict[str, Any]]
      :value: None



.. py:data:: logger

