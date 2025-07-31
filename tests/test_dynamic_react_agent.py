"""Test DynamicReactAgent implementation with real components.

This test verifies that the DynamicReactAgent can properly discover and load
tools dynamically, following the no-mocks testing philosophy.
"""

from langchain_core.tools import tool
import pytest

from haive.agents.react.dynamic_react_agent import DynamicReactAgent, DynamicToolState
from haive.core.engine.aug_llm import AugLLMConfig


@tool
def calculator(expression: str) -> float:
    """Calculate mathematical expression."""
    try:
        return eval(expression)
    except:
        return 0.0


@tool
def text_processor(text: str) -> str:
    """Process text by converting to uppercase."""
    return text.upper()


@tool
def word_counter(text: str) -> int:
    """Count words in text."""
    return len(text.split())


class TestDynamicReactAgent:
    """Test suite for DynamicReactAgent with real components."""

    def test_dynamic_tool_state_creation(self):
        """Test that DynamicToolState can be created and used."""
        state = DynamicToolState()

        # Test basic state functionality
        assert state.tool_categories == {}
        assert state.tool_usage_stats == {}
        assert state.last_tool_discovery is None
        assert state.discovery_queries == []

        # Test tool categorization
        state.categorize_tool("calculator", "math")
        assert "math" in state.tool_categories
        assert "calculator" in state.tool_categories["math"]

        # Test tool usage tracking
        state.track_tool_usage("calculator")
        assert state.tool_usage_stats["calculator"] == 1

        state.track_tool_usage("calculator")
        assert state.tool_usage_stats["calculator"] == 2

    def test_dynamic_react_agent_creation(self):
        """Test that DynamicReactAgent can be created with proper configuration."""
        config = AugLLMConfig(
            temperature=0.7,
            system_message="You are a helpful assistant with dynamic tool capabilities.",
        )

        agent = DynamicReactAgent(name="test_dynamic_agent", engine=config)

        # Test basic agent properties
        assert agent.name == "test_dynamic_agent"
        assert agent.engine == config
        # Schema is dynamically generated, so check it's a subclass or has expected fields
        assert hasattr(agent, "state_schema")
        assert agent.state_schema is not None

        # Test that the agent has no tools initially
        assert agent.discovery_agent is None
        assert agent.rag_tool_agent is None

    def test_create_with_tools_factory(self):
        """Test factory method for creating agent with pre-registered tools."""
        tools = [
            {
                "id": "calc",
                "name": "Calculator",
                "description": "Mathematical calculations",
                "component": calculator,
                "category": "math",
            },
            {
                "id": "text_proc",
                "name": "Text Processor",
                "description": "Text processing operations",
                "component": text_processor,
                "category": "text",
            },
        ]

        agent = DynamicReactAgent.create_with_tools(
            name="tool_agent", tools=tools, engine=AugLLMConfig()
        )

        assert agent.name == "tool_agent"
        # tools_to_register is set during factory method - might be None after setup
        # The important thing is that tools were registered to the engine

        # Verify tools are registered during setup
        agent.setup_agent()

        # Check that tools were added to engine
        assert calculator in agent.engine.tools
        assert text_processor in agent.engine.tools

    def test_create_with_discovery_factory(self):
        """Test factory method for creating agent with discovery capabilities."""
        agent = DynamicReactAgent.create_with_discovery(
            name="discovery_agent",
            document_path="@haive-tools",
            engine=AugLLMConfig(),
            use_mcp=False,
        )

        assert agent.name == "discovery_agent"
        assert hasattr(agent, "_discovery_config")
        assert agent._discovery_config["document_path"] == "@haive-tools"
        assert agent._discovery_config["use_mcp"] is False

    def test_create_with_rag_tooling_factory(self):
        """Test factory method for creating agent with RAG-based tool discovery."""
        documents = [
            "Python has many useful libraries for data analysis like pandas and numpy.",
            "For web scraping, you can use requests and BeautifulSoup.",
            "Matplotlib and seaborn are great for data visualization.",
            "Calculator tools are useful for mathematical operations.",
        ]

        agent = DynamicReactAgent.create_with_rag_tooling(
            name="rag_agent",
            engine=AugLLMConfig(),
            rag_documents=documents,
            use_mcp=False,
        )

        assert agent.name == "rag_agent"
        assert hasattr(agent, "_rag_config")
        assert agent._rag_config["rag_documents"] == documents
        assert agent._rag_config["use_mcp"] is False

    def test_dynamic_tool_discovery_tool_functionality(self):
        """Test that the dynamic tool discovery tool works properly."""
        # Create agent with some initial tools
        tools = [
            {
                "id": "calc",
                "name": "Calculator",
                "description": "Mathematical calculations",
                "component": calculator,
                "category": "math",
            }
        ]

        agent = DynamicReactAgent.create_with_tools(
            name="discovery_test_agent", tools=tools, engine=AugLLMConfig()
        )

        # Setup agent to initialize the discovery tool
        agent.setup_agent()

        # Verify the discovery tool was added
        engine_tools = agent.engine.tools
        discovery_tool = None

        for tool in engine_tools:
            if hasattr(tool, "name") and "discover_and_load_tools" in tool.name:
                discovery_tool = tool
                break

        assert (
            discovery_tool is not None
        ), "Dynamic tool discovery tool should be added to engine"

        # Test the discovery tool functionality
        # Since we don't have a real discovery agent, it should return an appropriate message
        result = discovery_tool.invoke(
            {"task_description": "mathematical calculations"}
        )
        assert isinstance(result, str)
        assert (
            "discovery" in result.lower()
            or "tool" in result.lower()
            or "available" in result.lower()
        )

    @pytest.mark.asyncio
    async def test_discover_and_load_tools_method(self):
        """Test the discover_and_load_tools method with real components."""
        # Create agent with basic setup
        agent = DynamicReactAgent(name="discovery_method_test", engine=AugLLMConfig())

        # Setup agent
        agent.setup_agent()

        # Test discover_and_load_tools method
        # Since we don't have a discovery agent, this should return empty list
        tools = await agent.discover_and_load_tools("data processing")
        assert isinstance(tools, list)
        # Should be empty since no discovery agent is configured
        assert len(tools) == 0

    def test_tool_management_methods(self):
        """Test tool management methods like categorization and usage tracking."""
        agent = DynamicReactAgent(name="management_test", engine=AugLLMConfig())

        # Setup agent
        agent.setup_agent()

        # Create a mock state for testing
        # In real usage, this would be handled by the workflow
        # Since we can't assign to state directly, we'll test the methods differently
        # Let's just test that the methods exist and work with a proper state instance
        state = DynamicToolState()

        # Test tool categorization using the state instance
        state.categorize_tool("calculator", "math")
        math_tools = state.get_tools_by_category("math")
        assert "calculator" in math_tools

        # Test tool usage statistics
        state.track_tool_usage("calculator")
        stats = state.get_tool_usage_stats()
        assert stats.get("calculator") == 1

        # Test registry statistics
        registry_stats = state.get_activation_stats()
        assert isinstance(registry_stats, dict)
        assert "total_components" in registry_stats

    def test_agent_has_dynamic_tool_discovery_capability(self):
        """Test that the agent has the capability to discover tools dynamically."""
        agent = DynamicReactAgent(name="capability_test", engine=AugLLMConfig())

        # Setup agent
        agent.setup_agent()

        # Verify the agent has discovery capabilities
        assert hasattr(agent, "discover_and_load_tools")
        assert callable(agent.discover_and_load_tools)

        # Verify the agent has tool management capabilities
        assert hasattr(agent, "categorize_tool")
        assert hasattr(agent, "get_tools_by_category")
        assert hasattr(agent, "get_tool_usage_stats")
        assert hasattr(agent, "activate_tool_by_name")
        assert hasattr(agent, "deactivate_tool_by_name")

        # Verify the agent has the discovery tool in its engine
        engine_tools = agent.engine.tools
        has_discovery_tool = any(
            hasattr(tool, "name") and "discover_and_load_tools" in tool.name
            for tool in engine_tools
        )
        assert has_discovery_tool, "Agent should have dynamic tool discovery tool"

    def test_recompilation_mixin_integration(self):
        """Test that the agent integrates with recompilation mixin for dynamic updates."""
        tools = [
            {
                "id": "calc",
                "name": "Calculator",
                "description": "Mathematical calculations",
                "component": calculator,
                "category": "math",
            }
        ]

        agent = DynamicReactAgent.create_with_tools(
            name="recompilation_test", tools=tools, engine=AugLLMConfig()
        )

        # Setup agent
        agent.setup_agent()

        # Verify MetaStateSchema wrapper exists
        assert hasattr(agent, "_meta_self")
        assert agent._meta_self is not None

        # Verify recompilation context
        if agent._meta_self:
            context = agent._meta_self.graph_context
            assert context.get("recompilation_enabled") is True
            assert context.get("tool_discovery") is True
            assert context.get("agent_type") == "dynamic_react"

    def test_tool_inference_and_categorization(self):
        """Test tool category inference based on task descriptions."""
        agent = DynamicReactAgent(name="inference_test", engine=AugLLMConfig())

        # Test category inference
        math_category = agent._infer_tool_category(
            "calculate compound interest",
            {"name": "calculator", "description": "math tool"},
        )
        assert math_category == "math"

        web_category = agent._infer_tool_category(
            "search for information online",
            {"name": "web_search", "description": "search tool"},
        )
        assert web_category == "web"

        file_category = agent._infer_tool_category(
            "read file contents",
            {"name": "file_reader", "description": "file operations"},
        )
        assert file_category == "file"

        viz_category = agent._infer_tool_category(
            "create a chart", {"name": "plotter", "description": "visualization tool"}
        )
        assert viz_category == "visualization"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
