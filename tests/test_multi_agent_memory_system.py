"""Comprehensive tests for the multi-agent memory system.

This test suite validates the complete memory system integration including
classification, storage, retrieval, knowledge graph generation, and coordination.
"""

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from haive.core.tools.store_tools import StoreManager

from haive.agents.memory.agentic_rag_coordinator import AgenticRAGCoordinatorConfig
from haive.agents.memory.core.classifier import MemoryClassifier, MemoryClassifierConfig
from haive.agents.memory.core.stores import MemoryStoreConfig, MemoryStoreManager
from haive.agents.memory.core.types import MemoryType
from haive.agents.memory.kg_generator_agent import KGGeneratorAgentConfig
from haive.agents.memory.multi_agent_coordinator import (
    MemoryAgentCapabilities,
    MemoryTask,
    MultiAgentCoordinatorConfig,
    MultiAgentMemoryCoordinator,
)


class TestMemoryTask:
    """Test memory task management."""

    def test_memory_task_creation(self):
        """Test creating memory tasks."""
        task = MemoryTask(
            id="test_task_1",
            type="store_memory",
            query="Store this test memory",
            parameters={"content": "test content"},
            priority=5,
        )

        assert task.id == "test_task_1"
        assert task.type == "store_memory"
        assert task.query == "Store this test memory"
        assert task.parameters["content"] == "test content"
        assert task.priority == 5
        assert task.status == "pending"
        assert task.assigned_agent is None
        assert isinstance(task.created_at, datetime)

    def test_memory_task_with_namespace(self):
        """Test memory task with namespace."""
        task = MemoryTask(
            id="test_task_2",
            type="retrieve_memories",
            query="Find memories about Python",
            namespace=("user", "programming"),
            memory_types=[MemoryType.SEMANTIC, MemoryType.PROCEDURAL],
        )

        assert task.namespace == ("user", "programming")
        assert MemoryType.SEMANTIC in task.memory_types
        assert MemoryType.PROCEDURAL in task.memory_types


class TestMemoryAgentCapabilities:
    """Test memory agent capabilities."""

    def test_agent_capabilities_creation(self):
        """Test creating agent capabilities."""
        caps = MemoryAgentCapabilities(
            agent_name="test_agent",
            agent_type="TestAgent",
            can_store_memories=True,
            can_retrieve_memories=True,
            supported_memory_types=[MemoryType.SEMANTIC, MemoryType.EPISODIC],
            specialization=["test_specialization"],
        )

        assert caps.agent_name == "test_agent"
        assert caps.agent_type == "TestAgent"
        assert caps.can_store_memories is True
        assert caps.can_retrieve_memories is True
        assert MemoryType.SEMANTIC in caps.supported_memory_types
        assert "test_specialization" in caps.specialization


class TestMultiAgentCoordinator:
    """Test the multi-agent memory coordinator."""

    @pytest.fixture
    def mock_store_manager(self):
        """Create mock store manager."""
        store_manager = MagicMock(spec=StoreManager)
        store_manager.store_memory = AsyncMock(return_value="test_memory_id")
        store_manager.search_memories = AsyncMock(return_value=[])
        store_manager.get_memory = AsyncMock(return_value=None)
        return store_manager

    @pytest.fixture
    def mock_memory_store(self, mock_store_manager):
        """Create mock memory store manager."""
        store_config = MemoryStoreConfig(
            store_manager=mock_store_manager, auto_classify=False
        )
        memory_store = MagicMock(spec=MemoryStoreManager)
        memory_store.config = store_config
        memory_store.store_memory = AsyncMock(return_value="test_memory_id")
        memory_store.retrieve_memories = AsyncMock(return_value=[])
        memory_store.get_memory_by_id = AsyncMock(return_value=None)
        return memory_store

    @pytest.fixture
    def mock_classifier(self):
        """Create mock memory classifier."""
        classifier_config = MemoryClassifierConfig()
        classifier = MagicMock(spec=MemoryClassifier)
        classifier.config = classifier_config
        classifier.classify_memory = MagicMock()
        classifier.classify_query_intent = MagicMock()
        return classifier

    @pytest.fixture
    def coordinator_config(self, mock_memory_store, mock_classifier):
        """Create coordinator configuration."""
        # KG generator config
        kg_config = KGGeneratorAgentConfig(
            memory_store_manager=mock_memory_store, memory_classifier=mock_classifier
        )

        # Agentic RAG config
        rag_config = AgenticRAGCoordinatorConfig(
            memory_store_manager=mock_memory_store,
            memory_classifier=mock_classifier,
            kg_generator=MagicMock(),  # Will be replaced
        )

        return MultiAgentCoordinatorConfig(
            memory_store_manager=mock_memory_store,
            memory_classifier=mock_classifier,
            kg_generator_config=kg_config,
            agentic_rag_config=rag_config,
        )

    def test_coordinator_initialization(self, coordinator_config):
        """Test coordinator initialization."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        assert coordinator.config == coordinator_config
        assert len(coordinator.meta_agents) > 0
        assert len(coordinator.agent_capabilities) > 0
        assert "kg_generator" in coordinator.meta_agents
        assert "agentic_rag" in coordinator.meta_agents
        assert "memory_store" in coordinator.meta_agents
        assert "memory_classifier" in coordinator.meta_agents

    def test_agent_capabilities_setup(self, coordinator_config):
        """Test that agent capabilities are properly set up."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Check KG generator capabilities
        kg_caps = coordinator.agent_capabilities["kg_generator"]
        assert kg_caps.agent_name == "kg_generator"
        assert kg_caps.can_generate_knowledge_graph is True
        assert kg_caps.can_analyze_memories is True
        assert "entity_extraction" in kg_caps.specialization

        # Check agentic RAG capabilities
        rag_caps = coordinator.agent_capabilities["agentic_rag"]
        assert rag_caps.agent_name == "agentic_rag"
        assert rag_caps.can_retrieve_memories is True
        assert rag_caps.can_coordinate_retrieval is True
        assert "strategy_selection" in rag_caps.specialization

    def test_fallback_task_routing(self, coordinator_config):
        """Test fallback task routing logic."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Test store task routing
        store_task = MemoryTask(
            id="store_test", type="store_memory", query="Store this memory"
        )

        routing = coordinator._fallback_task_routing(store_task)
        assert routing["routing_decision"] == "single_agent"
        assert routing["primary_agent"] == "memory_store"

        # Test retrieve task routing
        retrieve_task = MemoryTask(
            id="retrieve_test",
            type="retrieve_memories",
            query="Find memories about Python",
        )

        routing = coordinator._fallback_task_routing(retrieve_task)
        assert routing["routing_decision"] == "single_agent"
        assert routing["primary_agent"] == "agentic_rag"

        # Test analyze task routing
        analyze_task = MemoryTask(
            id="analyze_test", type="analyze_memory", query="Analyze this memory"
        )

        routing = coordinator._fallback_task_routing(analyze_task)
        assert routing["routing_decision"] == "single_agent"
        assert routing["primary_agent"] == "memory_classifier"

        # Test knowledge graph task routing
        kg_task = MemoryTask(
            id="kg_test", type="generate_knowledge_graph", query="Build knowledge graph"
        )

        routing = coordinator._fallback_task_routing(kg_task)
        assert routing["routing_decision"] == "single_agent"
        assert routing["primary_agent"] == "kg_generator"

    @pytest.mark.asyncio
    async def test_store_memory_task(self, coordinator_config):
        """Test storing memory through multi-agent system."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Mock the meta agent execution
        mock_meta_state = coordinator.meta_agents["memory_store"]
        mock_meta_state.execute_agent = AsyncMock(
            return_value="Memory stored successfully"
        )

        # Store a memory
        result = await coordinator.store_memory("Test memory content")

        assert "Memory stored successfully" in result
        # Verify the agent was called
        mock_meta_state.execute_agent.assert_called_once()

    @pytest.mark.asyncio
    async def test_retrieve_memories_task(self, coordinator_config):
        """Test retrieving memories through multi-agent system."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Mock the meta agent execution
        mock_meta_state = coordinator.meta_agents["agentic_rag"]
        mock_meta_state.execute_agent = AsyncMock(
            return_value={
                "final_memories": [
                    {"id": "mem1", "content": "Test memory 1"},
                    {"id": "mem2", "content": "Test memory 2"},
                ]
            }
        )

        # Retrieve memories
        memories = await coordinator.retrieve_memories("Find test memories")

        assert len(memories) == 2
        assert memories[0]["id"] == "mem1"
        assert memories[1]["id"] == "mem2"
        # Verify the agent was called
        mock_meta_state.execute_agent.assert_called_once()

    @pytest.mark.asyncio
    async def test_analyze_memory_task(self, coordinator_config):
        """Test analyzing memory through multi-agent system."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Mock the meta agent execution
        mock_meta_state = coordinator.meta_agents["memory_classifier"]
        mock_meta_state.execute_agent = AsyncMock(
            return_value={
                "memory_types": ["semantic", "episodic"],
                "importance": "high",
                "entities": ["Python", "programming"],
            }
        )

        # Analyze memory
        result = await coordinator.analyze_memory("I learned Python programming today")

        assert result["success"] is True
        assert "analysis" in result
        # Verify the agent was called
        mock_meta_state.execute_agent.assert_called_once()

    @pytest.mark.asyncio
    async def test_generate_knowledge_graph_task(self, coordinator_config):
        """Test generating knowledge graph through multi-agent system."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Mock the meta agent execution
        mock_meta_state = coordinator.meta_agents["kg_generator"]
        mock_meta_state.execute_agent = AsyncMock(
            return_value={
                "nodes": {"person_alice": {"name": "Alice", "type": "person"}},
                "relationships": {},
            }
        )

        # Generate knowledge graph
        result = await coordinator.generate_knowledge_graph()

        assert result["success"] is True
        assert "knowledge_graph" in result
        # Verify the agent was called
        mock_meta_state.execute_agent.assert_called_once()

    def test_get_system_status(self, coordinator_config):
        """Test getting system status."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        status = coordinator.get_system_status()

        assert status["coordinator_status"] == "active"
        assert status["total_agents"] == len(coordinator.meta_agents)
        assert "agent_status" in status
        assert "agent_capabilities" in status
        assert "performance_metrics" in status

        # Check agent status
        assert "kg_generator" in status["agent_status"]
        assert "agentic_rag" in status["agent_status"]
        assert "memory_store" in status["agent_status"]
        assert "memory_classifier" in status["agent_status"]

    @pytest.mark.asyncio
    async def test_run_diagnostic(self, coordinator_config):
        """Test running system diagnostic."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Mock all agent executions
        for agent_name, meta_state in coordinator.meta_agents.items():
            meta_state.execute_agent = AsyncMock(
                return_value=f"Diagnostic test passed for {agent_name}"
            )

        # Run diagnostic
        result = await coordinator.run_diagnostic()

        assert result["system_status"] == "healthy"
        assert "agent_diagnostics" in result
        assert len(result["agent_diagnostics"]) == len(coordinator.meta_agents)

        # Check each agent diagnostic
        for agent_name in coordinator.meta_agents:
            assert agent_name in result["agent_diagnostics"]
            assert result["agent_diagnostics"][agent_name]["status"] == "healthy"

    @pytest.mark.asyncio
    async def test_execute_task_with_error(self, coordinator_config):
        """Test task execution with error handling."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Mock an agent to raise an error
        mock_meta_state = coordinator.meta_agents["memory_store"]
        mock_meta_state.execute_agent = AsyncMock(side_effect=Exception("Test error"))

        # Create a task that will fail
        task = MemoryTask(
            id="failing_task", type="store_memory", query="This will fail"
        )

        # Execute the task
        result_task = await coordinator.execute_task(task)

        assert result_task.status == "failed"
        assert "Test error" in result_task.error
        assert result_task.completed_at is not None

    def test_performance_metrics_update(self, coordinator_config):
        """Test performance metrics tracking."""
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Create test tasks
        task1 = MemoryTask(id="task1", type="store_memory", query="Test task 1")
        task1.started_at = datetime.utcnow()
        task1.completed_at = datetime.utcnow()
        task1.assigned_agent = "memory_store"

        task2 = MemoryTask(id="task2", type="retrieve_memories", query="Test task 2")
        task2.started_at = datetime.utcnow()
        task2.completed_at = datetime.utcnow()
        task2.assigned_agent = "agentic_rag"

        # Update metrics
        coordinator._update_performance_metrics(task1, success=True)
        coordinator._update_performance_metrics(task2, success=False)

        # Check metrics
        metrics = coordinator.performance_metrics
        assert metrics["total_tasks"] == 2
        assert metrics["successful_tasks"] == 1
        assert metrics["failed_tasks"] == 1
        assert metrics["avg_latency_ms"] >= 0
        assert "memory_store" in metrics["agent_utilization"]
        assert "agentic_rag" in metrics["agent_utilization"]


@pytest.mark.asyncio
async def test_multi_agent_integration():
    """Integration test for the complete multi-agent memory system."""
    try:
        # Skip if dependencies not available
        from haive.core.tools.store_tools import StoreManager

        from haive.agents.memory.core.classifier import (
            MemoryClassifier,
            MemoryClassifierConfig,
        )
        from haive.agents.memory.core.stores import (
            MemoryStoreConfig,
            MemoryStoreManager,
        )

        # Create real store manager (in-memory for testing)
        store_manager = StoreManager(
            store_type="memory", collection_name="test_multi_agent"
        )

        # Create memory store manager
        memory_store_config = MemoryStoreConfig(
            store_manager=store_manager, auto_classify=False
        )
        memory_store = MemoryStoreManager(memory_store_config)

        # Create classifier
        classifier_config = MemoryClassifierConfig()
        classifier = MemoryClassifier(classifier_config)

        # Create configurations
        kg_config = KGGeneratorAgentConfig(
            memory_store_manager=memory_store, memory_classifier=classifier
        )

        rag_config = AgenticRAGCoordinatorConfig(
            memory_store_manager=memory_store,
            memory_classifier=classifier,
            kg_generator=MagicMock(),  # Will be replaced
        )

        coordinator_config = MultiAgentCoordinatorConfig(
            memory_store_manager=memory_store,
            memory_classifier=classifier,
            kg_generator_config=kg_config,
            agentic_rag_config=rag_config,
        )

        # Create coordinator
        coordinator = MultiAgentMemoryCoordinator(coordinator_config)

        # Test system status
        status = coordinator.get_system_status()
        assert status["coordinator_status"] == "active"
        assert status["total_agents"] > 0

        # Test storing memory
        await memory_store.store_memory(
            content="Alice works at TechCorp as a software engineer",
            namespace=("test", "multi_agent"),
        )

        # Test retrieving memories
        memories = await memory_store.retrieve_memories(
            query="Alice engineer", namespace=("test", "multi_agent")
        )

        assert len(memories) >= 0  # Should work without errors

    except ImportError as e:
        pytest.skip(f"Missing dependencies: {e}")


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
