#!/usr/bin/env python3
"""
Test script for the improved SimpleAgent with schema handling capabilities.

This script demonstrates:
1. Creating agents with various schema configurations
2. Using structured output models
3. Different agent creation methods
4. Examining derived schemas
5. Running agents with different input formats
"""

import logging
import sys
from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.utils.pydantic_utils import display_model, display_code, pretty_print

from haive.agents.simple.agent import SimpleAgent
from haive.agents.simple.config import SimpleAgentConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("simple_agent_test")

# Define structured output models
class Plan(BaseModel):
    """Structured plan with steps and reasoning."""
    steps: List[str] = Field(description="A list of concrete steps to complete the task")
    reasoning: str = Field(description="Explanation of the overall approach")

class CreativeIdea(BaseModel):
    """Creative idea with concept, benefits and implementation."""
    concept: str = Field(description="The core idea concept")
    benefits: List[str] = Field(description="Benefits of this idea")
    implementation: List[str] = Field(description="How to implement this idea")

# Define custom input schema
class PlanningInput(BaseModel):
    """Input schema for planning tasks."""
    goal: str = Field(description="The goal to plan for")
    constraints: Optional[List[str]] = Field(default=None, description="Constraints to consider")
    deadline: Optional[str] = Field(default=None, description="When the plan needs to be completed")
    
# Define custom message schema
class MessageInput(BaseModel):
    """Input schema with messages field."""
    messages: List[Any] = Field(default_factory=list, description="Conversation messages")
    context: Optional[str] = Field(default=None, description="Additional context for the conversation")

def test_basic_agent():
    """Test a basic SimpleAgent with auto-derived schemas."""
    logger.info("Testing basic SimpleAgent with auto-derived schemas")
    
    # Create AugLLMConfig
    aug_llm = AugLLMConfig(
        name="basic_llm",
        model="gpt-4o",
        system_prompt="You are a helpful assistant."
    )
    
    # Create SimpleAgentConfig with auto-derived schemas
    config = SimpleAgentConfig.from_aug_llm(
        aug_llm=aug_llm, 
        name="basic_agent"
    )
    
    # Create agent
    agent = SimpleAgent(config)
    
    # Print info about schemas
    print("\n===== Basic Agent Schemas =====")
    print(f"Input Schema: {config.input_schema.__name__ if config.input_schema else 'None'}")
    print(f"Output Schema: {config.output_schema.__name__ if config.output_schema else 'None'}")
    print(f"State Schema: {config.state_schema.__name__ if config.state_schema else 'None'}")
    
    # Run the agent
    result = agent.run("What are the three laws of robotics?")
    print("\n===== Basic Agent Result =====")
    pretty_print(result, "Basic Agent Result")
    
    return agent

def test_structured_output_agent():
    """Test a SimpleAgent with structured output model."""
    logger.info("Testing SimpleAgent with structured output model")
    
    # Create agent directly with structured output model
    agent = SimpleAgentConfig.with_structured_output(
        output_model=Plan,
        system_prompt="You are a planning assistant that creates detailed step-by-step plans.",
        name="planning_agent"
    ).build_agent()
    
    # Print info about schemas
    print("\n===== Planning Agent Schemas =====")
    print(f"Input Schema: {agent.config.input_schema.__name__ if agent.config.input_schema else 'None'}")
    print(f"Output Schema: {agent.config.output_schema.__name__ if agent.config.output_schema else 'None'}")
    print(f"State Schema: {agent.config.state_schema.__name__ if agent.config.state_schema else 'None'}")
    
    # Show the Plan model definition
    print("\n===== Plan Model Definition =====")
    display_code(Plan, "Plan Model")
    
    # Run the agent
    result = agent.run("Create a plan for launching a small online business")
    print("\n===== Planning Agent Result =====")
    pretty_print(result, "Planning Result")
    
    # Demonstrate that the result is a Plan instance
    if isinstance(result, Plan):
        print("\nThe result is a valid Plan instance")
        print(f"Number of steps: {len(result.steps)}")
        print(f"First step: {result.steps[0] if result.steps else 'No steps'}")
    
    return agent

def test_custom_input_schema():
    """Test a SimpleAgent with custom input schema."""
    logger.info("Testing SimpleAgent with custom input schema")
    
    # Create agent with custom input schema
    config = SimpleAgentConfig.from_scratch(
        system_prompt="You are a planning assistant that creates detailed plans based on goals and constraints.",
        input_schema=PlanningInput,
        structured_output_model=Plan,
        name="custom_input_agent"
    )
    
    # Create agent
    agent = SimpleAgent(config)
    
    # Print info about schemas
    print("\n===== Custom Input Agent Schemas =====")
    print(f"Input Schema: {config.input_schema.__name__ if config.input_schema else 'None'}")
    print(f"Output Schema: {config.output_schema.__name__ if config.output_schema else 'None'}")
    print(f"State Schema: {config.state_schema.__name__ if config.state_schema else 'None'}")
    
    # Show the input schema definition
    print("\n===== Custom Input Schema Definition =====")
    display_model(PlanningInput, "Planning Input Schema")
    
    # Run with structured input
    input_data = PlanningInput(
        goal="Learn to play the piano", 
        constraints=["Limited to 30 minutes practice per day", "No prior musical experience"],
        deadline="3 months"
    )
    
    result = agent.run(input_data)
    print("\n===== Custom Input Agent Result =====")
    pretty_print(result, "Planning Result")
    
    return agent

def test_schema_composition():
    """Test schema composition with SimpleAgent."""
    logger.info("Testing schema composition with SimpleAgent")
    
    # Create AugLLMConfig with structured output
    aug_llm = AugLLMConfig(
        name="creative_llm",
        model="gpt-4o",
        temperature=0.7,
        system_prompt="You are a creative assistant that generates innovative ideas.",
        structured_output_model=CreativeIdea
    )
    
    # Use SchemaComposer to examine schemas
    schema_composer = SchemaComposer.from_components([aug_llm])
    
    # Print schema composer info
    print("\n===== Schema Composer Information =====")
    print(f"Derived fields: {list(schema_composer.fields.keys())}")
    
    # Create state schema from composer
    state_schema = schema_composer.build()
    print(f"Created state schema: {state_schema.__name__}")
    
    # Create input/output schemas
    input_schema = schema_composer.create_input_schema()
    output_schema = schema_composer.create_output_schema()
    
    print(f"Input schema: {input_schema.__name__}")
    display_model(input_schema, "Input Schema")
    
    print(f"Output schema: {output_schema.__name__}")
    display_model(output_schema, "Output Schema")
    
    # Create agent using the composed schemas
    config = SimpleAgentConfig(
        engine=aug_llm,
        state_schema=state_schema,
        input_schema=input_schema, 
        output_schema=CreativeIdea,  # Use the structured model directly
        name="composed_schema_agent"
    )
    
    agent = SimpleAgent(config)
    
    # Run the agent
    result = agent.run("Generate a creative idea for reducing plastic waste in everyday life")
    print("\n===== Schema Composition Agent Result =====")
    pretty_print(result, "Creative Idea")
    
    return agent

def test_all():
    """Run all SimpleAgent tests."""
    print("\n\n" + "="*50)
    print("RUNNING SIMPLE AGENT TESTS")
    print("="*50 + "\n")
    
    test_basic_agent()
    test_structured_output_agent()
    test_custom_input_schema()
    test_schema_composition()
    
    print("\n\n" + "="*50)
    print("ALL TESTS COMPLETED")
    print("="*50 + "\n")

if __name__ == "__main__":
    test_all()