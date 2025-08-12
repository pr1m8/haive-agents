#!/usr/bin/env python3
"""Deep investigation of AugLLMConfig internals - format instructions and structured output."""


from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)

def investigate_aug_llm_config_internals():
    """Comprehensive investigation of AugLLMConfig internals."""
    print("🔍 DEEP DIVE: AugLLMConfig Internals")
    print("=" * 80)

    # Create config with debugging
    print("1. Creating AugLLMConfig with structured_output_model...")
    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        temperature=0.1
    )

    # 2. Examine internal state after creation
    print("\n2. INTERNAL STATE AFTER CREATION:")
    print(f"   structured_output_model: {config.structured_output_model}")
    print(f"   structured_output_version: {config.structured_output_version}")
    print(f"   include_format_instructions: {config.include_format_instructions}")
    print(f"   use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")
    print(f"   tool_is_base_model: {config.tool_is_base_model}")
    print(f"   parse_raw_output: {config.parse_raw_output}")

    # 3. Check internal format instructions state
    print("\n3. FORMAT INSTRUCTIONS INTERNAL STATE:")
    if hasattr(config, "_format_instructions_text"):
        instructions = config._format_instructions_text
        print(f"   _format_instructions_text exists: {len(instructions)} chars")
        print(f"   Preview: {instructions[:150]}...")
    else:
        print("   ❌ _format_instructions_text not found")

    # 4. Examine prompt template in detail
    print("\n4. PROMPT TEMPLATE ANALYSIS:")
    template = config.prompt_template
    print(f"   Type: {type(template)}")
    print(f"   Input variables: {template.input_variables}")
    print(f"   Optional variables: {getattr(template, 'optional_variables', 'N/A')}")

    # Check all attributes of prompt template
    print("   All prompt template attributes:")
    for attr in dir(template):
        if not attr.startswith("_") and attr != "messages":
            try:
                value = getattr(template, attr)
                if not callable(value):
                    print(f"     {attr}: {type(value)} = {str(value)[:100]}...")
            except:
                pass

    # 5. Check partial variables in detail
    print("\n5. PARTIAL VARIABLES DETAILED:")
    partials = template.partial_variables
    print(f"   Keys: {list(partials.keys())}")
    for key, value in partials.items():
        print(f"   {key}:")
        print(f"     Type: {type(value)}")
        print(f"     Value: {str(value)[:200]}...")

    # 6. Check if format instructions are elsewhere
    print("\n6. SEARCHING FOR FORMAT INSTRUCTIONS:")
    # Check in messages
    if hasattr(template, "messages"):
        print(f"   Template messages: {len(template.messages)}")
        for i, msg in enumerate(template.messages):
            print(f"     Message {i}: {type(msg)}")
            if hasattr(msg, "prompt") and hasattr(msg.prompt, "template"):
                template_text = msg.prompt.template
                if "format" in template_text.lower() or "schema" in template_text.lower():
                    print(f"       Contains format/schema text: {template_text[:100]}...")

    # 7. Test the _should_setup_format_instructions method
    print("\n7. SHOULD SETUP FORMAT INSTRUCTIONS TEST:")
    if hasattr(config, "_should_setup_format_instructions"):
        should_setup = config._should_setup_format_instructions()
        print(f"   _should_setup_format_instructions(): {should_setup}")

        # If it should but doesn't, investigate why
        if should_setup and "format_instructions" not in partials:
            print("   ❌ Should setup but format_instructions not in partials!")

            # Check individual conditions
            print("   Checking individual conditions:")
            print(f"     include_format_instructions: {config.include_format_instructions}")
            print(f"     structured_output_model exists: {config.structured_output_model is not None}")
            print(f"     use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")

    # 8. Try to manually call setup methods
    print("\n8. MANUAL SETUP ATTEMPTS:")
    try:
        # Try calling setup method directly
        print("   Calling _setup_format_instructions()...")
        config._setup_format_instructions()

        # Check if it worked
        new_partials = config.prompt_template.partial_variables
        if "format_instructions" in new_partials:
            print("   ✅ Manual setup worked! Format instructions now present")
        else:
            print("   ❌ Manual setup didn't add format_instructions")
            print(f"   New partials keys: {list(new_partials.keys())}")

    except Exception as e:
        print(f"   ❌ Manual setup failed: {e}")
        import traceback
        traceback.print_exc()

    # 9. Compare with v1 mode
    print("\n9. V1 VS V2 COMPARISON:")
    try:
        config_v1 = AugLLMConfig(
            structured_output_model=Plan[Task],
            structured_output_version="v1",
            temperature=0.1
        )

        v1_partials = config_v1.prompt_template.partial_variables
        v2_partials = config.prompt_template.partial_variables

        print(f"   V1 partials: {list(v1_partials.keys())}")
        print(f"   V2 partials: {list(v2_partials.keys())}")

        print(f"   V1 force_tool_use: {config_v1.force_tool_use}")
        print(f"   V2 force_tool_use: {config.force_tool_use}")

        print(f"   V1 use_tool_for_format_instructions: {config_v1.use_tool_for_format_instructions}")
        print(f"   V2 use_tool_for_format_instructions: {config.use_tool_for_format_instructions}")

    except Exception as e:
        print(f"   ❌ V1 comparison failed: {e}")

    # 10. Check runnable structure
    print("\n10. RUNNABLE STRUCTURE:")
    try:
        runnable = config.create_runnable()
        print(f"    Runnable type: {type(runnable)}")
        print(f"    Runnable steps: {len(runnable.steps) if hasattr(runnable, 'steps') else 'N/A'}")

        # Check if runnable has bound tools
        for i, step in enumerate(getattr(runnable, "steps", [])):
            print(f"    Step {i}: {type(step)}")
            if hasattr(step, "bound") or "bind" in str(type(step)).lower():
                print("      Has binding capabilities")

    except Exception as e:
        print(f"    ❌ Runnable analysis failed: {e}")

    return config

if __name__ == "__main__":
    config = investigate_aug_llm_config_internals()

    print("\n" + "=" * 80)
    print("CONCLUSIONS:")
    print("=" * 80)

    # Key findings
    partials = config.prompt_template.partial_variables
    has_format_instructions = "format_instructions" in partials
    has_internal_instructions = hasattr(config, "_format_instructions_text")

    print(f"1. Format instructions in partials: {'✅' if has_format_instructions else '❌'}")
    print(f"2. Internal format instructions exist: {'✅' if has_internal_instructions else '❌'}")
    print(f"3. Structured output version: {config.structured_output_version}")
    print(f"4. Force tool use: {'✅' if config.force_tool_use else '❌'}")
    print(f"5. Tool routes correct: {'✅' if config.tool_routes.get('plan_task_generic') == 'parse_output' else '❌'}")

    if has_internal_instructions and not has_format_instructions:
        print("\n🔍 KEY ISSUE: Format instructions exist internally but not in prompt template!")
        print("   This suggests v2 mode handles format instructions differently.")
        print("   Need to investigate how v2 mode works with tool calling.")
    elif has_format_instructions:
        print("\n✅ FORMAT INSTRUCTIONS WORKING: Found in prompt template.")
    else:
        print("\n❌ NO FORMAT INSTRUCTIONS: Neither internal nor in template!")
