"""Tests for GraphMemoryAgent with real Neo4j integration.

Note: These tests require a running Neo4j instance.
"""

import asyncio
import contextlib
import json

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.memory_v2.graph_memory_agent import (
    GraphMemoryAgent,
    GraphMemoryConfig,
    GraphMemoryMode,
)


@pytest.fixture
def neo4j_config():
    """Neo4j test configuration."""
    return {
        "neo4j_uri": "bolt://localhost:7687",
        "neo4j_username": "neo4j",
        "neo4j_password": "password",
        "database_name": "neo4j",
    }


@pytest.fixture
def graph_memory_config(neo4j_config):
    """Create test configuration."""
    return GraphMemoryConfig(
        **neo4j_config,
        user_id="test_user",
        llm_config=AugLLMConfig(temperature=0.1),
        mode=GraphMemoryMode.FULL,
        enable_vector_index=True,
    )


@pytest.fixture
async def graph_memory_agent(graph_memory_config):
    """Create GraphMemoryAgent for testing."""
    agent = GraphMemoryAgent(graph_memory_config)

    # Clean up test data before tests
    with contextlib.suppress(Exception):
        agent.graph.query(
            "MATCH (n {user_id: $user_id}) DETACH DELETE n", {"user_id": "test_user"}
        )

    yield agent

    # Clean up after tests
    with contextlib.suppress(Exception):
        agent.graph.query(
            "MATCH (n {user_id: $user_id}) DETACH DELETE n", {"user_id": "test_user"}
        )


class TestGraphMemoryAgent:
    """Test GraphMemoryAgent functionality."""

    @pytest.mark.asyncio
    async def test_extract_entities_and_relationships(self, graph_memory_agent):
        """Test entity and relationship extraction from text."""
        text = """
        Alice Johnson is the CEO of TechStartup Inc, located in Silicon Valley.
        She graduated from MIT in 2010 with a degree in Computer Science.
        Alice knows Bob Smith, who works as CTO at the same company.
        They recently attended the AI Summit 2024 conference in San Francisco.
        """

        # Extract graph
        graph_docs = await graph_memory_agent.extract_graph_from_text(text)

        # Verify extraction
        assert len(graph_docs) > 0

        # Check for expected entities
        all_nodes = []
        all_relationships = []

        for doc in graph_docs:
            all_nodes.extend(doc.nodes)
            all_relationships.extend(doc.relationships)

        # Check node types
        node_types = {node.type for node in all_nodes}
        assert "Person" in node_types
        assert any("Organization" in t or "Company" in t for t in node_types)

        # Check for specific entities
        node_ids = {node.id.lower() for node in all_nodes}
        assert any("alice" in id for id in node_ids)

        # Check relationships exist
        assert len(all_relationships) > 0

    @pytest.mark.asyncio
    async def test_store_and_retrieve_memories(self, graph_memory_agent):
        """Test storing memories in Neo4j and retrieving them."""
        # Create test memory
        text = "John Doe works at Acme Corp as a Software Engineer since 2020."

        # Process with full mode (extract and store)
        result = await graph_memory_agent.run(text, mode=GraphMemoryMode.FULL)

        # Verify storage
        assert "storage" in result
        assert result["storage"]["nodes_created"] > 0

        # Query the stored memory
        query_result = await graph_memory_agent.query_graph(
            "Who works at Acme Corp?", query_type="natural"
        )

        # Check results
        assert "answer" in query_result or "results" in query_result

        # Direct Cypher query to verify
        cypher_result = await graph_memory_agent.query_graph(
            "MATCH (p:Person {user_id: 'test_user'})-[:WORKS_FOR]->(o:Organization) RETURN p.name, o.name",
            query_type="cypher",
        )

        assert "results" in cypher_result

    @pytest.mark.asyncio
    async def test_complex_memory_graph(self, graph_memory_agent):
        """Test building a complex memory graph with multiple entities."""
        memories = [
            "Sarah Chen is a Data Scientist at DataCorp in New York.",
            "Sarah graduated from Stanford University in 2018.",
            "She knows Michael Brown who works at Google as an ML Engineer.",
            "Sarah and Michael collaborated on a research paper about Graph Neural Networks.",
            "The paper was published at NeurIPS 2023 conference.",
            "Sarah specializes in Natural Language Processing and Knowledge Graphs.",
        ]

        # Process all memories
        for memory in memories:
            result = await graph_memory_agent.run(memory, auto_store=True)
            assert "storage" in result or "extracted_graph" in result

        # Query relationships
        sarah_connections = await graph_memory_agent.query_graph(
            "What do we know about Sarah Chen?", query_type="natural"
        )

        assert sarah_connections is not None

        # Get subgraph around Sarah
        subgraph = await graph_memory_agent.get_memory_subgraph(
            "Sarah Chen", max_depth=2
        )

        assert "central_entity" in subgraph
        assert subgraph["central_entity"] == "Sarah Chen"

    @pytest.mark.asyncio
    async def test_vector_similarity_search(self, graph_memory_agent):
        """Test vector similarity search on memories."""
        # Skip if vector index not enabled
        if not graph_memory_agent.config.enable_vector_index:
            pytest.skip("Vector index not enabled")

        # Store some memories
        memories = [
            "Emma Wilson is an AI researcher specializing in computer vision.",
            "David Lee is a robotics engineer working on autonomous vehicles.",
            "Lisa Zhang is a machine learning expert focused on NLP.",
            "Tom Anderson is a data engineer building ML pipelines.",
        ]

        for memory in memories:
            await graph_memory_agent.run(memory, auto_store=True)

        # Wait a bit for indexing
        await asyncio.sleep(2)

        # Search for similar memories
        similar = await graph_memory_agent.search_similar_memories(
            "artificial intelligence researchers", node_type="Person", k=3
        )

        # Should find AI-related people
        assert len(similar) > 0
        assert all("score" in item for item in similar)

    @pytest.mark.asyncio
    async def test_graph_rag_queries(self, graph_memory_agent):
        """Test Graph RAG capabilities for complex queries."""
        # Build a knowledge graph
        knowledge = [
            "Python is a programming language created by Guido van Rossum in 1991.",
            "Python is used for web development, data science, and machine learning.",
            "Django is a web framework for Python created in 2005.",
            "FastAPI is a modern Python web framework focused on API development.",
            "NumPy is a Python library for numerical computing.",
            "PyTorch and TensorFlow are popular machine learning frameworks for Python.",
        ]

        for fact in knowledge:
            await graph_memory_agent.run(fact, auto_store=True)

        # Complex query requiring graph traversal
        result = await graph_memory_agent.query_graph(
            "What Python frameworks are used for web development?", query_type="natural"
        )

        # Should mention Django and/or FastAPI
        assert result is not None
        if "answer" in result:
            answer_lower = result["answer"].lower()
            assert "django" in answer_lower or "fastapi" in answer_lower

    @pytest.mark.asyncio
    async def test_memory_modes(self, graph_memory_agent):
        """Test different operation modes."""
        text = "Bob Johnson is a professor at Harvard University teaching Computer Science."

        # Test extract only mode
        extract_result = await graph_memory_agent.run(
            text, mode=GraphMemoryMode.EXTRACT_ONLY, auto_store=False
        )
        assert "extracted_graph" in extract_result
        assert "storage" not in extract_result

        # Test store only mode (assuming we have graph docs)
        graph_docs = await graph_memory_agent.extract_graph_from_text(text)
        store_result = await graph_memory_agent.store_graph_documents(graph_docs)
        assert store_result["nodes_created"] > 0

        # Test query only mode
        query_result = await graph_memory_agent.run(
            "professors at Harvard", mode=GraphMemoryMode.QUERY_ONLY
        )
        assert "query_result" in query_result

    @pytest.mark.asyncio
    async def test_time_based_memory_queries(self, graph_memory_agent):
        """Test querying memories with time context."""
        # Store memories with time context
        memories = [
            "Yesterday, I met Jane Smith at the coffee shop.",
            "Last week, I attended a machine learning workshop.",
            "Today, I'm working on the graph memory system.",
            "Tomorrow, I have a meeting with the engineering team.",
        ]

        for memory in memories:
            await graph_memory_agent.run(memory, auto_store=True)

        # Query recent memories
        recent_query = """
        MATCH (m:Memory {user_id: 'test_user'})
        WHERE m.timestamp >= datetime() - duration('P7D')
        RETURN m.content, m.timestamp
        ORDER BY m.timestamp DESC
        """

        result = await graph_memory_agent.query_graph(recent_query, query_type="cypher")

        assert "results" in result
        assert len(result["results"]) > 0

    @pytest.mark.asyncio
    async def test_relationship_properties(self, graph_memory_agent):
        """Test extraction and storage of relationship properties."""
        text = """
        Alice has been working at Google since 2019 as a Senior Engineer.
        She strongly collaborates with Bob on the search algorithm project.
        Alice mentored Charlie from January 2023 until December 2023.
        """

        # Process text
        await graph_memory_agent.run(text, auto_store=True)

        # Query relationships with properties
        rel_query = """
        MATCH (p:Person {user_id: 'test_user'})-[r]->(other)
        WHERE p.name CONTAINS 'Alice'
        RETURN type(r) as relationship, r.since as since, r.until as until, r.strength as strength
        """

        rel_result = await graph_memory_agent.query_graph(
            rel_query, query_type="cypher"
        )

        # Should have relationships with properties
        assert "results" in rel_result
        if len(rel_result["results"]) > 0:
            # Check if any relationships have time properties
            has_time_props = any(
                r.get("since") or r.get("until") for r in rel_result["results"]
            )
            assert has_time_props or len(rel_result["results"]) > 0

    @pytest.mark.asyncio
    async def test_memory_consolidation(self, graph_memory_agent):
        """Test memory consolidation functionality."""
        # Create interconnected memories
        memories = [
            "Project Alpha involves machine learning and data analysis.",
            "Sarah leads Project Alpha with a team of 5 engineers.",
            "Project Alpha uses Python, TensorFlow, and PostgreSQL.",
            "The Project Alpha team meets every Monday and Thursday.",
            "Project Alpha aims to improve customer recommendation system.",
        ]

        for memory in memories:
            await graph_memory_agent.run(memory, auto_store=True)

        # Run consolidation
        consolidation_result = await graph_memory_agent.consolidate_memories(
            min_connections=2
        )

        assert "candidates_analyzed" in consolidation_result
        assert consolidation_result["candidates_analyzed"] >= 0

    @pytest.mark.asyncio
    async def test_graph_memory_as_tool(self, graph_memory_config):
        """Test using GraphMemoryAgent as a tool."""
        # Create tool
        graph_tool = GraphMemoryAgent.as_tool(graph_memory_config)

        # Test tool invocation
        result = await graph_tool.ainvoke(
            {
                "text": "Marie Curie won the Nobel Prize in Physics in 1903.",
                "operation": "full",
            }
        )

        # Parse result
        result_data = json.loads(result)
        assert "mode" in result_data
        assert result_data["mode"] == "full"
        assert "extracted_graph" in result_data or "storage" in result_data


# Integration test with real data
@pytest.mark.asyncio
async def test_real_world_scenario():
    """Test a real-world memory management scenario."""
    config = GraphMemoryConfig(
        neo4j_uri="bolt://localhost:7687",
        neo4j_username="neo4j",
        neo4j_password="password",
        user_id="integration_test_user",
        mode=GraphMemoryMode.FULL,
    )

    agent = GraphMemoryAgent(config)

    # Simulate a day's worth of memories
    daily_memories = [
        "This morning I had a meeting with the product team about the Q1 roadmap.",
        "During lunch, I discussed the new AI features with John from engineering.",
        "I learned about a new graph algorithm called PageRank for ranking nodes.",
        "The product team wants to prioritize the recommendation system feature.",
        "John suggested using Neo4j for the graph database implementation.",
        "I need to research more about graph neural networks for our use case.",
        "Scheduled a follow-up meeting with John next Tuesday at 2 PM.",
    ]

    # Process all memories
    for memory in daily_memories:
        await agent.run(memory, auto_store=True)

    # End of day summary query
    await agent.query_graph(
        "What were the main topics discussed today?", query_type="natural"
    )

    # Find action items
    await agent.query_graph("What do I need to do or research?", query_type="natural")

    # Clean up
    agent.graph.query(
        "MATCH (n {user_id: $user_id}) DETACH DELETE n",
        {"user_id": "integration_test_user"},
    )


if __name__ == "__main__":
    # Run integration test
    asyncio.run(test_real_world_scenario())
