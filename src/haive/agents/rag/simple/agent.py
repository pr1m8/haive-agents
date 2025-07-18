"""Simple RAG Agent.

Uses clean MultiAgent with sequential execution to compose BaseRAG with answer generation.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig, LLMConfig
from langchain_core.documents import Document

from haive.agents.multi import MultiAgent
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.rag.common.answer_generators.prompts import RAG_ANSWER_STANDARD
from haive.agents.simple.agent import SimpleAgent


class SimpleRAGAgent(MultiAgent):
    """Simple RAG workflow: Retrieval → Answer Generation"""

    @classmethod
    def from_documents(
        cls, documents: list[Document], llm_config: LLMConfig | None = None, **kwargs
    ):
        """Create SimpleRAG from documents."""
        # Create retrieval agent
        retrieval_agent = BaseRAGAgent.from_documents(
            documents=documents, name="retriever"
        )

        # Create answer agent with RAG prompt
        if not llm_config:
            llm_config = AzureLLMConfig(
                deployment_name="gpt-4",
                azure_endpoint="${AZURE_OPENAI_API_BASE}",
                api_key="${AZURE_OPENAI_API_KEY}",
            )

        answer_agent = SimpleAgent(
            engine=AugLLMConfig(
                llm_config=llm_config, prompt_template=RAG_ANSWER_STANDARD
            ),
            name="answer_generator",
        )

        # Use the clean MultiAgent.create() method
        # Remove name from kwargs to avoid conflict
        agent_name = kwargs.pop("name", "simple_rag_agent")
        return cls.create(
            agents=[retrieval_agent, answer_agent],
            name=agent_name,
            execution_mode="sequential",
            **kwargs
        )
