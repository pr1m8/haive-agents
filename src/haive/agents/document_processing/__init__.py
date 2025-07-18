"""Document Processing Agent Package.

This package provides comprehensive document processing capabilities including:
- Document fetching with ReactAgent + search tools
- Auto-loading with bulk processing (230+ formats)
- Transform/split/annotate/embed pipeline
- Advanced RAG features (refined queries, self-query, etc.)
- State management and persistence

The main components are:
- DocumentProcessingAgent: Main agent class
- DocumentProcessingConfig: Configuration for processing
- DocumentProcessingResult: Result container
- DocumentProcessingState: State management

Example:
    Basic usage::

        from haive.agents.document_processing import DocumentProcessingAgent

        agent = DocumentProcessingAgent()
        result = await agent.process_query("Analyze financial reports from company.com")

    Advanced configuration::

        from haive.agents.document_processing import DocumentProcessingAgent, DocumentProcessingConfig

        config = DocumentProcessingConfig(
            rag_strategy="adaptive",
            annotation_enabled=True,
            search_enabled=True,
            bulk_processing=True
        )

        agent = DocumentProcessingAgent(config=config)
        result = await agent.process_query("Find all Q4 2024 projections")

Author: Claude (Haive AI Agent Framework)
Version: 1.0.0
"""

from .agent import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
    DocumentProcessingResult,
    DocumentProcessingState,
)

__all__ = [
    "DocumentProcessingAgent",
    "DocumentProcessingConfig",
    "DocumentProcessingResult",
    "DocumentProcessingState",
]

__version__ = "1.0.0"
