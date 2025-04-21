"""Configuration for the SimpleAgent.

This module provides the configuration class for the SimpleAgent,
which focuses on a single-node workflow with an LLM engine.
"""

from typing import Any, Dict, List, Optional, Union, Type
from pydantic import Field, model_validator

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig

from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.base import Engine
from haive.core.engine.aug_llm.base import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig, OpenAILLMConfig, AnthropicLLMConfig
from haive.core.graph.node.config import NodeConfig

from haive.agents.simple.state import SimpleAgentState


class SimpleAgentConfig(AgentConfig):
    """
    Configuration for the SimpleAgent.
    
    The SimpleAgent provides a single-node workflow that processes input
    through an LLM engine and returns the response.
    """
    # Override engine type to be more specific
    engine: Optional[Union[Engine, str, AugLLMConfig]] = Field(
        default=None,
        description="The main engine to use (defaults to AugLLMConfig)"
    )
    
    # Specific SimpleAgent fields
    system_prompt: Optional[str] = Field(
        default=None,
        description="System prompt for the LLM"
    )
    
    input_key: str = Field(
        default="messages",
        description="Key in the state to read input from"
    )
    
    output_key: str = Field(
        default="messages",
        description="Key in the state to write output to"
    )
    
    # Processing node name
    node_name: str = Field(
        default="process",
        description="Name of the processing node"
    )
    
    # Override state schema with SimpleAgentState
    state_schema: Type[SimpleAgentState] = Field(
        default=SimpleAgentState,
        description="State schema for the agent"
    )

    # Constructor validation to ensure we have a proper engine
    @model_validator(mode='after')
    def ensure_engine_setup(self):
        """Ensure the engine is properly set up."""
        # If no engine is provided, create a default AugLLMConfig
        if self.engine is None:
            # Create a default prompt if system_prompt is provided
            prompt = None
            if self.system_prompt:
                prompt = ChatPromptTemplate.from_messages([
                    ("system", self.system_prompt),
                    ("human", "{input}")
                ])
            
            # Create default AugLLMConfig with Azure as the underlying provider
            self.engine = AugLLMConfig(
                name=f"{self.name}_engine",
                llm_config=AzureLLMConfig(),
                prompt_template=prompt
            )
        
        # If engine is AugLLMConfig and system_prompt is provided but no prompt_template
        elif isinstance(self.engine, AugLLMConfig) and self.system_prompt and not self.engine.prompt_template:
            # Create a prompt from the system prompt
            self.engine.prompt_template = ChatPromptTemplate.from_messages([
                ("system", self.system_prompt),
                ("human", "{input}")
            ])
            
        return self
        
    def derive_schema(self) -> Type[SimpleAgentState]:
        """Override to always use SimpleAgentState."""
        return SimpleAgentState