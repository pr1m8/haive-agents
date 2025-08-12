#!/usr/bin/env python3
"""Comprehensive test with basic nested BaseModel to understand the real issue."""

from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


# Test 1: Simple nested model (no generics)
class SimpleTask(BaseModel):
    """Simple task without generics."""
    description: str = Field(description="Task description")
    priority: str = Field(default="medium", description="Task priority")


class SimplePlan(BaseModel):
    """Simple plan without generics."""
    objective: str = Field(description="Plan objective")
    tasks: list[SimpleTask] = Field(description="List of tasks")


# Test 2: Generic nested model (our problematic case)
class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


# Test 3: Deeply nested model
class Contact(BaseModel):
    """Contact information."""
    name: str = Field(description="Contact name")
    email: str = Field(description="Contact email")


class Event(BaseModel):
    """Event details."""
    name: str = Field(description="Event name")
    date: str = Field(description="Event date")
    contacts: list[Contact] = Field(description="Event contacts")


class DeepPlan(BaseModel):
    """Deeply nested plan."""
    title: str = Field(description="Plan title")
    events: list[Event] = Field(description="Plan events")


def test_model_comprehensive(model_class, model_name, test_data):
    """Comprehensive test for any BaseModel."""
    print(f"\n{'='*80}")
    print(f"🧪 TESTING {model_name}")
    print(f"{'='*80}")

    # Test 1: Basic Pydantic functionality
    print("1. BASIC PYDANTIC TEST:")
    try:
        instance = model_class(**test_data)
        print("   ✅ Basic instantiation works")
        print(f"   Instance: {instance}")
    except Exception as e:
        print(f"   ❌ Basic instantiation failed: {e}")
        return False

    # Test 2: AugLLMConfig creation
    print("\n2. AUGLLMCONFIG CREATION TEST:")
    try:
        config_v1 = AugLLMConfig(
            structured_output_model=model_class,
            structured_output_version="v1"
        )
        config_v2 = AugLLMConfig(
            structured_output_model=model_class,
            structured_output_version="v2"
        )
        print("   ✅ Both V1 and V2 configs created")
    except Exception as e:
        print(f"   ❌ AugLLMConfig creation failed: {e}")
        return False

    # Test 3: Format instructions generation
    print("\n3. FORMAT INSTRUCTIONS TEST:")
    for version, config in [("V1", config_v1), ("V2", config_v2)]:
        has_internal = hasattr(config, "_format_instructions_text") and config._format_instructions_text
        has_partial = "format_instructions" in config.prompt_template.partial_variables

        print(f"   {version} - Internal: {has_internal}, Partial: {has_partial}")

        if has_internal:
            instructions = config._format_instructions_text
            print(f"   {version} - Instructions length: {len(instructions)} chars")

            # Check if schema is complete
            if model_name in instructions and "properties" in instructions:
                print(f"   {version} - ✅ Schema appears complete")
            else:
                print(f"   {version} - ❌ Schema may be incomplete")

    # Test 4: Tool schema generation
    print("\n4. TOOL SCHEMA TEST:")
    try:
        from langchain_core.tools import StructuredTool

        def dummy_func(**kwargs):
            return kwargs

        tool = StructuredTool.from_function(
            func=dummy_func,
            name=f"test_{model_name.lower()}",
            description=f"Test tool for {model_name}",
            args_schema=model_class
        )

        schema = tool.get_input_schema().model_json_schema()
        print("   ✅ Tool schema created")
        print(f"   Schema has $defs: {'$defs' in schema}")
        print(f"   Schema properties: {list(schema.get('properties', {}).keys())}")

        # Check for nested references
        nested_refs = []
        def find_refs(obj, path=""):
            if isinstance(obj, dict):
                if "$ref" in obj:
                    nested_refs.append(f"{path}: {obj['$ref']}")
                for key, value in obj.items():
                    find_refs(value, f"{path}.{key}" if path else key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    find_refs(item, f"{path}[{i}]")

        find_refs(schema)
        if nested_refs:
            print(f"   Nested references: {nested_refs}")
        else:
            print("   No nested references found")

    except Exception as e:
        print(f"   ❌ Tool schema creation failed: {e}")
        return False

    # Test 5: Actual LLM execution
    print("\n5. LLM EXECUTION TEST:")
    try:
        runnable = config_v2.create_runnable()

        # Test input that should trigger the nested structure
        input_data = {
            "messages": [{
                "role": "user",
                "content": f"Create a sample {model_name.lower()} with all required nested fields properly structured."
            }]
        }

        result = runnable.invoke(input_data)

        if hasattr(result, "tool_calls") and result.tool_calls:
            tool_call = result.tool_calls[0]
            args = tool_call["args"] if isinstance(tool_call, dict) else tool_call.args

            print("   ✅ LLM execution successful")
            print(f"   Tool call args keys: {list(args.keys())}")

            # Analyze nested structure
            nested_fields = []
            for key, value in args.items():
                if isinstance(value, list) and value and isinstance(value[0], dict):
                    nested_fields.append(key)
                    print(f"   Nested field '{key}': {len(value)} items")
                    print(f"   First item structure: {list(value[0].keys())}")

            if nested_fields:
                print(f"   ✅ LLM returned proper nested structure in: {nested_fields}")
            else:
                print("   ❌ LLM did not return nested structures")

            # Try to reconstruct the model
            try:
                reconstructed = model_class(**args)
                print(f"   ✅ LLM output can be parsed back to {model_name}")
                return True
            except Exception as e:
                print(f"   ❌ LLM output cannot be parsed back to {model_name}: {e}")
                return False
        else:
            print("   ❌ No tool calls in LLM result")
            return False

    except Exception as e:
        print(f"   ❌ LLM execution failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def comprehensive_nested_basemodel_test():
    """Run comprehensive tests on multiple nested BaseModel patterns."""
    print("🚀 COMPREHENSIVE NESTED BASEMODEL TEST SUITE")
    print("="*80)
    print("Purpose: Determine if nested BaseModel issues are:")
    print("1. General to all nested BaseModels")
    print("2. Specific to generic types Plan[T]")
    print("3. Related to format instructions delivery")
    print("4. Related to LLM interpretation of schemas")

    # Test data for each model
    test_cases = [
        (
            SimplePlan,
            "SimplePlan",
            {
                "objective": "Simple test objective",
                "tasks": [
                    {"description": "First task", "priority": "high"},
                    {"description": "Second task", "priority": "low"}
                ]
            }
        ),
        (
            Plan[Task],
            "Plan[Task]",
            {
                "objective": "Generic test objective",
                "steps": [
                    {"description": "First step"},
                    {"description": "Second step"}
                ]
            }
        ),
        (
            DeepPlan,
            "DeepPlan",
            {
                "title": "Deep test plan",
                "events": [
                    {
                        "name": "Event 1",
                        "date": "2025-01-01",
                        "contacts": [
                            {"name": "John Doe", "email": "john@example.com"},
                            {"name": "Jane Smith", "email": "jane@example.com"}
                        ]
                    }
                ]
            }
        )
    ]

    results = []
    for model_class, model_name, test_data in test_cases:
        success = test_model_comprehensive(model_class, model_name, test_data)
        results.append((model_name, success))

    # Summary analysis
    print(f"\n{'='*80}")
    print("🏁 COMPREHENSIVE ANALYSIS RESULTS")
    print(f"{'='*80}")

    for model_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{model_name:20}: {status}")

    # Determine patterns
    all_pass = all(success for _, success in results)
    all_fail = all(not success for _, success in results)

    if all_pass:
        print("\n🎯 CONCLUSION: All nested BaseModels work correctly")
        print("   - Issue may be elsewhere in validation routing")
        print("   - Format instructions may be working as intended")
    elif all_fail:
        print("\n🎯 CONCLUSION: Systematic issue with nested BaseModels")
        print("   - Format instructions delivery problem")
        print("   - Or fundamental AugLLMConfig issue")
    else:
        print("\n🎯 CONCLUSION: Mixed results - specific pattern issues")
        simple_works = results[0][1]  # SimplePlan
        generic_works = results[1][1]  # Plan[Task]
        deep_works = results[2][1]     # DeepPlan

        if not generic_works and (simple_works or deep_works):
            print("   - Generic types Plan[T] are the specific problem")
        elif not deep_works and (simple_works or generic_works):
            print("   - Deep nesting is the specific problem")
        else:
            print("   - Complex interaction of multiple factors")

    return results


if __name__ == "__main__":
    results = comprehensive_nested_basemodel_test()

    print(f"\n{'='*80}")
    print("📋 LONG-TERM PLAN TO SORT THIS OUT")
    print(f"{'='*80}")

    print("Phase 1: Root Cause Identification")
    print("  1.1 Determine which BaseModel patterns fail")
    print("  1.2 Isolate format instructions delivery issue")
    print("  1.3 Compare tool schema vs format instructions")
    print("  1.4 Test LLM behavior with explicit schemas")

    print("\nPhase 2: Fix Implementation")
    print("  2.1 Fix format instructions setup in AugLLMConfig")
    print("  2.2 Ensure proper schema delivery to LLM")
    print("  2.3 Test validation node routing with correct data")
    print("  2.4 Verify SimpleAgent works end-to-end")

    print("\nPhase 3: Validation & Testing")
    print("  3.1 Test all BaseModel patterns comprehensively")
    print("  3.2 Validate V1 vs V2 mode differences")
    print("  3.3 Test validation routing with real schemas")
    print("  3.4 End-to-end integration testing")

    print("\nPhase 4: Documentation & Prevention")
    print("  4.1 Document the root cause and solution")
    print("  4.2 Add regression tests for nested BaseModels")
    print("  4.3 Update development guidelines")
    print("  4.4 Create monitoring for similar issues")

    # Immediate next steps based on results
    failed_models = [name for name, success in results if not success]
    if failed_models:
        print("\n🚨 IMMEDIATE PRIORITY:")
        print(f"   Focus on failed models: {', '.join(failed_models)}")
        print("   Debug format instructions delivery")
        print("   Fix _setup_format_instructions() method")
    else:
        print("\n✅ ALL MODELS WORK:")
        print("   Issue may be in validation routing")
        print("   Test SimpleAgent graph structure next")
