import operator
from typing import Annotated, List

from langchain_core.messages import AnyMessage
from pydantic import BaseModel, Field


class Plan(BaseModel):
    """
    A plan is a list of steps that are executed in order.
    """

    steps: List[str] = Field(description="The steps to execute")


class TestState(BaseModel):
    """ """

    messages: Annotated[List[AnyMessage], operator.add]
