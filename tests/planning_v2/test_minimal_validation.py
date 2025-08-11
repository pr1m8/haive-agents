#!/usr/bin/env python3
"""Minimal test to understand the validation issue."""

from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig

class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Overall objective")
    steps: List[T] = Field(description="List of steps", max_length=3)  # Limit steps

def test_basic_setup():
    """Test basic setup to understand the issue."""
    print("\n=== BASIC VALIDATION TEST ===\n")
    
    # 1. Create config with Plan[Task]
    config = AugLLMConfig(structured_output_model=Plan[Task])
    
    print("1. Tool routes in AugLLMConfig:")
    for name, route in config.tool_routes.items():
        print(f"   {name} -> {route}")
    
    print("\n2. The issue:")
    print("   - LLM calls tool with name: 'plan_task_generic'")
    print("   - Tool route exists for: 'plan_task_generic' -> 'parse_output'")
    print("   - But validation still fails with recursion")
    
    print("\n3. What we found:")
    print("   - ValidationNodeConfigV2 creates ToolMessage successfully")
    print("   - But graph routes back to agent_node instead of parse_output")
    print("   - This causes recursion")
    
    print("\n4. The fix we made:")
    print("   - Updated validation_router_v2.py to handle 'parse_output' route")
    print("   - But still getting 'Unknown tool' warning")
    
    print("\n5. Current status:")
    print("   - Need to find where 'Unknown tool' warning comes from")
    print("   - Need to verify routing actually goes to parse_output node")

if __name__ == "__main__":
    test_basic_setup()