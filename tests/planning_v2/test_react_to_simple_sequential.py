#!/usr/bin/env python3
"""Test ReactAgent piping to SimpleAgent with structured output in sequential pattern."""

import asyncio

from langchain_core.tools import tool
from pydantic import BaseModel, Field

# Import base Agent first to ensure it's defined
from haive.agents.base import Agent
from haive.agents.multi import MultiAgent
from haive.agents.react import ReactAgent
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Ensure models are rebuilt
Agent.model_rebuild()
SimpleAgent.model_rebuild()
ReactAgent.model_rebuild()


# Define a simple structured output model for testing
class TaskResult(BaseModel):
    """Structured result from task execution."""
    task_description: str = Field(description="What was done")
    success: bool = Field(description="Whether task succeeded")
    output: str = Field(description="The actual output/result")
    tool_calls_made: int = Field(default=0, description="Number of tool calls")


# Create a simple calculator tool for ReactAgent
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression.
    
    Args:
        expression: Mathematical expression to evaluate
        
    Returns:
        Result of the calculation
    """
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e!s}"


@tool
def word_counter(text: str) -> str:
    """Count words in text.
    
    Args:
        text: Text to count words in
        
    Returns:
        Number of words
    """
    words = len(text.split())
    return f"The text contains {words} words"


async def test_react_to_simple_sequential():
    """Test ReactAgent doing work then SimpleAgent formatting output."""
    print("🧪 TESTING REACT → SIMPLE SEQUENTIAL PATTERN")
    print("=" * 60)

    # 1. Create ReactAgent with tools
    react_config = AugLLMConfig(
        temperature=0.3,
        system_message="You are a helpful assistant that uses tools to solve problems."
    )

    react_agent = ReactAgent(
        name="tool_executor",
        engine=react_config,
        tools=[calculator, word_counter],
        max_iterations=3  # Limit iterations
    )

    print("✅ ReactAgent created with calculator and word_counter tools")

    # 2. Create SimpleAgent with structured output
    simple_config = AugLLMConfig(
        temperature=0.1,
        structured_output_model=TaskResult,
        system_message="You format task execution results into structured output."
    )

    simple_agent = SimpleAgent(
        name="result_formatter",
        engine=simple_config
    )

    print("✅ SimpleAgent created with TaskResult structured output")

    # 3. Create sequential multi-agent using MultiAgent
    sequential_agent = MultiAgent(
        name="react_simple_sequential",
        agents=[react_agent, simple_agent],
        execution_mode="sequential"
    )

    print("✅ Sequential multi-agent created: ReactAgent → SimpleAgent")
    print(f"   MultiAgent type: {type(sequential_agent).__name__}")
    print(f"   Execution mode: {sequential_agent.execution_mode}")

    # 4. Test execution
    test_input = {
        "messages": [{
            "role": "user",
            "content": "Please calculate 25 * 4 and then count the words in 'The quick brown fox jumps over the lazy dog'"
        }]
    }

    print("\n📤 Sending request to sequential agent...")
    print(f"   Input: {test_input['messages'][0]['content']}")

    try:
        # Run with debug to see execution flow
        result = await sequential_agent.arun(test_input, debug=True)

        print("\n✅ Sequential execution completed!")
        print("\n📊 Result Analysis:")

        # Check if we got structured output
        if hasattr(result, "content"):
            print(f"   Raw content: {result.content[:200]}...")

        # The SimpleAgent should have formatted the ReactAgent's output
        # into our TaskResult structure
        if hasattr(result, "tool_calls") and result.tool_calls:
            tool_call = result.tool_calls[0]
            args = tool_call.get("args", {}) if isinstance(tool_call, dict) else tool_call.args

            print("\n📋 Structured Output:")
            print(f"   Task: {args.get('task_description', 'N/A')}")
            print(f"   Success: {args.get('success', 'N/A')}")
            print(f"   Output: {args.get('output', 'N/A')}")
            print(f"   Tool calls: {args.get('tool_calls_made', 'N/A')}")

            return True
        print("   ⚠️ No structured output found in result")
        print(f"   Result type: {type(result)}")
        print(f"   Result: {result}")
        return False

    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_with_complex_task():
    """Test with a more complex task requiring multiple tool calls."""
    print("\n\n🧪 TESTING WITH COMPLEX TASK")
    print("=" * 60)

    # Create agents
    react_agent = ReactAgent(
        name="worker",
        engine=AugLLMConfig(temperature=0.3),
        tools=[calculator, word_counter],
        max_iterations=5
    )

    simple_agent = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            temperature=0.1,
            structured_output_model=TaskResult
        )
    )

    multi_agent = MultiAgent(
        name="complex_workflow",
        agents=[react_agent, simple_agent],
        execution_mode="sequential"
    )

    # Complex task
    complex_input = {
        "messages": [{
            "role": "user",
            "content": "First calculate (15 * 8) + (12 * 3), then count words in the result description"
        }]
    }

    print(f"📤 Complex task: {complex_input['messages'][0]['content']}")

    try:
        result = await multi_agent.arun(complex_input)
        print("✅ Complex task completed!")
        return True
    except Exception as e:
        print(f"❌ Complex task failed: {e}")
        return False


async def main():
    """Run all tests."""
    print("📚 Overview of Components:")
    print("=" * 60)
    print("1. ReactAgent: Agent with tool-calling capabilities")
    print("   - Executes its own reasoning loop")
    print("   - Calls tools (calculator, word_counter)")
    print("   - Returns raw execution results")
    print("\n2. SimpleAgent: Agent with structured output")
    print("   - Takes ReactAgent's output as input")
    print("   - Formats into TaskResult model")
    print("   - Returns structured data")
    print("\n3. MultiAgent: Sequential orchestration")
    print("   - Manages agent execution order")
    print("   - Passes state between agents")
    print("   - Returns final structured output")
    print("\n" + "=" * 60 + "\n")

    # Test 1: Basic sequential pattern
    success1 = await test_react_to_simple_sequential()

    # Test 2: Complex task
    success2 = await test_with_complex_task()

    print("\n" + "=" * 60)
    print("🏁 TEST SUMMARY")
    print("=" * 60)
    print(f"Basic sequential test: {'✅ PASS' if success1 else '❌ FAIL'}")
    print(f"Complex task test: {'✅ PASS' if success2 else '❌ FAIL'}")

    if success1 and success2:
        print("\n✅ All tests passed!")
        print("\n📝 Key Findings:")
        print("  1. ReactAgent successfully executes with its own tools")
        print("  2. SimpleAgent formats ReactAgent output into structured model")
        print("  3. Sequential pattern works: React (work) → Simple (format)")
        print("  4. This pattern is suitable for executor → formatter flow")
        print("\n🎯 Next Steps:")
        print("  - Implement executor with Tavily search tool")
        print("  - Add post-hook for status updates")
        print("  - Create replanner with Response[Union[Answer, Plan[Task]]]")
    else:
        print("\n❌ Some tests failed - need investigation")


if __name__ == "__main__":
    asyncio.run(main())
