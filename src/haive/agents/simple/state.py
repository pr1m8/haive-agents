"""State schema for the SimpleAgent.

This module provides the state schema for the SimpleAgent, which focuses
on a simple messages-based workflow with minimal additional fields.
"""

from typing import Any, Dict, List, Optional
from langchain_core.messages import BaseMessage
from typing import Annotated

from pydantic import Field
from langgraph.graph import add_messages
from haive.core.schema.state_schema import StateSchema


class SimpleAgentState(StateSchema):
    """
    State schema for SimpleAgent.
    
    This state tracks messages and any structured output produced by the engine.
    It also provides a context dictionary for additional state information.
    """
    messages: Annotated[List[BaseMessage], add_messages] = Field(
        default_factory=list,
        description="Messages exchanged between the user and the agent"
    )
    
    output: Any = Field(
        default=None,
        description="Structured output from the agent's processing"
    )
    
    context: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional context information for the agent"
    )
    
    # Configure message merging with LangGraph's add_messages
    __reducer_fields__ = {"messages": add_messages}
    __serializable_reducers__ = {"messages": "add_messages"}
    
    # Make messages shared with parent graphs
    __shared_fields__ = ["messages"]