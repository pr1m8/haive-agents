# =============================================
# Simple Agent Config
# =============================================

import logging
import traceback
from datetime import datetime
from typing import Optional, Dict, Type, Any

from pydantic import BaseModel, Field, ValidationError, field_validator
from langchain_core.messages import SystemMessage
from langchain.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate

from haive_core.engine.agent.agent import AgentConfig
from haive_core.engine.aug_llm import AugLLMConfig
from haive_core.models.llm.base import AzureLLMConfig, LLMConfig

# Setup Logging
LOG_FILE = "debug_simple_agent.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import sys
from haive_core.engine.aug_llm import AugLLMConfig

print("AugLLMConfig Path:", sys.modules.get("haive_core.engine.aug_llm.base"))
print("AugLLMConfig Class:", AugLLMConfig)
print("AugLLMConfig File:", AugLLMConfig.__module__)

class SimpleAgentConfig(AgentConfig):
    """
    Configuration for a simple single-node agent.
    
    This is a basic agent with a single reasoning node that processes input
    and generates output without complex workflow or tool usage.
    """
    engine: Optional[Any] = Field(
        default=None,
        description="The engine to use for the agent."
    )
    
    node_name: str = Field(default="simple_agent_node", description="Name for the single processing node.")
    input_mapping: Optional[Dict[str, str]] = Field(default=None, description="Maps state fields to engine input fields.")
    output_mapping: Optional[Dict[str, str]] = Field(default=None, description="Maps engine output fields to state fields.")
    system_prompt: str = Field(default="You are a helpful assistant.", description="System prompt for the agent.")
    state_schema: Optional[Type[BaseModel]] = Field(default=None, description="Schema for the agent state.")
    visualize: bool = Field(default=True, description="Whether to visualize the graph.")

    @field_validator("engine", mode="after")
    def check_engine_present(cls, v):
        """
        Ensures that `engine` is an instance of `AugLLMConfig`
        """
        try:
            if v is None:
                logger.error("🚨 Engine is required but got None")
                raise ValueError("Engine is required.")
            
            # Get the class name rather than doing direct isinstance check
            engine_class_name = v.__class__.__name__
            if engine_class_name != "AugLLMConfig" and not isinstance(v, AgentConfig):
                logger.error(f"🚨 Invalid engine type: Expected AugLLMConfig, got {type(v)}")
                raise TypeError(f"Expected AugLLMConfig, but got {type(v)}")
            
            logger.debug(f"✅ Engine validated successfully: {v}")
            return v
        except Exception as e:
            logger.error("🚨 Error in check_engine_present", exc_info=True)
            print(f"🚨 Error in check_engine_present: {e}")
            traceback.print_exc()
            raise
    
    @classmethod
    def from_aug_llm(cls, aug_llm: AugLLMConfig, name: Optional[str] = None, system_prompt: Optional[str] = None, **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig from an existing AugLLMConfig.
        
        Args:
            aug_llm: Existing AugLLMConfig to use
            name: Optional agent name
            system_prompt: Optional system prompt
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig instance
        """
        try:
            logger.debug(f"🛠️ Creating SimpleAgentConfig with AugLLMConfig: {aug_llm}")
            if not isinstance(aug_llm, AugLLMConfig):
                logger.error(f"🚨 from_aug_llm received incorrect type: {type(aug_llm)}")
                raise TypeError(f"Expected AugLLMConfig but received {type(aug_llm)}")

            # Import locally to avoid circular imports
            from haive_agents.simple.state import SimpleAgentState
            
            config = cls(
                name=name or f"simple_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                engine=aug_llm,
                system_prompt=system_prompt or "You are a helpful assistant.",
                state_schema=SimpleAgentState,  # Always set state_schema to SimpleAgentState
                **kwargs
            )
            
            return config
        except (TypeError, ValidationError) as e:
            logger.error("🚨 Error in from_aug_llm", exc_info=True)
            print(f"🚨 Error in from_aug_llm: {e}")
            traceback.print_exc()
            raise

    @classmethod
    def from_scratch(cls, system_prompt: Optional[str] = None, model: str = "gpt-4o", temperature: float = 0.7, name: Optional[str] = None, **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig from scratch.
        
        Args:
            system_prompt: Optional system prompt
            model: Model name to use
            temperature: Temperature for generation
            name: Optional agent name
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig instance
        """
        try:
            logger.debug(f"🛠️ Creating AugLLMConfig from scratch with model: {model}")

            llm_config = AzureLLMConfig(
                model=model,
                parameters={"temperature": temperature}
            )

            system_prompt = system_prompt or "You are a helpful assistant."
            messages = [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="messages")
            ]
            prompt_template = ChatPromptTemplate.from_messages(messages)

            aug_llm = AugLLMConfig(
                name=f"{name or 'simple'}_llm",
                llm_config=llm_config,
                prompt_template=prompt_template,
                system_prompt=system_prompt
            )

            # Import locally to avoid circular imports
            from haive_agents.simple.state import SimpleAgentState
            
            config = cls(
                name=name or f"simple_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                engine=aug_llm,
                system_prompt=system_prompt,
                state_schema=SimpleAgentState,  # Always set state_schema to SimpleAgentState
                **kwargs
            )
            
            return config
        except (TypeError, ValidationError) as e:
            logger.error("🚨 Error in from_scratch", exc_info=True)
            print(f"🚨 Error in from_scratch: {e}")
            traceback.print_exc()
            raise

    def _process_state_schema(self):
        """Process and validate state schema."""
        # Always ensure we have a proper state schema
        if self.state_schema is None:
            # Import locally to avoid circular imports
            from haive_agents.simple.state import SimpleAgentState
            self.state_schema = SimpleAgentState