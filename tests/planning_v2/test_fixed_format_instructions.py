#!/usr/bin/env python3
"""Test that the format instructions fix works with a real AugLLMConfig configuration."""

import os

from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def test_format_instructions_fix():
    """Test that format instructions are now properly set up."""
    print("🧪 TESTING FORMAT INSTRUCTIONS FIX")
    print("=" * 50)

    # Enable debug output
    os.environ.setdefault("DEBUG_MODE", "1")

    # Create config
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )

    print("\n1. AFTER CONFIGURATION CREATION:")
    partials = config.prompt_template.partial_variables
    print(f"   Partial variables: {list(partials.keys())}")
    has_instructions = "format_instructions" in partials
    print(f"   Has format_instructions: {has_instructions}")

    if has_instructions:
        instructions = partials["format_instructions"]
        print(f"   ✅ Format instructions found! Length: {len(instructions)} chars")
        print(f"   Preview: {instructions[:300]}...")

        # Verify they contain our model fields
        if "objective" in instructions and "steps" in instructions:
            print("   ✅ Instructions contain model fields")
            return True
        print("   ❌ Instructions missing model fields")
        return False
    print("   ❌ Format instructions still missing")

    # Try to debug why
    print("\n2. DEBUG INFO:")
    print(f"   _format_instructions_text exists: {hasattr(config, '_format_instructions_text')}")
    if hasattr(config, "_format_instructions_text"):
        internal_text = config._format_instructions_text
        print(f"   Internal instructions: {'Yes' if internal_text else 'No'}")
        if internal_text:
            print(f"   Internal length: {len(internal_text)} chars")

    return False


def test_simple_agent_with_fixed_format_instructions():
    """Test SimpleAgent with the format instructions fix."""
    print("\n" + "=" * 50)
    print("🤖 TESTING SIMPLE AGENT WITH FIXED FORMAT INSTRUCTIONS")
    print("=" * 50)

    from haive.agents.simple.agent import SimpleAgent

    # Create agent with structured output
    agent = SimpleAgent(
        name="test_planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            structured_output_version="v2",
            temperature=0.1
        )
    )

    # Check if agent has format instructions
    engine = agent.engine
    partials = engine.prompt_template.partial_variables
    has_instructions = "format_instructions" in partials

    print(f"1. Agent engine format instructions: {has_instructions}")

    if has_instructions:
        print("   ✅ Agent has format instructions!")

        # Now test actual execution with debug
        try:
            print("\n2. Testing agent execution...")
            result = agent.run("Create a simple plan with 2 steps", debug=True)
            print("   ✅ Execution completed")
            print(f"   Result type: {type(result)}")
            print(f"   Result: {str(result)[:200]}...")
            return True

        except Exception as e:
            print(f"   ❌ Execution failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    else:
        print("   ❌ Agent missing format instructions")
        return False


if __name__ == "__main__":
    success1 = test_format_instructions_fix()
    success2 = test_simple_agent_with_fixed_format_instructions() if success1 else False

    print("\n" + "=" * 50)
    print("🏁 RESULTS")
    print("=" * 50)
    print(f"Format instructions fix: {'✅' if success1 else '❌'}")
    print(f"SimpleAgent execution: {'✅' if success2 else '❌'}")

    if success1 and success2:
        print("\n🎉 SUCCESS: Format instructions fix resolves the issue!")
    elif success1:
        print("\n🔧 PARTIAL: Fix works but agent still has issues")
    else:
        print("\n❌ FAILED: Format instructions still not working")
