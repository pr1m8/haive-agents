"""Fixed SelfDiscoverSelector that properly handles prompt template variables."""

import logging
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

from .self_discover_enhanced_v4 import ModuleSelectionOutput

logger = logging.getLogger(__name__)


class FixedSelfDiscoverSelector(SimpleAgentV3):
    """Fixed version of SelfDiscoverSelector that properly passes prompt variables."""

    name: str = Field(default="sd_selector")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3,
            max_tokens=1000,
            structured_output_model=ModuleSelectionOutput,
            system_message="You are an expert at selecting appropriate reasoning strategies for tasks.")
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Available reasoning modules:
{available_modules}

Task to solve:
{task}

Select 3-5 most relevant modules for solving this task. For each module, provide:
- number: The module number
- name: The module name
- reason: Why this module is relevant for this specific task"""),
            ]
        )
    )

    def _prepare_input(self, input_data: Any) -> Any:
        """Override to properly format the prompt with all variables."""
        if isinstance(input_data, dict):
            # Extract the required fields
            task = input_data.get("task", "")
            available_modules = input_data.get("available_modules", "")
            system_message = input_data.get(
                "system_message", self.engine.system_message
            )

            # Format the prompt with all variables
            formatted_messages = self.prompt_template.format_messages(
                task=task,
                available_modules=available_modules,
                system_message=system_message)

            # Return as messages for the graph
            return {"messages": formatted_messages}
        # Fall back to parent implementation
        return super()._prepare_input(input_data)
