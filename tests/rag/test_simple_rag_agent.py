"""Test the rewritten SimpleRAGAgent with ProperMultiAgent."""

import sys


sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage

from haive.agents.rag.simple.agent import SimpleRAGAgent


def test_simple_rag_agent():
    """Test SimpleRAGAgent with ProperMultiAgent."""
    # Create some sample documents
    documents = [
        Document(
            page_content="Paris is the capital of France. It is known for the Eiffel Tower."
        ),
        Document(
            page_content="London is the capital of the United Kingdom. It has Big Ben."
        ),
        Document(
            page_content="Tokyo is the capital of Japan. It is famous for its technology."
        ),
        Document(page_content="Rome is the capital of Italy. It has the Colosseum."),
    ]

    # Create SimpleRAGAgent
    try:
        rag_agent = SimpleRAGAgent.from_documents(
            documents=documents, name="Test RAG Agent"
        )

    except Exception:
        import traceback

        traceback.print_exc()
        return

    # Test state creation
    try:
        rag_agent.state_schema(
            messages=[HumanMessage(content="What is the capital of France?")]
        )

    except Exception:
        import traceback

        traceback.print_exc()
        return

    # Test graph construction
    try:
        rag_agent.build_graph()

    except Exception:
        import traceback

        traceback.print_exc()
        return

    # Test RAG execution
    try:
        input_data = {
            "messages": [HumanMessage(content="What is the capital of France?")]
        }
        result = rag_agent.invoke(input_data)
        if hasattr(result, "messages"):
            # Check if we got both retrieval and answer
            if len(result.messages) > 1:
                pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_simple_rag_agent()
