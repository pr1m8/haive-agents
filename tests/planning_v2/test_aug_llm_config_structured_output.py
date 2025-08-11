#!/usr/bin/env python3
"""Test AugLLMConfig with structured output to verify correct setup."""

import pytest
from typing import List
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig

class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)

@pytest.fixture
def plan_task_model():
    """Fixture for Plan[Task] model."""
    return Plan[Task]

@pytest.fixture
def aug_llm_config_with_structured_output(plan_task_model):
    """Fixture for AugLLMConfig with structured output."""
    return AugLLMConfig(
        structured_output_model=plan_task_model,
        temperature=0.1
    )

def test_aug_llm_config_basic_setup(aug_llm_config_with_structured_output):
    """Test basic AugLLMConfig setup with structured output."""
    config = aug_llm_config_with_structured_output
    
    print("\n=== TESTING AugLLMConfig BASIC SETUP ===")
    
    # Test 1: Structured output model is set
    assert config.structured_output_model is not None
    print(f"✅ structured_output_model: {config.structured_output_model}")
    
    # Test 2: Force tool use should be True for structured output
    assert config.force_tool_use is True
    print(f"✅ force_tool_use: {config.force_tool_use}")
    
    # Test 3: Force tool choice should be set to sanitized name
    expected_tool_name = "plan_task_generic"  # Plan[Task] -> plan_task_generic
    assert config.force_tool_choice == expected_tool_name
    print(f"✅ force_tool_choice: {config.force_tool_choice}")

def test_aug_llm_config_tool_routes(aug_llm_config_with_structured_output):
    """Test that AugLLMConfig sets up correct tool routes."""
    config = aug_llm_config_with_structured_output
    
    print("\n=== TESTING TOOL ROUTES ===")
    
    # Test 1: Tool routes should contain sanitized name
    print(f"All tool routes: {config.tool_routes}")
    
    assert "plan_task_generic" in config.tool_routes
    print(f"✅ plan_task_generic route exists")
    
    # Test 2: Route should be 'parse_output' for structured output
    route = config.tool_routes["plan_task_generic"]
    assert route == "parse_output", f"Expected 'parse_output' but got '{route}'"
    print(f"✅ plan_task_generic → {route}")
    
    # Test 3: Should not have pydantic_model route for structured output
    pydantic_routes = {k: v for k, v in config.tool_routes.items() if v == "pydantic_model"}
    if pydantic_routes:
        print(f"⚠️  Found pydantic_model routes: {pydantic_routes}")
    else:
        print(f"✅ No pydantic_model routes (correct for structured output)")

def test_aug_llm_config_tools_list(aug_llm_config_with_structured_output):
    """Test that tools list is set up correctly."""
    config = aug_llm_config_with_structured_output
    
    print("\n=== TESTING TOOLS LIST ===")
    
    # Test 1: Tools list should contain the model
    print(f"Tools list: {config.tools}")
    assert len(config.tools) == 1
    print(f"✅ Tools list has {len(config.tools)} tool(s)")
    
    # Test 2: The tool should be our Plan[Task] class
    tool = config.tools[0]
    assert tool.__name__ == "Plan[Task]"
    print(f"✅ Tool is Plan[Task]: {tool}")

def test_aug_llm_config_tool_metadata(aug_llm_config_with_structured_output):
    """Test tool metadata is set correctly."""
    config = aug_llm_config_with_structured_output
    
    print("\n=== TESTING TOOL METADATA ===")
    
    # Test 1: Metadata should exist for both original and sanitized names
    print(f"Tool metadata keys: {list(config.tool_metadata.keys())}")
    
    assert "plan_task_generic" in config.tool_metadata
    print(f"✅ plan_task_generic metadata exists")
    
    # Test 2: Check metadata contents
    metadata = config.tool_metadata["plan_task_generic"]
    print(f"Metadata for plan_task_generic: {metadata}")
    
    assert metadata.get("is_structured_output") is True
    assert metadata.get("tool_type") == "structured_output_model"
    print(f"✅ Correct metadata flags set")

def test_aug_llm_config_prompt_template(aug_llm_config_with_structured_output):
    """Test that prompt template includes format instructions."""
    config = aug_llm_config_with_structured_output
    
    print("\n=== TESTING PROMPT TEMPLATE ===")
    
    # Test 1: Should have partial variables with format instructions
    partial_vars = config.prompt_template.partial_variables
    print(f"Partial variables keys: {list(partial_vars.keys())}")
    
    assert "format_instructions" in partial_vars
    print(f"✅ format_instructions in partial variables")
    
    # Test 2: Format instructions should mention the schema
    format_instructions = partial_vars["format_instructions"]
    assert "objective" in format_instructions  # Our Plan model has objective field
    assert "steps" in format_instructions      # Our Plan model has steps field
    print(f"✅ Format instructions contain model fields")
    print(f"Format instructions preview: {format_instructions[:200]}...")

def test_aug_llm_config_create_runnable(aug_llm_config_with_structured_output):
    """Test that we can create a runnable from the config."""
    config = aug_llm_config_with_structured_output
    
    print("\n=== TESTING RUNNABLE CREATION ===")
    
    try:
        runnable = config.create_runnable()
        print(f"✅ Runnable created successfully: {type(runnable)}")
        
        # Check if runnable has bound tools
        if hasattr(runnable, 'bound'):
            print(f"   Bound tools: {getattr(runnable, 'bound', 'N/A')}")
            
    except Exception as e:
        print(f"❌ Failed to create runnable: {e}")
        raise

if __name__ == "__main__":
    # Run tests manually for debugging
    plan_model = Plan[Task]
    config = AugLLMConfig(structured_output_model=plan_model, temperature=0.1)
    
    test_aug_llm_config_basic_setup(config)
    test_aug_llm_config_tool_routes(config)
    test_aug_llm_config_tools_list(config)
    test_aug_llm_config_tool_metadata(config)
    test_aug_llm_config_prompt_template(config)
    test_aug_llm_config_create_runnable(config)
    
    print("\n🎯 ALL TESTS COMPLETED")