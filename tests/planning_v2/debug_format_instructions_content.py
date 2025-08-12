#!/usr/bin/env python3
"""Debug the actual format instructions content to see if it's telling the LLM the correct schema."""


from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def debug_format_instructions_content():
    """Debug the exact content of format instructions."""
    print("🔍 DEBUGGING FORMAT INSTRUCTIONS CONTENT")
    print("=" * 60)

    config = AugLLMConfig(
        structured_output_model=Plan[Task],
        structured_output_version="v2"
    )

    # Get the format instructions
    if hasattr(config, "_format_instructions_text") and config._format_instructions_text:
        instructions = config._format_instructions_text
        print("1. Format instructions found:")
        print(f"   Length: {len(instructions)} characters")

        print("\n2. FULL FORMAT INSTRUCTIONS:")
        print("-" * 40)
        print(instructions)
        print("-" * 40)

        # Look for specific schema elements
        print("\n3. SCHEMA ANALYSIS:")
        print(f"   Contains 'Task': {'Task' in instructions}")
        print(f"   Contains 'description': {'description' in instructions}")
        print(f"   Contains 'steps': {'steps' in instructions}")
        print(f"   Contains 'objective': {'objective' in instructions}")

        # Look for the actual JSON schema structure
        import json
        import re

        # Try to extract the JSON schema
        schema_match = re.search(r"```\s*(\{.*?\})\s*```", instructions, re.DOTALL)
        if schema_match:
            try:
                schema_json = schema_match.group(1)
                schema = json.loads(schema_json)
                print("\n4. EXTRACTED JSON SCHEMA:")
                print(json.dumps(schema, indent=2))

                # Check if steps schema is correct
                if "properties" in schema and "steps" in schema["properties"]:
                    steps_schema = schema["properties"]["steps"]
                    print("\n5. STEPS SCHEMA ANALYSIS:")
                    print(f"   Steps schema: {steps_schema}")

                    if "items" in steps_schema:
                        items_schema = steps_schema["items"]
                        print(f"   Items schema: {items_schema}")

                        if "$ref" in items_schema:
                            ref = items_schema["$ref"]
                            print(f"   References: {ref}")

                            # Check if the referenced Task schema exists
                            if "$defs" in schema and "Task" in schema["$defs"]:
                                task_schema = schema["$defs"]["Task"]
                                print(f"   Task schema: {json.dumps(task_schema, indent=2)}")
                            else:
                                print("   ❌ Task schema not found in $defs!")
                        else:
                            print("   ❌ Items schema doesn't reference Task!")
                    else:
                        print("   ❌ Steps schema missing items!")
                else:
                    print("   ❌ Steps not found in schema properties!")

            except json.JSONDecodeError as e:
                print(f"   ❌ Failed to parse schema JSON: {e}")
        else:
            print("   ❌ Could not extract JSON schema from instructions")

        # Try to find example usage
        if "example" in instructions.lower():
            print("\n6. CONTAINS EXAMPLES: Yes")
            # Extract examples
            example_matches = re.findall(r'\{[^}]*"foo"[^}]*\}', instructions)
            if example_matches:
                print(f"   Example structures found: {len(example_matches)}")
                for i, example in enumerate(example_matches):
                    print(f"   Example {i+1}: {example}")
        else:
            print("\n6. CONTAINS EXAMPLES: No")

    else:
        print("❌ No format instructions found!")


def test_correct_data_structure():
    """Test Plan[Task] with the correct data structure."""
    import json
    print("\n" + "=" * 60)
    print("✅ TESTING CORRECT DATA STRUCTURE")
    print("=" * 60)

    # Create the data structure the LLM should be producing
    correct_data = {
        "objective": "Organize a birthday party",
        "steps": [
            {"description": "Choose a theme for the party and decide on the decorations."},
            {"description": "Send out invitations to the guests."}
        ]
    }

    print("1. Correct data structure:")
    print(json.dumps(correct_data, indent=2))

    try:
        plan = Plan[Task](**correct_data)
        print("\n2. ✅ Successfully created Plan[Task]!")
        print(f"   Objective: {plan.objective}")
        print(f"   Steps count: {len(plan.steps)}")
        for i, step in enumerate(plan.steps):
            print(f"   Step {i+1}: {step.description}")

        return True

    except Exception as e:
        print(f"\n2. ❌ Failed to create Plan[Task]: {e}")
        return False


if __name__ == "__main__":
    debug_format_instructions_content()
    success = test_correct_data_structure()

    print("\n" + "=" * 60)
    print("🏁 CONCLUSION")
    print("=" * 60)

    if success:
        print("✅ Plan[Task] works with correct data structure")
        print("🔍 ISSUE: Format instructions may not be telling LLM about Task schema")
        print("💡 SOLUTION: Fix format instructions to include nested Task structure")
    else:
        print("❌ Plan[Task] has fundamental issues even with correct data")
