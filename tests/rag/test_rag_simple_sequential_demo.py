"""Demo script for RAG + SimpleAgent sequential pattern.

This demonstrates the manual sequential execution without pytest dependencies.
"""

from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig, VectorStoreProvider
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent


# Structured output model
class RAGAnswer(BaseModel):
    """Structured answer generated from RAG retrieval."""

    question: str = Field(description="The original question asked")
    answer: str = Field(description="Comprehensive answer based on retrieved documents")
    confidence: float = Field(description="Confidence in the answer (0-1)")
    key_points: List[str] = Field(description="Key points extracted from the answer")
    sources_used: List[str] = Field(description="Sources referenced in the answer")


def create_sample_documents():
    """Create sample documents for testing."""
    return [
        Document(
            page_content="Haive is an AI agent framework designed for building sophisticated multi-agent systems. "
            "It provides a flexible architecture for creating agents that can work together to solve complex problems.",
            metadata={"source": "haive_overview.md", "section": "introduction"},
        ),
        Document(
            page_content="The core components of Haive include engines, agents, tools, and graphs. "
            "Engines handle LLM interactions, agents orchestrate behavior, tools provide capabilities, "
            "and graphs manage execution flow.",
            metadata={"source": "haive_architecture.md", "section": "components"},
        ),
        Document(
            page_content="Multi-agent systems in Haive can be configured in sequential, parallel, or conditional modes. "
            "Sequential execution passes results from one agent to the next, while parallel execution runs multiple agents simultaneously.",
            metadata={"source": "haive_multi_agent.md", "section": "execution_modes"},
        ),
        Document(
            page_content="RAG (Retrieval-Augmented Generation) in Haive allows agents to access external knowledge. "
            "The BaseRAGAgent handles document retrieval, which can be combined with other agents for answer generation.",
            metadata={"source": "haive_rag.md", "section": "rag_agents"},
        ),
    ]


def main():
    """Run the RAG + SimpleAgent demo."""
    print("=== RAG + SimpleAgent Sequential Demo ===\n")

    # Create sample documents
    print("1. Creating sample documents...")
    documents = create_sample_documents()
    print(f"   Created {len(documents)} documents")

    # Create vector store config
    print("\n2. Setting up vector store...")
    vector_store_config = VectorStoreConfig(
        name="demo_rag_store",
        documents=documents,
        vector_store_provider=VectorStoreProvider.FAISS,
        embedding_model=HuggingFaceEmbeddingConfig(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
    )
    print("   Vector store configured with FAISS and MiniLM embeddings")

    # Create RAG agent
    print("\n3. Creating BaseRAGAgent...")
    rag_agent = BaseRAGAgent(name="document_retriever", engine=vector_store_config)
    print(f"   RAG agent created: {rag_agent.name}")

    # Create answer generator agent
    print("\n4. Creating SimpleAgent for answer generation...")
    answer_agent = SimpleAgent(
        name="answer_generator",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3),
            system_message="""You are an expert answer generator for a RAG system. 
            Given retrieved documents and a question, generate a comprehensive, well-structured answer.
            Always reference your sources and extract key points.""",
        ),
        structured_output_model=RAGAnswer,
        structured_output_version="v2",
    )
    print(f"   Answer agent created: {answer_agent.name}")
    print(f"   Using structured output model: {RAGAnswer.__name__}")

    # Test query
    query = "What are the core components of Haive and how do they work together?"
    print(f"\n5. Testing with query: '{query}'")

    # Step 1: RAG Retrieval
    print("\n--- Step 1: Document Retrieval ---")
    try:
        retrieval_result = rag_agent.run({"query": query})

        # Extract retrieved documents
        retrieved_docs = []
        if (
            isinstance(retrieval_result, dict)
            and "retrieved_documents" in retrieval_result
        ):
            retrieved_docs = retrieval_result["retrieved_documents"]

        print(f"✅ Retrieved {len(retrieved_docs)} documents")

        for i, doc in enumerate(retrieved_docs[:3]):
            print(f"\n   Document {i+1}:")
            print(f"   Source: {doc.metadata.get('source', 'Unknown')}")
            print(f"   Preview: {doc.page_content[:100]}...")

    except Exception as e:
        print(f"❌ Retrieval error: {e}")
        return

    # Step 2: Answer Generation
    print("\n--- Step 2: Answer Generation ---")

    # Format context for answer generation
    context = f"Question: {query}\n\nRetrieved Documents:\n"
    for i, doc in enumerate(retrieved_docs):
        source = doc.metadata.get("source", "Unknown")
        context += f'\n{i+1}. From {source}:\n"{doc.page_content}"\n'

    print(f"Context prepared ({len(context)} chars)")

    try:
        # Generate answer
        answer_prompt = f"""Based on the following retrieved documents, generate a comprehensive answer with key points and source citations.

{context}"""

        answer_result = answer_agent.run(answer_prompt)

        print("\n✅ Answer generated successfully!")
        print(f"   Result type: {type(answer_result)}")

        # Display the structured answer if available
        if isinstance(answer_result, dict) and "analysis" in answer_result:
            analysis = answer_result["analysis"]
            print(f"\n   Structured Answer:")
            print(f"   - Question: {getattr(analysis, 'question', 'N/A')}")
            print(f"   - Confidence: {getattr(analysis, 'confidence', 'N/A')}")
            print(f"   - Key Points: {len(getattr(analysis, 'key_points', []))} points")
            print(
                f"   - Sources Used: {len(getattr(analysis, 'sources_used', []))} sources"
            )
        elif isinstance(answer_result, RAGAnswer):
            print(f"\n   Structured Answer:")
            print(f"   - Question: {answer_result.question}")
            print(f"   - Confidence: {answer_result.confidence}")
            print(f"   - Key Points: {len(answer_result.key_points)} points")
            for point in answer_result.key_points[:3]:
                print(f"     • {point}")
            print(f"   - Sources: {answer_result.sources_used}")
        else:
            print(f"\n   Raw answer: {str(answer_result)[:200]}...")

    except Exception as e:
        print(f"❌ Answer generation error: {e}")
        import traceback

        traceback.print_exc()

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
