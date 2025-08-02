"""SimpleRAG - Class inheriting from MultiAgent."""
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.retriever import BaseRetrieverConfig
from haive.core.engine.vectorstore import VectorStoreConfig
from pydantic import Field, model_validator
from haive.agents.multi.clean import MultiAgent
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent
from .answer_generator import RAG_CHAT_TEMPLATE, RAGAnswer

class SimpleRAG(MultiAgent):
    """SimpleRAG inheriting from MultiAgent with sequential BaseRAGAgent + SimpleAgent."""
    retriever_config: BaseRetrieverConfig | VectorStoreConfig = Field(..., description='Configuration for the retriever agent')
    llm_config: AugLLMConfig = Field(..., description='Configuration for the generator agent')

    @model_validator(mode='after')
    def create_agents(self) -> 'SimpleRAG':
        """Create the retriever and generator agents."""
        retriever = BaseRAGAgent(name=f'{self.name}_retriever', engine=self.retriever_config)
        generator_config = self.llm_config.model_copy()
        generator_config.prompt_template = RAG_CHAT_TEMPLATE
        generator_config.structured_output_model = RAGAnswer
        generator = SimpleAgent(name=f'{self.name}_generator', engine=generator_config)
        self.agents = {'retriever': retriever, 'generator': generator}
        self.execution_mode = 'sequential'
        return self
__all__ = ['SimpleRAG']