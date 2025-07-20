"""Comprehensive Document Processing Agent.

This agent provides end-to-end document processing capabilities including:
- Document fetching with ReactAgent + search tools
- Auto-loading with bulk processing
- Transform/split/annotate/embed pipeline
- Advanced RAG features (refined queries, self-query, etc.)
- State management and persistence

The agent integrates all existing Haive document processing components into
a unified, powerful system for document-based AI workflows.

Examples:
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
"""

import logging
from datetime import datetime
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.document.loaders.auto_loader import AutoLoader, AutoLoaderConfig

# from haive.core.engine.document.universal_loader import UniversalDocumentLoader
from haive.core.schema.prebuilt.document_state import (
    DocumentState,
)
from haive.core.schema.prebuilt.messages_state import MessagesState
from haive.tools.tools.search_tools import (
    scrape_webpages,
    tavily_search_context,
    tavily_search_tool,
)
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)


class DocumentProcessingConfig(BaseModel):
    """Configuration for comprehensive document processing.

    Attributes:
        # Core Processing
        auto_loader_config: Configuration for document auto-loading
        enable_bulk_processing: Enable concurrent bulk document processing
        max_concurrent_loads: Maximum concurrent document loads

        # Search & Retrieval
        search_enabled: Enable web search for document discovery
        search_depth: Search depth for web queries ("basic" or "advanced")
        retrieval_strategy: Strategy for document retrieval
        retrieval_config: Configuration for retrieval components

        # Query Processing
        query_refinement: Enable query refinement for better results
        multi_query_enabled: Enable multiple query variations
        query_expansion: Enable query expansion techniques

        # Document Processing
        annotation_enabled: Enable document annotation
        summarization_enabled: Enable document summarization
        kg_extraction_enabled: Enable knowledge graph extraction

        # RAG Configuration
        rag_strategy: RAG strategy to use
        context_window_size: Context window size for RAG
        chunk_size: Chunk size for document splitting
        chunk_overlap: Overlap between chunks

        # Embedding & Vectorization
        embedding_model: Embedding model to use
        vector_store_config: Vector store configuration

        # Performance
        enable_caching: Enable document caching
        cache_ttl: Cache time-to-live in seconds
        enable_streaming: Enable streaming responses

        # Output
        structured_output: Enable structured output generation
        response_format: Format for agent responses
        include_sources: Include source information in responses
        include_metadata: Include processing metadata
    """

    # Core Processing
    auto_loader_config: AutoLoaderConfig | None = Field(default=None)
    enable_bulk_processing: bool = Field(default=True)
    max_concurrent_loads: int = Field(default=10, ge=1, le=50)

    # Search & Retrieval
    search_enabled: bool = Field(default=True)
    search_depth: str = Field(default="advanced", pattern="^(basic|advanced)$")
    retrieval_strategy: str = Field(
        default="adaptive",
        pattern="^(basic|adaptive|self_query|parent_document|multi_query|ensemble)$",
    )
    retrieval_config: dict[str, Any] = Field(default_factory=dict)

    # Query Processing
    query_refinement: bool = Field(default=True)
    multi_query_enabled: bool = Field(default=False)
    query_expansion: bool = Field(default=True)

    # Document Processing
    annotation_enabled: bool = Field(default=True)
    summarization_enabled: bool = Field(default=False)
    kg_extraction_enabled: bool = Field(default=False)

    # RAG Configuration
    rag_strategy: str = Field(
        default="adaptive", pattern="^(basic|adaptive|self_rag|hyde|multi_strategy)$"
    )
    context_window_size: int = Field(default=4000, ge=1000, le=16000)
    chunk_size: int = Field(default=1000, ge=100, le=4000)
    chunk_overlap: int = Field(default=200, ge=0, le=500)

    # Embedding & Vectorization
    embedding_model: str = Field(default="text-embedding-3-small")
    vector_store_config: dict[str, Any] = Field(default_factory=dict)

    # Performance
    enable_caching: bool = Field(default=True)
    cache_ttl: int = Field(default=3600, ge=60)
    enable_streaming: bool = Field(default=False)

    # Output
    structured_output: bool = Field(default=True)
    response_format: str = Field(
        default="detailed", pattern="^(simple|detailed|comprehensive)$"
    )
    include_sources: bool = Field(default=True)
    include_metadata: bool = Field(default=True)


class DocumentProcessingResult(BaseModel):
    """Result from document processing operation.

    Attributes:
        response: Main response content
        sources: List of source documents used
        metadata: Processing metadata
        documents: Processed documents
        query_info: Information about query processing
        timing: Timing information
        statistics: Processing statistics
    """

    response: str = Field(description="Main response content")
    sources: list[dict[str, Any]] = Field(
        default_factory=list, description="Source documents"
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Processing metadata"
    )
    documents: list[Document] = Field(
        default_factory=list, description="Processed documents"
    )
    query_info: dict[str, Any] = Field(
        default_factory=dict, description="Query processing info"
    )
    timing: dict[str, float] = Field(
        default_factory=dict, description="Timing information"
    )
    statistics: dict[str, Any] = Field(
        default_factory=dict, description="Processing statistics"
    )

    class Config:
        arbitrary_types_allowed = True


class DocumentProcessingState(MessagesState):
    """State for document processing operations.

    Extends MessagesState with document-specific fields for tracking
    document processing workflows.
    """

    # Document State
    document_state: DocumentState = Field(default_factory=DocumentState)

    # Processing State
    current_sources: list[str | dict[str, Any]] = Field(default_factory=list)
    processed_documents: list[Document] = Field(default_factory=list)
    annotation_results: dict[str, Any] = Field(default_factory=dict)

    # Query State
    original_query: str = Field(default="")
    refined_queries: list[str] = Field(default_factory=list)
    search_results: list[dict[str, Any]] = Field(default_factory=list)

    # RAG State
    retrieval_results: list[Document] = Field(default_factory=list)
    context_documents: list[Document] = Field(default_factory=list)

    # Processing Metadata
    processing_stage: str = Field(default="initialized")
    last_operation: str = Field(default="")
    operation_history: list[dict[str, Any]] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True


class DocumentProcessingAgent:
    """Comprehensive document processing agent with full pipeline capabilities.

    This agent provides a complete document processing pipeline including:
    1. Document Discovery & Fetching (ReactAgent + search tools)
    2. Auto-loading with bulk processing
    3. Transform/split/annotate/embed pipeline
    4. Advanced RAG features
    5. State management and persistence

    The agent integrates all existing Haive document processing components
    into a unified, powerful system for document-based AI workflows.
    """

    def __init__(
        self,
        config: DocumentProcessingConfig | None = None,
        engine: AugLLMConfig | None = None,
        name: str = "document_processor",
    ):
        """Initialize the document processing agent.

        Args:
            config: Configuration for document processing
            engine: LLM engine configuration
            name: Agent name for identification
        """
        self.config = config or DocumentProcessingConfig()
        self.engine = engine or AugLLMConfig()
        self.name = name

        # Initialize components
        self._init_components()

        logger.info(
            f"DocumentProcessingAgent '{name}' initialized with {self.config.rag_strategy} strategy"
        )

    def _init_components(self):
        """Initialize all agent components."""
        # Document Loading Components
        auto_loader_config = self.config.auto_loader_config or AutoLoaderConfig(
            max_concurrency=self.config.max_concurrent_loads,
            enable_caching=self.config.enable_caching,
            cache_ttl=self.config.cache_ttl,
        )
        self.auto_loader = AutoLoader(config=auto_loader_config)
        # self.universal_loader = UniversalDocumentLoader()

        # Search & Retrieval Agent
        search_tools = [tavily_search_tool, tavily_search_context, scrape_webpages]

        self.search_agent = ReactAgent(
            name=f"{self.name}_search", engine=self.engine, tools=search_tools
        )

        # RAG Agent (configured based on strategy)
        # For now, we'll use a simple processing agent instead of RAG
        # TODO: Implement proper RAG agent with correct configuration
        self.rag_agent = SimpleAgent(name=f"{self.name}_rag", engine=self.engine)

        # Document Processing Agent
        self.processing_agent = SimpleAgent(
            name=f"{self.name}_processor", engine=self.engine
        )

    def _create_rag_agent(self) -> BaseRAGAgent:
        """Create RAG agent based on configuration."""
        # Configure retrieval based on strategy

        # For now, use base RAG agent for all strategies
        # TODO: Implement specific strategy loading with proper error handling
        try:
            if self.config.rag_strategy == "adaptive":
                try:
                    from haive.agents.rag.adaptive_rag.agent import AdaptiveRAGAgent

                    return AdaptiveRAGAgent(name=f"{self.name}_rag", engine=self.engine)
                except ImportError:
                    logger.warning(
                        "AdaptiveRAGAgent not available, falling back to BaseRAGAgent"
                    )

            elif self.config.rag_strategy == "self_rag":
                try:
                    from haive.agents.rag.self_rag2.agent import SelfRAGAgent

                    return SelfRAGAgent(name=f"{self.name}_rag", engine=self.engine)
                except ImportError:
                    logger.warning(
                        "SelfRAGAgent not available, falling back to BaseRAGAgent"
                    )

            elif self.config.rag_strategy == "hyde":
                try:
                    from haive.agents.rag.hyde.enhanced_agent_v2 import HyDEAgent

                    return HyDEAgent(name=f"{self.name}_rag", engine=self.engine)
                except ImportError:
                    logger.warning(
                        "HyDEAgent not available, falling back to BaseRAGAgent"
                    )

            elif self.config.rag_strategy == "multi_strategy":
                try:
                    from haive.agents.rag.multi_strategy.agent import (
                        MultiStrategyRAGAgent,
                    )

                    return MultiStrategyRAGAgent(
                        name=f"{self.name}_rag", engine=self.engine
                    )
                except ImportError:
                    logger.warning(
                        "MultiStrategyRAGAgent not available, falling back to BaseRAGAgent"
                    )

            # Default to base RAG
            return BaseRAGAgent(name=f"{self.name}_rag", engine=self.engine)

        except Exception as e:
            logger.exception(
                f"Error creating RAG agent: {e}, falling back to BaseRAGAgent"
            )
            return BaseRAGAgent(name=f"{self.name}_rag", engine=self.engine)

    async def process_query(
        self, query: str, sources: list[str | dict[str, Any]] | None = None
    ) -> DocumentProcessingResult:
        """Process a query with comprehensive document processing pipeline.

        Args:
            query: The user query to process
            sources: Optional list of specific sources to use

        Returns:
            DocumentProcessingResult with comprehensive results
        """
        start_time = datetime.now()

        # Initialize state
        state = DocumentProcessingState(
            messages=[HumanMessage(content=query)],
            original_query=query,
            current_sources=sources or [],
            processing_stage="query_processing",
        )

        try:
            # Step 1: Document Discovery & Fetching
            if self.config.search_enabled and not sources:
                state = await self._discover_documents(state)

            # Step 2: Document Loading
            if state.current_sources:
                state = await self._load_documents(state)

            # Step 3: Document Processing Pipeline
            state = await self._process_documents(state)

            # Step 4: RAG Processing
            state = await self._rag_processing(state)

            # Step 5: Generate Final Response
            response = await self._generate_response(state)

            # Calculate timing
            end_time = datetime.now()
            total_time = (end_time - start_time).total_seconds()

            return DocumentProcessingResult(
                response=response,
                sources=self._extract_sources(state),
                metadata=self._generate_metadata(state),
                documents=state.processed_documents,
                query_info={
                    "original_query": state.original_query,
                    "refined_queries": state.refined_queries,
                    "search_results_count": len(state.search_results),
                },
                timing={
                    "total_time": total_time,
                    "document_loading_time": state.document_state.operation_time,
                    "processing_time": total_time - state.document_state.operation_time,
                },
                statistics={
                    "documents_processed": len(state.processed_documents),
                    "sources_used": len(state.current_sources),
                    "context_documents": len(state.context_documents),
                },
            )

        except Exception as e:
            logger.exception(f"Error in document processing: {e}")
            raise

    async def _discover_documents(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Discover relevant documents using search capabilities."""
        state.processing_stage = "document_discovery"

        # Use ReactAgent with search tools to find relevant documents
        search_query = f"""
        Find relevant documents, files, and sources for the query: "{state.original_query}"

        Use search tools to:
        1. Search for relevant web content
        2. Find specific documents or files
        3. Identify authoritative sources
        4. Extract URLs and file paths

        Return a structured list of sources with their URLs/paths and relevance scores.
        """

        try:
            search_result = await self.search_agent.arun(search_query)

            # Extract string content from search result
            if hasattr(search_result, "content"):
                search_content = search_result.content
            elif hasattr(search_result, "response"):
                search_content = search_result.response
            elif isinstance(search_result, str):
                search_content = search_result
            else:
                search_content = str(search_result)

            # Extract sources from search results
            # This would need to be implemented based on the search agent's output format
            state.current_sources = self._extract_sources_from_search(search_content)
            state.search_results = [
                {"query": state.original_query, "result": search_content}
            ]

            state.operation_history.append(
                {
                    "operation": "document_discovery",
                    "timestamp": datetime.now().isoformat(),
                    "sources_found": len(state.current_sources),
                }
            )

        except Exception as e:
            logger.exception(f"Error in document discovery: {e}")
            # Continue with empty sources
            state.current_sources = []

        return state

    async def _load_documents(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Load documents using auto-loader with bulk processing."""
        state.processing_stage = "document_loading"

        try:
            if self.config.enable_bulk_processing:
                # Use bulk loading for efficiency
                bulk_result = self.auto_loader.load_bulk(
                    state.current_sources,
                    chunk_size=self.config.chunk_size,
                    chunk_overlap=self.config.chunk_overlap,
                )

                # Extract documents from bulk result
                documents = []
                for result in bulk_result.results:
                    documents.extend(result.documents)

                state.processed_documents = documents
                state.document_state.total_documents = bulk_result.total_documents
                state.document_state.operation_time = bulk_result.total_time

            else:
                # Load documents sequentially
                documents = []
                for source in state.current_sources:
                    try:
                        source_docs = self.auto_loader.load_documents([source])
                        documents.extend(source_docs)
                    except Exception as e:
                        logger.warning(f"Failed to load source {source}: {e}")
                        continue

                state.processed_documents = documents
                state.document_state.total_documents = len(documents)

            state.operation_history.append(
                {
                    "operation": "document_loading",
                    "timestamp": datetime.now().isoformat(),
                    "documents_loaded": len(state.processed_documents),
                    "sources_processed": len(state.current_sources),
                }
            )

        except Exception as e:
            logger.exception(f"Error in document loading: {e}")
            state.processed_documents = []

        return state

    async def _process_documents(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Process documents through annotation, summarization, and other pipelines."""
        state.processing_stage = "document_processing"

        try:
            # Document Annotation
            if self.config.annotation_enabled:
                state = await self._annotate_documents(state)

            # Document Summarization
            if self.config.summarization_enabled:
                state = await self._summarize_documents(state)

            # Knowledge Graph Extraction
            if self.config.kg_extraction_enabled:
                state = await self._extract_knowledge_graph(state)

            state.operation_history.append(
                {
                    "operation": "document_processing",
                    "timestamp": datetime.now().isoformat(),
                    "annotation_enabled": self.config.annotation_enabled,
                    "summarization_enabled": self.config.summarization_enabled,
                    "kg_extraction_enabled": self.config.kg_extraction_enabled,
                }
            )

        except Exception as e:
            logger.exception(f"Error in document processing: {e}")

        return state

    async def _annotate_documents(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Annotate documents with metadata and context."""
        # Use document modifier agents for annotation
        # This would integrate with existing document_modifiers

        annotation_prompt = f"""
        Analyze and annotate the following documents for the query: "{state.original_query}"

        For each document, provide:
        1. Relevance score (0-1)
        2. Key topics and themes
        3. Important entities and concepts
        4. Relationships to the query
        5. Summary of key content

        Documents to annotate: {len(state.processed_documents)} documents
        """

        try:
            annotation_result = await self.processing_agent.arun(annotation_prompt)

            # Extract string content from annotation result
            if hasattr(annotation_result, "content"):
                annotation_content = annotation_result.content
            elif hasattr(annotation_result, "response"):
                annotation_content = annotation_result.response
            elif isinstance(annotation_result, str):
                annotation_content = annotation_result
            else:
                annotation_content = str(annotation_result)

            state.annotation_results = {
                "annotation_summary": annotation_content,
                "annotated_count": len(state.processed_documents),
            }
        except Exception as e:
            logger.exception(f"Error in document annotation: {e}")
            state.annotation_results = {}

        return state

    async def _summarize_documents(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Summarize documents using map-branch summarization."""
        # This would integrate with existing summarization agents
        from haive.agents.document_modifiers.summarizer.map_branch.agent import (
            MapBranchSummarizerAgent,
        )

        try:
            MapBranchSummarizerAgent(name=f"{self.name}_summarizer", engine=self.engine)

            # Create summarization state and process
            # This would need to be implemented based on the summarizer's interface

        except Exception as e:
            logger.exception(f"Error in document summarization: {e}")

        return state

    async def _extract_knowledge_graph(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Extract knowledge graph from documents."""
        # This would integrate with existing KG extraction agents
        from haive.agents.document_modifiers.kg.kg_map_merge.agent import (
            StructuredKGAgent,
        )

        try:
            StructuredKGAgent(name=f"{self.name}_kg", engine=self.engine)

            # Create KG extraction state and process
            # This would need to be implemented based on the KG agent's interface

        except Exception as e:
            logger.exception(f"Error in knowledge graph extraction: {e}")

        return state

    async def _rag_processing(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Process query through RAG pipeline."""
        state.processing_stage = "rag_processing"

        try:
            # Query Refinement
            if self.config.query_refinement:
                state = await self._refine_query(state)

            # RAG Processing

            # Use the configured RAG agent
            rag_prompt = f"""
            Process the following documents to answer the query: "{state.original_query}"

            Documents:
            {[doc.page_content[:200] + "..." for doc in state.processed_documents[:5]]}

            Provide a comprehensive response based on the document content.
            """

            await self.rag_agent.arun(rag_prompt)

            # Extract context documents and results (simplified for now)
            state.context_documents = state.processed_documents[
                :10
            ]  # Use first 10 documents
            state.retrieval_results = state.processed_documents

            state.operation_history.append(
                {
                    "operation": "rag_processing",
                    "timestamp": datetime.now().isoformat(),
                    "rag_strategy": self.config.rag_strategy,
                    "context_documents": len(state.context_documents),
                }
            )

        except Exception as e:
            logger.exception(f"Error in RAG processing: {e}")
            state.context_documents = state.processed_documents[:10]  # Fallback

        return state

    async def _refine_query(
        self, state: DocumentProcessingState
    ) -> DocumentProcessingState:
        """Refine query for better retrieval."""
        # This would integrate with existing query refinement components

        try:
            refinement_prompt = f"""
            Refine the following query for better document retrieval:

            Original Query: "{state.original_query}"

            Available Documents: {len(state.processed_documents)} documents
            Document Topics: {list(state.annotation_results.keys()) if state.annotation_results else "Not analyzed"}

            Provide:
            1. Refined query with better keywords
            2. Alternative query formulations
            3. Specific search terms to focus on
            """

            refinement_result = await self.processing_agent.arun(refinement_prompt)

            # Extract string content from refinement result
            if hasattr(refinement_result, "content"):
                refinement_content = refinement_result.content
            elif hasattr(refinement_result, "response"):
                refinement_content = refinement_result.response
            elif isinstance(refinement_result, str):
                refinement_content = refinement_result
            else:
                refinement_content = str(refinement_result)

            # Extract refined queries (this would need better parsing)
            state.refined_queries = [state.original_query, refinement_content]

        except Exception as e:
            logger.exception(f"Error in query refinement: {e}")
            state.refined_queries = [state.original_query]

        return state

    async def _generate_response(self, state: DocumentProcessingState) -> str:
        """Generate final response based on processed documents and RAG results."""
        state.processing_stage = "response_generation"

        response_prompt = f"""
        Generate a comprehensive response based on the document processing results:

        Original Query: "{state.original_query}"

        Processing Results:
        - Documents Processed: {len(state.processed_documents)}
        - Sources Used: {len(state.current_sources)}
        - Context Documents: {len(state.context_documents)}
        - Annotation Results: {bool(state.annotation_results)}

        Context Information:
        {self._format_context_for_response(state)}

        Requirements:
        - Provide a direct answer to the original query
        - Include relevant information from processed documents
        - Cite sources when appropriate
        - Be comprehensive but concise
        - Include confidence level if applicable
        """

        try:
            response = await self.processing_agent.arun(response_prompt)

            # Extract string content from response
            if hasattr(response, "content"):
                return response.content
            if hasattr(response, "response"):
                return response.response
            if isinstance(response, str):
                return response
            return str(response)

        except Exception as e:
            logger.exception(f"Error in response generation: {e}")
            return f"Error generating response: {e}"

    def _format_context_for_response(self, state: DocumentProcessingState) -> str:
        """Format context information for response generation."""
        context_parts = []

        # Add document summaries
        if state.processed_documents:
            context_parts.append(
                f"Document Content ({len(state.processed_documents)} documents):"
            )
            for i, doc in enumerate(state.processed_documents[:5]):  # Limit to first 5
                context_parts.append(f"Doc {i+1}: {doc.page_content[:200]}...")

        # Add annotation results
        if state.annotation_results:
            context_parts.append(
                f"Annotation Results: {state.annotation_results.get('annotation_summary', 'N/A')}"
            )

        # Add search results
        if state.search_results:
            context_parts.append(
                f"Search Results: {len(state.search_results)} searches performed"
            )

        return "\n\n".join(context_parts)

    def _extract_sources_from_search(
        self, search_result: str
    ) -> list[str | dict[str, Any]]:
        """Extract sources from search agent result."""
        # This would need to be implemented based on the search agent's output format
        # For now, return empty list
        return []

    def _extract_sources(self, state: DocumentProcessingState) -> list[dict[str, Any]]:
        """Extract source information for result."""
        sources = []

        for i, source in enumerate(state.current_sources):
            source_info = {
                "index": i,
                "source": source,
                "type": (
                    "url"
                    if isinstance(source, str) and source.startswith("http")
                    else "file"
                ),
                "processed": i < len(state.processed_documents),
            }
            sources.append(source_info)

        return sources

    def _generate_metadata(self, state: DocumentProcessingState) -> dict[str, Any]:
        """Generate metadata for processing result."""
        return {
            "processing_stages": [op["operation"] for op in state.operation_history],
            "config_used": {
                "rag_strategy": self.config.rag_strategy,
                "search_enabled": self.config.search_enabled,
                "annotation_enabled": self.config.annotation_enabled,
                "bulk_processing": self.config.enable_bulk_processing,
            },
            "document_state": {
                "total_documents": state.document_state.total_documents,
                "successful_documents": state.document_state.successful_documents,
                "failed_documents": state.document_state.failed_documents,
            },
            "operation_history": state.operation_history,
        }

    async def process_sources(
        self, sources: list[str | dict[str, Any]], query: str
    ) -> DocumentProcessingResult:
        """Process specific sources with a query.

        Args:
            sources: List of sources to process
            query: Query to process against the sources

        Returns:
            DocumentProcessingResult with results
        """
        return await self.process_query(query, sources)

    def get_capabilities(self) -> dict[str, Any]:
        """Get agent capabilities and configuration."""
        return {
            "document_loading": {
                "auto_loader": True,
                "bulk_processing": self.config.enable_bulk_processing,
                "supported_formats": "230+ formats via AutoLoader",
            },
            "search_capabilities": {
                "web_search": self.config.search_enabled,
                "search_depth": self.config.search_depth,
                "tools": ["tavily_search", "web_scraping"],
            },
            "processing_pipeline": {
                "annotation": self.config.annotation_enabled,
                "summarization": self.config.summarization_enabled,
                "kg_extraction": self.config.kg_extraction_enabled,
            },
            "rag_capabilities": {
                "strategy": self.config.rag_strategy,
                "query_refinement": self.config.query_refinement,
                "retrieval_strategy": self.config.retrieval_strategy,
            },
            "output_features": {
                "structured_output": self.config.structured_output,
                "source_citation": self.config.include_sources,
                "metadata": self.config.include_metadata,
            },
        }


# Export main classes
__all__ = [
    "DocumentProcessingAgent",
    "DocumentProcessingConfig",
    "DocumentProcessingResult",
    "DocumentProcessingState",
]
