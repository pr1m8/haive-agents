from typing import Any
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, model_validator
from haive.agents import tools
from haive.agents.simple.config import SimpleAgentConfig


class StructuredOutputAgentConfig(SimpleAgentConfig):
    """Configuration for a structured output agent.

    Automatically sets up a single StructuredOutputTool for the provided model
    and configures the engine to always use this tool.
    """

    structured_output_model: type[BaseModel]
    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(force_tool_use=True, force_tool_choice=True)
    )
    output_parser: PydanticOutputParser = Field(default_factory=lambda: PydanticOutputParser())
    output_schema = structured_output_model

    @model_validator(mode="after")
    def validate_and_setup(self) -> Any:
        """Set up the structured output tool and configure the engine."""
        output_tool = tools.StructuredOutputTool(self.structured_output_model)
        self.engine.tools = [output_tool]
        self.engine.structured_output_model = self.structured_output_model
        if hasattr(output_tool, "name"):
            self.engine.force_tool_choice = output_tool.name
        elif hasattr(output_tool, "id"):
            self.engine.force_tool_choice = output_tool.id
        else:
            raise ValueError("StructuredOutputTool must have a name or id attribute")
        self.output_parser = PydanticOutputParser(pydantic_object=self.structured_output_model)
        if len(self.engine.tools) != 1:
            raise ValueError(f"Expected exactly one tool, but got {len(self.engine.tools)}")
        return self
