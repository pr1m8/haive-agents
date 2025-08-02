import uuid
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, ConfigDict, Field, model_validator
from haive.agents.rag.base.config import BaseRAGConfig
from haive.agents.rag.llm_rag.state import LLMRAGInputState, LLMRAGOutputState, LLMRAGState
RAG_BASE_PROMPT = 'You are an assistant for question-answering tasks.\nUse the following pieces of retrieved context to answer the question.\n\nFirst, determine if the context is relevant to the question. If the context is not relevant to\nthe question, respond with "The retrieved documents are not relevant to the question."\n\nIf the context is relevant:\n- Use the provided context to answer the question\n- If you don\'t know the answer even with the context, just say that you don\'t know\n- Use three sentences maximum and keep the answer concise\n- Base your answer solely on the provided context\n\nQuestion: {query}\nContext: {context}\nAnswer:\n'
RELEVANCE_CHECKER_PROMPT = 'You are an assistant that determines if retrieved documents are relevant to a user query.\nYour task is to analyze the query and retrieved documents to determine if they contain information\nthat would help answer the query.\n\nQuery: {query}\nRetrieved Documents:\n{documents}\n\nAre these documents relevant to the query? Reply with just "Yes" or "No".\n'

class LLMRAGConfig(BaseRAGConfig):
    """Configuration for an LLM-enhanced RAG agent."""
    model_config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True)
    name: str = Field(default_factory=lambda: f'llm_rag_agent_{uuid.uuid4().hex[:8]}')
    description: str = Field(default='LLM-enhanced Retrieval-Augmented Generation agent')
    llm_config: AugLLMConfig = Field(default_factory=lambda: AugLLMConfig(name='rag_llm', prompt_template=ChatPromptTemplate.from_template(RAG_BASE_PROMPT)), description='Configuration for the LLM component')
    relevance_checker_config: AugLLMConfig | None = Field(default_factory=lambda: AugLLMConfig(name='relevance_checker', prompt_template=ChatPromptTemplate.from_template(RELEVANCE_CHECKER_PROMPT)), description='Configuration for checking document relevance')
    state_schema: type[BaseModel] = LLMRAGState
    input_schema: type[BaseModel] = LLMRAGInputState
    output_schema: type[BaseModel] = LLMRAGOutputState

    @model_validator(mode='after')
    def setup_engines(self) -> 'LLMRAGConfig':
        """After validation, register all engines needed by the agent.
        This ensures the agent workflow can access all the necessary components.
        """
        self.engine = self.retriever_config
        if not self.llm_config.name or self.llm_config.name == 'aug_llm':
            self.llm_config.name = f'rag_llm_{uuid.uuid4().hex[:6]}'
        if self.relevance_checker_config and (not self.relevance_checker_config.name or self.relevance_checker_config.name == 'aug_llm'):
            self.relevance_checker_config.name = f'relevance_checker_{uuid.uuid4().hex[:6]}'
        return self