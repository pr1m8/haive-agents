"""
Example usage of SimpleAgent implementation with enhanced debugging.

This script demonstrates how to create and use SimpleAgent with custom state schema.
"""

import logging
import os
import sys
import uuid
from typing import Any, Dict, List, Optional

# Setup enhanced logging with rich
import rich
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.traceback import install as install_rich_traceback

from haive.agents.simple import (
    SimpleAgent,
    SimpleAgentConfig,
    SimpleAgentState,
    create_simple_agent,
)

# Install rich traceback for better error display
install_rich_traceback(show_locals=True, width=120, suppress=[])

# Create console
console = Console()

# Configure logging with rich handler
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for more verbose output
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True, show_path=False)],
)

# Get logger
logger = logging.getLogger("SimpleAgentDebug")


def debug_print(title, obj, expand=False):
    """Print debugging information in a rich panel."""
    if isinstance(obj, dict):
        from rich.pretty import Pretty

        console.print(
            Panel(Pretty(obj, expand_all=expand), title=title, border_style="cyan")
        )
    else:
        console.print(Panel(str(obj), title=title, border_style="cyan"))


def example_with_custom_state_schema():
    """Create an agent with a custom state schema with enhanced debugging."""
    console.rule("[bold cyan]Creating agent with custom state schema")

    # Define a custom state schema with additional fields
    class CustomAgentState(BaseModel):
        messages: List[BaseMessage] = Field(default_factory=list)
        input: str = Field(default="")
        output: str = Field(default="")  # This field will receive the LLM output
        result: str = Field(default="")  # Adding a result field as well for fallback
        error: Optional[str] = Field(default=None)
        context: List[str] = Field(
            default_factory=list, description="Contextual information"
        )
        metadata: Dict[str, Any] = Field(
            default_factory=dict, description="Additional metadata"
        )
        confidence: float = Field(default=1.0, description="Confidence level")

    console.print("[bold green]Defined CustomAgentState with fields:")
    for field_name, field in CustomAgentState.model_fields.items():
        console.print(f"  - [bold]{field_name}[/bold]: {field.annotation}")

    # Create a prompt template that uses context and input
    prompt = PromptTemplate.from_template(
        """
        Context information: {context}
        
        User query: {input}
        
        Please provide a helpful response based on the context and query.
        """
    )

    console.print("[bold green]Created prompt template:")
    console.print(f"  - Template: {prompt.template}")
    console.print(f"  - Variables: {prompt.input_variables}")

    # Create AugLLMConfig with debugging output
    console.print("[bold green]Creating AugLLMConfig")
    aug_llm = AugLLMConfig(
        name="custom_state_llm",
        llm_config=AzureLLMConfig(model="gpt-4o"),
        prompt_template=prompt,
        output_parser=StrOutputParser(),
        system_prompt="You are a helpful assistant.",
    )

    debug_print(
        "AugLLMConfig",
        {
            "name": aug_llm.name,
            "id": getattr(aug_llm, "id", None),
            "prompt_variables": getattr(aug_llm.prompt_template, "input_variables", []),
            "system_prompt": aug_llm.system_message,
        },
    )

    # Create the agent with custom state schema
    # Input/output mappings should be auto-detected based on field names
    console.print("[bold green]Creating SimpleAgent with custom schema")
    agent = create_simple_agent(
        name="custom_state_agent",
        engine=aug_llm,
        state_schema=CustomAgentState,
        debug=True,
    )

    # Set a thread ID for consistent state tracking
    thread_id = str(uuid.uuid4())
    agent.runnable_config["configurable"]["thread_id"] = thread_id
    console.print(f"[bold]Set thread ID:[/bold] {thread_id}")

    # Debug print the input data
    input_data = {
        "input": "What is the capital of Slovakia",
        "context": ["Slovakia is a country in Central Europe."],
    }
    debug_print("Input Data", input_data)

    # Use the agent
    console.print("[bold green]Running the agent...")
    try:
        response = agent.run(input_data, debug=True)

        # Print results
        console.print("[bold green]Agent completed successfully!")
        debug_print("Response", response)

    except Exception as e:
        console.print("[bold red]Error running agent:")
        console.print_exception(show_locals=True)

    return agent


if __name__ == "__main__":
    console.rule("[bold magenta]SimpleAgent Debug Example")
    example_with_custom_state_schema()
