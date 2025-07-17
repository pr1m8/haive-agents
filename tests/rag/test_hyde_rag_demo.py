"""Demo: HyDE RAG Pattern - Hypothetical Document Embeddings for Better Retrieval

This demonstrates how HyDE (Hypothetical Document Embeddings) improves RAG retrieval:

1. Generate a hypothetical document that would answer the query
2. Use the hypothetical document for similarity search (better semantic matching)
3. Retrieve real documents based on hypothetical document embeddings
4. Generate final answer from retrieved real documents

The key insight: Hypothetical documents bridge the semantic gap between queries and documents.
"""

from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig, VectorStoreProvider
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent


# HyDE Result Model
class HyDEResult(BaseModel):
    """Hypothetical Document result."""

    hypothetical_doc: str = Field(description="Generated hypothetical document")
    confidence: float = Field(description="Confidence (0-1)", ge=0.0, le=1.0)


# HyDE Prompt
HYDE_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """Generate a detailed hypothetical document that would answer the question.
Write as if creating an authoritative reference document with specific details and examples.
Do not mention this is hypothetical - write as stating facts.""",
        ),
        ("human", "Generate a document answering: {query}"),
    ]
)


def create_sample_knowledge_base():
    """Create sample documents showing where HyDE helps."""
    return [
        Document(
            page_content="""Neural networks consist of interconnected layers of nodes. Each node 
            applies weights to inputs, adds bias, and uses activation functions like ReLU or sigmoid. 
            Backpropagation adjusts weights to minimize loss. Common architectures include CNNs for 
            images, RNNs for sequences, and Transformers for language tasks.""",
            metadata={"source": "neural_networks.md"},
        ),
        Document(
            page_content="""Machine learning optimization techniques include gradient descent variants. 
            SGD processes one sample at a time. Mini-batch GD balances efficiency and convergence. 
            Adam combines momentum and adaptive learning rates. Learning rate scheduling and early 
            stopping prevent overfitting.""",
            metadata={"source": "ml_optimization.md"},
        ),
        Document(
            page_content="""Deep learning revolutionized AI through automatic feature extraction. 
            Key breakthroughs: AlexNet (2012) for computer vision, LSTM for sequences, Attention 
            mechanism leading to Transformers. GPT and BERT transformed NLP. Challenges include 
            computational requirements and interpretability.""",
            metadata={"source": "deep_learning_history.md"},
        ),
    ]


def demonstrate_hyde_rag():
    """Demonstrate the HyDE RAG pattern."""
    print("=== HyDE RAG Pattern Demo ===\n")

    # 1. Create knowledge base
    print("1. Creating knowledge base...")
    documents = create_sample_knowledge_base()
    print(f"   Created {len(documents)} documents about ML/AI")

    # 2. Set up vector store
    print("\n2. Setting up vector store...")
    vector_config = VectorStoreConfig(
        name="hyde_demo_store",
        documents=documents,
        vector_store_provider=VectorStoreProvider.FAISS,
        embedding_model=HuggingFaceEmbeddingConfig(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
    )

    # 3. Create agents
    print("\n3. Creating agents...")

    # HyDE Generator
    hyde_generator = SimpleAgent(
        name="hyde_generator",
        engine=AugLLMConfig(
            prompt_template=HYDE_PROMPT,
            system_message="Generate hypothetical documents",
        ),
        structured_output_model=HyDEResult,
        structured_output_version="v2",
    )
    print("   ✅ HyDE generator created")

    # RAG Retriever
    rag_retriever = BaseRAGAgent(name="retriever", engine=vector_config)
    print("   ✅ RAG retriever created")

    # Answer Generator
    answer_generator = SimpleAgent(
        name="answerer",
        engine=AugLLMConfig(
            system_message="Generate clear answers from retrieved documents"
        ),
    )
    print("   ✅ Answer generator created")

    # 4. Test query
    query = "How does backpropagation work in neural networks?"
    print(f"\n4. Testing with query: '{query}'")

    # 5. Standard retrieval (for comparison)
    print("\n5. Standard Retrieval (direct query):")
    try:
        standard_result = rag_retriever.run({"query": query})
        standard_docs = (
            standard_result.get("retrieved_documents", [])
            if isinstance(standard_result, dict)
            else []
        )
        print(f"   Retrieved {len(standard_docs)} documents")
        for doc in standard_docs[:2]:
            print(f"   - {doc.metadata.get('source')}: {doc.page_content[:60]}...")
    except Exception as e:
        print(f"   Error: {e}")

    # 6. HyDE-enhanced retrieval
    print("\n6. HyDE-Enhanced Retrieval:")

    # Generate hypothetical document
    print("   a) Generating hypothetical document...")
    try:
        hyde_result = hyde_generator.run(query)

        if hasattr(hyde_result, "hypothetical_doc"):
            hypothetical_doc = hyde_result.hypothetical_doc
            print(f"   ✅ Generated {len(hypothetical_doc)} char hypothetical document")
            print(f"   Preview: '{hypothetical_doc[:100]}...'")
            print(f"   Confidence: {hyde_result.confidence}")
        else:
            hypothetical_doc = str(hyde_result)
            print(f"   Generated: {hypothetical_doc[:100]}...")
    except Exception as e:
        print(f"   Error generating HyDE: {e}")
        return

    # Use hypothetical document for retrieval
    print("\n   b) Retrieving with hypothetical document...")
    try:
        hyde_retrieval = rag_retriever.run({"query": hypothetical_doc})
        hyde_docs = (
            hyde_retrieval.get("retrieved_documents", [])
            if isinstance(hyde_retrieval, dict)
            else []
        )
        print(f"   ✅ Retrieved {len(hyde_docs)} documents using HyDE")
        for doc in hyde_docs[:2]:
            print(f"   - {doc.metadata.get('source')}: {doc.page_content[:60]}...")
    except Exception as e:
        print(f"   Error in HyDE retrieval: {e}")
        hyde_docs = []

    # 7. Generate final answer
    print("\n7. Generating final answer...")

    answer_context = f"""Question: {query}

Retrieved Documents (via HyDE):
{chr(10).join([f"- {doc.page_content}" for doc in hyde_docs[:2]])}

Provide a clear, concise answer based on the retrieved information."""

    try:
        answer = answer_generator.run(answer_context)
        print(f"\n   Final Answer:")
        print(f"   {answer}")
    except Exception as e:
        print(f"   Error generating answer: {e}")

    # 8. Summary
    print("\n=== HyDE Benefits Demonstrated ===")
    print("1. Query asks about 'backpropagation' - a specific technical term")
    print("2. Hypothetical document includes related concepts and context")
    print("3. Retrieval using hypothetical doc finds semantically similar content")
    print("4. Final answer benefits from better document retrieval")
    print("\nHyDE bridges the gap between how users ask questions and how")
    print("information is stored in documents, leading to better retrieval!")


def compare_retrieval_methods():
    """Compare standard vs HyDE retrieval."""
    print("\n\n=== Retrieval Method Comparison ===\n")

    queries = [
        "What are the main optimization algorithms in deep learning?",
        "Explain the history and impact of transformer models",
        "How do convolutional layers work?",
    ]

    # Set up
    documents = create_sample_knowledge_base()
    vector_config = VectorStoreConfig(
        name="comparison_store",
        documents=documents,
        vector_store_provider=VectorStoreProvider.FAISS,
        embedding_model=HuggingFaceEmbeddingConfig(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
    )

    retriever = BaseRAGAgent(name="retriever", engine=vector_config)
    hyde_gen = SimpleAgent(
        name="hyde",
        engine=AugLLMConfig(prompt_template=HYDE_PROMPT),
        structured_output_model=HyDEResult,
        structured_output_version="v2",
    )

    for query in queries:
        print(f"\nQuery: '{query}'")

        # Standard
        try:
            std_result = retriever.run({"query": query})
            std_docs = (
                std_result.get("retrieved_documents", [])
                if isinstance(std_result, dict)
                else []
            )
            print(
                f"Standard: Retrieved from {[d.metadata.get('source') for d in std_docs[:2]]}"
            )
        except:
            print("Standard: Error")

        # HyDE
        try:
            hyde_result = hyde_gen.run(query)
            hypothetical = (
                hyde_result.hypothetical_doc
                if hasattr(hyde_result, "hypothetical_doc")
                else str(hyde_result)
            )
            hyde_ret = retriever.run({"query": hypothetical})
            hyde_docs = (
                hyde_ret.get("retrieved_documents", [])
                if isinstance(hyde_ret, dict)
                else []
            )
            print(
                f"HyDE: Retrieved from {[d.metadata.get('source') for d in hyde_docs[:2]]}"
            )
        except:
            print("HyDE: Error")


if __name__ == "__main__":
    # Run main demo
    demonstrate_hyde_rag()

    # Run comparison
    compare_retrieval_methods()
