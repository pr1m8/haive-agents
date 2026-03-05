"""Self-Discover Module Selector Agent.

Agent that selects relevant reasoning modules for a given task.
"""

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class ModuleSelectionOutput(BaseModel):
    """Output from module selector - string format."""

    selected_modules: str = Field(
        description="Selected reasoning modules as formatted text"
    )


class SelfDiscoverSelector(SimpleAgent):
    """Agent that selects relevant reasoning modules."""

    name: str = Field(default="sd_selector")

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.3,
            max_tokens=1000,
            structured_output_model=ModuleSelectionOutput,
            system_message="You are an expert at selecting appropriate reasoning strategies for tasks.",
        )
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert at selecting appropriate reasoning strategies for tasks.",
                ),
                ("human", "{messages}"),
            ]
        )
    )
