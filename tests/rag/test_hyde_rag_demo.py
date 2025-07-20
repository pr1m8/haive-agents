"""Demo: HyDE RAG Pattern - Hypothetical Document Embeddings for Better Retrieval.

This demonstrates how HyDE (Hypothetical Document Embeddings) improves RAG retrieval:

1. Generate a hypothetical document that would answer the query
2. Use the hypothetical document for similarity search (better semantic matching)
3. Retrieve real documents based on hypothetical document embeddings
4. Generate final answer from retrieved real documents

The key insight: Hypothetical documents bridge the semantic gap between queries and documents.
"""

import contextlib

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
    # 1. Create knowledge base
    documents = create_sample_knowledge_base()

    # 2. Set up vector store
    vector_config = VectorStoreConfig(
        name="hyde_demo_store",
        documents=documents,
        vector_store_provider=VectorStoreProvider.FAISS,
        embedding_model=HuggingFaceEmbeddingConfig(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
    )

    # 3. Create agents

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

    # RAG Retriever
    rag_retriever = BaseRAGAgent(name="retriever", engine=vector_config)

    # Answer Generator
    answer_generator = SimpleAgent(
        name="answerer",
        engine=AugLLMConfig(
            system_message="Generate clear answers from retrieved documents"
        ),
    )

    # 4. Test query
    query = "How does backpropagation work in neural networks?"

    # 5. Standard retrieval (for comparison)
    try:
        standard_result = rag_retriever.run({"query": query})
        standard_docs = (
            standard_result.get("retrieved_documents", [])
            if isinstance(standard_result, dict)
            else []
        )
        for _doc in standard_docs[:2]:
            pass
    except Exception:
        pass

    # 6. HyDE-enhanced retrieval

    # Generate hypothetical document
    try:
        hyde_result = hyde_generator.run(query)

        if hasattr(hyde_result, "hypothetical_doc"):
            hypothetical_doc = hyde_result.hypothetical_doc
        else:
            hypothetical_doc = str(hyde_result)
    except Exception:
        return

    # Use hypothetical document for retrieval
    try:
        hyde_retrieval = rag_retriever.run({"query": hypothetical_doc})
        hyde_docs = (
            hyde_retrieval.get("retrieved_documents", [])
            if isinstance(hyde_retrieval, dict)
            else []
        )
        for _doc in hyde_docs[:2]:
            pass
    except Exception:
        hyde_docs = []

    # 7. Generate final answer

    answer_context = f"""Question: {query}

Retrieved Documents (via HyDE):
{chr(10).join([f"- {doc.page_content}" for doc in hyde_docs[:2]])}

Provide a clear, concise answer based on the retrieved information."""

    with contextlib.suppress(Exception):
        answer_generator.run(answer_context)

    # 8. Summary


def compare_retrieval_methods():
    """Compare standard vs HyDE retrieval."""
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

        # Standard
        try:
            std_result = retriever.run({"query": query})
            (
                std_result.get("retrieved_documents", [])
                if isinstance(std_result, dict)
                else []
            )
        except:
            pass

        # HyDE
        try:
            hyde_result = hyde_gen.run(query)
            hypothetical = (
                hyde_result.hypothetical_doc
                if hasattr(hyde_result, "hypothetical_doc")
                else str(hyde_result)
            )
            hyde_ret = retriever.run({"query": hypothetical})
            (
                hyde_ret.get("retrieved_documents", [])
                if isinstance(hyde_ret, dict)
                else []
            )
        except:
            pass


if __name__ == "__main__":
    # Run main demo
    demonstrate_hyde_rag()

    # Run comparison
    compare_retrieval_methods()
