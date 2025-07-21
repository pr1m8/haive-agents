#!/usr/bin/env python3
"""SimpleRAG - Proper MultiAgentState Implementation.

This is the CORRECT SimpleRAG implementation following the working pattern from the guides:
- Use MultiAgentState (not MultiAgent class inheritance)
- Use create_agent_node_v3() for execution
- Direct field updates through structured outputs
- Sequential execution: retriever → generator

Architecture:
    SimpleRAGState extends MultiAgentState
    agents = [BaseRAGAgent, SimpleAgent]
    Sequential execution via nodes: retriever_node → generator_node
    Direct field access: state.documents, state.answer

Examples:
    Basic usage::

        from haive.agents.rag.simple.simple_rag_state import SimpleRAGState, create_simple_rag_workflow

        # Create the complete workflow
        state = create_simple_rag_workflow(
            query="What is machine learning?",
            vector_store=your_vector_store,
            top_k=5
        )

        # Execute sequential workflow
        result = await execute_simple_rag(state)

        # Access results directly
        print(f"Answer: {result.answer}")
        print(f"Sources: {result.sources}")
"""

from __future__ import annotations

import logging
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from langchain_core.documents import Document
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)


# ================================
# Structured Output Models
# ================================


class DocumentRetrieval(BaseModel):
    """Output from the document retrieval agent."""

    documents: list[Document] = Field(
        default_factory=list, description="Retrieved documents from vector store"
    )
    retrieved_count: int = Field(
        default=0, description="Number of documents successfully retrieved"
    )
    query_processed: str = Field(
        default="", description="Processed version of the input query"
    )


class AnswerGeneration(BaseModel):
    """Output from the answer generation agent."""

    answer: str = Field(
        default="", description="Generated answer based on retrieved documents"
    )
    sources: list[str] = Field(
        default_factory=list, description="Source references used in the answer"
    )
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score for the generated answer",
    )


# ================================
# SimpleRAG State Schema
# ================================


class SimpleRAGState(MultiAgentState):
    """State schema for SimpleRAG workflow using MultiAgentState pattern.

    This follows the working pattern from the guides:
    - Extends MultiAgentState for proper agent management
    - Contains all input and output fields as direct attributes
    - Agents update fields directly through structured outputs
    - No complex nested structures - just clean, direct field access

    Flow:
        1. Input: query, configuration
        2. Retriever updates: documents, retrieved_count, query_processed
        3. Generator updates: answer, sources, confidence
        4. Direct access: state.answer, state.sources, etc.
    """

    # =============================
    # Input Fields
    # =============================

    query: str = Field(default="", description="User query for RAG processing")

    top_k: int = Field(
        default=5, ge=1, le=50, description="Number of documents to retrieve"
    )

    # =============================
    # Retriever Agent Outputs
    # =============================

    documents: list[Document] = Field(
        default_factory=list, description="Retrieved documents from vector store"
    )

    retrieved_count: int = Field(
        default=0, description="Number of documents successfully retrieved"
    )

    query_processed: str = Field(
        default="", description="Processed version of the input query"
    )

    # =============================
    # Generator Agent Outputs
    # =============================

    answer: str = Field(
        default="", description="Generated answer based on retrieved documents"
    )

    sources: list[str] = Field(
        default_factory=list, description="Source references used in the answer"
    )

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score for the generated answer",
    )

    # =============================
    # Metadata
    # =============================

    rag_workflow_id: str = Field(
        default="", description="Unique identifier for this RAG workflow execution"
    )


# ================================
# Agent Creation Functions
# ================================


def create_rag_agents(
    vector_store_config: VectorStoreConfig,
    llm_config: AugLLMConfig,
    structured_output_model: type[BaseModel] | None = None,
) -> tuple[BaseRAGAgent, SimpleAgent]:
    """Create the retriever and generator agents for SimpleRAG.

    Args:
        vector_store_config: Configuration for the vector store
        llm_config: Configuration for the LLM
        structured_output_model: Optional custom output model for generator

    Returns:
        Tuple of (retriever_agent, generator_agent)
    """
    # Create retriever agent
    retriever = BaseRAGAgent(name="retriever", engine=vector_store_config)

    # Create generator agent with RAG-specific system prompt
    generator_config = llm_config.model_copy()
    if not generator_config.system_message:
        generator_config.system_message = (
            "You are a helpful assistant that answers questions based on provided context. "
            "Use only the information in the context to answer the question. "
            "If the context doesn't contain enough information, say so clearly. "
            "Provide source references when possible."
        )

    generator = SimpleAgent(
        name="generator",
        engine=generator_config,
        structured_output_model=structured_output_model or AnswerGeneration,
    )

    return retriever, generator


def create_simple_rag_workflow(
    query: str,
    vector_store_config: VectorStoreConfig,
    llm_config: AugLLMConfig | None = None,
    top_k: int = 5,
    structured_output_model: type[BaseModel] | None = None,
    workflow_id: str = "",
) -> SimpleRAGState:
    """Create a complete SimpleRAG workflow state.

    Args:
        query: The query to process
        vector_store_config: Vector store configuration
        llm_config: LLM configuration (uses default if None)
        top_k: Number of documents to retrieve
        structured_output_model: Optional custom output model
        workflow_id: Unique workflow identifier

    Returns:
        Initialized SimpleRAGState ready for execution
    """
    # Use default LLM config if none provided
    if llm_config is None:
        llm_config = AugLLMConfig(temperature=0.7)

    # Create agents
    retriever, generator = create_rag_agents(
        vector_store_config=vector_store_config,
        llm_config=llm_config,
        structured_output_model=structured_output_model,
    )

    # Create and return state
    return SimpleRAGState(
        agents=[retriever, generator],
        query=query,
        top_k=top_k,
        rag_workflow_id=workflow_id or f"rag_{hash(query) % 10000}",
    )


# ================================
# Execution Functions
# ================================


async def execute_simple_rag(
    state: SimpleRAGState, debug: bool = False
) -> SimpleRAGState:
    """Execute the complete SimpleRAG workflow.

    This follows the working pattern from the guides:
    - Sequential execution using create_agent_node_v3()
    - Direct field updates through structured outputs
    - Clean, simple execution flow

    Args:
        state: The SimpleRAGState to execute
        debug: Enable debug logging

    Returns:
        Updated state with all results populated
    """
    # Basic config
    config = {"configurable": {"thread_id": state.rag_workflow_id}}

    if debug:
        logger.info("🔍 Starting SimpleRAG workflow")
        logger.info(f"Query: {state.query}")
        logger.info(f"Top K: {state.top_k}")
        logger.info(f"Agents: {list(state.agents.keys())}")

    # Step 1: Document Retrieval
    if debug:
        logger.info("📚 Step 1: Document Retrieval...")

    retriever_node = create_agent_node_v3("retriever")
    retriever_node(state, config)

    if debug:
        logger.info(f"✅ Retrieved {state.retrieved_count} documents")
        logger.info(f"Processed query: {state.query_processed}")

    # Step 2: Answer Generation
    if debug:
        logger.info("🤖 Step 2: Answer Generation...")

    generator_node = create_agent_node_v3("generator")
    generator_node(state, config)

    if debug:
        logger.info(f"✅ Generated answer: {len(state.answer)} characters")
        logger.info(f"Sources used: {len(state.sources)}")
        logger.info(f"Confidence: {state.confidence:.2f}")

    if debug:
        logger.info("🎯 SimpleRAG workflow completed successfully")

    return state


def run_simple_rag(
    query: str,
    vector_store_config: VectorStoreConfig,
    llm_config: AugLLMConfig | None = None,
    top_k: int = 5,
    debug: bool = False,
) -> SimpleRAGState:
    """Synchronous wrapper for SimpleRAG execution.

    Args:
        query: The query to process
        vector_store_config: Vector store configuration
        llm_config: LLM configuration
        top_k: Number of documents to retrieve
        debug: Enable debug logging

    Returns:
        Completed SimpleRAGState with results
    """
    import asyncio

    # Create workflow
    state = create_simple_rag_workflow(
        query=query,
        vector_store_config=vector_store_config,
        llm_config=llm_config,
        top_k=top_k,
    )

    # Execute
    return asyncio.run(execute_simple_rag(state, debug=debug))


# ================================
# Utility Functions
# ================================


def display_rag_results(state: SimpleRAGState) -> None:
    """Display SimpleRAG results in a formatted way.

    Args:
        state: Completed SimpleRAGState with results
    """
    if state.sources:
        for _i, _source in enumerate(state.sources, 1):
            pass
    else:
        pass


def get_rag_summary(state: SimpleRAGState) -> dict[str, Any]:
    """Get a summary of the RAG execution.

    Args:
        state: Completed SimpleRAGState

    Returns:
        Dictionary with execution summary
    """
    return {
        "workflow_id": state.rag_workflow_id,
        "query": state.query,
        "documents_retrieved": state.retrieved_count,
        "answer_length": len(state.answer),
        "sources_count": len(state.sources),
        "confidence": state.confidence,
        "has_answer": bool(state.answer),
        "agents_used": list(state.agents.keys()) if state.agents else [],
    }


# ================================
# Export
# ================================

__all__ = [
    "AnswerGeneration",
    "DocumentRetrieval",
    "SimpleRAGState",
    "create_rag_agents",
    "create_simple_rag_workflow",
    "display_rag_results",
    "execute_simple_rag",
    "get_rag_summary",
    "run_simple_rag",
]


# ================================
# Example Usage
# ================================

if __name__ == "__main__":
    from langchain_core.documents import Document

    async def demo():
        """Demonstrate SimpleRAG using the correct MultiAgentState pattern."""
        # This would use real vector store and LLM configs in practice
        # For demo purposes, we're showing the structure

        # Example of how it would work with real configs:
        # state = create_simple_rag_workflow(
        #     query="What is machine learning?",
        #     vector_store_config=your_vector_store_config,
        #     llm_config=AugLLMConfig(temperature=0.7)
        # )
        #
        # result = await execute_simple_rag(state, debug=True)
        # display_rag_results(result)

    # Uncomment to run demo
    # asyncio.run(demo())
