"""Simple RAG Agent - BaseRAGAgent + AnswerAgent in sequence."""

from typing import List

from pydantic import Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.rag.simple.answer_agent import AnswerAgent


class SimpleRAGAgent(EnhancedMultiAgentV4):
    """Simple RAG = BaseRAGAgent + AnswerAgent in sequence."""

    agents: List = Field(
        default_factory=lambda: [
            BaseRAGAgent(name="retriever"),
            AnswerAgent(name="answerer"),
        ]
    )

    execution_mode: str = Field(default="sequential")
