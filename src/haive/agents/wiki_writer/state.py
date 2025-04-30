
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import List, Optional
from agents.wiki_writer.models import Editor
from agents.wiki_writer.utils import add_messages, update_references, update_editor

class InterviewState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    references: Annotated[Optional[dict], update_references]
    editor: Annotated[Optional[Editor], update_editor]