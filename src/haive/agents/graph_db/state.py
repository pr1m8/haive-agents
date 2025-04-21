

from pydantic import BaseModel, Field


class InputState(BaseModel):
    """Input state for the graph database agent.
    """
    question: str = Field(description="The user's question")


class OutputState(BaseModel):
    """Output state for the graph database agent.
    """
    answer: str = Field(default="",description="The answer to the user's question")
    steps: list[str] = Field(default_factory=list,description="The steps taken to reach the current state")
    cypher_statement: str = Field(default="",description="The Cypher statement to execute")

class OverallState(InputState,OutputState):
    """Overall state for the graph database agent.
    """
    #question: str = Field(description="The user's question")
    next_action: str = Field(default="",description="The next action to take")
    #cypher_statement: str = Field(default="",description="The Cypher statement to execute")
    cypher_errors: list[str] = Field(default=[],description="The errors in the Cypher statement")
    database_records: list[dict] = Field(default=[],description="The records retrieved from the database")
    #steps: Annotated[List[str], add] = Field(description="The steps taken to reach the current state")


