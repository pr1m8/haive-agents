# Base RAG Agent

Base Retrieval-Augmented Generation (RAG) agent that provides document retrieval functionality using vector similarity search.

## Overview

The `BaseRAGAgent` is a foundational agent that handles document retrieval from vector stores. It extends the base `Agent` class and includes `RetrieverMixin` for enhanced retrieval capabilities.

## Architecture

```python
BaseRAGAgent = Agent + RetrieverMixin + VectorStore + Embeddings
```

### Components

- **Agent Base**: Core agent functionality
- **RetrieverMixin**: Automatic vector store configuration
- **Vector Store**: Document storage and similarity search
- **Embedding Model**: Text-to-vector conversion (default: HuggingFace)

## Usage

### Basic Usage

```python
from haive.agents.rag.base.agent import BaseRAGAgent

# Create with default configuration
retriever = BaseRAGAgent(name="my_retriever")

# Execute retrieval
result = retriever.run("machine learning concepts")
print(result)  # Returns retrieved documents and context
```

### From Documents

```python
from langchain_core.documents import Document

# Create from document list
documents = [
    Document(page_content="Machine learning is...", metadata={"source": "ml_book"}),
    Document(page_content="Neural networks are...", metadata={"source": "nn_guide"})
]

retriever = BaseRAGAgent.from_documents(
    documents=documents,
    name="doc_retriever"
)

result = retriever.run("What are neural networks?")
```

## Configuration

### Default Configuration

```python
class BaseRAGAgent(RetrieverMixin, Agent):
    engine: BaseRetrieverConfig | VectorStoreConfig = Field(
        default_factory=lambda: VectorStoreConfig(
            name="default_vectorstore",
            provider="InMemory",
            embedding_config=HuggingFaceEmbeddingConfig()
        )
    )
```

## Testing

### Real Component Testing

```python
def test_base_rag_agent_retrieval():
    """Test BaseRAGAgent with real components - NO MOCKS."""
    # Create test documents
    docs = [
        Document(page_content="Python is a programming language"),
        Document(page_content="Machine learning uses algorithms")
    ]

    # Create agent from documents
    agent = BaseRAGAgent.from_documents(documents=docs, name="test_agent")

    # Real retrieval
    result = agent.run("programming language")

    # Verify structure
    assert "retrieved_documents" in result
    assert "context" in result
    assert len(result["retrieved_documents"]) > 0
```

## See Also

- [SimpleRAGAgent](../simple/README.md) - Complete RAG workflow
- [CollectiveRAGAgent](../collective_rag_agent_v4.py) - Multiple RAG sources
