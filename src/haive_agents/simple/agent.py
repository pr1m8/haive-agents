# src/haive/agents/simple/agent.py

from typing import Any, Dict, List, Optional, Type, Union, TypedDict    
import logging
from datetime import datetime

from pydantic import BaseModel, Field
from haive_agents.plan_and_execute.aug_llms import planner_aug_llm_config
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, SystemMessage, BaseMessage, HumanMessage
from langgraph.graph import END, add_messages, START

from haive_core.engine.agent.agent2 import Agent, AgentConfig, register_agent
from haive_core.engine.aug_llm import AugLLMConfig
from haive_core.models.llm.base import AzureLLMConfig, LLMConfig
from haive_core.graph.dynamic_graph_builder import DynamicGraph
from typing import Annotated, Sequence
from haive_agents.simple.state import SimpleAgentState
from haive_agents.simple.config import SimpleAgentConfig
from haive_core.schema.schema_composer import SchemaComposer
from haive_core.engine.agent.persistence.types import CheckpointerType
from haive_core.engine.agent.persistence import MemoryCheckpointerConfig

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
    def setup_workflow(self) -> None:
        """Set up a simple single-node workflow."""
        logger.debug(f"Setting up workflow for SimpleAgent {self.config.name}")
        
        # Create a DynamicGraph with the agent's engine_configs and schema
        graph_builder = DynamicGraph(
            name=self.config.name,
            components=[self.config.engine],  # Use engine_configs instead of engines
            state_schema=self.state_schema,
            default_runnable_config=self.runnable_config
        )
        
        # Log the schema for debugging
        logger.debug(f"State schema: {self.state_schema}")
        
        # Add default routing with main engine config
        if self.config.engine:
            # Explicitly create the node config to ensure END is properly set
            from langgraph.graph import END
            
            graph_builder.add_node(
                name="process",
                config=self.config.engine,  # Use engine_config instead of engine
                command_goto=END  # Make sure END is properly imported and used
            )
            
            # Explicitly add edge from START to process
            graph_builder.add_edge(START, "process")
            
            # Explicitly add edge from process to END 
            graph_builder.add_edge("process", END)
            
            # Set entry point (this is redundant but makes it explicit)
            graph_builder.set_entry_point("process")
            
            # Verify edges were added
            logger.debug(f"Edges in graph: {graph_builder.edges}")
        else:
            logger.warning(f"No 'main' engine found in engine_configs. Available: {list(self.engine_configs.keys())}")
        
        # Build the graph - use build instead of build_graph
        self.graph = graph_builder.build()
        
        # Log graph structure
        logger.debug(f"Graph structure: START -> process -> END")
        
        logger.info(f"Set up simple workflow for {self.config.name} with node process")

from pydantic import BaseModel,Field
from typing import Annotated
from langchain_core.messages import BaseMessage
from typing import Sequence
from langgraph.graph import add_messages

# =============================================
# Default State Schema
# =============================================
class SimpleAgentState(BaseModel):
    """Default schema for simple agents."""
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(
        default=[],
        description="Messages in the conversation"
    )
    
# Create SimpleAgentConfig with explicit memory persistence

a = SimpleAgent(config=SimpleAgentConfig(name="test"))
# Use the correct parameter name "input_data" instead of "input"
d = a.run(input_data={"messages": [HumanMessage(content="Hello, world!")]})
