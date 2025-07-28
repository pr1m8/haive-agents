"""Test BaseRAGAgent with sample documents to understand its output schema."""

import asyncio

from haive.core.engine.embedding.providers.HuggingFaceEmbeddingConfig import (
    HuggingFaceEmbeddingConfig,
)
from langchain_core.documents import Document

from haive.agents.rag.base.agent import BaseRAGAgent


async def test_baserag_with_documents():
    """Test BaseRAGAgent with sample documents and debug mode."""
    print("\n=== Testing BaseRAGAgent Output Schema ===\n")

    # 1. Create sample documents
    documents = [
        Document(
            page_content="Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
            metadata={"source": "AI Basics", "topic": "ML", "page": 1},
        ),
        Document(
            page_content="Deep learning is a specialized form of machine learning that uses neural networks with multiple layers to progressively extract higher-level features from raw input.",
            metadata={"source": "Deep Learning Guide", "topic": "DL", "page": 5},
        ),
        Document(
            page_content="Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and manipulate human language.",
            metadata={"source": "NLP Handbook", "topic": "NLP", "page": 2},
        ),
        Document(
            page_content="Reinforcement learning is an area of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.",
            metadata={"source": "RL Theory", "topic": "RL", "page": 10},
        ),
        Document(
            page_content="Computer vision is a field of AI that trains computers to interpret and understand the visual world using digital images from cameras and videos.",
            metadata={"source": "CV Guide", "topic": "CV", "page": 3},
        ),
    ]

    print(f"Created {len(documents)} sample documents about AI topics\n")

    # 2. Create embedding configuration
    embedding_config = HuggingFaceEmbeddingConfig(
        model="sentence-transformers/all-MiniLM-L6-v2", use_cache=True
    )

    # 3. Create BaseRAGAgent from documents
    print("Creating BaseRAGAgent from documents...")
    try:
        base_rag = BaseRAGAgent.from_documents(
            documents=documents,
            embedding_config=embedding_config,
            name="test_baserag",
            k=3,  # Retrieve top 3 documents
            similarity_threshold=0.0,  # No threshold for testing
        )

        print(f"✅ Created BaseRAGAgent: {base_rag.name}")
        print(f"   Engine type: {type(base_rag.engine).__name__}")
        print(f"   Engine config: {base_rag.engine}")

    except Exception as e:
        print(f"❌ Error creating BaseRAGAgent: {e}")
        import traceback

        traceback.print_exc()
        return

    # 4. Build the graph to understand structure
    print("\n4. Building agent graph...")
    try:
        graph = base_rag.build_graph()
        print(f"   Graph name: {graph.name}")
        print(f"   Graph nodes: {list(graph.nodes)}")
        print(f"   Graph edges: {list(graph.edges)}")
    except Exception as e:
        print(f"   Error building graph: {e}")

    # 5. Test retrieval with debug mode
    print("\n5. Testing retrieval with debug=True...")
    test_queries = [
        "What is machine learning?",
        "Explain deep learning",
        "How does reinforcement learning work?",
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*60}")
        print(f"Query {i}: {query}")
        print(f"{'='*60}\n")

        try:
            # Run with debug mode
            result = await base_rag.arun(query, debug=True)

            # Analyze the result structure
            print("\n📊 Result Analysis:")
            print(f"   Type: {type(result)}")

            if isinstance(result, dict):
                print(f"   Keys: {list(result.keys())}")

                # Check for different possible output formats
                if "documents" in result:
                    docs = result["documents"]
                    print("\n   'documents' field:")
                    print(f"      - Count: {len(docs)}")
                    if docs:
                        print(f"      - First doc type: {type(docs[0])}")
                        print(
                            f"      - First doc preview: {docs[0].page_content[:100]}..."
                        )
                        print(f"      - First doc metadata: {docs[0].metadata}")

                if "retrieved_documents" in result:
                    docs = result["retrieved_documents"]
                    print("\n   'retrieved_documents' field:")
                    print(f"      - Count: {len(docs)}")
                    if docs:
                        print(f"      - First doc type: {type(docs[0])}")
                        print(
                            f"      - First doc preview: {docs[0].page_content[:100]}..."
                        )

                if "output" in result:
                    print("\n   'output' field:")
                    print(f"      - Type: {type(result['output'])}")
                    print(f"      - Content: {str(result['output'])[:200]}...")

                if "metadata" in result:
                    print("\n   'metadata' field:")
                    print(f"      - Content: {result['metadata']}")

                # Show full result structure
                print("\n   Full result structure:")
                import json

                def serialize_result(obj):
                    if isinstance(obj, Document):
                        return {
                            "page_content": obj.page_content[:100] + "...",
                            "metadata": obj.metadata,
                        }
                    elif isinstance(obj, list) and obj and isinstance(obj[0], Document):
                        return [
                            serialize_result(doc) for doc in obj[:2]
                        ]  # First 2 docs
                    elif isinstance(obj, dict):
                        return {k: serialize_result(v) for k, v in obj.items()}
                    else:
                        return (
                            str(obj)[:200] + "..." if len(str(obj)) > 200 else str(obj)
                        )

                print(json.dumps(serialize_result(result), indent=2))

            elif isinstance(result, list):
                print(f"   Result is a list with {len(result)} items")
                if result and isinstance(result[0], Document):
                    print("   List contains Document objects")
                    print(f"   First document: {result[0].page_content[:100]}...")
                    print(f"   First doc metadata: {result[0].metadata}")

            elif isinstance(result, str):
                print(f"   Result is a string: {result[:200]}...")

            else:
                print(f"   Unexpected result type: {type(result)}")
                print(f"   Result: {str(result)[:200]}...")

        except Exception as e:
            print(f"❌ Error during retrieval: {e}")
            import traceback

            traceback.print_exc()

    # 6. Check if BaseRAGAgent has any output schema methods
    print("\n\n6. Checking BaseRAGAgent methods and attributes...")
    print(f"   Has 'output_schema': {'output_schema' in dir(base_rag)}")
    print(f"   Has 'get_output_schema': {'get_output_schema' in dir(base_rag)}")
    print(f"   Has 'schema': {'schema' in dir(base_rag)}")

    # Check retriever-specific attributes
    if hasattr(base_rag, "engine"):
        print("\n   Engine attributes:")
        engine_attrs = [
            attr for attr in dir(base_rag.engine) if not attr.startswith("_")
        ]
        for attr in ["k", "top_k", "similarity_threshold", "score_threshold"]:
            if attr in engine_attrs:
                print(f"      - {attr}: {getattr(base_rag.engine, attr, 'N/A')}")

    # 7. Try to understand the graph execution
    print("\n7. Understanding graph execution...")
    try:
        # Get the compiled graph
        compiled_graph = base_rag.graph
        print(f"   Compiled graph type: {type(compiled_graph)}")

        # Check state schema
        if hasattr(compiled_graph, "state_schema"):
            print(f"   State schema: {compiled_graph.state_schema}")

        # Check input/output schemas
        if hasattr(compiled_graph, "input_schema"):
            print(f"   Input schema: {compiled_graph.input_schema}")
        if hasattr(compiled_graph, "output_schema"):
            print(f"   Output schema: {compiled_graph.output_schema}")

    except Exception as e:
        print(f"   Error inspecting graph: {e}")


if __name__ == "__main__":
    asyncio.run(test_baserag_with_documents())
