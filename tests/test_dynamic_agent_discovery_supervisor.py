"""Tests for DynamicAgentDiscoverySupervisor with real components."""

import os
import tempfile

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.agents.supervisor.dynamic_agent_discovery_supervisor import (
    AgentDiscoveryMode,
    DynamicAgentDiscoverySupervisor,
)


class TestDynamicAgentDiscoverySupervisor:
    """Test suite for DynamicAgentDiscoverySupervisor."""

    @pytest.fixture
    def base_config(self):
        """Base LLM configuration for tests."""
        return AugLLMConfig(temperature=0.1, max_tokens=500)

    @pytest.fixture
    def initial_agents(self, base_config):
        """Create initial agents for testing."""
        return {"generalist": SimpleAgent(name="generalist", engine=base_config)}

    @pytest.fixture
    def agent_specs(self):
        """Sample agent specifications."""
        return [
            {
                "name": "data_analyst",
                "agent_type": "ReactAgent",
                "description": "Expert in data analysis and statistics",
                "specialties": ["data analysis", "statistics", "visualization"],
                "tools": ["calculator", "data_processor"],
                "config": {},
            },
            {
                "name": "researcher",
                "agent_type": "SimpleAgent",
                "description": "Expert in research and information gathering",
                "specialties": ["research", "fact-checking", "summarization"],
                "tools": ["web_search", "document_reader"],
                "config": {},
            },
            {
                "name": "writer",
                "agent_type": "SimpleAgent",
                "description": "Expert in content writing and editing",
                "specialties": ["writing", "editing", "copywriting"],
                "tools": [],
                "config": {},
            },
        ]

    def test_supervisor_creation(self, base_config, initial_agents):
        """Test basic supervisor creation."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="test_supervisor", agents=initial_agents, engine=base_config
        )

        assert supervisor.name == "test_supervisor"
        assert len(supervisor.agents) == 1
        assert "generalist" in supervisor.agents
        assert supervisor.discovery_mode == AgentDiscoveryMode.HYBRID
        assert len(supervisor.discovered_agents) == 0

    def test_agent_factory_initialization(self, base_config, initial_agents):
        """Test that agent factory is properly initialized."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="test_supervisor", agents=initial_agents, engine=base_config
        )

        assert "SimpleAgent" in supervisor.agent_factory
        assert "ReactAgent" in supervisor.agent_factory
        assert "PerplexityStyleAgent" in supervisor.agent_factory

    def test_register_discovered_agent(self, base_config, initial_agents):
        """Test registering a discovered agent."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="test_supervisof", agents=initial_agents, engine=base_config
        )

        # Register new agent
        agent_data = {
            "name": "specialist",
            "agent_type": "SimpleAgent",
            "description": "A specialist agent",
            "specialties": ["analysis"],
            "config": {},
        }

        success = supervisor._register_discovered_agent(agent_data)

        assert success is True
        assert "specialist" in supervisor.agents
        assert "specialist" in supervisor.discovered_agents
        assert "specialist" in supervisor.agent_capabilities

        # Check capability was stored
        capability = supervisor.agent_capabilities["specialist"]
        assert capability.name == "specialist"
        assert capability.agent_type == "SimpleAgent"
        assert capability.description == "A specialist agent"
        assert capability.specialties == ["analysis"]

    def test_discovery_modes(self, base_config, initial_agents):
        """Test different discovery modes."""
        modes = [
            AgentDiscoveryMode.COMPONENT_DISCOVERY,
            AgentDiscoveryMode.RAG_DISCOVERY,
            AgentDiscoveryMode.MCP_DISCOVERY,
            AgentDiscoveryMode.HYBRID,
        ]

        for mode in modes:
            supervisor = DynamicAgentDiscoverySupervisor(
                name=f"supervisor_{mode}",
                agents=initial_agents,
                engine=base_config,
                discovery_mode=mode,
            )

            assert supervisor.discovery_mode == mode

    def test_factory_with_agent_specs(self, base_config, agent_specs):
        """Test factory method with agent specifications."""
        supervisor = DynamicAgentDiscoverySupervisor.create_with_agent_specs(
            name="spec_supervisor", initial_agent_specs=agent_specs, engine=base_config
        )

        assert supervisor.name == "spec_supervisor"
        assert len(supervisor.agents) == 3
        assert "data_analyst" in supervisor.agents
        assert "researcher" in supervisor.agents
        assert "writer" in supervisor.agents

        # Check agent types
        assert isinstance(supervisor.agents["data_analyst"], ReactAgent)
        assert isinstance(supervisor.agents["researcher"], SimpleAgent)
        assert isinstance(supervisor.agents["writer"], SimpleAgent)

    @pytest.mark.asyncio
    async def test_routing_decision_with_specialists(self, base_config, agent_specs):
        """Test routing decisions considering agent specialties."""
        # Create supervisor with specialists
        supervisor = DynamicAgentDiscoverySupervisor.create_with_agent_specs(
            name="routing_supervisor",
            initial_agent_specs=agent_specs,
            engine=base_config,
        )

        # Test routing for data task
        from haive.agents.supervisor.types import SupervisorState

        state = SupervisorState(
            messages=[
                HumanMessage(content="Analyze the sales data and create a report")
            ],
            next_agent="",
            agent_outputs={},
        )

        decision = await supervisor._make_decision(state)

        assert decision.next_agent in supervisor.agents
        assert decision.confidence > 0.5
        assert decision.reasoning != ""

    @pytest.mark.asyncio
    async def test_agent_discovery_trigger(self, base_config, initial_agents):
        """Test that agent discovery is triggered for specialized tasks."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="discovery_supervisor", agents=initial_agents, engine=base_config
        )

        # Task requiring specialist
        from haive.agents.supervisor.types import SupervisorState

        state = SupervisorState(
            messages=[
                HumanMessage(
                    content="I need a financial expert to analyze investment options"
                )
            ],
            next_agent="",
            agent_outputs={},
        )

        decision = await supervisor._make_decision(state)

        # Should route to self for discovery since no specialists exist
        assert decision.next_agent == supervisor.name
        assert (
            "specialist" in decision.reasoning.lower()
            or "discover" in decision.reasoning.lower()
        )

    def test_factory_with_discovery_sources(self, base_config, initial_agents):
        """Test factory with discovery source configuration."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sample agent documentation
            agent_doc_path = os.path.join(temp_dir, "agents.md")
            with open(agent_doc_path, "w") as f:
                f.write(
                    """# Available Agents

## Financial Analyst Agent
- Type: ReactAgent
- Description: Expert in financial analysis and market trends
- Specialties: finance, markets, investment, analysis
- Tools: calculator, market_data, financial_reports

## Legal Expert Agent
- Type: SimpleAgent
- Description: Expert in legal matters and compliance
- Specialties: legal, compliance, contracts, regulations
- Tools: legal_database, document_analyzer

## Medical Consultant Agent
- Type: SimpleAgent
- Description: Medical and healthcare expert
- Specialties: medical, healthcare, diagnosis, treatment
- Tools: medical_database, symptom_checker
"""
                )

            supervisor = DynamicAgentDiscoverySupervisor.create_with_discovery(
                name="configured_supervisof",
                agents=initial_agents,
                engine=base_config,
                discovery_mode=AgentDiscoveryMode.HYBRID,
                component_discovery_config={"registry_path": "./agents"},
                rag_documents_path=temp_dir,
                mcp_config={"endpoint": "http://localhost:8000"},
            )

            assert supervisor.discovery_mode == AgentDiscoveryMode.HYBRID
            assert supervisor.rag_discovery_agent is not None
            assert supervisor.mcp_framework is not None

    @pytest.mark.asyncio
    async def test_supervisor_run_with_discovery(self, base_config):
        """Test full supervisor run with agent discovery."""
        initial_agents = {
            "assistant": SimpleAgent(name="assistant", engine=base_config)
        }

        supervisor = DynamicAgentDiscoverySupervisor(
            name="main_supervisor", agents=initial_agents, engine=base_config
        )

        # Run supervisor with a task
        result = await supervisor.arun("I need help writing a technical report")

        assert isinstance(result, str)
        assert len(result) > 0

    def test_agent_capability_tracking(self, base_config, initial_agents):
        """Test that agent capabilities are properly tracked."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="capability_supervisof", agents=initial_agents, engine=base_config
        )

        # Register multiple agents with different capabilities
        agents_to_register = [
            {
                "name": "analyst",
                "agent_type": "ReactAgent",
                "description": "Data analyst",
                "specialties": ["data", "statistics"],
                "tools": ["calculator", "visualizer"],
            },
            {
                "name": "coder",
                "agent_type": "SimpleAgent",
                "description": "Code expert",
                "specialties": ["python", "javascript"],
                "tools": ["code_executor", "debugger"],
            },
        ]

        for agent_data in agents_to_register:
            supervisor._register_discovered_agent(agent_data)

        # Check capabilities
        assert len(supervisor.agent_capabilities) == 2

        analyst_cap = supervisor.agent_capabilities["analyst"]
        assert "data" in analyst_cap.specialties
        assert "calculator" in analyst_cap.tools

        coder_cap = supervisor.agent_capabilities["coder"]
        assert "python" in coder_cap.specialties
        assert "code_executor" in coder_cap.tools

    def test_duplicate_agent_prevention(self, base_config, initial_agents):
        """Test that duplicate agents are not registered."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="duplicate_supervisof", agents=initial_agents, engine=base_config
        )

        agent_data = {
            "name": "new_agent",
            "agent_type": "SimpleAgent",
            "description": "Test agent",
        }

        # First registration should succeed
        success1 = supervisor._register_discovered_agent(agent_data)
        assert success1 is True
        assert len(supervisor.agents) == 2

        # Second registration should fail
        success2 = supervisor._register_discovered_agent(agent_data)
        assert success2 is False
        assert len(supervisor.agents) == 2  # No change

    def test_max_discovery_attempts(self, base_config, initial_agents):
        """Test max discovery attempts configuration."""
        supervisor = DynamicAgentDiscoverySupervisor(
            name="limited_supervisor",
            agents=initial_agents,
            engine=base_config,
            max_discovery_attempts=5,
        )

        assert supervisor.max_discovery_attempts == 5

        # Test validation
        with pytest.raises(Exception):
            DynamicAgentDiscoverySupervisor(
                name="invalid_supervisor",
                agents=initial_agents,
                engine=base_config,
                max_discovery_attempts=0,  # Should fail validation
            )
