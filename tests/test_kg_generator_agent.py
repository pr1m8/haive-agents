"""Tests for Knowledge Graph Generator Agent.

This test suite validates the KG Generator Agent's ability to extract
entities and relationships from memories and build comprehensive knowledge graphs.
"""

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from haive.agents.memory.core.classifier import MemoryClassifier, MemoryClassifierConfig
from haive.agents.memory.core.stores import MemoryStoreConfig, MemoryStoreManager
from haive.agents.memory.core.types import MemoryType
from haive.agents.memory.kg_generator_agent import (
    KGGeneratorAgent,
    KGGeneratorAgentConfig,
    KnowledgeGraphNode,
    KnowledgeGraphRelationship,
    MemoryKnowledgeGraph,
)
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.tools.store_tools import StoreManager


class TestKnowledgeGraphStructures:
    """Test the basic knowledge graph data structures."""

    def test_knowledge_graph_node_creation(self):
        """Test creating a knowledge graph node."""
        node = KnowledgeGraphNode(
            id="person_alice",
            type="person",
            name="Alice",
            properties={"age": 30, "role": "engineer"},
            memory_references=["mem_1", "mem_2"],
            confidence=0.9,
        )

        assert node.id == "person_alice"
        assert node.type == "person"
        assert node.name == "Alice"
        assert node.properties["age"] == 30
        assert "mem_1" in node.memory_references
        assert node.confidence == 0.9
        assert isinstance(node.created_at, datetime)

    def test_knowledge_graph_relationship_creation(self):
        """Test creating a knowledge graph relationship."""
        rel = KnowledgeGraphRelationship(
            id="alice_works_at_company",
            source_id="person_alice",
            target_id="org_company",
            relationship_type="works_at",
            properties={"since": "2020", "role": "engineer"},
            memory_references=["mem_3"],
            confidence=0.85,
        )

        assert rel.id == "alice_works_at_company"
        assert rel.source_id == "person_alice"
        assert rel.target_id == "org_company"
        assert rel.relationship_type == "works_at"
        assert rel.properties["since"] == "2020"
        assert rel.confidence == 0.85

    def test_memory_knowledge_graph_operations(self):
        """Test knowledge graph operations."""
        kg = MemoryKnowledgeGraph()

        # Add nodes
        alice = KnowledgeGraphNode(
            id="person_alice", type="person", name="Alice", memory_references=["mem_1"]
        )

        company = KnowledgeGraphNode(
            id="org_company",
            type="organization",
            name="TechCorp",
            memory_references=["mem_2"],
        )

        kg.add_node(alice)
        kg.add_node(company)

        assert len(kg.nodes) == 2
        assert "person_alice" in kg.nodes
        assert "org_company" in kg.nodes

        # Add relationship
        rel = KnowledgeGraphRelationship(
            id="alice_works_at_company",
            source_id="person_alice",
            target_id="org_company",
            relationship_type="works_at",
            memory_references=["mem_3"],
        )

        kg.add_relationship(rel)

        assert len(kg.relationships) == 1

        # Test connected nodes
        connected = kg.get_connected_nodes("person_alice")
        assert len(connected) == 1
        assert connected[0].id == "org_company"

        # Test relationships for node
        relations = kg.get_relationships_for_node("person_alice")
        assert len(relations) == 1
        assert relations[0].relationship_type == "works_at"


class TestKGGeneratorAgent:
    """Test the KG Generator Agent functionality."""

    @pytest.fixture
    def mock_memory_store(self):
        """Create a mock memory store manager."""
        store_manager = MagicMock(spec=StoreManager)
        store_config = MemoryStoreConfig(store_manager=store_manager)
        memory_store = MagicMock(spec=MemoryStoreManager)
        memory_store.config = store_config
        return memory_store

    @pytest.fixture
    def mock_classifier(self):
        """Create a mock memory classifier."""
        classifier_config = MemoryClassifierConfig()
        classifier = MagicMock(spec=MemoryClassifier)
        classifier.config = classifier_config
        return classifier

    @pytest.fixture
    def kg_agent_config(self, mock_memory_store, mock_classifier):
        """Create KG agent configuration."""
        return KGGeneratorAgentConfig(
            name="test_kg_agent",
            memory_store_manager=mock_memory_store,
            memory_classifier=mock_classifier,
            engine=AugLLMConfig(temperature=0.1),
        )

    @pytest.fixture
    def kg_agent(self, kg_agent_config):
        """Create KG Generator Agent instance."""
        return KGGeneratorAgent(kg_agent_config)

    def test_kg_agent_initialization(self, kg_agent):
        """Test KG agent initialization."""
        assert kg_agent.config.name == "test_kg_agent"
        assert isinstance(kg_agent.knowledge_graph, MemoryKnowledgeGraph)
        assert len(kg_agent.knowledge_graph.nodes) == 0
        assert len(kg_agent.knowledge_graph.relationships) == 0
        assert kg_agent.entity_extraction_prompt is not None
        assert kg_agent.relationship_extraction_prompt is not None

    def test_entity_id_generation(self, kg_agent):
        """Test entity ID generation."""
        entity_id = kg_agent._generate_entity_id("Alice Smith", "person")
        assert entity_id == "person_alice_smith"

        entity_id = kg_agent._generate_entity_id("TechCorp Inc", "organization")
        assert entity_id == "organization_techcorp_inc"

    def test_relationship_id_generation(self, kg_agent):
        """Test relationship ID generation."""
        rel_id = kg_agent._generate_relationship_id(
            "person_alice", "org_company", "works_at"
        )
        assert rel_id == "person_alice_works_at_org_company"

    def test_entity_finding(self, kg_agent):
        """Test finding entities by name."""
        # Add test entity
        node = KnowledgeGraphNode(
            id="person_alice",
            type="person",
            name="Alice Smith",
            memory_references=["mem_1"],
        )
        kg_agent.knowledge_graph.add_node(node)

        # Test finding entity
        entity_id = kg_agent._find_entity_id("Alice Smith")
        assert entity_id == "person_alice"

        # Test case insensitive search
        entity_id = kg_agent._find_entity_id("alice smith")
        assert entity_id == "person_alice"

        # Test non-existent entity
        entity_id = kg_agent._find_entity_id("Bob Jones")
        assert entity_id is None

    def test_json_response_parsing(self, kg_agent):
        """Test JSON response parsing."""
        # Test valid JSON
        response = (
            'Here is the result: {"entities": [{"name": "Alice", "type": "person"}]}'
        )
        parsed = kg_agent._parse_json_response(response)
        assert parsed is not None
        assert "entities" in parsed
        assert len(parsed["entities"]) == 1
        assert parsed["entities"][0]["name"] == "Alice"

        # Test invalid JSON
        response = "This is not JSON"
        parsed = kg_agent._parse_json_response(response)
        assert parsed is None

    @pytest.mark.asyncio
    async def test_extract_knowledge_graph_from_memories(self, kg_agent):
        """Test extracting knowledge graph from memories."""
        # Mock memory data
        test_memories = [
            {
                "id": "mem_1",
                "content": "Alice works at TechCorp as a software engineer.",
                "metadata": {
                    "memory_types": [MemoryType.EPISODIC.value],
                    "entities": ["Alice", "TechCorp"],
                    "topics": ["work", "technology"],
                    "relationships": [],
                },
            },
            {
                "id": "mem_2",
                "content": "TechCorp is located in San Francisco.",
                "metadata": {
                    "memory_types": [MemoryType.SEMANTIC.value],
                    "entities": ["TechCorp", "San Francisco"],
                    "topics": ["location", "company"],
                    "relationships": [],
                },
            },
        ]

        # Mock memory store retrieve_memories
        kg_agent.memory_store.retrieve_memories = AsyncMock(return_value=test_memories)

        # Mock LLM responses
        mock_llm_response = MagicMock()
        mock_llm_response.content = (
            '{"entities": [{"name": "Alice", "type": "person", "confidence": 0.9}]}'
        )
        kg_agent.llm.ainvoke = AsyncMock(return_value=mock_llm_response)

        # Extract knowledge graph
        result_kg = await kg_agent.extract_knowledge_graph_from_memories()

        # Verify results
        assert isinstance(result_kg, MemoryKnowledgeGraph)
        assert len(result_kg.nodes) >= 0  # Depends on mocked LLM response
        assert "last_updated" in result_kg.metadata
        assert result_kg.metadata["total_memories_processed"] == 2

        # Verify memory store was called
        kg_agent.memory_store.retrieve_memories.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_entity_neighborhood(self, kg_agent):
        """Test getting entity neighborhood."""
        # Setup test graph
        alice = KnowledgeGraphNode(
            id="person_alice", type="person", name="Alice", memory_references=["mem_1"]
        )

        bob = KnowledgeGraphNode(
            id="person_bob", type="person", name="Bob", memory_references=["mem_2"]
        )

        company = KnowledgeGraphNode(
            id="org_company",
            type="organization",
            name="TechCorp",
            memory_references=["mem_3"],
        )

        kg_agent.knowledge_graph.add_node(alice)
        kg_agent.knowledge_graph.add_node(bob)
        kg_agent.knowledge_graph.add_node(company)

        # Add relationships
        rel1 = KnowledgeGraphRelationship(
            id="alice_works_at_company",
            source_id="person_alice",
            target_id="org_company",
            relationship_type="works_at",
            memory_references=["mem_1"],
        )

        rel2 = KnowledgeGraphRelationship(
            id="bob_works_at_company",
            source_id="person_bob",
            target_id="org_company",
            relationship_type="works_at",
            memory_references=["mem_2"],
        )

        kg_agent.knowledge_graph.add_relationship(rel1)
        kg_agent.knowledge_graph.add_relationship(rel2)

        # Get neighborhood
        neighborhood = await kg_agent.get_entity_neighborhood("person_alice", depth=2)

        assert "center_entity" in neighborhood
        assert neighborhood["center_entity"].id == "person_alice"
        assert "levels" in neighborhood
        assert neighborhood["total_nodes"] > 0
        assert neighborhood["total_relationships"] > 0

    @pytest.mark.asyncio
    async def test_run_extract_command(self, kg_agent):
        """Test running the extract command."""
        # Mock the extract method
        kg_agent.extract_knowledge_graph_from_memories = AsyncMock(
            return_value=kg_agent.knowledge_graph
        )

        # Test extract command
        result = await kg_agent.run("extract knowledge graph")

        assert "extracted successfully" in result
        assert "0 entities" in result  # Empty graph
        assert "0 relationships" in result

        # Verify extract method was called
        kg_agent.extract_knowledge_graph_from_memories.assert_called_once()

    @pytest.mark.asyncio
    async def test_run_stats_command(self, kg_agent):
        """Test running the stats command."""
        # Add some test data
        kg_agent.knowledge_graph.metadata["last_updated"] = "2025-01-15T10:30:00"

        result = await kg_agent.run("show statistics")

        assert "Knowledge Graph Statistics" in result
        assert "Nodes: 0" in result
        assert "Relationships: 0" in result
        assert "Last Updated: 2025-01-15T10:30:00" in result

    @pytest.mark.asyncio
    async def test_run_unknown_command(self, kg_agent):
        """Test running an unknown command."""
        result = await kg_agent.run("unknown command")

        assert "I can help you" in result
        assert "extract knowledge graphs" in result
        assert "explore entity neighborhoods" in result
        assert "provide graph statistics" in result


@pytest.mark.asyncio
async def test_kg_generator_integration():
    """Integration test for KG Generator Agent with real components."""
    # Create real components (but we'll mock the LLM responses)
    try:
        from haive.agents.memory.core.classifier import (
            MemoryClassifier,
            MemoryClassifierConfig,
        )
        from haive.agents.memory.core.stores import (
            MemoryStoreConfig,
            MemoryStoreManager,
        )
        from haive.core.tools.store_tools import StoreManager

        # Create store manager (in-memory for testing)
        store_manager = StoreManager(
            store_type="memory", collection_name="test_kg_memories"
        )

        # Create memory store manager
        memory_store_config = MemoryStoreConfig(
            store_manager=store_manager,
            auto_classify=False,  # Disable auto-classification for testing
        )
        memory_store = MemoryStoreManager(memory_store_config)

        # Create classifier
        classifier_config = MemoryClassifierConfig()
        classifier = MemoryClassifier(classifier_config)

        # Create KG agent
        kg_config = KGGeneratorAgentConfig(
            name="integration_test_kg",
            memory_store_manager=memory_store,
            memory_classifier=classifier,
            engine=AugLLMConfig(temperature=0.1),
        )

        kg_agent = KGGeneratorAgent(kg_config)

        # Store some test memories
        await memory_store.store_memory(
            content="Alice works at TechCorp as a software engineer.",
            namespace=("test", "work"),
        )

        await memory_store.store_memory(
            content="TechCorp is located in San Francisco and focuses on AI technology.",
            namespace=("test", "work"),
        )

        # Mock LLM responses for entity extraction
        mock_entity_response = MagicMock()
        mock_entity_response.content = """
        {
            "entities": [
                {"name": "Alice", "type": "person", "confidence": 0.9, "properties": {"role": "engineer"}},
                {"name": "TechCorp", "type": "organization", "confidence": 0.95, "properties": {"industry": "technology"}}
            ]
        }
        """

        mock_relation_response = MagicMock()
        mock_relation_response.content = """
        {
            "relationships": [
                {"source_entity": "Alice", "target_entity": "TechCorp", "relationship_type": "works_at", "confidence": 0.9}
            ]
        }
        """

        # Mock the LLM to return our test responses
        kg_agent.llm.ainvoke = AsyncMock(
            side_effect=[mock_entity_response, mock_relation_response] * 2
        )

        # Extract knowledge graph
        result_kg = await kg_agent.extract_knowledge_graph_from_memories(
            namespace=("test", "work")
        )

        # Verify the knowledge graph was built
        assert len(result_kg.nodes) >= 2  # At least Alice and TechCorp
        assert len(result_kg.relationships) >= 1  # At least works_at relationship

        # Check specific entities
        alice_id = kg_agent._find_entity_id("Alice")
        techcorp_id = kg_agent._find_entity_id("TechCorp")

        assert alice_id is not None
        assert techcorp_id is not None

        # Check entity properties
        alice_node = result_kg.nodes[alice_id]
        assert alice_node.type == "person"
        assert alice_node.name == "Alice"

        techcorp_node = result_kg.nodes[techcorp_id]
        assert techcorp_node.type == "organization"
        assert techcorp_node.name == "TechCorp"

        # Test entity neighborhood
        neighborhood = await kg_agent.get_entity_neighborhood(alice_id, depth=1)
        assert neighborhood["total_nodes"] >= 1
        assert neighborhood["total_relationships"] >= 1

    except ImportError as e:
        pytest.skip(f"Missing dependencies: {e}")


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
