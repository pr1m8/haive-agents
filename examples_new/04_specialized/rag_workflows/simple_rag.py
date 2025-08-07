"""
Simple RAG Example - Basic Document Q&A Agent
============================================

This example demonstrates a basic RAG (Retrieval-Augmented Generation) agent
that can answer questions about documents using vector search.

Key concepts:
- Document loading and chunking
- Vector store creation and embedding
- Similarity search for retrieval
- Context-aware Q&A generation
"""

import asyncio
from typing import Any, Dict, List

from haive.core.embeddings import HuggingFaceEmbeddings
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from haive.agents.rag.simple.agent import SimpleRAGAgent


async def main():
    """Run simple RAG example."""
    print("Simple RAG Example - Document Q&A\n")
    print("=" * 50)

    # Step 1: Create sample documents about AI agents
    documents = [
        Document(
            page_content="""
            AI agents are autonomous software programs that can perceive their environment,
            make decisions, and take actions to achieve specific goals. They use various
            techniques including machine learning, natural language processing, and 
            reasoning to interact with their surroundings and complete tasks.
            """,
            metadata={"source": "ai_basics.txt", "topic": "introduction"},
        ),
        Document(
            page_content="""
            There are several types of AI agents:
            1. Simple Reflex Agents: React to current percepts without considering history
            2. Model-Based Agents: Maintain internal state to track the world
            3. Goal-Based Agents: Work towards achieving specific objectives
            4. Utility-Based Agents: Maximize a utility function to make optimal decisions
            5. Learning Agents: Improve performance through experience
            """,
            metadata={"source": "agent_types.txt", "topic": "classification"},
        ),
        Document(
            page_content="""
            RAG (Retrieval-Augmented Generation) combines the power of large language
            models with external knowledge retrieval. It works by:
            1. Indexing documents into a vector database
            2. Converting user queries into embeddings
            3. Finding relevant documents through similarity search
            4. Using retrieved context to generate accurate responses
            This approach reduces hallucinations and provides more factual answers.
            """,
            metadata={"source": "rag_explained.txt", "topic": "rag"},
        ),
        Document(
            page_content="""
            Best practices for building AI agents include:
            - Clear goal definition and success metrics
            - Robust error handling and fallback mechanisms
            - Continuous monitoring and improvement
            - Ethical considerations and bias mitigation
            - User feedback integration
            - Transparent decision-making processes
            """,
            metadata={"source": "best_practices.txt", "topic": "guidelines"},
        ),
    ]

    # Step 2: Split documents into chunks
    print("\n1. Chunking documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    all_chunks = []
    for doc in documents:
        chunks = text_splitter.split_documents([doc])
        all_chunks.extend(chunks)

    print(f"   Created {len(all_chunks)} chunks from {len(documents)} documents")

    # Step 3: Create vector store with embeddings
    print("\n2. Creating vector store...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = InMemoryVectorStore(embeddings)
    await vector_store.aadd_documents(all_chunks)
    print(f"   Indexed {len(all_chunks)} chunks in vector store")

    # Step 4: Create SimpleRAGAgent
    print("\n3. Initializing SimpleRAGAgent...")
    rag_agent = SimpleRAGAgent(
        name="document_qa",
        engine=AugLLMConfig(
            temperature=0.3,  # Lower temperature for factual responses
            system_message="You are a helpful Q&A assistant. Answer questions based on the provided context.",
        ),
        vector_store=vector_store,
        k=3,  # Retrieve top 3 most relevant chunks
    )

    # Step 5: Ask questions about the documents
    questions = [
        "What are AI agents?",
        "What are the different types of AI agents?",
        "How does RAG work?",
        "What are some best practices for building AI agents?",
        "What is a utility-based agent?",
    ]

    print("\n4. Asking questions:\n")
    for i, question in enumerate(questions, 1):
        print(f"Q{i}: {question}")

        # Run the RAG agent
        response = await rag_agent.arun(question)

        print(f"A{i}: {response}\n")
        print("-" * 50 + "\n")

    # Step 6: Demonstrate handling of out-of-scope questions
    print("5. Testing out-of-scope question:\n")
    out_of_scope = "What is the weather like today?"
    print(f"Q: {out_of_scope}")
    response = await rag_agent.arun(out_of_scope)
    print(f"A: {response}\n")

    # Step 7: Show retrieved context for transparency
    print("6. Demonstrating context retrieval:\n")
    query = "Explain model-based agents"
    print(f"Query: {query}")

    # Get similar documents
    relevant_docs = await vector_store.asimilarity_search(query, k=2)
    print(f"\nRetrieved {len(relevant_docs)} relevant chunks:")
    for i, doc in enumerate(relevant_docs, 1):
        print(f"\n   Chunk {i} (from {doc.metadata.get('source', 'unknown')}):")
        print(f"   {doc.page_content[:100]}...")

    # Get answer with context
    response = await rag_agent.arun(query)
    print(f"\nFinal Answer: {response}")


if __name__ == "__main__":
    print("Starting Simple RAG Example...")
    print("This demonstrates basic document Q&A with vector search\n")

    asyncio.run(main())

    print("\n✅ Simple RAG example completed!")
    print("\nKey takeaways:")
    print("- Documents are chunked for better retrieval")
    print("- Vector embeddings enable semantic search")
    print("- Retrieved context grounds LLM responses")
    print("- SimpleRAGAgent handles the full RAG pipeline")
