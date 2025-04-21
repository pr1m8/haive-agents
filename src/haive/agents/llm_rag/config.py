
from pydantic import BaseModel, Field

from haive.agents.rag.base.config import BaseRAGConfig
from haive.agents.rag.llm_rag.engine import rag_aug_llm
from haive.agents.rag.llm_rag.state import LLMRAGOutputState
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm.base import AugLLMConfig


class LLMRAGConfig(BaseRAGConfig):
    llm_rag_engine: AugLLMConfig | AgentConfig = Field(default=rag_aug_llm)
    output_schema: type[BaseModel] = LLMRAGOutputState
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.engines['llm_rag_engine'] = self.llm_rag_engine
        self.engines["answer_generator"] = self.llm_rag_engine
