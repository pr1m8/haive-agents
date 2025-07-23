"""Test to demonstrate document passing between agents in SimpleRAG V3."""

import asyncio
from typing import Any, Dict, List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.documents import Document

from haive.agents.rag.simple.enhanced_v3.answer_generator_agent import SimpleAnswerAgent
from haive.agents.rag.simple.enhanced_v3.retriever_agent import RetrieverAgent


async def demonstrate_document_passing():
    """Demonstrate how documents flow from RetrieverAgent to SimpleAnswerAgent."""
    print("\n=== Document Passing in SimpleRAG V3 ===\n")

    # 1. Create mock retrieval result (simulating RetrieverAgent output)
    print("1. RetrieverAgent Output Format:")
    print("-" * 50)

    # This is what RetrieverAgent returns
    retriever_output = {
        "query": "What is machine learning?",
        "documents": [
            {
                "page_content": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.",
                "metadata": {"source": "AI Basics Guide", "page": 1},
            },
            {
                "page_content": "ML algorithms build mathematical models based on training data to make predictions or decisions without being explicitly programmed to perform the task.",
                "metadata": {"source": "ML Handbook", "page": 5},
            },
            {
                "page_content": "Deep learning is a specialized form of machine learning that uses neural networks with multiple layers.",
                "metadata": {"source": "Deep Learning Guide", "page": 2},
            },
        ],
        "metadata": {
            "retrieval_method": "similarity_search",
            "score_threshold": 0.5,
            "num_documents": 3,
            "search_time": 0.123,
        },
    }

    print(f"Query: {retriever_output['query']}")
    print(f"Retrieved {len(retriever_output['documents'])} documents")
    print(f"Metadata: {retriever_output['metadata']}")

    # 2. Show how SimpleAnswerAgent processes this input
    print("\n2. SimpleAnswerAgent Input Processing:")
    print("-" * 50)

    # Create SimpleAnswerAgent
    answer_agent = SimpleAnswerAgent(
        name="answer_generator",
        engine=AugLLMConfig(temperature=0.7),
        max_context_length=4000,
        include_citations=True,
        citation_style="inline",
    )

    # Show what happens in _parse_retriever_input
    print("SimpleAnswerAgent._parse_retriever_input() extracts:")
    print(f"  - query: '{retriever_output['query']}'")
    print(
        f"  - documents: List of {len(retriever_output['documents'])} Document objects"
    )
    print(f"  - metadata: {retriever_output['metadata']}")

    # 3. Show document context building
    print("\n3. Document Context Building:")
    print("-" * 50)

    # Convert dicts to Document objects (normally done by RetrieverAgent)
    documents = [
        Document(page_content=doc["page_content"], metadata=doc["metadata"])
        for doc in retriever_output["documents"]
    ]

    # Build context (this happens inside SimpleAnswerAgent)
    context_info = answer_agent._build_context_from_documents(
        documents=documents, query=retriever_output["query"], debug=True
    )

    print(f"\nBuilt context:")
    print(f"  - Total length: {context_info['total_length']} chars")
    print(f"  - Documents used: {context_info['document_count']}")
    print(f"  - Sources: {context_info['sources']}")
    print(f"\nFormatted context preview:")
    print(context_info["formatted_context"][:500] + "...")

    # 4. Show the final prompt
    print("\n4. Final Prompt to LLM:")
    print("-" * 50)

    formatted_prompt = answer_agent._format_prompt_with_context(
        query=retriever_output["query"], context_info=context_info, debug=True
    )

    print(formatted_prompt[:500] + "...")

    # 5. Sequential flow in SimpleRAG V3
    print("\n5. Complete Sequential Flow in SimpleRAG V3:")
    print("-" * 50)
    print("User Query")
    print("    ↓")
    print("RetrieverAgent")
    print("    ├─ Searches vector store")
    print("    ├─ Returns: {")
    print("    │     'query': original_query,")
    print("    │     'documents': [Document, ...],  # Retrieved docs")
    print("    │     'metadata': {...}")
    print("    │   }")
    print("    ↓")
    print("SimpleAnswerAgent")
    print("    ├─ Receives RetrieverAgent output")
    print("    ├─ Extracts documents from input")
    print("    ├─ Builds context from documents")
    print("    ├─ Formats prompt with context")
    print("    ├─ Generates answer using LLM")
    print("    └─ Returns final answer with citations")

    # 6. Key points about document passing
    print("\n6. Key Points About Document Passing:")
    print("-" * 50)
    print("✓ Documents are passed as part of a structured dict")
    print("✓ SimpleAnswerAgent expects 'documents' key in input")
    print("✓ Documents maintain metadata throughout the pipeline")
    print("✓ Citation tracking preserves document sources")
    print("✓ Context building respects max_context_length")
    print("✓ The 'retrieved_documents' become 'documents' in the flow")


if __name__ == "__main__":
    asyncio.run(demonstrate_document_passing())
