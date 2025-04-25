from pydantic import BaseModel, Field
from typing import List, Optional, Union
from langchain.schema import Document
from haive.core.engine.agent.agent import AgentConfig

class BaseRAGInputState(BaseModel):
    """Input state for RAG agents."""
    query: str = Field(..., description="The query to search the RAG database with.")

class BaseRAGOutputState(BaseModel):
    """Output state for RAG agents."""
    answer:str = Field(default="", description="The generation of the RAG search.")
    
class BaseRAGState(BaseRAGInputState,BaseRAGOutputState):
    """State for RAG agents."""
    retrieverd_documents: Optional[Union[List[Document], List[str]]] = Field(default=[], description="The results of the RAG search.")
    #filtered_documents: Optional[Union[List[Document], List[str]]] = Field(default=[], description="The filtered documents from the RAG search.")

