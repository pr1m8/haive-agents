# src/haive/agents/tot/state.py

from typing import List, Optional, Union, Annotated, Any, Dict
from pydantic import BaseModel, Field, field_validator, ConfigDict
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from haive_agents.tot.modular.models import Candidate

class ToTState(BaseModel):
    """
    The state schema for Tree of Thoughts agent.
    """
    # Basic state tracking
    messages: Annotated[List[BaseMessage], add_messages] = Field(
        default_factory=list,
        description="Message history"
    )
    
    # Problem definition
    problem: str = Field(
        default="",
        description="The problem to solve"
    )
    
    # ToT algorithm state
    candidates: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Current candidate solutions"
    )
    
    scored_candidates: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Scored candidate solutions"
    )
    
    # Search parameters
    depth: int = Field(
        default=0,
        description="Current search depth"
    )
    
    max_depth: int = Field(
        default=5,
        description="Maximum search depth"
    )
    
    best_candidate: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Best candidate found so far"
    )
    
    # For expansion
    current_seed: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Current seed candidate for expansion"
    )
    
    # Output field
    answer: Optional[str] = Field(
        default=None,
        description="Final answer to the problem"
    )
    
    # Use Pydantic v2 configuration
    model_config = ConfigDict(
        validate_assignment=True,
        extra="allow",
        arbitrary_types_allowed=True,
    )
    
    @field_validator('candidates', 'scored_candidates', mode='before')
    @classmethod
    def convert_candidates(cls, v):
        """Convert Candidate objects to dictionaries if needed."""
        if v is None:
            return []
        if isinstance(v, str) and v == "clear":
            return []
        if not isinstance(v, list):
            return []
            
        result = []
        for item in v:
            if isinstance(item, Candidate):
                # Convert Candidate objects to dictionaries
                result.append({
                    "content": item.content,
                    "score": item.score,
                    "feedback": item.feedback,
                    "metadata": item.metadata
                })
            elif isinstance(item, dict):
                result.append(item)
            else:
                # Skip invalid items
                continue
        return result
    
    @field_validator('best_candidate', 'current_seed', mode='before')
    @classmethod
    def convert_single_candidate(cls, v):
        """Convert a single Candidate object to a dictionary if needed."""
        if v is None:
            return None
        if isinstance(v, Candidate):
            # Convert Candidate object to dictionary
            return {
                "content": v.content,
                "score": v.score,
                "feedback": v.feedback,
                "metadata": v.metadata
            }
        return v