# =============================================
# Helper Functions
# =============================================
from typing import Optional
from pydantic import BaseModel
from haive_core.engine.aug_llm import AugLLMConfig
from haive_agents.simple.agent import SimpleAgent
from haive_agents.simple.config import SimpleAgentConfig   

def create_simple_agent(
    system_prompt: Optional[str] = "You are a helpful assistant.",
    model: str = "gpt-4o",
    temperature: float = 0.7,
    name: Optional[str] = None,
    engine: Optional[AugLLMConfig] = None,
    visualize: bool = True,
    structured_output_model: Optional[BaseModel] = None,
    **kwargs
) -> SimpleAgent:
    """
    Create a simple agent with minimal configuration.
    
    Args:
        system_prompt: Optional system prompt
        model: Model name to use (if engine not provided)
        temperature: Temperature for generation (if engine not provided)
        name: Optional name for the agent
        engine: Optional existing AugLLMConfig to use
        visualize: Whether to generate a visualization
        **kwargs: Additional configuration parameters
        
    Returns:
        SimpleAgent instance
    """
    if engine:
        # Create from existing AugLLMConfig
        config = SimpleAgentConfig.from_aug_llm(
            aug_llm=engine,
            name=name,
            system_prompt=system_prompt,
            visualize=visualize,
            #structured_output_model=structured_output_model,
            **kwargs
        )
    else:
        # Create from scratch
        config = SimpleAgentConfig.from_scratch(
            system_prompt=system_prompt,
            model=model,
            temperature=temperature,
            name=name,
            visualize=visualize,
            structured_output_model=structured_output_model,
            **kwargs
        )
    
    # Build and return the agent
    return config.build_agent()
