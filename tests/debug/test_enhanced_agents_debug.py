#!/usr/bin/env python3
"""Test enhanced agents with debug=True and real components.

This script tests the enhanced agents with:
1. Real LLM components (no mocks)
2. debug=True for detailed execution info
3. Actual execution to see how they perform
"""

import asyncio
import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

import contextlib

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.tools import tool


# Test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool
def word_counter(text: str) -> str:
    """Count words in text."""
    words = text.split()
    return f"The text contains {len(words)} words"


# Test retriever
class TestRetriever(BaseRetriever):
    """Simple test retriever."""

    def _get_relevant_documents(self, query: str) -> list[Document]:
        # Return some test documents
        return [
            Document(
                page_content=f"Information about {query}: This is relevant content.",
                metadata={"source": "test_doc_1.txt"},
            ),
            Document(
                page_content=f"More details on {query}: Additional information here.",
                metadata={"source": "test_doc_2.txt"},
            ),
        ]

    async def _aget_relevant_documents(self, query: str) -> list[Document]:
        return self._get_relevant_documents(query)


async def test_simple_agent():
    """Test SimpleAgent with debug=True."""
    try:

        from haive.agents.simple.enhanced_simple_real import SimpleAgent

        # Create agent
        agent = SimpleAgent(
            name="test_simple",
            temperature=0.1,
            system_message="You are a helpful assistant. Keep responses brief.",
        )

        # Test with debug
        await agent.arun("What is 2+2?", debug=True)

    except Exception:
        import traceback

        traceback.print_exc()


async def test_react_agent():
    """Test ReactAgent with tools and debug=True."""
    try:

        from haive.agents.react.enhanced_react_agent import ReactAgent

        # Create agent with tools
        agent = ReactAgent(
            name="test_react",
            temperature=0.1,
            tools=[calculator, word_counter],
            max_iterations=3,
        )

        # Test with debug - should use calculator tool
        await agent.arun(
            "Calculate 15 * 23 and tell me how many words are in your response",
            debug=True,
        )

    except Exception:
        import traceback

        traceback.print_exc()


async def test_supervisor_agent():
    """Test SupervisorAgent with workers and debug=True."""
    try:
        from haive.agents.multi.enhanced_supervisor_agent import SupervisorAgent
        from haive.agents.simple.enhanced_simple_real import SimpleAgent

        # Create worker agents
        analyst = SimpleAgent(name="analyst", temperature=0.1)
        writer = SimpleAgent(name="writer", temperature=0.7)

        # Create supervisor
        supervisor = SupervisorAgent(
            name="manager",
            workers={"analyst": analyst, "writer": writer},
            delegation_strategy="best",
            temperature=0.3,
        )

        # Test with debug
        await supervisor.arun(
            "Analyze the benefits of Python and write a short summary", debug=True
        )

    except Exception:
        import traceback

        traceback.print_exc()


async def test_sequential_agent():
    """Test SequentialAgent pipeline with debug=True."""
    try:
        from haive.agents.multi.enhanced_sequential_agent import SequentialAgent
        from haive.agents.simple.enhanced_simple_real import SimpleAgent

        # Create pipeline steps
        step1 = SimpleAgent(name="analyzer", temperature=0.1)
        step2 = SimpleAgent(name="summarizer", temperature=0.3)

        # Create sequential pipeline
        pipeline = SequentialAgent(
            name="analysis_pipeline",
            agents=[step1, step2],
            process_between_steps=False,
            return_all_outputs=True,
        )

        # Test with debug
        await pipeline.execute_sequence("Explain machine learning")

    except Exception:
        import traceback

        traceback.print_exc()


async def test_rag_agent():
    """Test RAG agent with debug=True."""
    try:
        from haive.agents.rag.enhanced_simple_rag_agent import SimpleRAGAgent

        # Create RAG agent with test retriever
        rag = SimpleRAGAgent(
            name="test_rag", retriever=TestRetriever(), k=2, include_sources=True
        )

        # Test retrieval
        docs = await rag.retrieve("Python programming")

        # Format context
        rag.format_context(docs)

        # Test quick answer
        await rag.quick_answer("What is Python?")

    except Exception:
        import traceback

        traceback.print_exc()


async def test_parallel_agent():
    """Test ParallelAgent with debug=True."""
    try:
        from haive.agents.multi.enhanced_parallel_agent import ParallelAgent
        from haive.agents.simple.enhanced_simple_real import SimpleAgent

        # Create parallel agents
        agents = [SimpleAgent(name=f"expert_{i}", temperature=0.5) for i in range(3)]

        # Create parallel ensemble
        ensemble = ParallelAgent(
            name="expert_panel",
            agents=agents,
            aggregation_strategy="all",
            timeout_per_agent=10.0,
        )

        # Test with debug
        results = await ensemble.execute_parallel(
            "What are the key features of Python?"
        )
        for _i, _result in enumerate(results):
            pass

    except Exception:
        import traceback

        traceback.print_exc()


async def main():
    """Run all tests with debug=True."""
    # Run tests
    await test_simple_agent()
    await test_react_agent()
    await test_supervisor_agent()
    await test_sequential_agent()
    await test_rag_agent()
    await test_parallel_agent()


if __name__ == "__main__":
    # Check if we have proper environment
    with contextlib.suppress(ImportError):
        pass

    # Run tests
    asyncio.run(main())
