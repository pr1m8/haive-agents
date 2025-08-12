#!/usr/bin/env python3
"""Debug what the LLM actually receives and why it's returning incorrect format."""


from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def debug_llm_prompt_and_tools():
    """Debug what exactly gets sent to the LLM."""
    print("🔍 DEBUGGING LLM PROMPT AND TOOLS")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )

    # Get the runnable
    runnable = config.create_runnable()

    # Create input
    input_data = {
        "messages": [
            {
                "role": "user",
                "content": "Create a plan to organize a birthday party with exactly 2 tasks. Make sure each task has a proper description field."
            }
        ]
    }

    print("1. Input to runnable:")
    print(f"   User message: {input_data['messages'][0]['content']}")

    # Instead of invoking, let's examine what gets prepared for the LLM
    try:
        # Get the prompt template (first step)
        prompt_template = runnable.steps[0]

        # Format the prompt
        formatted_messages = prompt_template.format_prompt(**input_data)
        print("\n2. Formatted messages to LLM:")
        for i, msg in enumerate(formatted_messages.messages):
            print(f"   Message {i} ({msg.type}): {msg.content}")

        # Get the LLM with tools (second step)
        llm_with_tools = runnable.steps[1]

        # Examine the tools bound to the LLM
        if hasattr(llm_with_tools, "kwargs") and "tools" in llm_with_tools.kwargs:
            tools = llm_with_tools.kwargs["tools"]
            print("\n3. Tools sent to LLM:")

            for i, tool in enumerate(tools):
                print(f"   Tool {i}:")
                print(f"     Name: {getattr(tool, 'name', 'Unknown')}")
                print(f"     Description: {getattr(tool, 'description', 'No description')}")

                # Get the schema that actually gets sent to the LLM
                if hasattr(tool, "get_input_schema"):
                    schema = tool.get_input_schema()
                    if hasattr(schema, "model_json_schema"):
                        json_schema = schema.model_json_schema()

                        print("     Schema properties:")
                        for prop_name, prop_def in json_schema.get("properties", {}).items():
                            print(f"       {prop_name}: {prop_def}")

                        # Check the steps array specifically
                        if "steps" in json_schema.get("properties", {}):
                            steps_def = json_schema["properties"]["steps"]
                            print(f"     Steps definition: {steps_def}")

                            if "items" in steps_def and "$ref" in steps_def["items"]:
                                ref = steps_def["items"]["$ref"]
                                print(f"     Steps items reference: {ref}")

                                # Check if the referenced definition exists
                                if "$defs" in json_schema:
                                    ref_name = ref.split("/")[-1]  # Get 'Task' from '#/$defs/Task'
                                    if ref_name in json_schema["$defs"]:
                                        ref_def = json_schema["$defs"][ref_name]
                                        print(f"     Referenced definition ({ref_name}): {ref_def}")
                                    else:
                                        print(f"     ❌ Referenced definition {ref_name} not found!")
                                else:
                                    print("     ❌ No $defs section in schema!")

            # Check tool_choice
            tool_choice = llm_with_tools.kwargs.get("tool_choice")
            print(f"\n4. Tool choice: {tool_choice}")

        print("\n5. Now executing to see LLM response...")
        result = runnable.invoke(input_data)

        print("6. LLM Response:")
        print(f"   Type: {type(result)}")
        if hasattr(result, "tool_calls") and result.tool_calls:
            tool_call = result.tool_calls[0]
            print(f"   Tool call name: {tool_call['name'] if isinstance(tool_call, dict) else tool_call.name}")
            print(f"   Tool call args: {tool_call['args'] if isinstance(tool_call, dict) else tool_call.args}")

            # Analyze the args structure
            args = tool_call["args"] if isinstance(tool_call, dict) else tool_call.args
            if "steps" in args:
                steps = args["steps"]
                print("   Steps returned by LLM:")
                for i, step in enumerate(steps):
                    print(f"     Step {i}: {step} (type: {type(step)})")
                    if isinstance(step, str):
                        print("       ❌ LLM returned string instead of object!")
                    elif isinstance(step, dict) and "description" in step:
                        print("       ✅ LLM returned proper object structure")

    except Exception as e:
        print(f"❌ Debug failed: {e}")
        import traceback
        traceback.print_exc()


def test_explicit_prompt_guidance():
    """Test with more explicit prompting to guide the LLM."""
    print("\n" + "=" * 60)
    print("🎯 TESTING EXPLICIT PROMPT GUIDANCE")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2",
        temperature=0.1
    )

    runnable = config.create_runnable()

    # More explicit input
    explicit_input = {
        "messages": [
            {
                "role": "user",
                "content": """Create a plan to organize a birthday party with exactly 2 tasks.

IMPORTANT: Each task in the steps array must be an object with a "description" field, like this:
{"description": "the task description"}

Do NOT return plain strings in the steps array. Each step must be a proper Task object."""
            }
        ]
    }

    print("1. Testing with explicit guidance...")
    result = runnable.invoke(explicit_input)

    if hasattr(result, "tool_calls") and result.tool_calls:
        tool_call = result.tool_calls[0]
        args = tool_call["args"] if isinstance(tool_call, dict) else tool_call.args

        print("2. Result with explicit guidance:")
        if "steps" in args:
            steps = args["steps"]
            for i, step in enumerate(steps):
                print(f"   Step {i}: {step} (type: {type(step)})")
                if isinstance(step, dict) and "description" in step:
                    print("     ✅ Proper structure!")
                else:
                    print("     ❌ Still incorrect structure!")

        return args
    print("2. ❌ No tool calls in result")
    return None


if __name__ == "__main__":
    debug_llm_prompt_and_tools()
    explicit_result = test_explicit_prompt_guidance()

    print("\n" + "=" * 60)
    print("🏁 DIAGNOSIS")
    print("=" * 60)

    if explicit_result and "steps" in explicit_result:
        steps = explicit_result["steps"]
        if all(isinstance(step, dict) and "description" in step for step in steps):
            print("✅ SOLUTION: Explicit prompting fixes the issue!")
            print("🔍 ROOT CAUSE: LLM needs clearer guidance about nested object structure")
        else:
            print("❌ Even explicit prompting doesn't work - deeper issue")
    else:
        print("❓ Need more investigation")
