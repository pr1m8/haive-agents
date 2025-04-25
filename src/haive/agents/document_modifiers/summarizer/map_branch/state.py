"""State for the summarizer agent"""
from typing import List,Annotated
from langchain_core.documents import Document
import operator
from pydantic import BaseModel,Field,field_validator
from typing_extensions import TypedDict
class InputState(BaseModel):
    contents: List[str] = Field(default_factory=list, description="The contents of the documents")

    @field_validator("contents", mode="before")
    @classmethod
    def normalize_contents(cls, v):
        """
        Normalize inputs to strings.
        Accepts:
        - List[str]
        - List[Document]
        - Mixed
        """
        if not isinstance(v, list):
            raise TypeError("Expected a list for 'contents'")
        
        normalized = []
        for item in v:
            if isinstance(item, Document):
                # Convert Document to string content
                normalized.append(item.page_content)
            elif isinstance(item, str):
                normalized.append(item)
            else:
                raise TypeError(f"Unsupported item type in contents: {type(item)}")
        
        return normalized



class OutputState(BaseModel):
    """Output state for the summarizer agent"""
    #summary: str = Field(default="",description="The summary of the documents")
    #summary_documents: List[Document] = Field(default_factory=list,description="The summary documents of the documents")
    final_summary: str = Field(default="",description="The final summary of the documents")


class SummaryState(InputState,OutputState):
    """State for the summarizer agent - we use the operator.add to combine the summaries"""
    #contents: List[str] = Field(default_factory=list,description="The contents of the documents")
    summaries: Annotated[list, operator.add] = Field(default_factory=list,description="The summaries of the documents")
    collapsed_summaries: List[Document] = Field(default_factory=list,description="The collapsed summaries of the documents")
    #final_summary: str = Field(default="",description="The final summary of the documents")