"""State model for the LLM Compiler agent."""

from typing import Any

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field

from .dag_models import DAGPlan


class CompilerState(BaseModel):
    """State for the LLM Compiler agent.

    Tracks query, DAG plan, execution results, messages, and replan count.
    """

    query: str = Field(default="", description="User's original query")
    dag_plan: DAGPlan | None = Field(default=None, description="Current DAG execution plan")
    results: dict[int, Any] = Field(default_factory=dict, description="Task ID -> result")
    messages: list[BaseMessage] = Field(default_factory=list, description="Conversation history")
    replan_count: int = Field(default=0, description="Replan attempts")
    done: bool = Field(default=False, description="Whether execution is complete")

    # Keep old field for backwards compat with existing models
    plan: Any = Field(default=None, description="Legacy plan field")

    class Config:
        arbitrary_types_allowed = True
