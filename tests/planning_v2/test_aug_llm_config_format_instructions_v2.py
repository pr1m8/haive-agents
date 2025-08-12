#!/usr/bin/env python3
"""Test AugLLMConfig format instructions setup in v2 mode - mimicking haive-core patterns.

Based on existing haive-core test patterns for structured output validation."""


from pydantic import BaseModel, Field
import pytest

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing structured output."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type for testing structured output."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


class SearchResult(BaseModel):
    """Search result schema for testing structured output - matches haive-core patterns."""
    answer: str = Field(description="Answer to the query")
    sources: list[str] = Field(default_factory=list, description="Source documents")
    confidence: float = Field(default=0.0, description="Confidence score")


@pytest.fixture
def plan_task_model():
    """Fixture for Plan[Task] model."""
    return Plan[Task]


@pytest.fixture
def search_result_model():
    """Fixture for SearchResult model."""
    return SearchResult


class TestAugLLMConfigFormatInstructionsV2:
    """Test AugLLMConfig format instructions in v2 mode - following haive-core patterns."""

    def test_v2_mode_format_instructions_internal_generation(self, plan_task_model):
        """Test that v2 mode generates format instructions internally."""
        print("\n=== TESTING V2 FORMAT INSTRUCTIONS INTERNAL GENERATION ===")

        config = AugLLMConfig(
            structured_output_model=plan_task_model,
            structured_output_version="v2",
            temperature=0.1
        )

        # Test 1: Check internal format instructions exist (like haive-core tests)
        print("1. Internal format instructions check:")
        if hasattr(config, "_format_instructions_text"):
            instructions = config._format_instructions_text
            print(f"   ✅ _format_instructions_text exists: {len(instructions)} chars")
            print(f"   Content preview: {instructions[:200]}...")

            # Verify it contains our model fields
            assert "objective" in instructions, "Format instructions should mention 'objective' field"
            assert "steps" in instructions, "Format instructions should mention 'steps' field"
            print("   ✅ Contains model fields")
        else:
            pytest.fail("❌ _format_instructions_text not found - this is unexpected!")

        # Test 2: Check configuration flags (matching haive-core patterns)
        print("\n2. Configuration flags:")
        print(f"   structured_output_version: {config.structured_output_version}")
        print(f"   include_format_instructions: {config.include_format_instructions}")
        print(f"   use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")
        print(f"   force_tool_use: {config.force_tool_use}")

        # These should be True for v2 structured output
        assert config.structured_output_version == "v2"
        assert config.include_format_instructions is True
        assert config.force_tool_use is True

        print("   ✅ All configuration flags correct for v2 mode")

    def test_should_setup_format_instructions_logic(self, plan_task_model):
        """Test the _should_setup_format_instructions method logic."""
        print("\n=== TESTING _should_setup_format_instructions LOGIC ===")

        config = AugLLMConfig(
            structured_output_model=plan_task_model,
            structured_output_version="v2"
        )

        # Test the method that determines if format instructions should be set up
        if hasattr(config, "_should_setup_format_instructions"):
            should_setup = config._should_setup_format_instructions()
            print(f"1. _should_setup_format_instructions() returns: {should_setup}")

            # Debug the individual conditions
            print("2. Individual condition checks:")
            print(f"   include_format_instructions: {config.include_format_instructions}")
            print(f"   structured_output_model exists: {config.structured_output_model is not None}")
            print(f"   use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")

            # According to the logic, if include_format_instructions=True and structured_output_model exists
            # and use_tool_for_format_instructions=False, then it should return True
            expected = (
                config.include_format_instructions and
                config.structured_output_model is not None and
                not config.use_tool_for_format_instructions
            )
            print(f"   Expected result: {expected}")

            if expected != should_setup:
                print(f"   ❌ ISSUE: Expected {expected} but got {should_setup}")

                # Investigate further - check if there are other conditions
                print("3. Additional investigation:")
                print(f"   tool_is_base_model: {getattr(config, 'tool_is_base_model', 'N/A')}")
                print(f"   parse_raw_output: {getattr(config, 'parse_raw_output', 'N/A')}")
        else:
            print("   ❌ _should_setup_format_instructions method not found!")

    def test_format_instructions_in_partial_variables(self, plan_task_model):
        """Test whether format instructions end up in prompt template partial variables."""
        print("\n=== TESTING FORMAT INSTRUCTIONS IN PARTIAL VARIABLES ===")

        config = AugLLMConfig(
            structured_output_model=plan_task_model,
            structured_output_version="v2"
        )

        # Test 1: Check current state
        partial_vars = config.prompt_template.partial_variables
        print(f"1. Current partial variables: {list(partial_vars.keys())}")

        has_format_instructions = "format_instructions" in partial_vars
        print(f"   format_instructions present: {has_format_instructions}")

        # Test 2: Try manual setup (like haive-core tests)
        print("\n2. Manual setup attempt:")
        try:
            if hasattr(config, "_setup_format_instructions"):
                print("   Calling _setup_format_instructions()...")
                config._setup_format_instructions()

                # Check if it worked
                new_partial_vars = config.prompt_template.partial_variables
                new_has_format_instructions = "format_instructions" in new_partial_vars
                print(f"   After manual setup - format_instructions present: {new_has_format_instructions}")

                if new_has_format_instructions:
                    instructions = new_partial_vars["format_instructions"]
                    print(f"   ✅ Manual setup worked! Length: {len(instructions)} chars")
                else:
                    print("   ❌ Manual setup didn't add format_instructions")
                    print(f"   New partial vars: {list(new_partial_vars.keys())}")
            else:
                print("   ❌ _setup_format_instructions method not found")

        except Exception as e:
            print(f"   ❌ Manual setup failed: {e}")
            import traceback
            traceback.print_exc()

    def test_v1_vs_v2_format_instructions_comparison(self, search_result_model):
        """Test format instructions behavior in v1 vs v2 mode."""
        print("\n=== TESTING V1 VS V2 FORMAT INSTRUCTIONS COMPARISON ===")

        # Create v1 config
        config_v1 = AugLLMConfig(
            structured_output_model=search_result_model,
            structured_output_version="v1"
        )

        # Create v2 config
        config_v2 = AugLLMConfig(
            structured_output_model=search_result_model,
            structured_output_version="v2"
        )

        print("1. V1 Configuration:")
        print(f"   structured_output_version: {config_v1.structured_output_version}")
        print(f"   force_tool_use: {config_v1.force_tool_use}")
        print(f"   include_format_instructions: {config_v1.include_format_instructions}")
        print(f"   use_tool_for_format_instructions: {config_v1.use_tool_for_format_instructions}")

        print("\n2. V2 Configuration:")
        print(f"   structured_output_version: {config_v2.structured_output_version}")
        print(f"   force_tool_use: {config_v2.force_tool_use}")
        print(f"   include_format_instructions: {config_v2.include_format_instructions}")
        print(f"   use_tool_for_format_instructions: {config_v2.use_tool_for_format_instructions}")

        # Check partial variables
        v1_partials = config_v1.prompt_template.partial_variables
        v2_partials = config_v2.prompt_template.partial_variables

        print("\n3. Partial Variables Comparison:")
        print(f"   V1 partials: {list(v1_partials.keys())}")
        print(f"   V2 partials: {list(v2_partials.keys())}")

        v1_has_instructions = "format_instructions" in v1_partials
        v2_has_instructions = "format_instructions" in v2_partials

        print(f"   V1 has format_instructions: {v1_has_instructions}")
        print(f"   V2 has format_instructions: {v2_has_instructions}")

        # Check internal format instructions
        v1_internal = hasattr(config_v1, "_format_instructions_text") and config_v1._format_instructions_text
        v2_internal = hasattr(config_v2, "_format_instructions_text") and config_v2._format_instructions_text

        print("\n4. Internal Format Instructions:")
        print(f"   V1 has internal instructions: {bool(v1_internal)}")
        print(f"   V2 has internal instructions: {bool(v2_internal)}")

        # Key insight: Both should have internal instructions, but behavior differs
        if v1_internal and v2_internal:
            print("   ✅ Both versions generate internal format instructions")
        elif v2_internal and not v1_internal:
            print("   ❓ Only V2 has internal instructions")
        elif v1_internal and not v2_internal:
            print("   ❓ Only V1 has internal instructions")
        else:
            print("   ❌ Neither version has internal instructions!")

    def test_tool_routes_for_structured_output(self, plan_task_model):
        """Test tool routes setup for structured output - following haive-core patterns."""
        print("\n=== TESTING TOOL ROUTES FOR STRUCTURED OUTPUT ===")

        config = AugLLMConfig(
            structured_output_model=plan_task_model,
            structured_output_version="v2"
        )

        print("1. Tool Routes Analysis:")
        print(f"   All routes: {config.tool_routes}")

        # Check for the sanitized name (Plan[Task] -> plan_task_generic)
        expected_route_name = "plan_task_generic"
        expected_route_type = "parse_output"

        if expected_route_name in config.tool_routes:
            actual_route = config.tool_routes[expected_route_name]
            print(f"   ✅ Found route: {expected_route_name} → {actual_route}")

            assert actual_route == expected_route_type, f"Expected {expected_route_type}, got {actual_route}"
            print("   ✅ Route type correct")
        else:
            pytest.fail(f"❌ Expected route '{expected_route_name}' not found in {list(config.tool_routes.keys())}")

        # Test 2: Check tool metadata
        print("\n2. Tool Metadata Analysis:")
        if expected_route_name in config.tool_metadata:
            metadata = config.tool_metadata[expected_route_name]
            print(f"   Metadata for {expected_route_name}: {metadata}")

            assert metadata.get("is_structured_output") is True
            assert metadata.get("tool_type") == "structured_output_model"
            print("   ✅ Metadata flags correct")
        else:
            pytest.fail(f"❌ Metadata for '{expected_route_name}' not found")


def test_comprehensive_format_instructions_investigation():
    """Comprehensive test mimicking haive-core integration testing patterns."""
    print("\n" + "="*80)
    print("COMPREHENSIVE FORMAT INSTRUCTIONS INVESTIGATION")
    print("="*80)

    # Test with Plan[Task] (our problematic case)
    plan_model = Plan[Task]
    config = AugLLMConfig(
        structured_output_model=plan_model,
        structured_output_version="v2",
        temperature=0.1
    )

    print("\n1. CONFIGURATION SUMMARY:")
    print(f"   Model: {config.structured_output_model}")
    print(f"   Version: {config.structured_output_version}")
    print(f"   Force tool use: {config.force_tool_use}")
    print(f"   Tool routes: {config.tool_routes}")

    print("\n2. FORMAT INSTRUCTIONS STATUS:")
    internal_exists = hasattr(config, "_format_instructions_text") and config._format_instructions_text
    template_exists = "format_instructions" in config.prompt_template.partial_variables

    print(f"   Internal format instructions: {'✅' if internal_exists else '❌'}")
    print(f"   Template format instructions: {'✅' if template_exists else '❌'}")

    if internal_exists and not template_exists:
        print("\n   🔍 KEY FINDING: Internal instructions exist but not in template!")
        print("   This confirms our hypothesis about v2 mode behavior.")

        instructions = config._format_instructions_text
        print(f"   Internal instructions preview: {instructions[:300]}...")

    print("\n3. NEXT INVESTIGATION STEPS:")
    if internal_exists and not template_exists:
        print("   ✅ Confirmed: V2 mode generates internal format instructions")
        print("   🔍 Need to investigate: How does v2 mode use these instructions?")
        print("   🔍 Need to investigate: Is this causing the validation routing issue?")

    return config


if __name__ == "__main__":
    # Run the comprehensive investigation
    config = test_comprehensive_format_instructions_investigation()

    print("\n" + "="*80)
    print("INVESTIGATION COMPLETE")
    print("="*80)
