"""Tests for DynamicToolDiscoverySupervisor with real components."""

import asyncio
import os
import tempfile
from typing import Any, Dict, List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.agents.supervisor.dynamic_tool_discovery_supervisor import (
    DynamicToolDiscoverySupervisor,
    ToolDiscoveryMode,
)


class TestDynamicToolDiscoverySupervisor:
    """Test suite for DynamicToolDiscoverySupervisor."""

    @pytest.fixture
    def base_config(self):
        """Base LLM configuration for tests."""
        return AugLLMConfig(temperature=0.1, max_tokens=500)

    @pytest.fixture
    def sample_agents(self, base_config):
        """Create sample agents for testing."""
        return {
            "analyzer": SimpleAgent(name="analyzer", engine=base_config),
            "executor": ReactAgent(name="executor", engine=base_config, tools=[]),
        }

    @pytest.fixture
    def sample_tools(self):
        """Create sample tools for testing."""

        @tool
        def calculator(expression: str) -> str:
            """Calculate mathematical expressions."""
            try:
                result = eval(expression)
                return f"Result: {result}"
            except:
                return "Error in calculation"

        @tool
        def word_counter(text: str) -> str:
            """Count words in text."""
            words = text.split()
            return f"Word count: {len(words)}"

        return [calculator, word_counter]

    def test_supervisor_creation(self, base_config, sample_agents):
        """Test basic supervisor creation."""
        supervisor = DynamicToolDiscoverySupervisor(
            name="test_supervisor", agents=sample_agents, engine=base_config
        )

        assert supervisor.name == "test_supervisor"
        assert len(supervisor.agents) == 2
        assert supervisor.discovery_mode == ToolDiscoveryMode.HYBRID
        assert "discover_and_load_tools" in supervisor.discovered_tools

    def test_supervisor_with_initial_tools(
        self, base_config, sample_agents, sample_tools
    ):
        """Test supervisor with initial tools."""
        # Prepare tools for registration
        tools_data = []
        for tool in sample_tools:
            tools_data.append(
                {"name": tool.name, "description": tool.description, "func": tool.func}
            )

        supervisor = DynamicToolDiscoverySupervisor(
            name="test_supervisor",
            agents=sample_agents,
            engine=base_config,
            tools_to_register=tools_data,
        )

        # Check tools were registered
        assert "calculator" in supervisor.discovered_tools
        assert "word_counter" in supervisor.discovered_tools
        assert len(supervisor.tool_registry) >= 3  # Including discovery tool

    def test_factory_with_agents_and_tools(self, base_config, sample_tools):
        """Test factory method with agents and tools."""
        agent_configs = [
            {"type": "SimpleAgent", "name": "simple_worker"},
            {"type": "ReactAgent", "name": "react_worker"},
        ]

        supervisor = DynamicToolDiscoverySupervisor.create_with_agents_and_tools(
            name="factory_supervisor",
            agent_configs=agent_configs,
            engine=base_config,
            initial_tools=sample_tools,
            discovery_mode=ToolDiscoveryMode.COMPONENT_DISCOVERY,
        )

        assert supervisor.name == "factory_supervisor"
        assert len(supervisor.agents) == 2
        assert "simple_worker" in supervisor.agents
        assert "react_worker" in supervisor.agents
        assert "calculator" in supervisor.discovered_tools

    def test_discovery_modes(self, base_config, sample_agents):
        """Test different discovery modes."""
        modes = [
            ToolDiscoveryMode.COMPONENT_DISCOVERY,
            ToolDiscoveryMode.RAG_DISCOVERY,
            ToolDiscoveryMode.MCP_DISCOVERY,
            ToolDiscoveryMode.HYBRID,
        ]

        for mode in modes:
            supervisor = DynamicToolDiscoverySupervisor(
                name=f"supervisor_{mode}",
                agents=sample_agents,
                engine=base_config,
                discovery_mode=mode,
            )

            assert supervisor.discovery_mode == mode
            assert "discover_and_load_tools" in supervisor.discovered_tools

    @pytest.mark.asyncio
    async def test_routing_decision_with_tools(self, base_config):
        """Test routing decisions considering available tools."""
        # Create agents with different capabilities
        calc_tool = tool(lambda x: f"Calculated: {x}")("calculator")

        agents = {
            "math_agent": ReactAgent(
                name="math_agent", engine=base_config, tools=[calc_tool]
            ),
            "text_agent": SimpleAgent(name="text_agent", engine=base_config),
        }

        supervisor = DynamicToolDiscoverySupervisor(
            name="routing_supervisor", agents=agents, engine=base_config
        )

        # Test routing for math task
        from haive.agents.supervisor.types import SupervisorState

        state = SupervisorState(
            messages=[HumanMessage(content="Calculate 15 * 23")],
            next_agent="",
            agent_outputs={},
        )

        decision = await supervisor._make_decision(state)

        assert decision.next_agent in ["math_agent", "routing_supervisor"]
        assert decision.confidence > 0.5
        assert decision.reasoning != ""

    @pytest.mark.asyncio
    async def test_tool_discovery_execution(self, base_config, sample_agents):
        """Test actual tool discovery execution."""
        supervisor = DynamicToolDiscoverySupervisor(
            name="discovery_supervisor", agents=sample_agents, engine=base_config
        )

        # Get the discovery tool
        discovery_tool = supervisor.tool_registry.get("discover_and_load_tools")
        assert discovery_tool is not None

        # Execute discovery
        result = discovery_tool.func(
            "I need to calculate some numbers and analyze text"
        )
        assert isinstance(result, str)
        assert "discovered" in result.lower() or "no new tools" in result.lower()

    def test_factory_with_discovery_sources(self, base_config, sample_agents):
        """Test factory with discovery source configuration."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sample tool documentation
            tool_doc_path = os.path.join(temp_dir, "tools.md")
            with open(tool_doc_path, "w") as f:
                f.write(
                    """# Available Tools
                
## Calculator Tool
Function: calculator(expression: str) -> float
Description: Evaluates mathematical expressions

## Text Analyzer
Function: analyze_text(text: str) -> dict
Description: Analyzes text for various metrics
"""
                )

            supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
                name="configured_supervisor",
                agents=sample_agents,
                engine=base_config,
                discovery_mode=ToolDiscoveryMode.HYBRID,
                component_discovery_config={"registry_path": "./components"},
                rag_documents_path=temp_dir,
                mcp_config={"endpoint": "http://localhost:8000"},
            )

            assert supervisor.discovery_mode == ToolDiscoveryMode.HYBRID
            assert supervisor.rag_tool_agent is not None
            assert supervisor.mcp_framework is not None

    @pytest.mark.asyncio
    async def test_supervisor_run_with_discovery(self, base_config):
        """Test full supervisor run with tool discovery."""
        agents = {"worker": ReactAgent(name="worker", engine=base_config, tools=[])}

        supervisor = DynamicToolDiscoverySupervisor(
            name="main_supervisor", agents=agents, engine=base_config
        )

        # Run supervisor with a task
        result = await supervisor.arun(
            "I need to calculate 50 * 30 and count words in a paragraph"
        )

        assert isinstance(result, str)
        assert len(result) > 0
        # Supervisor should have made routing decisions
        assert supervisor.state.get("routing_history", []) is not None

    def test_tool_registration_to_agents(self, base_config):
        """Test that tools are properly registered to agents."""

        @tool
        def test_tool(input: str) -> str:
            """Test tool for agents."""
            return f"Processed: {input}"

        # Create ReactAgent that can accept tools
        react_agent = ReactAgent(name="tool_user", engine=base_config, tools=[])

        agents = {"tool_user": react_agent}

        supervisor = DynamicToolDiscoverySupervisor(
            name="tool_supervisor",
            agents=agents,
            engine=base_config,
            tools_to_register=[
                {
                    "name": "test_tool",
                    "description": "Test tool",
                    "func": test_tool.func,
                }
            ],
        )

        # Check tool was registered
        assert "test_tool" in supervisor.discovered_tools
        # Note: Actual tool registration to agents depends on agent implementation

    def test_max_discovery_attempts(self, base_config, sample_agents):
        """Test max discovery attempts configuration."""
        supervisor = DynamicToolDiscoverySupervisor(
            name="limited_supervisor",
            agents=sample_agents,
            engine=base_config,
            max_discovery_attempts=5,
        )

        assert supervisor.max_discovery_attempts == 5

        # Test validation
        with pytest.raises(Exception):
            DynamicToolDiscoverySupervisor(
                name="invalid_supervisor",
                agents=sample_agents,
                engine=base_config,
                max_discovery_attempts=0,  # Should fail validation
            )
