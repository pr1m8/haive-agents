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
        
        # Extract configuration for the node
        input_mapping = self.config.input_mapping
        output_mapping = self.config.output_mapping
        
        # Create NodeConfig with debug enabled to detect mappings
        node_config = NodeConfig(
            name=self.config.node_name,
            engine=self.config.engine,
            command_goto="END",
            input_mapping=input_mapping,
            output_mapping=output_mapping,
            debug=True
        )
        
        # Extract prompt variables if available
        prompt_vars = []
        if hasattr(self.config.engine, "prompt_template") and hasattr(self.config.engine.prompt_template, "input_variables"):
            prompt_vars = self.config.engine.prompt_template.input_variables
            logger.debug(f"Prompt variables: {prompt_vars}")
        
        # Auto-derive input mapping if none provided but prompt has variables
        if not input_mapping and prompt_vars:
            input_mapping = {var: var for var in prompt_vars}
            logger.debug(f"Auto-derived input mapping: {input_mapping}")
        
        # Auto-derive output mapping based on structured output model if available
        if not output_mapping and hasattr(self.config.engine, "structured_output_model"):
            structured_model = self.config.engine.structured_output_model
            if structured_model:
                if isinstance(structured_model, type):
                    model_name = structured_model.__name__.lower()
                    output_mapping = {"result": model_name}
                    logger.debug(f"Auto-derived output mapping for structured model: {output_mapping}")
                else:
                    output_mapping = {"result": "result"}
        elif not output_mapping:
            # Default output mapping
            output_mapping = {"content": "output"}
        
        # Create DynamicGraph with proper component registration
        gb = DynamicGraph(
            name=self.config.name,
            components=[self.config.engine],
            state_schema=self.config.state_schema
        )
        
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