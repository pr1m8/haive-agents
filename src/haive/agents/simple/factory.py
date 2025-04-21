"""Factory functions for SimpleAgent creation.

This module provides convenient factory functions for creating
SimpleAgent instances with various configurations.
"""

from typing import Any, Dict, List, Optional, Type, Union

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel

from haive.core.engine.agent.persistence.types import CheckpointerType
from haive.core.engine.agent.persistence import PostgresCheckpointerConfig, MemoryCheckpointerConfig
from haive.core.engine.base import Engine
from haive.core.engine.aug_llm.base import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig, OpenAILLMConfig, AnthropicLLMConfig

from haive.agents.simple.config import SimpleAgentConfig
from haive.agents.simple.agent import SimpleAgent


def create_simple_agent(
    name: str = "simple_agent",
    system_prompt: Optional[str] = None,
    engine: Optional[Union[Engine, str]] = None,
    persistence_type: str = "postgres",
    persistence_config: Optional[Dict[str, Any]] = None,
    structured_output_model: Optional[Type[BaseModel]] = None,
    visualize: bool = True,
    debug: bool = False,
    **kwargs
) -> SimpleAgent:
    """
    Create a SimpleAgent with the specified configuration.
    
    Args:
        name: Name for the agent
        system_prompt: Optional system prompt for the LLM
        engine: Optional custom engine (if not provided, creates a default AugLLMConfig)
        persistence_type: Type of persistence ("postgres", "memory", or "none")
        persistence_config: Optional configuration for persistence
        structured_output_model: Optional pydantic model for structured output
        visualize: Whether to generate visualizations
        debug: Whether to enable debug mode
        **kwargs: Additional parameters for SimpleAgentConfig
        
    Returns:
        Instantiated SimpleAgent
    """
    # Handle persistence configuration
    persistence = None
    if persistence_type.lower() == "postgres":
        try:
            persistence = PostgresCheckpointerConfig(**(persistence_config or {}))
        except ImportError:
            # Fall back to memory if PostgreSQL is not available
            persistence = MemoryCheckpointerConfig()
    elif persistence_type.lower() == "memory":
        persistence = MemoryCheckpointerConfig()
    
    # Set up the engine if provided
    if engine is None and structured_output_model is not None:
        # Create a default engine with structured output
        default_prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt or "You are a helpful assistant."),
            ("human", "{input}")
        ])
        
        engine = AugLLMConfig(
            llm_config=AzureLLMConfig(),
            prompt_template=default_prompt,
            structured_output_model=structured_output_model
        )
    
    # Create agent config
    config = SimpleAgentConfig(
        name=name,
        system_prompt=system_prompt,
        engine=engine,
        persistence=persistence,
        visualize=visualize,
        debug=debug,
        **kwargs
    )
    
    # Build and return the agent
    return config.build_agent()

