#!/usr/bin/env python3
"""Detailed test of AugLLMConfig to identify issues."""


from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)

def detailed_debug():
    """Detailed debug of AugLLMConfig setup."""
    print("🔍 DETAILED AugLLMConfig DEBUG")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        temperature=0.1
    )

    # 1. Core Configuration
    print("1. CORE CONFIGURATION:")
    print(f"   structured_output_model: {config.structured_output_model}")
    print(f"   force_tool_use: {config.force_tool_use}")
    print(f"   force_tool_choice: {config.force_tool_choice}")
    print(f"   structured_output_version: {config.structured_output_version}")

    # 2. Tool Routes (CRITICAL)
    print("\n2. TOOL ROUTES:")
    for name, route in config.tool_routes.items():
        print(f"   {name} → {route}")
        if route != "parse_output":
            print(f"   ❌ ISSUE: Expected parse_output, got {route}")

    # 3. Tools and Metadata
    print("\n3. TOOLS AND METADATA:")
    print(f"   Tools count: {len(config.tools)}")
    print(f"   Tools: {config.tools}")
    print(f"   Tool metadata keys: {list(config.tool_metadata.keys())}")

    for key, metadata in config.tool_metadata.items():
        if "plan" in key.lower():
            print(f"   {key} metadata:")
            for k, v in metadata.items():
                print(f"     {k}: {v}")

    # 4. Prompt Template Details
    print("\n4. PROMPT TEMPLATE:")
    template = config.prompt_template
    print(f"   Template type: {type(template)}")
    print(f"   Input variables: {template.input_variables}")
    print(f"   Optional variables: {getattr(template, 'optional_variables', [])}")
    print(f"   Partial variables: {list(template.partial_variables.keys())}")

    # Check if format instructions are in partial variables
    if "format_instructions" in template.partial_variables:
        format_instructions = template.partial_variables["format_instructions"]
        print(f"   ✅ Format instructions found ({len(format_instructions)} chars)")
        print(f"   Preview: {format_instructions[:150]}...")
    else:
        print("   ❌ No format_instructions in partial_variables")

        # Maybe it's somewhere else?
        all_partials = template.partial_variables
        print("   All partial variables:")
        for k, v in all_partials.items():
            print(f"     {k}: {str(v)[:100]}...")

    # 5. Create Runnable Test
    print("\n5. RUNNABLE CREATION:")
    try:
        runnable = config.create_runnable()
        print(f"   ✅ Runnable created: {type(runnable)}")

        # Test invoke to see what happens
        print("   Testing runnable invoke...")
        test_messages = [{"role": "user", "content": "Create a simple plan"}]

        # Don't actually invoke (would call LLM), just check structure
        print("   Runnable ready for testing")

    except Exception as e:
        print(f"   ❌ Runnable creation failed: {e}")
        import traceback
        traceback.print_exc()

    # 6. Schema Information
    print("\n6. SCHEMA INFORMATION:")
    if config.schemas:
        print(f"   Schemas: {config.schemas}")
    else:
        print("   ❌ No schemas found")

    # 7. Tool Processing
    print("\n7. TOOL PROCESSING:")
    print(f"   Pydantic tools: {config.pydantic_tools}")
    print(f"   Tool instances: {config.tool_instances}")

    return config

if __name__ == "__main__":
    config = detailed_debug()

    print("\n" + "=" * 60)
    print("SUMMARY:")

    # Check key requirements
    issues = []

    if "plan_task_generic" not in config.tool_routes:
        issues.append("Missing plan_task_generic in tool_routes")
    elif config.tool_routes["plan_task_generic"] != "parse_output":
        issues.append(f"Wrong route: {config.tool_routes['plan_task_generic']} (should be parse_output)")

    if not config.force_tool_use:
        issues.append("force_tool_use should be True")

    if config.force_tool_choice != "plan_task_generic":
        issues.append(f"Wrong force_tool_choice: {config.force_tool_choice}")

    if "format_instructions" not in config.prompt_template.partial_variables:
        issues.append("Missing format_instructions in prompt template")

    if issues:
        print("❌ ISSUES FOUND:")
        for issue in issues:
            print(f"   - {issue}")
    else:
        print("✅ ALL CHECKS PASSED - AugLLMConfig setup is correct!")
