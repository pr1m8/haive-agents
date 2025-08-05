#!/usr/bin/env python3
"""Test Simple RAG with clean MultiAgent implementation."""

from langchain_core.documents import Document
import pytest

from haive.agents.rag.simple.agent import SimpleRAGAgent


def test_simple_rag_structure():
    """Test Simple RAG structure without execution."""
    # Create test documents
    documents = [
        Document(
            page_content="Haive is an AI agent framework built for composable, flexible agent systems.",
            metadata={"source": "doc1"},
        ),
        Document(
            page_content="MultiAgent systems in Haive allow coordination of multiple agents with intelligent routing.",
            metadata={"source": "doc2"},
        ),
        Document(
            page_content="RAG (Retrieval-Augmented Generation) combines document retrieval with language generation.",
            metadata={"source": "doc3"},
        ),
    ]

    # Create Simple RAG agent using clean MultiAgent
    simple_rag_agent = SimpleRAGAgent.from_documents(documents=documents, name="test_simple_rag")

    # Verify agent creation
    assert simple_rag_agent.name == "test_simple_rag"
    assert isinstance(simple_rag_agent, SimpleRAGAgent)
    assert list(simple_rag_agent.agents.keys()) == ["retriever", "answer_generator"]
    assert simple_rag_agent.execution_mode == "sequential"

    # Verify agent components
    assert "retriever" in simple_rag_agent.agents
    assert "answer_generator" in simple_rag_agent.agents


@pytest.mark.asyncio
async def test_simple_rag_agent_structure():
    """Test Simple RAG agent structure and components."""
    # Create minimal documents
    documents = [Document(page_content="Test content", metadata={"source": "test"})]

    # Create agent
    agent = SimpleRAGAgent.from_documents(documents=documents)

    # Verify structure
    assert hasattr(agent, "agents")
    assert hasattr(agent, "execution_mode")
    assert len(agent.agents) == 2

    # Verify agent names
    expected_agents = ["retriever", "answer_generator"]
    assert all(agent_name in agent.agents for agent_name in expected_agents)

    # Verify execution mode
    assert agent.execution_mode == "sequential"


@pytest.mark.asyncio
async def test_simple_rag_custom_name():
    """Test Simple RAG with custom agent name."""
    documents = [Document(page_content="Test content", metadata={"source": "test"})]

    # Create agent with custom name
    custom_name = "my_custom_rag"
    agent = SimpleRAGAgent.from_documents(documents=documents, name=custom_name)

    # Verify custom name
    assert agent.name == custom_name


if __name__ == "__main__":
    import asyncio

    async def run_tests():
        test_simple_rag_structure()
        await test_simple_rag_agent_structure()
        await test_simple_rag_custom_name()

    asyncio.run(run_tests())
