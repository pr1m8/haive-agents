from pydantic import Field

from haive.agents.rag.base.state import BaseRagOutputState


class LLMRAGOutputState(BaseRagOutputState):
    answer: str = Field(default=...,description="The answer to the question")


