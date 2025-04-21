from typing import Any

from pydantic import BaseModel, Field


class InputState(BaseModel):
    """Input state for the SQL database agent."""
    question: str = Field(description="The question to ask the SQL database")


class OutputState(BaseModel):
    """Output state for the SQL database agent."""
    answer: str = Field(description="The answer to the question")
    sql_statement: str = Field(default="", description="The SQL statement that was executed")
    hallucination_check: str | None = Field(default=None, description="Result of hallucination check")
    answer_grade: str | None = Field(default=None, description="Result of answer grading")


class OverallState(InputState, OutputState):
    """Overall state for the SQL database agent."""
    # Input
    #question: str = Field(default="", description="The question to ask the SQL database")

    # Intermediary
    steps: list[str] = Field(default_factory=list, description="Steps executed in the agent")
    next_action: str = Field(default="", description="The next action to take")
    analysis: dict[str, Any] = Field(default_factory=dict, description="Analysis of the query")
    sql_statement: str = Field(default="", description="The SQL statement to execute")
    sql_errors: list[str] = Field(default_factory=list, description="Errors in the SQL statement")
    database_records: Any = Field(default=None, description="Results from the database query")
    messages: list[Any] = Field(default_factory=list, description="Messages in the conversation")

    # Output
    #answer: str = Field(default="", description="The final answer to the question")
    #hallucination_check: Optional[str] = Field(default=None, description="Result of hallucination check")
    #answer_grade: Optional[str] = Field(default=None, description="Result of answer grading")
