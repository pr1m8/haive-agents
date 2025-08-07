#!/usr/bin/env python3
"""Best practices for handling AddableValuesDict return type in LangGraph.

This module demonstrates multiple approaches to handle structured output
when LangGraph returns AddableValuesDict.

Date: August 7, 2025
"""

import asyncio
from typing import Any, Generic, List, Optional, TypeVar

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured output models
class AnalysisResult(BaseModel):
    """Analysis result with structured fields."""

    topic: str = Field(description="Topic being analyzed")
    findings: List[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendation: str = Field(description="Main recommendation")


class TaskResult(BaseModel):
    """Task execution result."""

    task_id: str = Field(description="Unique task identifier")
    status: str = Field(description="Task status: success/failed/pending")
    output: str = Field(description="Task output")
    metadata: dict = Field(default_factory=dict, description="Additional metadata")


# Type variable for generic structured output
T = TypeVar("T", bound=BaseModel)


class StructuredOutputExtractor(Generic[T]):
    """Helper class to extract structured output from AddableValuesDict.

    This class provides a clean interface for handling LangGraph's
    AddableValuesDict return type and extracting structured output.
    """

    def __init__(self, output_model: type[T], field_name: Optional[str] = None):
        """Initialize the extractor.

        Args:
            output_model: The Pydantic model class for structured output
            field_name: Optional field name to extract (auto-detected if None)
        """
        self.output_model = output_model
        self.field_name = field_name or self._generate_field_name()

    def _generate_field_name(self) -> str:
        """Generate field name from model name."""
        # Convert CamelCase to snake_case
        import re

        name = self.output_model.__name__
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
        return name

    def extract(self, result: Any) -> Optional[T]:
        """Extract structured output from result.

        Args:
            result: The AddableValuesDict or dict-like result from LangGraph

        Returns:
            The extracted structured output or None if not found
        """
        if isinstance(result, dict):
            # Try the configured field name
            if self.field_name in result:
                value = result[self.field_name]
                if isinstance(value, self.output_model):
                    return value

            # Try common field names
            for field in [
                "analysis_result",
                "task_result",
                "structured_output",
                "output",
            ]:
                if field in result:
                    value = result[field]
                    if isinstance(value, self.output_model):
                        return value

            # Check all fields for the model type
            for key, value in result.items():
                if isinstance(value, self.output_model):
                    return value

        return None

    def extract_or_raise(self, result: Any) -> T:
        """Extract structured output or raise an error.

        Args:
            result: The AddableValuesDict or dict-like result

        Returns:
            The extracted structured output

        Raises:
            ValueError: If structured output not found
        """
        output = self.extract(result)
        if output is None:
            raise ValueError(
                f"Could not find {self.output_model.__name__} in result. "
                f"Available keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
            )
        return output


def create_structured_agent_wrapper(
    agent_class: type, output_model: type[BaseModel], **agent_kwargs
) -> tuple[Any, StructuredOutputExtractor]:
    """Create an agent with structured output and its extractor.

    This factory function creates both the agent and a corresponding
    extractor for clean structured output handling.

    Args:
        agent_class: The agent class to instantiate
        output_model: The Pydantic model for structured output
        **agent_kwargs: Arguments to pass to the agent constructor

    Returns:
        Tuple of (agent, extractor)
    """
    # Ensure structured_output_model is set
    agent_kwargs["structured_output_model"] = output_model

    # Create agent
    agent = agent_class(**agent_kwargs)

    # Create extractor
    extractor = StructuredOutputExtractor(output_model)

    return agent, extractor


# Convenience functions for common patterns
async def run_with_structured_output(
    agent: Any, input_data: dict, output_model: type[T]
) -> T:
    """Run agent and extract structured output.

    Args:
        agent: The agent to run
        input_data: Input data for the agent
        output_model: Expected output model type

    Returns:
        The extracted structured output

    Raises:
        ValueError: If structured output not found
    """
    extractor = StructuredOutputExtractor(output_model)
    result = await agent.arun(input_data)
    return extractor.extract_or_raise(result)


# Example: Agent with built-in extraction
class StructuredAgent(SimpleAgentV3):
    """Agent that automatically extracts structured output."""

    structured_output_model: type[BaseModel] = Field(
        ..., description="The structured output model"
    )

    async def arun_structured(self, input_data: dict) -> BaseModel:
        """Run and return structured output directly.

        Args:
            input_data: Input data for the agent

        Returns:
            The structured output model instance
        """
        result = await self.arun(input_data)
        extractor = StructuredOutputExtractor(self.structured_output_model)
        return extractor.extract_or_raise(result)


# Tool for examples
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Error: Invalid expression"


async def example_1_basic_extraction():
    """Example 1: Basic extraction pattern."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Basic Extraction Pattern")
    print("=" * 60)

    # Create agent with structured output
    agent = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Create extractor
    extractor = StructuredOutputExtractor(AnalysisResult)

    # Run agent
    result = await agent.arun(
        {"messages": [HumanMessage(content="Analyze AI productivity impact")]}
    )

    # Extract structured output
    analysis = extractor.extract(result)

    if analysis:
        print(f"✅ Extracted Analysis:")
        print(f"   Topic: {analysis.topic}")
        print(f"   Confidence: {analysis.confidence}")
        print(f"   Findings: {len(analysis.findings)} items")
    else:
        print("❌ Failed to extract analysis")


async def example_2_factory_pattern():
    """Example 2: Factory pattern with automatic extraction."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Factory Pattern")
    print("=" * 60)

    # Create agent and extractor together
    agent, extractor = create_structured_agent_wrapper(
        ReactAgentV4,
        output_model=TaskResult,
        name="task_executor",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator],
    )

    # Run agent
    result = await agent.arun(
        {"messages": [HumanMessage(content="Execute task: Calculate 15% of 200")]}
    )

    # Extract with error handling
    try:
        task_result = extractor.extract_or_raise(result)
        print(f"✅ Task Completed:")
        print(f"   ID: {task_result.task_id}")
        print(f"   Status: {task_result.status}")
        print(f"   Output: {task_result.output}")
    except ValueError as e:
        print(f"❌ Extraction failed: {e}")


async def example_3_convenience_function():
    """Example 3: One-line convenience function."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Convenience Function")
    print("=" * 60)

    # Create agent
    agent = SimpleAgentV3(
        name="reporter",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Run and extract in one line
    analysis = await run_with_structured_output(
        agent,
        {"messages": [HumanMessage(content="Report on cloud computing trends")]},
        AnalysisResult,
    )

    print(f"✅ Direct extraction successful:")
    print(f"   Topic: {analysis.topic}")
    print(f"   Recommendation: {analysis.recommendation}")


async def example_4_custom_agent():
    """Example 4: Custom agent with built-in extraction."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Custom Agent with Built-in Extraction")
    print("=" * 60)

    # Create custom agent
    agent = StructuredAgent(
        name="smart_analyzer",
        engine=AugLLMConfig(temperature=0.1),
        structured_output_model=AnalysisResult,
    )

    # Use the custom method that returns structured output directly
    analysis = await agent.arun_structured(
        {"messages": [HumanMessage(content="Analyze blockchain impact on finance")]}
    )

    print(f"✅ Direct structured output:")
    print(f"   Type: {type(analysis).__name__}")
    print(f"   Topic: {analysis.topic}")
    print(f"   Confidence: {analysis.confidence}")


async def main():
    """Run all examples."""
    print("🔧 HANDLING AddableValuesDict - Best Practices")
    print("=" * 60)
    print("Demonstrating multiple approaches to handle LangGraph's")
    print("AddableValuesDict return type for structured output.")

    # Run examples
    await example_1_basic_extraction()
    await example_2_factory_pattern()
    await example_3_convenience_function()
    await example_4_custom_agent()

    print("\n" + "=" * 60)
    print("💡 KEY TAKEAWAYS")
    print("=" * 60)
    print("1. LangGraph always returns AddableValuesDict (dict-like)")
    print("2. Structured output is nested inside as a field")
    print("3. Use StructuredOutputExtractor for clean extraction")
    print("4. Create wrapper functions for convenience")
    print("5. Consider custom agent classes for repeated patterns")


if __name__ == "__main__":
    import os

    os.environ["HAIVE_LOG_LEVEL"] = "ERROR"
    asyncio.run(main())
