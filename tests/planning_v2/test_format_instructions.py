#!/usr/bin/env python3
"""Test format instructions setup in AugLLMConfig."""

from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig

class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)

def test_format_instructions():
    """Test format instructions setup."""
    print("🔍 TESTING FORMAT INSTRUCTIONS SETUP")
    print("=" * 50)
    
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        temperature=0.1
    )
    
    # Check format instruction settings
    print("1. Format Instruction Settings:")
    print(f"   include_format_instructions: {config.include_format_instructions}")
    print(f"   structured_output_version: {config.structured_output_version}")
    
    # Check if format instructions were generated
    print(f"\n2. Format Instructions Status:")
    partial_vars = config.prompt_template.partial_variables
    print(f"   Partial variables keys: {list(partial_vars.keys())}")
    
    if "format_instructions" in partial_vars:
        instructions = partial_vars["format_instructions"]
        print(f"   ✅ Format instructions found ({len(instructions)} chars)")
        print(f"   Preview: {instructions[:200]}...")
    else:
        print(f"   ❌ Format instructions missing!")
        
        # Check internal state
        if hasattr(config, '_format_instructions_text'):
            internal_instructions = config._format_instructions_text
            print(f"   Internal instructions: {internal_instructions}")
    
    # Try to manually trigger format instructions setup
    print(f"\n3. Manual Setup Test:")
    try:
        config._setup_format_instructions()
        print(f"   Manual setup called")
        
        # Check again
        partial_vars = config.prompt_template.partial_variables
        if "format_instructions" in partial_vars:
            instructions = partial_vars["format_instructions"]
            print(f"   ✅ After manual setup: format_instructions found ({len(instructions)} chars)")
        else:
            print(f"   ❌ Still no format_instructions after manual setup")
            
    except Exception as e:
        print(f"   ❌ Manual setup failed: {e}")
    
    # Check if the issue is with v2 vs v1
    print(f"\n4. Version Comparison:")
    
    config_v1 = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v1",
        temperature=0.1
    )
    
    v1_partials = config_v1.prompt_template.partial_variables
    print(f"   V1 partial variables: {list(v1_partials.keys())}")
    
    if "format_instructions" in v1_partials:
        print(f"   ✅ V1 has format_instructions")
    else:
        print(f"   ❌ V1 also missing format_instructions")

if __name__ == "__main__":
    test_format_instructions()