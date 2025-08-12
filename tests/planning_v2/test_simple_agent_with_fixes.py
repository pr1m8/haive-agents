#!/usr/bin/env python3
"""Test SimpleAgent with Plan[Task] after the format instructions fix."""


from pydantic import BaseModel, Field

from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class Task(BaseModel):
    """Task model for testing."""
    description: str = Field(description="Task description")


class Plan[T](BaseModel):
    """Plan model with generic type."""
    objective: str = Field(description="Plan objective")
    steps: list[T] = Field(description="Plan steps", max_length=2)


def test_simple_agent_execution():
    """Test SimpleAgent execution with Plan[Task] structured output."""
    print("🤖 TESTING SIMPLE AGENT WITH PLAN[TASK]")
    print("=" * 50)

    # Create agent with our problematic structured output
    agent = SimpleAgent(
        name="test_planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            structured_output_version="v2",
            temperature=0.1
        )
    )

    print("1. Agent created successfully")
    print(f"   Engine type: {type(agent.engine)}")
    print(f"   Structured output model: {agent.engine.structured_output_model}")
    print(f"   Tool routes: {agent.engine.tool_routes}")

    # Check internal format instructions
    has_internal = hasattr(agent.engine, "_format_instructions_text") and agent.engine._format_instructions_text
    print(f"   Internal format instructions: {'✅' if has_internal else '❌'}")

    try:
        print("\n2. Testing execution with debug=True...")
        result = agent.run(
            "Create a simple plan to organize a birthday party with exactly 2 tasks",
            debug=True
        )

        print("\n3. EXECUTION RESULTS:")
        print("   ✅ Execution completed successfully!")
        print(f"   Result type: {type(result)}")
        print(f"   Result: {str(result)[:300]}...")

        # Try to parse as our expected model
        if isinstance(result, Plan):
            print("   ✅ Result is Plan[Task] instance!")
            print(f"   Objective: {result.objective}")
            print(f"   Steps count: {len(result.steps)}")
            for i, step in enumerate(result.steps):
                print(f"   Step {i+1}: {step.description}")
        else:
            print(f"   ⚠️  Result is not Plan[Task], got: {type(result)}")

        return True

    except Exception as e:
        print(f"\n❌ EXECUTION FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_with_recursion_limit():
    """Test SimpleAgent with recursion limit to check for our original issue."""
    print("\n" + "=" * 50)
    print("🔄 TESTING WITH RECURSION LIMIT (ORIGINAL ISSUE)")
    print("=" * 50)

    from langchain_core.runnables.config import RunnableConfig

    agent = SimpleAgent(
        name="limited_planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            structured_output_version="v2"
        )
    )

    try:
        print("1. Testing with recursion_limit=5...")
        config = RunnableConfig(recursion_limit=5)

        result = agent.invoke(
            {"messages": [{"role": "user", "content": "Create a simple plan with 2 steps"}]},
            config=config
        )

        print("   ✅ No recursion error!")
        print(f"   Result type: {type(result)}")
        return True

    except RecursionError:
        print("   ❌ Still getting RecursionError - validation routing issue persists")
        return False
    except Exception as e:
        print(f"   ⚠️  Different error: {e}")
        return False


if __name__ == "__main__":
    success1 = test_simple_agent_execution()
    success2 = test_with_recursion_limit()

    print("\n" + "=" * 50)
    print("🏁 RESULTS")
    print("=" * 50)
    print(f"SimpleAgent execution: {'✅' if success1 else '❌'}")
    print(f"Recursion limit test: {'✅' if success2 else '❌'}")

    if success1 and success2:
        print("\n🎉 SUCCESS: All fixes working! Original validation routing issue resolved!")
    elif success1:
        print("\n🔧 PARTIAL: Agent works but may still have recursion issues")
    else:
        print("\n❌ FAILED: Issues still persist")
