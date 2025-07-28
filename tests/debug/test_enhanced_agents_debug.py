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
    print("\n" + "=" * 60)
    print("Testing SimpleAgent with debug=True")
    print("=" * 60)

    try:

        from haive.agents.simple.enhanced_simple_real import SimpleAgent

        # Create agent
        agent = SimpleAgent(
            name="test_simple",
            temperature=0.1,
            system_message="You are a helpful assistant. Keep responses brief.",
        )

        print(f"Created: {agent}")

        # Test with debug
        result = await agent.arun("What is 2+2?", debug=True)
        print(f"\nResult: {result}")

    except Exception as e:
        print(f"Error testing SimpleAgent: {e}")
        import traceback

        traceback.print_exc()


async def test_react_agent():
    """Test ReactAgent with tools and debug=True."""
    print("\n" + "=" * 60)
    print("Testing ReactAgent with tools and debug=True")
    print("=" * 60)

    try:

        from haive.agents.react.enhanced_react_agent import ReactAgent

        # Create agent with tools
        agent = ReactAgent(
            name="test_react",
            temperature=0.1,
            tools=[calculator, word_counter],
            max_iterations=3,
        )

        print(f"Created: {agent}")
        print(f"Tools: {[t.name for t in agent.tools]}")

        # Test with debug - should use calculator tool
        result = await agent.arun(
            "Calculate 15 * 23 and tell me how many words are in your response",
            debug=True,
        )
        print(f"\nResult: {result}")

    except Exception as e:
        print(f"Error testing ReactAgent: {e}")
        import traceback

        traceback.print_exc()


async def test_supervisor_agent():
    """Test SupervisorAgent with workers and debug=True."""
    print("\n" + "=" * 60)
    print("Testing SupervisorAgent with debug=True")
    print("=" * 60)

    try:
        from haive.agents.multi.enhanced_supervisor_agent import SupervisorAgent
        from haive.agents.simple.enhanced_simple_real import SimpleAgent

        # Create worker agents
        analyst = SimpleAgent(name="analyst", temperature=0.1)
        writer = SimpleAgent(name="writer", temperature=0.7)

        # Create supervisor
        supervisor = SupervisorAgent(
            name="managef",
            workers={"analyst": analyst, "writer": writer},
            delegation_strategy="best",
            temperature=0.3,
        )

        print(f"Created: {supervisor}")
        print(f"Workers: {supervisor.list_workers()}")

        # Test with debug
        result = await supervisor.arun(
            "Analyze the benefits of Python and write a short summary", debug=True
        )
        print(f"\nResult: {result}")

    except Exception as e:
        print(f"Error testing SupervisorAgent: {e}")
        import traceback

        traceback.print_exc()


async def test_sequential_agent():
    """Test SequentialAgent pipeline with debug=True."""
    print("\n" + "=" * 60)
    print("Testing SequentialAgent with debug=True")
    print("=" * 60)

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

        print(f"Created: {pipeline}")
        print(f"Pipeline: {pipeline.get_pipeline_description()}")

        # Test with debug
        outputs = await pipeline.execute_sequence("Explain machine learning")
        print(f"\nAll outputs: {outputs}")

    except Exception as e:
        print(f"Error testing SequentialAgent: {e}")
        import traceback

        traceback.print_exc()


async def test_rag_agent():
    """Test RAG agent with debug=True."""
    print("\n" + "=" * 60)
    print("Testing RAG Agent with debug=True")
    print("=" * 60)

    try:
        from haive.agents.rag.enhanced_simple_rag_agent import SimpleRAGAgent

        # Create RAG agent with test retriever
        rag = SimpleRAGAgent(
            name="test_rag", retriever=TestRetriever(), k=2, include_sources=True
        )

        print(f"Created: {rag}")

        # Test retrieval
        docs = await rag.retrieve("Python programming")
        print(f"\nRetrieved {len(docs)} documents")

        # Format context
        context = rag.format_context(docs)
        print(f"\nFormatted context:\n{context}")

        # Test quick answer
        answer = await rag.quick_answer("What is Python?")
        print(f"\nQuick answer: {answer}")

    except Exception as e:
        print(f"Error testing RAG agent: {e}")
        import traceback

        traceback.print_exc()


async def test_parallel_agent():
    """Test ParallelAgent with debug=True."""
    print("\n" + "=" * 60)
    print("Testing ParallelAgent with debug=True")
    print("=" * 60)

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

        print(f"Created: {ensemble}")

        # Test with debug
        results = await ensemble.execute_parallel(
            "What are the key features of Python?"
        )
        print(f"\nParallel results ({len(results)} agents):")
        for i, result in enumerate(results):
            print(f"  Agent {i}: {result}")

    except Exception as e:
        print(f"Error testing ParallelAgent: {e}")
        import traceback

        traceback.print_exc()


async def main():
    """Run all tests with debug=True."""
    print("Enhanced Agents Testing with debug=True")
    print("Using REAL components - NO MOCKS")
    print("This will show actual execution details")

    # Run tests
    await test_simple_agent()
    await test_react_agent()
    await test_supervisor_agent()
    await test_sequential_agent()
    await test_rag_agent()
    await test_parallel_agent()

    print("\n" + "=" * 60)
    print("Testing Complete")
    print("=" * 60)


if __name__ == "__main__":
    # Check if we have proper environment
    print("Checking environment...")
    try:
        from haive.core.engine.aug_llm.config import AugLLMConfig

        print("✓ Core imports working")
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Make sure to run with: poetry run python test_enhanced_agents_debug.py")

    # Run tests
    asyncio.run(main())
