from typing import Dict, List, Any, Optional, Union, Type, Literal
from pydantic import BaseModel, Field, model_validator
from langchain_core.tools import BaseTool, StructuredTool
from haive_agents.simple.config import SimpleAgentConfig
from haive_core.engine.aug_llm import AugLLMConfig
from haive_agents.react.react.state import ReactAgentState

class ReactAgentConfig(SimpleAgentConfig):
    """
    Configuration for React Agent, extending SimpleAgentConfig.
    
    React Agent routes between an LLM and tools to perform multi-step
    reasoning and action to accomplish tasks.
    """
    # Override state schema with ReactAgentState
    state_schema: Type[BaseModel] = Field(default=ReactAgentState)
    
    # Tool configuration
    tools: List[Union[BaseTool, Dict[str, Any]]] = Field(
        default_factory=list,
        description="Tools available to the agent"
    )
    
    # Agent configuration
    max_iterations: int = Field(
        default=10,
        description="Maximum number of iterations for the agent"
    )
    
    # Structured output
    structured_output_schema: Optional[Type[BaseModel]] = Field(
        default=None,
        description="Schema for structured output"
    )
    
    # Prompt configuration
    system_prompt: Optional[str] = Field(
        default=None,
        description="System prompt for the agent"
    )
    
    tool_choice: Optional[Union[Literal["auto", "any", "none"], Dict[str, Any]]] = Field(
        default="auto",
        description="Tool choice configuration for the LLM"
    )
    
    # Node names for the graph
    llm_node_name: str = Field(default="agent")
    tool_node_name: str = Field(default="execute_tools")
    router_node_name: str = Field(default="route")
    output_node_name: str = Field(default="structured_output")
    
    @model_validator(mode="after")
    def ensure_valid_configuration(self):
        """Validate the configuration."""
        if not self.tools and not hasattr(self, 'tool_node'):
            # Warning rather than error to allow dynamic tool loading
            import logging
            logging.warning("No tools provided for React Agent")
        
        # Set react-specific prompt if not provided
        if not self.system_prompt:
            self.system_prompt = """You are a helpful AI assistant. 
            
Answer the human's questions thoughtfully and accurately.
            
When you need more information or need to perform an action:
1. Use the available tools to gather information or perform actions
2. Always think step-by-step about what information you need
3. After using tools, reflect on the results before deciding next steps
4. Provide a final answer when you have enough information"""
        
        return self