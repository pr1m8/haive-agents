from agents.react_agent.state import AgentState
from agents.long_term_memory.models import KnowledgeTriple
from pydantic import BaseModel
from typing import List, Union
from pydantic import Field

class LongTermMemoryState(AgentState):
    """State for the long term memory agent."""
    memories: List[Union[BaseModel, KnowledgeTriple]] = Field(default_factory=list, description="List of memories to be used for the agent")
