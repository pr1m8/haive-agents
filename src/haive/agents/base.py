from haive.core.engine.agent.agent import Agent, AgentConfig, register_agent
from langchain_core.documents import Document   
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field
from typing import List, AnyMessage, Dict
from pydantic import BaseModel

class ContentsState(BaseModel):
    """
    The state of the document agent.
    """
    documents:List[Document,AnyMessage,Dict,str] = Field(default_factory=list,description="The documents to process.")



class DocumentAgentConfig(AgentConfig):
    """
    The configuration for the document agent.
    """
    aug_llm_config: AugLLMConfig = Field(default=AugLLMConfig())

@register_agent(DocumentAgentConfig)
class DocumentAgent(Agent[DocumentAgentConfig]):
    def __init__(self, config: DocumentAgentConfig):
        super().__init__(config)

    def run(self, document: Document):
        pass
