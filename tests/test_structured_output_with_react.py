"""Test StructuredOutputAgent with ReactAgent using sequential multi-agent pattern."""

from typing import Any, Dict, List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.structured_output.agent import StructuredOutputAgent
from haive.agents.structured_output.models import (
    Analysis,
    SearchQuery,
    SearchResult,
    TaskResult,
)


# Define test models for structured output
class ResearchResult(BaseModel):
    """Structured research result from ReactAgent."""

    topic: str = Field(description="Research topic")
    findings: List[str] = Field(description="Key findings")
    sources: List[str] = Field(description="Sources consulted")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendations: List[str] = Field(description="Next steps or recommendations")


class CalculationResult(BaseModel):
    """Structured calculation result."""

    expression: str = Field(description="Original calculation expression")
    result: float = Field(description="Calculation result")
    steps: List[str] = Field(description="Calculation steps")
    method: str = Field(description="Method used")


# Create test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {str(e)}"


@tool
def search_tool(query: str) -> str:
    """Search for information (mock implementation for testing)."""
    # Mock search results
    mock_results = {
        "python": "Python is a high-level programming language known for its simplicity and readability.",
        "ai": "Artificial Intelligence (AI) refers to computer systems that can perform tasks requiring human intelligence.",
        "quantum": "Quantum computing uses quantum mechanics principles for computation.",
        "default": "Search results for your query.",
    }

    for key, value in mock_results.items():
        if key.lower() in query.lower():
            return value

    return mock_results["default"]


class TestStructuredOutputWithReact:
    """Test StructuredOutputAgent with ReactAgent integration."""

    def test_basic_react_with_structured_output(self):
        """Test basic ReactAgent enhanced with structured output."""
        # Create ReactAgent with tools
        react_agent = ReactAgent(
            name="research_agent",
            engine=AugLLMConfig(
                temperature=0.3,
                system_message="You are a research assistant with access to search and calculation tools.",
            ),
            tools=[search_tool, calculator],
        )

        # Enhance with structured output
        enhanced_agent = StructuredOutputAgent.enhance_agent(
            base_agent=react_agent,
            output_models=[ResearchResult, CalculationResult],
            name="enhanced_research_agent",
        )

        # Verify configuration
        assert enhanced_agent.name == "enhanced_research_agent"
        assert enhanced_agent.execution_mode == "sequential"
        assert len(enhanced_agent.agents) == 2
        assert "research_agent" in enhanced_agent.agents
        assert "research_agent_structured_output" in enhanced_agent.agents

    def test_react_calculation_with_structured_output(self):
        """Test ReactAgent doing calculations with structured output."""
        # Create ReactAgent
        calc_agent = ReactAgent(
            name="calculator_agent",
            engine=AugLLMConfig(
                temperature=0.1,
                system_message="You are a calculation assistant. Use the calculator tool for all calculations.",
            ),
            tools=[calculator],
        )

        # Create structured output processor
        structured_processor = StructuredOutputAgent.create_processor(
            output_models=[CalculationResult],
            name="calc_processor",
            system_message="Convert calculation results into structured CalculationResult format.",
        )

        # Test components exist
        assert calc_agent is not None
        assert structured_processor is not None
        assert structured_processor.output_models == [CalculationResult]

    def test_react_research_with_structured_output(self):
        """Test ReactAgent doing research with structured output."""
        # Create research agent
        research_agent = ReactAgent(
            name="researcher",
            engine=AugLLMConfig(
                temperature=0.5,
                system_message="Research topics using available tools and provide comprehensive results.",
            ),
            tools=[search_tool, calculator],
        )

        # Enhance with multiple output models
        enhanced = StructuredOutputAgent.enhance_agent(
            base_agent=research_agent,
            output_models=[ResearchResult, Analysis, TaskResult],
            include_original_input=True,
        )

        # Verify multi-agent structure
        assert enhanced.agents["researcher"] == research_agent
        assert "researcher_structured_output" in enhanced.agents

        # Verify state schema has structured output capability
        state = enhanced.state_schema()
        assert hasattr(state, "structured_output_models")
        assert hasattr(state, "parse_structured_outputs")

    def test_sequential_execution_pattern(self):
        """Test the sequential execution pattern of enhanced agent."""
        # Create base ReactAgent
        base_agent = ReactAgent(
            name="base_react", engine=AugLLMConfig(), tools=[search_tool]
        )

        # Enhance with structured output
        enhanced = StructuredOutputAgent.enhance_agent(
            base_agent=base_agent, output_models=[SearchQuery, SearchResult]
        )

        # Check execution mode and agents
        assert enhanced.execution_mode == "sequential"

        # Check agents are in correct order (ProperMultiAgent stores agents as a dict)
        agent_names = list(enhanced.agents.keys())
        assert "base_react" in agent_names
        assert "base_react_structured_output" in agent_names

        # Verify agents dictionary structure
        assert isinstance(enhanced.agents, dict)
        assert len(enhanced.agents) == 2

        # Verify each agent type
        assert isinstance(enhanced.agents["base_react"], ReactAgent)
        assert isinstance(
            enhanced.agents["base_react_structured_output"], StructuredOutputAgent
        )

    def test_state_schema_integration(self):
        """Test that state schema properly integrates structured output parsing."""
        # Create enhanced agent
        react_agent = ReactAgent(
            name="test_react", engine=AugLLMConfig(), tools=[calculator]
        )

        enhanced = StructuredOutputAgent.enhance_agent(
            base_agent=react_agent, output_models=[CalculationResult, Analysis]
        )

        # Create state instance
        state = enhanced.state_schema(messages=[], agents=enhanced.agents)

        # Verify structured output fields
        assert state.structured_output_models is not None
        assert state.parse_structured_outputs == True
        assert len(state.structured_output_models) == 2

        # Verify it has the parsing methods
        assert hasattr(state, "enable_structured_output_parsing")
        assert hasattr(state, "get_parsed_tool_calls")
        assert hasattr(state, "get_latest_structured_output")

    def test_custom_structured_processor(self):
        """Test creating custom structured output processors."""
        # Create reflection processor
        reflection_processor = StructuredOutputAgent.create_reflection_processor(
            reflection_models=[Analysis, TaskResult], name="reflect_processor"
        )

        assert reflection_processor.name == "reflect_processor"
        assert reflection_processor.output_models == [Analysis, TaskResult]
        assert "reflection" in reflection_processor.engine.system_message.lower()

        # Create validation processor
        validation_processor = StructuredOutputAgent.create_validation_processor(
            validation_models=[TaskResult], name="validate_processor"
        )

        assert validation_processor.name == "validate_processor"
        assert "validation" in validation_processor.engine.system_message.lower()
        assert validation_processor.engine.temperature == 0.0  # Deterministic

    def test_multi_model_support(self):
        """Test support for multiple output models in one agent."""
        # Create agent with multiple tools
        multi_tool_agent = ReactAgent(
            name="multi_tool", engine=AugLLMConfig(), tools=[search_tool, calculator]
        )

        # Enhance with multiple output models
        enhanced = StructuredOutputAgent.enhance_agent(
            base_agent=multi_tool_agent,
            output_models=[
                SearchQuery,
                SearchResult,
                CalculationResult,
                ResearchResult,
                Analysis,
            ],
        )

        # Verify all models are configured
        structured_agent = enhanced.agents["multi_tool_structured_output"]
        assert len(structured_agent.output_models) == 5

        # Verify state can handle all models
        state = enhanced.state_schema()
        assert len(state.structured_output_models) == 5

    @pytest.mark.asyncio
    async def test_async_execution_compatibility(self):
        """Test that enhanced agent works with async execution."""
        # Create async-compatible agent
        async_react = ReactAgent(
            name="async_react", engine=AugLLMConfig(), tools=[search_tool]
        )

        # Enhance
        enhanced = StructuredOutputAgent.enhance_agent(
            base_agent=async_react, output_models=[SearchResult]
        )

        # Verify async methods exist
        assert hasattr(enhanced, "arun")
        assert hasattr(enhanced.agents["async_react"], "arun")
        assert hasattr(enhanced.agents["async_react_structured_output"], "arun")

    def test_error_handling_configuration(self):
        """Test error handling in structured output processing."""
        # Create agent
        agent = ReactAgent(name="error_test", engine=AugLLMConfig(), tools=[calculator])

        # Create processor with error handling
        processor = StructuredOutputAgent.create_processor(
            output_models=[CalculationResult],
            fallback_on_error=True,  # Should fallback on parse errors
            name="error_processor",
        )

        assert processor.fallback_on_error == True

        # Test enhancement with error handling
        enhanced = StructuredOutputAgent.enhance_agent(
            base_agent=agent, output_models=[CalculationResult], fallback_on_error=True
        )

        structured_agent = enhanced.agents["error_test_structured_output"]
        assert structured_agent.fallback_on_error == True


if __name__ == "__main__":
    # Run basic tests
    test = TestStructuredOutputWithReact()

    print("Testing basic ReactAgent with structured output...")
    test.test_basic_react_with_structured_output()
    print("✅ Basic integration test passed")

    print("\nTesting calculation with structured output...")
    test.test_react_calculation_with_structured_output()
    print("✅ Calculation test passed")

    print("\nTesting research with structured output...")
    test.test_react_research_with_structured_output()
    print("✅ Research test passed")

    print("\nTesting sequential execution pattern...")
    test.test_sequential_execution_pattern()
    print("✅ Sequential pattern test passed")

    print("\nTesting state schema integration...")
    test.test_state_schema_integration()
    print("✅ State schema test passed")

    print("\nAll tests passed! ✅")
