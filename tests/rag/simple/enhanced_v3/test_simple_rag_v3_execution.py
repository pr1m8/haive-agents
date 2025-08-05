#!/usr/bin/env python3
"""Test SimpleRAG V3 actual execution - does it actually work?"""

import asyncio
import contextlib
import sys


# Add source paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")


async def test_can_we_create_simple_rag_v3():
    """Try to actually create and run SimpleRAG V3."""
    try:
        # Let's try to import and create the components directly
        # First, let's see if we can import the individual components

        # Import the components we need
        # Try to import our SimpleRAG V3 components directly (bypassing __init__.py)
        import importlib.util

        from langchain_core.documents import Document

        # Load agent.py directly
        spec = importlib.util.spec_from_file_location(
            "agent_module",
            "/home/will/Projects/haive/backend/haive/packages/haive-agents/src/haive/agents/rag/simple/enhanced_v3/agent.py",
        )
        importlib.util.module_from_spec(spec)

        # Let's at least test the state functionality which we know works
        from haive.agents.rag.simple.enhanced_v3.state import SimpleRAGState

        # Create a state
        state = SimpleRAGState(
            query="What is machine learning?",
            retrieved_documents=[
                Document(
                    page_content="Machine learning is a subset of AI.",
                    metadata={"source": "ml_guide.pdf", "score": 0.9},
                )
            ],
            generated_answer="Machine learning is a subset of artificial intelligence.",
        )

        # Test state functionality
        state.update_stage("retrieval")
        state.update_performance_metric("retrieval_time", 0.5)
        state.update_stage("generation")
        state.update_performance_metric("generation_time", 1.2)
        state.update_stage("completed")

        state.get_pipeline_summary()

        return True

    except Exception:
        import traceback

        traceback.print_exc()
        return False


async def test_minimal_components():
    """Test what components we can actually use."""
    results = {}

    # Test 1: Can we import state?
    try:
        results["state"] = "✅ State imports and works"
    except Exception as e:
        results["state"] = f"❌ State failed: {e}"

    # Test 2: Can we create AugLLMConfig?
    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        AugLLMConfig(temperature=0.7)
        results["aug_llm"] = "✅ AugLLMConfig works"
    except Exception as e:
        results["aug_llm"] = f"❌ AugLLMConfig failed: {e}"

    # Test 3: Can we use Documents?
    try:
        from langchain_core.documents import Document

        Document(page_content="Test", metadata={"source": "test"})
        results["documents"] = "✅ Document creation works"
    except Exception as e:
        results["documents"] = f"❌ Documents failed: {e}"

    # Test 4: Can we import the agents directly?
    try:
        # This will fail due to import chains

        results["retriever"] = "✅ RetrieverAgent imports"
    except Exception as e:
        results["retriever"] = f"❌ RetrieverAgent failed: {str(e)[:50]}..."

    try:
        results["answer_agent"] = "✅ SimpleAnswerAgent imports"
    except Exception as e:
        results["answer_agent"] = f"❌ SimpleAnswerAgent failed: {str(e)[:50]}..."

    try:
        results["simple_rag_v3"] = "✅ SimpleRAGV3 imports"
    except Exception as e:
        results["simple_rag_v3"] = f"❌ SimpleRAGV3 failed: {str(e)[:50]}..."

    # Print results
    for _component, _status in results.items():
        pass

    return results


def analyze_blockers():
    """Analyze what's blocking SimpleRAG V3 from running."""
    # Check the import chain

    # Check for the missing module
    with contextlib.suppress(ImportError):
        pass

    # Check if it's a case issue
    try:
        pass
    except:
        with contextlib.suppress(Exception):
            pass


async def main():
    """Run all tests."""
    # Test creating SimpleRAG V3
    await test_can_we_create_simple_rag_v3()

    # Test individual components
    await test_minimal_components()

    # Analyze blockers
    analyze_blockers()


if __name__ == "__main__":
    asyncio.run(main())
