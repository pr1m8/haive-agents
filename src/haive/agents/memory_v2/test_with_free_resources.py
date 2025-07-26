"""Test Memory V2 with free/local resources (no API keys needed)."""

import asyncio
import tempfile
from pathlib import Path


async def test_with_huggingface_embeddings():
    """Test memory system with free HuggingFace embeddings."""
    try:
        # Use HuggingFace embeddings (free, no API key)
        from langchain_community.embeddings import HuggingFaceEmbeddings

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False},
        )

        # Test embedding some text
        test_texts = [
            "Alice is an AI researcher at TechCorp",
            "Bob works as CTO at DataCorp",
            "Carol is a data scientist",
        ]

        embeddings.embed_documents(test_texts)

        return embeddings

    except Exception:
        import traceback

        traceback.print_exc()
        return None


async def test_vector_store_with_free_embeddings():
    """Test creating a vector store with free embeddings."""
    embeddings = await test_with_huggingface_embeddings()
    if not embeddings:
        return None

    try:
        from langchain_community.vectorstores import FAISS
        from langchain_core.documents import Document

        # Create some test documents
        documents = [
            Document(
                page_content="Alice Johnson is a senior AI researcher at TechCorp working on neural networks.",
                metadata={"type": "person", "company": "TechCorp"},
            ),
            Document(
                page_content="Bob Smith is the CTO of DataCorp, specializing in distributed systems.",
                metadata={"type": "person", "company": "DataCorp"},
            ),
            Document(
                page_content="TechCorp is a leading AI research company founded in 2020.",
                metadata={"type": "company", "industry": "AI"},
            ),
            Document(
                page_content="DataCorp provides cloud infrastructure solutions for enterprises.",
                metadata={"type": "company", "industry": "Cloud"},
            ),
        ]

        vector_store = FAISS.from_documents(documents, embeddings)

        # Test search
        query = "Who works with AI?"
        results = vector_store.similarity_search(query, k=2)

        for _i, _doc in enumerate(results):
            pass

        return vector_store

    except Exception:
        import traceback

        traceback.print_exc()
        return None


async def test_memory_rag_with_free_resources():
    """Test a simple RAG memory system without paid APIs."""
    vector_store = await test_vector_store_with_free_embeddings()
    if not vector_store:
        return None

    try:
        # Create a simple retriever
        retriever = vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": 3}
        )

        # Test queries
        test_queries = [
            "Tell me about Alice",
            "What companies are mentioned?",
            "Who is the CTO?",
            "What does TechCorp do?",
        ]

        for query in test_queries:
            docs = retriever.invoke(query)
            for _i, _doc in enumerate(docs):
                pass

        # Save the vector store for later use
        temp_dir = tempfile.mkdtemp()
        save_path = Path(temp_dir) / "memory_store"
        vector_store.save_local(str(save_path))

        # Test loading
        FAISS.load_local(
            str(save_path), embeddings, allow_dangerous_deserialization=True
        )

        return retriever

    except Exception:
        import traceback

        traceback.print_exc()
        return None


async def test_memory_state_with_embeddings():
    """Test memory state with embedding support."""
    embeddings = await test_with_huggingface_embeddings()
    if not embeddings:
        return None

    try:
        from haive.agents.memory_v2.memory_state_original import (
            EnhancedMemoryItem,
            ImportanceLevel,
            MemoryState,
            MemoryType,
        )

        # Create memory state
        state = MemoryState(user_id="test_user")

        # Create memories with embeddings
        memories_data = [
            (
                "Alice Johnson is a senior AI researcher at TechCorp.",
                MemoryType.FACTUAL,
                ImportanceLevel.HIGH,
            ),
            (
                "Meeting with Alice scheduled for next Monday at 2 PM.",
                MemoryType.CONVERSATIONAL,
                ImportanceLevel.MEDIUM,
            ),
            (
                "Alice's expertise includes transformer models and NLP.",
                MemoryType.FACTUAL,
                ImportanceLevel.HIGH,
            ),
            (
                "Bob Smith is the CTO of DataCorp.",
                MemoryType.FACTUAL,
                ImportanceLevel.HIGH,
            ),
            (
                "DataCorp is our main technology partner.",
                MemoryType.FACTUAL,
                ImportanceLevel.MEDIUM,
            ),
        ]

        for content, mem_type, importance in memories_data:
            # Create embedding
            embedding_vector = embeddings.embed_query(content)

            # Create enhanced memory with embedding
            memory = EnhancedMemoryItem(
                content=content,
                memory_type=mem_type,
                importance=importance,
                embedding=embedding_vector,
                user_id="test_user",
            )
            state.add_memory_item(memory)

        # Test similarity search using embeddings
        query = "Who works on AI and machine learning?"
        query_embedding = embeddings.embed_query(query)

        # Simple cosine similarity search
        from numpy import dot
        from numpy.linalg import norm

        def cosine_similarity(a, b):
            return dot(a, b) / (norm(a) * norm(b))

        # Score all memories
        scored_memories = []
        for memory_entry in state.memories:
            if memory_entry.memory_item and memory_entry.memory_item.embedding:
                score = cosine_similarity(
                    query_embedding, memory_entry.memory_item.embedding
                )
                scored_memories.append((score, memory_entry))

        # Sort by score and get top results
        scored_memories.sort(key=lambda x: x[0], reverse=True)
        top_results = scored_memories[:3]

        for _i, (score, _entry) in enumerate(top_results):
            pass

        return state

    except Exception:
        import traceback

        traceback.print_exc()
        return None


async def main():
    """Run all free resource tests."""
    # Run tests
    await test_with_huggingface_embeddings()
    await test_vector_store_with_free_embeddings()
    await test_memory_rag_with_free_resources()
    await test_memory_state_with_embeddings()


if __name__ == "__main__":
    # Install sentence-transformers if needed
    try:
        import sentence_transformers
    except ImportError:
        import subprocess

        subprocess.check_call(["poetry", "add", "sentence-transformers"])

    asyncio.run(main())
