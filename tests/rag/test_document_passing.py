"""Test to demonstrate document passing between agents in SimpleRAG V3."""

import asyncio

from langchain_core.documents import Document

from haive.agents.rag.simple.enhanced_v3.answer_generator_agent import SimpleAnswerAgent
from haive.core.engine.aug_llm import AugLLMConfig


async def demonstrate_document_passing():
    """Demonstrate how documents flow from RetrieverAgent to SimpleAnswerAgent."""
    # 1. Create mock retrieval result (simulating RetrieverAgent output)

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

    # 2. Show how SimpleAnswerAgent processes this input

    # Create SimpleAnswerAgent
    answer_agent = SimpleAnswerAgent(
        name="answer_generator",
        engine=AugLLMConfig(temperature=0.7),
        max_context_length=4000,
        include_citations=True,
        citation_style="inline",
    )

    # Show what happens in _parse_retriever_input

    # 3. Show document context building

    # Convert dicts to Document objects (normally done by RetrieverAgent)
    documents = [
        Document(page_content=doc["page_content"], metadata=doc["metadata"])
        for doc in retriever_output["documents"]
    ]

    # Build context (this happens inside SimpleAnswerAgent)
    context_info = answer_agent._build_context_from_documents(
        documents=documents, query=retriever_output["query"], debug=True
    )

    # 4. Show the final prompt

    answer_agent._format_prompt_with_context(
        query=retriever_output["query"], context_info=context_info, debug=True
    )

    # 5. Sequential flow in SimpleRAG V3

    # 6. Key points about document passing


if __name__ == "__main__":
    asyncio.run(demonstrate_document_passing())
