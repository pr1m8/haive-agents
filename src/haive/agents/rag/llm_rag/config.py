from haive.agents.rag.base.config import BaseRAGConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.agent.agent import AgentConfig
from typing import Union,Type
from haive.agents.rag.llm_rag.state import LLMRAGOutputState
from pydantic import Field,BaseModel
from haive.agents.rag.llm_rag.engine import rag_aug_llm


class LLMRAGConfig(BaseRAGConfig):
    llm_rag_engine: Union[AugLLMConfig,AgentConfig] = Field(default=rag_aug_llm)
    output_schema: Type[BaseModel] = LLMRAGOutputState
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.engines['llm_rag_engine'] = self.llm_rag_engine
        self.engines['answer_generator'] = self.llm_rag_engine