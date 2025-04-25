"""
Example of using the RAG agent with the new architecture.
"""

import logging
from langchain_community.document_loaders import WebBaseLoader

# Import from our architecture
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig
from haive.core.engine.vectorstore import VectorStoreConfig
from haive.core.engine.retriever import VectorStoreRetrieverConfig
# from haive.agents.rag.base.config import BaseRAGConfig
# from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.rag.llm_rag.config import LLMRAGConfig
from haive.agents.rag.llm_rag.agent import LLMRAGAgent

def main():
    # Configure logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Clear any existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add a basic stream handler with formatting
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 1. Load documents
    logger.info("Loading documents...")
    docs = WebBaseLoader("https://langchain.com/docs/").load()
    logger.info(f"Loaded {len(docs)} documents")

    # 2. Create VectorStore config
    logger.info("Creating vector store...")
    vs_config = VectorStoreConfig(
        name="langchain_docs_vectorstore",
        documents=docs,
        embedding_model=HuggingFaceEmbeddingConfig(
            model="sentence-transformers/all-mpnet-base-v2"
        )
    )

    # 3. Create retriever config (Method 1: explicitly)
    logger.info("Creating retriever config (Method 1)...")
    retriever_config = VectorStoreRetrieverConfig(
        name="langchain_docs_retriever",
        vector_store_config=vs_config,
        k=3
    )

    # Method 2: Pass vector store directly to RAG config
    logger.info("Creating RAG agent (Method 2)...")
    rag_agent_1 = LLMRAGAgent(
        LLMRAGConfig(
            name="direct_vectorstore_rag",
            retriever_config=vs_config
        )
    )

    logger.info("Creating RAG agent with explicit retriever...")
    rag_agent_2 = LLMRAGAgent(
        LLMRAGConfig(
            name="explicit_retriever_rag",
            retriever_config=retriever_config
        )
    )

    # 4. Run queries
    query = "What is LangChain?"

    logger.info(f"Running query with agent 1: {query}")
    result_1 = rag_agent_1.run({"query": query})
    logger.info(f"Agent 1 state: {result_1}")

    logger.info(f"Running query with agent 2: {query}")
    result_2 = rag_agent_2.run({"query": query})
    logger.info(f"Agent 2 state: {result_2}")

    # Now you can index the dict normally, e.g.:
    retrieved_1 = result_1.get("retrieved_documents", [])
    retrieved_2 = result_2.get("retrieved_documents", [])

    logger.info(f"Retrieved {len(retrieved_1)} documents (Agent 1)")
    logger.info(f"Retrieved {len(retrieved_2)} documents (Agent 2)")

    if retrieved_1:
        logger.info("First document from agent 1:")
        logger.info(retrieved_1[0]["page_content"][:200] + "...")

    if retrieved_2:
        logger.info("First document from agent 2:")
        logger.info(retrieved_2[0]["page_content"][:200] + "...")

    return result_1, result_2


if __name__ == "__main__":
    main()
