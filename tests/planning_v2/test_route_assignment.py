#!/usr/bin/env python3
"""Test to verify what route structured output models get."""

from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig

class Task(BaseModel):
    description: str = Field(description="Task")

class Plan[T](BaseModel):
    objective: str = Field(description="Objective")
    steps: List[T] = Field(description="Steps", max_length=2)

def test_route_assignment():
    """Check what route Plan[Task] gets."""
    print("\n=== ROUTE ASSIGNMENT TEST ===\n")
    
    # Create config with structured output
    config = AugLLMConfig(structured_output_model=Plan[Task])
    
    print("1. Tool routes:")
    for name, route in config.tool_routes.items():
        print(f"   {name} → {route}")
    
    print(f"\n2. Structured output model: {config.structured_output_model}")
    
    # Check metadata
    print("\n3. Tool metadata:")
    for name, metadata in config.tool_metadata.items():
        print(f"   {name}:")
        for key, value in metadata.items():
            print(f"      {key}: {value}")
    
    # The key finding
    if "plan_task_generic" in config.tool_routes:
        route = config.tool_routes["plan_task_generic"]
        print(f"\n🎯 KEY FINDING: plan_task_generic gets route: {route}")
        
        if route == "parse_output":
            print("   ✅ This is CORRECT for structured output!")
        else:
            print(f"   ❌ Expected 'parse_output' but got '{route}'")

if __name__ == "__main__":
    test_route_assignment()