"""Test BaseRAG to SimpleAgent flow with ChatPromptTemplate."""

import asyncio

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.embedding.providers.HuggingFaceEmbeddingConfig import (
    HuggingFaceEmbeddingConfig,
)


# Define the RAG answer prompt template with retrieved_documents
RAG_ANSWER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant that answers questions based on retrieved documents.",
        ),
        (
            "human",
            """Based on the following retrieved documents, answer the question.

Retrieved Documents:
{retrieved_documents}

Question: {query}

Answer:""",
        ),
    ]
)


# Optional: Structured output model
class RAGAnswer(BaseModel):
    """Structured answer from RAG."""

    answer: str = Field(description="The answer based on retrieved documents")
    sources: list[str] = Field(description="Source documents used")
    confidence: float = Field(description="Confidence score 0-1")


async def test_baserag_to_simple_flow():
    """Test BaseRAG → SimpleAgent flow."""
    # 1. Create sample documents
    documents = [
        Document(
            page_content="Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
            metadata={"source": "ML Guide", "page": 1},
        ),
        Document(
            page_content="Deep learning uses neural networks with multiple layers to process complex patterns.",
            metadata={"source": "DL Handbook", "page": 5},
        ),
        Document(
            page_content="Natural Language Processing enables computers to understand human language.",
            metadata={"source": "NLP Book", "page": 2},
        ),
    ]

    # 2. Create BaseRAGAgent
    embedding_config = HuggingFaceEmbeddingConfig(model="sentence-transformers/all-MiniLM-L6-v2")

    base_rag = BaseRAGAgent.from_documents(
        documents=documents,
        embedding_config=embedding_config,
        name="retriever",
        k=2,  # Get top 2 documents
    )

    # 3. Create SimpleAgent with ChatPromptTemplate
    simple_agent = SimpleAgent(
        name="answer_generator",
        engine=AugLLMConfig(
            prompt_template=RAG_ANSWER_PROMPT,
            structured_output_model=RAGAnswer,  # Optional structured output
            temperature=0.7,
        ),
    )

    # 4. Test the flow
    query = "What is machine learning?"

    # Step 1: Retrieve documents with BaseRAG
    retrieval_result = await base_rag.arun(query)

    # Show what BaseRAG returns

    # Format retrieved documents for display
    retrieved_docs_text = "\n\n".join(
        [
            f"[Source: {doc.metadata.get('source', 'Unknown')}]\n{doc.page_content}"
            for doc in retrieval_result.retrieved_documents
        ]
    )

    # Step 2: Generate answer with SimpleAgent

    # Prepare input for SimpleAgent with ChatPromptTemplate variables
    answer_input = {"retrieved_documents": retrieved_docs_text, "query": query}

    answer = await simple_agent.arun(answer_input)

    if isinstance(answer, RAGAnswer):
        pass
    else:
        pass

    # Alternative: Without structured output
    simple_agent_v2 = SimpleAgent(
        name="simple_answer",
        engine=AugLLMConfig(prompt_template=RAG_ANSWER_PROMPT, temperature=0.7),
    )

    await simple_agent_v2.arun(answer_input)


if __name__ == "__main__":
    asyncio.run(test_baserag_to_simple_flow())
