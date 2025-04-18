from pydantic import BaseModel,Field
from haive_agents.rag.base.state import BaseRagOutputState
class LLMRAGOutputState(BaseRagOutputState):
    answer: str = Field(default=...,description="The answer to the question")


    