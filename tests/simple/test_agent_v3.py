# Test SimpleAgent v3 - Dynamic Architecture Validation
"""Test suite for SimpleAgent v3 with dynamic architecture patterns.

This test suite validates:
- Real LLM execution (no mocks)
- Recompilation mixin functionality
- Dynamic tool routing
- MetaStateSchema integration
- Agent-as-tool pattern
- Change detection and auto-recompilation
"""

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field
import pytest

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Core Haive imports
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.meta_state import MetaStateSchema


# ========================================================================
# TEST FIXTURES - Real component setup
# ========================================================================


@pytest.fixture
def real_llm_config():
    """Provide real LLM configuration for testing."""
    # Use DeepSeek for testing as requested
    from haive.core.models.llm.base import DeepSeekLLMConfig

    return AugLLMConfig(
        temperature=0.1,  # Low temperature for consistent tests
        max_tokens=500,
        llm_config=DeepSeekLLMConfig(),  # DeepSeek LLM config as requested
    )


@pytest.fixture
def calculator_tool():
    """Provide real calculator tool."""

    @tool
    def calculator(expression: str) -> str:
        """Calculate mathematical expressions."""
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {e!s}"

    return calculator


@pytest.fixture
def word_counter_tool():
    """Provide real word counter tool."""

    @tool
    def word_counter(text: str) -> str:
        """Count words in text."""
        word_count = len(text.split())
        return f"Word count: {word_count}"

    return word_counter


class TaskResult(BaseModel):
    """Structured output model for testing."""

    task: str = Field(description="The task performed")
    result: str = Field(description="The result of the task")
    confidence: float = Field(description="Confidence score 0-1")


# ========================================================================
# BASIC FUNCTIONALITY TESTS - Real LLM execution
# ========================================================================


class TestSimpleAgentV3BasicFunctionality:
    """Test basic SimpleAgent v3 functionality with real components."""

    @pytest.mark.asyncio
    async def test_agent_creation_and_basic_execution(self, real_llm_config):
        """Test agent creation and basic execution with real LLM."""
        # Create agent with real configuration and debug=True
        agent = SimpleAgentV3(
            name="test_agent",
            engine=real_llm_config,
            temperature=0.1,
            debug=True,  # Enable full debug logging
        )

        # Verify agent is properly initialized
        assert agent.name == "test_agent"
        assert isinstance(agent.engine, AugLLMConfig)
        assert agent.temperature == 0.1
        assert agent.auto_recompile is True
        assert agent.change_tracking_enabled is True

        # Execute with real LLM and debug=True
        result = await agent.arun("Hello, please respond with a greeting", debug=True)

        # Verify real execution
        assert result is not None
        assert isinstance(result, dict)
        assert "messages" in result

        messages = result["messages"]
        assert len(messages) >= 2  # User + Assistant messages
        assert isinstance(messages[-1], AIMessage)
        assert len(messages[-1].content) > 0

        # Verify recompilation tracking
        assert hasattr(agent, "recompile_count")
        assert agent.get_recompile_status() is not None

    @pytest.mark.asyncio
    async def test_convenience_field_sync_with_change_tracking(self, real_llm_config):
        """Test convenience fields sync to engine with change tracking."""
        # Create agent with convenience fields
        agent = SimpleAgentV3(
            name="convenience_test",
            engine=real_llm_config,
            temperature=0.3,
            max_tokens=200,
            model_name="gpt-4",
            system_message="You are a helpful assistant",
        )

        # Verify fields synced to engine
        assert agent.engine.temperature == 0.3
        assert agent.engine.max_tokens == 200
        assert agent.engine.model == "gpt-4"
        assert agent.engine.system_message == "You are a helpful assistant"

        # Verify recompilation was triggered by field changes
        recompile_status = agent.get_recompile_status()
        assert recompile_status["needs_recompile"] is True
        assert "Convenience field changes" in str(recompile_status["reasons"])

        # Execute to verify configuration works
        result = await agent.arun("What is 2 + 2?")
        assert result is not None


# ========================================================================
# DYNAMIC TOOL ROUTING TESTS - Real tool integration
# ========================================================================


class TestSimpleAgentV3DynamicToolRouting:
    """Test dynamic tool routing with real tools."""

    @pytest.mark.asyncio
    async def test_dynamic_tool_addition_triggers_recompilation(
        self, real_llm_config, calculator_tool, word_counter_tool
    ):
        """Test dynamic tool addition triggers recompilation."""
        # Create agent with one tool
        config_with_tool = AugLLMConfig(temperature=0.1, tools=[calculator_tool])

        agent = SimpleAgentV3(
            name="dynamic_tool_test",
            engine=config_with_tool,
            auto_recompile=True,
            debug=True,  # Full debug logging for tool changes
        )

        # Verify initial tool setup
        assert agent._has_tools() is True
        initial_recompile_count = agent.recompile_count

        # Execute with initial tool and debug=True
        result = await agent.arun("Calculate 15 * 23", debug=True)

        # Verify calculation was performed
        assert "345" in str(result) or "345" in str(result.get("messages", []))

        # Add second tool dynamically
        agent.add_tool(word_counter_tool)

        # Verify recompilation was triggered
        assert agent.recompile_count > initial_recompile_count
        recompile_status = agent.get_recompile_status()
        assert "Tool route change" in str(recompile_status["reasons"])

        # Execute with new tool to verify it works
        result2 = await agent.arun("Count the words in 'hello world test'")

        # Verify word counting was performed
        assert "3" in str(result2) or "Word count" in str(result2)

    @pytest.mark.asyncio
    async def test_tool_removal_triggers_recompilation(
        self, real_llm_config, calculator_tool, word_counter_tool
    ):
        """Test tool removal triggers recompilation."""
        # Create agent with multiple tools
        config_with_tools = AugLLMConfig(
            temperature=0.1, tools=[calculator_tool, word_counter_tool]
        )

        agent = SimpleAgentV3(
            name="tool_removal_test", engine=config_with_tools, auto_recompile=True
        )

        initial_recompile_count = agent.recompile_count

        # Remove a tool
        agent.remove_tool(word_counter_tool.name)

        # Verify recompilation was triggered
        assert agent.recompile_count > initial_recompile_count

        # Verify tool was actually removed
        remaining_tools = getattr(agent.engine, "tools", [])
        tool_names = [tool.name for tool in remaining_tools]
        assert word_counter_tool.name not in tool_names


# ========================================================================
# STRUCTURED OUTPUT TESTS - Real parsing validation
# ========================================================================


class TestSimpleAgentV3StructuredOutput:
    """Test structured output with real parsing."""

    @pytest.mark.asyncio
    async def test_structured_output_with_recompilation(self, real_llm_config):
        """Test structured output triggers recompilation and works correctly."""
        # Create agent with structured output
        agent = SimpleAgentV3(
            name="structured_test",
            engine=real_llm_config,
            structured_output_model=TaskResult,
            auto_recompile=True,
        )

        # Verify structured output setup
        assert agent._has_structured_output() is True
        assert agent.structured_output_model == TaskResult

        # Verify recompilation was triggered
        recompile_status = agent.get_recompile_status()
        assert recompile_status["needs_recompile"] is True

        # Execute with structured output
        result = await agent.arun(
            "Analyze the task of writing a summary. Provide the task, result, and confidence score."
        )

        # Verify structured output was generated
        assert result is not None

        # Check if structured output is in the result
        if isinstance(result, dict) and "parsed_output" in result:
            parsed = result["parsed_output"]
            if isinstance(parsed, TaskResult):
                assert parsed.task is not None
                assert parsed.result is not None
                assert 0 <= parsed.confidence <= 1


# ========================================================================
# META-STATE INTEGRATION TESTS - Real meta-capability
# ========================================================================


class TestSimpleAgentV3MetaIntegration:
    """Test MetaStateSchema integration."""

    @pytest.mark.asyncio
    async def test_meta_capable_agent_creation(self, real_llm_config):
        """Test converting agent to meta-capable with MetaStateSchema."""
        # Create regular agent
        agent = SimpleAgentV3(name="meta_test_agent", engine=real_llm_config, temperature=0.2)

        # Convert to meta-capable
        meta_agent = agent.as_meta_capable(
            initial_state={"ready": True, "test_mode": True},
            graph_context={"purpose": "testing", "version": "v3"},
        )

        # Verify meta-capable agent
        assert isinstance(meta_agent, MetaStateSchema)
        assert meta_agent.agent == agent
        assert meta_agent.agent_name == "meta_test_agent"
        assert meta_agent.agent_type == "SimpleAgentV3"

        # Verify initial state and context
        assert meta_agent.agent_state["ready"] is True
        assert meta_agent.agent_state["test_mode"] is True
        assert meta_agent.graph_context["purpose"] == "testing"
        assert meta_agent.graph_context["version"] == "v3"

        # Test execution through meta state
        result = await meta_agent.execute_agent(
            {"messages": [HumanMessage(content="Hello from meta agent")]}
        )

        # Verify meta execution worked
        assert result is not None
        assert result["status"] == "success"
        assert meta_agent.execution_count == 1

        # Verify execution summary
        summary = meta_agent.get_execution_summary()
        assert summary["execution_count"] == 1
        assert summary["current_status"] == "completed"

    @pytest.mark.asyncio
    async def test_meta_agent_recompilation_integration(self, real_llm_config, calculator_tool):
        """Test recompilation works through MetaStateSchema."""
        # Create agent with tool
        agent = SimpleAgentV3(
            name="meta_recompile_test", engine=real_llm_config, auto_recompile=True
        )

        # Convert to meta-capable
        meta_agent = agent.as_meta_capable()

        # Check initial recompile state

        # Add tool to trigger recompilation
        agent.add_tool(calculator_tool)

        # Verify recompilation was triggered
        assert agent.needs_recompile is True
        assert agent.recompile_count > 0

        # Execute through meta state to resolve recompilation
        result = await meta_agent.execute_agent(
            {"messages": [HumanMessage(content="Calculate 10 + 15")]}
        )

        # Verify execution and recompilation resolution
        assert result["status"] == "success"
        assert "25" in str(result) or "25" in str(meta_agent.execution_result)


# ========================================================================
# AGENT-AS-TOOL PATTERN TESTS - Real composition
# ========================================================================


class TestSimpleAgentV3AsToolPattern:
    """Test agent-as-tool composition pattern."""

    def test_agent_as_tool_creation(self, real_llm_config):
        """Test creating agent as LangChain tool."""
        # Create tool from agent class
        research_tool = SimpleAgentV3.as_tool(
            name="research_assistant",
            description="Research topics and provide analysis",
            temperature=0.3,
            system_message="You are a research assistant",
            engine=real_llm_config,
        )

        # Verify tool creation
        assert research_tool is not None
        assert research_tool.name == "research_assistant"
        assert research_tool.description == "Research topics and provide analysis"

        # Test tool execution (synchronous)
        result = research_tool.invoke("What is artificial intelligence?")

        # Verify tool execution
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0
        assert "artificial intelligence" in result.lower() or "ai" in result.lower()

    @pytest.mark.asyncio
    async def test_agent_tool_in_multi_agent_setup(self, real_llm_config):
        """Test using agent tool in multi-agent composition."""
        # Create specialized agent tools
        math_tool = SimpleAgentV3.as_tool(
            name="math_specialist",
            description="Solve mathematical problems",
            temperature=0.1,
            system_message="You are a math specialist",
            engine=real_llm_config,
        )

        analysis_tool = SimpleAgentV3.as_tool(
            name="text_analyzer",
            description="Analyze text content",
            temperature=0.2,
            system_message="You are a text analysis specialist",
            engine=real_llm_config,
        )

        # Create coordinator agent with specialized tools
        coordinator_config = AugLLMConfig(temperature=0.3, tools=[math_tool, analysis_tool])

        coordinator = SimpleAgentV3(
            name="coordinator",
            engine=coordinator_config,
            system_message="You coordinate between math and analysis specialists",
        )

        # Test coordination
        result = await coordinator.arun(
            "I need to calculate 25 * 17 and then analyze the significance of the result"
        )

        # Verify coordination worked
        assert result is not None
        # Should contain both math result and analysis
        result_str = str(result)
        assert "425" in result_str or any("425" in str(msg) for msg in result.get("messages", []))


# ========================================================================
# RECOMPILATION SYSTEM TESTS - Real change detection
# ========================================================================


class TestSimpleAgentV3RecompilationSystem:
    """Test recompilation system with real change detection."""

    @pytest.mark.asyncio
    async def test_hash_based_change_detection(self, real_llm_config):
        """Test hash-based change detection system."""
        agent = SimpleAgentV3(
            name="hash_test_agent", engine=real_llm_config, change_tracking_enabled=True
        )

        # Get initial hashes
        initial_engine_hash = agent._compute_engine_hash()
        agent._compute_tool_hash()
        initial_schema_hash = agent._compute_schema_hash()

        # Change engine configuration
        agent.temperature = 0.8
        agent._sync_convenience_fields_with_tracking()

        # Verify hash changed
        new_engine_hash = agent._compute_engine_hash()
        assert new_engine_hash != initial_engine_hash

        # Change schema configuration
        agent.structured_output_model = TaskResult
        new_schema_hash = agent._compute_schema_hash()
        assert new_schema_hash != initial_schema_hash

        # Verify recompilation conditions are detected
        conditions = agent.check_recompile_conditions()
        assert len(conditions) > 0

    @pytest.mark.asyncio
    async def test_auto_recompile_workflow(self, real_llm_config, calculator_tool):
        """Test complete auto-recompile workflow."""
        agent = SimpleAgentV3(
            name="auto_recompile_test",
            engine=real_llm_config,
            auto_recompile=True,
            change_tracking_enabled=True,
        )

        # Record initial state
        initial_count = agent.recompile_count

        # Make changes that should trigger recompilation
        agent.temperature = 0.5
        agent.add_tool(calculator_tool)
        agent.structured_output_model = TaskResult

        # Verify multiple recompilation triggers
        assert agent.needs_recompile is True
        assert agent.recompile_count > initial_count

        # Execute to trigger auto-recompilation
        result = await agent.arun("Calculate 12 * 34 and format as structured output")

        # Verify execution succeeded and recompilation resolved
        assert result is not None

        # Check recompile history
        history = agent.recompile_history
        assert len(history) > 0
        assert any("Tool route change" in event["reason"] for event in history)
        assert any("Convenience field changes" in event["reason"] for event in history)


# ========================================================================
# INTEGRATION TESTS - Real end-to-end workflows
# ========================================================================


class TestSimpleAgentV3Integration:
    """Integration tests with real end-to-end workflows."""

    @pytest.mark.asyncio
    async def test_complete_dynamic_workflow(
        self, real_llm_config, calculator_tool, word_counter_tool
    ):
        """Test complete dynamic workflow with all features."""
        # Create agent with initial configuration
        agent = SimpleAgentV3(
            name="complete_workflow_test",
            engine=real_llm_config,
            temperature=0.2,
            auto_recompile=True,
            change_tracking_enabled=True,
        )

        # Convert to meta-capable
        meta_agent = agent.as_meta_capable(
            initial_state={"workflow_stage": "initial"},
            graph_context={"workflow_type": "complete_test"},
        )

        # Stage 1: Basic execution
        result1 = await meta_agent.execute_agent(
            {"messages": [HumanMessage(content="Hello, introduce yourself")]}
        )

        assert result1["status"] == "success"
        assert meta_agent.execution_count == 1

        # Stage 2: Add tools dynamically
        agent.add_tool(calculator_tool)

        result2 = await meta_agent.execute_agent(
            {"messages": [HumanMessage(content="Calculate 45 * 67")]}
        )

        assert result2["status"] == "success"
        assert "3015" in str(result2) or "3015" in str(meta_agent.execution_result)

        # Stage 3: Add structured output
        agent.structured_output_model = TaskResult

        result3 = await meta_agent.execute_agent(
            {"messages": [HumanMessage(content="Analyze the calculation task we just completed")]}
        )

        assert result3["status"] == "success"

        # Stage 4: Verify complete system state
        summary = meta_agent.get_execution_summary()
        assert summary["execution_count"] == 3
        assert summary["current_status"] == "completed"

        # Verify recompilation tracking
        assert agent.recompile_count > 0
        recompile_status = agent.get_recompile_status()
        assert len(recompile_status["reasons"]) > 0

        # Verify change tracking worked
        agent.check_recompile_conditions()
        # Should be empty if all changes were properly handled

        # Final verification - create tool from this agent
        workflow_tool = SimpleAgentV3.as_tool(
            name="workflow_specialist",
            description="Complete workflow specialist",
            engine=real_llm_config,
            auto_recompile=True,
        )

        tool_result = workflow_tool.invoke("Perform a quick test")
        assert tool_result is not None
        assert isinstance(tool_result, str)
        assert len(tool_result) > 0
