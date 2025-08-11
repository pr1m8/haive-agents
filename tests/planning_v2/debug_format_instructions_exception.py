#!/usr/bin/env python3
"""
Debug what exception is preventing format instructions setup.
"""

from typing import List
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)


def debug_pydantic_output_parser():
    """Debug PydanticOutputParser with Plan[Task] model."""
    print("🔍 DEBUGGING PYDANTIC OUTPUT PARSER")
    print("=" * 50)
    
    model = Plan[Task]
    print(f"1. Model: {model}")
    print(f"   Model name: {model.__name__}")
    
    try:
        print(f"\n2. Creating PydanticOutputParser...")
        parser = PydanticOutputParser(pydantic_object=model)
        print(f"   ✅ Parser created successfully")
        print(f"   Parser type: {type(parser)}")
        
        print(f"\n3. Getting format instructions...")
        instructions = parser.get_format_instructions()
        print(f"   ✅ Instructions retrieved successfully")
        print(f"   Length: {len(instructions)} chars")
        print(f"   Preview: {instructions[:300]}...")
        return True
        
    except Exception as e:
        print(f"   ❌ Exception occurred: {e}")
        print(f"   Exception type: {type(e)}")
        import traceback
        traceback.print_exc()
        return False


def debug_manual_setup_with_exception_details():
    """Debug the manual setup with detailed exception handling."""
    print(f"\n" + "=" * 50)
    print("🛠️  DEBUGGING MANUAL SETUP WITH EXCEPTION DETAILS")
    print("=" * 50)
    
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )
    
    print(f"1. Config created, testing manual _setup_format_instructions()...")
    
    # Manually recreate the logic from _setup_format_instructions
    print(f"   Step 1: Clear existing format_instructions...")
    if "format_instructions" in config.partial_variables:
        del config.partial_variables["format_instructions"]
        config._format_instructions_text = None
        print(f"   ✅ Cleared existing instructions")
    else:
        print(f"   ℹ️  No existing instructions to clear")
    
    print(f"   Step 2: Check should_setup conditions...")
    should_setup = config._should_setup_format_instructions()
    print(f"   should_setup result: {should_setup}")
    
    if not should_setup:
        print(f"   ❌ Conditions not met - stopping")
        return False
    
    print(f"   Step 3: Try PydanticOutputParser...")
    try:
        model = config.structured_output_model
        print(f"   Model: {model}")
        print(f"   Model name: {model.__name__}")
        
        parser = PydanticOutputParser(pydantic_object=model)
        print(f"   ✅ Parser created")
        
        instructions = parser.get_format_instructions()
        print(f"   ✅ Instructions retrieved: {len(instructions)} chars")
        
        # Try to add to partial_variables
        config.partial_variables["format_instructions"] = instructions
        config._format_instructions_text = instructions
        print(f"   ✅ Instructions added to config")
        
        # Verify
        has_instructions = "format_instructions" in config.partial_variables
        print(f"   Verification: {has_instructions}")
        
        return has_instructions
        
    except Exception as e:
        print(f"   ❌ Exception in manual setup: {e}")
        print(f"   Exception type: {type(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_format_instructions_with_simple_model():
    """Test with a simple model to see if generics are the issue."""
    print(f"\n" + "=" * 50)
    print("🧪 TESTING WITH SIMPLE MODEL (NO GENERICS)")
    print("=" * 50)
    
    class SimpleTask(BaseModel):
        """Simple task without generics."""
        description: str = Field(description="Task description")
    
    class SimplePlan(BaseModel):
        """Simple plan without generics."""
        objective: str = Field(description="Plan objective")  
        tasks: List[SimpleTask] = Field(description="Plan tasks")
    
    print(f"1. Testing PydanticOutputParser with SimplePlan...")
    try:
        parser = PydanticOutputParser(pydantic_object=SimplePlan)
        instructions = parser.get_format_instructions()
        print(f"   ✅ Simple model works! Length: {len(instructions)} chars")
        
        # Test with AugLLMConfig
        config = AugLLMConfig(
            structured_output_model=SimplePlan,
            structured_output_version="v2"
        )
        
        partials = config.prompt_template.partial_variables
        has_instructions = "format_instructions" in partials
        print(f"   AugLLMConfig with simple model: {has_instructions}")
        
        return has_instructions
        
    except Exception as e:
        print(f"   ❌ Even simple model fails: {e}")
        return False


if __name__ == "__main__":
    result1 = debug_pydantic_output_parser()
    result2 = debug_manual_setup_with_exception_details()
    result3 = test_format_instructions_with_simple_model()
    
    print(f"\n" + "=" * 50)
    print("🏁 DIAGNOSIS")
    print("=" * 50)
    print(f"PydanticOutputParser works: {'✅' if result1 else '❌'}")
    print(f"Manual setup works: {'✅' if result2 else '❌'}")
    print(f"Simple model works: {'✅' if result3 else '❌'}")
    
    if not result1:
        print(f"\n🔍 CONCLUSION: PydanticOutputParser cannot handle Plan[Task] generic types")
    elif result2:
        print(f"\n🔍 CONCLUSION: Manual setup works - there's a different issue in AugLLMConfig")
    elif result3:
        print(f"\n🔍 CONCLUSION: Generic types are the problem")