from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional, Union
from langchain_core.messages import BaseMessage
from typing import Annotated, Sequence
from haive_agents.react.react.state import ReactAgentState
from langgraph.graph import add_messages
from haive_agents.react.memory.models import MemoryItem, KnowledgeTriple


class MemoryAgentState(ReactAgentState):
    """
    State for Memory Agent, extending ReactAgentState.
    
    Adds fields for storing and retrieving memories.
    """
    # Loaded memories for the current conversation
    recall_memories: List[str] = Field(default_factory=list, description="Memories retrieved for context")
    
    # Memories extracted from the current conversation
    extracted_memories: List[Union[MemoryItem, KnowledgeTriple]] = Field(
        default_factory=list, 
        description="Memories extracted from the current conversation"
    )
    
    # User information
    user_id: Optional[str] = Field(default=None, description="ID of the current user")
    
    # Memory operation flags
    should_save_memories: bool = Field(default=True, description="Whether to save memories")
    memory_type: str = Field(default="unstructured", description="Type of memory: unstructured or structured")
    
    model_config = ConfigDict(arbitrary_types_allowed = True,)
