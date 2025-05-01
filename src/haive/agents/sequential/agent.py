"""
SequentialAgent implementation that connects components in a linear workflow.

This module defines the SequentialAgent class which constructs a linear
workflow graph from a sequence of engine components.
"""

import logging
from typing import Any, Dict, List, Optional

from langgraph.graph import END, StateGraph

from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from haive.agents.sequential.config import SequentialAgentConfig, StepConfig

logger = logging.getLogger(__name__)

@register_agent(SequentialAgentConfig)
class SequentialAgent(Agent[SequentialAgentConfig]):
    """
    A sequential agent that connects components in a linear workflow.
    
    This agent automatically builds a linear graph from a sequence of
    components, handling the connections between them and managing state flow.
    
    Features:
    - Automatic connection of components in sequence
    - Auto-derived input/output mappings between steps
    - Support for any engine components (AugLLMConfig, etc.)
    - Schema derivation from all components
    """
    
    def __init__(self, config: SequentialAgentConfig):
        """
        Initialize the SequentialAgent with configuration.
        
        Args:
            config: SequentialAgentConfig instance
        """
        super().__init__(config)
    
    def setup_workflow(self) -> None:
        """
        Build a linear workflow from the sequence of components.
        
        This method:
        1. Creates a DynamicGraph with all components
        2. Adds each step as a node with appropriate mappings
        3. Connects the nodes in sequential order
        4. Sets the entry point
        """
        logger.info(f"Setting up sequential workflow for {self.config.name}")
        
        # Create DynamicGraph with all components
        gb = DynamicGraph(
            name=self.config.name,
            components=self.config.components,
            state_schema=self.config.state_schema,
            visualize=self.config.visualize
        )
        
        # Add each step as a node
        for i, step in enumerate(self.config.steps):
            # Get or derive input/output mappings
            input_mapping = step.input_mapping
            output_mapping = step.output_mapping
            
            # Add the node
            logger.debug(f"Adding step node: {step.name}")
            gb.add_node(
                name=step.name,
                config=step.component,
                # Last step goes to END, others connect to next step
                command_goto=END if i == len(self.config.steps) - 1 else None,
                input_mapping=input_mapping,
                output_mapping=output_mapping
            )
        
        # Connect the nodes in sequence
        for i in range(len(self.config.steps) - 1):
            current_step = self.config.steps[i]
            next_step = self.config.steps[i + 1]
            
            logger.debug(f"Connecting: {current_step.name} -> {next_step.name}")
            gb.add_edge(current_step.name, next_step.name)
        
        # Set entry point (first step by default)
        entry_node = self.config.entry_point or self.config.steps[0].name
        gb.set_entry_point(entry_node)
        
        # Get the built graph
        self.graph = gb.build()
        
        logger.info(f"Sequential workflow setup complete for {self.config.name} with {len(self.config.steps)} steps")
    
    def get_step_outputs(self, step_name: str, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract outputs produced by a specific step from the state.
        
        Args:
            step_name: Name of the step
            state: Current state dictionary
            
        Returns:
            Dictionary of outputs from the step
        """
        step = self.config.get_step_by_name(step_name)
        if not step:
            logger.warning(f"Step '{step_name}' not found")
            return {}
            
        # If no explicit output mapping, try to derive
        if not step.output_mapping:
            # Try to get output fields from component
            if hasattr(step.component, "get_output_fields"):
                try:
                    output_fields = step.component.get_output_fields()
                    # Extract these fields from state
                    return {k: state.get(k) for k in output_fields.keys() if k in state}
                except Exception as e:
                    logger.warning(f"Failed to get output fields: {e}")
        else:
            # Use explicit mapping to find outputs
            # Output mapping is from component field -> state field
            # We need to reverse it to extract from state
            reverse_mapping = {v: k for k, v in step.output_mapping.items()}
            return {comp_field: state.get(state_field) 
                   for state_field, comp_field in reverse_mapping.items() 
                   if state_field in state}
                   
        # Fallback to just returning structured outputs if present
        if hasattr(step.component, "structured_output_model"):
            model = step.component.structured_output_model
            if model:
                model_name = model.__name__.lower()
                if model_name in state:
                    return {model_name: state[model_name]}
        
        # Couldn't determine outputs
        return {}
    
    def explain_workflow(self) -> str:
        """
        Generate a human-readable explanation of the workflow.
        
        Returns:
            String explanation of the workflow steps
        """
        explanation = [f"Sequential Workflow: {self.config.name}"]
        explanation.append("=" * len(explanation[0]))
        explanation.append("")
        
        # Add information about each step
        for i, step in enumerate(self.config.steps, 1):
            # Get component info
            component_type = step.component.__class__.__name__
            component_name = getattr(step.component, "name", "unnamed")
            
            # Add step header
            explanation.append(f"Step {i}: {step.name}")
            explanation.append(f"Component: {component_type} ({component_name})")
            
            # Add description if available
            if step.description:
                explanation.append(f"Description: {step.description}")
                
            # Add model info if it's an AugLLMConfig
            if hasattr(step.component, "model"):
                explanation.append(f"Model: {step.component.model}")
                
            # Add structured output info if available
            if hasattr(step.component, "structured_output_model") and step.component.structured_output_model:
                model = step.component.structured_output_model
                explanation.append(f"Structured Output: {model.__name__}")
                
            explanation.append("")  # Add blank line between steps
        
        return "\n".join(explanation)