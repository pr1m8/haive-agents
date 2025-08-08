"""SimpleRAGAgentV4 - Simple RAG with retrieved documents in prompt."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore.vectorstore import VectorStoreConfig
from pydantic import Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.rag.answer_agent import AnswerAgent
from haive.agents.rag.base.agent import BaseRAGAgent


class SimpleRAGAgentV4(MultiAgent):
    """Simple RAG = MultiAgent([BaseRAGAgent, AnswerAgent], mode="sequential")."""

    vector_store_config: VectorStoreConfig = Field(
        ..., description="Vector store config for retrieval"
    )

    llm_config: AugLLMConfig = Field(
        default_factory=AugLLMConfig, description="LLM config for answer generation"
    )

    agents: list = Field(init=False)
    execution_mode: str = Field(default="sequential")

    def model_post_init(self, __context):
        """Set up the agents with the configs."""
        self.agents = [
            BaseRAGAgent(
                name=f"{self.name}_retriever", engine=self.vector_store_config
            ),
            AnswerAgent(name=f"{self.name}_answerer", engine=self.llm_config),
        ]
        super().model_post_init(__context)
