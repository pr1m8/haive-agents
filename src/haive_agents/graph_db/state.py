
from operator import add
from typing import Annotated, List

from typing_extensions import TypedDict
from pydantic import Field,BaseModel

class InputState(BaseModel):
    """
    Input state for the graph database agent.
    """
    question: str = Field(description="The user's question")


class OutputState(BaseModel):
    """
    Output state for the graph database agent.
    """
    answer: str = Field(default="",description="The answer to the user's question")
    steps: List[str] = Field(default_factory=list,description="The steps taken to reach the current state")
    cypher_statement: str = Field(default="",description="The Cypher statement to execute")

class OverallState(InputState,OutputState):
    """
    Overall state for the graph database agent.
    """
    #question: str = Field(description="The user's question")
    next_action: str = Field(default="",description="The next action to take")
    #cypher_statement: str = Field(default="",description="The Cypher statement to execute")
    cypher_errors: List[str] = Field(default=[],description="The errors in the Cypher statement")
    database_records: List[dict] = Field(default=[],description="The records retrieved from the database")
    #steps: Annotated[List[str], add] = Field(description="The steps taken to reach the current state")


 