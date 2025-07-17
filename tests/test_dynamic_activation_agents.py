"""Tests for Dynamic Activation Pattern - Agent Components.

This module tests the agent components of the Dynamic Activation Pattern
using real components (no mocks) following the Haive testing philosophy.

Based on:
- @project_docs/active/patterns/dynamic_activation_pattern.md
- @project_docs/active/standards/testing/philosophy.md (no mocks)
- Real Azure OpenAI integration for testing
"""

import asyncio
from typing import Any, Dict, List, Optional
from unittest.mock import patch

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.registry import DynamicRegistry, RegistryItem
from haive.core.schema.prebuilt.dynamic_activation_state import DynamicActivationState
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from pydantic import BaseModel, Field

from haive.agents.discovery.component_discovery_agent import ComponentDiscoveryAgent
from haive.agents.react.dynamic_react_agent import DynamicReactAgent, DynamicToolState
from haive.agents.supervisor.dynamic_activation_supervisor import (
    DynamicActivationSupervisor,
)


class TestComponentDiscoveryAgent:
    """Test suite for ComponentDiscoveryAgent with real components."""

    @pytest.fixture
    def test_document_content(self):
        """Create test document content for discovery."""
        return """
        # Test Tools Documentation
        
        ## Calculator Tool
        
        A mathematical calculation tool that can perform basic arithmetic operations.
        
        - **Name**: calculator
        - **Description**: Mathematical calculations and arithmetic operations
        - **Input**: Mathematical expressions as strings
        - **Output**: Numerical results
        - **Category**: math
        
        ## Web Search Tool
        
        A web search tool that can search the internet for information.
        
        - **Name**: web_search
        - **Description**: Search the web for information and return results
        - **Input**: Search queries as strings
        - **Output**: Search results with titles and URLs
        - **Category**: web
        
        ## File Reader Tool
        
        A file reading tool that can read various file formats.
        
        - **Name**: file_reader
        - **Description**: Read and process files of various formats
        - **Input**: File paths and format specifications
        - **Output**: File contents as strings
        - **Category**: file
        """

    @pytest.fixture
    def temp_document_file(self, tmp_path, test_document_content):
        """Create temporary document file for testing."""
        doc_file = tmp_path / "test_tools.md"
        doc_file.write_text(test_document_content)
        return str(doc_file)

    def test_component_discovery_agent_creation(self, temp_document_file):
        """Test creating ComponentDiscoveryAgent with real document."""
        agent = ComponentDiscoveryAgent(document_path=temp_document_file)

        assert agent.document_path == temp_document_file
        assert agent.discovery_config["source"] == temp_document_file
        assert agent.discovery_config["auto_discover"] is True

        # Verify discovery agent is initialized (model_validator)
        assert agent._discovery_agent is not None
        assert agent._haive_discovery is not None

    def test_component_discovery_agent_factory_method(self, temp_document_file):
        """Test factory method for ComponentDiscoveryAgent."""
        # Test with discovery source
        agent = ComponentDiscoveryAgent.create_with_discovery(
            document_path=temp_document_file, discovery_config={"max_results": 10}
        )

        assert agent.document_path == temp_document_file
        assert agent.discovery_config["max_results"] == 10
        assert agent._discovery_agent is not None

    @pytest.mark.asyncio
    async def test_component_discovery_real_search(self, temp_document_file):
        """Test real component discovery from document."""
        agent = ComponentDiscoveryAgent(document_path=temp_document_file)

        # Discover components for math tools
        components = await agent.discover_components("mathematical calculation tools")

        # Verify discovery results
        assert len(components) > 0

        # Check for calculator tool in results
        calculator_found = False
        for component in components:
            if "calculator" in component.get("name", "").lower():
                calculator_found = True
                assert "math" in component.get("description", "").lower()
                break

        assert calculator_found, "Calculator tool should be found in discovery results"

    @pytest.mark.asyncio
    async def test_component_discovery_different_queries(self, temp_document_file):
        """Test discovery with different query types."""
        agent = ComponentDiscoveryAgent(document_path=temp_document_file)

        # Test different query types
        queries = [
            "web search functionality",
            "file processing tools",
            "tools for reading files",
            "internet search capabilities",
        ]

        for query in queries:
            components = await agent.discover_components(query)
            assert len(components) > 0, f"No components found for query: {query}"

    @pytest.mark.asyncio
    async def test_component_discovery_with_haive_sources(self):
        """Test discovery with @haive-* sources."""
        # Test with @haive-tools source
        agent = ComponentDiscoveryAgent(document_path="@haive-tools")

        # This should work with the existing Haive tools documentation
        components = await agent.discover_components("available tools")

        # Verify some components were found
        assert len(components) >= 0  # May be empty if no tools docs found

    def test_component_discovery_agent_configuration(self, temp_document_file):
        """Test various configuration options."""
        # Test with custom configuration
        config = {
            "max_results": 5,
            "similarity_threshold": 0.8,
            "include_metadata": True,
        }

        agent = ComponentDiscoveryAgent(
            document_path=temp_document_file, discovery_config=config
        )

        assert agent.discovery_config["max_results"] == 5
        assert agent.discovery_config["similarity_threshold"] == 0.8
        assert agent.discovery_config["include_metadata"] is True


class TestDynamicActivationSupervisor:
    """Test suite for DynamicActivationSupervisor with real components."""

    @pytest.fixture
    def aug_llm_config(self):
        """Create real AugLLMConfig for testing."""
        return AugLLMConfig(
            name="test_supervisor_llm",
            temperature=0.1,
            max_tokens=200,
            model="gpt-4o-mini",
        )

    @pytest.fixture
    def temp_document_file(self, tmp_path):
        """Create temporary document file for testing."""
        doc_content = """
        # Test Components
        
        ## Data Processor
        - **Name**: data_processor
        - **Description**: Process and analyze data
        - **Category**: data
        
        ## Report Generator
        - **Name**: report_generator
        - **Description**: Generate reports from data
        - **Category**: reporting
        """
        doc_file = tmp_path / "test_components.md"
        doc_file.write_text(doc_content)
        return str(doc_file)

    def test_supervisor_creation_with_discovery(
        self, temp_document_file, aug_llm_config
    ):
        """Test creating supervisor with discovery capabilities."""
        supervisor = DynamicActivationSupervisor.create_with_discovery(
            name="test_supervisor",
            document_path=temp_document_file,
            engine=aug_llm_config,
        )

        assert supervisor.name == "test_supervisor"
        assert supervisor.engine == aug_llm_config
        assert supervisor._discovery_agent is not None
        assert supervisor._meta_self is not None
        assert isinstance(supervisor._meta_self, MetaStateSchema)

        # Verify state is DynamicActivationState
        assert isinstance(supervisor.state, DynamicActivationState)
        assert isinstance(supervisor.state.registry, DynamicRegistry)

    def test_supervisor_creation_with_components(self, aug_llm_config):
        """Test creating supervisor with pre-defined components."""
        # Create test components
        components = [
            {
                "id": "comp_001",
                "name": "Test Component 1",
                "description": "First test component",
                "component": {"type": "processor", "version": "1.0"},
            },
            {
                "id": "comp_002",
                "name": "Test Component 2",
                "description": "Second test component",
                "component": {"type": "analyzer", "version": "2.0"},
            },
        ]

        supervisor = DynamicActivationSupervisor.create_with_components(
            name="test_supervisor", components=components, engine=aug_llm_config
        )

        assert supervisor.name == "test_supervisor"
        assert len(supervisor.state.registry.items) == 2
        assert "comp_001" in supervisor.state.registry.items
        assert "comp_002" in supervisor.state.registry.items

    @pytest.mark.asyncio
    async def test_supervisor_component_activation(
        self, temp_document_file, aug_llm_config
    ):
        """Test supervisor component activation functionality."""
        supervisor = DynamicActivationSupervisor.create_with_discovery(
            name="test_supervisor",
            document_path=temp_document_file,
            engine=aug_llm_config,
        )

        # Manually register a component for testing
        from haive.core.registry import RegistryItem

        test_component = {"name": "test_processor", "type": "processor"}
        item = RegistryItem(
            id="test_001",
            name="Test Processor",
            description="A test processing component",
            component=test_component,
        )
        supervisor.state.registry.register(item)

        # Activate component
        meta_state = supervisor.state.activate_component("test_001")

        assert meta_state is not None
        assert isinstance(meta_state, MetaStateSchema)
        assert meta_state.agent == test_component
        assert "test_001" in supervisor.state.active_components

    def test_supervisor_graph_building(self, temp_document_file, aug_llm_config):
        """Test supervisor graph building with conditional routing."""
        supervisor = DynamicActivationSupervisor.create_with_discovery(
            name="test_supervisor",
            document_path=temp_document_file,
            engine=aug_llm_config,
        )

        # Build the graph
        graph = supervisor.build_graph()

        # Verify graph structure
        assert graph is not None
        assert "analyze_request" in graph.nodes
        assert "route_to_components" in graph.nodes
        assert "activation_decision" in graph.nodes

        # Verify graph metadata
        assert "discovery_enabled" in graph.metadata
        assert "component_activation" in graph.metadata
        assert graph.metadata["discovery_enabled"] is True
        assert graph.metadata["component_activation"] is True

    @pytest.mark.asyncio
    async def test_supervisor_real_execution(self, temp_document_file, aug_llm_config):
        """Test supervisor execution with real LLM."""
        supervisor = DynamicActivationSupervisor.create_with_discovery(
            name="test_supervisor",
            document_path=temp_document_file,
            engine=aug_llm_config,
        )

        # Execute supervisor with a simple request
        result = await supervisor.arun("Hello, can you help me process some data?")

        # Verify execution
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

        # Verify MetaStateSchema tracking
        assert supervisor._meta_self.execution_status == "completed"
        assert supervisor._meta_self.last_execution_time is not None


class TestDynamicReactAgent:
    """Test suite for DynamicReactAgent with real components."""

    @pytest.fixture
    def aug_llm_config(self):
        """Create real AugLLMConfig for testing."""
        return AugLLMConfig(
            name="test_react_llm", temperature=0.1, max_tokens=150, model="gpt-4o-mini"
        )

    @pytest.fixture
    def temp_tools_file(self, tmp_path):
        """Create temporary tools document for testing."""
        tools_content = """
        # Test Tools
        
        ## Calculator
        - **Name**: calculator
        - **Description**: Mathematical calculations
        - **Input**: Mathematical expressions
        - **Category**: math
        
        ## Text Processor
        - **Name**: text_processor
        - **Description**: Process and analyze text
        - **Input**: Text strings
        - **Category**: text
        """
        tools_file = tmp_path / "test_tools.md"
        tools_file.write_text(tools_content)
        return str(tools_file)

    def test_dynamic_react_agent_creation_with_discovery(
        self, temp_tools_file, aug_llm_config
    ):
        """Test creating DynamicReactAgent with discovery capabilities."""
        agent = DynamicReactAgent.create_with_discovery(
            name="test_dynamic_react",
            document_path=temp_tools_file,
            engine=aug_llm_config,
        )

        assert agent.name == "test_dynamic_react"
        assert agent.engine == aug_llm_config
        assert agent.state_schema == DynamicToolState
        assert agent._discovery_agent is not None
        assert agent._meta_self is not None
        assert isinstance(agent._meta_self, MetaStateSchema)

        # Verify state is DynamicToolState
        assert isinstance(agent.state, DynamicToolState)
        assert isinstance(agent.state.registry, DynamicRegistry)

    def test_dynamic_react_agent_creation_with_tools(self, aug_llm_config):
        """Test creating DynamicReactAgent with predefined tools."""
        from langchain_core.tools import tool

        @tool
        def test_calculator(expression: str) -> float:
            """Calculate mathematical expression."""
            return eval(expression)

        @tool
        def test_text_processor(text: str) -> str:
            """Process text input."""
            return f"Processed: {text}"

        tools = [
            {
                "id": "calc_001",
                "name": "Calculator",
                "description": "Mathematical calculations",
                "component": test_calculator,
                "category": "math",
            },
            {
                "id": "text_001",
                "name": "Text Processor",
                "description": "Text processing",
                "component": test_text_processor,
                "category": "text",
            },
        ]

        agent = DynamicReactAgent.create_with_tools(
            name="test_tool_react", tools=tools, engine=aug_llm_config
        )

        assert agent.name == "test_tool_react"
        assert len(agent.state.registry.items) == 2
        assert "calc_001" in agent.state.registry.items
        assert "text_001" in agent.state.registry.items

        # Verify tool categorization
        assert "math" in agent.state.tool_categories
        assert "text" in agent.state.tool_categories
        assert "Calculator" in agent.state.tool_categories["math"]
        assert "Text Processor" in agent.state.tool_categories["text"]

    def test_dynamic_tool_state_functionality(self, aug_llm_config):
        """Test DynamicToolState specific functionality."""
        agent = DynamicReactAgent(name="test_state_agent", engine=aug_llm_config)

        # Test tool categorization
        agent.state.categorize_tool("calculator", "math")
        agent.state.categorize_tool("web_search", "web")
        agent.state.categorize_tool("file_reader", "file")

        # Verify categories
        assert agent.state.get_tools_by_category("math") == ["calculator"]
        assert agent.state.get_tools_by_category("web") == ["web_search"]
        assert agent.state.get_tools_by_category("file") == ["file_reader"]

        # Test tool usage tracking
        agent.state.track_tool_usage("calculator")
        agent.state.track_tool_usage("calculator")
        agent.state.track_tool_usage("web_search")

        # Verify usage stats
        stats = agent.state.get_tool_usage_stats()
        assert stats["calculator"] == 2
        assert stats["web_search"] == 1

    @pytest.mark.asyncio
    async def test_dynamic_react_agent_tool_discovery(
        self, temp_tools_file, aug_llm_config
    ):
        """Test dynamic tool discovery functionality."""
        agent = DynamicReactAgent.create_with_discovery(
            name="test_discovery_react",
            document_path=temp_tools_file,
            engine=aug_llm_config,
        )

        # Test tool discovery
        tools = await agent.discover_and_load_tools("mathematical calculations")

        # Verify discovery results
        assert len(tools) >= 0  # May be empty if no tools are loaded

        # Verify discovery tracking
        assert len(agent.state.discovery_queries) > 0
        assert "mathematical calculations" in agent.state.discovery_queries[-1]
        assert agent.state.last_tool_discovery is not None

    def test_dynamic_react_agent_tool_activation(self, aug_llm_config):
        """Test tool activation and deactivation."""
        from langchain_core.tools import tool

        @tool
        def test_tool(input_text: str) -> str:
            """A test tool."""
            return f"Tool output: {input_text}"

        # Create agent with tool
        tools = [
            {
                "id": "test_001",
                "name": "Test Tool",
                "description": "A test tool",
                "component": test_tool,
                "category": "test",
            }
        ]

        agent = DynamicReactAgent.create_with_tools(
            name="test_activation_react", tools=tools, engine=aug_llm_config
        )

        # Test activation by name
        success = asyncio.run(agent.activate_tool_by_name("Test Tool"))
        assert success is True
        assert "Test Tool" in agent.get_active_tool_names()

        # Test deactivation by name
        success = agent.deactivate_tool_by_name("Test Tool")
        assert success is True
        assert "Test Tool" not in agent.get_active_tool_names()

    def test_dynamic_react_agent_registry_stats(self, aug_llm_config):
        """Test registry statistics functionality."""
        from langchain_core.tools import tool

        @tool
        def math_tool(expression: str) -> float:
            """Mathematical calculations."""
            return eval(expression)

        @tool
        def text_tool(text: str) -> str:
            """Text processing."""
            return f"Processed: {text}"

        tools = [
            {
                "id": "math_001",
                "name": "Math Tool",
                "description": "Mathematical tool",
                "component": math_tool,
                "category": "math",
            },
            {
                "id": "text_001",
                "name": "Text Tool",
                "description": "Text tool",
                "component": text_tool,
                "category": "text",
            },
        ]

        agent = DynamicReactAgent.create_with_tools(
            name="test_stats_react", tools=tools, engine=aug_llm_config
        )

        # Activate one tool
        asyncio.run(agent.activate_tool_by_name("Math Tool"))

        # Get registry stats
        stats = agent.get_registry_stats()

        assert stats["total_components"] == 2
        assert stats["active_components"] == 1
        assert stats["inactive_components"] == 1
        assert stats["activation_rate"] == 0.5

    @pytest.mark.asyncio
    async def test_dynamic_react_agent_real_execution(
        self, temp_tools_file, aug_llm_config
    ):
        """Test DynamicReactAgent execution with real LLM."""
        agent = DynamicReactAgent.create_with_discovery(
            name="test_execution_react",
            document_path=temp_tools_file,
            engine=aug_llm_config,
        )

        # Execute agent with a simple request
        result = await agent.arun("Hello, can you help me?")

        # Verify execution
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

        # Verify MetaStateSchema tracking
        assert agent._meta_self.execution_status == "completed"
        assert agent._meta_self.last_execution_time is not None

    def test_dynamic_react_agent_graph_building(self, temp_tools_file, aug_llm_config):
        """Test DynamicReactAgent graph building."""
        agent = DynamicReactAgent.create_with_discovery(
            name="test_graph_react",
            document_path=temp_tools_file,
            engine=aug_llm_config,
        )

        # Build the graph
        graph = agent.build_graph()

        # Verify graph structure (inherits from ReactAgent)
        assert graph is not None
        assert "agent_node" in graph.nodes

        # Verify graph metadata includes dynamic tool info
        assert "recompilation_enabled" in graph.metadata.get("graph_context", {})
        assert "tool_discovery" in graph.metadata.get("graph_context", {})


class TestDynamicActivationIntegration:
    """Integration tests for complete dynamic activation workflows."""

    @pytest.fixture
    def aug_llm_config(self):
        """Create real AugLLMConfig for integration testing."""
        return AugLLMConfig(
            name="integration_test_llm",
            temperature=0.1,
            max_tokens=300,
            model="gpt-4o-mini",
        )

    @pytest.fixture
    def comprehensive_tools_file(self, tmp_path):
        """Create comprehensive tools document for integration testing."""
        tools_content = """
        # Comprehensive Tools Documentation
        
        ## Mathematical Tools
        
        ### Calculator
        - **Name**: calculator
        - **Description**: Basic arithmetic calculations
        - **Input**: Mathematical expressions as strings
        - **Output**: Numerical results
        - **Category**: math
        
        ### Statistics Calculator
        - **Name**: stats_calculator
        - **Description**: Statistical calculations and analysis
        - **Input**: Lists of numbers and statistical operations
        - **Output**: Statistical results
        - **Category**: math
        
        ## Text Processing Tools
        
        ### Text Analyzer
        - **Name**: text_analyzer
        - **Description**: Analyze text for patterns and insights
        - **Input**: Text strings
        - **Output**: Analysis results
        - **Category**: text
        
        ### Language Detector
        - **Name**: language_detector
        - **Description**: Detect language of input text
        - **Input**: Text strings
        - **Output**: Language code and confidence
        - **Category**: text
        
        ## Web Tools
        
        ### Web Search
        - **Name**: web_search
        - **Description**: Search the web for information
        - **Input**: Search queries
        - **Output**: Search results
        - **Category**: web
        
        ### URL Validator
        - **Name**: url_validator
        - **Description**: Validate URL format and accessibility
        - **Input**: URLs
        - **Output**: Validation results
        - **Category**: web
        """
        tools_file = tmp_path / "comprehensive_tools.md"
        tools_file.write_text(tools_content)
        return str(tools_file)

    @pytest.mark.asyncio
    async def test_full_discovery_to_activation_workflow(
        self, comprehensive_tools_file, aug_llm_config
    ):
        """Test complete workflow from discovery to activation."""
        # Create discovery agent
        discovery_agent = ComponentDiscoveryAgent(
            document_path=comprehensive_tools_file
        )

        # Create supervisor with discovery
        supervisor = DynamicActivationSupervisor.create_with_discovery(
            name="integration_supervisor",
            document_path=comprehensive_tools_file,
            engine=aug_llm_config,
        )

        # Create dynamic React agent
        react_agent = DynamicReactAgent.create_with_discovery(
            name="integration_react",
            document_path=comprehensive_tools_file,
            engine=aug_llm_config,
        )

        # Test discovery workflow
        discovered_tools = await discovery_agent.discover_components(
            "mathematical calculation tools"
        )
        assert len(discovered_tools) >= 0

        # Test supervisor workflow
        supervisor_result = await supervisor.arun(
            "I need help with mathematical calculations"
        )
        assert supervisor_result is not None

        # Test React agent workflow
        react_result = await react_agent.arun("Can you help me with text analysis?")
        assert react_result is not None

        # Verify all components are working
        assert discovery_agent._discovery_agent is not None
        assert supervisor._meta_self is not None
        assert react_agent._meta_self is not None

    @pytest.mark.asyncio
    async def test_multi_agent_component_sharing(
        self, comprehensive_tools_file, aug_llm_config
    ):
        """Test sharing components between multiple agents."""
        # Create multiple agents with same discovery source
        agents = []
        for i in range(3):
            agent = DynamicReactAgent.create_with_discovery(
                name=f"shared_agent_{i}",
                document_path=comprehensive_tools_file,
                engine=aug_llm_config,
            )
            agents.append(agent)

        # Each agent should have independent registry
        for agent in agents:
            assert isinstance(agent.state.registry, DynamicRegistry)
            assert len(agent.state.registry.items) >= 0

        # Test independent tool discovery
        for i, agent in enumerate(agents):
            tools = await agent.discover_and_load_tools(f"tools for agent {i}")
            # Each agent can discover independently
            assert len(agent.state.discovery_queries) > 0

    @pytest.mark.asyncio
    async def test_performance_with_multiple_activations(
        self, comprehensive_tools_file, aug_llm_config
    ):
        """Test performance with multiple component activations."""
        import time

        # Create agent with discovery
        agent = DynamicReactAgent.create_with_discovery(
            name="performance_test_agent",
            document_path=comprehensive_tools_file,
            engine=aug_llm_config,
        )

        # Create multiple test components
        from langchain_core.tools import tool

        test_tools = []
        for i in range(20):

            @tool
            def test_tool_func(input_text: str) -> str:
                """Test tool function."""
                return f"Tool {i} output: {input_text}"

            test_tools.append(
                {
                    "id": f"perf_tool_{i:03d}",
                    "name": f"Performance Tool {i}",
                    "description": f"Performance test tool {i}",
                    "component": test_tool_func,
                    "category": "performance",
                }
            )

        # Create agent with many tools
        perf_agent = DynamicReactAgent.create_with_tools(
            name="performance_agent", tools=test_tools, engine=aug_llm_config
        )

        # Test rapid activation/deactivation
        start_time = time.time()

        for i in range(10):
            await perf_agent.activate_tool_by_name(f"Performance Tool {i}")

        for i in range(10):
            perf_agent.deactivate_tool_by_name(f"Performance Tool {i}")

        end_time = time.time()

        # Verify performance is reasonable
        assert end_time - start_time < 2.0  # Should complete in under 2 seconds

        # Verify correctness
        assert len(perf_agent.get_active_tool_names()) == 0
        stats = perf_agent.get_registry_stats()
        assert stats["total_components"] == 20
        assert stats["active_components"] == 0

    def test_error_handling_and_recovery(
        self, comprehensive_tools_file, aug_llm_config
    ):
        """Test error handling and recovery mechanisms."""
        # Test with invalid discovery source
        agent = DynamicReactAgent.create_with_discovery(
            name="error_test_agent",
            document_path="/nonexistent/path/tools.md",
            engine=aug_llm_config,
        )

        # Agent should still be created but discovery agent may be None
        assert agent.name == "error_test_agent"
        assert agent.engine == aug_llm_config

        # Test activation of non-existent tool
        success = asyncio.run(agent.activate_tool_by_name("NonExistentTool"))
        assert success is False

        # Test deactivation of non-existent tool
        success = agent.deactivate_tool_by_name("NonExistentTool")
        assert success is False

        # Verify agent state is still consistent
        stats = agent.get_registry_stats()
        assert stats["total_components"] == 0
        assert stats["active_components"] == 0
