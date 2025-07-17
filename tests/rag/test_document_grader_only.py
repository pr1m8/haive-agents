#!/usr/bin/env python3
"""Test DocumentGraderAgent only - ensure it works with real documents."""

import asyncio
import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.documents import Document

from haive.agents.rag.agentic.document_grader import DocumentGraderAgent


async def test_document_grader_simple():
    """Test DocumentGraderAgent with simple real documents."""
    print("🧪 Testing DocumentGraderAgent with Real Documents")
    print("=" * 50)

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

    print(f"Query: {query}")
    print(f"Documents: {len(test_docs)}")

    # Test using the convenience method
    try:
        result = await grader.grade_documents(query, test_docs)
        print(f"✅ Method call successful - result type: {type(result)}")

        # Check if it's the expected structured response
        if hasattr(result, "document_decisions"):
            print(f"✅ Found document_decisions: {len(result.document_decisions)}")
            for decision in result.document_decisions:
                print(
                    f"  - {decision.document_id}: {decision.decision} (confidence: {decision.confidence})"
                )
        else:
            print(f"❌ No document_decisions found in result")
            print(
                f"Result keys: {list(result.keys()) if hasattr(result, 'keys') else 'No keys'}"
            )

    except Exception as e:
        print(f"❌ Method call failed: {e}")
        import traceback

        traceback.print_exc()

    # Test direct agent call
    print("\n" + "=" * 50)
    print("Testing direct agent call...")

    try:
        # Format input exactly as expected
        input_data = {"query": query, "documents": test_docs}

        direct_result = await grader.arun(input_data)
        print(f"✅ Direct call successful - result type: {type(direct_result)}")

        # Try to access structured output
        if (
            hasattr(direct_result, "get")
            and "document_binary_response" in direct_result
        ):
            structured = direct_result["document_binary_response"]
            print(f"✅ Found structured output: {type(structured)}")
            if hasattr(structured, "document_decisions"):
                print(f"✅ Found decisions: {len(structured.document_decisions)}")
        else:
            print(f"❌ No structured output found")
            if hasattr(direct_result, "keys"):
                print(f"Available keys: {list(direct_result.keys())}")

    except Exception as e:
        print(f"❌ Direct call failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ DocumentGraderAgent test completed")


if __name__ == "__main__":
    asyncio.run(test_document_grader_simple())
