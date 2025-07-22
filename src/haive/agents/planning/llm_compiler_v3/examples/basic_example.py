"""Basic example of LLM Compiler V3 Agent usage.

This example demonstrates the core functionality of the LLM Compiler V3 Agent
with simple tools and a straightforward query.
"""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.planning.llm_compiler_v3 import LLMCompilerV3Agent


# Define some basic tools for the example
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression.replace("^", "**"))  # Handle exponents
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and return basic statistics."""
    words = text.split()
    chars = len(text)
    sentences = text.count(".") + text.count("!") + text.count("?")

    return (
        f"Text Analysis: {len(words)} words, {chars} characters, {sentences} sentences"
    )


@tool
def word_reverser(text: str) -> str:
    """Reverse the order of words in text."""
    return " ".join(text.split()[::-1])


async def basic_llm_compiler_example():
    """Basic example demonstrating LLM Compiler V3 functionality."""
    print("🚀 LLM Compiler V3 Basic Example")
    print("=" * 50)

    # Create tools
    tools = [calculator, text_analyzer, word_reverser]

    # Create agent with default configuration
    agent = LLMCompilerV3Agent(name="basic_compiler", tools=tools)

    # Example query that can benefit from parallelization
    query = """
    Please help me with these tasks:
    1. Calculate the result of (15 + 27) * 3
    2. Analyze this text: "The quick brown fox jumps over the lazy dog"
    3. Reverse the words in: "Hello world from LLM Compiler"
    
    Provide a summary of all results.
    """

    print(f"Query: {query}")
    print()

    # Execute the query
    print("🔄 Executing query with parallel task coordination...")
    start_time = asyncio.get_event_loop().time()

    try:
        result = await agent.arun(query)

        end_time = asyncio.get_event_loop().time()
        execution_time = end_time - start_time

        # Display results
        print("✅ Execution completed!")
        print(f"⏱️  Total execution time: {execution_time:.2f}s")
        print(f"📊 Agent execution time: {result.total_execution_time:.2f}s")
        print()

        print("📋 Execution Summary:")
        print(f"  • Tasks executed: {result.tasks_executed}")
        print(f"  • Success rate: {result.success_rate:.2%}")
        if result.parallel_efficiency:
            print(f"  • Parallel efficiency: {result.parallel_efficiency:.2%}")
        print()

        print("🎯 Final Answer:")
        print(result.final_answer)
        print()

        # Show detailed execution breakdown
        if result.execution_results:
            print("🔍 Task Execution Details:")
            for i, task_result in enumerate(result.execution_results, 1):
                status = "✅" if task_result.success else "❌"
                print(f"  {i}. {status} {task_result.task_id}")
                print(f"     Tool: {task_result.tool_name}")
                print(f"     Time: {task_result.execution_time:.3f}s")
                if task_result.error_message:
                    print(f"     Error: {task_result.error_message}")
                print()

        # Show reasoning trace
        if result.reasoning_trace:
            print("🧠 Reasoning Trace:")
            for i, step in enumerate(result.reasoning_trace, 1):
                print(f"  {i}. {step}")

        return result

    except Exception as e:
        print(f"❌ Execution failed: {e}")
        return None


async def parallel_efficiency_demo():
    """Demonstrate parallel execution efficiency."""
    print("🏃‍♂️ Parallel Execution Efficiency Demo")
    print("=" * 50)

    # Create agent
    agent = LLMCompilerV3Agent(
        name="efficiency_demo", tools=[calculator, text_analyzer, word_reverser]
    )

    # Query with multiple independent tasks
    parallel_query = """
    Perform these independent calculations and analyses:
    1. Calculate 123 + 456
    2. Calculate 789 * 12
    3. Analyze the text: "Parallel processing enables efficient task execution"
    4. Reverse the words: "Efficiency through parallelization"
    5. Calculate the square of 25
    """

    print(f"Query (5 independent tasks): {parallel_query}")
    print()

    # Execute and measure
    print("🔄 Executing with maximum parallelization...")
    result = await agent.arun(parallel_query)

    print("📊 Efficiency Analysis:")
    print(f"  • Total tasks: {result.tasks_executed}")
    print(f"  • Total time: {result.total_execution_time:.2f}s")
    print(
        f"  • Average per task: {result.total_execution_time / max(1, result.tasks_executed):.3f}s"
    )

    if result.parallel_efficiency:
        print(f"  • Parallel efficiency: {result.parallel_efficiency:.2%}")

    print()
    print("🎯 Results:")
    print(result.final_answer)

    return result


async def error_handling_demo():
    """Demonstrate error handling and replanning."""
    print("🛠️ Error Handling and Replanning Demo")
    print("=" * 50)

    # Tool that will fail
    @tool
    def failing_tool(input_text: str) -> str:
        """A tool that always fails."""
        raise Exception("This tool always fails for demonstration")

    # Create agent with failing tool
    agent = LLMCompilerV3Agent(
        name="error_demo", tools=[calculator, failing_tool, text_analyzer]
    )

    # Query that will trigger the failing tool
    error_query = """
    Please:
    1. Calculate 10 + 20
    2. Use the failing tool on "test input" 
    3. Analyze this text: "Error handling is important"
    
    Provide results even if some tasks fail.
    """

    print(f"Query (includes failing tool): {error_query}")
    print()

    print("🔄 Executing with intentional failure...")
    result = await agent.arun(error_query)

    print("📊 Error Handling Results:")
    print(f"  • Success rate: {result.success_rate:.2%}")
    print(f"  • Failed tasks: {len(result.get_failed_tasks())}")
    print(f"  • Successful tasks: {len(result.get_successful_tasks())}")
    print()

    # Show failed tasks
    failed_tasks = result.get_failed_tasks()
    if failed_tasks:
        print("❌ Failed Tasks:")
        for failed in failed_tasks:
            print(f"  • {failed.task_id}: {failed.error_message}")
        print()

    print("🎯 Final Answer (despite failures):")
    print(result.final_answer)

    return result


def main():
    """Run all examples."""
    print("🎯 LLM Compiler V3 Examples")
    print("=" * 60)
    print()

    # Run examples
    asyncio.run(basic_llm_compiler_example())
    print()
    print("=" * 60)
    print()

    asyncio.run(parallel_efficiency_demo())
    print()
    print("=" * 60)
    print()

    asyncio.run(error_handling_demo())

    print()
    print("✨ All examples completed!")


if __name__ == "__main__":
    main()
