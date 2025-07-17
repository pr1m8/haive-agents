#!/usr/bin/env python3
"""Test HyDE RAG with clean MultiAgent implementation."""

import pytest
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.documents import Document

from haive.agents.rag.hyde.agent import HyDERAGAgent


def test_hyde_rag_structure():
    """Test HyDE RAG structure without execution."""

    # Create test documents
    documents = [
        Document(
            page_content="Python is a high-level programming language known for its simplicity and readability.",
            metadata={"source": "doc1"},
        ),
        Document(
            page_content="Machine learning is a subset of artificial intelligence that focuses on algorithms that improve through experience.",
            metadata={"source": "doc2"},
        ),
        Document(
            page_content="FastAPI is a modern, fast web framework for building APIs with Python based on standard Python type hints.",
            metadata={"source": "doc3"},
        ),
    ]

    # Create HyDE RAG agent using clean MultiAgent
    hyde_agent = HyDERAGAgent.from_documents(documents=documents, name="test_hyde_rag")

    # Verify agent creation
    assert hyde_agent.name == "test_hyde_rag"
    assert isinstance(hyde_agent, HyDERAGAgent)
    assert list(hyde_agent.agents.keys()) == [
        "hyde_generator",
        "hyde_retriever",
        "hyde_answer_generator",
    ]
    assert hyde_agent.execution_mode == "sequential"

    # Verify agent components
    assert "hyde_generator" in hyde_agent.agents
    assert "hyde_retriever" in hyde_agent.agents
    assert "hyde_answer_generator" in hyde_agent.agents


@pytest.mark.asyncio
async def test_hyde_rag_agent_structure():
    """Test HyDE RAG agent structure and components."""

    # Create minimal documents
    documents = [Document(page_content="Test content", metadata={"source": "test"})]

    # Create agent
    agent = HyDERAGAgent.from_documents(documents=documents)

    # Verify structure
    assert hasattr(agent, "agents")
    assert hasattr(agent, "execution_mode")
    assert len(agent.agents) == 3

    # Verify agent names
    expected_agents = ["hyde_generator", "hyde_retriever", "hyde_answer_generator"]
    assert all(agent_name in agent.agents for agent_name in expected_agents)

    # Verify execution mode
    assert agent.execution_mode == "sequential"


if __name__ == "__main__":
    import asyncio

    async def run_tests():
        test_hyde_rag_structure()
        await test_hyde_rag_agent_structure()
        print("✅ All HyDE RAG tests passed!")

    asyncio.run(run_tests())
