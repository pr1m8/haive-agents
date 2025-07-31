"""Demo script for RAG + SimpleAgent sequential pattern.

This demonstrates the manual sequential execution without pytest dependencies.
"""

from langchain_core.documents import Document
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig, VectorStoreProvider
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig
from haive.core.models.llm.base import AzureLLMConfig


# Structured output model
class RAGAnswer(BaseModel):
    """Structured answer generated from RAG retrieval."""

    question: str = Field(description="The original question asked")
    answer: str = Field(description="Comprehensive answer based on retrieved documents")
    confidence: float = Field(description="Confidence in the answer (0-1)")
    key_points: list[str] = Field(description="Key points extracted from the answer")
    sources_used: list[str] = Field(description="Sources referenced in the answer")


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
    # Create sample documents
    documents = create_sample_documents()

    # Create vector store config
    vector_store_config = VectorStoreConfig(
        name="demo_rag_store",
        documents=documents,
        vector_store_provider=VectorStoreProvider.FAISS,
        embedding_model=HuggingFaceEmbeddingConfig(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
    )

    # Create RAG agent
    rag_agent = BaseRAGAgent(name="document_retriever", engine=vector_store_config)

    # Create answer generator agent
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

    # Test query
    query = "What are the core components of Haive and how do they work together?"

    # Step 1: RAG Retrieval
    try:
        retrieval_result = rag_agent.run({"query": query})

        # Extract retrieved documents
        retrieved_docs = []
        if (
            isinstance(retrieval_result, dict)
            and "retrieved_documents" in retrieval_result
        ):
            retrieved_docs = retrieval_result["retrieved_documents"]

        for i, doc in enumerate(retrieved_docs[:3]):
            pass

    except Exception:
        return

    # Step 2: Answer Generation

    # Format context for answer generation
    context = f"Question: {query}\n\nRetrieved Documents:\n"
    for i, doc in enumerate(retrieved_docs):
        source = doc.metadata.get("source", "Unknown")
        context += f'\n{i+1}. From {source}:\n"{doc.page_content}"\n'

    try:
        # Generate answer
        answer_prompt = f"""Based on the following retrieved documents, generate a comprehensive answer with key points and source citations.

{context}"""

        answer_result = answer_agent.run(answer_prompt)

        # Display the structured answer if available
        if isinstance(answer_result, dict) and "analysis" in answer_result:
            answer_result["analysis"]
        elif isinstance(answer_result, RAGAnswer):
            for _point in answer_result.key_points[:3]:
                pass
        else:
            pass

    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
