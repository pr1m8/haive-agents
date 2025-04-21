"""SimpleAgent implementation.

This module provides the SimpleAgent implementation, which offers a streamlined
single-node workflow for processing inputs through an LLM engine.
"""

import logging
from typing import Any, Dict, List, Optional

from langchain_core.messages import HumanMessage
from langgraph.graph import END, START
from langchain_core.output_parsers import StrOutputParser

from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.node.config import NodeConfig
from haive.core.engine.aug_llm.base import AugLLMConfig
from haive.agents.simple.config import SimpleAgentConfig
from haive.agents.simple.state import SimpleAgentState

# Set up logging
logger = logging.getLogger(__name__)


@register_agent(SimpleAgentConfig)
class SimpleAgent(Agent[SimpleAgentConfig]):
    """
    A simple agent with a single-node workflow.
    
    This agent processes input through one node that uses the provided engine
    to generate a response. It's designed for straightforward LLM interaction
    with minimal complexity.
    """
    
    def setup_workflow(self) -> None:
        """
        Set up a simple single-node workflow.
        
        This creates a graph with a single processing node that takes input from
        the state and returns output to the state.
        """
        logger.debug(f"Setting up workflow for SimpleAgent '{self.config.name}'")
        
        # Ensure we have a valid engine
        engine = self.engine_config
        
        # Configure input/output mapping based on config
        input_mapping = {self.config.input_key: "input"}
        
        # Create node configuration
        node_config = NodeConfig(
            name=self.config.node_name,
            engine=engine,
            command_goto=END,
            input_mapping=input_mapping
        )
        
        # Add the node to the graph
        self.graph_builder.add_node(self.config.node_name, node_config)
        
        # Add edge from START to our processing node
        self.graph_builder.add_edge(START, self.config.node_name)
        
        logger.info(f"Workflow setup complete for SimpleAgent '{self.config.name}'")

    def prepare_input(self, input_data: Any) -> Dict[str, Any]:
        """
        Prepare input data for the agent.
        
        This method converts various input formats into a suitable state format.
        
        Args:
            input_data: Input data in various formats
            
        Returns:
            Dictionary suitable for agent input
        """
        # Handle string input - convert to message
        if isinstance(input_data, str):
            return {"messages": [HumanMessage(content=input_data)]}
        
        # Handle dictionary input
        if isinstance(input_data, dict):
            # If input already has messages, use it directly
            if "messages" in input_data:
                return input_data
                
            # If input has a 'content' or 'query' field, convert to message
            for key in ["content", "query", "question", "input"]:
                if key in input_data and isinstance(input_data[key], str):
                    return {
                        "messages": [HumanMessage(content=input_data[key])],
                        **{k: v for k, v in input_data.items() if k != key}
                    }
            
            # Otherwise, pass through dictionary
            return input_data
            
        # Default handling for other types
        return {"messages": [HumanMessage(content=str(input_data))]}
        
    def run(self, input_data: Any, thread_id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Run the agent with input data.
        
        This method extends the base run method to handle input preprocessing.
        
        Args:
            input_data: Input data in various formats
            thread_id: Optional thread ID for persistence
            **kwargs: Additional parameters
            
        Returns:
            Output from the agent execution
        """
        # Prepare input in the correct format
        prepared_input = self.prepare_input(input_data)
        
        # Run the agent with prepared input
        return super().run(prepared_input, thread_id=thread_id, **kwargs)