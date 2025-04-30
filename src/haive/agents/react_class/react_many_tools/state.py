from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union, Literal
from langchain_core.messages import BaseMessage
from typing import Annotated, Sequence
from agents.react.react.state import ReactAgentState  

class ReactManyToolsState(ReactAgentState):
    """
    State for React Agent with many tools.
    
    Adds fields for tool selection, filtering, and document retrieval.
    """
    # Add fields specific to many tools
    tool_filter_query: Optional[str] = None
    filtered_tools: List[str] = Field(default_factory=list)
    tool_categories: Dict[str, List[str]] = Field(default_factory=dict)
    current_tool_category: Optional[str] = None
    
    # RAG integration fields
    query: Optional[str] = None
    retrieved_documents: List[Dict[str, Any]] = Field(default_factory=list)
    retrieval_metadata: Dict[str, Any] = Field(default_factory=dict)
