"""
Simple agent implementation with comprehensive schema handling.

This module defines a basic single-node agent that uses AugLLMConfig for reasoning,
with support for structured outputs, schema composition, and explicit input/output schemas.
"""

import logging
from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END

from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from haive.agents.simple.config import SimpleAgentConfig

# Set up logging
logger = logging.getLogger(__name__)

@register_agent(SimpleAgentConfig)
class SimpleAgent(Agent[SimpleAgentConfig]):
    """
    A simple agent with a single node workflow and comprehensive schema handling.
    
    Features:
    - Single processing node using AugLLMConfig
    - Support for explicit input/output schemas
    - Automatic schema derivation from engine
    - Intelligent input/output mapping
    - Structured output support
    """
    
    def __init__(self, config: SimpleAgentConfig):
        """
        Initialize the SimpleAgent with configuration.
        
        Args:
            config: SimpleAgentConfig instance
        """
        super().__init__(config)
    
    def setup_workflow(self) -> None:
        """
        Set up a single-node workflow with the configured schemas and mappings.
        
        This creates a simple graph with one processing node that handles:
        - Receiving input according to input schema
        - Processing with the AugLLM engine
        - Outputting results according to output schema
        """
        logger.info(f"Setting up workflow for {self.config.name}")
        
        # Create DynamicGraph with state schema
        gb = DynamicGraph(
            name=self.config.name,
            components=[self.config.engine],
            state_schema=self.config.state_schema,
            visualize=self.config.visualize
        )
        
        # Get mappings from config (handles auto-derivation)
        input_mapping = self.config.derive_input_mapping()
        output_mapping = self.config.derive_output_mapping()
        
        logger.debug(f"Using input mapping: {input_mapping}")
        logger.debug(f"Using output mapping: {output_mapping}")
        
        # Add the processing node
        gb.add_node(
            name=self.config.node_name,
            config=self.config.engine,
            command_goto=END,
            input_mapping=input_mapping,
            output_mapping=output_mapping
        )
        
        # Set entry point
        gb.set_entry_point(self.config.node_name)
        
        # Get the built graph
        self.graph = gb.build()
        
        logger.info(f"Workflow setup complete for {self.config.name}")
    
    def run(self, input_data: Any) -> Any:
        """
        Run the agent with the provided input.
        
        Supports various input formats:
        - String: Converted to a HumanMessage
        - List[BaseMessage]: Used directly
        - Dict: Used as-is
        - Pydantic model: Converted to dict
        
        Args:
            input_data: Input in various formats
            
        Returns:
            Agent result, potentially in structured format based on output_schema
        """
        # Ensure graph is compiled
        self.compile()
        
        # Process different input types
        processed_input = self._prepare_input(input_data)
        
        # Invoke the graph
        result = self.graph.invoke(processed_input)
        
        # Process the result if needed
        return self._process_output(result)
    
    def _prepare_input(self, input_data: Any) -> Dict[str, Any]:
        """
        Prepare input for the agent in the correct format.
        
        Args:
            input_data: Raw input in various formats
            
        Returns:
            Properly formatted input dictionary
        """
        # Handle string input (convert to message)
        if isinstance(input_data, str):
            return {"messages": [HumanMessage(content=input_data)]}
        
        # Handle list of messages
        if isinstance(input_data, list) and all(isinstance(m, BaseMessage) for m in input_data):
            return {"messages": input_data}
        
        # Handle dictionary input
        if isinstance(input_data, dict):
            # If no messages field, try to create one from other fields
            if "messages" not in input_data and self.has_messages_input():
                for field in ["input", "query", "content"]:
                    if field in input_data and isinstance(input_data[field], str):
                        input_data["messages"] = [HumanMessage(content=input_data[field])]
                        break
            return input_data
        
        # Handle Pydantic model input
        if isinstance(input_data, BaseModel):
            # If it matches our input schema, use it directly
            if self.config.input_schema and isinstance(input_data, self.config.input_schema):
                model_dict = input_data.model_dump()
                return model_dict
            
            # Otherwise convert to dict and process
            model_dict = input_data.model_dump()
            return self._prepare_input(model_dict)
        
        # Default case: wrap in dictionary
        return {"input": input_data}
    
    def _process_output(self, result: Any) -> Any:
        """
        Process the output to ensure it conforms to the output schema.
        
        Args:
            result: Raw result from the graph
            
        Returns:
            Processed result, potentially converted to output schema
        """
        # If we have a structured output model, try to validate against it
        if self.config.output_schema and isinstance(result, dict):
            try:
                # Check if output matches output schema fields
                fields = set(self.config.output_schema.model_fields.keys())
                
                # Find if we have model name as key for structured output
                model_name = self.config.output_schema.__name__.lower()
                if model_name in result and isinstance(result[model_name], dict):
                    # Convert to output schema model
                    return self.config.output_schema.model_validate(result[model_name])
                
                # Check if result contains all fields in output schema
                if all(field in result for field in fields):
                    # Filter to just the schema fields
                    schema_data = {field: result[field] for field in fields if field in result}
                    return self.config.output_schema.model_validate(schema_data)
            except Exception as e:
                logger.warning(f"Failed to convert result to output schema: {e}")
                
        # Return the raw result if no conversion applies
        return result
    
    def has_messages_input(self) -> bool:
        """
        Check if this agent accepts a 'messages' input.
        
        Returns:
            True if agent has a messages field in input schema
        """
        # Check input schema if available
        if self.config.input_schema:
            return "messages" in self.config.input_schema.model_fields
            
        # Check input mapping if available
        if self.config.input_mapping:
            return "messages" in self.config.input_mapping
            
        # Default assumption
        return True