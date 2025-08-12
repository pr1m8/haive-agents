#!/usr/bin/env python3
"""Debug what the prompt template is actually invoking and how format instructions get added."""


from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def debug_prompt_template_invoke():
    """Debug what happens when we invoke the prompt template."""
    print("🔍 DEBUGGING PROMPT TEMPLATE INVOKE LOGIC")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )

    print("1. Config state:")
    print(f"   _format_instructions_text exists: {hasattr(config, '_format_instructions_text')}")
    print(f"   partial_variables: {list(config.prompt_template.partial_variables.keys())}")

    # Test input
    input_data = {
        "messages": [{
            "role": "user",
            "content": "Create a plan"
        }]
    }

    # Get the prompt template directly
    prompt_template = config.prompt_template
    print("\n2. Prompt template analysis:")
    print(f"   Type: {type(prompt_template)}")
    print(f"   Input variables: {prompt_template.input_variables}")
    print(f"   Partial variables: {list(prompt_template.partial_variables.keys())}")

    # Check the actual messages in the template
    if hasattr(prompt_template, "messages"):
        print(f"   Message templates count: {len(prompt_template.messages)}")
        for i, msg_template in enumerate(prompt_template.messages):
            print(f"   Message {i}: {type(msg_template)}")

            # Look for format_instructions in the template
            if hasattr(msg_template, "prompt"):
                if hasattr(msg_template.prompt, "template"):
                    template_text = msg_template.prompt.template
                    print(f"     Template text: {template_text}")
                    if "{format_instructions}" in template_text:
                        print("     ✅ Found {format_instructions} placeholder!")
                    else:
                        print("     ❌ No {format_instructions} placeholder")

    # Try to format the prompt
    print("\n3. Prompt formatting test:")
    try:
        # This should show us what actually gets sent
        formatted = prompt_template.format_prompt(**input_data)
        print(f"   Formatted messages count: {len(formatted.messages)}")

        for i, msg in enumerate(formatted.messages):
            print(f"   Message {i} ({msg.type}):")
            content = msg.content
            print(f"     Content: {content}")

            # Check if format_instructions somehow got resolved
            if "JSON schema" in content or "format" in content.lower():
                print("     ✅ Format instructions appear to be in content!")
            else:
                print("     ❌ No format instructions in content")

    except Exception as e:
        print(f"   ❌ Format failed: {e}")
        import traceback
        traceback.print_exc()

    # Check if there's a different mechanism
    print("\n4. Alternative format instructions mechanism:")

    # Look for partial method calls
    if hasattr(prompt_template, "partial"):
        print("   Prompt template has partial method")

        # Try to manually add format instructions
        if hasattr(config, "_format_instructions_text") and config._format_instructions_text:
            print("   Trying manual partial with format instructions...")
            try:
                partial_template = prompt_template.partial(format_instructions=config._format_instructions_text)
                print("   ✅ Manual partial succeeded")
                print(f"   New partial variables: {list(partial_template.partial_variables.keys())}")

                # Test formatting with the partial template
                formatted_with_instructions = partial_template.format_prompt(**input_data)
                for i, msg in enumerate(formatted_with_instructions.messages):
                    content = msg.content
                    if "JSON schema" in content:
                        print(f"     ✅ Message {i} now has format instructions!")
                        print(f"     Content preview: {content[:200]}...")
                    else:
                        print(f"     Message {i}: {content}")

            except Exception as e:
                print(f"   ❌ Manual partial failed: {e}")


def debug_structured_output_setup():
    """Debug how structured output should set up format instructions."""
    print("\n" + "=" * 60)
    print("🔧 DEBUGGING STRUCTURED OUTPUT SETUP")
    print("=" * 60)

    # Test both versions
    for version in ["v1", "v2"]:
        print(f"\n{version.upper()} Mode:")

        config = AugLLMConfig(
            structured_output_model=Plan[Task],
            structured_output_version=version
        )

        print(f"   Internal instructions: {bool(getattr(config, '_format_instructions_text', None))}")
        print(f"   Partial variables: {list(config.prompt_template.partial_variables.keys())}")
        print(f"   Force tool use: {config.force_tool_use}")
        print(f"   Include format instructions: {config.include_format_instructions}")

        # Check if format instructions should be in the prompt for this version
        if version == "v1":
            print("   V1 should rely on format instructions in prompt")
        else:
            print("   V2 should rely on tool schema, but may also use format instructions")

        # Test prompt formatting
        input_data = {"messages": [{"role": "user", "content": "Test"}]}
        try:
            formatted = config.prompt_template.format_prompt(**input_data)
            has_format_content = any("schema" in msg.content.lower() or "format" in msg.content.lower() for msg in formatted.messages)
            print(f"   Format content in prompt: {has_format_content}")
        except Exception as e:
            print(f"   Prompt format failed: {e}")


if __name__ == "__main__":
    debug_prompt_template_invoke()
    debug_structured_output_setup()

    print("\n" + "=" * 60)
    print("🎯 KEY FINDINGS TO LOOK FOR:")
    print("=" * 60)
    print("1. Does the prompt template have {format_instructions} placeholder?")
    print("2. Is there logic that should populate format_instructions automatically?")
    print("3. Are format instructions supposed to be in partial_variables or handled differently?")
    print("4. Is there a difference between v1 and v2 mode format instruction handling?")
