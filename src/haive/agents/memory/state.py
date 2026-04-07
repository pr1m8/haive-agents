"""Memory agent state - extends ReactAgentState with memory fields."""

from typing import Any

from pydantic import Field

from haive.agents.react.state import ReactAgentState


class MemoryAgentState(ReactAgentState):
    """Extends ReactAgentState with memory-specific fields.

    Inherits from ReactAgentState:
        messages, tool_results, iteration, structured_output,
        intermediate_steps, requires_human_input, human_request
    """

    # Memory context loaded before response
    memory_context: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Retrieved memories injected as context before LLM call",
    )

    # User/thread scoping
    user_id: str = Field(default="default", description="User ID for memory scoping")
    thread_id: str = Field(default="", description="Thread ID for conversation scoping")

    # Token tracking for auto-summarization
    token_count: int = Field(default=0, description="Approximate token count of messages")
    summarized: bool = Field(default=False, description="Whether conversation was summarized this turn")

    # KG triples extracted this turn
    kg_triples: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Knowledge graph triples extracted this turn",
    )
