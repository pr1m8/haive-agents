#!/usr/bin/env python3
"""Debug exactly WHY _should_setup_format_instructions returns False.

Check each condition individually to find the failing one."""


from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def debug_format_instructions_conditions():
    """Debug each condition in _should_setup_format_instructions method."""
    print("🔍 DEBUGGING FORMAT INSTRUCTIONS CONDITIONS")
    print("=" * 60)

    # Create config
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )

    print("1. CHECKING INDIVIDUAL CONDITIONS:")

    # Condition 1: include_format_instructions
    include_fi = config.include_format_instructions
    print(f"   include_format_instructions: {include_fi}")
    if not include_fi:
        print("   ❌ FAIL: include_format_instructions is False")
        return "include_format_instructions"
    print("   ✅ PASS: include_format_instructions is True")

    # Condition 2: format_instructions not already in partial_variables
    partial_vars = config.prompt_template.partial_variables
    has_format_instructions = "format_instructions" in partial_vars
    print(f"   format_instructions in partial_variables: {has_format_instructions}")
    print(f"   partial_variables keys: {list(partial_vars.keys())}")
    if has_format_instructions:
        print("   ❌ FAIL: format_instructions already exists")
        return "already_exists"
    print("   ✅ PASS: format_instructions not in partial_variables")

    # Condition 3: structured_output_model exists
    has_model = config.structured_output_model is not None
    print(f"   structured_output_model exists: {has_model}")
    print(f"   structured_output_model: {config.structured_output_model}")
    if not has_model:
        print("   ❌ FAIL: structured_output_model is None")
        return "no_model"
    print("   ✅ PASS: structured_output_model exists")

    print("\n2. ALL CONDITIONS SHOULD PASS - TESTING METHOD:")

    # Test the actual method
    if hasattr(config, "_should_setup_format_instructions"):
        should_setup = config._should_setup_format_instructions()
        print(f"   _should_setup_format_instructions() returns: {should_setup}")

        if should_setup:
            print("   ✅ Method returns True as expected")
            return "success"
        print("   ❌ Method returns False - THERE'S A HIDDEN CONDITION!")

        # Try to find the hidden condition
        print("\n3. INVESTIGATING HIDDEN CONDITIONS:")

        # Check for additional attributes that might affect the decision
        attrs_to_check = [
            "use_tool_for_format_instructions",
            "tool_is_base_model",
            "parse_raw_output",
            "force_tool_use",
            "structured_output_version"
        ]

        for attr in attrs_to_check:
            if hasattr(config, attr):
                value = getattr(config, attr)
                print(f"   {attr}: {value}")

        return "hidden_condition"
    print("   ❌ _should_setup_format_instructions method not found!")
    return "method_not_found"


def test_manual_format_instructions_setup():
    """Test manually calling _setup_format_instructions."""
    print("\n" + "=" * 60)
    print("🛠️  TESTING MANUAL FORMAT INSTRUCTIONS SETUP")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )

    print("1. BEFORE MANUAL SETUP:")
    before_partials = config.prompt_template.partial_variables
    print(f"   Partial variables: {list(before_partials.keys())}")
    print(f"   Has format_instructions: {'format_instructions' in before_partials}")

    # Try manual setup
    if hasattr(config, "_setup_format_instructions"):
        print("\n2. CALLING _setup_format_instructions()...")
        try:
            config._setup_format_instructions()
            print("   ✅ Manual setup completed without error")

            # Check results
            after_partials = config.prompt_template.partial_variables
            print(f"   After setup - Partial variables: {list(after_partials.keys())}")
            has_instructions = "format_instructions" in after_partials
            print(f"   Has format_instructions: {has_instructions}")

            if has_instructions:
                instructions = after_partials["format_instructions"]
                print(f"   ✅ Format instructions added! Length: {len(instructions)} chars")
                print(f"   Preview: {instructions[:200]}...")
                return "manual_success"
            print("   ❌ Manual setup didn't add format_instructions")
            return "manual_failed"

        except Exception as e:
            print(f"   ❌ Manual setup failed with error: {e}")
            import traceback
            traceback.print_exc()
            return "manual_error"
    else:
        print("   ❌ _setup_format_instructions method not found")
        return "method_not_found"


def test_direct_partial_variables_modification():
    """Test directly adding format_instructions to partial_variables."""
    print("\n" + "=" * 60)
    print("🔧 TESTING DIRECT PARTIAL VARIABLES MODIFICATION")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )

    # Get the internal format instructions
    if hasattr(config, "_format_instructions_text") and config._format_instructions_text:
        instructions = config._format_instructions_text
        print(f"1. Internal format instructions found: {len(instructions)} chars")

        # Try to add them directly
        try:
            # Create new partial variables dict
            new_partials = config.prompt_template.partial_variables.copy()
            new_partials["format_instructions"] = instructions

            # Try to update the prompt template
            config.prompt_template.partial_variables = new_partials

            # Check if it worked
            updated_partials = config.prompt_template.partial_variables
            has_instructions = "format_instructions" in updated_partials
            print(f"2. Direct modification result: {has_instructions}")

            if has_instructions:
                print("   ✅ Direct modification successful!")
                return "direct_success"
            print("   ❌ Direct modification failed")
            return "direct_failed"

        except Exception as e:
            print(f"   ❌ Direct modification error: {e}")
            return "direct_error"
    else:
        print("1. ❌ No internal format instructions found")
        return "no_internal_instructions"


if __name__ == "__main__":
    result1 = debug_format_instructions_conditions()
    result2 = test_manual_format_instructions_setup()
    result3 = test_direct_partial_variables_modification()

    print("\n" + "=" * 60)
    print("🏁 SUMMARY")
    print("=" * 60)
    print(f"Conditions check: {result1}")
    print(f"Manual setup: {result2}")
    print(f"Direct modification: {result3}")

    if result1 == "hidden_condition":
        print("\n🔍 KEY FINDING: There's a hidden condition preventing format instructions setup!")
    elif result2 == "manual_success":
        print("\n✅ SOLUTION: Manual setup works - we can force format instructions!")
    elif result3 == "direct_success":
        print("\n✅ WORKAROUND: Direct modification works!")
