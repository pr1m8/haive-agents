"""Structured output agent implementation.

This module provides the StructuredOutputAgent that converts any agent's output
into structured formats using Pydantic models and tool-based extraction.
"""

from typing import Any

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.structured.models import GenericStructuredOutput
from haive.agents.structured.prompts import get_prompt_for_model


class StructuredOutputAgent(SimpleAgent):
    """Agent that converts any input into structured output.

    This agent specializes in taking unstructured text (typically from another
    agent's output) and converting it into a well-defined Pydantic model structure.
    It always uses tool-based structured output (v2) for reliable extraction.

    The agent can be used in multi-agent workflows where you need to:
    - Convert free-form agent responses into structured data
    - Extract specific fields from complex outputs
    - Ensure type-safe data flow between agents
    - Create consistent output formats across different agent types

    Examples:
        Basic usage with generic output::

            agent = StructuredOutputAgent(
                name="structurer",
                output_model=GenericStructuredOutput
            )
            result = agent.run("Some unstructured text...")

        Custom output model::

            class CustomOutput(BaseModel):
                title: str
                points: List[str]
                score: float

            agent = StructuredOutputAgent(
                name="custom_structurer",
                output_model=CustomOutput,
                custom_context="Focus on extracting title and scoring"
            )

        In multi-agent workflow::

            # Any agent produces unstructured output
            react_agent = ReactAgent(name="analyzer", ...)

            # StructuredOutputAgent converts it
            structurer = StructuredOutputAgent(
                name="structurer",
                output_model=AnalysisOutput
            )

            # Add both to workflow
            agents = [react_agent, structurer]
    """

    # Override structured_output_model to be required
    structured_output_model: type[BaseModel] = Field(
        ..., description="The Pydantic model to structure output into"
    )

    # Additional fields
    output_model: type[BaseModel] = Field(
        default=GenericStructuredOutput,
        description="Alias for structured_output_model for clarity",
    )

    custom_context: str | None = Field(
        default=None, description="Additional context for extraction"
    )

    custom_prompt: ChatPromptTemplate | None = Field(
        default=None, description="Custom prompt template (overrides default)"
    )

    def model_post_init(self, __context: Any) -> None:
        """Initialize the agent after Pydantic initialization."""
        # Mark this as a structured output handler to prevent wrapping
        self._is_structured_output_handler = True

        # Ensure structured_output_model is set from output_model if needed
        if not self.structured_output_model and self.output_model:
            self.structured_output_model = self.output_model

        # Configure engine for structured output
        if not self.engine:
            self.engine = AugLLMConfig()

        # Ensure we always use v2 (tool-based)
        self.engine.structured_output_version = "v2"
        # Also ensure the engine has the structured output model
        if not self.engine.structured_output_model:
            self.engine.structured_output_model = self.structured_output_model

        # Set up the prompt
        if not self.custom_prompt:
            model_name = self.structured_output_model.__name__
            self.prompt_template = get_prompt_for_model(model_name, self.custom_context)
        else:
            self.prompt_template = self.custom_prompt

        # Set low temperature for consistent extraction
        if self.engine.temperature is None:
            self.engine.temperature = 0.1

        # Update system message if not custom
        if not self.engine.system_message and not self.custom_prompt:
            self.engine.system_message = """You are a structured output converter.
Extract and organize information from input text into the required structured format.
Be thorough and accurate in your extraction."""

        # Call parent initialization
        super().model_post_init(__context)

    def extract_from_messages(self, messages: list) -> Any:
        """Extract structured output from a list of messages.

        This is useful when processing conversation history or
        multiple agent outputs.

        Args:
            messages: List of messages to process

        Returns:
            Structured output matching the output_model
        """
        # Convert messages to text
        if not messages:
            return self.run("No messages provided")

        # Get the last message content
        last_message = messages[-1]
        content = (
            last_message.content
            if hasattr(last_message, "content")
            else str(last_message)
        )

        return self.run(content)

    def extract_from_state(self, state: Any) -> Any:
        """Extract structured output from agent state.

        This is useful in multi-agent workflows where you need
        to structure another agent's output from the shared state.

        Args:
            state: Agent state containing messages

        Returns:
            Structured output matching the output_model
        """
        if hasattr(state, "messages") and state.messages:
            return self.extract_from_messages(state.messages)
        return self.run("No messages found in state")


def create_structured_agent(
    output_model: type[BaseModel],
    name: str = "structured_output",
    temperature: float = 0.1,
    custom_context: str | None = None,
    **kwargs,
) -> StructuredOutputAgent:
    """Factory function to create a structured output agent.

    This is a convenience function for creating structured agents
    with common configurations.

    Args:
        output_model: The Pydantic model for output structure
        name: Agent name (defaults to "structured_output")
        temperature: LLM temperature (defaults to 0.1 for consistency)
        custom_context: Additional extraction context
        **kwargs: Additional arguments passed to StructuredOutputAgent

    Returns:
        Configured StructuredOutputAgent

    Examples:
        Basic creation::

            agent = create_structured_agent(
                output_model=TaskOutput,
                name="task_structurer"
            )

        With custom context::

            agent = create_structured_agent(
                output_model=GenericStructuredOutput,
                custom_context="Focus on technical details",
                temperature=0.2
            )
    """
    engine = AugLLMConfig(temperature=temperature)

    return StructuredOutputAgent(
        name=name,
        engine=engine,
        output_model=output_model,
        structured_output_model=output_model,
        custom_context=custom_context,
        **kwargs,
    )


# Rebuild model to resolve forward references
try:
    import sys
    if 'sphinx' not in sys.modules and 'autoapi' not in sys.modules:
        StructuredOutputAgent.model_rebuild()
except Exception:
    pass
