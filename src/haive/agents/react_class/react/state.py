from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional, Union, Literal
from langchain_core.messages import BaseMessage
from typing import Annotated, Sequence
from haive.agents.simple.state import SimpleAgentState
from langgraph.graph import add_messages

class ReactAgentState(SimpleAgentState):
    """
    State for React Agent, extending SimpleAgentState.
    
    Adds fields for tool results, intermediate reasoning, 
    and structured output.
    """
    # Inherit messages field from SimpleAgentState
    
    # Tool-related fields
    tool_results: List[Dict[str, Any]] = Field(default_factory=list)
    active_tools: List[str] = Field(default_factory=list)
    selected_tools: List[Dict[str, Any]] = Field(default_factory=list)
    
    # Reasoning-related fields
    intermediate_steps: List[Dict[str, Any]] = Field(default_factory=list)
    reasoning: Optional[str] = None
    
    # Output-related fields
    structured_output: Optional[Dict[str, Any]] = None
    final_answer: Optional[str] = None
        
    model_config = ConfigDict(

            arbitrary_types_allowed = True,

    )
