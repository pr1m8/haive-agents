# src/haive/agents/react/state.py

from typing import List, Dict, Any, Optional, Sequence
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from typing import Annotated
from langgraph.graph import add_messages

class ReactAgentState(BaseModel):
    """State schema for React agent."""
    
    # Messages with the add_messages reducer
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(
        default_factory=list,
        description="Messages in the conversation"
    )
    
    # Tool results 
    tool_results: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Results from tool executions"
    )
    
    # Track iterations
    iteration: int = Field(
        default=0,
        description="Current iteration count"
    )
    
    # Optional structured output
    structured_output: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Structured output from the agent"
    )
    
    # Other useful state tracking
    intermediate_steps: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Intermediate reasoning steps"
    )
    
    # Flag for human assistance
    requires_human_input: bool = Field(
        default=False,
        description="Flag to indicate if human input is required"
    )
    
    # Human request content
    human_request: Optional[str] = Field(
        default=None,
        description="Request for human assistance"
    )