"""Enhanced RAG State Schema for SimpleRAG V3.

This module provides enhanced state management for SimpleRAG using Enhanced MultiAgent V3
with performance tracking, debug information, and comprehensive metadata.
"""

from typing import Any, Dict, List, Optional

from haive.core.schema.state_schema import StateSchema
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field


class RAGMetadata(BaseModel):
    """Metadata for RAG operations."""

    query_analysis: Dict[str, Any] = Field(default_factory=dict)
    retrieval_params: Dict[str, Any] = Field(default_factory=dict)
    generation_params: Dict[str, Any] = Field(default_factory=dict)
    timing_info: Dict[str, float] = Field(default_factory=dict)
    quality_scores: Dict[str, float] = Field(default_factory=dict)


class RetrievalDebugInfo(BaseModel):
    """Debug information for retrieval operations."""

    query_vector_dim: Optional[int] = Field(default=None)
    search_time: Optional[float] = Field(default=None)
    total_documents: Optional[int] = Field(default=None)
    similarity_scores: List[float] = Field(default_factory=list)
    retrieval_strategy: Optional[str] = Field(default=None)
    filtered_count: Optional[int] = Field(default=None)


class GenerationDebugInfo(BaseModel):
    """Debug information for generation operations."""

    context_length: Optional[int] = Field(default=None)
    prompt_tokens: Optional[int] = Field(default=None)
    completion_tokens: Optional[int] = Field(default=None)
    generation_time: Optional[float] = Field(default=None)
    model_used: Optional[str] = Field(default=None)
    temperature: Optional[float] = Field(default=None)


class SimpleRAGState(StateSchema):
    """Enhanced state schema for SimpleRAG V3 pipeline.

    This state schema extends the basic StateSchema with RAG-specific fields
    and enhanced tracking capabilities when performance_mode or debug_mode
    are enabled.

    Core RAG Fields:
        - query: User query string
        - retrieved_documents: Documents from retrieval step
        - generated_answer: Final answer from generation step

    Enhanced Tracking (when enabled):
        - retrieval_metadata: Retrieval operation metadata
        - generation_metadata: Generation operation metadata
        - performance_metrics: Performance tracking data
        - debug_info: Detailed debug information

    Examples:
        Basic usage (automatic schema selection)::

            # Enhanced features disabled - uses basic fields only
            state = SimpleRAGState(query="What is AI?")

        Enhanced usage::

            # Enhanced features enabled - includes all tracking
            state = SimpleRAGState(
                query="What is AI?",
                retrieval_metadata=RAGMetadata(
                    timing_info={"retrieval_time": 0.5}
                ),
                debug_mode=True
            )
    """

    # Core RAG fields (always present)
    query: str = Field(default="", description="User query for RAG processing")

    retrieved_documents: List[Document] = Field(
        default_factory=list, description="Documents retrieved from vector store"
    )

    generated_answer: str = Field(default="", description="Generated answer from LLM")

    # Enhanced tracking fields (populated when features enabled)
    retrieval_metadata: Optional[RAGMetadata] = Field(
        default=None, description="Metadata from retrieval operation"
    )

    generation_metadata: Optional[RAGMetadata] = Field(
        default=None, description="Metadata from generation operation"
    )

    # Performance tracking (when performance_mode=True)
    performance_metrics: Dict[str, float] = Field(
        default_factory=dict, description="Performance metrics for each stage"
    )

    # Debug information (when debug_mode=True)
    retrieval_debug: Optional[RetrievalDebugInfo] = Field(
        default=None, description="Debug information for retrieval"
    )

    generation_debug: Optional[GenerationDebugInfo] = Field(
        default=None, description="Debug information for generation"
    )

    # Execution tracking
    current_stage: str = Field(
        default="ready", description="Current stage of RAG pipeline"
    )

    stage_history: List[str] = Field(
        default_factory=list, description="History of pipeline stages"
    )

    # Source tracking
    document_sources: List[str] = Field(
        default_factory=list, description="Sources of retrieved documents"
    )

    citation_info: Dict[str, Any] = Field(
        default_factory=dict, description="Citation information for sources"
    )

    def update_stage(self, stage: str) -> None:
        """Update current stage and add to history."""
        self.stage_history.append(stage)
        self.current_stage = stage

    def add_retrieval_debug(
        self,
        query_vector_dim: Optional[int] = None,
        search_time: Optional[float] = None,
        total_documents: Optional[int] = None,
        similarity_scores: Optional[List[float]] = None,
        **kwargs
    ) -> None:
        """Add retrieval debug information."""
        if self.retrieval_debug is None:
            self.retrieval_debug = RetrievalDebugInfo()

        if query_vector_dim is not None:
            self.retrieval_debug.query_vector_dim = query_vector_dim
        if search_time is not None:
            self.retrieval_debug.search_time = search_time
        if total_documents is not None:
            self.retrieval_debug.total_documents = total_documents
        if similarity_scores is not None:
            self.retrieval_debug.similarity_scores = similarity_scores

        # Add any additional debug info
        for key, value in kwargs.items():
            if hasattr(self.retrieval_debug, key):
                setattr(self.retrieval_debug, key, value)

    def add_generation_debug(
        self,
        context_length: Optional[int] = None,
        prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        generation_time: Optional[float] = None,
        **kwargs
    ) -> None:
        """Add generation debug information."""
        if self.generation_debug is None:
            self.generation_debug = GenerationDebugInfo()

        if context_length is not None:
            self.generation_debug.context_length = context_length
        if prompt_tokens is not None:
            self.generation_debug.prompt_tokens = prompt_tokens
        if completion_tokens is not None:
            self.generation_debug.completion_tokens = completion_tokens
        if generation_time is not None:
            self.generation_debug.generation_time = generation_time

        # Add any additional debug info
        for key, value in kwargs.items():
            if hasattr(self.generation_debug, key):
                setattr(self.generation_debug, key, value)

    def update_performance_metric(self, metric_name: str, value: float) -> None:
        """Update a performance metric."""
        self.performance_metrics[metric_name] = value

    def get_pipeline_summary(self) -> Dict[str, Any]:
        """Get comprehensive pipeline summary."""
        return {
            "current_stage": self.current_stage,
            "stage_history": self.stage_history,
            "query": self.query,
            "documents_retrieved": len(self.retrieved_documents),
            "answer_generated": bool(self.generated_answer),
            "sources": self.document_sources,
            "performance_metrics": self.performance_metrics,
            "has_debug_info": {
                "retrieval": self.retrieval_debug is not None,
                "generation": self.generation_debug is not None,
            },
        }

    def get_retrieval_summary(self) -> Dict[str, Any]:
        """Get retrieval operation summary."""
        summary = {
            "documents_count": len(self.retrieved_documents),
            "sources": self.document_sources,
        }

        if self.retrieval_debug:
            summary.update(
                {
                    "search_time": self.retrieval_debug.search_time,
                    "total_documents": self.retrieval_debug.total_documents,
                    "similarity_scores": self.retrieval_debug.similarity_scores,
                    "avg_similarity": (
                        sum(self.retrieval_debug.similarity_scores)
                        / len(self.retrieval_debug.similarity_scores)
                        if self.retrieval_debug.similarity_scores
                        else None
                    ),
                }
            )

        if self.retrieval_metadata:
            summary.update({"metadata": self.retrieval_metadata.model_dump()})

        return summary

    def get_generation_summary(self) -> Dict[str, Any]:
        """Get generation operation summary."""
        summary = {
            "answer_length": len(self.generated_answer),
            "has_answer": bool(self.generated_answer),
        }

        if self.generation_debug:
            summary.update(
                {
                    "context_length": self.generation_debug.context_length,
                    "prompt_tokens": self.generation_debug.prompt_tokens,
                    "completion_tokens": self.generation_debug.completion_tokens,
                    "generation_time": self.generation_debug.generation_time,
                    "model_used": self.generation_debug.model_used,
                }
            )

        if self.generation_metadata:
            summary.update({"metadata": self.generation_metadata.model_dump()})

        return summary


# Legacy compatibility
BaseRAGState = SimpleRAGState

__all__ = [
    "SimpleRAGState",
    "RAGMetadata",
    "RetrievalDebugInfo",
    "GenerationDebugInfo",
    "BaseRAGState",  # Legacy
]
