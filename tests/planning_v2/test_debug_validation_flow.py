#!/usr/bin/env python3
"""Debug test to trace validation flow for Plan[Task] structured output."""

import logging
from typing import List
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# Focus on key components
for logger_name in [
    'haive.agents.simple.agent',
    'haive.core.graph.node.validation_node_config_v2',
    'haive.core.graph.node.validation_node_v2',
    'haive.core.common.mixins.tool_route_mixin',
    'haive.core.common.mixins.structured_output_mixin',
    'haive.core.engine.aug_llm.config',
    'langgraph.prebuilt.tool_validator'
]:
    logging.getLogger(logger_name).setLevel(logging.DEBUG)

print("\n" + "="*80)
print("DEBUGGING VALIDATION FLOW FOR Plan[Task]")
print("="*80)

# Define generic models like in planning_v2
class Task(BaseModel):
    """A single task."""
    description: str = Field(description="Task description")
    priority: int = Field(default=1, ge=1, le=5)

class Plan[T](BaseModel):
    """Generic plan container."""
    objective: str = Field(description="Overall objective")
    steps: List[T] = Field(description="List of steps")

# Create concrete version for comparison
class TaskPlan(BaseModel):
    """Concrete task plan."""
    objective: str = Field(description="Overall objective") 
    steps: List[Task] = Field(description="List of tasks")

async def test_generic_validation():
    """Test validation with generic Plan[Task]."""
    print("\n1️⃣ Testing Generic Plan[Task]")
    print("-" * 40)
    
    # Create config with generic structured output
    config = AugLLMConfig(
        temperature=0.1,
        structured_output_model=Plan[Task]
    )
    
    print(f"Structured output model: {config.structured_output_model}")
    print(f"Tool routes: {config.tool_routes}")
    print(f"Tools: {[t.name if hasattr(t, 'name') else str(t) for t in config.tools]}")
    
    # Check what name the model gets
    model_name = getattr(Plan[Task], '__name__', 'NO_NAME')
    print(f"\nModel __name__: {model_name}")
    
    # Check if sanitization happens
    from haive.core.utils.naming import sanitize_tool_name
    sanitized = sanitize_tool_name(model_name)
    print(f"Sanitized name: {sanitized}")
    
    # Create agent
    agent = SimpleAgent(
        name="test_planner",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a task planner."),
            ("human", "Create a plan for: {objective}")
        ])
    )
    
    print(f"\nAgent created. Checking graph...")
    print(f"Graph nodes: {list(agent.graph.nodes)}")
    
    # Try to run - this should trigger the validation error
    try:
        result = await agent.arun({
            "objective": "Debug validation error"
        })
        print(f"✅ Success! Result type: {type(result)}")
        return result
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return None

async def test_concrete_validation():
    """Test validation with concrete TaskPlan for comparison."""
    print("\n\n2️⃣ Testing Concrete TaskPlan") 
    print("-" * 40)
    
    config = AugLLMConfig(
        temperature=0.1,
        structured_output_model=TaskPlan
    )
    
    print(f"Structured output model: {config.structured_output_model}")
    print(f"Tool routes: {config.tool_routes}")
    
    agent = SimpleAgent(
        name="test_planner_concrete",
        engine=config,
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a task planner."),
            ("human", "Create a plan for: {objective}")
        ])
    )
    
    try:
        result = await agent.arun({
            "objective": "Debug validation error"
        })
        print(f"✅ Success! Result type: {type(result)}")
        return result
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
        return None

async def test_route_analysis():
    """Analyze routes for both models."""
    print("\n\n3️⃣ Route Analysis")
    print("-" * 40)
    
    # Generic model
    config1 = AugLLMConfig(structured_output_model=Plan[Task])
    print(f"Plan[Task] routes: {config1.tool_routes}")
    
    # Concrete model  
    config2 = AugLLMConfig(structured_output_model=TaskPlan)
    print(f"TaskPlan routes: {config2.tool_routes}")
    
    # Check route metadata
    print(f"\nPlan[Task] metadata: {config1.tool_route_metadata.get(list(config1.tool_routes.keys())[0])}")
    print(f"TaskPlan metadata: {config2.tool_route_metadata.get('TaskPlan')}")

if __name__ == "__main__":
    import asyncio
    
    asyncio.run(test_generic_validation())
    asyncio.run(test_concrete_validation())
    asyncio.run(test_route_analysis())
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)