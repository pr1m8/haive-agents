"""Test the rewritten SimpleRAGAgent with ProperMultiAgent."""

import sys

sys.path.insert(0, "packages/haive-agents/src")
sys.path.insert(0, "packages/haive-core/src")

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage

from haive.agents.rag.simple.agent import SimpleRAGAgent


def test_simple_rag_agent():
    """Test SimpleRAGAgent with ProperMultiAgent."""
    print("=== SIMPLE RAG AGENT TEST ===")

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
    print("\n1. Creating SimpleRAGAgent:")
    try:
        rag_agent = SimpleRAGAgent.from_documents(
            documents=documents, name="Test RAG Agent"
        )
        print("   ✅ SimpleRAGAgent created successfullyy")
        print(f"   Agent name: {rag_agent.name}")
        print(f"   Execution mode: {rag_agent.execution_mode}")
        print(f"   Agents: {list(rag_agent.agents.keys())}")
        print(f"   State schema: {rag_agent.state_schema.__name__}")

    except Exception as e:
        print(f"   ❌ SimpleRAGAgent creation failed: {e}")
        import traceback

        traceback.print_exc()
        return

    # Test state creation
    print("\n2. Testing state creation:")
    try:
        state = rag_agent.state_schema(
            messages=[HumanMessage(content="What is the capital of France?")]
        )
        print("   ✅ State created successfullyy")
        print(f"   State.agents: {list(state.agents.keys())}")
        print(f"   State.messages: {len(state.messages)}")

    except Exception as e:
        print(f"   ❌ State creation failed: {e}")
        import traceback

        traceback.print_exc()
        return

    # Test graph construction
    print("\n3. Testing graph construction:")
    try:
        graph = rag_agent.build_graph()
        print("   ✅ Graph built successfullyy")
        print(f"   Graph nodes: {list(graph.nodes.keys())}")
        print(f"   Graph edges: {list(graph.edges)}")

    except Exception as e:
        print(f"   ❌ Graph construction failed: {e}")
        import traceback

        traceback.print_exc()
        return

    # Test RAG execution
    print("\n4. Testing RAG execution:")
    try:
        input_data = {
            "messages": [HumanMessage(content="What is the capital of France?")]
        }
        result = rag_agent.invoke(input_data)
        print("   ✅ RAG execution completedd")
        print(f"   Result type: {type(result)}")
        if hasattr(result, "messages"):
            print(f"   Final messages: {len(result.messages)}")
            # Check if we got both retrieval and answer
            if len(result.messages) > 1:
                print("   ✅ Both retrieval and answer agents executedd")
                print(f"   Last message: {result.messages[-1].content[:100]}...")

    except Exception as e:
        print(f"   ❌ RAG execution failed: {e}")
        import traceback

        traceback.print_exc()

    print("\n✅ Simple RAG Agent test completed")


if __name__ == "__main__":
    test_simple_rag_agent()
