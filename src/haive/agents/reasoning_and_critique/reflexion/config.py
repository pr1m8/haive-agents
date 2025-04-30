from pydantic import BaseModel
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.agent.agent import AgentConfig,Agent,register_agent
from langchain_core.tools import StructuredTool,BaseTool
from langgraph.prebuilt import ToolNode
from typing import Union,List,Callable
from agents.reflexion.models import AnswerQuestion,ReviseAnswer
from agents.reflexion.aug_llms import initial_answer_chain_config,revision_chain_config
from typing import Dict
from agents.reflexion.state import ReflexionState
from agents.reflexion.tools import run_queries
class ReflexionConfig(AgentConfig):
    """Configuration for the Reflexion agent."""
    engines: Dict[str,AugLLMConfig] = {'responder':initial_answer_chain_config,'revisor':revision_chain_config}
    max_iterations: int = 5
    attempts: int = 3
    tools: List[Union[BaseTool,Callable]] = [run_queries]
    models: List[BaseModel] = [AnswerQuestion,ReviseAnswer]
    state_schema: BaseModel = ReflexionState
    @classmethod
    def create_agent(cls):
        from agents.reflexion.agent import ReflexionAgent
        return ReflexionAgent(config=cls())