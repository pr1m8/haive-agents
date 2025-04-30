from typing import List, Dict, Any, Optional, Union, Type, Tuple
from enum import Enum
from pydantic import BaseModel, Field

from langchain_core.messages import BaseMessage, AnyMessage
class ReactionData(BaseModel):
    """Data for agent reasoning and action."""
    thought: Optional[str] = Field(default=None, description="Agent's reasoning")
    action: Optional[str] = Field(default=None, description="Tool to use or 'final_answer'")
    action_input: Optional[Union[str, Dict[str, Any]]] = Field(
        default=None, 
        description="Input for the tool or final answer text"
    )

class ActionType(str, Enum):
    """Types of actions that the agent can take."""
    SEARCH = "search"
    CALCULATOR = "calculator"
    WEATHER = "weather"
    DATABASE = "database"
    FINAL_ANSWER = "final_answer"
    # Add more action types as needed


class Action(BaseModel):
    """An action that the agent decides to take."""
    action_type: ActionType
    action_input: str
    
    def __str__(self):
        return f"{self.action_type}: {self.action_input}"


class Thought(BaseModel):
    """The agent's reasoning process."""
    thought: str
    action: Action

    def __str__(self):
        return f"Thought: {self.thought}\nAction: ActionType.{self.action.action_type}, ActionInput: {self.action.action_input}"

import operator
from typing import Annotated
class ReactState(BaseModel):
    """State schema for React agent."""
    messages: List[AnyMessage] = Field(default_factory=list)  # Removed the operator.add annotation
    thoughts: List[Thought] = Field(default_factory=list)
    observations: List[str] = Field(default_factory=list)
    intermediate_steps: List[Union[Dict[str, Any], Tuple[Action, str]]] = Field(default_factory=list)
    final_answer: Optional[str] = None
    current_thought: Optional[Thought] = None
    iteration_count: int = 0
    max_iterations: int = 10
    tools: Dict[str, Any] = Field(default_factory=dict)
    tool_names: List[str] = Field(default_factory=list)
    status: str = "thinking"  # thinking, acting, observing, done
    current_action: Optional[Action] = None
    retry_attempts: Dict[str, int] = Field(default_factory=dict)
    max_retry_attempts: int = 3