"""Simple RAG Agent - BaseRAGAgent + AnswerAgent in sequence."""

from pydantic import Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.rag.simple.answer_agent import AnswerAgent


class SimpleRAGAgent(MultiAgent):
    """Simple RAG = BaseRAGAgent + AnswerAgent in sequence."""

    agents: list = Field(
        default_factory=lambda: [
            BaseRAGAgent(name="retriever"),
            AnswerAgent(name="answerer"),
        ]
    )

    execution_mode: str = Field(default="sequential")
