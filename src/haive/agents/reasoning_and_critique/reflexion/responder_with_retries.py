import json

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import ToolMessage
from langchain_core.output_parsers import PydanticToolsParser
from langgraph.types import Command
from pydantic import BaseModel, ValidationError


class ResponderWithRetries:
    """A responder that retries a given runnable a number of times if it fails to validate."""

    def __init__(self, aug_llm_config: AugLLMConfig, num_retries: int = 3, name: str | None = None):
        """Args:
        aug_llm_config: The config for the LLM to use.
        num_retries: The number of times to retry the runnable.
        """
        self.runnable = aug_llm_config.create_runnable()
        self.aug_llm_config = aug_llm_config
        # Create validator with safe tools access
        tools = getattr(aug_llm_config, "tools", [])
        self.validator = PydanticToolsParser(tools=tools) if tools else None
        self.name = name
        self.num_retries = num_retries

    def respond(self, state: BaseModel):
        """Respond to the user's message."""
        response = []
        reflections_count = getattr(state, "reflections_count", 0)
        for attempt in range(self.num_retries):
            response = self.runnable.invoke(
                {"messages": getattr(state, "messages", [])}, {"tags": [f"attempt:{attempt}"]}
            )
            try:
                if self.validator:
                    self.validator.invoke(response)
                if self.name == "revisor":
                    return Command(
                        update={
                            "messages": response,
                            "reflections_count": reflections_count + 1,
                        }
                    )
                return Command(update={"messages": response})
            except ValidationError as e:
                response = [
                    response,
                    ToolMessage(
                        content=f"{e!r}\n\nPay close attention to the function schema.\n\n"
                        + json.dumps(self.validator.schema() if self.validator else {}, indent=2)
                        + "\nRespond by fixing all validation errors.",
                        tool_call_id=response.tool_calls[0]["id"],
                    ),
                ]
        if self.name == "revisor":
            return Command(
                update={
                    "messages": response,
                    "reflections_count": reflections_count + 1,
                }
            )
        return Command(update={"messages": response})
