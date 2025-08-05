#!/usr/bin/env python3
"""Test DocumentGraderAgent only - ensure it works with real documents."""

import asyncio
import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")


from haive.agents.rag.agentic.document_grader import DocumentGraderAgent


async def test_document_grader_simple():
    """Test DocumentGraderAgent with simple real documents."""
    # Create the agent
    grader = DocumentGraderAgent.create_default(temperature=0.0)

    # Simple test documents
    test_docs = [
        {
            "id": "doc1",
            "content": "Machine learning is a subset of artificial intelligence.",
            "metadata": {"source": "ml_guide.pdf"},
        },
        {
            "id": "doc2",
            "content": "Pizza is a traditional Italian dish with tomato sauce.",
            "metadata": {"source": "food_guide.pdf"},
        },
    ]

    query = "What is machine learning?"

    # Test using the convenience method
    try:
        result = await grader.grade_documents(query, test_docs)

        # Check if it's the expected structured response
        if hasattr(result, "document_decisions"):
            for _decision in result.document_decisions:
                pass
        else:
            pass

    except Exception:
        import traceback

        traceback.print_exc()

    # Test direct agent call

    try:
        # Format input exactly as expected
        input_data = {"query": query, "documents": test_docs}

        direct_result = await grader.arun(input_data)

        # Try to access structured output
        if hasattr(direct_result, "get") and "document_binary_response" in direct_result:
            structured = direct_result["document_binary_response"]
            if hasattr(structured, "document_decisions"):
                pass
        elif hasattr(direct_result, "keys"):
            pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_document_grader_simple())
