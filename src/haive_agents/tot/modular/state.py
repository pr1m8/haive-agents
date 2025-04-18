from typing import List, Optional, Annotated, Any, Dict, Union, Sequence
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from haive_agents.tot.modular.models import Candidate

def update_candidates(
    existing: Optional[List[Candidate]] = None,
    updates: Optional[Union[List[Candidate], str, List[Dict[str, Any]]]] = None,
) -> List[Candidate]:
    """
    Update candidate list, handling special cases like clearing.
    
    Args:
        existing: Current list of candidates
        updates: New candidates to add, or "clear" to empty the list
        
    Returns:
        Updated list of candidates
    """
    if existing is None:
        existing = []
    if updates is None:
        return existing
    if updates == "clear":
        return []
    
    # Handle list of dictionaries by converting to Candidate objects
    if isinstance(updates, list) and updates and isinstance(updates[0], dict):
        candidate_objects = []
        for item in updates:
            candidate_objects.append(Candidate(**item))
        return existing + candidate_objects
    
    # Regular list concatenation
    return existing + updates

class ToTState(BaseModel):
    """
    The state schema for Tree of Thoughts agent.
    """
    # Basic state tracking
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(
        default_factory=list,
        description="Message history"
    )
    
    # Problem definition
    problem: str = Field(
        default="",
        description="The problem to solve"
    )
    
    # ToT algorithm state
    candidates: Annotated[List[Candidate], update_candidates] = Field(
        default_factory=list,
        description="Current candidate solutions"
    )
    
    scored_candidates: Annotated[List[Candidate], update_candidates] = Field(
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
    
    best_candidate: Optional[Candidate] = Field(
        default=None,
        description="Best candidate found so far"
    )
    
    # For expansion
    current_seed: Optional[Candidate] = Field(
        default=None,
        description="Current seed candidate for expansion"
    )
    
    # Output field
    answer: Optional[str] = Field(
        default=None,
        description="Final answer to the problem"
    )
    
    # Extra metadata
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )