from typing import Annotated, List, Optional, TypedDict
from langchain_core.messages import AnyMessage
from agents.wiki_writer.interview.models import Editor
from pydantic import BaseModel
from agents.wiki_writer.interview.utils import add_messages, update_references, update_editor

class InterviewState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    references: Annotated[Optional[dict], update_references]
    editor: Annotated[Optional[Editor], update_editor]
