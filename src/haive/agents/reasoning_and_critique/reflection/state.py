"""State schema for the Reflection Agent.
"""

from typing import Any, Optional

from agents.reflection.models import ReflectionResult
from agents.simple.state import SimpleAgentState
from langchain_core.messages import AIMessage, HumanMessage
from pydantic import Field


class ReflectionAgentState(SimpleAgentState):
    """State schema for the Reflection agent.
    """

    # Fields for tracking reflection
    original_request: Optional[str] = Field(default=None)
    response: Optional[str] = Field(default=None)
    feedback: Optional[str] = Field(default=None)
    reflection_round: int = Field(default=0)
    reflection_score: Optional[float] = Field(default=None)
    reflection_history: list[dict[str, Any]] = Field(default_factory=list)

    # Final output
    improved_response: Optional[str] = None

    # Optional search components
    search_queries: list[str] = Field(default_factory=list)
    search_results: list[dict[str, Any]] = Field(default_factory=list)

    @property
    def last_human_message(self -> Optional[str]:
        """Extract the last human message content.
        """
        for msg in reversed(self.messages):
            if isinstance(
    msg,
    HumanMessage) or getattr(
        msg,
        "type",
         "") == "human":
                return msg.content
        return None

    @ property
    def last_ai_message(self -> Optional[str]:
        """Extract the last AI message content.
        """
        for msg in reversed(self.messages):
            if isinstance(msg, AIMessage) or getattr(msg, "type", "") == "ai":
                return msg.content
        return None

    def add_reflection(self, reflection: ReflectionResult) -> None:
        """Add a reflection result to the history.
        """
        self.reflection_history.append(
            {
                "round": self.reflection_round,
                "reflection": reflection.model_dump(),
                "response": self.response,
            }
        )
        self.reflection_round += 1
        self.reflection_score=reflection.normalized_score
