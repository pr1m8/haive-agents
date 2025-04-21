from typing import AnyMessage

from langchain_core.documents import Document
from pydantic import BaseModel, Field

from haive.core.engine.agent.agent import Agent, AgentConfig, register_agent
from haive.core.engine.aug_llm.base import AugLLMConfig


class ContentsState(BaseModel):
    """The state of the document agent.
    """
    documents:list[Document,AnyMessage,dict,str] = Field(default_factory=list,description="The documents to process.")



class DocumentAgentConfig(AgentConfig):
    """The configuration for the document agent.
    """
    aug_llm_config: AugLLMConfig = Field(default=AugLLMConfig())

@register_agent(DocumentAgentConfig)
class DocumentAgent(Agent[DocumentAgentConfig]):
    def __init__(self, config: DocumentAgentConfig):
        super().__init__(config)

    def run(self, document: Document):
        pass
