import logging
from typing import Any, Literal
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, model_validator
from haive.agents.react_class.react.state import ReactAgentState
from haive.agents.simple.config import SimpleAgentConfig


class ReactAgentConfig(SimpleAgentConfig):
    """Configuration for React Agent, extending SimpleAgentConfig.

    React Agent routes between an LLM and tools to perform multi-step
    reasoning and action to accomplish tasks.
    """

    state_schema: type[BaseModel] = Field(default=ReactAgentState)
    tools: list[BaseTool | dict[str, Any]] = Field(
        default_factory=list, description="Tools available to the agent"
    )
    max_iterations: int = Field(
        default=10, description="Maximum number of iterations for the agent"
    )
    structured_output_schema: type[BaseModel] | None = Field(
        default=None, description="Schema for structured output"
    )
    system_prompt: str | None = Field(default=None, description="System prompt for the agent")
    tool_choice: Literal["auto", "any", "none"] | dict[str, Any] | None = Field(
        default="auto", description="Tool choice configuration for the LLM"
    )
    llm_node_name: str = Field(default="agent")
    tool_node_name: str = Field(default="execute_tools")
    router_node_name: str = Field(default="route")
    output_node_name: str = Field(default="structured_output")

    @model_validator(mode="after")
    def ensure_valid_configuration(self) -> Any:
        """Validate the configuration."""
        if not self.tools and (not hasattr(self, "tool_node")):
            logging.warning("No tools provided for React Agent")
        if not self.system_prompt:
            self.system_prompt = "You are a helpful AI assistant.\n\nAnswer the human's questions thoughtfully and accurately.\n\nWhen you need more information or need to perform an action:\n1. Use the available tools to gather information or perform actions\n2. Always think step-by-step about what information you need\n3. After using tools, reflect on the results before deciding next steps\n4. Provide a final answer when you have enough information"
        return self
