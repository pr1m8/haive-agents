# src/haive/agents/simple/agent.py

from typing import Any, Dict, List, Optional, Type, Union, TypedDict    
import logging
from datetime import datetime

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, SystemMessage, BaseMessage, HumanMessage
from langgraph.graph import END, add_messages

from haive.core.engine.agent.agent import Agent, AgentConfig, register_agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.config import NodeConfig
from haive.core.models.llm.base import AzureLLMConfig
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from typing import Annotated, Sequence
from haive.agents.simple.state import SimpleAgentState
from haive.agents.simple.config import SimpleAgentConfig

# Set up logging
logger = logging.getLogger(__name__)

# =============================================
# Simple Agent Implementation
# =============================================
@register_agent(SimpleAgentConfig)
class SimpleAgent(Agent[SimpleAgentConfig]):
    """
    A simple agent with a single node workflow.
    
    This agent processes input through one node that uses the engine
    to generate a response. No complex routing or tools are supported.
    """
    def __init__(self, config: SimpleAgentConfig=SimpleAgentConfig()):
        super().__init__(config)
        # Initialize any SimpleAgent-specific attributes here
        
    def setup_workflow(self) -> None:
        """Set up a simple single-node workflow with intelligent mapping derivation."""
        logger.info(f"Setting up workflow for {self.config.name}")
        
        # Create DynamicGraph with proper component registration
        gb = DynamicGraph(
            name=self.config.name,
            components=[self.config.engine],
            state_schema=self.config.state_schema
        )
        
        # Initialize mappings
        input_mapping = self.config.input_mapping
        output_mapping = self.config.output_mapping
        
        # Enhanced engine field detection
        engine = self.config.engine
        
        # Intelligently detect structured output model
        structured_model = None
        structured_model_name = None
        if hasattr(engine, "structured_output_model") and engine.structured_output_model:
            structured_model = engine.structured_output_model
            structured_model_name = structured_model.__name__.lower()
            logger.debug(f"Detected structured output model: {structured_model_name}")
        
        # If no input mapping is provided, derive it from engine
        if not input_mapping:
            # Try to get input fields directly from engine
            if hasattr(engine, "get_input_fields") and callable(engine.get_input_fields):
                try:
                    engine_input_fields = engine.get_input_fields()
                    input_mapping = {k: k for k in engine_input_fields.keys()}
                    logger.debug(f"Auto-derived input mapping from engine fields: {input_mapping}")
                except Exception as e:
                    logger.warning(f"Could not auto-derive input mapping from engine: {e}")
                    
            # Fall back to prompt variables if available
            if not input_mapping and hasattr(engine, "prompt_template") and hasattr(engine.prompt_template, "input_variables"):
                prompt_vars = engine.prompt_template.input_variables
                input_mapping = {var: var for var in prompt_vars}
                logger.debug(f"Auto-derived input mapping from prompt variables: {input_mapping}")
        
        # If no output mapping is provided, derive it intelligently
        if not output_mapping:
            # First try to get output fields directly from engine
            if hasattr(engine, "get_output_fields") and callable(engine.get_output_fields):
                try:
                    engine_output_fields = engine.get_output_fields()
                    
                    # Handle structured output model specially
                    if structured_model:
                        # Map the model itself to the corresponding state field
                        output_mapping = {structured_model_name: structured_model_name}
                        logger.debug(f"Auto-derived output mapping for structured model: {output_mapping}")
                    else:
                        # Map all output fields 1:1
                        output_mapping = {k: k for k in engine_output_fields.keys()}
                        logger.debug(f"Auto-derived output mapping from engine fields: {output_mapping}")
                except Exception as e:
                    logger.warning(f"Could not auto-derive output mapping from engine: {e}")
            
            # Fall back to structured model-based mapping
            if not output_mapping and structured_model:
                output_mapping = {structured_model_name: structured_model_name}
                logger.debug(f"Fall back to structured model mapping: {output_mapping}")
            
            # Final fallback to a reasonable default
            if not output_mapping:
                output_mapping = {"content": "output"}
                logger.debug(f"Using default output mapping: {output_mapping}")
        
        # Log the node creation with mappings
        logger.debug(f"Adding processing node: {self.config.node_name}")
        logger.debug(f"Using input_mapping: {input_mapping}")
        logger.debug(f"Using output_mapping: {output_mapping}")
        
        # Add the node with explicit mappings and END routing
        gb.add_node(
            name=self.config.node_name,
            config=self.config.engine,
            command_goto=END,
            input_mapping=input_mapping,
            output_mapping=output_mapping
        )
        
        # Set entry point
        logger.debug(f"Setting entry point to: {self.config.node_name}")
        gb.set_entry_point(self.config.node_name)
        
        # Get the built graph (not compiled yet)
        self.graph = gb.build()
        
        logger.info(f"Workflow setup complete for {self.config.name}")